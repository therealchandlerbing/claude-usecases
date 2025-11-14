# Integration Guide: Vianeo Persona Interactive Dashboard

This guide walks you through integrating the Interactive Dashboard with Vianeo Persona Builder output.

## Table of Contents

1. [Quick Integration](#quick-integration)
2. [Converting Persona Builder Output](#converting-persona-builder-output)
3. [Framework-Specific Guides](#framework-specific-guides)
4. [Data Mapping Reference](#data-mapping-reference)
5. [Advanced Integration](#advanced-integration)

---

## Quick Integration

### Step 1: Install Dependencies

```bash
npm install react react-dom
npm install -D typescript @types/react @types/react-dom
```

### Step 2: Copy Dashboard Files

```bash
# Copy to your project
cp -r skills/vianeo-persona-builder/powerups/interactive-dashboard ./src/components/persona-dashboard
```

### Step 3: Import and Use

```tsx
import { VianeoPersonaExplorer } from './components/persona-dashboard/src/VianeoPersonaExplorer';
import data from './data/personas.json';

function App() {
  return <VianeoPersonaExplorer data={data} />;
}
```

---

## Converting Persona Builder Output

### From Strategic Version to Dashboard JSON

The Vianeo Persona Builder generates personas in markdown format. Here's how to convert them to dashboard JSON:

#### Manual Conversion Process

1. **Identify Personas**
   - Count how many distinct personas are in your output
   - Note the persona type for each (partner, innovator, stakeholder, beneficiary)

2. **Extract Metadata**
   - Title and subtitle
   - Validation status (look for badges: ✓ Validated, ⚠ Inferred, ◐ Partial)
   - Interview count
   - Quality score

3. **Map Layer Content**
   - Layer 1: Extract Name, Age, Life/Motivations, Personality/Values
   - Layer 2: Extract Thinks/Feels, Observes, Does, Others Say
   - Layer 3: Extract Tasks, Pains, Expectations (as bullet lists)
   - Layer 4: Extract Current Solutions paragraph and gaps

4. **Extract Evidence**
   - Quotes with attribution
   - Source references
   - Interview numbers

#### Example Conversion

**Persona Builder Output (Markdown):**

```markdown
## Persona: Maria

**Type:** Partner
**Validation Status:** ⭐ Validated (Score 4)
**Sources:** 8 interviews

### Layer 1: Requester (Who They Are)

**Name:** Maria
**Age:** 42

**Life / Motivations:**
Maria serves as Deputy Director of a university technology transfer office...

**Evidence Notes:**
- "I want to see our innovations help people" (Interview 3)
```

**Dashboard JSON:**

```json
{
  "personas": {
    "maria": {
      "type": "partner",
      "title": "Maria",
      "subtitle": "Deputy Director of University Tech Transfer",
      "validationStatus": "validated",
      "interviewCount": 8,
      "qualityScore": 4,
      "evidenceSummary": "Based on 8 interviews with university staff",
      "layers": [...]
    }
  },
  "layerContent": {
    "maria-layer1": {
      "title": "Layer 1: Who They Are",
      "fields": [
        {
          "label": "Name",
          "content": "Maria",
          "source": "Interview #1"
        },
        {
          "label": "Age",
          "content": "42",
          "source": "Interview #1"
        }
      ],
      "quotes": [
        {
          "text": "I want to see our innovations help people",
          "author": "Maria",
          "source": "Interview 3"
        }
      ]
    }
  }
}
```

---

## Framework-Specific Guides

### Next.js Integration

**1. Create a page component:**

```tsx
// pages/personas.tsx
import { VianeoPersonaExplorer } from '@/components/persona-dashboard/src/VianeoPersonaExplorer';
import { DashboardData } from '@/components/persona-dashboard/src/types';

export async function getStaticProps() {
  // Load data from JSON file or API
  const data: DashboardData = await import('../data/personas.json');

  return {
    props: { data },
    revalidate: 3600 // Regenerate every hour
  };
}

export default function PersonasPage({ data }: { data: DashboardData }) {
  return (
    <div>
      <VianeoPersonaExplorer data={data} />
    </div>
  );
}
```

**2. With dynamic routes:**

```tsx
// pages/personas/[id].tsx
export async function getStaticPaths() {
  const personas = await loadAllPersonas();

  return {
    paths: personas.map(p => ({ params: { id: p.id } })),
    fallback: false
  };
}

export async function getStaticProps({ params }) {
  const data = await loadPersonaData(params.id);
  return { props: { data } };
}
```

### Vite Integration

**1. Setup:**

```bash
npm create vite@latest persona-dashboard -- --template react-ts
cd persona-dashboard
npm install
```

**2. Add dashboard:**

```tsx
// src/App.tsx
import { VianeoPersonaExplorer } from './components/VianeoPersonaExplorer';
import data from './data/personas.json';

function App() {
  return <VianeoPersonaExplorer data={data} />;
}

export default App;
```

**3. Configure for JSON imports:**

```json
// tsconfig.json
{
  "compilerOptions": {
    "resolveJsonModule": true,
    "esModuleInterop": true
  }
}
```

### Create React App Integration

**1. Add to src:**

```bash
cp -r interactive-dashboard src/components/
```

**2. Use in App.tsx:**

```tsx
import { VianeoPersonaExplorer } from './components/interactive-dashboard/src/VianeoPersonaExplorer';
import data from './data/personas.json';

function App() {
  return (
    <div className="App">
      <VianeoPersonaExplorer data={data} />
    </div>
  );
}
```

### Gatsby Integration

```tsx
// src/pages/personas.tsx
import { VianeoPersonaExplorer } from '@/components/VianeoPersonaExplorer';
import { graphql } from 'gatsby';

export default function PersonasPage({ data }) {
  const personaData = data.allPersonasJson.nodes[0];

  return <VianeoPersonaExplorer data={personaData} />;
}

export const query = graphql`
  query {
    allPersonasJson {
      nodes {
        personas {
          ...PersonaFields
        }
      }
    }
  }
`;
```

---

## Data Mapping Reference

### Validation Status Mapping

| Persona Builder | Dashboard JSON | Badge Color |
|----------------|----------------|-------------|
| ✓ Validated | `"validated"` | Green |
| ⚠ Inferred | `"inferred"` | Red |
| ◐ Partial | `"hybrid"` | Orange |

### Quality Score Mapping

| Score | Label | Interview Count |
|-------|-------|----------------|
| 5 | Exceptional | 10+ |
| 4 | Strong | 5-10 |
| 3 | Adequate | 3-5 |
| 2 | Weak | 1-2 |
| 1 | Critical Gap | 0 |

### Layer Structure Mapping

**Layer 1: Requester (Who They Are)**
- Fields: Name, Age, Life/Motivations, Personality/Values
- Format: Field objects with label, content, source

**Layer 2: Field of Application (Their World)**
- Fields: Thinks/Feels, Observes, Does, Others Say
- Format: Field objects with label, content, source

**Layer 3: Activities & Challenges**
- Sections: Tasks/Activities, Pains/Lacks, Expectations/Hopes
- Format: Section objects with label and items array

**Layer 4: Current Solutions**
- Content: Paragraph description
- Gaps: Array of gap descriptions
- Format: Single content object with gaps array

---

## Advanced Integration

### Dynamic Data Loading

```tsx
import { useState, useEffect } from 'react';
import { VianeoPersonaExplorer } from './VianeoPersonaExplorer';
import { DashboardData } from './types';

function DynamicDashboard({ apiUrl }: { apiUrl: string }) {
  const [data, setData] = useState<DashboardData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    fetch(apiUrl)
      .then(res => res.json())
      .then(jsonData => {
        setData(jsonData);
        setLoading(false);
      })
      .catch(err => {
        setError(err);
        setLoading(false);
      });
  }, [apiUrl]);

  if (loading) return <div>Loading personas...</div>;
  if (error) return <div>Error: {error.message}</div>;
  if (!data) return <div>No data available</div>;

  return <VianeoPersonaExplorer data={data} />;
}
```

### Server-Side Data Transformation

```typescript
// server/transform-personas.ts
import { readFile } from 'fs/promises';
import { DashboardData } from '../src/types';

export async function transformPersonaMarkdownToJSON(
  markdownPath: string
): Promise<DashboardData> {
  const markdown = await readFile(markdownPath, 'utf-8');

  // Parse markdown and extract personas
  const data: DashboardData = {
    personas: {},
    layerContent: {},
    metadata: {
      createdDate: new Date().toISOString().split('T')[0],
      version: '1.0'
    }
  };

  // Transformation logic here
  // (This would parse the markdown and populate the data object)

  return data;
}
```

### API Integration

```typescript
// api/personas.ts
import type { NextApiRequest, NextApiResponse } from 'next';
import { DashboardData } from '@/types';

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<DashboardData>
) {
  // Fetch from database or file system
  const data = await loadPersonasFromDatabase();

  res.status(200).json(data);
}
```

### Filtering and Search

```tsx
function FilterableDashboard({ data }: { data: DashboardData }) {
  const [filter, setFilter] = useState<PersonaType | 'all'>('all');

  const filteredData = {
    ...data,
    personas: Object.fromEntries(
      Object.entries(data.personas).filter(([_, persona]) =>
        filter === 'all' || persona.type === filter
      )
    )
  };

  return (
    <>
      <FilterControls filter={filter} onChange={setFilter} />
      <VianeoPersonaExplorer data={filteredData} />
    </>
  );
}
```

---

## Troubleshooting Integration Issues

### TypeScript Errors

**Issue:** Cannot find module './types'

**Solution:** Ensure the path to types.ts is correct:
```tsx
import { DashboardData } from './components/persona-dashboard/src/types';
```

### JSON Import Issues

**Issue:** Cannot import JSON files

**Solution:** Enable JSON imports in tsconfig.json:
```json
{
  "compilerOptions": {
    "resolveJsonModule": true
  }
}
```

### Build Errors

**Issue:** Module not found in production build

**Solution:** Check that all files are included in build:
```json
// tsconfig.json
{
  "include": ["src/**/*", "src/components/persona-dashboard/**/*"]
}
```

### Style Issues

**Issue:** Styles not rendering

**Solution:** Ensure your build tool supports inline styles, or extract to CSS:
```tsx
// Option 1: Use styled-components
import styled from 'styled-components';

// Option 2: Use CSS modules
import styles from './PersonaCard.module.css';
```

---

## Best Practices

1. **Version Control**
   - Keep persona data separate from code
   - Use Git LFS for large JSON files
   - Version your persona data alongside code

2. **Performance**
   - Load data asynchronously
   - Implement pagination for 50+ personas
   - Use React.memo for expensive components

3. **Accessibility**
   - Test with screen readers
   - Ensure keyboard navigation works
   - Maintain proper focus management

4. **Data Management**
   - Validate JSON structure before loading
   - Implement error boundaries
   - Provide fallback UI for missing data

5. **Deployment**
   - Pre-render pages with static data
   - Use CDN for JSON files
   - Implement caching strategies

---

## Next Steps

After integration:

1. **Customize** the dashboard colors and styling
2. **Add** export and sharing features
3. **Implement** search and filtering
4. **Connect** to your data pipeline
5. **Deploy** to production

For more help, see:
- [Main README](README.md)
- [Example usage](examples/usage-example.tsx)
- [Vianeo Persona Builder docs](../../README.md)
