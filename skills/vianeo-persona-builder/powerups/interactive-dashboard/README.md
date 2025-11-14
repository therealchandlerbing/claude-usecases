# Vianeo Persona Interactive Dashboard

**Category:** Powerup / Optional Add-on
**Purpose:** Interactive visualization and exploration of Vianeo persona data
**Parent Skill:** Vianeo Persona Builder
**Version:** 1.0.0

## Overview

The Vianeo Persona Interactive Dashboard is an optional powerup for the Vianeo Persona Builder skill. It provides a beautiful, interactive React-based interface for exploring validated stakeholder personas with their complete four-layer structure, evidence tracking, and validation status.

### Key Features

✅ **Interactive Exploration** - Click through personas and layers with smooth navigation
✅ **Evidence Tracking** - View quotes, sources, and validation status at every level
✅ **Validation Indicators** - Clear visual badges showing validated vs. inferred content
✅ **Quality Metrics** - Display interview counts and quality scores
✅ **Type-Safe** - Built with TypeScript for reliability and maintainability
✅ **Accessible** - WCAG 2.1 AA compliant with ARIA labels and keyboard navigation
✅ **Modular Architecture** - Clean component structure for easy customization
✅ **Responsive Design** - Works on desktop, tablet, and mobile devices

## When to Use This Powerup

**Use this dashboard when you want to:**
- Present personas to stakeholders in an interactive format
- Share persona insights with team members who can explore at their own pace
- Create a visual reference for validated research findings
- Build a persona library that can be updated over time
- Demonstrate the depth of validation evidence behind personas

**Skip this powerup when:**
- You only need text-based persona documentation
- You're submitting directly to Vianeo platform (use platform-ready format instead)
- You don't have a React/web development environment

## Installation

### Prerequisites

- Node.js 16+ and npm/yarn
- React 18+
- A build tool (Vite, Next.js, Create React App, etc.)

### Quick Start

1. **Copy the dashboard files to your project:**

```bash
# From your project root
cp -r skills/vianeo-persona-builder/powerups/interactive-dashboard ./src/persona-dashboard
```

2. **Install dependencies:**

```bash
npm install react react-dom
npm install -D typescript @types/react @types/react-dom
```

3. **Import and use the component:**

```tsx
import { VianeoPersonaExplorer } from './persona-dashboard/src/VianeoPersonaExplorer';
import dashboardData from './persona-dashboard/examples/sample-data.json';

function App() {
  return <VianeoPersonaExplorer data={dashboardData} />;
}
```

## Data Format

The dashboard expects data in this JSON structure:

```typescript
{
  "personas": {
    "persona-id": {
      "type": "partner" | "innovator" | "stakeholder" | "beneficiary",
      "title": "Persona Title",
      "subtitle": "Brief description",
      "validationStatus": "validated" | "inferred" | "hybrid",
      "interviewCount": 8,
      "qualityScore": 4,
      "evidenceSummary": "Description of evidence sources",
      "layers": [
        { "id": "layer1", "number": "1", "title": "...", "subtitle": "..." }
      ]
    }
  },
  "layerContent": {
    "layer-id": {
      // Layer-specific content structure
    }
  },
  "metadata": {
    "projectName": "Optional project name",
    "createdDate": "2024-11-14",
    "version": "1.0"
  }
}
```

See `examples/sample-data.json` for a complete example.

## Integration with Vianeo Persona Builder

### Workflow

1. **Generate personas** using the Vianeo Persona Builder skill
2. **Convert to JSON** format for the dashboard
3. **Load into dashboard** for interactive exploration
4. **Share** with stakeholders or embed in your application

### Manual Conversion

Currently, you'll need to manually structure your persona builder output into the dashboard JSON format. Follow the structure in `examples/sample-data.json`.

**Future Enhancement:** Automated markdown-to-JSON conversion tool is planned for a future release.

## Component Architecture

```
VianeoPersonaExplorer (Main component)
├── PersonaCard (Persona selection cards)
│   └── ValidationBadge (Validation status indicator)
├── LayerNavigation (4-layer navigation grid)
└── LayerContent (Dynamic layer content display)
    ├── FieldDisplay (Layer 1 & 2 fields)
    ├── SectionDisplay (Layer 3 sections)
    └── EvidenceQuote (Quote/evidence display)
```

### Key Components

- **VianeoPersonaExplorer** - Main container component, manages state
- **PersonaCard** - Individual persona cards with metrics
- **LayerNavigation** - Four-layer navigation interface
- **LayerContent** - Renders appropriate content based on layer type
- **ValidationBadge** - Shows validation status with icon
- **EvidenceQuote** - Displays quotes with attribution

## Customization

### Color Schemes

Persona types have predefined color schemes in `src/VianeoPersonaExplorer.tsx`:

