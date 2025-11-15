-- Intelligence Extraction Quality Dashboard Database Schema
-- Deploy this in Supabase SQL Editor

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Extractions table (main data)
CREATE TABLE IF NOT EXISTS extractions (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  extraction_id TEXT UNIQUE NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

  -- Source info
  source_file_name TEXT,
  source_file_url TEXT,
  meeting_type TEXT,

  -- Template info
  template_name TEXT,
  template_version TEXT,

  -- Extraction results
  entities_created INTEGER DEFAULT 0,
  entities_updated INTEGER DEFAULT 0,
  items_extracted INTEGER DEFAULT 0,

  -- Quality metrics
  completeness_score INTEGER,
  completeness_required INTEGER,
  completeness_optional INTEGER,
  confidence_level TEXT, -- 'high', 'medium', 'low'
  confidence_high_count INTEGER DEFAULT 0,
  confidence_medium_count INTEGER DEFAULT 0,
  confidence_low_count INTEGER DEFAULT 0,

  -- Quality indicators
  parsing_valid BOOLEAN DEFAULT true,
  parsing_errors TEXT[],
  issues_count INTEGER DEFAULT 0,
  issues_list TEXT[],
  warnings_count INTEGER DEFAULT 0,
  warnings_list TEXT[],

  -- Ratings and review
  auto_quality_rating TEXT, -- 'excellent', 'good', 'fair', 'poor'
  user_quality_rating TEXT,
  flagged_for_review BOOLEAN DEFAULT false,
  reviewed BOOLEAN DEFAULT false,
  reviewed_at TIMESTAMP WITH TIME ZONE,
  reviewed_by TEXT,

  -- Edit tracking
  edit_count INTEGER DEFAULT 0,
  human_edit_required BOOLEAN DEFAULT false,

  -- Processing
  processing_time_seconds DECIMAL,

  -- Experiment tracking
  experiment_id UUID,
  experiment_variant TEXT, -- 'A' or 'B'

  -- Full data (JSONB for flexibility)
  extraction_summary TEXT,
  completeness_details JSONB,
  entity_links JSONB,
  intelligence_data JSONB
);

-- Experiments table
CREATE TABLE IF NOT EXISTS experiments (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

  name TEXT NOT NULL,
  template_name TEXT NOT NULL,
  hypothesis TEXT,

  -- Version details
  version_a_description TEXT,
  version_b_changes TEXT,

  -- Metrics
  success_metric TEXT,
  secondary_metrics TEXT[],

  -- Status
  status TEXT DEFAULT 'running', -- 'running', 'completed', 'cancelled'
  started_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  ended_at TIMESTAMP WITH TIME ZONE,

  -- Results
  sample_size_target INTEGER DEFAULT 20,
  sample_size_actual INTEGER DEFAULT 0,
  winner TEXT, -- 'A', 'B', or 'no_difference'
  results JSONB
);

-- Edits table (tracks all manual edits)
CREATE TABLE IF NOT EXISTS edits (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

  extraction_id UUID REFERENCES extractions(id),

  -- What was edited
  entity_type TEXT, -- 'partnership', 'funding', 'stakeholder'
  entity_id TEXT, -- Asana task ID
  entity_name TEXT,

  -- Edit details
  field_name TEXT,
  old_value TEXT,
  new_value TEXT,
  edit_type TEXT, -- 'name', 'description', 'custom_field', 'delete'

  edited_by TEXT,

  -- Context
  asana_task_url TEXT
);

