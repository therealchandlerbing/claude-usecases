import { createClient } from '@supabase/supabase-js';

// Initialize Supabase client
const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL;
const supabaseAnonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;

if (!supabaseUrl || !supabaseAnonKey) {
  console.warn('Supabase environment variables not set. Using mock data.');
}

export const supabase = supabaseUrl && supabaseAnonKey
  ? createClient(supabaseUrl, supabaseAnonKey)
  : null;

/**
 * Fetch action center data (pending review items + attention queue)
 */
export async function fetchActionData() {
  if (!supabase) {
    return getMockActionData();
  }

  try {
    // Fetch pending review items
    const [
      relationshipsRes,
      commitmentsRes,
      signalsRes,
      serviceInterestsRes,
      objectionsRes
    ] = await Promise.all([
      supabase
        .from('relationships')
        .select('*, persona:persona_archetypes(display_name)')
        .eq('push_status', 'pending_review')
        .eq('is_active', true),
      supabase
        .from('commitments')
        .select('*, relationship:relationships(name, organization)')
        .eq('push_status', 'pending_review'),
      supabase
        .from('signals')
        .select('*, relationship:relationships(name, organization)')
        .eq('push_status', 'pending_review'),
      supabase
        .from('service_interest')
        .select('*, relationship:relationships(name, organization), service:services(display_name)')
        .eq('interest_level', 'evaluating'),
      supabase
        .from('objections')
        .select('*, relationship:relationships(name, organization)')
        .is('objection_overcome', null)
    ]);

    // Fetch attention queue items
    const [coolingRes, overdueOursRes, overdueTheirsRes] = await Promise.all([
      supabase
        .from('relationships')
        .select('*')
        .eq('is_active', true)
        .gt('days_since_contact', 30)
        .not('stage', 'in', '("closed_won","closed_lost","dormant")')
        .order('days_since_contact', { ascending: false }),
      supabase
        .from('commitments')
        .select('*, relationship:relationships(name, organization)')
        .eq('owner', 'us')
        .in('status', ['pending', 'overdue'])
        .lt('due_date', new Date().toISOString().split('T')[0]),
      supabase
        .from('commitments')
        .select('*, relationship:relationships(name, organization)')
        .eq('owner', 'them')
        .in('status', ['pending', 'overdue'])
        .lt('due_date', new Date().toISOString().split('T')[0])
    ]);

    // Transform relationships for UI
    const pendingRelationships = (relationshipsRes.data || []).map(r => ({
      id: r.id,
      table: 'relationships',
      name: r.name,
      organization: r.organization,
      title: r.title,
      persona_type: r.persona?.display_name || r.persona_id,
      geography: r.geography,
      stage: r.stage,
      source: r.source,
      notes: r.notes,
      confidence: r.persona_confidence || 'medium',
      strategic_fit_score: r.strategic_fit_score,
      from_meeting: r.how_we_met
    }));

    // Transform commitments
    const commitmentsOurs = (commitmentsRes.data || [])
      .filter(c => c.owner === 'us')
      .map(c => ({
        id: c.id,
        table: 'commitments',
        description: c.description,
        relationship_name: c.relationship?.name,
        commitment_type: c.commitment_type,
        due_date: c.due_date,
        due_date_type: c.due_date_type,
        service_context: c.push_destination
      }));

    const commitmentsTheirs = (commitmentsRes.data || [])
      .filter(c => c.owner === 'them')
      .map(c => ({
        id: c.id,
        table: 'commitments',
        description: c.description,
        relationship_name: c.relationship?.name,
        commitment_type: c.commitment_type,
        due_date: c.due_date,
        due_date_type: c.due_date_type,
        service_context: c.push_destination
      }));

    // Transform service interests
    const serviceInterests = (serviceInterestsRes.data || []).map(si => ({
      id: si.id,
      table: 'service_interest',
      service: si.service?.display_name,
      relationship_name: si.relationship?.name,
      interest_level: si.interest_level,
      budget_confirmed: si.budget_confirmed,
      timeline_confirmed: si.timeline_confirmed,
      estimated_value: si.estimated_value,
      confidence: 'medium'
    }));

    // Transform signals
    const signals = (signalsRes.data || []).map(s => ({
      id: s.id,
      table: 'signals',
      signal_type: s.signal_type,
      description: s.description,
      relationship_name: s.relationship?.name,
      significance: s.significance,
      amount: s.amount,
      actionable: s.actionable,
      action_required: s.action_required,
      confidence: s.confidence
    }));

    // Transform objections
    const objections = (objectionsRes.data || []).map(o => ({
      id: o.id,
      table: 'objections',
      objection_type: o.objection_type,
      objection_text: o.objection_text,
      verbatim_quote: o.verbatim_quote,
      relationship_name: o.relationship?.name,
      response_given: o.response_given,
      objection_overcome: o.objection_overcome,
      what_worked: o.what_worked
    }));

    // Transform cooling relationships
    const cooling = (coolingRes.data || []).map(r => ({
      id: r.id,
      table: 'relationships',
      name: r.name,
      organization: r.organization,
      geography: r.geography,
      stage: r.stage,
      temperature: r.temperature,
      days_since_contact: r.days_since_contact
    }));

    // Transform overdue commitments
    const overdueOurs = (overdueOursRes.data || []).map(c => ({
      id: c.id,
      table: 'commitments',
      description: c.description,
      relationship_name: c.relationship?.name,
      days_overdue: Math.floor((Date.now() - new Date(c.due_date).getTime()) / (1000 * 60 * 60 * 24))
    }));

    const overdueTheirs = (overdueTheirsRes.data || []).map(c => ({
      id: c.id,
      table: 'commitments',
      description: c.description,
      relationship_name: c.relationship?.name,
      days_overdue: Math.floor((Date.now() - new Date(c.due_date).getTime()) / (1000 * 60 * 60 * 24))
    }));

    return {
      pending: {
        relationships: pendingRelationships,
        service_interests: serviceInterests,
        commitments_ours: commitmentsOurs,
        commitments_theirs: commitmentsTheirs,
        objections: objections,
        signals: signals
      },
      attention: {
        cooling: cooling,
        overdue_ours: overdueOurs,
        overdue_theirs: overdueTheirs
      }
    };
  } catch (error) {
    console.error('Error fetching action data:', error);
    return getMockActionData();
  }
}

