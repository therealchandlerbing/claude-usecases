# Long-Term Impact Assessment

Analyzing societal-scale effects and feedback loops that compound over time.

## Societal-Scale Analysis

AI systems don't just affect individuals—they shape society. Assess impacts across multiple domains:

### Economic Impact

**Labor Market Effects**

**Job Displacement:**
- Which jobs and roles are automated or eliminated?
- Who is most vulnerable to displacement?
- Are there alternatives or retraining opportunities?
- What is the pace and scale of displacement?

**Job Creation:**
- What new roles emerge?
- Who has access to new opportunities?
- What skills are required?
- Do new jobs compensate for displaced jobs?

**Job Transformation:**
- How do existing roles change?
- Is work enriched or degraded?
- Power shifts between workers and employers?
- Wage and working condition effects?

**Wealth and Income Distribution**

**Concentration vs. Distribution:**
- Does AI concentrate wealth (winner-take-all) or distribute it?
- Who captures the economic value created by AI?
- Effect on inequality (within and between countries)
- Access to capital and opportunity

**Example Analysis:**
- Automation of manufacturing → job loss for middle-skill workers → income inequality increases
- Platform economy AI → concentration of value with platform owners → wealth concentration
- AI-powered finance → algorithmic trading benefits those with access → inequality grows

**Access to Economic Opportunity**

**Who Gets Access:**
- Do AI systems expand or restrict opportunity?
- Are barriers lowered or raised?
- Who is included vs. excluded?
- Geographic and demographic patterns

**Example:**
- AI lending could expand credit access OR perpetuate discriminatory denials
- AI hiring could reduce bias OR encode historical discrimination
- Educational AI could personalize learning OR track students into unequal paths

**Market Concentration and Monopoly**

**Competition Effects:**
- Network effects and data advantages creating monopolies?
- Barriers to entry for new competitors?
- Lock-in and switching costs?
- Innovation effects

**Power Implications:**
- Market power translating to political power?
- Regulatory capture risks?
- Consumer choice and welfare effects?

### Social Impact

**Social Cohesion and Polarization**

**Connection vs. Division:**
- Does AI bring people together or drive them apart?
- Filter bubbles and echo chambers
- Amplification of divisive content
- Social isolation vs. connection

**Trust in Institutions:**
- Does AI strengthen or undermine institutional trust?
- Mis/disinformation effects
- Transparency and accountability impacts
- Legitimacy of AI-mediated decisions

**Social Mobility Patterns**

**Opportunity Across Generations:**
- Does AI enable or constrain upward mobility?
- Intergenerational effects of algorithmic decisions
- Education and credentialing impacts
- Path dependence and lock-in

**Example:**
- Educational tracking by AI → students locked into trajectories early → reduced mobility
- Credit scoring → denied opportunities early → harder to build credit → persistent disadvantage

**Community Resilience**

**Strengthening vs. Weakening:**
- Community capacity to adapt and respond
- Dependence on external systems
- Local knowledge and autonomy
- Social bonds and mutual aid

### Political Impact

**Democratic Participation**

**Enablement vs. Suppression:**
- Does AI expand political voice or concentrate it?
- Access to political process and information
- Surveillance and chilling effects
- Mobilization and organizing capacity

**Information Ecosystems**

**Quality and Diversity:**
- Information quality and trustworthiness
- Diversity of perspectives and sources
- Amplification of mis/disinformation
- Gatekeeping and censorship

**Civic Discourse Quality**

**Constructive vs. Degraded:**
- Deliberation and reasoned discussion
- Polarization and tribalism
- Civility and respect
- Ability to find common ground

**Power Distribution**

**Concentration vs. Dispersal:**
- Who holds power to make consequential decisions?
- Checks and balances on power
- Transparency and accountability
- Democratic control vs. technocratic rule

### Environmental Impact

**Energy Consumption and Carbon Footprint**

**AI's Climate Impact:**
- Training large models: massive energy use (GPT-3: ~1,287 MWh)
- Inference at scale: ongoing energy consumption
- Data center emissions
- Comparison to other activities

**Mitigation:**
- Energy-efficient models and hardware
- Renewable energy for AI infrastructure
- Carbon accounting and offsetting
- Right-sizing models to actual needs

**Resource Extraction**

**Hardware Supply Chain:**
- Rare earth mineral mining for chips
- Water use in semiconductor manufacturing
- Environmental damage from extraction
- Human rights issues in supply chain

**E-Waste**

**Disposal and Recycling:**
- Rapid hardware obsolescence
- E-waste concentrated in Global South
- Toxic materials and health impacts
- Circular economy approaches

**Climate Justice Implications**

**Unequal Burden:**
- Global South bears environmental costs
- Global North captures benefits
- Vulnerable populations most affected by climate impacts
- Intergenerational justice

## Feedback Loop Analysis

Critical to identify self-reinforcing cycles that amplify over time.

### Positive Feedback Loops (Amplification)

**Type 1: Decisions Affecting Future Opportunities**

**Mechanism:**
AI decision → affects opportunity → affects outcomes → affects future data → reinforces AI decision

**Examples:**

**Hiring:**
1. AI hiring tool trained on historical data (biased toward demographic group A)
2. System recommends more candidates from group A
3. Group A hired more, gains experience, builds networks
4. Future training data shows group A more successful
5. System becomes more biased toward group A
→ **Result:** Initial bias amplifies over time

**Credit:**
1. Credit algorithm denies credit to group B
2. Group B can't build credit history
3. Group B continues to be denied credit
4. Data shows group B has poor credit
5. Algorithm's denial of group B seems validated
→ **Result:** Credit access gap widens

