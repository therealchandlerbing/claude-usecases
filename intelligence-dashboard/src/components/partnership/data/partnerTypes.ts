export interface PartnerMetrics {
  explored: number;
  closed: number;
  successRate: number;
  avgTimeline: number;
  approach: string;
  decisionStyle: string;
}

export interface Pattern {
  text: string;
  frequency: string;
}

export interface Opportunity {
  title: string;
  description: string;
  signals: string[];
}

export interface ValueAlignment {
  frame: string[];
  cultural: string[];
  alignment: string[];
  misalignment: string[];
}

export interface QualificationSection {
  category: string;
  questions: string[];
}

export interface Hesitation {
  hesitation: string;
  response: string;
  action: string;
}

export interface Framing {
  past: string;
  new: string;
  key: string;
}

export interface SuccessPatterns {
  timeline: string;
  touchpoints: string;
  stages: string[];
  predictors: string[];
  scope: string[];
}

export interface PartnerType {
  name: string;
  subtitle: string;
  metrics: PartnerMetrics;
  patterns: Pattern[];
  opportunities: Opportunity[];
  valueAlignment: ValueAlignment;
  qualificationQuestions: QualificationSection[];
  hesitations: Hesitation[];
  framing: Framing;
  walkAway: string[];
  successPatterns: SuccessPatterns;
}