/**
 * Fetch intelligence data (personas, services, competitors)
 */
export async function fetchIntelligenceData() {
  if (!supabase) {
    return getMockIntelligenceData();
  }

  try {
    const [personasRes, servicesRes, competitorsRes, objectionsRes] = await Promise.all([
      supabase.rpc('get_persona_dashboard_data').catch(() => ({ data: [] })),
      supabase.rpc('get_service_dashboard_data').catch(() => ({ data: [] })),
      supabase.from('v_competitor_battle_cards').select('*').catch(() => ({ data: [] })),
      supabase.from('v_objection_patterns').select('*').catch(() => ({ data: [] }))
    ]);

    // If RPC functions don't exist, fall back to direct queries
    let personas = personasRes.data || [];
    let services = servicesRes.data || [];

    if (personas.length === 0) {
      const { data } = await supabase.from('v_persona_engagement').select('*');
      personas = (data || []).map(p => ({
        id: p.persona_id,
        display_name: p.display_name,
        description: '',
        total_relationships: p.total_relationships || 0,
        active_pipeline: p.in_pipeline || 0,
        pipeline_value: p.pipeline_value || 0,
        conversion_rate: 0,
        temperature_dist: { hot: p.hot || 0, warm: p.warm || 0, cool: p.cool || 0, cold: p.cold || 0 },
        overdue_count: p.overdue_for_contact || 0,
        recommended_touch_days: p.recommended_touch_frequency_days || 14,
        avg_days_to_convert: 60,
        effective_proof_points: [],
        effective_language: [],
        top_objections: [],
        ineffective_approaches: [],
        cultural_notes: {}
      }));
    }

    if (services.length === 0) {
      const { data } = await supabase.from('v_service_traction').select('*');
      services = (data || []).map(s => ({
        id: s.service_id,
        display_name: s.display_name,
        category: s.category,
        pipeline_value: s.pipeline_value || 0,
        pipeline_stages: {
          mentioned: s.mentioned || 0,
          curious: s.curious || 0,
          evaluating: s.evaluating || 0,
          ready_to_buy: s.ready_to_buy || 0
        },
        win_rate: 0,
        avg_deal_size: 0,
        best_personas: [],
        winning_differentiators: [],
        top_objections: [],
        key_proof_points: []
      }));
    }

    const competitors = (competitorsRes.data || []).map(c => ({
      name: c.competitor_name,
      type: c.competitor_type,
      mentions: c.mention_count || 0,
      win_rate_against: c.win_rate_against || 50,
      perceived_strengths: c.perceived_strengths || [],
      perceived_weaknesses: c.perceived_weaknesses || [],
      winning_differentiator: c.differentiator_that_worked || 'Our integrated approach'
    }));

    const objectionPatterns = (objectionsRes.data || []).map(o => ({
      type: o.objection_type,
      count: o.occurrence_count || 0,
      overcome_rate: o.overcome_rate || 0,
      common_text: o.most_common_objection || '',
      winning_responses: []
    }));

    return {
      personas,
      services,
      competitors,
      objection_patterns: objectionPatterns
    };
  } catch (error) {
    console.error('Error fetching intelligence data:', error);
    return getMockIntelligenceData();
  }
}

