# Design Director Skill - Complete Guide

## What You Now Have

A comprehensive design elevation skill that automatically transforms generic visual outputs into professionally polished work. When you ask Claude to create presentations, dashboards, reports, HTML pages, or any visual content, this skill now ensures the result looks hand-crafted by a professional designer.

## How It Works

The skill activates automatically whenever you request visual outputs. It works invisibly, following this process:

1. **Builds functional version** - Gets content and features working first
2. **Interrogates design** - Systematically questions every design choice
3. **Selects techniques** - Chooses 2-3 specific visual improvements
4. **Applies systematically** - Ensures consistency throughout
5. **Validates quality** - Confirms professional standards are met
6. **Delivers polished result** - You see only the final output

You won't see this process unless you specifically ask. The default behavior is to simply deliver excellent design without explaining the thinking behind it.

## What's Inside the Skill

### Main Instructions (README.md)
The core workflow and triggering conditions. This is what Claude reads first to understand when and how to use the skill.

### Five Reference Files
Comprehensive guides that Claude consults during the design process:

**design-philosophy.md** (4.5 KB)
- Core principles for balancing boldness with restraint
- When to be bold, when to show restraint
- Context-appropriate excellence
- Quality signals and anti-patterns

**interrogation-checklist.md** (6.5 KB)
- Systematic questions for every design element
- Typography, color, layout, hierarchy validation
- Output-specific checks (presentations, spreadsheets, HTML, etc.)
- Red flags that indicate template-quality work

**technique-catalog.md** (11 KB)
- Specific, actionable visual techniques
- Organized by what they achieve (not just "make it pretty")
- Typography, color, layout, data visualization techniques
- Examples: "Headlines 2.5-3x body size, not 1.5x"
- References to Stripe, Linear, Apple approaches

**exemplars.md** (9.5 KB)
- Design patterns from leading systems
- Stripe (dashboards), Linear (interfaces), Apple (elegance)
- Bauhaus and Swiss design principles
- When to reference each exemplar
- How to adapt, not copy

**elevation-protocol.md** (11 KB)
- Systematic 6-phase refinement process
- Time estimates for simple vs. complex outputs
- Phase checklists and quality gates
- Special cases and anti-patterns
- Iteration support

## How to Use

### Basic Usage
Just ask for what you need:
- "Create a sales dashboard"
- "Make a presentation about Q4 strategy"
- "Build an HTML landing page"
- "Design a financial report"

The skill activates automatically. You'll get professional results without seeing the design process.

### Seeing the Design Thinking
If you want to understand the decisions:
- "Show me the design thinking behind this"
- "Explain your design choices"
- "Why did you choose these colors/fonts/layouts?"

### Iterating on Designs
Request changes naturally:
- "Make the colors bolder"
- "Reduce information density"
- "Make this look more like Stripe's style"
- "Increase white space"

The skill maintains consistency while incorporating changes.

## What Changes for You

**Before this skill:**
- Generic "professional" templates
- Default colors, fonts, spacing
- Functional but visually mediocre
- Obvious that it came from AI

**After this skill:**
- Specific design references (Stripe, Linear, Apple)
- Deliberate color palettes and typography
- Hand-crafted appearance
- Looks like a designer made intentional choices

## Examples of Transformation

