# Quality Checklist - Pre-Launch Validation

**Purpose:** Comprehensive validation checklist before deploying portfolio pages

**Version:** 1.0.0
**Last Updated:** 2025-11-16

---

## How to Use This Checklist

1. **Complete build** before using this checklist
2. **Work through each section** systematically
3. **Fix issues** as you find them
4. **Re-test** after fixes
5. **Deploy only when all critical items pass**

**Rating System:**
- 🚨 **Critical** - Must fix before launch
- ⚠️ **High Priority** - Should fix before launch
- ℹ️ **Standard** - Nice to have, fix if time permits

---

## Strategic Clarity

### Value Proposition (🚨 Critical)

- [ ] **10-Second Test:** Can viewer understand what the venture does in 10 seconds?
- [ ] **Problem is clear:** Is it obvious what problem they're solving?
- [ ] **Solution is clear:** Is it obvious how they're solving it?
- [ ] **Beneficiaries identified:** Is it clear who benefits?
- [ ] **Differentiation obvious:** Is it clear why this is unique/better?

**Test Method:** Show portfolio to someone unfamiliar with venture. Can they explain it back to you accurately in 30 seconds?

### Target Audience Alignment (⚠️ High Priority)

- [ ] **Investor-focused:** If targeting investors, traction/business model prominent?
- [ ] **Partner-focused:** If targeting partners, collaboration opportunities clear?
- [ ] **Ecosystem-focused:** If targeting ecosystem, mission/impact emphasized?
- [ ] **Language appropriate:** Technical level matches audience sophistication?
- [ ] **Call-to-action matches:** CTA aligns with target audience intent?

### Credibility (🚨 Critical)

- [ ] **No overselling:** Claims match evidence level
- [ ] **Specific metrics:** Numbers are specific, not vague ("5,200 families" not "thousands")
- [ ] **Appropriate confidence:** Language calibrated to validation stage
- [ ] **Professional tone:** Sounds credible, not hype or overly casual
- [ ] **Completeness:** No obvious gaps (missing sections, placeholder text)

---

## Design Excellence

### Visual Sophistication (⚠️ High Priority)

- [ ] **Hand-crafted feel:** Doesn't look template-based or generic
- [ ] **Asymmetry intentional:** Layout breaks symmetry purposefully
- [ ] **White space generous:** Content has breathing room, not cramped
- [ ] **Typography hierarchy:** Clear visual flow from large to small text
- [ ] **Color palette cohesive:** 2-3 colors used consistently and purposefully
- [ ] **No generic imagery:** No obvious stock photos or AI gradients

**Test Method:** Compare to high-end design studio websites (Stripe, Linear, Notion). Does it feel similar in craft and intention?

### 360 Brand Presence (🚨 Critical)

- [ ] **Logo/wordmark visible:** 360 branding in navigation or header
- [ ] **Footer attribution:** "Partnership with 360 Social Impact Studios" in footer
- [ ] **360 colors used:** Sage, terracotta, plum, gray in UI elements
- [ ] **Partnership section present:** Dedicated section explaining 360's role
- [ ] **Client is hero:** Client name/logo larger and more prominent than 360
- [ ] **360 doesn't overshadow:** Client venture is primary focus, 360 supports

### Visual Hierarchy (⚠️ High Priority)

- [ ] **Hero dominates:** Venture name is largest text on page
- [ ] **Section headers clear:** Easy to scan and understand page structure
- [ ] **Call-to-action obvious:** Primary CTA stands out visually
- [ ] **Related content grouped:** Visual proximity matches conceptual relationships
- [ ] **Eye flows naturally:** Design guides viewer through narrative arc

### Unexpected Details (ℹ️ Standard)

- [ ] **Unique visual elements:** At least 1-2 custom touches (not template standard)
- [ ] **Thoughtful interactions:** Hover states, animations feel intentional
- [ ] **Variable rhythm:** Section spacing and widths vary (not uniform)
- [ ] **Personality present:** Design reflects venture's sector/character

---

## Content Accessibility