-- Weekly analyses table
CREATE TABLE IF NOT EXISTS weekly_analyses (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

  week_start DATE NOT NULL,
  week_end DATE NOT NULL,

  -- Aggregate metrics
  total_extractions INTEGER,
  avg_completeness DECIMAL,
  avg_user_rating DECIMAL,
  avg_edit_count DECIMAL,
  review_rate DECIMAL,

  -- Claude analysis
  executive_summary TEXT,
  key_insights TEXT[],
  priority_improvements JSONB,
  experiments_proposed JSONB,
  positive_trends TEXT[],

  -- Raw data for reference
  metrics JSONB,
  problem_patterns JSONB,

  -- Follow-up
  asana_task_id TEXT,
  asana_task_url TEXT
);

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_extractions_created_at ON extractions(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_extractions_meeting_type ON extractions(meeting_type);
CREATE INDEX IF NOT EXISTS idx_extractions_template ON extractions(template_name, template_version);
CREATE INDEX IF NOT EXISTS idx_extractions_quality ON extractions(auto_quality_rating, user_quality_rating);
CREATE INDEX IF NOT EXISTS idx_edits_extraction ON edits(extraction_id);
CREATE INDEX IF NOT EXISTS idx_weekly_analyses_dates ON weekly_analyses(week_start, week_end);

-- ===== DATABASE FUNCTIONS =====

-- Get dashboard metrics
CREATE OR REPLACE FUNCTION get_dashboard_metrics()
RETURNS JSON AS $$
DECLARE
  result JSON;
BEGIN
  SELECT json_build_object(
    'total_extractions_7d', (
      SELECT COUNT(*) FROM extractions
      WHERE created_at >= NOW() - INTERVAL '7 days'
    ),
    'total_extractions_30d', (
      SELECT COUNT(*) FROM extractions
      WHERE created_at >= NOW() - INTERVAL '30 days'
    ),
    'avg_completeness_7d', (
      SELECT ROUND(AVG(completeness_score), 1) FROM extractions
      WHERE created_at >= NOW() - INTERVAL '7 days'
    ),
    'avg_user_rating_7d', (
      SELECT ROUND(AVG(
        CASE user_quality_rating
          WHEN 'excellent' THEN 5
          WHEN 'good' THEN 4
          WHEN 'fair' THEN 3
          WHEN 'poor' THEN 2
          WHEN 'failed' THEN 1
          ELSE NULL
        END
      ), 2)
      FROM extractions
      WHERE created_at >= NOW() - INTERVAL '7 days'
      AND user_quality_rating IS NOT NULL
    ),
    'flagged_rate_7d', (
      SELECT ROUND(
        (COUNT(*) FILTER (WHERE flagged_for_review = true) * 100.0) / NULLIF(COUNT(*), 0),
        1
      )
      FROM extractions
      WHERE created_at >= NOW() - INTERVAL '7 days'
    ),
    'trend_extractions', (
      SELECT ROUND(
        (COUNT(*) FILTER (WHERE created_at >= NOW() - INTERVAL '7 days') -
         COUNT(*) FILTER (WHERE created_at >= NOW() - INTERVAL '14 days' AND created_at < NOW() - INTERVAL '7 days')) * 100.0 /
        NULLIF(COUNT(*) FILTER (WHERE created_at >= NOW() - INTERVAL '14 days' AND created_at < NOW() - INTERVAL '7 days'), 0),
        1
      )
      FROM extractions
    ),
    'trend_completeness', (
      SELECT ROUND(
        AVG(completeness_score) FILTER (WHERE created_at >= NOW() - INTERVAL '7 days') -
        AVG(completeness_score) FILTER (WHERE created_at >= NOW() - INTERVAL '14 days' AND created_at < NOW() - INTERVAL '7 days'),
        1
      )
      FROM extractions
    ),
    'trend_rating', (
      SELECT ROUND(
        (AVG(CASE user_quality_rating WHEN 'excellent' THEN 5 WHEN 'good' THEN 4 WHEN 'fair' THEN 3 WHEN 'poor' THEN 2 WHEN 'failed' THEN 1 END)
         FILTER (WHERE created_at >= NOW() - INTERVAL '7 days' AND user_quality_rating IS NOT NULL) -
         AVG(CASE user_quality_rating WHEN 'excellent' THEN 5 WHEN 'good' THEN 4 WHEN 'fair' THEN 3 WHEN 'poor' THEN 2 WHEN 'failed' THEN 1 END)
         FILTER (WHERE created_at >= NOW() - INTERVAL '14 days' AND created_at < NOW() - INTERVAL '7 days' AND user_quality_rating IS NOT NULL)) * 100 /
        NULLIF(AVG(CASE user_quality_rating WHEN 'excellent' THEN 5 WHEN 'good' THEN 4 WHEN 'fair' THEN 3 WHEN 'poor' THEN 2 WHEN 'failed' THEN 1 END)
         FILTER (WHERE created_at >= NOW() - INTERVAL '14 days' AND created_at < NOW() - INTERVAL '7 days' AND user_quality_rating IS NOT NULL), 0),
        1
      )
      FROM extractions
    )
  ) INTO result;

  RETURN result;
END;
$$ LANGUAGE plpgsql;

-- Get quality trend for last 30 days
CREATE OR REPLACE FUNCTION get_quality_trend_30d()
RETURNS TABLE(
  date DATE,
  completeness NUMERIC,
  user_rating NUMERIC,
  extractions INTEGER
) AS $$
BEGIN
  RETURN QUERY
  SELECT
    DATE(e.created_at) as date,
    ROUND(AVG(e.completeness_score), 1) as completeness,
    ROUND(AVG(
      CASE e.user_quality_rating
        WHEN 'excellent' THEN 5
        WHEN 'good' THEN 4
        WHEN 'fair' THEN 3
        WHEN 'poor' THEN 2
        WHEN 'failed' THEN 1
        ELSE NULL
      END
    ), 2) as user_rating,
    COUNT(*)::INTEGER as extractions
  FROM extractions e
  WHERE e.created_at >= NOW() - INTERVAL '30 days'
  GROUP BY DATE(e.created_at)
  ORDER BY DATE(e.created_at);
END;
$$ LANGUAGE plpgsql;

-- Get template performance
CREATE OR REPLACE FUNCTION get_template_performance()
RETURNS TABLE(
  template_name TEXT,
  extraction_count BIGINT,
  avg_completeness NUMERIC,
  avg_user_rating NUMERIC,
  avg_edit_count NUMERIC,
  flagged_rate NUMERIC,
  performance_grade TEXT
) AS $$
BEGIN
  RETURN QUERY
  SELECT
    e.template_name,
    COUNT(*) as extraction_count,
    ROUND(AVG(e.completeness_score), 1) as avg_completeness,
    ROUND(AVG(
      CASE e.user_quality_rating
        WHEN 'excellent' THEN 5
        WHEN 'good' THEN 4
        WHEN 'fair' THEN 3
        WHEN 'poor' THEN 2
        WHEN 'failed' THEN 1
        ELSE NULL
      END
    ), 2) as avg_user_rating,
    ROUND(AVG(e.edit_count), 1) as avg_edit_count,
    ROUND((COUNT(*) FILTER (WHERE e.flagged_for_review = true) * 100.0) / COUNT(*), 1) as flagged_rate,
    CASE
      WHEN AVG(e.completeness_score) >= 85 AND AVG(e.edit_count) < 2 THEN 'excellent'
      WHEN AVG(e.completeness_score) >= 75 AND AVG(e.edit_count) < 3 THEN 'good'
      WHEN AVG(e.completeness_score) >= 65 THEN 'needs_work'
      ELSE 'poor'
    END as performance_grade
  FROM extractions e
  WHERE e.created_at >= NOW() - INTERVAL '30 days'
  AND e.template_name IS NOT NULL
  GROUP BY e.template_name
  ORDER BY avg_completeness DESC;
END;
$$ LANGUAGE plpgsql;

-- Enable Row Level Security (RLS)
ALTER TABLE extractions ENABLE ROW LEVEL SECURITY;
ALTER TABLE experiments ENABLE ROW LEVEL SECURITY;
ALTER TABLE edits ENABLE ROW LEVEL SECURITY;
ALTER TABLE weekly_analyses ENABLE ROW LEVEL SECURITY;

-- Create policies (allow all operations for now - can restrict later)
CREATE POLICY "Allow all operations on extractions" ON extractions FOR ALL USING (true);
CREATE POLICY "Allow all operations on experiments" ON experiments FOR ALL USING (true);
CREATE POLICY "Allow all operations on edits" ON edits FOR ALL USING (true);
CREATE POLICY "Allow all operations on weekly_analyses" ON weekly_analyses FOR ALL USING (true);

-- Enable real-time
ALTER PUBLICATION supabase_realtime ADD TABLE extractions;
ALTER PUBLICATION supabase_realtime ADD TABLE experiments;
