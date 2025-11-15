export type Json =
  | string
  | number
  | boolean
  | null
  | { [key: string]: Json | undefined }
  | Json[]

export interface Database {
  public: {
    Tables: {
      extractions: {
        Row: {
          id: string
          extraction_id: string
          created_at: string
          source_file_name: string | null
          source_file_url: string | null
          meeting_type: string | null
          template_name: string | null
          template_version: string | null
          entities_created: number
          entities_updated: number
          items_extracted: number
          completeness_score: number | null
          completeness_required: number | null
          completeness_optional: number | null
          confidence_level: string | null
          confidence_high_count: number
          confidence_medium_count: number
          confidence_low_count: number
          parsing_valid: boolean
          parsing_errors: string[] | null
          issues_count: number
          issues_list: string[] | null
          warnings_count: number
          warnings_list: string[] | null
          auto_quality_rating: string | null
          user_quality_rating: string | null
          flagged_for_review: boolean
          reviewed: boolean
          reviewed_at: string | null
          reviewed_by: string | null
          edit_count: number
          human_edit_required: boolean
          processing_time_seconds: number | null
          experiment_id: string | null
          experiment_variant: string | null
          extraction_summary: string | null
          completeness_details: Json | null
          entity_links: Json | null
          intelligence_data: Json | null
        }
        Insert: {
          id?: string
          extraction_id: string
          created_at?: string
          source_file_name?: string | null
          source_file_url?: string | null
          meeting_type?: string | null
          template_name?: string | null
          template_version?: string | null
          entities_created?: number
          entities_updated?: number
          items_extracted?: number
          completeness_score?: number | null
          completeness_required?: number | null
          completeness_optional?: number | null
          confidence_level?: string | null
          confidence_high_count?: number
          confidence_medium_count?: number
          confidence_low_count?: number
          parsing_valid?: boolean
          parsing_errors?: string[] | null
          issues_count?: number
          issues_list?: string[] | null
          warnings_count?: number
          warnings_list?: string[] | null
          auto_quality_rating?: string | null
          user_quality_rating?: string | null
          flagged_for_review?: boolean
          reviewed?: boolean
          reviewed_at?: string | null
          reviewed_by?: string | null
          edit_count?: number
          human_edit_required?: boolean
          processing_time_seconds?: number | null
          experiment_id?: string | null
          experiment_variant?: string | null
          extraction_summary?: string | null
          completeness_details?: Json | null
          entity_links?: Json | null
          intelligence_data?: Json | null
        }
        Update: {
          id?: string
          extraction_id?: string
          created_at?: string
          source_file_name?: string | null
          source_file_url?: string | null
          meeting_type?: string | null
          template_name?: string | null
          template_version?: string | null
          entities_created?: number
          entities_updated?: number
          items_extracted?: number
          completeness_score?: number | null
          completeness_required?: number | null
          completeness_optional?: number | null
          confidence_level?: string | null
          confidence_high_count?: number
          confidence_medium_count?: number
          confidence_low_count?: number
          parsing_valid?: boolean
          parsing_errors?: string[] | null
          issues_count?: number
          issues_list?: string[] | null
          warnings_count?: number
          warnings_list?: string[] | null
          auto_quality_rating?: string | null
          user_quality_rating?: string | null
          flagged_for_review?: boolean
          reviewed?: boolean
          reviewed_at?: string | null
          reviewed_by?: string | null
          edit_count?: number
          human_edit_required?: boolean
          processing_time_seconds?: number | null
          experiment_id?: string | null
          experiment_variant?: string | null
          extraction_summary?: string | null
          completeness_details?: Json | null
          entity_links?: Json | null
          intelligence_data?: Json | null
        }
      }
      experiments: {
        Row: {
          id: string
          created_at: string
          name: string
          template_name: string
          hypothesis: string | null
          version_a_description: string | null
          version_b_changes: string | null
          success_metric: string | null
          secondary_metrics: string[] | null
          status: string
          started_at: string
          ended_at: string | null
          sample_size_target: number
          sample_size_actual: number
          winner: string | null
          results: Json | null
        }
      }
      edits: {
        Row: {
          id: string
          created_at: string
          extraction_id: string | null
          entity_type: string | null
          entity_id: string | null
          entity_name: string | null
          field_name: string | null
          old_value: string | null
          new_value: string | null
          edit_type: string | null
          edited_by: string | null
          asana_task_url: string | null
        }
      }
      weekly_analyses: {
        Row: {
          id: string
          created_at: string
          week_start: string
          week_end: string
          total_extractions: number | null
          avg_completeness: number | null
          avg_user_rating: number | null
          avg_edit_count: number | null
          review_rate: number | null
          executive_summary: string | null
          key_insights: string[] | null
          priority_improvements: Json | null
          experiments_proposed: Json | null
          positive_trends: string[] | null
          metrics: Json | null
          problem_patterns: Json | null
          asana_task_id: string | null
          asana_task_url: string | null
        }
      }
    }
    Functions: {
      get_dashboard_metrics: {
        Args: Record<string, never>
        Returns: Json
      }
      get_quality_trend_30d: {
        Args: Record<string, never>
        Returns: {
          date: string
          completeness: number
          user_rating: number
          extractions: number
        }[]
      }
      get_template_performance: {
        Args: Record<string, never>
        Returns: {
          template_name: string
          extraction_count: number
          avg_completeness: number
          avg_user_rating: number
          avg_edit_count: number
          flagged_rate: number
          performance_grade: string
        }[]
      }
    }
  }
}
