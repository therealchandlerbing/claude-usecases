-- ============================================================
-- RELATIONSHIP INTELLIGENCE SCHEMA - COMBINED
-- Version: 1.0.0 (Fixed for Supabase compatibility)
--
-- This file combines:
--   1. Core schema (relationships, interactions, commitments, signals)
--   2. Extended intelligence schema (personas, services, battle cards)
--
-- FIX APPLIED: Removed CURRENT_DATE from partial index predicate
-- (PostgreSQL requires IMMUTABLE functions in index predicates)
--
-- Deploy: Paste entire file into Supabase SQL Editor and run
-- ============================================================

-- Enable extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ============================================================
-- PART 1: CORE TABLES
-- ============================================================

-- ------------------------------------------------------------
-- RELATIONSHIPS (People + Organizations)
-- Primary unit is person, organization is attribute
-- ------------------------------------------------------------
CREATE TABLE relationships (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

  -- Identity
  name TEXT NOT NULL,
  email TEXT,
  organization TEXT,
  title TEXT,
  linkedin_url TEXT,

  -- Classification (multi-select via array)
  relationship_types TEXT[] DEFAULT '{}',
    -- Values: 'client', 'partner', 'funder', 'advisor', 'prospect',
    --         'referral_source', 'vendor', 'team_member', 'board_member'

  -- Geography (maps to your Asana Geography field)
  geography TEXT,
    -- Values: 'brazil', 'north_america', 'europe', 'latin_america',
    --         'asia_pacific', 'global'
  geography_detail TEXT,
    -- Values: 'sao_paulo', 'rio_de_janeiro', 'campinas',
    --         'rio_grande_do_sul', etc.

  -- Cultural context for engagement approach
  cultural_context TEXT,
    -- Values: 'government', 'academic', 'corporate', 'startup',
    --         'foundation', 'ngo', 'individual'

  -- Origin & Network
  source TEXT,
    -- Values: 'conference', 'warm_intro', 'cold_outreach', 'inbound',
    --         'institutional', 'existing_network', 'client_referral'
  introducer_id UUID REFERENCES relationships(id),
  first_contact_date DATE,
  how_we_met TEXT,

  -- Current Status (maps to your Asana Partnership Stage field)
  stage TEXT DEFAULT 'research',
    -- Values: 'research', 'initial_outreach', 'discovery', 'proposal',
    --         'negotiation', 'active', 'renewal', 'closed_won',
    --         'closed_lost', 'dormant'
  stage_changed_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

  -- Temperature (auto-calculated based on last_interaction_date)
  temperature TEXT DEFAULT 'warm',
    -- Values: 'hot', 'warm', 'cool', 'cold'
  temperature_updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

  -- Strategic assessment
  strategic_fit_score INTEGER CHECK (strategic_fit_score >= 1 AND strategic_fit_score <= 10),

  -- Activity metrics (auto-updated by triggers)
  last_interaction_date DATE,
  last_interaction_id UUID,
  interaction_count INTEGER DEFAULT 0,
  days_since_contact INTEGER,

  -- Financial (maps to your Asana Deal Value field)
  deal_value DECIMAL,
  deal_currency TEXT DEFAULT 'USD',

  -- Notes
  notes TEXT,
  cultural_notes TEXT,

  -- Asana sync (populated when you push)
  asana_task_gid TEXT UNIQUE,
  asana_project_gid TEXT,
  asana_last_sync TIMESTAMP WITH TIME ZONE,

  -- Push control
  push_status TEXT DEFAULT 'pending_review',
    -- Values: 'pending_review', 'pushed', 'supabase_only', 'declined'
  push_decided_at TIMESTAMP WITH TIME ZONE,

  -- Soft delete
  is_active BOOLEAN DEFAULT true,
  archived_at TIMESTAMP WITH TIME ZONE,
  archive_reason TEXT
);

COMMENT ON TABLE relationships IS 'Core relationship records. Primary unit is person with organization as attribute.';
COMMENT ON COLUMN relationships.push_status IS 'Controls whether this record has been pushed to Asana. pending_review = awaiting decision, pushed = synced to Asana, supabase_only = keep in intelligence layer only, declined = explicitly excluded';

-- ------------------------------------------------------------
-- INTERACTIONS (Meeting History)
-- Every meeting/touchpoint logged from transcripts
-- ------------------------------------------------------------
CREATE TABLE interactions (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

  -- When and who
  interaction_date DATE NOT NULL,
  relationship_id UUID NOT NULL REFERENCES relationships(id) ON DELETE CASCADE,

  -- Meeting details
  meeting_type TEXT,
    -- Values: 'exploratory', 'negotiation', 'check_in', 'delivery',
    --         'strategy', 'introduction', 'internal', 'presentation'
  meeting_format TEXT,
    -- Values: 'video', 'phone', 'in_person', 'email_thread', 'async'
  duration_minutes INTEGER,
  initiated_by TEXT,
    -- Values: 'us', 'them'

  -- Participants
  participants JSONB DEFAULT '[]',
    -- Format: [{"name": "...", "role": "...", "relationship_id": "..."}]
  our_attendees TEXT[],

  -- Outcome assessment
  outcome TEXT,
    -- Values: 'advanced', 'maintained', 'stalled', 'closed', 'unclear'
  temperature_change TEXT,
    -- Values: 'warmed', 'cooled', 'stable'
  stage_change_to TEXT,

  -- Content
  topics TEXT[],
  summary TEXT,
  key_quotes TEXT[],

  -- Source tracking
  transcript_url TEXT,
  transcript_file_name TEXT,
  calendar_event_id TEXT,

  -- Processing status
  processed_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  needs_review BOOLEAN DEFAULT false,
  reviewed BOOLEAN DEFAULT false,
  reviewed_at TIMESTAMP WITH TIME ZONE,
  review_notes TEXT
);

COMMENT ON TABLE interactions IS 'Meeting and touchpoint records extracted from transcripts.';

-- ------------------------------------------------------------
-- COMMITMENTS (Two-way Promise Tracking)
-- What we promised, what they promised
-- ------------------------------------------------------------
CREATE TABLE commitments (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

  -- Context
  interaction_id UUID REFERENCES interactions(id) ON DELETE SET NULL,
  relationship_id UUID NOT NULL REFERENCES relationships(id) ON DELETE CASCADE,

  -- Commitment details
  owner TEXT NOT NULL,
    -- Values: 'us', 'them'
  description TEXT NOT NULL,
  commitment_type TEXT,
    -- Values: 'deliverable', 'meeting', 'introduction', 'information',
    --         'decision', 'follow_up', 'payment', 'contract'

  -- Timing
  due_date DATE,
  due_date_type TEXT,
    -- Values: 'explicit', 'implied', 'asap', 'no_deadline'

  -- Status
  status TEXT DEFAULT 'pending',
    -- Values: 'pending', 'completed', 'overdue', 'cancelled', 'blocked'
  completed_at TIMESTAMP WITH TIME ZONE,
  blocked_reason TEXT,

  -- Asana sync (for our commitments when pushed)
  asana_task_gid TEXT,
  asana_task_url TEXT,

  -- Push control
  push_status TEXT DEFAULT 'pending_review',
    -- Values: 'pending_review', 'pushed', 'supabase_only', 'declined'
  push_destination TEXT,
    -- Values: 'bd_followup', 'client_delivery', 'growth_hub', 'ops'
  push_decided_at TIMESTAMP WITH TIME ZONE,

  -- Follow-up tracking
  reminder_sent BOOLEAN DEFAULT false,
  follow_up_count INTEGER DEFAULT 0
);

COMMENT ON TABLE commitments IS 'Promises made in meetings. Tracks both our commitments and theirs.';
COMMENT ON COLUMN commitments.owner IS 'us = we committed to do something, them = they committed to do something';

