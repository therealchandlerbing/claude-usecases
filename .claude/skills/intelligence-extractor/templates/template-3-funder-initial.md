# Template 3: Funder Initial Contact

**When to Use:** First conversation with potential funding source

**Version:** 1.0
**Template ID:** template-3

---

## Context Requirements

Provide:
- Funder organization name
- Program name (if specific)
- Funder type (Foundation/Impact Investor/Government/Corporate)
- Meeting type (Cold outreach/Warm introduction/They reached out)
- Introducer (if warm intro)
- Date and participants

---

## Extraction Priorities

### 1. Program Fit Assessment (CRITICAL)

Extract:
- **What do they actually fund?** (beyond website copy)
- **What are they looking for right now?** (current priorities)
- **Who have they funded recently?** (comparable organizations mentioned)
- **What are they NOT funding?** (exclusions, restrictions)
- **Geographic restrictions** or preferences
- **Issue area focus** and boundaries
- **Types of organizations** preferred (size, stage, approach)

### 2. Decision Process Intelligence (HIGH PRIORITY)

Capture:
- **Application stages**: LOI? Full proposal? Site visit? Pitch? Other?
- **Decision timeline**: When do they review? How often? Board meeting schedule?
- **Key decision-makers**: Board? Committee? Program officer discretion? Executive director?
- **Success rate signals**: How competitive? High bar? Open to new grantees?
- **Review criteria**: What do they actually evaluate on?

### 3. What They Really Care About (HIGH PRIORITY)

Beyond stated priorities:
- **Questions they ask repeatedly** reveal true interests
- **Topics that generate energy** vs. topics that don't
- **Evidence preferences**: Stories? Data? Research? Case studies? Community voice?
- **Innovation appetite**: Want proven approaches or experimental?
- **Systems change vs. programmatic focus**
- **Community voice expectations**: Authentic participation valued or nice-to-have?
- **Metrics orientation**: What do they measure? How?

### 4. Relationship & Political Intelligence

Observe:
- **Program officer's role**: Champion? Gatekeeper? Administrator? Influencer?
- **Board dynamics hints**: Who really decides? Rubber stamp or active?
- **Peer organization relationships**: Who do they fund/respect/avoid?
- **Unofficial guidance**: What did they say "off the record" or hint at?
- **Responsiveness**: Fast to reply? Slow? Detailed responses?
- **Helpfulness**: Generous with guidance? Cryptic? Encouraging?

### 5. Application Strategy Intelligence

Determine:
- **Budget range appropriate**: Too small for them? Too big? Just right?
- **Overhead/indirect policies**: Restrictions mentioned? Limits? Flexibility?
- **Multi-year possibility**: Do they do it? How to position?
- **Partnership expectations**: Want collaboration with others? Solo applicants preferred?
- **Reporting burden**: Heavy? Light? Specific requirements?
- **Timeline fit**: When could we apply? When would funding start?

---

## Stakeholder Extraction (Program Officer Focus)

For the program officer, capture detailed profile:

**Communication Intelligence:**
- Style: Formal? Conversational? Data-driven? Visionary? Relational?
- Responsiveness: Quick to reply? Slow? Detailed? Brief?
- Guidance generosity: Helpful and forthcoming? Cryptic? Encouraging? Neutral?
- Tone: Warm? Businesslike? Enthusiastic? Cautious?

**Power Signals:**
- Do they champion applications or just process them?
- Decision influence level: Advisory? Strong influence? Final say?
- Board relationship: Do they present to board? Recommend? Implement only?
- Language of authority: "I can..." vs. "The board decides..." vs. "We look for..."

**What They Care About:**
- Topics that generate energy
- Questions they ask repeatedly
- Evidence they request
- Organizations they mention admiringly

---

## Pattern Recognition

### Look for these FUNDER patterns:

**Positioning Guidance:**
- "Organizations like yours typically..." → How they see us, how to position
- "The board really cares about..." → True decision priorities beyond stated goals
- "We funded [org] last year because..." → What actually wins
- "Successful applicants usually..." → Template for success

**Fit Signals:**
- "This aligns perfectly with..." → Strong fit
- "We don't usually fund..." → Red flag, restriction
- "That's outside our focus but..." → Boundary testing
- "Tell me more about..." → Genuine interest area

**Decision Process Clues:**
- "We review applications in [month]" → Timeline
- "The board meets..." → Decision rhythm
- "Typically we require..." → Process steps
- "I present to the committee..." → Who really decides