**Type 2: Historical Bias Perpetuated**

**Mechanism:**
Past discrimination → in training data → learned by AI → applied to new decisions → becomes new data → cycle continues

**Breaking the Loop:**
- Use data that reflects desired fairness, not historical bias
- Adjust for known historical discrimination
- Monitor for feedback loops
- Regular retraining with debiasing
- Circuit breakers when bias detected

**Type 3: Rich-Get-Richer Dynamics**

**Mechanism:**
Initial advantage → AI amplifies → greater advantage → more amplification

**Examples:**

**Platform Recommendations:**
1. Popular content gets recommended
2. Recommendations drive more engagement
3. More engagement makes content more popular
4. Even more recommendations
→ **Result:** Winner-take-all dynamics, diversity loss

**Predictive Policing:**
1. More police in neighborhood A
2. More arrests in neighborhood A
3. Data shows neighborhood A is "high crime"
4. Model predicts more crime in neighborhood A
5. More police sent to neighborhood A
→ **Result:** Self-fulfilling prophecy

**Type 4: Echo Chambers and Filter Bubbles**

**Mechanism:**
Content personalization → engagement with similar content → more personalization → less diversity → more extreme views

**Breaking the Loop:**
- Diverse recommendations (not just engagement-maximizing)
- Exposure to different perspectives
- Transparency about filtering
- User control over personalization

### Intervention Points

**Where to Break Feedback Loops:**

**1. Data Collection**
- Collect data that reflects desired outcomes, not just past patterns
- Oversample underrepresented groups
- Adjust for known biases

**2. Model Training**
- Use fairness constraints during training
- Debias training data
- Regularization techniques
- Adversarial debiasing

**3. Decision-Making**
- Human review of decisions, especially for vulnerable groups
- Randomization to break patterns
- Quotas or targets for equity
- Transparency about basis for decisions

**4. Monitoring**
- Track outcomes over time by group
- Detect emerging disparities early
- Statistical process control
- Alert when loops detected

**5. Regular Refresh**
- Retrain models regularly
- Don't let historical data dominate
- Introduce diversity in training data
- Sunset old data

**6. Circuit Breakers**
- Automatic shutdown when bias exceeds threshold
- Human review triggered
- Rollback to previous version
- Incident response activated

## Long-Term Assessment Framework

### Scenario Analysis

**Best Case Scenario:**
- How could this system, at its best, shape society in 10-20 years?
- What positive changes could compound?
- Who benefits most?

**Worst Case Scenario:**
- What if feedback loops amplify harms?
- How could initial disparities compound?
- What's the worst plausible outcome?

**Most Likely Scenario:**
- Given current trends, what's most probable?
- What middle-path outcomes are expected?
- What unintended consequences might emerge?

### Intergenerational Impact

**Effects on Future Generations:**
- Decisions made today shape opportunities for children
- Educational tracking affects lifetime trajectories
- Environmental costs paid by future generations
- Data created now may affect individuals for decades

**Seven Generations Thinking:**
Borrowed from Indigenous philosophy: consider impacts seven generations forward
- What legacy are we creating?
- Are we preserving options for future generations?
- What irreversible changes might occur?

### Reversibility Assessment

**Can Impacts Be Reversed?**
- Are decisions reversible or permanent?
- Can data be deleted or forgotten?
- Can systems be rolled back if harmful?
- What's the cost of reversal?

**Irreversible Harms:**
- Lost opportunities (education, jobs)
- Reputation damage
- Crystallized inequality
- Environmental damage
- Eroded trust

### Adaptive Capacity

**Can Society Adapt?**
- How quickly can regulations catch up?
- Can affected communities organize and resist?
- Are there safety valves and corrective mechanisms?
- What's the pace of change vs. pace of adaptation?

## Long-Term Impact Report Template

```
LONG-TERM SOCIETAL IMPACT ASSESSMENT

System: [Name]
Time Horizon: [10 years / 20 years / generational]

ECONOMIC IMPACTS
- Labor market: [Analysis]
- Wealth distribution: [Trend]
- Access to opportunity: [Assessment]
- Market structure: [Concentration effects]

SOCIAL IMPACTS
- Social cohesion: [Strengthen / Weaken / Mixed]
- Institutional trust: [Analysis]
- Social mobility: [Enable / Constrain / Neutral]
- Community resilience: [Assessment]

POLITICAL IMPACTS
- Democratic participation: [Analysis]
- Information ecosystem: [Quality trends]
- Civic discourse: [Constructive / Degraded]
- Power distribution: [Concentration assessment]

ENVIRONMENTAL IMPACTS
- Carbon footprint: [Estimate]
- Resource extraction: [Analysis]
- E-waste: [Volume and management]
- Climate justice: [Assessment]

FEEDBACK LOOPS IDENTIFIED
1. [Description of loop, amplification potential]
2. [Description of loop, amplification potential]
3. [Description of loop, amplification potential]

INTERVENTION POINTS
- [Where/how to break negative loops]

IRREVERSIBLE HARMS
- [Permanent or difficult-to-reverse impacts]

INTERGENERATIONAL EFFECTS
- [How this shapes opportunities for future generations]

RECOMMENDATIONS
1. [Long-term monitoring requirement]
2. [Policy intervention needed]
3. [System redesign suggestion]
```

Remember: Short-term metrics often miss long-term harms. The most consequential impacts of AI systems may not be visible for years or decades.