/**
 * Update push status for an item
 */
export async function updatePushStatus(table, id, status) {
  if (!supabase) {
    console.log(`[Mock] Would update ${table}/${id} to status: ${status}`);
    return { success: true };
  }

  const { error } = await supabase
    .from(table)
    .update({
      push_status: status,
      push_decided_at: new Date().toISOString()
    })
    .eq('id', id);

  if (error) throw error;
  return { success: true };
}

/**
 * Push item to Asana (creates task)
 */
export async function pushToAsana(item) {
  // For now, just update the push_status
  // Full Asana integration would use the Asana API
  console.log('[Asana] Would create task for:', item);

  if (!supabase) {
    console.log('[Mock] Would push to Asana:', item);
    return { success: true };
  }

  // Update the item's push status
  const { error } = await supabase
    .from(item.table)
    .update({
      push_status: 'pushed',
      push_decided_at: new Date().toISOString()
    })
    .eq('id', item.id);

  if (error) throw error;

  // Log the push
  await supabase.from('push_log').insert({
    source_table: item.table,
    source_id: item.id,
    pushed_by: 'dashboard',
    push_type: 'manual'
  });

  return { success: true };
}

/**
 * Mark a commitment as resolved/completed
 */
export async function resolveCommitment(id) {
  if (!supabase) {
    console.log(`[Mock] Would resolve commitment ${id}`);
    return { success: true };
  }

  const { error } = await supabase
    .from('commitments')
    .update({
      status: 'completed',
      completed_at: new Date().toISOString()
    })
    .eq('id', id);

  if (error) throw error;
  return { success: true };
}

/**
 * Save objection response to playbook
 */
export async function saveToPlaybook(objection) {
  console.log('[Playbook] Saving objection pattern:', objection);
  // This would update the objection with successful response patterns
  return { success: true };
}

/**
 * Log a reach-out action for a cooling relationship
 */
export async function logReachOut(relationshipId) {
  if (!supabase) {
    console.log(`[Mock] Would log reach out for ${relationshipId}`);
    return { success: true };
  }

  // Update last interaction date to today
  const { error } = await supabase
    .from('relationships')
    .update({
      last_interaction_date: new Date().toISOString().split('T')[0],
      temperature: 'warm'
    })
    .eq('id', relationshipId);

  if (error) throw error;
  return { success: true };
}

// Mock data for development without Supabase
function getMockActionData() {
  return {
    pending: {
      relationships: [],
      service_interests: [],
      commitments_ours: [],
      commitments_theirs: [],
      objections: [],
      signals: []
    },
    attention: {
      cooling: [],
      overdue_ours: [],
      overdue_theirs: []
    }
  };
}

function getMockIntelligenceData() {
  return {
    personas: [],
    services: [],
    competitors: [],
    objection_patterns: []
  };
}