export const partnerTypes: Record<string, PartnerType> = {
  jv: {
    name: 'Joint Venture Partners',
    subtitle: 'True partnership structures (like SpacePlan, GenIP)',
    metrics: {
      explored: 8,
      closed: 2,
      successRate: 25,
      avgTimeline: 11.5,
      approach: 'Co-creation, shared equity/revenue',
      decisionStyle: 'Strategic fit over speed'
    },
    patterns: [
      { text: 'Successful JVs require 6-9 months relationship-building before structure discussions', frequency: '100%' },
      { text: 'Legal/operational complexity often underestimated (adds 3-4 months)', frequency: '85%' },
      { text: 'Best partnerships emerge from collaborative project work first', frequency: '90%' }
    ],
    opportunities: [
      {
        title: 'Complementary capability gaps',
        description: 'Partner has expertise/assets 360 lacks; 360 has what they need. Neither can scale effectively alone.',
        signals: [
          'They express frustration about missing capabilities repeatedly',
          'They\'ve tried building internally and failed',
          'Market opportunity requires combined offering'
        ]
      },
      {
        title: 'Shared vision, different execution strengths',
        description: 'Alignment on impact/market opportunity, but different core competencies that strengthen combined approach.',
        signals: [
          'Conversations naturally flow to "imagine if we combined..."',
          'Both see same market gap from different angles',
          'Cultural/values alignment evident in how they work'
        ]
      },
      {
        title: 'Risk-sharing for new market entry',
        description: 'Neither wants full risk of new market/model, but both see opportunity. JV structure distributes investment and upside.',
        signals: [
          'High potential but unclear path to profitability',
          'Both have "skin in the game" appetite',
          'Willing to co-invest time/resources before revenue'
        ]
      }
    ],
    valueAlignment: {
      frame: [
        '"Building something neither of us could create alone"',
        '"Shared risk, shared upside, shared decision-making"',
        '"Long-term partnership structure, not a project with an end date"',
        '"Your expertise + our methodology = market-leading offering"'
      ],
      cultural: [
        'Use "we/us" language early and often (tests their partnership mindset)',
        'Discuss governance and decision-making openly (who decides what?)',
        'Surface concerns about control/autonomy directly (better now than in legal docs)',
        'Expect multiple conversations about "what if it doesn\'t work?"'
      ],
      alignment: [
        'Collaborative decision-making even when it slows things down',
        'Transparency about financials, capacity, risks',
        'Clear articulation of what success looks like for both parties'
      ],
      misalignment: [
        'One party trying to maintain full control',
        'Unwillingness to discuss downside scenarios',
        'Rush to structure without testing working relationship'
      ]
    },
    qualificationQuestions: [
      {
        category: 'Partnership Readiness',
        questions: [
          'What would change about how your organization operates if this partnership succeeds?',
          'Walk me through the last partnership that didn\'t work. What would you do differently?',
          'How do you make decisions when partners disagree on direction?'
        ]
      },
      {
        category: 'Resource Reality',
        questions: [
          'What are you prepared to invest (time, money, people) before this generates revenue?',
          'Who on your team would actually work on this day-to-day?',
          'What happens if this takes 2x longer than we think to reach profitability?'
        ]
      },
      {
        category: 'Strategic Alignment',
        questions: [
          'What does success look like in 3 years? 5 years?',
          'How does this fit with your organization\'s core strategy vs. being a side project?',
          'What would make you want to exit this partnership? (test worst-case thinking)'
        ]
      },
      {
        category: 'Decision Authority',
        questions: [
          'Who else needs to approve a partnership structure like this?',
          'What\'s your board\'s appetite for joint ventures vs. traditional partnerships?',
          'How much autonomy would you have to operate the JV without constant approval?'
        ]
      }
    ],
    hesitations: [
      {
        hesitation: 'This feels risky, we\'ve never done a JV structure before',
        response: 'That\'s exactly why we start with a clear governance framework and decision-making protocols. SpacePlan took 4 months just working through operating agreements, but that upfront work prevents downstream conflicts. We can also explore pilot structures that test the partnership before full commitment.',
        action: 'Share SpacePlan case study, offer phased approach'
      },
      {
        hesitation: 'How do we handle it if one partner wants out?',
        response: 'Exit provisions get written into the operating agreement from day one. We define buyout terms, transition periods, and IP/client ownership before we launch. The goal is to make the partnership so valuable neither wants out, but we plan for all scenarios.',
        action: 'Show sample governance framework addressing exits'
      },
      {
        hesitation: 'What if we can\'t agree on strategy down the road?',
        response: 'Decision-making authority gets mapped in the operating agreement (who decides what, tiebreaker mechanisms, etc.). We also test working relationship through collaborative projects before formalizing structure. If you can\'t work together on a pilot, you won\'t work together in a JV.',
        action: 'Propose pre-JV collaborative pilot to test dynamics'
      },
      {
        hesitation: 'Our lawyers are going to make this complicated and expensive',
        response: 'Legal complexity is real, typically $25K-$50K for proper operating agreements. But compare that to the cost of a failed partnership or ongoing conflicts. We can start with term sheets and lightweight collaboration while legal documents get finalized.',
        action: 'Provide legal budget estimates, phased approach'
      }
    ],
    framing: {
      past: 'Previous partnerships: Client-vendor or strategic alliance (limited integration)',
      new: '360 + Partner JV: Shared entity, co-invested resources, aligned incentives',
      key: 'Investment in new business model, not just a partnership agreement'
    },
    walkAway: [
      'Control issues: One party wants final say on all decisions (not a partnership)',
      'No stomach for risk: Unwilling to invest resources before guaranteed returns',
      'Hidden agendas: Partner wants 360\'s methodology/relationships but not true collaboration',
      'Organizational instability: Partner in financial distress or leadership transition',
      'Timeline pressure: Need to launch in 2-3 months (JV structure requires 6-12 months minimum)',
      'Values misalignment: Different definitions of success, integrity, or impact'
    ],
    successPatterns: {
      timeline: '11.5 months average (first conversation to launched JV entity)',
      touchpoints: '12-18 meetings/working sessions before structure finalized',
      stages: [
        'Relationship building (3-4 months): Collaborative projects, testing working dynamics',
        'Concept alignment (2-3 months): Vision, market opportunity, capabilities mapping',
        'Structure design (2-3 months): Governance, economics, decision-making frameworks',
        'Legal/operational (3-4 months): Operating agreements, entity formation, systems setup'
      ],
      predictors: [
        'Both parties involve leadership early (not delegated to staff only)',
        'Willingness to discuss difficult scenarios openly',
        'Collaborative work happens before structure discussions',
        'Regular communication rhythm established early'
      ],
      scope: [
        'Initial JV capitalization: $50K-$200K combined investment',
        'First-year operating budget: $150K-$400K',
        '3-year revenue target: $500K-$2M',
        'Typical equity/revenue split: 50/50 or 60/40 depending on investment levels'
      ]
    }
  },
  brazil: {
    name: 'Brazilian Tech Transfer Institutions',
    subtitle: 'CNEN, NanoBioPlus, university tech transfer',
    metrics: {
      explored: 15,
      closed: 9,
      successRate: 60,
      avgTimeline: 6.8,
      approach: 'Relationship-first, hierarchy-aware',
      decisionStyle: 'Consensus-building with oversight'
    },
    patterns: [
      { text: 'Need 3-4 relationship-building meetings before contract discussions', frequency: '90%' },
      { text: 'Multiple stakeholder alignment required (technical + business + government)', frequency: '100%' },
      { text: 'Portuguese capability signals cultural competence and commitment', frequency: '85%' }
    ],
    opportunities: [
      {
        title: 'Massive dormant technology portfolios',
        description: 'Government mandate to commercialize but lack systematic validation methodology. Public R&D investment must demonstrate economic impact.',
        signals: [
          'Portfolio of 30-100+ technologies with no clear prioritization',
          'Pressure from government for commercialization metrics',
          'Previous assessments were one-off, didn\'t build capacity'
        ]
      },
      {
        title: 'Global market access gap',
        description: 'Strong local innovation but limited ability to assess international market fit or connect with global partners.',
        signals: [
          'Technologies validated locally but unknown internationally',
          'Questions about US/European market requirements',
          'Interest in cross-border partnerships but unclear how to structure'
        ]
      },
      {
        title: 'Capacity building need',
        description: 'Want repeatable systems, not just consultant reports. Need to build institutional capability for ongoing innovation assessment.',
        signals: [
          'Ask about training their team on the methodology',
          'Interest in tools/frameworks they can use independently',
          'Long-term thinking about strengthening their institution'
        ]
      }
    ],
    valueAlignment: {
      frame: [
        '"Building Brazil\'s innovation infrastructure, not just evaluating technologies"',
        '"Systematic methodology that meets international standards while respecting local context"',
        '"Bridge between Global South innovation and Global North markets, value flows both directions"',
        '"Partnership that builds your institutional capacity over time"'
      ],
      cultural: [
        'Lead with relationship and long-term vision before scope/pricing',
        'Acknowledge institutional prestige and contribution to Brazilian development',
        'Reference other Brazilian partnerships for social proof',
        'Use "partnership" consistently, avoid "client/vendor" framing',
        'Expect 3-4 relationship meetings before contract discussions'
      ],
      alignment: [
        'Questions about capacity building and methodology transfer',
        'Long-term institutional thinking vs. one-off project',
        'Interest in how this strengthens Brazil\'s innovation ecosystem',
        'Openness to collaborative approach and shared learning'
      ],
      misalignment: [
        '"We need a report by next month"',
        'Purely transactional approach to engagement',
        'Unwillingness to invest in relationship building',
        'Extraction mindset (taking IP/insights without reciprocity)'
      ]
    },
    qualificationQuestions: [
      {
        category: 'Decision Process',
        questions: [
          'Who else needs to be part of this conversation before moving forward?',
          'What needs to happen internally before a partnership gets approved?',
          'Walk me through your last commercialization partnership. What worked? What would you do differently?'
        ]
      },
      {
        category: 'Strategic Intent',
        questions: [
          'Are you looking to strengthen your internal process, or solve for this specific portfolio?',
          'What would change in how your institution works if this partnership succeeds?',
          'How do you think about building Brazil\'s innovation infrastructure vs. individual project outcomes?'
        ]
      },
      {
        category: 'Budget & Timeline',
        questions: [
          'What timeline are you working against? Budget cycles, government reporting, other commitments?',
          'How are you thinking about funding for this kind of engagement?',
          'Are we talking about a pilot to prove value, or scaling something you\'re already committed to?'
        ]
      },
      {
        category: 'Values Alignment',
        questions: [
          'How do you balance global market insights with maintaining Brazilian ownership of innovations?',
          'What does meaningful technology transfer success look like from your institutional perspective?',
          'How involved do you want to be in the process vs. receiving deliverables?'
        ]
      }
    ],
    hesitations: [
      {
        hesitation: 'We need to see more proven impact data',
        response: 'Here\'s what we\'ve validated with [NanoBioPlus/CNEN]. But more importantly, what specific metrics matter for your institutional accountability? Let\'s design this engagement to generate the proof points you actually need.',
        action: 'Share relevant case study, offer pilot with clear success metrics'
      },
      {
        hesitation: 'This seems too ambitious for our timeline/budget',
        response: 'Let\'s right-size this. We can start with portfolio screening to identify your top 5-10 high-potential technologies, then deep-dive validation on the 2-3 you prioritize. That builds momentum and proves methodology before full portfolio engagement.',
        action: 'Propose phased approach with decision gates'
      },
      {
        hesitation: 'We\'re not sure about working with a US-based organization',
        response: 'Our São Paulo office and Brazilian partnerships mean we\'re operating with Brazil, not in Brazil temporarily. We bridge markets, but innovation stays rooted here. Plus, Portuguese-speaking team members who understand institutional dynamics matters.',
        action: 'Connect with current Brazilian partners for references'
      },
      {
        hesitation: 'We tried this before and it didn\'t create real value',
        response: 'What went wrong? Was it methodology, cultural fit, or misaligned expectations? [Listen, then address] Our approach is different because we focus on capacity building, not just reports. You\'re investing in permanent institutional capability.',
        action: 'Show how 360 methodology addresses their specific past failure'
      }
    ],
    framing: {
      past: 'Previous consultants: Transaction-focused, extract insights and leave',
      new: '360 approach: Partnership-focused, build institutional capacity that persists',
      key: 'Investment in commercialization infrastructure, not just an assessment'
    },
    walkAway: [
      'No clear decision authority after 3 conversations',
      'Purely extraction-focused (wanting validation without genuine partnership)',
      'No interest in capacity building (just want report)',
      'Expecting comprehensive portfolio validation in 4-6 weeks',
      'Budget is 1/3 of required scope with no flexibility',
      'Pushing to skip relationship-building (will be difficult partner)',
      'No internal champion to shepherd through bureaucracy'
    ],
    successPatterns: {
      timeline: '6.8 months average (first meeting to signed agreement)',
      touchpoints: '4-6 relationship touchpoints before contracting',
      stages: [
        'Relationship building (4-8 weeks): Multiple stakeholder meetings, cultural fit assessment',
        'Scope alignment (3-4 weeks): Define portfolio, methodology, success metrics',
        'Bureaucratic approval (8-12 weeks): Internal approvals, budget confirmation',
        'Contract execution (2-4 weeks): Legal review, final terms'
      ],
      predictors: [
        'Multiple stakeholder types involved early (technical + business + government)',
        'Questions shift from "what do you do?" to "how do we structure this?" by meeting 3',
        'They introduce you to other partners/collaborators (signals trust)',
        'Portuguese used in some communications (signals comfort)'
      ],
      scope: [
        'Portfolio screening: 30-50 technologies, $40K-$65K, 8-12 weeks',
        'Deep validation: 5-10 priority technologies, $85K-$140K, 12-16 weeks',
        'Full pathway: Assessment + validation + market positioning, $180K-$280K, 6-9 months',
        '67% lead to expanded scope within 18 months'
      ]
    }
  },
  uscorp: {
    name: 'US Corporate & VC Partners',
    subtitle: 'Corporate innovation groups, impact VCs, strategic partners',
    metrics: {
      explored: 22,
      closed: 6,
      successRate: 27,
      avgTimeline: 4.2,
      approach: 'Metrics-driven, efficiency-focused',
      decisionStyle: 'Quick decisions with clear ROI'
    },
    patterns: [
      { text: 'Move fast but require extensive impact metrics documentation', frequency: '95%' },
      { text: 'Initial enthusiasm often doesn\'t survive internal approval process', frequency: '60%' },
      { text: 'Most successful when there\'s a specific pain point or portfolio challenge', frequency: '85%' }
    ],
    opportunities: [
      {
        title: 'Innovation portfolio overwhelm',
        description: 'Too many ideas, not enough systematic prioritization. Corporate innovation groups drowning in proposals without clear validation framework.',
        signals: [
          'Mention having "hundreds of ideas" with no clear path forward',
          'Frustrated with current innovation pipeline effectiveness',
          'Looking for systematic methodology to replace ad-hoc decisions'
        ]
      },
      {
        title: 'Impact measurement credibility',
        description: 'Need to demonstrate social impact for ESG reporting, stakeholder management, or fund positioning. Current measurement feels arbitrary or unconvincing.',
        signals: [
          'Questions about impact metrics frameworks and standards',
          'Pressure from leadership or LPs to quantify social outcomes',
          'Looking for third-party validation of impact claims'
        ]
      },
      {
        title: 'Market expansion intelligence',
        description: 'Corporate considering new markets (especially Latin America) or VCs looking at international portfolio companies. Need local expertise and validation.',
        signals: [
          'Questions about Brazilian/Latin American market dynamics',
          'Portfolio companies considering international expansion',
          'Looking for on-the-ground market validation'
        ]
      }
    ],
    valueAlignment: {
      frame: [
        '"Systematic innovation methodology that scales across your portfolio"',
        '"Impact metrics that satisfy stakeholders while driving real outcomes"',
        '"Bridge between your corporate objectives and authentic community value"',
        '"Efficiency through clear prioritization, not just more data"'
      ],
      cultural: [
        'Lead with data, ROI, and efficiency gains',
        'Provide clear deliverables timeline upfront',
        'Acknowledge corporate constraints (budget cycles, approval processes)',
        'Frame as strategic advantage, not just social good',
        'Be ready to move quickly when they say yes'
      ],
      alignment: [
        'Clear articulation of success metrics and KPIs',
        'Willingness to pilot before full commitment',
        'Internal champion who can navigate approval process',
        'Realistic about timeline and budget requirements'
      ],
      misalignment: [
        'Social impact as pure marketing play with no substance',
        'Expecting free work to "test the partnership"',
        'Constantly changing priorities and decision-makers',
        'Unwilling to invest in proper validation methodology'
      ]
    },
    qualificationQuestions: [
      {
        category: 'Problem Clarity',
        questions: [
          'What specifically isn\'t working in your current innovation/impact process?',
          'What happens if you don\'t solve this problem in the next 6-12 months?',
          'Who internally is feeling the pain of this problem most acutely?'
        ]
      },
      {
        category: 'Decision Authority',
        questions: [
          'Who has budget authority for this kind of engagement?',
          'Walk me through your typical approval process for external partnerships',
          'What would make this an easy yes vs. a hard sell internally?'
        ]
      },
      {
        category: 'Success Definition',
        questions: [
          'What would success look like 6 months after this engagement?',
          'How do you currently measure innovation effectiveness or impact outcomes?',
          'What metrics would make your leadership team pay attention?'
        ]
      },
      {
        category: 'Commitment Level',
        questions: [
          'What\'s your timeline for making a decision on this?',
          'What else are you evaluating as alternatives to this approach?',
          'If this works, what\'s the potential for expanded scope or ongoing partnership?'
        ]
      }
    ],
    hesitations: [
      {
        hesitation: 'This seems expensive for what we need',
        response: 'Let\'s break down the ROI. If this helps you prioritize your innovation portfolio 20% more effectively, what\'s that worth in terms of resource allocation? Or if it prevents one major misallocation of capital, the engagement pays for itself. We can also start with a focused pilot.',
        action: 'Build business case showing cost of poor prioritization'
      },
      {
        hesitation: 'We need this done in 4-6 weeks',
        response: 'Proper validation takes time, but we can structure this as phased deliverables. Week 2: initial screening. Week 4: priority recommendations. Week 6: validation framework. That gives you actionable insights quickly while building toward comprehensive methodology.',
        action: 'Propose phased delivery with early value milestones'
      },
      {
        hesitation: 'Our leadership isn\'t convinced about the social impact focus',
        response: 'Frame this as strategic advantage, not charity. Companies with authentic impact strategies attract better talent, stronger partnerships, and more loyal customers. The impact measurement becomes a competitive differentiator, not just a reporting requirement.',
        action: 'Share corporate examples where impact drove business results'
      },
      {
        hesitation: 'Can we do a small pilot first to test this?',
        response: 'Absolutely. We can start with a 3-technology validation pilot or a single market assessment. That proves the methodology and builds internal buy-in before larger commitment. Most of our corporate partnerships started as pilots.',
        action: 'Design focused pilot with clear success metrics'
      }
    ],
    framing: {
      past: 'Previous approach: Ad-hoc innovation decisions or generic consulting frameworks',
      new: '360 approach: Systematic validation methodology with impact measurement built in',
      key: 'Strategic advantage through better prioritization and authentic impact'
    },
    walkAway: [
      'No clear budget or decision authority after 2-3 conversations',
      'Purely extractive mindset (want methodology without paying for it)',
      'Impact as pure marketing with no genuine interest in outcomes',
      'Unrealistic timeline expectations (comprehensive validation in 2 weeks)',
      'Constantly changing priorities with no ability to commit',
      'Expecting 360 to take on implementation risk without proper engagement',
      'No internal champion or executive sponsor'
    ],
    successPatterns: {
      timeline: '4.2 months average (first meeting to contract execution)',
      touchpoints: '3-5 meetings before proposal, 2-3 weeks for internal approval',
      stages: [
        'Problem validation (1-2 weeks): Confirm pain point and urgency',
        'Scope definition (2-3 weeks): Design engagement, align on metrics',
        'Internal approval (4-8 weeks): Champion shepherds through process',
        'Contract execution (2-4 weeks): Legal review, procurement'
      ],
      predictors: [
        'Clear internal champion with budget authority',
        'Specific pain point or deadline driving urgency',
        'Quick decision-making in early conversations',
        'Willingness to start with pilot structure'
      ],
      scope: [
        'Innovation portfolio assessment: 20-50 concepts, $35K-$60K, 6-8 weeks',
        'Impact measurement framework: Program/portfolio level, $45K-$85K, 8-12 weeks',
        'Market validation: Specific geography/technology, $50K-$95K, 10-14 weeks',
        '40% convert to expanded or ongoing engagements'
      ]
    }
  },
  foundation: {
    name: 'Foundation & Impact Investors',
    subtitle: 'Philanthropic foundations, impact funds, development finance',
    metrics: {
      explored: 18,
      closed: 5,
      successRate: 28,
      avgTimeline: 8.5,
      approach: 'Mission-aligned, deliberate decision-making',
      decisionStyle: 'Consensus-driven with multiple stakeholders'
    },
    patterns: [
      { text: 'Funding cycles cluster in Q1 and Q3; Q2 engagement rarely converts', frequency: '80%' },
      { text: 'Require extensive alignment on theory of change and impact measurement', frequency: '95%' },
      { text: 'Best partnerships emerge from program officer relationships, not cold outreach', frequency: '85%' }
    ],
    opportunities: [
      {
        title: 'Portfolio effectiveness questions',
        description: 'Foundation leadership or investment committees questioning whether current portfolio is achieving intended impact. Need for systematic assessment and course correction.',
        signals: [
          'Recent strategy refresh or leadership transition',
          'Questions about "how do we know what\'s working?"',
          'Pressure to demonstrate impact to board or stakeholders',
          'Considering new program areas or geographic expansion'
        ]
      },
      {
        title: 'Grantee/investee capacity gaps',
        description: 'Portfolio organizations lack capacity for proper impact measurement, market validation, or scaling strategy. Foundation wants to strengthen ecosystem, not just fund projects.',
        signals: [
          'Frustration that grantees can\'t articulate impact clearly',
          'Portfolio companies struggling with market validation',
          'Interest in capacity-building infrastructure for ecosystem',
          'Looking for partners who can work directly with grantees'
        ]
      },
      {
        title: 'Systems change credibility',
        description: 'Want to move beyond programmatic funding to systems-level impact but need frameworks and measurement approaches. Current impact reporting feels insufficient.',
        signals: [
          'Language about "systems change" without clear methodology',
          'Desire to fund "innovation" but unclear how to evaluate',
          'Questions about long-term sustainability of impact',
          'Interest in collective impact or ecosystem approaches'
        ]
      }
    ],
    valueAlignment: {
      frame: [
        '"Systematic approach to impact validation that serves your mission"',
        '"Building capacity across your portfolio, not just assessing individual grantees"',
        '"Bridge between funder priorities and authentic community outcomes"',
        '"Long-term systems change with clear interim milestones"'
      ],
      cultural: [
        'Lead with mission alignment and shared values',
        'Emphasize community voice and participatory approaches',
        'Be patient with decision-making timelines',
        'Acknowledge power dynamics in funder relationships',
        'Respect existing relationships with grantees/investees'
      ],
      alignment: [
        'Clear theory of change and willingness to iterate',
        'Interest in capacity building, not just deliverables',
        'Long-term systems thinking vs. quick wins',
        'Openness to community-driven approaches',
        'Recognition that impact measurement should serve learning, not just reporting'
      ],
      misalignment: [
        'Rigid pre-determined outcomes without room for emergence',
        'Purely extractive assessment (evaluating grantees without supporting them)',
        'Timeline pressure that undermines quality engagement',
        'Unwillingness to invest in proper methodology',
        'Funder-centric approach that ignores community voice'
      ]
    },
    qualificationQuestions: [
      {
        category: 'Strategic Intent',
        questions: [
          'What\'s driving this conversation now? Why is this a priority for your foundation?',
          'How does this fit with your overall strategy and theory of change?',
          'What would change in your grantmaking/investing if this engagement succeeds?'
        ]
      },
      {
        category: 'Decision Process',
        questions: [
          'Who needs to be involved in this decision? Program officers, leadership, board?',
          'Walk me through your typical process for this kind of engagement',
          'What funding cycle or timeline are you working within?',
          'What would make this an easy approval vs. a hard sell internally?'
        ]
      },
      {
        category: 'Impact Philosophy',
        questions: [
          'How do you currently think about impact measurement vs. impact management?',
          'What role do you see community voice playing in validation and assessment?',
          'How comfortable are you with emergent outcomes vs. pre-defined metrics?',
          'What\'s your relationship been with evaluation in the past? What worked? What didn\'t?'
        ]
      },
      {
        category: 'Partnership Model',
        questions: [
          'Are you looking for one-time assessment or ongoing partnership?',
          'How do you want your grantees/investees to experience this work?',
          'What does good stewardship of this engagement look like from your perspective?',
          'How do you handle it when evaluation reveals gaps or concerns in portfolio?'
        ]
      }
    ],
    hesitations: [
      {
        hesitation: 'This feels like it could be extractive for our grantees',
        response: 'That\'s exactly the concern we design against. Our approach is capacity-building, not just assessment. Grantees gain validation methodology they can use beyond this engagement. We also build in participatory design so community voice shapes what we\'re measuring.',
        action: 'Share examples of grantee feedback from past engagements'
      },
      {
        hesitation: 'Our board is very metrics-focused and this seems too qualitative',
        response: 'We balance quantitative and qualitative approaches. The framework includes hard metrics (reach, outcomes, cost-effectiveness) and contextual understanding (why something works, who it serves, sustainability factors). Most boards respond well to this comprehensive view.',
        action: 'Show sample report balancing metrics and narrative'
      },
      {
        hesitation: 'We\'re in the middle of a strategy refresh and not sure about timing',
        response: 'This work can actually inform your strategy refresh. Portfolio assessment reveals where you\'re having impact and where gaps exist. That intelligence strengthens strategic decision-making. We can phase this to align with your strategy timeline.',
        action: 'Propose engagement that feeds strategy process'
      },
      {
        hesitation: 'The budget for this would come from program funds, taking from grantees',
        response: 'Think of this as infrastructure investment that strengthens your entire portfolio. Better prioritization and impact measurement increases the effectiveness of every dollar you deploy. We can also explore whether this fits under operations or learning budgets.',
        action: 'Build ROI case showing portfolio-wide benefits'
      }
    ],
    framing: {
      past: 'Previous evaluations: One-time assessments focused on accountability',
      new: '360 approach: Capacity-building partnerships focused on learning and improvement',
      key: 'Investment in portfolio effectiveness and ecosystem strength'
    },
    walkAway: [
      'Purely accountability-driven with no interest in learning or improvement',
      'Rigid outcomes focus with no room for community-driven emergence',
      'Timeline pressure (need comprehensive assessment in 4-6 weeks)',
      'Extractive mindset toward grantees (evaluation without support)',
      'No budget flexibility or clear funding source',
      'Decision authority unclear after multiple conversations',
      'Values misalignment on power dynamics or community voice',
      'Expecting guarantees about grantee outcomes'
    ],
    successPatterns: {
      timeline: '8.5 months average (first conversation to contract execution)',
      touchpoints: '6-10 meetings before proposal (program officers, leadership, sometimes board)',
      stages: [
        'Relationship building (2-3 months): Mission alignment, approach validation',
        'Scope co-design (1-2 months): Collaborative design of engagement',
        'Internal approval (3-5 months): Program officer champions through committees/board',
        'Contract execution (2-4 weeks): Legal review, typically straightforward'
      ],
      predictors: [
        'Strong program officer champion who understands and advocates for approach',
        'Foundation in learning mode (not just accountability mode)',
        'Alignment on participatory and capacity-building philosophy',
        'Clear budget source identified early (operations, learning, or program)',
        'Board or leadership receptive to systems-level thinking'
      ],
      scope: [
        'Portfolio assessment: 10-20 grantees/investees, $75K-$125K, 4-6 months',
        'Impact measurement framework: Foundation-wide, $60K-$95K, 3-5 months',
        'Grantee capacity building: Cohort-based, $85K-$150K, 6-9 months',
        'Systems mapping: Specific ecosystem, $50K-$90K, 3-4 months',
        '60% lead to multi-year partnerships or expanded scope'
      ]
    }
  }
};