-- ------------------------------------------------------------
-- SIGNALS (Strategic Intelligence)
-- Valuable information extracted from conversations
-- ------------------------------------------------------------
CREATE TABLE signals (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

  -- Context
  interaction_id UUID REFERENCES interactions(id) ON DELETE SET NULL,
  relationship_id UUID NOT NULL REFERENCES relationships(id) ON DELETE CASCADE,

  -- Signal details
  signal_type TEXT NOT NULL,
    -- Values: 'funding_interest', 'partnership_interest', 'client_interest',
    --         'introduction_offer', 'introduction_request', 'risk_concern',
    --         'competitive_intel', 'timeline_shift', 'decision_maker_identified',
    --         'budget_signal', 'priority_shift', 'organizational_change',
    --         'positive_sentiment', 'negative_sentiment', 'referral_opportunity'
  description TEXT NOT NULL,
  verbatim_quote TEXT,

  -- Assessment
  confidence TEXT DEFAULT 'medium',
    -- Values: 'high', 'medium', 'low'
  significance TEXT DEFAULT 'normal',
    -- Values: 'critical', 'high', 'normal', 'low'

  -- Type-specific details
  amount DECIMAL,
  amount_currency TEXT DEFAULT 'USD',
  timeline TEXT,
  person_mentioned TEXT,
  organization_mentioned TEXT,

  -- Action tracking
  actionable BOOLEAN DEFAULT false,
  action_required TEXT,
  action_taken TEXT,
  action_taken_at TIMESTAMP WITH TIME ZONE,

  -- Outcome tracking (for pattern analysis)
  outcome TEXT,
    -- Values: 'confirmed', 'partially_confirmed', 'not_realized', 'pending'
  outcome_notes TEXT,
  outcome_recorded_at TIMESTAMP WITH TIME ZONE,

  -- Push control (most signals stay in Supabase)
  push_status TEXT DEFAULT 'supabase_only',
    -- Values: 'pending_review', 'pushed', 'supabase_only'
  push_decided_at TIMESTAMP WITH TIME ZONE
);

COMMENT ON TABLE signals IS 'Strategic intelligence extracted from conversations. Funding signals, risks, opportunities, etc.';

-- ------------------------------------------------------------
-- INTRODUCTIONS (Network Flow)
-- Who introduced whom, tracking introduction ROI
-- ------------------------------------------------------------
CREATE TABLE introductions (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

  -- Direction
  direction TEXT NOT NULL,
    -- Values: 'inbound' (we received intro), 'outbound' (we made intro)

  -- Parties
  introducer_id UUID REFERENCES relationships(id) ON DELETE SET NULL,
  introduced_id UUID REFERENCES relationships(id) ON DELETE SET NULL,
  introduced_name TEXT,
  introduced_organization TEXT,

  -- Context
  interaction_id UUID REFERENCES interactions(id) ON DELETE SET NULL,
  context TEXT,

  -- Status progression
  status TEXT DEFAULT 'discussed',
    -- Values: 'discussed', 'requested', 'made', 'accepted', 'meeting_held',
    --         'converted', 'declined', 'no_response'
  requested_at TIMESTAMP WITH TIME ZONE,
  made_at TIMESTAMP WITH TIME ZONE,
  first_meeting_at TIMESTAMP WITH TIME ZONE,

  -- Outcome tracking
  outcome TEXT,
  outcome_relationship_id UUID REFERENCES relationships(id) ON DELETE SET NULL,
  value_generated DECIMAL,
  value_currency TEXT DEFAULT 'USD',

  -- Push control
  push_status TEXT DEFAULT 'supabase_only',
    -- Values: 'pending_review', 'pushed', 'supabase_only'
  push_decided_at TIMESTAMP WITH TIME ZONE
);

COMMENT ON TABLE introductions IS 'Network flow tracking. Who introduced whom, and what came of it.';

-- ============================================================
-- PART 2: PATTERN TRACKING TABLES
-- ============================================================

-- ------------------------------------------------------------
-- STAGE_TRANSITIONS (Funnel Analysis)
-- Automatically logged when relationship.stage changes
-- ------------------------------------------------------------
CREATE TABLE stage_transitions (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

  relationship_id UUID NOT NULL REFERENCES relationships(id) ON DELETE CASCADE,
  from_stage TEXT NOT NULL,
  to_stage TEXT NOT NULL,
  transition_date DATE NOT NULL,

  -- Context
  days_in_previous_stage INTEGER,
  interaction_id UUID REFERENCES interactions(id) ON DELETE SET NULL,

  -- Denormalized for pattern queries
  relationship_source TEXT,
  relationship_geography TEXT,
  relationship_type TEXT
);

COMMENT ON TABLE stage_transitions IS 'Auto-logged when relationship stage changes. Enables funnel and velocity analysis.';

-- ------------------------------------------------------------
-- WEEKLY_SNAPSHOTS (Trend Analysis)
-- Pre-aggregated metrics for performance
-- ------------------------------------------------------------
CREATE TABLE weekly_snapshots (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  week_start DATE NOT NULL,
  week_end DATE NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

  -- Portfolio counts
  total_relationships INTEGER,
  by_stage JSONB,
  by_temperature JSONB,
  by_geography JSONB,
  by_type JSONB,

  -- Activity metrics
  meetings_held INTEGER,
  unique_relationships_touched INTEGER,
  new_relationships INTEGER,
  relationships_warmed INTEGER,
  relationships_cooled INTEGER,

  -- Stage movement
  stage_progressions JSONB,

  -- Commitment metrics
  commitments_made_us INTEGER,
  commitments_completed_us INTEGER,
  commitments_made_them INTEGER,
  commitments_completed_them INTEGER,

  -- Signal summary
  signals_by_type JSONB,
  actionable_signals INTEGER,

  -- Pipeline
  total_pipeline_value DECIMAL,
  pipeline_by_stage JSONB,

  -- Introduction activity
  intros_received INTEGER,
  intros_made INTEGER,
  intros_converted INTEGER
);

COMMENT ON TABLE weekly_snapshots IS 'Pre-aggregated weekly metrics for trend analysis and pattern dashboards.';

-- ------------------------------------------------------------
-- PUSH_LOG (Audit Trail)
-- Track what was pushed to Asana and when
-- ------------------------------------------------------------
CREATE TABLE push_log (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

  -- Source
  source_table TEXT NOT NULL,
  source_id UUID NOT NULL,

  -- Destination
  asana_project_gid TEXT,
  asana_task_gid TEXT,
  asana_task_url TEXT,

  -- Context
  pushed_by TEXT DEFAULT 'manual',
  push_type TEXT
    -- Values: 'manual', 'bulk', 'auto_rule'
);

COMMENT ON TABLE push_log IS 'Audit log of all items pushed to Asana.';

-- ============================================================
-- PART 3: INDEXES
-- ============================================================

-- Relationships
CREATE INDEX idx_relationships_stage ON relationships(stage);
CREATE INDEX idx_relationships_temperature ON relationships(temperature);
CREATE INDEX idx_relationships_geography ON relationships(geography);
CREATE INDEX idx_relationships_last_interaction ON relationships(last_interaction_date);
CREATE INDEX idx_relationships_days_since ON relationships(days_since_contact);
CREATE INDEX idx_relationships_asana_gid ON relationships(asana_task_gid);
CREATE INDEX idx_relationships_introducer ON relationships(introducer_id);
CREATE INDEX idx_relationships_active ON relationships(is_active) WHERE is_active = true;
CREATE INDEX idx_relationships_push_status ON relationships(push_status);
CREATE INDEX idx_relationships_source ON relationships(source);

-- Interactions
CREATE INDEX idx_interactions_date ON interactions(interaction_date DESC);
CREATE INDEX idx_interactions_relationship ON interactions(relationship_id);
CREATE INDEX idx_interactions_type ON interactions(meeting_type);
CREATE INDEX idx_interactions_outcome ON interactions(outcome);
CREATE INDEX idx_interactions_needs_review ON interactions(needs_review) WHERE needs_review = true;

-- Commitments
CREATE INDEX idx_commitments_status ON commitments(status);
CREATE INDEX idx_commitments_owner ON commitments(owner);
CREATE INDEX idx_commitments_due_date ON commitments(due_date);
CREATE INDEX idx_commitments_relationship ON commitments(relationship_id);
-- FIX: Removed CURRENT_DATE from predicate (not IMMUTABLE)
-- Original: WHERE status = 'pending' AND due_date < CURRENT_DATE
CREATE INDEX idx_commitments_overdue ON commitments(status, due_date)
  WHERE status = 'pending';
CREATE INDEX idx_commitments_push_status ON commitments(push_status);

-- Signals
CREATE INDEX idx_signals_type ON signals(signal_type);
CREATE INDEX idx_signals_actionable ON signals(actionable) WHERE actionable = true;
CREATE INDEX idx_signals_relationship ON signals(relationship_id);
CREATE INDEX idx_signals_significance ON signals(significance);
CREATE INDEX idx_signals_push_status ON signals(push_status);

