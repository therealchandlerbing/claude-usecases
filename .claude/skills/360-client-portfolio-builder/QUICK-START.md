# Quick Start Guide - 360 Client Portfolio Builder

Build your first 360 client portfolio in under 2 hours. This guide gets you from Vianeo data to live website with minimal reading.

## Prerequisites (5 minutes)

**What you need:**
- [ ] Vianeo sprint outputs for one client team
- [ ] Basic team information (founders, mission, sector)
- [ ] 3-5 key milestones or traction metrics
- [ ] Access to Claude with this skill enabled
- [ ] Netlify account (free, create at netlify.com)

**What you don't need:**
- Design experience
- Coding knowledge
- Previous portfolio building experience

## Fast Track Process

### Step 1: Collect Data (15 minutes)

Use the [Vianeo Intake Form](templates/vianeo-intake-form.md). Fill out these sections minimum:

**Critical information:**
- Team name and tagline
- Problem being solved (2-3 sentences)
- Solution approach (2-3 sentences)
- Target audience/market
- Current stage (TRL, validation status)
- Key milestones achieved
- 360 partnership context

**Copy this prompt template:**
```
I'm using the Vianeo Intake Form. Here's what I have:

TEAM: [name]
TAGLINE: [one sentence]
PROBLEM: [what they're solving]
SOLUTION: [their approach]
STAGE: [TRL and validation status from Vianeo]
TRACTION: [3-5 key achievements]
SECTOR: [industry/domain]
360 CONTEXT: [how we're supporting them]
```

### Step 2: Build Portfolio with Claude (60 minutes)

**Prompt Claude:**
```
Using the 360 Client Portfolio Builder skill, create a portfolio page for this team:

[paste your filled-in information from Step 1]

Target audience: [investors / partners / ecosystem]
Design direction: Editorial sophistication, not corporate template
Sector: [cleantech / healthtech / edtech / other]
```

**What Claude will do:**
1. Ask clarifying questions about design preferences
2. Translate your Vianeo data into accessible narrative
3. Create HTML with sophisticated design
4. Generate a complete portfolio page

**You'll receive:**
- Complete HTML file
- Design rationale explanation
- Deployment instructions

### Step 3: Review & Refine (20 minutes)

**Open the HTML file in your browser and check:**

✅ **First 10 seconds test:** Is value proposition immediately clear?
✅ **Mobile test:** View on phone (375px width minimum)
✅ **Content test:** Would non-technical person understand this?
✅ **Visual test:** Does it look hand-crafted, not template-based?

**Common refinements to request:**
- "Make the hero section more asymmetric"
- "Simplify the Vianeo technical language in the innovation section"
- "Add more white space between sections"
- "Emphasize the traction metrics more prominently"
- "Adjust color palette to feel more [sector-appropriate]"

### Step 4: Deploy Live (15 minutes)

**Using Netlify (easiest):**

1. Go to **drop.netlify.com**
2. Drag your HTML file into the upload area
3. Get instant live URL
4. **For permanent site:** Create Netlify account, claim the site

**Alternative: Netlify with account (recommended for production):**

1. Go to **app.netlify.com**
2. Click "Add new site" → "Deploy manually"
3. Drag HTML file into deploy zone
4. Site goes live with yoursite.netlify.app URL
5. Optional: Add custom domain in site settings

**Done!** You now have a live portfolio at [yoursite].netlify.app

### Step 5: Share & Update (5 minutes)

**Share with client:**
- Send live URL
- Explain it's their professional web presence
- Mention it's optimized for investor/partner sharing

**Future updates:**
- Edit HTML file locally
- Go to Netlify > Deploys tab
- Drag updated file to redeploy
- Changes live in 10-15 seconds

## Total Time: ~2 hours

- Data collection: 15 min
- Building with Claude: 60 min
- Review & refine: 20 min
- Deployment: 15 min
- Sharing: 5 min

## Example Prompt for Your First Portfolio

Here's a complete example to copy and modify:

```
Using the 360 Client Portfolio Builder skill, create a portfolio page for this team:

TEAM: SolarGrid Technologies
TAGLINE: Making renewable energy accessible for off-grid communities in East Africa
PROBLEM: 600 million people in sub-Saharan Africa lack reliable electricity. Existing
solar solutions are either too expensive or too unreliable for sustained use.
SOLUTION: We've developed a modular microgrid system that costs 40% less than
traditional solar installations and includes AI-powered load management for reliability.
STAGE: TRL 6 (system demonstrated in operational environment). We completed 50+
customer discovery interviews and currently running paid pilots with 3 anchor customers
in Kenya and Tanzania.
TRACTION:
- Deployed 12 microgrids serving 2,400 people
- $180K in pilot revenue over 6 months
- Partnership with Kenya Power & Lighting for grid integration
- Selected for Shell Foundation's Energy Access accelerator
- Team includes former Tesla energy engineer and local community organizers
SECTOR: Cleantech / Energy Access
360 CONTEXT: We're supporting SolarGrid through a 6-month Vianeo sprint focused on
commercial pathway validation and investor readiness. They're preparing for seed round.

Target audience: Impact investors and energy access foundations
Design direction: Editorial sophistication, credible but not corporate, emphasize
both innovation and community impact
```

## Success Checklist

After your first portfolio, you should have:

✅ Live website at [name].netlify.app
✅ Mobile-responsive design that works on all devices
✅ Content that translates Vianeo data into accessible language
✅ Design that looks hand-crafted, not template-based
✅ Clear 360 partnership presence without overshadowing client
✅ Deployment process you can repeat for future updates

## Common First-Time Issues

**Issue:** "Portfolio looks too corporate/template-ish"
**Fix:** Request "more asymmetric layout, unexpected details, hand-crafted feel"

**Issue:** "Vianeo language still sounds too technical"
**Fix:** Ask Claude to "translate all technical terms into stakeholder-friendly language"

**Issue:** "Not sure what sector positioning to use"
**Fix:** Check [sector-positioning.md](references/sector-positioning.md) for guidance

**Issue:** "Mobile layout looks broken"
**Fix:** Request "optimize for mobile breakpoints 375px, 768px, 1024px"

**Issue:** "Don't know what to emphasize"
**Fix:** Ask Claude "what are the 3 most compelling data points from this Vianeo output?"

## Next Steps After First Portfolio

**Immediate:**
- Share with client for feedback
- Test with target audience (investors/partners)
- Track engagement metrics if possible

**Within 1 week:**
- Review [SKILL.md](SKILL.md) for complete process understanding
- Study one [example portfolio](examples/) matching your sector
- Understand [design-standards.md](references/design-standards.md) for future builds

**Within 1 month:**
- Build 2-3 more portfolios to establish pattern recognition
- Contribute learnings back to skill documentation
- Develop sector-specific templates for your common use cases

## Getting Help

**If stuck during build:**
1. Check [quality-checklist.md](references/quality-checklist.md) to identify specific issue
2. Reference relevant guide ([design-standards.md](references/design-standards.md), [content-strategy.md](references/content-strategy.md), etc.)
3. Look at [examples/](examples/) for working patterns
4. Ask Claude specific questions about the issue

**If stuck after deployment:**
1. Review [netlify-guide.md](deployment/netlify-guide.md) for troubleshooting
2. Check browser console for errors
3. Test on multiple devices and browsers
4. Validate HTML and accessibility

## Resources for Your First Build

**Must read:**
- [vianeo-intake-form.md](templates/vianeo-intake-form.md) - Data collection template

**Reference while building:**
- [vianeo-translation-guide.md](references/vianeo-translation-guide.md) - Technical to narrative
- [content-strategy.md](references/content-strategy.md) - Writing guidance

**Check before launching:**
- [quality-checklist.md](references/quality-checklist.md) - Pre-launch validation

**After you're comfortable:**
- [SKILL.md](SKILL.md) - Complete process understanding
- [IMPLEMENTATION-GUIDE.md](IMPLEMENTATION-GUIDE.md) - Deep patterns and rationale

## Measuring Success

**For first portfolio:**
- Client approves final version
- Loads in under 3 seconds on mobile
- Readable without technical background
- Looks professionally designed
- Successfully deploys to live URL

**For ongoing usage:**
- Build time decreases to 90-120 minutes
- Client feedback improves
- Stakeholder engagement increases (tracked via analytics)
- Portfolio inquiries convert to partnership discussions
- 360's ecosystem visibility grows

## Building Confidence

**First portfolio:** Follow this guide exactly, use provided prompt template
**Second portfolio:** Adapt prompt template, reference guides as needed
**Third portfolio:** Freestyle with guide check-ins for validation
**Fourth+ portfolio:** Develop your own patterns, contribute back to skill

---

**Ready to start?** Copy the example prompt above, fill in your client's information, and paste it to Claude.

**Questions?** Check [INDEX.md](INDEX.md) for navigation to specific resources.

**After your first portfolio?** Read [SKILL.md](SKILL.md) for complete process mastery.
