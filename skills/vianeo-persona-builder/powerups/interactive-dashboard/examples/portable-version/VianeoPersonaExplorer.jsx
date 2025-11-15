import React, { useState } from 'react';

export default function VianeoPersonaExplorer() {
  const [activePersona, setActivePersona] = useState(null);
  const [activeLayer, setActiveLayer] = useState(null);

  const personaTypeColors = {
    partner: { border: '#64748b', accent: '#f8fafc', stat: '#475569', subtle: '#e2e8f0' },
    innovator: { border: '#059669', accent: '#f0fdf4', stat: '#047857', subtle: '#d1fae5' },
    stakeholder: { border: '#7c3aed', accent: '#faf5ff', stat: '#6d28d9', subtle: '#e9d5ff' },
    beneficiary: { border: '#d97706', accent: '#fffbeb', stat: '#b45309', subtle: '#fde68a' }
  };

  const validationStatusConfig = {
    validated: { label: 'Validated', color: '#059669', bgColor: '#d1fae5', icon: '✓' },
    inferred: { label: 'Not Yet Validated', color: '#dc2626', bgColor: '#fee2e2', icon: '⚠' },
    hybrid: { label: 'Partially Validated', color: '#d97706', bgColor: '#fef3c7', icon: '◐' }
  };

  const personas = {
    'university-partner': {
      type: 'partner',
      title: 'Research University Tech Transfer Office',
      subtitle: 'Major Brazilian public university with 850+ active patents',
      validationStatus: 'validated',
      interviewCount: 8,
      qualityScore: 5,
      evidenceSummary: 'Based on 8 stakeholder interviews, 12 partnership meetings, and 14 months of engagement tracking',
      layers: [
        { id: 'layer1', number: '1', title: 'Requester', subtitle: 'Who They Are' },
        { id: 'layer2', number: '2', title: 'Field of Application', subtitle: 'Their World' },
        { id: 'layer3', number: '3', title: 'Activities & Challenges', subtitle: 'What They Do' },
        { id: 'layer4', number: '4', title: 'Current Solutions', subtitle: 'Present Reality' }
      ]
    },
    'early-innovator': {
      type: 'innovator',
      title: 'Academic Researcher Seeking Commercialization',
      subtitle: 'PhD researcher with novel biotech platform, 6+ years development',
      validationStatus: 'hybrid',
      interviewCount: 5,
      qualityScore: 4,
      evidenceSummary: 'Based on 5 researcher interviews, 8 months direct engagement, and project documentation review',
      layers: [
        { id: 'layer1-i', number: '1', title: 'Requester', subtitle: 'Who They Are' },
        { id: 'layer2-i', number: '2', title: 'Field of Application', subtitle: 'Their World' },
        { id: 'layer3-i', number: '3', title: 'Activities & Challenges', subtitle: 'What They Do' },
        { id: 'layer4-i', number: '4', title: 'Current Solutions', subtitle: 'Present Reality' }
      ]
    },
    'small-business': {
      type: 'stakeholder',
      title: 'Small Business Owner',
      subtitle: 'Boutique marketing agency, 12 employees, 5 years operation',
      validationStatus: 'validated',
      interviewCount: 12,
      qualityScore: 5,
      evidenceSummary: 'Based on 12 small business owner interviews and 6 months of operational observation',
      layers: [
        { id: 'layer1-sb', number: '1', title: 'Requester', subtitle: 'Who They Are' },
        { id: 'layer2-sb', number: '2', title: 'Field of Application', subtitle: 'Their World' },
        { id: 'layer3-sb', number: '3', title: 'Activities & Challenges', subtitle: 'What They Do' },
        { id: 'layer4-sb', number: '4', title: 'Current Solutions', subtitle: 'Present Reality' }
      ]
    }
  };

  const layerContent = {
    'layer1': {
      title: 'Layer 1: Requester (Who They Are)',
      fields: [
        { label: 'First Name', content: 'Dr. Maria', source: 'Interview #1, #3, #5' },
        { label: 'Age', content: '47', source: 'Interview #1' },
        {
          label: 'Life/Motivations',
          content: 'Leads the technology transfer office at a major public research university in São Paulo with 850+ active patents and 40 annual technology disclosures. Transitioned to this role five years ago after 15 years as tenured faculty in materials science. Success means increasing commercialization from current 12% to 25% while maintaining the university\'s constitutional mandate to serve Brazilian society. Personally motivated by seeing research impact beyond academic papers after watching her own doctoral work gather dust for a decade.',
          source: 'Interview #1, #2, #5'
        },
        {
          label: 'Personality/Values',
          content: 'Highly strategic and relationship-focused, believing successful partnerships take 18-24 months to build properly and can\'t be rushed. Values radical transparency over polished presentations, becoming immediately skeptical when potential partners lead with aggressive IP acquisition terms rather than collaborative development frameworks. Makes decisions by consensus-building across faculty inventors, university administration, and partner organizations, even when it slows timelines.',
          source: 'Interview #1, #3, #5, Meeting observations'
        }
      ],
      quotes: [
        {
          text: 'Our researchers didn\'t spend six years developing breakthrough materials just to see them locked in a patent portfolio. We need partners who understand the social impact potential and will develop it with Brazilian communities in mind, not extract IP and manufacture elsewhere.',
          author: 'Dr. Maria, Interview #1',
          source: 'Interview March 2024'
        }
      ]
    },
    'layer2': {
      title: 'Layer 2: Field of Application (Their World)',
      fields: [
        {
          label: 'Thinks/Feels',
          content: 'Constantly wrestling with pressure from university administration to show increasing commercialization metrics (currently at 12%, pressure to reach 20%) while protecting decades-old faculty relationships that could be damaged by aggressive commercialization push. Frustrated when spending 6 hours preparing for partnership meetings only to discover within 15 minutes that the partner wants exclusive global IP rights with minimal development commitment. Anxious about competitors (other Brazilian universities) closing deals faster while she maintains rigorous vetting processes.',
          source: 'Interview #2, #5, #7'
        },
        {
          label: 'Observes',
          content: 'Watches peer universities rush into partnerships that look impressive in press releases but collapse within 18 months due to misaligned expectations, leaving bitter faculty who refuse future commercialization attempts. Sees the same three international tech scouting firms recycling the same partnership templates across Latin America without adapting to local contexts. Notes that successful long-term partnerships always start with 3-6 months of relationship-building before any commercial discussions, but most potential partners expect term sheets within 30 days.',
          source: 'Interview #1, #3, #6'
        },
        {
          label: 'Does',
          content: 'Spends 16 hours weekly building informal relationships with potential partners before formal discussions (coffee meetings, conference conversations, facility tours). Maintains detailed tracking spreadsheet of 47 active partnership conversations, noting relationship temperature, decision-makers met, faculty inventor engagement level, and cultural fit indicators. Holds monthly "commercialization readiness" sessions with faculty inventors to set expectations about partnership timelines and typical negotiation points. Reviews every partnership agreement personally, often pushing back on university legal team\'s standard templates to preserve relationship-building flexibility.',
          source: 'Interview #2, #4, Calendar analysis'
        },
        {
          label: 'Others Say',
          content: 'Faculty inventors describe her as "protective like a mother bear" of their research but sometimes wish she would "just close a deal already" when promising partners appear. University administration publicly praises her relationship-building approach while privately pressuring her to show more commercialization numbers in quarterly reports. International partners appreciate her transparency but admit they sometimes lose patience with the 90-120 day decision cycles. Former partners consistently cite her as the reason they\'re willing to consider additional university technologies.',
          source: 'Interview #3, #6, #8, Partner feedback'
        }
      ],
      quotes: [
        {
          text: 'When I explain to US partners that we need three months to get faculty alignment before signing anything, they think we\'re being difficult or bureaucratic. But I\'ve seen what happens when you skip that step. You end up with a signed contract and a faculty inventor who sabotages the partnership because they never really bought in. That\'s how you build partnerships that last 10 years, not partnerships that look good in a press release.',
          author: 'Dr. Maria, Interview #3',
          source: 'Interview April 2024'
        }
      ]
    },
    'layer3': {
      title: 'Layer 3: Activities & Challenges (What They Do and Struggle With)',
      sections: [
        {
          label: 'Tasks/Activities',
          items: [
            'Evaluate 40+ new technology disclosures annually for commercialization potential, social impact alignment, and market readiness (requires 3-4 hours per technology)',
            'Build and maintain relationships with 30-45 potential partner organizations globally, requiring 8-12 international trips annually and 20+ hours weekly on video calls across time zones',
            'Coordinate between faculty inventors (who speak science), university administration (who speak metrics), and external partners (who speak market opportunity), translating between three different languages',
            'Review and negotiate partnership agreements ensuring IP protection, fair valuation, development milestones, and social impact commitments, typically 6-8 weeks per agreement with 15+ revision cycles',
            'Track portfolio progress across 23 active partnerships and report metrics to university leadership quarterly, requiring manual data collection from multiple sources taking 40+ hours per quarter'
          ]
        },
        {
          label: 'Pains/Lacks',
          items: [
            'No systematic way to assess which partners are genuinely committed (invest real resources) vs. exploring options (just collecting information), leading to 40% of partnership time spent on non-serious prospects',
            'Faculty inventors often lack business context and realistic expectations, requiring 8-12 hours of education per inventor before partnership discussions can begin productively',
            'University bureaucracy creates 90-120 day decision cycles from initial interest to signed agreements, losing 30-40% of impatient partners who move to competitors',
            'Limited budget ($50K annually) for market validation and proof-of-concept work, forcing reliance on partner resources which creates misaligned incentives and power imbalances',
            'Difficulty finding partners who understand both the technology complexity and Brazilian market context, resulting in either tech-savvy partners with no local expertise or local partners lacking technical depth',
            'No objective framework for qualifying partnership readiness, leading to inconsistent decisions that faculty inventors perceive as arbitrary or politically motivated'
          ]
        },
        {
          label: 'Expectations/Hopes',
          items: [
            'Reduce time spent on non-serious partners from 40% to under 15% by implementing better qualification frameworks that identify genuine commitment signals early',
            'Increase faculty engagement with commercialization from current 30% participation to 60% by demonstrating repeatable success patterns and protecting faculty interests',
            'Find or create validation frameworks that both university stakeholders and external partners trust and respect, eliminating the current "trust me" approach',
            'Build 3-5 repeatable partnership models (templates, processes, expectations) that don\'t require reinventing everything for each technology or partner',
            'Double commercialization rate from 12% to 25% over 3 years while maintaining 100% social impact alignment and faculty satisfaction scores above 4.2/5',
            'Establish the university as the preferred Latin American partner for ethical technology commercialization, attracting higher-quality partners proactively rather than constantly outbound hunting'
          ]
        }
      ],
      quotes: [
        {
          text: 'I spend somewhere between 200-250 hours per quarter on partnerships that go absolutely nowhere because the partner was never really committed, they were just doing market research on our dime. I need better ways to qualify serious partners in the first 2-3 conversations, not after 6 months of work. If I could cut that wasted time in half, I could double our actual partnership output.',
          author: 'Dr. Maria, Interview #5',
          source: 'Interview July 2024'
        }
      ]
    },
    'layer4': {
      title: 'Layer 4: Current Solutions (Their Present Reality)',
      content: 'Currently uses a fragmented system cobbling together: (1) informal relationship-building through conferences and warm introductions, requiring 15+ hours weekly but producing inconsistent results; (2) manual technology assessment spreadsheets tracking 40+ metrics per technology, requiring constant updates and prone to version control chaos when multiple team members edit; (3) ad-hoc partnership processes that vary significantly by partner type, technology category, and deal complexity, making it impossible to train new team members or scale operations. The university\'s legal team handles contract negotiations using 15-year-old templates designed for equipment purchases, requiring 20-30 hours of customization per partnership and creating friction with modern partnership structures. Technology validation happens exclusively through partner-funded pilots or research grants, creating problematic incentive misalignments where partners control validation processes and outcomes. This approach works reasonably well for the 8-10 established relationships built over 3-5 years (65% success rate) but completely breaks down when trying to scale to new partners who don\'t have years of trust built up (15% success rate). The system is held together entirely by Maria\'s personal network, institutional knowledge, and 60-hour work weeks, making it completely non-transferable and unsustainable.',
      source: 'Interview #2, #4, #6, Process documentation, Time tracking data',
      gaps: [
        'No systematic partner qualification framework that identifies serious prospects within first 2-3 interactions rather than after months of investment',
        'No standardized technology validation methodology that both university and external partners view as credible and objective',
        'No scalable partnership templates beyond basic legal agreements, each deal requires complete custom negotiation taking 6-8 weeks',
        'No objective metrics for assessing partnership readiness or technology-market fit beyond subjective judgment',
        'No knowledge management system, everything exists in Maria\'s head and personal spreadsheets making succession planning impossible',
        'No partner relationship management system, tracking 47 active conversations across email, WhatsApp, LinkedIn, and paper notes'
      ],
      quotes: [
        {
          text: 'We have spreadsheets and email threads and my personal notes from 100+ conversations, but nothing that gives us or our partners a clear, objective view of where a technology actually stands in terms of validation, market readiness, or partnership fit. It\'s all relationship-based and judgment-based, which is fine when you have years to build trust, but it absolutely doesn\'t scale. Every new partner requires rebuilding credibility from scratch.',
          author: 'Dr. Maria, Interview #4',
          source: 'Interview May 2024'
        }
      ]
    },
    'layer1-i': {
      title: 'Layer 1: Requester (Who They Are)',
      fields: [
        { label: 'First Name', content: 'Dr. João', source: 'Interview #1, Project records' },
        { label: 'Age', content: '34', source: 'Interview #1' },
        {
          label: 'Life/Motivations',
          content: 'Recently completed PhD in biotechnology at a leading Brazilian university, developing a novel biomaterial platform during six years of doctoral research with potential medical device applications in wound healing and tissue regeneration. Currently splits time 60/40 between post-doctoral research (maintaining academic career path) and commercialization efforts. Motivated by watching previous lab innovations never reach patients despite clear clinical potential, seeing his doctoral advisor\'s 15 years of breakthrough research cited in 200+ papers but never commercialized. Success means seeing his technology help actual patients while maintaining academic credibility for faculty position applications.',
          source: 'Interview #1, #2'
        },
        {
          label: 'Personality/Values',
          content: 'Scientifically rigorous and deeply skeptical of business processes that seem to oversimplify complex technologies or make claims beyond what data supports. Values intellectual honesty to the point of self-sabotage, becoming visibly uncomfortable when mentors suggest "softening" technical limitations in investor pitches. Makes decisions slowly and methodically, wanting to see all data before committing, which frustrates business-oriented advisors who value speed. Believes deeply that good science should serve society, not just generate publications or profits.',
          source: 'Interview #1, #3, #5'
        }
      ],
      quotes: [
        {
          text: 'I spent six years developing this technology, running 400+ experiments, publishing 8 papers, and I genuinely believe it can help thousands of patients with chronic wounds. But I don\'t know how to talk to investors or business partners without feeling like I\'m either overselling the science or underselling the opportunity. Every pitch feels like I\'m compromising something.',
          author: 'Dr. João, Interview #1',
          source: 'Interview February 2024'
        }
      ]
    },
    'layer2-i': {
      title: 'Layer 2: Field of Application (Their World)',
      fields: [
        {
          label: 'Thinks/Feels',
          content: 'Feels torn between academic career expectations (publish-or-perish, currently 2 papers per year) and commercial opportunity that could have real patient impact but provides no academic credit. Constantly worried that senior colleagues will view commercialization as "selling out" or compromising research integrity, especially after his department chair made dismissive comments about another researcher "wasting time on business stuff." Anxious about protecting intellectual property while sharing enough information to attract partners, unsure where the line is between necessary disclosure and giving away key innovations. Frustrated that he can articulate every technical nuance to scientific peers but struggles to explain value proposition in 30 seconds to business people.',
          source: 'Interview #2, #4',
          validation: 'hybrid'
        },
        {
          label: 'Observes',
          content: 'Watches other post-doctoral researchers in his network struggle with identical challenges, noting that the few who succeed in commercialization usually either have strong business co-founders (often family members) or mentors with industry experience who provide hand-holding through every step. Sees international biotech companies increasingly interested in Brazilian innovation at conferences, but notes they typically want technologies at much higher readiness levels than his current stage. Observes that researchers who pivot fully to commercialization often struggle to return to academia if the venture fails, creating real career risk that his peers discuss privately but rarely acknowledge publicly.',
          source: 'Interview #2, Meeting notes',
          validation: 'inferred'
        },
        {
          label: 'Does',
          content: 'Continues academic research 60% time (maintaining publication pipeline and lab relationships) while pursuing commercialization 40% time, creating constant time management stress and guilt about shortchanging both. Attends business development workshops and pitch events 2-3 times monthly, initially feeling like an imposter but gradually becoming more comfortable with business language while still preferring technical discussions. Responds to 5-8 partnership inquiries monthly, spending 3-4 hours per inquiry only to discover most are early-stage exploratory with no near-term commitment potential. Maintains detailed lab notebooks not just for scientific rigor but also for IP protection, adding 2-3 hours weekly of documentation overhead.',
          source: 'Interview #3, #5, Calendar data',
          validation: 'hybrid'
        },
        {
          label: 'Others Say',
          content: 'Academic advisors explicitly warn him that "spending too much time on business stuff will hurt your publication record and faculty job prospects," recommending he wait until securing tenure before commercialization. Technology transfer office appreciates his diligence and scientific rigor but privately wishes he would move faster on promising opportunities and be less perfectionist about having complete data packages. Early-stage investors describe his pitches as "too technical, we need the business case not the science lesson," while strategic corporate partners appreciate the technical depth but want more market validation before serious discussions. Friends observe he seems increasingly stressed trying to maintain both academic and commercial tracks simultaneously.',
          source: 'Interview #4, Feedback from TTO, Advisor emails',
          validation: 'inferred'
        }
      ],
      quotes: [
        {
          text: 'My doctoral advisor keeps warning me that spending time on business stuff will hurt my publication record and my chances at faculty positions. But honestly, what\'s the point of publishing if the technology never leaves the lab? I\'ve watched his 15 years of brilliant research get cited hundreds of times but help exactly zero patients. That can\'t be the only path.',
          author: 'Dr. João, Interview #2',
          source: 'Interview March 2024'
        }
      ]
    },
    'layer3-i': {
      title: 'Layer 3: Activities & Challenges (What They Do and Struggle With)',
      sections: [
        {
          label: 'Tasks/Activities',
          items: [
            'Continue post-doctoral research while pursuing commercialization (24 hours weekly on research, 16 hours weekly on business development, constant context switching)',
            'Respond to partnership inquiries (5-8 monthly) and evaluate potential collaborators against criteria he\'s still developing as he learns',
            'Attend business development workshops, pitch competitions, and networking events (2-3 monthly, requiring 8-12 hours including preparation and travel)',
            'Prepare technical documentation and presentations for non-technical audiences, requiring complete reframing of 6 years of research into 10-slide decks',
            'Seek regulatory guidance for medical device approval pathways (FDA, ANVISA), spending 10+ hours monthly navigating unfamiliar regulatory frameworks',
            'Maintain lab relationships and publication pipeline (2 papers per year minimum) to preserve academic career backup option'
          ],
          validation: 'hybrid'
        },
        {
          label: 'Pains/Lacks',
          items: [
            'No clear framework for evaluating which partnerships align with research goals (advancing science) vs. commercial goals (generating revenue), leading to analysis paralysis on partnership decisions',
            'Lacks business co-founder or experienced team to handle commercial development, market analysis, regulatory strategy, requiring him to learn everything from scratch while maintaining research',
            'Insufficient funding ($0 currently, needs $150-300K) to advance technology from bench-scale to stage where commercial partners are comfortable (partners want pilot data, but he can\'t generate it without funding)',
            'Struggles to translate technical advantages into market value propositions, can explain why biomaterial has 40% better cell adhesion but can\'t articulate what that means for patient outcomes or hospital economics',
            'Limited time (16 hours weekly) to pursue commercialization while maintaining research productivity (needs 24+ hours weekly for competitive publication rate)',
            'No network in business/investment community, every partnership conversation starts from zero credibility building',
            'Caught in validation catch-22: partners want more data before committing resources, but he needs their resources to generate that data'
          ],
          validation: 'hybrid'
        },
        {
          label: 'Expectations/Hopes',
          items: [
            'Find validation pathway that advances technology readiness without compromising scientific rigor or requiring unrealistic personal funding',
            'Identify 2-3 partners who value collaborative development over aggressive IP acquisition, willing to invest in validation stages',
            'Secure initial funding ($150-300K) that supports both continued research and commercial development without requiring equity sale or exclusive rights',
            'Build small team with business expertise (or find co-founder) without giving up control of technology direction or scientific decision-making',
            'Maintain academic credibility and publication record while building commercial value, keeping faculty position path open',
            'See technology reach clinical trials within 3-4 years, helping actual patients rather than just generating more publications',
            'Create sustainable income stream ($80-100K annually) that allows full-time focus on commercialization without financial stress'
          ],
          validation: 'inferred'
        }
      ],
      quotes: [
        {
          text: 'I need a validation process that I can trust as a scientist, with proper controls and statistical rigor, but that business people will also respect and view as credible market validation. Right now I feel like I\'m speaking completely different languages to different audiences. Scientists want p-values and confidence intervals, investors want customer interviews and market size. I need something that works for both.',
          author: 'Dr. João, Interview #4',
          source: 'Interview May 2024'
        }
      ]
    },
    'layer4-i': {
      title: 'Layer 4: Current Solutions (Their Present Reality)',
      content: 'Currently relying on university technology transfer office for partnership identification and support, but finding their process painfully slow (120+ day cycles) and overly bureaucratic, requiring 15+ approval signatures for simple partnership discussions. Using a makeshift combination of academic conferences for networking (3-4 annually, hit-or-miss for finding relevant partners), LinkedIn cold outreach (5-10 messages weekly, 10% response rate), and warm introductions from doctoral advisor and lab colleagues (most valuable but limited to academic circles). The lack of systematic validation framework means each partner conversation starts completely from scratch, requiring re-explanation of six years of research, re-proof of the technology\'s potential, and re-establishment of credibility as both scientist and potential business partner. This scattered approach generates moderate interest (5-8 inquiries monthly) but very few concrete commitments because partners universally want more validation than he can provide with current resources ($0 budget, limited lab access, no clinical partners). Attempted to use incubator program for 3 months but found the business mentors lacked biotech expertise and gave generic startup advice irrelevant to medical device commercialization. Currently stuck in classic valley of death: too advanced for academic grants (past basic research stage), too early for commercial investment (needs more validation), and lacking bridge funding or resources to get from current state to partner-ready stage.',
      source: 'Interview #2, #3, #4, Email tracking, Calendar analysis',
      validation: 'hybrid',
      gaps: [
        'No systematic partner evaluation framework that separates serious prospects (will invest real resources) from information gatherers (just exploring)',
        'No established validation pathway between academic proof-of-concept (what he has now) and commercial readiness (what partners require), leaving a $150-300K funding gap',
        'No business co-founder or team to handle commercial development, regulatory strategy, market analysis, partnership negotiations',
        'No access to funding for validation work before partnership commitments materialize (classic catch-22: need validation to get partners, need partners to fund validation)',
        'No clinical partners or hospital relationships to generate early patient data or understand real-world application requirements',
        'No regulatory expertise or guidance to navigate FDA/ANVISA pathways, which partners expect him to have figured out',
        'No credible third-party validation that gives partners confidence without requiring them to do all due diligence themselves'
      ],
      quotes: [
        {
          text: 'I\'m completely stuck in this catch-22 situation: every serious partner wants validation data before committing real resources, but I need their commitment to fund the validation work. My university can\'t help with that gap. A trusted third-party validation process that partners would respect could actually break this cycle, but I haven\'t found anything that works for medical device technologies in Brazil.',
          author: 'Dr. João, Interview #3',
          source: 'Interview April 2024'
        }
      ]
    },
    'layer1-sb': {
      title: 'Layer 1: Requester (Who They Are)',
      fields: [
        { label: 'First Name', content: 'Sarah', source: 'Interview #1, #4, #7' },
        { label: 'Age', content: '38', source: 'Interview #1' },
        {
          label: 'Life/Motivations',
          content: 'Owns a boutique marketing agency with 12 employees (mix of creative, strategy, and account management) focused on mission-driven clients in sustainability and social impact sectors. Founded the agency five years ago after leaving corporate marketing director role at Fortune 500 company, driven by desire to build something meaningful with authentic client relationships while maintaining work-life balance (she has two school-age children). Success means sustainable 20-25% annual growth, maintaining 95%+ client retention, and team satisfaction scores above 4.5/5 while working reasonable hours (targeting 45-50 hour weeks, currently at 60-65 hours). Views the agency as a 10+ year commitment, not a flip-and-sell opportunity.',
          source: 'Interview #1, #4, #7'
        },
        {
          label: 'Personality/Values',
          content: 'Highly organized and detail-oriented but increasingly overwhelmed as administrative complexity has grown faster than organizational infrastructure. Values transparency and authentic relationships with both clients (prefers honest capability discussions over overselling) and employees (shares financial performance openly, includes team in major decisions). Makes decisions based on long-term sustainability over short-term revenue, regularly turning down clients whose values don\'t align even when it means missing quarterly targets. Strong bias toward "doing it right" rather than "doing it fast," which sometimes creates bottlenecks when perfectionism isn\'t warranted.',
          source: 'Interview #1, #4, #9'
        }
      ],
      quotes: [
        {
          text: 'I left corporate life specifically to build something where I could be home for dinner with my kids and do meaningful work with clients I actually believe in. But I\'m working more hours now than I did in corporate, and it\'s all administrative stuff that doesn\'t move the needle for clients or for revenue. That\'s not what I signed up for.',
          author: 'Sarah, Interview #1',
          source: 'Interview January 2024'
        }
      ]
    },
    'layer2-sb': {
      title: 'Layer 2: Field of Application (Their World)',
      fields: [
        {
          label: 'Thinks/Feels',
          content: 'Constantly worried about dropping balls with client projects as complexity has outgrown informal tracking systems, waking up at 3 AM wondering if anyone followed up on that deliverable. Fears that continued growth will force her to choose between boutique quality that differentiates the agency and operational efficiency, watching larger competitors win pitches by showing sophisticated project dashboards she can\'t match. Frustrated that she spends 60-65% of time on administrative tasks (status updates, client check-ins, resource allocation, reporting) instead of strategic creative work that originally excited her about agency life. Anxious that her best employees (especially two senior strategists) are considering leaving because they\'re also bogged down in manual processes rather than doing creative work they were hired for.',
          source: 'Interview #1, #6, #8'
        },
        {
          label: 'Observes',
          content: 'Watches her project managers waste 12-15 hours weekly updating multiple spreadsheets that inevitably fall out of sync, leading to conflicting information and client confusion. Sees clients getting frustrated with delayed responses about project status (she aims for 24-hour response time, currently averaging 48-72 hours). Notices her best employees considering leaving because they spend too much time on administrative coordination rather than strategic creative work. Observes competitors winning new business pitches by showing real-time project dashboards and automated client portals she can\'t match, losing 3 significant opportunities in the past 6 months specifically due to perceived operational sophistication gap.',
          source: 'Interview #2, #6, #9'
        },
        {
          label: 'Does',
          content: 'Stays late every night (typically until 8-9 PM, sometimes later) updating master project tracker and reviewing status across all active projects. Manually creates weekly client reports by pulling data from five different sources (Google Sheets, Asana, email, Slack, accounting system), requiring 8-12 hours weekly and often containing errors due to manual aggregation. Holds 90-minute all-hands Monday meetings to align everyone on project status because there\'s no central visibility system, eating into productive time. Sends 40-60 individual check-in messages daily to various team members asking about specific task status because she has no other way to maintain visibility. Maintains detailed personal notes about every client interaction and project decision because nothing is systematically documented.',
          source: 'Interview #2, #4, Calendar analysis, Time tracking'
        },
        {
          label: 'Others Say',
          content: 'Clients consistently praise the agency\'s creative quality and authentic partnership approach but frequently mention communication could be smoother and updates more timely ("we love the work but sometimes feel like we\'re chasing you for basic status"). Employees respect her vision and values but privately complain about inefficient processes that waste their time ("we spend more time updating Sarah than actually doing the work"). Her business mentor (former agency owner) keeps pushing her to "systematize or stay small forever," warning that current model caps growth at 15-20 employees maximum. Former clients who left cited communication friction and perceived disorganization despite creative quality.',
          source: 'Interview #3, #7, #10, Client feedback surveys'
        }
      ],
      quotes: [
        {
          text: 'I watch larger agencies show up to pitches with these beautiful real-time dashboards and automated client portals, and I\'m still manually creating status reports in Google Docs. We do better creative work, but we look less professional in the operational stuff. I\'ve lost at least three big opportunities in the past six months specifically because we couldn\'t demonstrate operational sophistication.',
          author: 'Sarah, Interview #6',
          source: 'Interview March 2024'
        }
      ]
    },
    'layer3-sb': {
      title: 'Layer 3: Activities & Challenges (What They Do and Struggle With)',
      sections: [
        {
          label: 'Tasks/Activities',
          items: [
            'Track 15-20 concurrent client projects across different stages (strategy, creative, production, delivery), each with 3-8 individual workstreams and 5-15 deliverables',
            'Generate weekly status reports for each major client (currently 8 clients requiring weekly updates, 3 requiring daily updates), consuming 10-12 hours weekly',
            'Coordinate resources across creative team (4 people), strategy team (3 people), and account management team (3 people), requiring constant negotiation and replanning',
            'Monitor project budgets and profitability in real-time to avoid overruns (targeting 35-40% margin, currently achieving 28-32% due to scope creep and inefficiencies)',
            'Onboard new clients with consistent process including discovery, strategy, creative brief, timeline, and budget, currently requiring 15-20 hours per client and highly variable',
            'Maintain visibility into team capacity and workload to avoid burnout while maximizing utilization (targeting 75-80% billable, currently at 65-70%)',
            'Handle new business development including pitches, proposals, and relationship building (needs 10-15 hours weekly, currently only spending 5-8 hours)'
          ]
        },
        {
          label: 'Pains/Lacks',
          items: [
            'No unified view of all projects, requiring constant context switching across multiple tools and spreadsheets, leading to frequent errors and missed updates',
            'Spending 10-12 hours weekly on manual status reporting that provides no strategic value, pure administrative overhead',
            'Can\'t see resource conflicts until they become crises (typically discovering overallocation 2-3 days before deadline when it\'s too late to adjust)',
            'Missing early warning signs of projects going over budget, typically discovering budget overruns at 80-90% completion when margin is already destroyed',
            'Lack of historical data to improve estimation accuracy, repeating the same underestimation mistakes on similar projects because nothing is systematically tracked',
            'No automated client communication about project milestones or status changes, requiring manual outreach that often gets delayed when team is busy',
            'Team members updating different spreadsheets with conflicting information, creating confusion about what\'s actually current and accurate',
            'Unable to quickly answer basic questions like "what\'s our team capacity next month" or "which projects are most profitable" without hours of manual analysis'
          ]
        },
        {
          label: 'Expectations/Hopes',
          items: [
            'Reduce administrative time by at least 50% (from current 25-30 hours weekly to under 15 hours) to focus on strategic client work and business development',
            'Give clients self-service access to real-time project status, eliminating 80% of status update requests and improving client satisfaction',
            'Predict resource bottlenecks 2-3 weeks in advance instead of 2-3 days, allowing proactive planning rather than constant firefighting',
            'Automate routine status updates and milestone notifications to clients, maintaining communication quality while reducing manual effort',
            'Scale to 20-25 employees over next 18 months without adding dedicated admin staff or project managers, maintaining current team structure',
            'Maintain boutique service quality and client relationships while achieving operational efficiency of larger competitors',
            'Improve project profitability from current 28-32% to target 35-40% by catching budget overruns early and reducing internal inefficiency',
            'Make data-driven decisions about which types of projects to pursue based on historical profitability and team efficiency patterns'
          ]
        }
      ],
      quotes: [
        {
          text: 'I spend somewhere between 25-30 hours per week on pure administrative overhead, updating spreadsheets, chasing status updates, creating reports. That\'s more than half my time doing work that generates zero value for clients and zero revenue for the business. If I could cut that in half, I could either take on 30-40% more clients with the same team, or I could actually go home for dinner with my kids. Right now I\'m doing neither.',
          author: 'Sarah, Interview #4',
          source: 'Interview February 2024'
        }
      ]
    },
    'layer4-sb': {
      title: 'Layer 4: Current Solutions (Their Present Reality)',
      content: 'Currently cobbling together a fragile system using: (1) Google Sheets for master project tracking (15+ different spreadsheets that frequently fall out of sync, no single source of truth, version control chaos); (2) Asana for some task management (tried to implement 18 months ago, 3 team members use it regularly, 9 team members ignore it and work from their own systems); (3) Slack for team communication (creates information silos, important decisions buried in chat history, no systematic documentation); (4) Manual email updates for clients (time-consuming, inconsistent, often delayed when team is busy); (5) QuickBooks for budget tracking (disconnected from project management, requiring manual reconciliation consuming 6-8 hours monthly). Tried Monday.com in pilot last year but found it too expensive ($250+ monthly for needed features) and too rigid for creative agency workflows where every project is somewhat unique. The spreadsheet system technically works but breaks down whenever someone forgets to update their section (happens 2-3 times weekly), causing cascade failures in reporting and client communication. Information exists in Sarah\'s head, in individual spreadsheets, in Slack threads, in email chains, and in people\'s personal notes, making it impossible to onboard new team members efficiently (currently takes 6-8 weeks to get someone productive due to tribal knowledge problem). The system is held together by Sarah working 60-65 hour weeks and having encyclopedic memory of every project detail, completely unsustainable and non-transferable.',
      source: 'Interview #2, #4, #8, System documentation, Time tracking data',
      validation: 'validated',
      gaps: [
        'No unified project management system that works for creative workflows, everything is fragmented across 5-7 different tools',
        'No automated reporting or client dashboards, everything manually created consuming 10-12 hours weekly',
        'No resource management capability beyond Sarah\'s mental model and spreadsheet tracking, causing frequent overallocation crises',
        'No early warning system for budget overruns, typically discovering problems when 80-90% of budget is spent',
        'No historical project data or analytics to improve estimation, resource planning, or project selection decisions',
        'No systematic documentation or knowledge management, everything exists in tribal knowledge making scaling impossible',
        'No integration between project management, time tracking, and financial systems, requiring manual reconciliation'
      ],
      quotes: [
        {
          text: 'We have spreadsheets and Asana and Slack and email threads and my personal notes from client meetings, but absolutely nothing that gives us or our clients a clear, real-time view of where projects actually stand. I spend hours every week just trying to figure out current status so I can report to clients. Meanwhile competitors show up to pitches with beautiful live dashboards that automatically update. We look like amateurs despite doing better work.',
          author: 'Sarah, Interview #8',
          source: 'Interview April 2024'
        }
      ]
    }
  };

  return (
    <div style={{
      fontFamily: "'Inter', -apple-system, sans-serif",
      background: 'linear-gradient(135deg, #fafaf9 0%, #f5f5f4 100%)',
      padding: '40px 20px',
      minHeight: '100vh',
      color: '#1a1a1a'
    }}>
      <style>{`
        /* Mobile Optimizations for Vianeo Persona Explorer */

        /* Tablets and smaller (max-width: 768px) */
        @media (max-width: 768px) {
          .vianeo-container {
            padding: 24px 16px !important;
          }

          .vianeo-header h1 {
            font-size: 32px !important;
          }

          .vianeo-header-description {
            font-size: 14px !important;
          }

          .vianeo-persona-grid {
            grid-template-columns: 1fr !important;
            gap: 16px !important;
          }

          .vianeo-layer-grid {
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)) !important;
            gap: 12px !important;
          }

          .vianeo-persona-detail {
            padding: 24px !important;
          }

          .vianeo-quote-footer {
            flex-direction: column !important;
            gap: 8px !important;
            align-items: flex-start !important;
          }
        }

        /* Mobile devices (max-width: 480px) */
        @media (max-width: 480px) {
          .vianeo-container {
            padding: 20px 12px !important;
          }

          .vianeo-header {
            margin-bottom: 32px !important;
            padding-bottom: 24px !important;
          }

          .vianeo-header h1 {
            font-size: 28px !important;
          }

          .vianeo-header-description {
            font-size: 14px !important;
          }

          .vianeo-persona-card {
            padding: 20px !important;
          }

          .vianeo-persona-detail {
            padding: 20px !important;
          }

          .vianeo-layer-grid {
            grid-template-columns: 1fr !important;
          }

          .vianeo-layer-card {
            padding: 16px !important;
          }

          .vianeo-field,
          .vianeo-content-block,
          .vianeo-quote {
            padding: 16px !important;
          }

          .vianeo-section-item {
            padding: 10px 14px !important;
          }

          .vianeo-gaps-block {
            padding: 14px 16px !important;
          }
        }

        /* Very small devices (max-width: 360px) */
        @media (max-width: 360px) {
          .vianeo-container {
            padding: 16px 8px !important;
          }

          .vianeo-header h1 {
            font-size: 24px !important;
          }

          .vianeo-persona-card,
          .vianeo-persona-detail {
            padding: 16px !important;
          }
        }
      `}</style>
      <div className="vianeo-container" style={{ maxWidth: '1400px', margin: '0 auto' }}>

        {/* Header */}
        <header className="vianeo-header" style={{
          textAlign: 'center',
          marginBottom: '48px',
          paddingBottom: '32px',
          borderBottom: '2px solid #e7e5e4'
        }}>
          <div style={{
            textTransform: 'uppercase',
            letterSpacing: '3px',
            fontSize: '11px',
            fontWeight: '500',
            color: '#78716c',
            marginBottom: '12px'
          }}>Vianeo Business Validation Framework</div>

          <h1 style={{
            fontSize: '42px',
            fontWeight: '300',
            letterSpacing: '-0.5px',
            marginBottom: '16px',
            color: '#292524'
          }}>Stakeholder Persona Explorer</h1>

          <p className="vianeo-header-description" style={{
            fontSize: '16px',
            color: '#57534e',
            maxWidth: '700px',
            margin: '0 auto',
            lineHeight: '1.7'
          }}>
            Navigate through validated stakeholder personas built from research data.
            Each persona follows the Vianeo four-layer structure with evidence tracking.
          </p>
        </header>

        {/* Persona Cards */}
        <div className="vianeo-persona-grid" style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
          gap: '20px',
          marginBottom: '48px'
        }}>
          {Object.entries(personas).map(([id, persona]) => {
            const colors = personaTypeColors[persona.type];
            const validation = validationStatusConfig[persona.validationStatus];
            const isActive = activePersona === id;

            return (
              <div
                key={id}
                className="vianeo-persona-card"
                onClick={() => {
                  setActivePersona(id);
                  setActiveLayer(null);
                }}
                style={{
                  background: isActive ? colors.accent : '#ffffff',
                  border: `2px solid ${isActive ? colors.border : '#e7e5e4'}`,
                  borderRadius: '8px',
                  padding: '24px',
                  cursor: 'pointer',
                  transition: 'all 0.3s ease',
                  transform: isActive ? 'translateY(-2px)' : 'translateY(0)',
                  boxShadow: isActive ? `0 8px 24px ${colors.border}25` : '0 1px 3px rgba(0,0,0,0.08)'
                }}
              >
                {/* Badges */}
                <div style={{ display: 'flex', gap: '8px', marginBottom: '12px', flexWrap: 'wrap' }}>
                  <div style={{
                    fontSize: '10px',
                    padding: '4px 8px',
                    background: colors.subtle,
                    color: colors.stat,
                    borderRadius: '3px',
                    fontWeight: '600',
                    textTransform: 'uppercase'
                  }}>{persona.type}</div>

                  <div style={{
                    fontSize: '10px',
                    padding: '4px 8px',
                    background: validation.bgColor,
                    color: validation.color,
                    borderRadius: '3px',
                    fontWeight: '500',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '4px'
                  }}>
                    <span>{validation.icon}</span>
                    <span>{validation.label}</span>
                  </div>
                </div>

                {/* Title */}
                <div style={{
                  fontSize: '20px',
                  fontWeight: '500',
                  color: colors.border,
                  marginBottom: '6px',
                  lineHeight: '1.3'
                }}>{persona.title}</div>

                {/* Subtitle */}
                <div style={{
                  fontSize: '14px',
                  color: '#78716c',
                  marginBottom: '20px',
                  lineHeight: '1.5'
                }}>{persona.subtitle}</div>

                {/* Stats */}
                <div style={{
                  display: 'flex',
                  gap: '16px',
                  paddingTop: '16px',
                  borderTop: `1px solid ${colors.border}40`
                }}>
                  <div style={{ flex: 1 }}>
                    <div style={{
                      fontSize: '11px',
                      textTransform: 'uppercase',
                      color: '#a8a29e',
                      marginBottom: '4px'
                    }}>Interviews</div>
                    <div style={{
                      fontSize: '24px',
                      fontWeight: '300',
                      color: colors.stat
                    }}>{persona.interviewCount}</div>
                  </div>
                  <div style={{ flex: 1 }}>
                    <div style={{
                      fontSize: '11px',
                      textTransform: 'uppercase',
                      color: '#a8a29e',
                      marginBottom: '4px'
                    }}>Quality Score</div>
                    <div style={{
                      fontSize: '24px',
                      fontWeight: '300',
                      color: colors.stat
                    }}>{persona.qualityScore}/5</div>
                  </div>
                </div>
              </div>
            );
          })}
        </div>

        {/* Active Persona Detail */}
        {activePersona && personas[activePersona] && (
          <div className="vianeo-persona-detail" style={{
            background: '#ffffff',
            border: `2px solid ${personaTypeColors[personas[activePersona].type].border}`,
            borderRadius: '8px',
            padding: '32px',
            marginBottom: '32px'
          }}>
            <h2 style={{
              fontSize: '32px',
              fontWeight: '300',
              color: personaTypeColors[personas[activePersona].type].border,
              marginBottom: '12px'
            }}>{personas[activePersona].title}</h2>

            <p style={{
              fontSize: '16px',
              color: '#57534e',
              marginBottom: '20px'
            }}>{personas[activePersona].evidenceSummary}</p>

            {/* Layer Navigation */}
            <div style={{
              fontSize: '11px',
              textTransform: 'uppercase',
              letterSpacing: '1.5px',
              color: '#78716c',
              marginBottom: '16px',
              marginTop: '32px',
              fontWeight: '600'
            }}>Vianeo Four-Layer Structure</div>

            <div className="vianeo-layer-grid" style={{
              display: 'grid',
              gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
              gap: '14px',
              marginBottom: '32px'
            }}>
              {personas[activePersona].layers.map((layer) => {
                const isActiveLayer = activeLayer === layer.id;
                const colors = personaTypeColors[personas[activePersona].type];

                return (
                  <div
                    key={layer.id}
                    className="vianeo-layer-card"
                    onClick={() => setActiveLayer(layer.id)}
                    style={{
                      background: isActiveLayer ? colors.accent : '#fafaf9',
                      border: `2px solid ${isActiveLayer ? colors.border : '#e7e5e4'}`,
                      borderRadius: '6px',
                      padding: '18px',
                      cursor: 'pointer',
                      transition: 'all 0.2s ease'
                    }}
                  >
                    <div style={{
                      fontSize: '12px',
                      fontWeight: '600',
                      color: colors.stat,
                      marginBottom: '8px'
                    }}>Layer {layer.number}</div>

                    <div style={{
                      fontSize: '16px',
                      fontWeight: '500',
                      color: '#292524',
                      marginBottom: '4px'
                    }}>{layer.title}</div>

                    <div style={{
                      fontSize: '12px',
                      color: '#78716c'
                    }}>{layer.subtitle}</div>
                  </div>
                );
              })}
            </div>

            {/* Layer Content */}
            {activeLayer && layerContent[activeLayer] && (
              <div style={{ paddingTop: '20px', borderTop: '1px solid #e7e5e4' }}>
                <h3 style={{
                  fontSize: '24px',
                  fontWeight: '300',
                  color: personaTypeColors[personas[activePersona].type].border,
                  marginBottom: '20px'
                }}>{layerContent[activeLayer].title}</h3>

                {/* Fields (for Layers 1 & 2) */}
                {layerContent[activeLayer].fields && layerContent[activeLayer].fields.map((field, idx) => (
                  <div key={idx} className="vianeo-field" style={{
                    background: '#fafaf9',
                    border: '1px solid #e7e5e4',
                    padding: '18px 20px',
                    marginBottom: '12px',
                    borderRadius: '6px'
                  }}>
                    <div style={{
                      display: 'flex',
                      justifyContent: 'space-between',
                      alignItems: 'center',
                      marginBottom: '8px'
                    }}>
                      <div style={{
                        fontSize: '13px',
                        textTransform: 'uppercase',
                        color: personaTypeColors[personas[activePersona].type].stat,
                        fontWeight: '600'
                      }}>{field.label}</div>
                      {field.validation && (
                        <div style={{
                          fontSize: '10px',
                          padding: '3px 8px',
                          background: field.validation === 'validated' ? '#d1fae5' :
                                     field.validation === 'hybrid' ? '#fef3c7' : '#fee2e2',
                          color: field.validation === 'validated' ? '#059669' :
                                 field.validation === 'hybrid' ? '#d97706' : '#dc2626',
                          borderRadius: '3px',
                          fontWeight: '500'
                        }}>
                          {field.validation === 'validated' ? '✓ Validated' :
                           field.validation === 'hybrid' ? '◐ Partial' : '⚠ Inferred'}
                        </div>
                      )}
                    </div>

                    <div style={{
                      fontSize: '14px',
                      lineHeight: '1.7',
                      color: '#44403c',
                      marginBottom: '10px'
                    }}>{field.content}</div>

                    <div style={{
                      fontSize: '11px',
                      color: '#a8a29e',
                      background: '#ffffff',
                      padding: '4px 10px',
                      borderRadius: '3px',
                      display: 'inline-block'
                    }}>
                      <strong>Evidence:</strong> {field.source}
                    </div>
                  </div>
                ))}

                {/* Sections (for Layer 3) */}
                {layerContent[activeLayer].sections && layerContent[activeLayer].sections.map((section, idx) => (
                  <div key={idx} style={{ marginBottom: '28px' }}>
                    <div style={{
                      display: 'flex',
                      justifyContent: 'space-between',
                      alignItems: 'center',
                      marginBottom: '14px'
                    }}>
                      <div style={{
                        fontSize: '13px',
                        textTransform: 'uppercase',
                        letterSpacing: '1px',
                        color: '#78716c',
                        fontWeight: '600'
                      }}>{section.label}</div>
                      {section.validation && (
                        <div style={{
                          fontSize: '10px',
                          padding: '4px 10px',
                          background: section.validation === 'validated' ? '#d1fae5' :
                                     section.validation === 'hybrid' ? '#fef3c7' : '#fee2e2',
                          color: section.validation === 'validated' ? '#059669' :
                                 section.validation === 'hybrid' ? '#d97706' : '#dc2626',
                          borderRadius: '3px',
                          fontWeight: '600'
                        }}>
                          {section.validation === 'validated' ? '✓ Validated' :
                           section.validation === 'hybrid' ? '◐ Partial' : '⚠ Inferred'}
                        </div>
                      )}
                    </div>
                    {section.items.map((item, itemIdx) => (
                      <div key={itemIdx} className="vianeo-section-item" style={{
                        background: '#ffffff',
                        padding: '12px 16px',
                        marginBottom: '8px',
                        fontSize: '14px',
                        lineHeight: '1.6',
                        color: '#292524',
                        borderRadius: '4px',
                        border: '1px solid #e7e5e4'
                      }}>• {item}</div>
                    ))}
                  </div>
                ))}

                {/* Content (for Layer 4) */}
                {layerContent[activeLayer].content && (
                  <div className="vianeo-content-block" style={{
                    background: '#fafaf9',
                    border: '1px solid #e7e5e4',
                    padding: '20px',
                    marginBottom: '20px',
                    borderRadius: '6px'
                  }}>
                    <div style={{
                      fontSize: '14px',
                      lineHeight: '1.7',
                      color: '#44403c',
                      marginBottom: '12px'
                    }}>{layerContent[activeLayer].content}</div>

                    <div style={{
                      fontSize: '11px',
                      color: '#a8a29e',
                      background: '#ffffff',
                      padding: '4px 10px',
                      borderRadius: '3px',
                      display: 'inline-block'
                    }}>
                      <strong>Evidence:</strong> {layerContent[activeLayer].source}
                    </div>

                    {layerContent[activeLayer].validation && (
                      <div style={{
                        fontSize: '10px',
                        padding: '3px 8px',
                        background: layerContent[activeLayer].validation === 'validated' ? '#d1fae5' :
                                   layerContent[activeLayer].validation === 'hybrid' ? '#fef3c7' : '#fee2e2',
                        color: layerContent[activeLayer].validation === 'validated' ? '#059669' :
                               layerContent[activeLayer].validation === 'hybrid' ? '#d97706' : '#dc2626',
                        borderRadius: '3px',
                        fontWeight: '500',
                        display: 'inline-block',
                        marginLeft: '10px'
                      }}>
                        {layerContent[activeLayer].validation === 'validated' ? '✓ Validated' :
                         layerContent[activeLayer].validation === 'hybrid' ? '◐ Partial' : '⚠ Inferred'}
                      </div>
                    )}
                  </div>
                )}

                {/* Gaps (for Layer 4) */}
                {layerContent[activeLayer].gaps && (
                  <div className="vianeo-gaps-block" style={{
                    background: '#fef3c7',
                    border: '1px solid #fde68a',
                    borderLeft: '4px solid #d97706',
                    padding: '16px 20px',
                    marginBottom: '20px',
                    borderRadius: '4px'
                  }}>
                    <div style={{
                      fontSize: '12px',
                      textTransform: 'uppercase',
                      letterSpacing: '1px',
                      color: '#b45309',
                      marginBottom: '10px',
                      fontWeight: '600'
                    }}>⚠ Current Solution Gaps</div>
                    {layerContent[activeLayer].gaps.map((gap, idx) => (
                      <div key={idx} style={{
                        fontSize: '13px',
                        lineHeight: '1.6',
                        color: '#78350f',
                        marginBottom: '6px'
                      }}>• {gap}</div>
                    ))}
                  </div>
                )}

                {/* Quotes */}
                {layerContent[activeLayer].quotes && (
                  <div style={{ marginTop: '24px' }}>
                    <div style={{
                      fontSize: '13px',
                      textTransform: 'uppercase',
                      letterSpacing: '1.5px',
                      color: '#78716c',
                      marginBottom: '14px',
                      fontWeight: '600'
                    }}>Supporting Evidence</div>

                    {layerContent[activeLayer].quotes.map((quote, idx) => (
                      <div key={idx} className="vianeo-quote" style={{
                        background: '#ffffff',
                        border: '1px solid #e7e5e4',
                        padding: '18px 20px',
                        marginBottom: '10px',
                        borderRadius: '6px'
                      }}>
                        <div style={{
                          fontSize: '14px',
                          lineHeight: '1.7',
                          color: '#44403c',
                          marginBottom: '12px'
                        }}>"{quote.text}"</div>

                        <div className="vianeo-quote-footer" style={{
                          display: 'flex',
                          justifyContent: 'space-between',
                          fontSize: '12px'
                        }}>
                          <span style={{
                            color: personaTypeColors[personas[activePersona].type].stat,
                            fontWeight: '500'
                          }}>{quote.author}</span>
                          <span style={{ color: '#a8a29e' }}>{quote.source}</span>
                        </div>
                      </div>
                    ))}
                  </div>
                )}
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