### Sales Dashboard
**Before**: Default Excel styling, generic blues, cramped layout
**After**: Stripe-inspired palette (#0A2540), 8-point grid spacing, Inter typography with clear hierarchy, subtle shadows for depth

### Presentation Deck
**Before**: Times New Roman, centered text, clip art
**After**: Apple-inspired minimalism, SF Pro typography at 2.5x scale for headlines, generous white space, bold singular color choice per slide

### HTML Landing Page
**Before**: Bootstrap defaults, generic blue buttons, standard spacing
**After**: Linear-inspired interface, #5E6AD2 primary color, 4-point grid system, thoughtful hover states, responsive breakpoints

### Financial Report
**Before**: Dense Arial text, no hierarchy, default table borders
**After**: Swiss-inspired systematic layout, Georgia + Inter pairing, clear typographic scale, subtle zebra striping in tables

## Design References Built In

The skill draws from proven exemplars:

**Stripe** - Trust, clarity, financial interfaces
**Linear** - Modern, efficient, product tools
**Apple** - Elegance, restraint, consumer-facing
**Notion** - Content-first, collaborative
**Bauhaus** - Geometric, bold, systematic
**Swiss Design** - Grid-based, typography-focused

Claude automatically chooses the right reference based on:
- Purpose (persuade, inform, analyze)
- Audience (technical, executive, consumer)
- Information density (high, medium, low)
- Medium (presentation, report, web, dashboard)

## Technical Details

### File Size
Total: 42.5 KB across 6 files
- Efficient for context window
- Progressive disclosure (reads only what's needed)

### Structure
```
design-director/
├── README.md (main documentation)
├── INDEX.md (navigation)
├── COMPLETE-GUIDE.md (this file)
├── QUICK-REFERENCE.md (condensed guide)
├── references/
│   ├── design-philosophy.md (4.5 KB)
│   ├── interrogation-checklist.md (6.5 KB)
│   ├── technique-catalog.md (11 KB)
│   ├── exemplars.md (9.5 KB)
│   └── elevation-protocol.md (11 KB)
└── examples/
    └── README.md (transformation examples)
```

### Reading Strategy
Claude doesn't load everything at once. It uses progressive disclosure:
1. Always reads: README.md (overview)
2. Reads as needed: Specific reference files based on task
3. Never reads: Unnecessary sections

This keeps context usage efficient while maintaining quality.

## Quality Assurance

Every output validated against:
- Would this fit in Stripe/Linear/Apple's design system?
- Does it look hand-crafted, not template-based?
- Are 2-3 signature choices evident?
- Is every choice defensible and intentional?
- Would you include this in a design portfolio?

If any answer is "no," the design is refined until it passes.

## Customization Options

The skill is comprehensive out of the box, but you can:

**Add your brand guidelines:**
Create a new reference file with your colors, fonts, and patterns. Claude will incorporate them alongside Stripe/Linear/Apple references.

**Add industry-specific exemplars:**
If you work in a specific domain (healthcare, finance, education), add reference files showing excellent design in that space.

**Adjust elevation intensity:**
The skill documentation includes time estimates. You can request "quick elevation" for simple outputs or "comprehensive elevation" for high-stakes materials.

## When NOT to Use This Skill

The skill focuses on visual design quality, not:
- Content strategy (what to say)
- Data analysis (what insights to draw)
- Code functionality (how things work)
- Writing quality (prose improvement)

It elevates the visual presentation of content, assuming the content itself is already sound.

## Maintenance and Updates

The skill is complete as delivered. However, you might update it if:
- Design trends shift significantly
- You want to add new exemplars
- Your organization develops brand guidelines
- You discover output types that need special handling

To update: Modify the reference files directly in the repository.

## Success Indicators

You'll know the skill is working when:
- Colleagues ask "Did you hire a designer?"
- Visual outputs feel distinctly more professional
- You stop tweaking formatting manually
- Presentations/reports command more attention
- Design quality matches content quality

## Philosophy Behind the Skill

The skill embodies several key principles:

**Professional, not precious**: Design serves content, never the other way around

**Confidence through restraint**: 2-3 deliberate techniques beat 10 mediocre ones

**Specific over generic**: "Stripe's #0A2540" not "professional blue"

**Borrowed excellence**: Reference the best, adapt for context

**Hand-crafted appearance**: Every choice intentional, nothing default

These principles ensure outputs are elevated without being over-designed.

## Getting the Most Value

**For quick tasks:**
Just ask naturally. The skill handles simple elevation automatically in 15-20 minutes.

**For important deliverables:**
The skill applies comprehensive elevation (50-75 minutes) to high-stakes outputs like board presentations, major proposals, or public-facing materials.

**For iteration:**
Request changes naturally. The skill maintains design consistency while incorporating your feedback.

**For learning:**
Ask "explain your design choices" to understand why specific techniques were applied. This helps you develop design intuition over time.

## Support and Troubleshooting

**If outputs don't look elevated:**
- Ask explicitly: "Apply design-director skill to this"
- Request specific exemplar: "Make this look like Stripe/Linear/Apple"
- Specify intensity: "Comprehensive design elevation needed"

**If design feels over-done:**
- The skill defaults to 2-3 techniques (restraint)
- If you see more, ask: "Simplify this design"
- Reference philosophy: "Apply design-philosophy restraint principles"

**If you need specific style:**
- Mention exemplar: "Reference Linear's approach"
- Specify output: "Optimize for dashboard/presentation/report"
- Request adjustment: "More bold" or "More minimal"

## What Makes This Different

Most design tools give you templates. This skill gives you principles and systematic thinking. It:

- **Interrogates every choice** (no defaults accepted)
- **References proven exemplars** (Stripe, Linear, Apple)
- **Applies specific techniques** (not generic "make it pretty")
- **Ensures consistency** (throughout entire output)
- **Validates quality** (against professional standards)

Result: Outputs that look hand-crafted by someone who understands design, not generated from templates.

## Related Documentation

- **[Quick Reference](QUICK-REFERENCE.md)** - Condensed one-page guide
- **[Main Documentation](README.md)** - Complete skill documentation
- **[File Index](INDEX.md)** - Navigation to all components
- **[Examples](examples/README.md)** - Transformation examples
- **[Design Philosophy](references/design-philosophy.md)** - Core principles
- **[Technique Catalog](references/technique-catalog.md)** - Specific techniques

## Version History

- v1.0 - 2025-11-14 - Initial release with complete documentation