```typescript
const personaTypeColors = {
  partner: { border: '#64748b', accent: '#f8fafc', ... },
  innovator: { border: '#059669', accent: '#f0fdf4', ... },
  stakeholder: { border: '#7c3aed', accent: '#faf5ff', ... },
  beneficiary: { border: '#d97706', accent: '#fffbeb', ... }
};
```

Modify these to match your brand colors.

### Styling

The dashboard uses inline styles for portability. To customize:

1. **Extract styles** to CSS modules or styled-components
2. **Modify inline styles** directly in component files
3. **Override with CSS classes** using your own stylesheet

### Adding Features

The modular architecture makes it easy to add:

- Export to PDF/PNG functionality
- Search and filter capabilities
- Comparison views (side-by-side personas)
- Commenting and annotation features
- Integration with analytics tools

## Accessibility

The dashboard is built with accessibility in mind:

- ✅ Semantic HTML structure
- ✅ ARIA labels and roles
- ✅ Keyboard navigation support (Tab, Enter, Space)
- ✅ Focus management
- ✅ Screen reader friendly
- ✅ Proper heading hierarchy
- ✅ Color contrast compliance

## Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Mobile)

## Performance

The dashboard is optimized for:

- **Small datasets:** 1-10 personas - Instant loading
- **Medium datasets:** 10-50 personas - Fast loading
- **Large datasets:** 50+ personas - Consider pagination

For large datasets, consider implementing:
- Virtual scrolling for persona lists
- Lazy loading of layer content
- Data pagination or filtering

## Deployment Options

### Option 1: Static Site

Build a standalone static site:

```bash
npm run build
# Deploy the dist/ folder to Netlify, Vercel, GitHub Pages, etc.
```

### Option 2: Embed in Existing App

Import the component into your React app:

```tsx
import { VianeoPersonaExplorer } from './persona-dashboard';
import data from './persona-data.json';

<VianeoPersonaExplorer data={data} />
```

### Option 3: Next.js Integration

Use in Next.js with server-side rendering:

```tsx
import { VianeoPersonaExplorer } from '@/components/persona-dashboard';

export async function getStaticProps() {
  const data = await loadPersonaData();
  return { props: { data } };
}

export default function PersonasPage({ data }) {
  return <VianeoPersonaExplorer data={data} />;
}
```

## File Structure

```
interactive-dashboard/
├── README.md                        # This file
├── INTEGRATION.md                   # Integration guide
├── package.json                     # Dependencies
├── src/
│   ├── VianeoPersonaExplorer.tsx   # Main component
│   ├── types.ts                     # TypeScript definitions
│   ├── components/                  # Modular components
│   │   ├── PersonaCard.tsx
│   │   ├── LayerNavigation.tsx
│   │   ├── LayerContent.tsx
│   │   ├── ValidationBadge.tsx
│   │   └── EvidenceQuote.tsx
│   └── utils/
│       └── dataTransformer.ts       # Data utilities
├── examples/
│   ├── sample-data.json             # Example data
│   └── usage-example.tsx            # Usage examples
└── dist/                            # Build output (generated)
```

## Troubleshooting

### Common Issues

**Issue:** TypeScript errors about missing types
**Solution:** Ensure all dependencies are installed: `npm install`

**Issue:** Styles not rendering correctly
**Solution:** Check that your build tool supports inline styles

**Issue:** Data not loading
**Solution:** Validate your JSON structure against `examples/sample-data.json`

**Issue:** Component not rendering
**Solution:** Ensure React 18+ is installed and imported correctly

## Examples

See `examples/` directory for:

- **sample-data.json** - Complete data example with 2 personas
- **usage-example.tsx** - Multiple usage patterns and integration examples

## Future Enhancements

Planned features for future versions:

- [ ] Automated markdown-to-JSON conversion
- [ ] Export to PDF/PNG
- [ ] Comparison view (side-by-side personas)
- [ ] Search and filter functionality
- [ ] Print-friendly version
- [ ] Share links with deep linking to specific layers
- [ ] Comments and annotations
- [ ] Version history tracking
- [ ] Analytics integration

## Support

For issues, questions, or feature requests:

1. Check the [Integration Guide](INTEGRATION.md)
2. Review the [examples](examples/)
3. Consult the main [Vianeo Persona Builder documentation](../../README.md)

## Version History

- **v1.0.0** (2024-11-14) - Initial release
  - Interactive persona exploration
  - Four-layer navigation
  - Evidence tracking and validation status
  - TypeScript support
  - Accessibility features
  - Mobile-responsive design

## License

This powerup is part of the Vianeo Persona Builder skill and follows the same license.

---

**Created with the Vianeo Persona Builder skill**
**Part of the 360 Innovation Toolkit**