-- Introductions
CREATE INDEX idx_introductions_introducer ON introductions(introducer_id);
CREATE INDEX idx_introductions_introduced ON introductions(introduced_id);
CREATE INDEX idx_introductions_status ON introductions(status);
CREATE INDEX idx_introductions_direction ON introductions(direction);

-- Stage Transitions
CREATE INDEX idx_transitions_relationship ON stage_transitions(relationship_id);
CREATE INDEX idx_transitions_date ON stage_transitions(transition_date);
CREATE INDEX idx_transitions_stages ON stage_transitions(from_stage, to_stage);
CREATE INDEX idx_transitions_source ON stage_transitions(relationship_source);
CREATE INDEX idx_transitions_geography ON stage_transitions(relationship_geography);

-- Weekly Snapshots
CREATE INDEX idx_snapshots_week ON weekly_snapshots(week_start DESC);

-- Push Log
CREATE INDEX idx_push_log_source ON push_log(source_table, source_id);

-- ============================================================
-- PART 4: FUNCTIONS & TRIGGERS
-- ============================================================

-- ------------------------------------------------------------
-- Auto-update updated_at timestamp
-- ------------------------------------------------------------
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER relationships_updated_at
  BEFORE UPDATE ON relationships
  FOR EACH ROW
  EXECUTE FUNCTION update_updated_at();

-- ------------------------------------------------------------
-- Calculate days_since_contact
-- ------------------------------------------------------------
CREATE OR REPLACE FUNCTION calculate_days_since_contact()
RETURNS TRIGGER AS $$
BEGIN
  IF NEW.last_interaction_date IS NOT NULL THEN
    NEW.days_since_contact = CURRENT_DATE - NEW.last_interaction_date;
  ELSE
    NEW.days_since_contact = NULL;
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER relationships_days_since_contact
  BEFORE INSERT OR UPDATE OF last_interaction_date ON relationships
  FOR EACH ROW
  EXECUTE FUNCTION calculate_days_since_contact();

-- ------------------------------------------------------------
-- Auto-update temperature based on days_since_contact
-- Thresholds: 30-60 warm->cool, 60-90 cool->cold
-- ------------------------------------------------------------
CREATE OR REPLACE FUNCTION auto_update_temperature()
RETURNS TRIGGER AS $$
BEGIN
  -- Skip if relationship is closed or dormant
  IF NEW.stage IN ('closed_won', 'closed_lost', 'dormant') THEN
    RETURN NEW;
  END IF;

  -- Skip if no contact date
  IF NEW.days_since_contact IS NULL THEN
    RETURN NEW;
  END IF;

  -- Apply temperature rules
  IF NEW.days_since_contact <= 30 THEN
    -- Recent contact: can be hot or warm, don't auto-cool
    NULL; -- Keep current temperature

  ELSIF NEW.days_since_contact > 30 AND NEW.days_since_contact <= 60 THEN
    -- 30-60 days: should be cool at most
    IF NEW.temperature = 'hot' THEN
      NEW.temperature = 'warm';
      NEW.temperature_updated_at = NOW();
    ELSIF NEW.temperature = 'warm' THEN
      NEW.temperature = 'cool';
      NEW.temperature_updated_at = NOW();
    END IF;

  ELSIF NEW.days_since_contact > 60 AND NEW.days_since_contact <= 90 THEN
    -- 60-90 days: should be cool
    IF NEW.temperature IN ('hot', 'warm') THEN
      NEW.temperature = 'cool';
      NEW.temperature_updated_at = NOW();
    END IF;

  ELSIF NEW.days_since_contact > 90 THEN
    -- 90+ days: cold
    IF NEW.temperature != 'cold' THEN
      NEW.temperature = 'cold';
      NEW.temperature_updated_at = NOW();
    END IF;
  END IF;

  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER relationships_auto_temperature
  BEFORE INSERT OR UPDATE OF days_since_contact ON relationships
  FOR EACH ROW
  EXECUTE FUNCTION auto_update_temperature();

-- ------------------------------------------------------------
-- Log stage transitions automatically
-- ------------------------------------------------------------
CREATE OR REPLACE FUNCTION log_stage_transition()
RETURNS TRIGGER AS $$
BEGIN
  IF OLD.stage IS DISTINCT FROM NEW.stage THEN
    INSERT INTO stage_transitions (
      relationship_id,
      from_stage,
      to_stage,
      transition_date,
      days_in_previous_stage,
      relationship_source,
      relationship_geography,
      relationship_type
    ) VALUES (
      NEW.id,
      OLD.stage,
      NEW.stage,
      CURRENT_DATE,
      CASE
        WHEN OLD.stage_changed_at IS NOT NULL
        THEN CURRENT_DATE - OLD.stage_changed_at::date
        ELSE NULL
      END,
      NEW.source,
      NEW.geography,
      NEW.relationship_types[1]
    );
    NEW.stage_changed_at = NOW();
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER relationships_stage_transition
  BEFORE UPDATE OF stage ON relationships
  FOR EACH ROW
  EXECUTE FUNCTION log_stage_transition();

-- ------------------------------------------------------------
-- Update relationship metrics after new interaction
-- ------------------------------------------------------------
CREATE OR REPLACE FUNCTION update_relationship_from_interaction()
RETURNS TRIGGER AS $$
DECLARE
  temp_change TEXT;
BEGIN
  -- Get temperature change value
  temp_change := NEW.temperature_change;

  UPDATE relationships
  SET
    last_interaction_date = NEW.interaction_date,
    last_interaction_id = NEW.id,
    interaction_count = interaction_count + 1,
    -- Update stage if interaction indicates change
    stage = COALESCE(NEW.stage_change_to, stage),
    -- Temperature adjustment based on interaction outcome
    temperature = CASE
      WHEN temp_change = 'warmed' THEN 'hot'
      WHEN temp_change = 'cooled' AND temperature = 'hot' THEN 'warm'
      WHEN temp_change = 'cooled' AND temperature = 'warm' THEN 'cool'
      WHEN temp_change = 'cooled' AND temperature = 'cool' THEN 'cold'
      ELSE temperature
    END,
    temperature_updated_at = CASE
      WHEN temp_change IN ('warmed', 'cooled') THEN NOW()
      ELSE temperature_updated_at
    END
  WHERE id = NEW.relationship_id;

  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER interactions_update_relationship
  AFTER INSERT ON interactions
  FOR EACH ROW
  EXECUTE FUNCTION update_relationship_from_interaction();

-- ------------------------------------------------------------
-- Mark commitments as overdue (run via scheduled job)
-- ------------------------------------------------------------
CREATE OR REPLACE FUNCTION mark_overdue_commitments()
RETURNS INTEGER AS $$
DECLARE
  updated_count INTEGER;
BEGIN
  UPDATE commitments
  SET status = 'overdue'
  WHERE status = 'pending'
    AND due_date < CURRENT_DATE;

  GET DIAGNOSTICS updated_count = ROW_COUNT;
  RETURN updated_count;
END;
$$ LANGUAGE plpgsql;

-- ------------------------------------------------------------
-- Refresh days_since_contact for all relationships
-- (run daily via scheduled job)
-- ------------------------------------------------------------
CREATE OR REPLACE FUNCTION refresh_days_since_contact()
RETURNS INTEGER AS $$
DECLARE
  updated_count INTEGER;
BEGIN
  UPDATE relationships
  SET days_since_contact = CURRENT_DATE - last_interaction_date
  WHERE last_interaction_date IS NOT NULL
    AND is_active = true;

  GET DIAGNOSTICS updated_count = ROW_COUNT;
  RETURN updated_count;
END;
$$ LANGUAGE plpgsql;

-- ============================================================
-- PART 5: VIEWS
-- ============================================================

-- ------------------------------------------------------------
-- Pending Review Queue
-- Items awaiting your decision to push to Asana
-- ------------------------------------------------------------
CREATE OR REPLACE VIEW v_pending_review AS
SELECT
  'relationship' as item_type,
  r.id,
  r.name as title,
  r.organization as subtitle,
  r.created_at,
  NULL::date as due_date,
  r.source,
  NULL as confidence,
  r.push_status,
  NULL::uuid as interaction_id