### Understandability (🚨 Critical)

- [ ] **No unexplained jargon:** Technical terms defined or avoided
- [ ] **Concrete examples:** Abstract concepts illustrated with specifics
- [ ] **One idea per sentence:** Sentences are scannable, not dense
- [ ] **Active voice:** Most sentences use active voice (subject does action)
- [ ] **Lead with outcomes:** Benefits/results stated before mechanisms

**Test Method:** Show to non-specialist (someone outside the sector). Can they understand without asking questions?

### Story Flow (⚠️ High Priority)

- [ ] **Logical progression:** Sections follow narrative arc (problem → solution → evidence → future)
- [ ] **Transitions smooth:** Each section connects to next
- [ ] **No redundancy:** Key points made once, not repeated
- [ ] **Appropriate pacing:** Right balance of detail (not too sparse, not too dense)
- [ ] **Coherent narrative:** Overall story is clear and compelling

### Vianeo Data Translation (🚨 Critical)

- [ ] **TRL translated:** Technology readiness explained in accessible terms
- [ ] **Market validation clear:** Customer discovery/pilots framed as traction
- [ ] **No raw metrics:** All data has context and meaning
- [ ] **Confidence calibrated:** Claims match evidence level (no overselling early-stage work)
- [ ] **Business model understandable:** Commercial pathway clear to non-experts

**Reference:** [vianeo-translation-guide.md](vianeo-translation-guide.md)

### Content Completeness (⚠️ High Priority)

- [ ] **All required sections:** Hero, Mission, Innovation, Traction, Commercial, What's Next, 360 Partnership
- [ ] **No placeholder text:** No Lorem ipsum or [TBD] markers
- [ ] **Contact information:** Clear way to get in touch
- [ ] **Attribution complete:** All quotes, data, images properly attributed
- [ ] **Dates current:** All referenced dates are accurate and current

---

## Technical Quality

### Performance (🚨 Critical)

- [ ] **Load time under 3 seconds:** Test on 4G connection (use Chrome DevTools throttling)
- [ ] **Images optimized:** All images compressed, ideally WebP format
- [ ] **No render-blocking:** Critical CSS inline, non-critical deferred
- [ ] **Fonts preconnected:** Google Fonts use preconnect for faster load
- [ ] **No unnecessary libraries:** Only include CSS/JS actually used

**Test Tools:**
- Google PageSpeed Insights: https://pagespeed.web.dev/
- GTmetrix: https://gtmetrix.com/

### Browser Compatibility (⚠️ High Priority)

- [ ] **Chrome works:** Test in latest Chrome (70% market share)
- [ ] **Safari works:** Test in latest Safari (20% market share)
- [ ] **Firefox works:** Test in latest Firefox (8% market share)
- [ ] **Edge works:** Test in latest Edge (Chromium-based)
- [ ] **No console errors:** Check browser console, fix all errors

**Test Method:** Use BrowserStack or manually test in each browser

### Mobile Responsiveness (🚨 Critical)

- [ ] **375px works:** iPhone SE size (smallest common viewport)
- [ ] **768px works:** iPad portrait
- [ ] **1024px works:** iPad landscape / small laptop
- [ ] **1440px+ works:** Desktop
- [ ] **No horizontal scroll:** Never requires side-scrolling
- [ ] **Text readable:** No zooming required to read body text
- [ ] **Touch targets sized:** Buttons/links minimum 44x44px for touch

**Test Method:** Use Chrome DevTools Device Toolbar, test on real devices if possible

### Accessibility - WCAG AA (🚨 Critical)

#### Color Contrast

- [ ] **Body text contrast:** 4.5:1 minimum (16px text on background)
- [ ] **Large text contrast:** 3:1 minimum (24px+ text on background)
- [ ] **UI element contrast:** 3:1 minimum (buttons, icons)
- [ ] **Link contrast:** Distinguishable from body text
- [ ] **Color not only signal:** Information conveyed beyond color alone

**Test Tool:** WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/

#### Keyboard Navigation

