# Examples

This directory contains example usage and sample data for the Vianeo Persona Interactive Dashboard.

## Files

- **sample-data.json** - Example persona data in the expected format
- **usage-example.tsx** - Example React integration code

## Building Standalone and Portable Versions

The standalone HTML and portable JSX versions are now generated via build scripts rather than maintained manually. This ensures they stay in sync with the main codebase.

### Standalone HTML (Single-file dashboard)

Builds a complete, single-file HTML dashboard with all dependencies bundled:

```bash
npm run build:standalone
```

Output: `dist/standalone/index.html`

This creates a fully self-contained HTML file that can be:
- Opened directly in a browser
- Shared via email or chat
- Embedded in documentation
- Deployed to any static hosting

### Portable JSX (For AI/code generation)

Builds a single JSX file optimized for AI code generation and manual integration:

```bash
npm run build:portable
```

Output: `dist/portable.jsx`

This ESM bundle is useful for:
- AI-assisted code integration
- Manual component extraction
- Learning the component structure

### Build All Variants

To build all output formats at once:

```bash
npm run build:all
```

This runs:
1. Library build (`dist/`)
2. Standalone HTML (`dist/standalone/`)
3. Portable JSX (`dist/portable.jsx`)

## Integration Example

See `usage-example.tsx` for how to integrate the dashboard into your own React application:

```tsx
import { VianeoPersonaExplorer, DashboardData } from 'vianeo-persona-interactive-dashboard'

const data: DashboardData = {
  metadata: {
    title: 'My Stakeholder Analysis',
    createdDate: '2024-01-15',
    // ...
  },
  personas: [
    // ... persona data
  ]
}

function App() {
  return <VianeoPersonaExplorer data={data} />
}
```

## Sample Data Format

See `sample-data.json` for the complete data structure. Key elements:

- **metadata**: Dashboard title, dates, research context
- **personas**: Array of persona objects with 4-layer structure
  - Layer 1: Identity (name, archetype, summary)
  - Layer 2: Goals & Frustrations
  - Layer 3: Needs analysis with evidence
  - Layer 4: Solutions with evidence tracking