FROM relationships r
WHERE r.push_status = 'pending_review'
  AND r.is_active = true

UNION ALL

SELECT
  CASE WHEN c.owner = 'us' THEN 'commitment_ours' ELSE 'commitment_theirs' END as item_type,
  c.id,
  c.description as title,
  r.name as subtitle,
  c.created_at,
  c.due_date,
  NULL as source,
  NULL as confidence,
  c.push_status,
  c.interaction_id
FROM commitments c
JOIN relationships r ON c.relationship_id = r.id
WHERE c.push_status = 'pending_review'

UNION ALL

SELECT
  'signal' as item_type,
  s.id,
  s.description as title,
  r.name as subtitle,
  s.created_at,
  NULL::date as due_date,
  NULL as source,
  s.confidence,
  s.push_status,
  s.interaction_id
FROM signals s
JOIN relationships r ON s.relationship_id = r.id
WHERE s.push_status = 'pending_review'

ORDER BY created_at DESC;

COMMENT ON VIEW v_pending_review IS 'Items awaiting decision to push to Asana or keep in Supabase only.';

-- ------------------------------------------------------------
-- Attention Queue
-- Cooling relationships, overdue commitments, actionable signals
-- ------------------------------------------------------------
CREATE OR REPLACE VIEW v_attention_queue AS

-- Cooling relationships
SELECT
  'cooling_relationship' as attention_type,
  r.id,
  r.name as title,
  r.organization as subtitle,
  r.stage,
  r.temperature,
  r.days_since_contact,
  r.last_interaction_date,
  NULL::date as due_date,
  CASE
    WHEN r.days_since_contact > 60 THEN 1
    WHEN r.days_since_contact > 45 THEN 2
    ELSE 3
  END as urgency
FROM relationships r
WHERE r.is_active = true
  AND r.stage NOT IN ('closed_won', 'closed_lost', 'dormant')
  AND r.days_since_contact > 30

UNION ALL

-- Our overdue commitments
SELECT
  'commitment_ours_overdue' as attention_type,
  c.id,
  c.description as title,
  r.name as subtitle,
  NULL as stage,
  NULL as temperature,
  NULL as days_since_contact,
  NULL::date as last_interaction_date,
  c.due_date,
  CASE
    WHEN c.due_date < CURRENT_DATE - INTERVAL '7 days' THEN 1
    WHEN c.due_date < CURRENT_DATE THEN 2
    ELSE 3
  END as urgency
FROM commitments c
JOIN relationships r ON c.relationship_id = r.id
WHERE c.owner = 'us'
  AND c.status IN ('pending', 'overdue')
  AND c.due_date <= CURRENT_DATE

UNION ALL

-- Their overdue commitments
SELECT
  'commitment_theirs_overdue' as attention_type,
  c.id,
  c.description as title,
  r.name as subtitle,
  NULL as stage,
  NULL as temperature,
  NULL as days_since_contact,
  NULL::date as last_interaction_date,
  c.due_date,
  CASE
    WHEN c.due_date < CURRENT_DATE - INTERVAL '14 days' THEN 1
    WHEN c.due_date < CURRENT_DATE - INTERVAL '7 days' THEN 2
    ELSE 3
  END as urgency
FROM commitments c
JOIN relationships r ON c.relationship_id = r.id
WHERE c.owner = 'them'
  AND c.status IN ('pending', 'overdue')
  AND c.due_date <= CURRENT_DATE

UNION ALL

-- Actionable signals
SELECT
  'signal_actionable' as attention_type,
  s.id,
  s.description as title,
  r.name as subtitle,
  NULL as stage,
  NULL as temperature,
  NULL as days_since_contact,
  NULL::date as last_interaction_date,
  NULL::date as due_date,
  CASE
    WHEN s.significance = 'critical' THEN 1
    WHEN s.significance = 'high' THEN 2
    ELSE 3
  END as urgency
FROM signals s
JOIN relationships r ON s.relationship_id = r.id
WHERE s.actionable = true
  AND s.action_taken IS NULL

ORDER BY urgency, attention_type;

COMMENT ON VIEW v_attention_queue IS 'Items needing attention: cooling relationships, overdue commitments, actionable signals.';

-- ------------------------------------------------------------
-- Portfolio Health Summary
-- Aggregated counts by stage, temperature, geography
-- ------------------------------------------------------------
CREATE OR REPLACE VIEW v_portfolio_health AS
SELECT
  -- Temperature distribution
  COUNT(*) FILTER (WHERE temperature = 'hot') as hot_count,
  COUNT(*) FILTER (WHERE temperature = 'warm') as warm_count,
  COUNT(*) FILTER (WHERE temperature = 'cool') as cool_count,
  COUNT(*) FILTER (WHERE temperature = 'cold') as cold_count,

  -- Stage distribution
  COUNT(*) FILTER (WHERE stage = 'research') as stage_research,
  COUNT(*) FILTER (WHERE stage = 'initial_outreach') as stage_outreach,
  COUNT(*) FILTER (WHERE stage = 'discovery') as stage_discovery,
  COUNT(*) FILTER (WHERE stage = 'proposal') as stage_proposal,
  COUNT(*) FILTER (WHERE stage = 'negotiation') as stage_negotiation,
  COUNT(*) FILTER (WHERE stage = 'active') as stage_active,
  COUNT(*) FILTER (WHERE stage = 'renewal') as stage_renewal,
  COUNT(*) FILTER (WHERE stage = 'dormant') as stage_dormant,
  COUNT(*) FILTER (WHERE stage = 'closed_won') as stage_closed_won,
  COUNT(*) FILTER (WHERE stage = 'closed_lost') as stage_closed_lost,

  -- Geography distribution
  COUNT(*) FILTER (WHERE geography = 'brazil') as geo_brazil,
  COUNT(*) FILTER (WHERE geography = 'north_america') as geo_north_america,
  COUNT(*) FILTER (WHERE geography = 'europe') as geo_europe,
  COUNT(*) FILTER (WHERE geography = 'latin_america') as geo_latin_america,
  COUNT(*) FILTER (WHERE geography = 'asia_pacific') as geo_apac,
  COUNT(*) FILTER (WHERE geography = 'global') as geo_global,

  -- Pipeline value
  SUM(deal_value) FILTER (WHERE stage IN ('discovery', 'proposal', 'negotiation')) as active_pipeline_value,
  SUM(deal_value) FILTER (WHERE stage = 'active') as active_relationship_value,
  SUM(deal_value) FILTER (WHERE stage = 'closed_won') as closed_won_value,

  -- Total
  COUNT(*) as total_relationships
FROM relationships
WHERE is_active = true;

COMMENT ON VIEW v_portfolio_health IS 'Aggregated portfolio metrics for health dashboard.';

-- ------------------------------------------------------------
-- Introducer ROI
-- Who sends the best introductions
-- ------------------------------------------------------------
CREATE OR REPLACE VIEW v_introducer_roi AS
SELECT
  r.id as introducer_id,
  r.name as introducer_name,
  r.organization as introducer_org,
  COUNT(i.id) as total_intros,
  COUNT(i.id) FILTER (WHERE i.status IN ('converted', 'meeting_held')) as successful_intros,
  ROUND(
    COUNT(i.id) FILTER (WHERE i.status IN ('converted', 'meeting_held'))::decimal
    / NULLIF(COUNT(i.id), 0) * 100,
    1
  ) as conversion_rate,
  SUM(i.value_generated) as total_value_generated,
  MAX(i.created_at) as last_intro_date
FROM relationships r
LEFT JOIN introductions i ON r.id = i.introducer_id AND i.direction = 'inbound'
WHERE r.is_active = true
GROUP BY r.id, r.name, r.organization
HAVING COUNT(i.id) > 0
ORDER BY conversion_rate DESC, total_intros DESC;

COMMENT ON VIEW v_introducer_roi IS 'Ranking of introducers by conversion rate and value generated.';

-- ------------------------------------------------------------
-- Conversion Funnel
-- Stage-to-stage conversion rates
-- ------------------------------------------------------------
CREATE OR REPLACE VIEW v_conversion_funnel AS
SELECT
  from_stage,
  to_stage,
  COUNT(*) as transition_count,
  AVG(days_in_previous_stage) as avg_days_in_stage,
  relationship_source,
  relationship_geography
