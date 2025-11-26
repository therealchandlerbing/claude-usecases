/**
 * Zapier → Supabase Integration Code
 *
 * This replaces the Google Sheets step in your extraction workflow.
 * Use this in a "Code by Zapier" step after Claude extraction.
 */

// ===== CONFIGURATION =====
// Provide secrets via Zapier "Environment" variables or encrypted input fields
// instead of hard-coding them in the script.
const SUPABASE_URL = inputData.supabase_url || process.env.SUPABASE_URL;
const SUPABASE_SERVICE_ROLE_KEY =
  inputData.supabase_service_role_key || process.env.SUPABASE_SERVICE_ROLE_KEY;
// Prefer a scoped anon key when available; fall back to service role only when necessary
const SUPABASE_ANON_KEY =
  inputData.supabase_anon_key || process.env.SUPABASE_ANON_KEY || SUPABASE_SERVICE_ROLE_KEY;

if (!SUPABASE_URL) {
  throw new Error('Missing Supabase URL. Set supabase_url input or SUPABASE_URL secret.');
}

if (!SUPABASE_SERVICE_ROLE_KEY && !SUPABASE_ANON_KEY) {
  throw new Error(
    'Missing Supabase credentials. Provide supabase_service_role_key or supabase_anon_key as a secret input or environment variable.'
  );
}

// ===== MAIN FUNCTION =====

/**
 * Send extraction data to Supabase
 *
 * Input variables expected from previous Zapier steps:
 * - extraction_id
 * - source_file_name
 * - source_file_url
 * - meeting_type
 * - template_name
 * - template_version
 * - entities_created
 * - entities_updated
 * - items_extracted
 * - completeness_score
 * - confidence_dominant
 * - auto_quality_rating
 * - flagged_for_review
 * - processing_time
 * - intelligence_data (JSON string)
 * - etc.
 */

const extractionData = {
  extraction_id: inputData.extraction_id,
  source_file_name: inputData.source_file_name,
  source_file_url: inputData.source_file_url,
  meeting_type: inputData.meeting_type,

  template_name: inputData.template_name,
  template_version: inputData.template_version,

  entities_created: parseInt(inputData.entities_created) || 0,
  entities_updated: parseInt(inputData.entities_updated) || 0,
  items_extracted: parseInt(inputData.items_extracted) || 0,

  completeness_score: parseInt(inputData.completeness_score) || null,
  completeness_required: parseInt(inputData.completeness_required) || null,
  completeness_optional: parseInt(inputData.completeness_optional) || null,

  confidence_level: inputData.confidence_dominant,
  confidence_high_count: parseInt(inputData.confidence_high_count) || 0,
  confidence_medium_count: parseInt(inputData.confidence_medium_count) || 0,
  confidence_low_count: parseInt(inputData.confidence_low_count) || 0,

  parsing_valid: inputData.parsing_valid === 'true' || inputData.parsing_valid === true,
  parsing_errors: inputData.parsing_errors ? inputData.parsing_errors.split(';').filter(e => e) : [],

  issues_count: parseInt(inputData.issues_count) || 0,
  issues_list: inputData.issues_list ? inputData.issues_list.split(';').filter(e => e) : [],
  warnings_count: parseInt(inputData.warnings_count) || 0,
  warnings_list: inputData.warnings_list ? inputData.warnings_list.split(';').filter(e => e) : [],

  auto_quality_rating: inputData.auto_quality_rating,
  flagged_for_review: inputData.flagged_for_review === 'true' || inputData.flagged_for_review === true,

  processing_time_seconds: parseFloat(inputData.processing_time) || null,

  extraction_summary: inputData.extraction_summary,
  completeness_details: tryParseJSON(inputData.completeness_details),
  entity_links: tryParseJSON(inputData.entity_links),
  intelligence_data: tryParseJSON(inputData.intelligence_data)
};

// ===== INSERT TO SUPABASE =====

try {
  const response = await fetch(`${SUPABASE_URL}/rest/v1/extractions`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'apikey': SUPABASE_ANON_KEY,
      'Authorization': `Bearer ${SUPABASE_ANON_KEY}`,
      'Prefer': 'return=representation'  // Return the created row
    },
    body: JSON.stringify(extractionData)
  });

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(`Supabase API error: ${response.status} - ${errorText}`);
  }

  const result = await response.json();

  // Return data for use in subsequent Zapier steps
  output = {
    success: true,
    supabase_id: result[0].id,
    created_at: result[0].created_at,
    message: 'Extraction data successfully saved to Supabase'
  };

} catch (error) {
  // Log error and return for Zapier error handling
  output = {
    success: false,
    error: error.message,
    extraction_id: extractionData.extraction_id
  };

  // Optionally: Send error to Slack or email
  console.error('Failed to save to Supabase:', error);
}

// ===== HELPER FUNCTIONS =====

function tryParseJSON(jsonString) {
  if (!jsonString) return null;
  try {
    return JSON.parse(jsonString);
  } catch (e) {
    console.warn('Failed to parse JSON:', jsonString);
    return null;
  }
}


// ===== ALTERNATIVE: UPDATE EXISTING EXTRACTION =====

/**
 * If you need to UPDATE an extraction (e.g., when user rates it),
 * use this code instead:
 */

/*
const updateData = {
  user_quality_rating: inputData.user_rating,  // 'excellent', 'good', 'fair', 'poor'
  reviewed: true,
  reviewed_at: new Date().toISOString(),
  reviewed_by: inputData.user_name
};

const response = await fetch(
  `${SUPABASE_URL}/rest/v1/extractions?extraction_id=eq.${inputData.extraction_id}`,
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
      'apikey': SUPABASE_ANON_KEY,
      'Authorization': `Bearer ${SUPABASE_ANON_KEY}`,
      'Prefer': 'return=representation'
    },
    body: JSON.stringify(updateData)
  }
);
*/


// ===== ALTERNATIVE: RECORD AN EDIT =====

/**
 * When tracking manual edits from Asana, use this to insert into edits table:
 */

/*
const editData = {
  extraction_id: inputData.extraction_supabase_id,  // Link to extraction
  entity_type: inputData.entity_type,  // 'partnership', 'funding', 'stakeholder'
  entity_id: inputData.asana_task_id,
  entity_name: inputData.entity_name,
  field_name: inputData.field_edited,
  old_value: inputData.old_value,
  new_value: inputData.new_value,
  edit_type: inputData.edit_type,  // 'name', 'description', 'custom_field'
  edited_by: inputData.editor_name,
  asana_task_url: inputData.task_url
};

await fetch(`${SUPABASE_URL}/rest/v1/edits`, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'apikey': SUPABASE_ANON_KEY,
    'Authorization': `Bearer ${SUPABASE_ANON_KEY}`
  },
  body: JSON.stringify(editData)
});

// Also increment edit_count on the extraction
await fetch(
  `${SUPABASE_URL}/rest/v1/extractions?id=eq.${inputData.extraction_supabase_id}`,
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
      'apikey': SUPABASE_ANON_KEY,
      'Authorization': `Bearer ${SUPABASE_ANON_KEY}`
    },
    body: JSON.stringify({
      edit_count: inputData.current_edit_count + 1,
      human_edit_required: true
    })
  }
);
*/