- [ ] **Tab works:** Can navigate entire page with Tab key
- [ ] **Logical tab order:** Tab follows visual top-to-bottom, left-to-right
- [ ] **Focus visible:** Clear visual indicator for focused element
- [ ] **No keyboard traps:** Can tab in and out of all interactive elements
- [ ] **Skip to main:** Skip link for screen reader users

**Test Method:** Disconnect mouse, navigate site with keyboard only

#### Screen Reader Support

- [ ] **Alt text present:** Every image has descriptive alt attribute
- [ ] **Alt text meaningful:** Describes content, not "image" or filename
- [ ] **Heading hierarchy:** H1 → H2 → H3 progression (no skipping)
- [ ] **Semantic HTML:** Use `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`
- [ ] **ARIA when needed:** aria-label on complex elements
- [ ] **Links descriptive:** Link text explains destination (not "click here")

**Test Tools:**
- WAVE Browser Extension: https://wave.webaim.org/extension/
- Lighthouse (Chrome DevTools): Run Accessibility audit

#### Forms (if present)

- [ ] **Labels present:** Every input has associated label
- [ ] **Error messages clear:** Validation errors explain what's wrong
- [ ] **Required fields marked:** Visually and semantically
- [ ] **Autocomplete enabled:** Use autocomplete attributes where applicable

### Code Quality (ℹ️ Standard)

- [ ] **Valid HTML:** No unclosed tags or syntax errors
- [ ] **Semantic markup:** Use appropriate HTML5 elements
- [ ] **CSS organized:** Logical structure, commented sections
- [ ] **No inline styles:** CSS in stylesheet, not style attributes
- [ ] **JavaScript unobtrusive:** Site works with JS disabled (enhanced experience with JS)

**Test Tool:** W3C Validator: https://validator.w3.org/

---

## SEO Basics

### Meta Tags (⚠️ High Priority)

- [ ] **Title tag present:** Descriptive title under 60 characters
- [ ] **Meta description:** Compelling description under 155 characters
- [ ] **Viewport meta:** `<meta name="viewport" content="width=device-width, initial-scale=1">`
- [ ] **Open Graph tags:** og:title, og:description, og:type for social sharing
- [ ] **Favicon:** Site icon present and loads correctly

### Content Structure (ℹ️ Standard)

- [ ] **One H1:** Single H1 per page (venture name)
- [ ] **Heading hierarchy:** H2, H3, H4 used appropriately
- [ ] **Descriptive URLs:** If multi-page, URLs are human-readable
- [ ] **Image filenames:** Descriptive names (not IMG_1234.jpg)
- [ ] **Internal links:** Use descriptive anchor text

---

## Content Accuracy

### Factual Verification (🚨 Critical)

- [ ] **Team names correct:** All names spelled correctly
- [ ] **Titles accurate:** Roles and titles are current
- [ ] **Dates accurate:** All referenced dates are correct
- [ ] **Metrics verified:** All numbers match source data
- [ ] **Company names correct:** Partner/client organizations spelled correctly
- [ ] **Links work:** All external and internal links functional

### Grammar & Spelling (⚠️ High Priority)

- [ ] **No typos:** Run spell check
- [ ] **Grammar correct:** Use Grammarly or similar tool
- [ ] **Consistent capitalization:** Product names, company names consistent
- [ ] **Consistent formatting:** Dates, numbers formatted uniformly
- [ ] **Punctuation correct:** Check quotes, commas, apostrophes

**Test Method:** Copy all text to Grammarly or Hemingway Editor

---

## Client-Specific Checks

### Brand Alignment (if client has established brand)

- [ ] **Logo correct:** Latest version, high resolution
- [ ] **Brand colors:** Using client's official color palette
- [ ] **Tone matches:** Writing style aligns with client's voice
- [ ] **Messaging consistent:** Key messages match client's positioning
- [ ] **Legal names:** Official legal entity name if required

### Stakeholder Review (⚠️ High Priority)