FROM stage_transitions
WHERE transition_date >= CURRENT_DATE - INTERVAL '6 months'
GROUP BY from_stage, to_stage, relationship_source, relationship_geography
ORDER BY from_stage, to_stage;

COMMENT ON VIEW v_conversion_funnel IS 'Stage transition metrics for funnel analysis.';

-- ------------------------------------------------------------
-- Recent Activity Summary
-- Last 7 days activity
-- ------------------------------------------------------------
CREATE OR REPLACE VIEW v_recent_activity AS
SELECT
  -- Meetings
  (SELECT COUNT(*) FROM interactions WHERE interaction_date >= CURRENT_DATE - INTERVAL '7 days') as meetings_this_week,
  (SELECT COUNT(DISTINCT relationship_id) FROM interactions WHERE interaction_date >= CURRENT_DATE - INTERVAL '7 days') as relationships_touched,

  -- New relationships
  (SELECT COUNT(*) FROM relationships WHERE created_at >= CURRENT_DATE - INTERVAL '7 days' AND is_active = true) as new_relationships,

  -- Commitments
  (SELECT COUNT(*) FROM commitments WHERE created_at >= CURRENT_DATE - INTERVAL '7 days' AND owner = 'us') as new_commitments_ours,
  (SELECT COUNT(*) FROM commitments WHERE created_at >= CURRENT_DATE - INTERVAL '7 days' AND owner = 'them') as new_commitments_theirs,
  (SELECT COUNT(*) FROM commitments WHERE completed_at >= CURRENT_DATE - INTERVAL '7 days' AND owner = 'us') as completed_commitments_ours,

  -- Signals
  (SELECT COUNT(*) FROM signals WHERE created_at >= CURRENT_DATE - INTERVAL '7 days') as new_signals,
  (SELECT COUNT(*) FROM signals WHERE created_at >= CURRENT_DATE - INTERVAL '7 days' AND actionable = true) as actionable_signals,

  -- Stage changes
  (SELECT COUNT(*) FROM stage_transitions WHERE transition_date >= CURRENT_DATE - INTERVAL '7 days') as stage_changes,

  -- Pending review
  (SELECT COUNT(*) FROM v_pending_review) as pending_review_count;

COMMENT ON VIEW v_recent_activity IS 'Summary of activity in the last 7 days.';

-- ============================================================
-- PART 6: ROW LEVEL SECURITY
-- ============================================================

ALTER TABLE relationships ENABLE ROW LEVEL SECURITY;
ALTER TABLE interactions ENABLE ROW LEVEL SECURITY;
ALTER TABLE commitments ENABLE ROW LEVEL SECURITY;
ALTER TABLE signals ENABLE ROW LEVEL SECURITY;
ALTER TABLE introductions ENABLE ROW LEVEL SECURITY;
ALTER TABLE stage_transitions ENABLE ROW LEVEL SECURITY;
ALTER TABLE weekly_snapshots ENABLE ROW LEVEL SECURITY;
ALTER TABLE push_log ENABLE ROW LEVEL SECURITY;

-- Allow all operations (you can restrict later for multi-user)
CREATE POLICY "Allow all on relationships" ON relationships FOR ALL USING (true);
CREATE POLICY "Allow all on interactions" ON interactions FOR ALL USING (true);
CREATE POLICY "Allow all on commitments" ON commitments FOR ALL USING (true);
CREATE POLICY "Allow all on signals" ON signals FOR ALL USING (true);
CREATE POLICY "Allow all on introductions" ON introductions FOR ALL USING (true);
CREATE POLICY "Allow all on stage_transitions" ON stage_transitions FOR ALL USING (true);
CREATE POLICY "Allow all on weekly_snapshots" ON weekly_snapshots FOR ALL USING (true);
CREATE POLICY "Allow all on push_log" ON push_log FOR ALL USING (true);

-- ============================================================
-- PART 7: REALTIME SUBSCRIPTIONS
-- ============================================================

-- Enable realtime for key tables
ALTER PUBLICATION supabase_realtime ADD TABLE relationships;
ALTER PUBLICATION supabase_realtime ADD TABLE interactions;
ALTER PUBLICATION supabase_realtime ADD TABLE commitments;
ALTER PUBLICATION supabase_realtime ADD TABLE signals;


-- ============================================================
-- ============================================================
-- PART 8: EXTENDED INTELLIGENCE SCHEMA (v2.0)
-- Personas, Services, Battle Intelligence
-- ============================================================
-- ============================================================

-- ============================================================
-- PERSONA INTELLIGENCE
-- ============================================================

-- ------------------------------------------------------------
-- PERSONA ARCHETYPES
-- The types of people you engage with, with playbook data
-- ------------------------------------------------------------
CREATE TABLE persona_archetypes (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

  -- Identity
  name TEXT NOT NULL UNIQUE,
    -- Examples: 'government_innovation', 'university_tto', 'corporate_innovation',
    --           'vc_partner', 'foundation_program', 'startup_founder',
    --           'research_director', 'c_suite_executive'
  display_name TEXT NOT NULL,
  description TEXT,

  -- Engagement guidance (evolves from learnings)
  typical_title_patterns TEXT[],
    -- e.g., ['Director', 'Head of Innovation', 'Chief']
  typical_organizations TEXT[],
    -- e.g., ['CNEN', 'FAPESP', 'FINEP'] for government_innovation

  -- Decision patterns
  typical_decision_timeline TEXT,
    -- e.g., '3-6 months', '6-12 months for government'
  decision_influencers TEXT,
    -- Who else needs to be involved?
  budget_cycle_notes TEXT,
    -- e.g., 'Government: fiscal year ends March. Proposals needed by November.'

  -- Engagement playbook
  preferred_meeting_format TEXT,
    -- e.g., 'in_person first, then video'
  communication_style_notes TEXT,
    -- e.g., 'Formal initial approach, relationship-building before business'
  cultural_considerations JSONB,
    -- By geography: {"brazil": "...", "north_america": "..."}

  -- What works
  effective_proof_points TEXT[],
    -- Proof points that resonate with this persona
  effective_language TEXT[],
    -- Phrases/framing that works
  ineffective_approaches TEXT[],
    -- What to avoid

  -- Engagement cadence
  recommended_touch_frequency_days INTEGER,
    -- How often to reach out
  warming_activities TEXT[],
    -- Activities that build relationship

  -- Metrics (auto-calculated)
  total_relationships INTEGER DEFAULT 0,
  active_relationships INTEGER DEFAULT 0,
  avg_conversion_days DECIMAL,
  conversion_rate DECIMAL,
  avg_deal_value DECIMAL
);

-- Seed with initial persona archetypes
INSERT INTO persona_archetypes (name, display_name, description, typical_title_patterns, typical_decision_timeline, recommended_touch_frequency_days) VALUES
('government_innovation', 'Government Innovation', 'Innovation directors and program managers at government agencies and ministries',
 ARRAY['Director', 'Coordinator', 'Secretary', 'Superintendent'], '6-12 months', 21),
('university_tto', 'University Tech Transfer', 'Technology transfer officers and commercialization leads at universities',
 ARRAY['Director of Tech Transfer', 'Licensing Manager', 'Commercialization Director'], '3-6 months', 14),
('corporate_innovation', 'Corporate Innovation', 'Innovation and R&D leaders at established companies',
 ARRAY['VP Innovation', 'Chief Innovation Officer', 'Head of R&D', 'Director of Strategy'], '3-6 months', 14),
('vc_partner', 'VC/Investment Partner', 'Partners and principals at venture capital and investment firms',
 ARRAY['Partner', 'Principal', 'Managing Director', 'Investment Director'], '1-3 months', 7),
('foundation_program', 'Foundation/Grant Program', 'Program officers and directors at philanthropic foundations',
 ARRAY['Program Officer', 'Program Director', 'Grants Manager'], '6-12 months', 21),
('startup_founder', 'Startup Founder/CEO', 'Founders and CEOs of early-stage companies',
 ARRAY['Founder', 'CEO', 'Co-founder', 'CTO'], '1-2 months', 7),
('research_director', 'Research Director', 'Principal investigators and research group leaders',
 ARRAY['Professor', 'Principal Investigator', 'Research Director', 'Lab Director'], '3-6 months', 14),