**Competitive Landscape:**
- "We get a lot of applications for..." → Highly competitive
- "We're specifically looking for..." → Less competitive, targeted
- "We funded [similar org]..." → Direct comparison/competition
- "Most applicants propose X, but we'd like to see Y..." → Differentiation opportunity

**Relationship Building:**
- Offers of additional guidance → Wants to help you succeed
- Suggests intro to colleagues/board → Strong interest
- Proposes site visit → Serious consideration
- "Feel free to reach out with questions" → Open door

### Look for these RED FLAGS:

**Mission Misalignment:**
- Disinterest in core aspects of your work
- Questions suggesting they don't understand your approach
- Mismatch on values (community voice, equity, etc.)

**Process Red Flags:**
- Reporting burden seems disproportionate to grant size
- Intellectual property restrictions or approach mandates
- Geographic/constituency requirements you can't meet
- Timeline doesn't align with your capacity

**Relationship Red Flags:**
- Unresponsive or slow to follow up
- Cryptic or unhelpful when asked for guidance
- Signals they prefer different organization types
- Past grantees very different from your org

### Look for these GREEN FLAGS:

**Strong Fit:**
- Excitement about your approach
- "This aligns perfectly with our priorities"
- Specific encouragement to apply
- Proactive offers of help

**Relationship Promise:**
- Responsive and helpful
- Generous with time and guidance
- Introduction to other staff or board
- Site visit offer or interest in learning more

**Decision Positioning:**
- Clear path to funding described
- Timeline works for both
- Budget range appropriate
- "I'll be presenting this to the board" language

---

## Output Requirements

Generate:

1. **Funding Intelligence** object:
   - Confidence: medium or high
   - Action: create_new
   - Comprehensive fit assessment
   - Decision process as detailed as possible
   - Positioning strategy based on conversation

2. **Stakeholder Intelligence** for program officer:
   - Detailed profile
   - Communication style and preferences
   - Power and influence assessment
   - What they care about

3. **Flag for review if**:
   - Unclear fit (mixed signals)
   - Conflicting signals about eligibility
   - Significant restrictions that may be dealbreakers
   - Need for strategic decision on whether to pursue

---

## Confidence Calibration

**High Confidence (75-100%):**
- Clear program description and fit assessment possible
- Detailed decision process explained
- Program officer forthcoming with information
- Specific guidance provided
- Timeline and budget range clear

**Medium Confidence (50-74%):**
- General program understanding
- Some decision process details
- Program officer helpful but not comprehensive
- Some ambiguity on fit or process
- Timeline or budget range partially clear

**Low Confidence (<50%):**
- Brief or surface conversation
- Vague about program or process
- Program officer cryptic or unhelpful
- Significant unknowns about fit
- Should be flagged for more research

---

## Cultural Context Notes

### Foundation vs. Impact Investor vs. Government

**Foundations:**
- Often relationship-driven (especially smaller family foundations)
- Board decision-making (program officer presents and recommends)
- Values and mission alignment critical
- Timeline: usually slower, board meeting schedule dependent
- Language: "grantmaking", "philanthropic priorities", "mission alignment"

**Impact Investors:**
- Financial sustainability focus
- Dual bottom line (social impact + financial return)
- Due diligence process (more like business investment)
- Timeline: can be faster or slower depending on fund
- Language: "portfolio", "investees", "theory of change", "impact metrics", "exit strategy"

**Government Programs:**
- Compliance and criteria-heavy
- Less relationship-driven, more process-driven
- Clear eligibility requirements
- Timeline: bureaucratic (can be very slow)
- Language: "eligible applicants", "compliance", "deliverables", "reporting requirements"

**Corporate Partnerships:**
- Strategic alignment with business goals
- Efficiency and ROI oriented
- Decision-making can be fast if executive champion
- Timeline: varies widely
- Language: "partnership", "shared value", "strategic alignment", "impact measurement"

---

## Example Extraction