- [ ] **Founder approval:** Client founder/CEO has reviewed and approved
- [ ] **Technical accuracy:** Technical details verified by team
- [ ] **360 approval:** 360 team has reviewed for brand consistency
- [ ] **Legal clear:** No confidential information exposed
- [ ] **Sensitivities addressed:** Cultural/political sensitivities considered

---

## Deployment Readiness

### Pre-Deploy (🚨 Critical)

- [ ] **File named correctly:** `index.html` for root deploy
- [ ] **Images included:** All images accessible (not local-only paths)
- [ ] **External resources:** CDN links for fonts, libraries work
- [ ] **Analytics ready:** Google Analytics or tracking code if needed
- [ ] **Domain ready:** Custom domain configured if applicable

### Post-Deploy Verification (🚨 Critical)

- [ ] **Live URL works:** Site loads at deployed URL
- [ ] **All pages load:** No 404 errors
- [ ] **Images load:** All images display correctly
- [ ] **Links work:** All internal and external links functional
- [ ] **Mobile test:** View on actual mobile device
- [ ] **Share test:** Preview looks good when shared on social media

### Handoff Documentation (⚠️ High Priority)

- [ ] **Update instructions:** Client knows how to make simple text changes
- [ ] **Deployment process:** Instructions for redeploying after edits
- [ ] **Contact for issues:** Clear point of contact for technical problems
- [ ] **Analytics access:** Client has access to analytics if implemented

---

## Final Pre-Launch Checklist

Go through each critical (🚨) item one final time:

**Strategic:**
- [ ] Value proposition clear in 10 seconds
- [ ] Target audience alignment confirmed
- [ ] Credibility: no overselling, specific metrics

**Design:**
- [ ] 360 brand present but client is hero
- [ ] Visual hierarchy guides eye naturally

**Content:**
- [ ] Non-specialist can understand without questions
- [ ] Vianeo data translated to accessible language
- [ ] All sections complete, no placeholders

**Technical:**
- [ ] Loads under 3 seconds on 4G
- [ ] Mobile responsive at 375px, 768px, 1024px, 1440px+
- [ ] WCAG AA accessible (contrast, keyboard, screen reader)

**Accuracy:**
- [ ] Names, titles, dates verified correct
- [ ] All metrics match source data
- [ ] Client approval obtained

**Deployment:**
- [ ] File ready (index.html, images included)
- [ ] Live URL tested and works
- [ ] Client has update instructions

---

## Success Criteria

Portfolio is ready to launch when:

1. ✅ **All 🚨 Critical items pass**
2. ✅ **At least 80% of ⚠️ High Priority items pass**
3. ✅ **Client has approved final version**
4. ✅ **Deployed URL loads correctly on desktop and mobile**

---

## Common Issues & Fixes

### "Portfolio looks too corporate"
**Check:**
- [ ] Asymmetry is intentional (not centered everything)
- [ ] White space is generous (not cramped)
- [ ] Typography pairing (serif + sans, not single font)
- [ ] Color used sparingly (not rainbow effect)

**Fix:** Reference [design-standards.md](design-standards.md)

### "Content too technical"
**Check:**
- [ ] TRL translated to accessible language
- [ ] Jargon defined or avoided
- [ ] Concrete examples used

**Fix:** Reference [vianeo-translation-guide.md](vianeo-translation-guide.md)

### "Mobile layout broken"
**Check:**
- [ ] Grid columns stack on mobile (1fr not multi-column)
- [ ] Font sizes readable (min 16px body text)
- [ ] Touch targets sized (min 44x44px)
- [ ] No horizontal scroll

**Fix:** Add mobile breakpoints, test at 375px

### "Slow load time"
**Check:**
- [ ] Images optimized (compressed, WebP format)
- [ ] CSS minified
- [ ] No unused JavaScript libraries

**Fix:** Use TinyPNG, inline critical CSS

---

**Last Updated:** 2025-11-16
**Version:** 1.0.0

---

**Remember:** Quality > Speed. Better to launch 2 hours late with high quality than rush a mediocre portfolio.