('c_suite_executive', 'C-Suite Executive', 'C-level executives making strategic decisions',
 ARRAY['CEO', 'COO', 'CFO', 'Chief Strategy Officer'], '2-4 months', 14);

-- ------------------------------------------------------------
-- Add persona_id to relationships table
-- ------------------------------------------------------------
ALTER TABLE relationships ADD COLUMN IF NOT EXISTS persona_id UUID REFERENCES persona_archetypes(id);
ALTER TABLE relationships ADD COLUMN IF NOT EXISTS persona_confidence TEXT DEFAULT 'medium';
  -- Values: 'high', 'medium', 'low', 'unclassified'

-- Index for persona queries
CREATE INDEX IF NOT EXISTS idx_relationships_persona ON relationships(persona_id);

-- ============================================================
-- SERVICE INTELLIGENCE
-- ============================================================

-- ------------------------------------------------------------
-- SERVICES (360's offerings)
-- ------------------------------------------------------------
CREATE TABLE services (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

  -- Identity
  name TEXT NOT NULL UNIQUE,
  display_name TEXT NOT NULL,
  category TEXT,
    -- 'assessment', 'validation', 'strategy', 'venture_studio', 'advisory'
  description TEXT,

  -- Positioning
  value_proposition TEXT,
  ideal_customer_profile TEXT,
  typical_engagement_length TEXT,

  -- Pricing intelligence
  pricing_model TEXT,
    -- 'fixed_fee', 'retainer', 'equity', 'success_fee', 'hybrid'
  typical_price_range_low DECIMAL,
  typical_price_range_high DECIMAL,
  price_currency TEXT DEFAULT 'USD',

  -- Persona fit (which personas buy this)
  best_fit_personas UUID[],
  secondary_fit_personas UUID[],

  -- Proof points
  key_case_studies TEXT[],
  quantified_outcomes TEXT[],
    -- e.g., ['40% faster time to market', '3x pipeline increase']

  -- Battle intelligence
  common_objections TEXT[],
  competitive_alternatives TEXT[],
  differentiation_points TEXT[],

  -- Metrics (auto-calculated)
  total_interest_signals INTEGER DEFAULT 0,
  active_opportunities INTEGER DEFAULT 0,
  closed_won_count INTEGER DEFAULT 0,
  closed_lost_count INTEGER DEFAULT 0,
  win_rate DECIMAL,
  avg_deal_size DECIMAL
);

-- Seed with 360's service offerings
INSERT INTO services (name, display_name, category, description, pricing_model) VALUES
('innovation_compass', '360 Innovation Compass', 'assessment',
 'Systematic IP and innovation portfolio assessment combining GenIP tools with Vianeo validation', 'fixed_fee'),
('vianeo_validation', 'Business Validation (Vianeo)', 'validation',
 'Structured business model validation using Vianeo framework', 'fixed_fee'),
('ip_assessment', 'IP Portfolio Assessment', 'assessment',
 'Technology portfolio evaluation and prioritization for commercialization', 'fixed_fee'),
('university_partnership', 'University Partnership Development', 'strategy',
 'Strategic partnership design between universities and industry', 'retainer'),
('venture_studio', 'Venture Studio Support', 'venture_studio',
 'End-to-end venture building from ideation to launch', 'equity'),
('market_entry_brazil', 'Brazil Market Entry', 'strategy',
 'Go-to-market strategy and partnership development for Brazil', 'hybrid'),
('innovation_strategy', 'Innovation Strategy Consulting', 'strategy',
 'Strategic advisory for innovation programs and initiatives', 'retainer'),
('franchise_development', '360 Franchise Development', 'venture_studio',
 'Licensing 360 methodology to regional partners', 'hybrid');

-- ------------------------------------------------------------
-- SERVICE INTEREST (Links relationships to services)
-- ------------------------------------------------------------
CREATE TABLE service_interest (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

  -- Links
  relationship_id UUID NOT NULL REFERENCES relationships(id) ON DELETE CASCADE,
  service_id UUID NOT NULL REFERENCES services(id) ON DELETE CASCADE,

  -- Interest level
  interest_level TEXT DEFAULT 'mentioned',
    -- 'mentioned', 'curious', 'evaluating', 'ready_to_buy', 'purchased', 'churned'
  interest_source TEXT,
    -- 'inbound_request', 'outbound_pitch', 'referral', 'organic_discovery'

  -- Context
  first_mentioned_interaction_id UUID REFERENCES interactions(id),
  first_mentioned_date DATE,

  -- Buying signals
  budget_confirmed BOOLEAN DEFAULT false,
  timeline_confirmed BOOLEAN DEFAULT false,
  decision_maker_engaged BOOLEAN DEFAULT false,

  -- Scope signals
  estimated_scope TEXT,
  estimated_value DECIMAL,
  scope_notes TEXT,

  -- Outcome
  outcome TEXT,
    -- 'won', 'lost', 'stalled', 'active', 'not_a_fit'
  outcome_date DATE,
  outcome_notes TEXT,
  lost_reason TEXT,
  lost_to_competitor TEXT,

  -- Unique constraint
  UNIQUE(relationship_id, service_id)
);

CREATE INDEX idx_service_interest_relationship ON service_interest(relationship_id);
CREATE INDEX idx_service_interest_service ON service_interest(service_id);
CREATE INDEX idx_service_interest_level ON service_interest(interest_level);

-- ============================================================
-- BATTLE INTELLIGENCE
-- ============================================================

-- ------------------------------------------------------------
-- OBJECTIONS (What pushback do we hear?)
-- ------------------------------------------------------------
CREATE TABLE objections (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

  -- Context
  interaction_id UUID REFERENCES interactions(id) ON DELETE SET NULL,
  relationship_id UUID NOT NULL REFERENCES relationships(id) ON DELETE CASCADE,
  service_id UUID REFERENCES services(id) ON DELETE SET NULL,
  persona_id UUID REFERENCES persona_archetypes(id) ON DELETE SET NULL,

  -- The objection
  objection_type TEXT NOT NULL,
    -- 'price', 'timing', 'authority', 'need', 'trust', 'competition',
    -- 'scope', 'risk', 'internal_politics', 'other'
  objection_text TEXT NOT NULL,
  verbatim_quote TEXT,

  -- Response
  response_given TEXT,
  response_effective BOOLEAN,

  -- Outcome
  objection_overcome BOOLEAN,
  what_worked TEXT,

  -- For pattern analysis
  geography TEXT,
  cultural_context TEXT
);

CREATE INDEX idx_objections_type ON objections(objection_type);
CREATE INDEX idx_objections_service ON objections(service_id);
CREATE INDEX idx_objections_persona ON objections(persona_id);

-- ------------------------------------------------------------
-- COMPETITOR MENTIONS
-- ------------------------------------------------------------
CREATE TABLE competitor_intel (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

  -- Context
  interaction_id UUID REFERENCES interactions(id) ON DELETE SET NULL,
  relationship_id UUID NOT NULL REFERENCES relationships(id) ON DELETE CASCADE,
  service_id UUID REFERENCES services(id) ON DELETE SET NULL,

  -- Competitor
  competitor_name TEXT NOT NULL,
  competitor_type TEXT,
    -- 'direct', 'indirect', 'internal_option', 'do_nothing'

  -- Intelligence
  context TEXT NOT NULL,
  verbatim_quote TEXT,

  -- Comparison
  perceived_strengths TEXT[],
  perceived_weaknesses TEXT[],
  price_comparison TEXT,
    -- 'higher', 'lower', 'similar', 'unknown'

  -- Outcome
  won_against BOOLEAN,
  lost_to BOOLEAN,
  differentiator_that_worked TEXT,

  -- For pattern analysis
  geography TEXT,
  persona_id UUID REFERENCES persona_archetypes(id)
);

CREATE INDEX idx_competitor_intel_competitor ON competitor_intel(competitor_name);
CREATE INDEX idx_competitor_intel_service ON competitor_intel(service_id);

-- ------------------------------------------------------------
-- PROOF POINTS (What evidence resonates?)
-- ------------------------------------------------------------
CREATE TABLE proof_points (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

  -- The proof point
  name TEXT NOT NULL,
  category TEXT,
    -- 'case_study', 'metric', 'testimonial', 'credential', 'methodology'
  description TEXT NOT NULL,
  quantified_result TEXT,
    -- e.g., '40% faster time to market'

  -- Source
  source_client TEXT,
  source_project TEXT,
  can_name_publicly BOOLEAN DEFAULT false,

  -- Applicability
  relevant_services UUID[],
  relevant_personas UUID[],
  relevant_geographies TEXT[],

  -- Effectiveness tracking
  times_used INTEGER DEFAULT 0,
  times_resonated INTEGER DEFAULT 0,
  resonance_rate DECIMAL
);

-- ------------------------------------------------------------
-- PROOF POINT USAGE (Track when proof points are used)
-- ------------------------------------------------------------
CREATE TABLE proof_point_usage (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

  proof_point_id UUID NOT NULL REFERENCES proof_points(id) ON DELETE CASCADE,
  interaction_id UUID REFERENCES interactions(id) ON DELETE SET NULL,
  relationship_id UUID NOT NULL REFERENCES relationships(id) ON DELETE CASCADE,

  -- Effectiveness
  resonated BOOLEAN,
  reaction_notes TEXT
);

-- ============================================================
-- ENHANCED SIGNALS (Add service/persona context)
-- ============================================================

-- Add service context to signals
ALTER TABLE signals ADD COLUMN IF NOT EXISTS service_id UUID REFERENCES services(id);
ALTER TABLE signals ADD COLUMN IF NOT EXISTS persona_id UUID REFERENCES persona_archetypes(id);

-- ============================================================
-- PATTERN TRACKING
-- ============================================================

-- ------------------------------------------------------------
-- CONVERSION PATTERNS
-- Pre-aggregated for analysis
-- ------------------------------------------------------------
CREATE TABLE conversion_patterns (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  calculated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

  -- Segment
  segment_type TEXT NOT NULL,
    -- 'persona', 'geography', 'source', 'service', 'persona_geo', 'service_persona'
  segment_value TEXT NOT NULL,
  segment_value_2 TEXT,
    -- For compound segments

  -- Metrics
  total_relationships INTEGER,
  converted_count INTEGER,
  conversion_rate DECIMAL,
  avg_days_to_convert DECIMAL,
  avg_deal_value DECIMAL,
  total_value DECIMAL,

  -- Stage breakdown
  stage_distribution JSONB,

  -- Time period
  period_start DATE,
  period_end DATE
);

CREATE INDEX idx_conversion_patterns_segment ON conversion_patterns(segment_type, segment_value);

-- ------------------------------------------------------------
-- ENGAGEMENT PATTERNS
-- What engagement patterns predict success?
-- ------------------------------------------------------------
CREATE TABLE engagement_patterns (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  calculated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

  -- Pattern
  pattern_name TEXT NOT NULL,
  pattern_description TEXT,

  -- Segment
  persona_id UUID REFERENCES persona_archetypes(id),
  service_id UUID REFERENCES services(id),
  geography TEXT,

  -- The pattern
  avg_meetings_to_convert DECIMAL,
  avg_days_between_meetings DECIMAL,
  optimal_meeting_frequency_days INTEGER,
  common_meeting_sequence TEXT[],
    -- e.g., ['intro', 'discovery', 'proposal_review', 'negotiation']

  -- What predicts success
  positive_indicators TEXT[],
  negative_indicators TEXT[],
  stall_predictors TEXT[],

  -- Sample size
  sample_size INTEGER
);

-- ============================================================
-- BATTLE CARD VIEWS
-- ============================================================

-- ------------------------------------------------------------
-- Service Battle Cards
-- Aggregated intelligence for each service
-- ------------------------------------------------------------
CREATE OR REPLACE VIEW v_service_battle_cards AS
SELECT
  s.id as service_id,
  s.name,
  s.display_name,
  s.category,
  s.value_proposition,
  s.typical_price_range_low,
  s.typical_price_range_high,
  s.pricing_model,

  -- Traction metrics
  COUNT(DISTINCT si.relationship_id) FILTER (WHERE si.interest_level != 'mentioned') as active_opportunities,
  COUNT(DISTINCT si.relationship_id) FILTER (WHERE si.outcome = 'won') as wins,
  COUNT(DISTINCT si.relationship_id) FILTER (WHERE si.outcome = 'lost') as losses,
  ROUND(
    COUNT(DISTINCT si.relationship_id) FILTER (WHERE si.outcome = 'won')::decimal /
    NULLIF(COUNT(DISTINCT si.relationship_id) FILTER (WHERE si.outcome IN ('won', 'lost')), 0) * 100,
    1
  ) as win_rate,
  AVG(si.estimated_value) FILTER (WHERE si.outcome = 'won') as avg_deal_size,

  -- Top objections (aggregated separately)
  s.common_objections,
  s.competitive_alternatives,
  s.differentiation_points,
  s.key_case_studies,
  s.quantified_outcomes

FROM services s
LEFT JOIN service_interest si ON s.id = si.service_id
GROUP BY s.id;

-- ------------------------------------------------------------
-- Persona Battle Cards
-- Aggregated intelligence for each persona
-- ------------------------------------------------------------
CREATE OR REPLACE VIEW v_persona_battle_cards AS
SELECT
  p.id as persona_id,
  p.name,
  p.display_name,
  p.description,

  -- Engagement guidance
  p.typical_decision_timeline,
  p.preferred_meeting_format,
  p.communication_style_notes,
  p.cultural_considerations,
  p.recommended_touch_frequency_days,

  -- What works
  p.effective_proof_points,
  p.effective_language,
  p.ineffective_approaches,

  -- Metrics
  COUNT(DISTINCT r.id) as total_relationships,
  COUNT(DISTINCT r.id) FILTER (WHERE r.stage = 'active') as active_relationships,
  COUNT(DISTINCT r.id) FILTER (WHERE r.stage = 'closed_won') as closed_won,
  ROUND(
    COUNT(DISTINCT r.id) FILTER (WHERE r.stage = 'closed_won')::decimal /
    NULLIF(COUNT(DISTINCT r.id) FILTER (WHERE r.stage IN ('closed_won', 'closed_lost')), 0) * 100,
    1
  ) as conversion_rate,
  AVG(r.deal_value) FILTER (WHERE r.stage = 'closed_won') as avg_deal_value

FROM persona_archetypes p
LEFT JOIN relationships r ON p.id = r.persona_id AND r.is_active = true
GROUP BY p.id;

-- ------------------------------------------------------------
-- Competitor Battle Cards
-- Aggregated competitor intelligence
-- ------------------------------------------------------------
CREATE OR REPLACE VIEW v_competitor_battle_cards AS
SELECT
  ci.competitor_name,
  ci.competitor_type,
  COUNT(*) as mention_count,
  COUNT(*) FILTER (WHERE ci.won_against = true) as wins_against,
  COUNT(*) FILTER (WHERE ci.lost_to = true) as losses_to,
  ROUND(
    COUNT(*) FILTER (WHERE ci.won_against = true)::decimal /
    NULLIF(COUNT(*) FILTER (WHERE ci.won_against = true OR ci.lost_to = true), 0) * 100,
    1
  ) as win_rate_against,

  -- Service context
  array_agg(DISTINCT s.display_name) as related_services

FROM competitor_intel ci
LEFT JOIN services s ON ci.service_id = s.id
GROUP BY ci.competitor_name, ci.competitor_type
ORDER BY mention_count DESC;

-- ------------------------------------------------------------
-- Objection Patterns
-- What objections come up and how to handle them
-- ------------------------------------------------------------
CREATE OR REPLACE VIEW v_objection_patterns AS
SELECT
  o.objection_type,
  s.display_name as service_name,
  p.display_name as persona_name,
  COUNT(*) as occurrence_count,
  COUNT(*) FILTER (WHERE o.objection_overcome = true) as overcome_count,
  ROUND(
    COUNT(*) FILTER (WHERE o.objection_overcome = true)::decimal /
    NULLIF(COUNT(*), 0) * 100,
    1
  ) as overcome_rate,

  -- Most common objection texts
  mode() WITHIN GROUP (ORDER BY o.objection_text) as most_common_objection

FROM objections o
LEFT JOIN services s ON o.service_id = s.id
LEFT JOIN persona_archetypes p ON o.persona_id = p.id
GROUP BY o.objection_type, s.display_name, p.display_name
ORDER BY occurrence_count DESC;

-- ============================================================
-- INTELLIGENCE DASHBOARD VIEWS
-- ============================================================

-- ------------------------------------------------------------
-- Service Traction Dashboard
-- Which services are getting interest?
-- ------------------------------------------------------------
CREATE OR REPLACE VIEW v_service_traction AS
SELECT
  s.id as service_id,
  s.display_name,
  s.category,

  -- Interest funnel
  COUNT(DISTINCT si.relationship_id) FILTER (WHERE si.interest_level = 'mentioned') as mentioned,
  COUNT(DISTINCT si.relationship_id) FILTER (WHERE si.interest_level = 'curious') as curious,
  COUNT(DISTINCT si.relationship_id) FILTER (WHERE si.interest_level = 'evaluating') as evaluating,
  COUNT(DISTINCT si.relationship_id) FILTER (WHERE si.interest_level = 'ready_to_buy') as ready_to_buy,
  COUNT(DISTINCT si.relationship_id) FILTER (WHERE si.interest_level = 'purchased') as purchased,

  -- Pipeline value
  SUM(si.estimated_value) FILTER (WHERE si.outcome = 'active') as pipeline_value,

  -- Recent activity (last 30 days)
  COUNT(DISTINCT si.relationship_id) FILTER (WHERE si.created_at > NOW() - INTERVAL '30 days') as new_interest_30d

FROM services s
LEFT JOIN service_interest si ON s.id = si.service_id
LEFT JOIN relationships r ON si.relationship_id = r.id
LEFT JOIN persona_archetypes p ON r.persona_id = p.id
GROUP BY s.id
ORDER BY evaluating DESC, curious DESC;

-- ------------------------------------------------------------
-- Persona Engagement Dashboard
-- How is engagement by persona type?
-- ------------------------------------------------------------
CREATE OR REPLACE VIEW v_persona_engagement AS
SELECT
  p.id as persona_id,
  p.display_name,
  p.recommended_touch_frequency_days,

  -- Relationship counts
  COUNT(DISTINCT r.id) as total_relationships,
  COUNT(DISTINCT r.id) FILTER (WHERE r.temperature = 'hot') as hot,
  COUNT(DISTINCT r.id) FILTER (WHERE r.temperature = 'warm') as warm,
  COUNT(DISTINCT r.id) FILTER (WHERE r.temperature = 'cool') as cool,
  COUNT(DISTINCT r.id) FILTER (WHERE r.temperature = 'cold') as cold,

  -- Engagement health
  COUNT(DISTINCT r.id) FILTER (WHERE r.days_since_contact > p.recommended_touch_frequency_days) as overdue_for_contact,
  AVG(r.days_since_contact) as avg_days_since_contact,

  -- Pipeline
  COUNT(DISTINCT r.id) FILTER (WHERE r.stage IN ('discovery', 'proposal', 'negotiation')) as in_pipeline,
  SUM(r.deal_value) FILTER (WHERE r.stage IN ('discovery', 'proposal', 'negotiation')) as pipeline_value,

  -- Activity (last 30 days)
  COUNT(DISTINCT i.id) FILTER (WHERE i.interaction_date > CURRENT_DATE - INTERVAL '30 days') as meetings_30d

FROM persona_archetypes p
LEFT JOIN relationships r ON p.id = r.persona_id AND r.is_active = true
LEFT JOIN interactions i ON r.id = i.relationship_id
GROUP BY p.id
ORDER BY total_relationships DESC;

-- ------------------------------------------------------------
-- Signal Intelligence Dashboard
-- What signals are we seeing across the portfolio?
-- ------------------------------------------------------------
CREATE OR REPLACE VIEW v_signal_intelligence AS
SELECT
  s.signal_type,
  COUNT(*) as total_signals,
  COUNT(*) FILTER (WHERE s.created_at > NOW() - INTERVAL '30 days') as signals_30d,
  COUNT(*) FILTER (WHERE s.actionable = true AND s.action_taken IS NULL) as pending_action,

  -- Outcome tracking
  COUNT(*) FILTER (WHERE s.outcome = 'confirmed') as confirmed,
  COUNT(*) FILTER (WHERE s.outcome = 'not_realized') as not_realized,
  ROUND(
    COUNT(*) FILTER (WHERE s.outcome = 'confirmed')::decimal /
    NULLIF(COUNT(*) FILTER (WHERE s.outcome IS NOT NULL), 0) * 100,
    1
  ) as confirmation_rate

FROM signals s
LEFT JOIN services svc ON s.service_id = svc.id
LEFT JOIN persona_archetypes p ON s.persona_id = p.id
GROUP BY s.signal_type
ORDER BY total_signals DESC;

-- ============================================================
-- EXTENDED RLS POLICIES
-- ============================================================

ALTER TABLE persona_archetypes ENABLE ROW LEVEL SECURITY;
ALTER TABLE services ENABLE ROW LEVEL SECURITY;
ALTER TABLE service_interest ENABLE ROW LEVEL SECURITY;
ALTER TABLE objections ENABLE ROW LEVEL SECURITY;
ALTER TABLE competitor_intel ENABLE ROW LEVEL SECURITY;
ALTER TABLE proof_points ENABLE ROW LEVEL SECURITY;
ALTER TABLE proof_point_usage ENABLE ROW LEVEL SECURITY;
ALTER TABLE conversion_patterns ENABLE ROW LEVEL SECURITY;
ALTER TABLE engagement_patterns ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Allow all on persona_archetypes" ON persona_archetypes FOR ALL USING (true);
CREATE POLICY "Allow all on services" ON services FOR ALL USING (true);
CREATE POLICY "Allow all on service_interest" ON service_interest FOR ALL USING (true);
CREATE POLICY "Allow all on objections" ON objections FOR ALL USING (true);
CREATE POLICY "Allow all on competitor_intel" ON competitor_intel FOR ALL USING (true);
CREATE POLICY "Allow all on proof_points" ON proof_points FOR ALL USING (true);
CREATE POLICY "Allow all on proof_point_usage" ON proof_point_usage FOR ALL USING (true);
CREATE POLICY "Allow all on conversion_patterns" ON conversion_patterns FOR ALL USING (true);
CREATE POLICY "Allow all on engagement_patterns" ON engagement_patterns FOR ALL USING (true);

-- ============================================================
-- SCHEMA DOCUMENTATION
-- ============================================================

COMMENT ON TABLE persona_archetypes IS 'Persona types with engagement playbooks. AI should classify new relationships into these.';
COMMENT ON TABLE services IS '360 service offerings. AI should detect interest signals for specific services.';
COMMENT ON TABLE service_interest IS 'Links relationships to services they have expressed interest in.';
COMMENT ON TABLE objections IS 'Objections heard in meetings. AI should extract these for battle card building.';
COMMENT ON TABLE competitor_intel IS 'Competitor mentions and intelligence. AI should extract these.';
COMMENT ON TABLE proof_points IS 'Evidence and case studies that resonate. Track effectiveness.';

-- ============================================================
-- DEPLOYMENT COMPLETE
-- ============================================================
--
-- Tables created (17 total):
--   CORE: relationships, interactions, commitments, signals, introductions,
--         stage_transitions, weekly_snapshots, push_log
--   INTELLIGENCE: persona_archetypes, services, service_interest, objections,
--                 competitor_intel, proof_points, proof_point_usage,
--                 conversion_patterns, engagement_patterns
--
-- Views created (13 total):
--   CORE: v_pending_review, v_attention_queue, v_portfolio_health,
--         v_introducer_roi, v_conversion_funnel, v_recent_activity
--   INTELLIGENCE: v_service_battle_cards, v_persona_battle_cards,
--                 v_competitor_battle_cards, v_objection_patterns,
--                 v_service_traction, v_persona_engagement, v_signal_intelligence
--
-- Functions created:
--   - update_updated_at() - Auto-update timestamps
--   - calculate_days_since_contact() - Calculate days since last interaction
--   - auto_update_temperature() - Auto-cool relationships based on time
--   - log_stage_transition() - Auto-log stage changes
--   - update_relationship_from_interaction() - Update metrics on new interaction
--   - mark_overdue_commitments() - Mark overdue (run via cron)
--   - refresh_days_since_contact() - Refresh all (run via cron)
--
-- Seeded data:
--   - 8 persona archetypes (government_innovation, university_tto, etc.)
--   - 8 services (innovation_compass, vianeo_validation, etc.)
--
-- ============================================================