**Source:**
> Call with James Peterson, Program Officer at Foundation for Educational Change
> Re: Systems Innovation in Education Grant Program
> Warm introduction from Maria Silva (InovaEduK)
>
> They fund $250K-$1M grants for systems-change work in education, focusing on Latin America and US. Current priority is work that bridges international learning - "not importing US models to the Global South, but genuine cross-pollination." Interested in our community-driven approach but want to see more impact data from past work.
>
> Application: LOI due June 1 (5 pages max), then selected applicants invited for full proposal. Board meets in September for decisions, funding starts January 2026. About 15% success rate (competitive).
>
> James suggested scheduling a site visit in April to see our work firsthand - "helps me make a stronger case to the board." He mentioned the board (8 members, mostly educators and community leaders) really cares about sustainability plans beyond grant period.
>
> Referenced Instituto Natura as example of past grantee they loved - community engagement approach, rigorous evaluation, sustained impact. He was very helpful - responded to my follow-up email same day with additional resources.
>
> One concern: They typically fund organizations with 5+ years track record and we're only 3 years. But James said, "If the approach is strong and the team is experienced, we can be flexible. The work matters more than organizational age."

**Output:**

```json
{
  "extraction_summary": "Strong initial conversation with Foundation for Educational Change. Good mission fit, interested in our approach. Competitive process (15% success rate) but program officer supportive. Site visit offered. Timeline: LOI June 1, decision September, funding January 2026.",

  "intelligence_items": [
    {
      "type": "funding",
      "confidence": "high",
      "action": "create_new",
      "funder_name": "Foundation for Educational Change",
      "program_name": "Systems Innovation in Education Grant Program",
      "program_officer": "James Peterson",
      "funder_type": "Foundation",
      "funding_amount_range": "$250K-$1M",
      "application_deadline": "2025-06-01",
      "decision_expected": "2025-09-30",
      "decision_timeline": "Standard (2-4 months)",
      "decision_intelligence": {
        "process": "LOI (5 pages max) due June 1 → Selected applicants invited to full proposal → Board meeting September → Decision → Funding starts January 2026",
        "decision_makers": "Board of 8 members (mostly educators and community leaders). James presents and recommends. Board makes final decision.",
        "success_rate_signals": "15% success rate - highly competitive. James offering site visit suggests we're in serious consideration for that 15%.",
        "past_patterns": "Past grantees like Instituto Natura valued for: community engagement, rigorous evaluation, sustained impact. This reveals what board values."
      },
      "positioning_strategy": {
        "how_to_frame": "Frame as 'genuine cross-pollination' not 'US model export' or 'Global South as recipients'. Emphasize community-driven approach (like Instituto Natura). Highlight rigorous evaluation and sustainability plan.",
        "evidence_needed": "Need more impact data from past work (James mentioned this). Need to show: community engagement depth, evaluation rigor, sustainability beyond grant, experienced team despite young org.",
        "differentiation": "International bridge-building (Brazil-US), community-driven not top-down, experienced team in young organization, systems-change orientation not programmatic"
      },
      "requirements_mentioned": [
        "LOI: 5 pages maximum, due June 1",
        "Impact data from past work",
        "Sustainability plan beyond grant period",
        "Site visit (offered for April)",
        "Full proposal (if selected after LOI)",
        "Organizational track record (typically 5+ years, but flexible)"
      ],
      "red_flags": [
        "Competitive (15% success rate - need strong application)",
        "Organizational age concern (they prefer 5+ years, we're 3 years - but James said flexible if approach/team strong)"
      ],
      "success_factors": [
        "James offering site visit (April) - strong signal, helps him make case to board",
        "Warm introduction from Maria Silva (InovaEduK) - she's credible reference",
        "Community-driven approach aligns with their values (Instituto Natura example)",
        "International cross-pollination focus matches our Brazil-US work",
        "James is responsive and helpful (same-day email reply, proactive guidance)",
        "Experienced team can offset young org concern"
      ],
      "fit_assessment": {
        "mission_alignment": "Excellent - systems change in education, international learning, community-driven",
        "geographic_fit": "Perfect - they fund Latin America and US, we work Brazil-US",
        "capacity_match": "Need to strengthen: more impact data, sustainability plan. Have: experienced team, strong approach, community engagement",
        "values_alignment": "Strong - they value community engagement, cross-pollination not extraction, sustained impact, rigorous evaluation"
      },
      "interaction_notes": "First call, very positive. James is knowledgeable, helpful, responsive. Offered site visit (strong interest signal). Acknowledged org age concern but opened door ('work matters more than organizational age'). Referenced Instituto Natura as model - community engagement, evaluation, sustained impact. Board cares about sustainability. Competitive but we have strong positioning. Warm intro from Maria Silva helps.",
      "next_actions": [
        "Schedule site visit for April (James offered)",
        "Strengthen impact data from past work (James noted need)",
        "Draft sustainability plan (board priority)",
        "Research Instituto Natura approach (model grantee)",
        "Prepare LOI for June 1 deadline",
        "Follow up with James re: site visit scheduling"
      ],
      "application_owner": "Chandler"
    },
    {
      "type": "stakeholder",
      "confidence": "high",
      "action": "create_new",
      "full_name": "James Peterson",
      "organization": "Foundation for Educational Change",
      "title_role": "Program Officer",
      "stakeholder_type": "Funder Contact",
      "communication_style": "Collaborative & Inclusive",
      "communication_preferences": {
        "meeting_format": "Video Comfortable",
        "response_time": "Very Fast (<24hrs)",
        "language_preference": "English",
        "preparation_needs": "Responsive to questions, provides resources proactively"
      },
      "cultural_context": "US Nonprofit",
      "cultural_communication_notes": {
        "relationship_building_pace": "Moderate - willing to invest in relationship (site visit offer) but also efficient",
        "formality_level": "Informal but professional",
        "time_orientation": "Timeline-focused (clear deadlines) but relationship-oriented (site visit)",
        "decision_making_culture": "Consultative - presents to board, but his recommendation matters"
      },
      "decision_authority": "Strong Influence",
      "decision_making_intelligence": {
        "decision_style": "He presents to board and recommends. Board makes final call, but his advocacy matters ('helps me make stronger case to board'). Data-driven but also values relationship and site visits.",
        "information_needs": "Impact data, sustainability plans, community engagement evidence, evaluation rigor, team experience",
        "risk_tolerance": "Moderate - will champion good work even if org is young ('work matters more than organizational age') but needs strong case",
        "timeline_patterns": "Follows foundation rhythm - board meeting schedule drives decisions"
      },
      "what_they_care_about": [
        "Genuine cross-pollination (not US-centric approaches imposed on Global South)",
        "Community-driven work (referenced Instituto Natura's community engagement)",
        "Rigorous evaluation and impact data",
        "Sustainability beyond grant period",
        "Systems change not programmatic quick fixes",
        "Experienced teams and strong approaches"
      ],
      "power_dynamics_awareness": "High (language about 'not importing US models' suggests awareness of North-South dynamics)",
      "systems_change_orientation": "Deep Systems Thinker",
      "relationship_stage": "Building Trust",
      "strategic_value": {
        "level": "high",
        "reasoning": "Program officer for foundation funding $250K-$1M in our exact focus area. Responsive, helpful, offering site visit. His advocacy to board matters significantly. Strong potential funding source."
      },
      "do_list": [
        "Respond quickly to his requests (he's very responsive, match that)",
        "Prepare well for site visit (critical for his board advocacy)",
        "Provide impact data and evidence he can use to make case",
        "Frame work as cross-pollination not extraction",
        "Emphasize community engagement and sustainability"
      ],
      "dont_list": [
        "Don't position as 'US model' being exported",
        "Don't underestimate board's role (he influences but doesn't decide alone)",
        "Don't skip sustainability planning (board priority)"
      ],
      "interaction_notes": "First call. Very helpful and encouraging. Offered site visit proactively. Responsive (same-day email). Knowledgeable about field. Aware of power dynamics in international development. Values community engagement, evaluation, sustainability. Will champion us to board if we build strong case.",
      "next_actions": [
        "Schedule April site visit with James",
        "Send any follow-up materials he requested"
      ],
      "relationship_owner": "Chandler"
    }
  ],

  "flagged_for_review": [],

  "extraction_metadata": {
    "source_type": "meeting_transcript",
    "source_date": "2025-03-12",
    "participants": ["Chandler Bing (360)", "James Peterson (Foundation for Educational Change, Program Officer)"],
    "meeting_type": "Funder Initial Contact - Warm Introduction",
    "language": "english",
    "cultural_context": "US Foundation context - board-driven decision-making, relationship-building valued, evidence-based"
  },

  "cross_references": [
    {
      "type": "stakeholder_to_funding",
      "from": "James Peterson",
      "to": "Foundation for Educational Change - Systems Innovation Grant",
      "relationship": "Program Officer, will present to board and advocate"
    },
    {
      "type": "funder_to_partnership",
      "from": "Foundation for Educational Change",
      "to": "InovaEduK (Maria Silva provided warm introduction)",
      "relationship": "Maria Silva made warm introduction - she's credible reference, likely past grantee or known to them"
    }
  ]
}
```

---

This template ensures comprehensive intelligence capture from initial funder conversations, supporting strategic decision-making about whether and how to pursue funding opportunities.
