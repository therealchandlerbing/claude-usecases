/**
 * Usage Example: Vianeo Persona Explorer
 *
 * This example demonstrates how to use the VianeoPersonaExplorer component
 * with data from the Vianeo Persona Builder skill.
 */

import React from 'react';
import { VianeoPersonaExplorer } from '../src/VianeoPersonaExplorer';
import { createSampleDashboardData } from '../src/utils/dataTransformer';

/**
 * Example 1: Using sample data
 */
export function ExampleWithSampleData() {
  const data = createSampleDashboardData();

  return <VianeoPersonaExplorer data={data} />;
}

/**
 * Example 2: Loading from JSON file
 */
export function ExampleWithJSONFile() {
  const [data, setData] = React.useState(null);

  React.useEffect(() => {
    // Load data from JSON file
    fetch('./examples/sample-data.json')
      .then((response) => response.json())
      .then((jsonData) => setData(jsonData))
      .catch((error) => console.error('Error loading data:', error));
  }, []);

  if (!data) {
    return <div>Loading...</div>;
  }

  return <VianeoPersonaExplorer data={data} />;
}

/**
 * Example 3: With custom metadata
 */
export function ExampleWithMetadata() {
  const data = {
    ...createSampleDashboardData(),
    metadata: {
      projectName: 'My Innovation Project',
      createdDate: new Date().toISOString().split('T')[0],
      version: '2.0'
    }
  };

  return <VianeoPersonaExplorer data={data} />;
}

/**
 * Example 4: Using in Next.js
 */
export default function PersonaDashboardPage() {
  // In Next.js, you can load data from getStaticProps or getServerSideProps
  const data = createSampleDashboardData();

  return (
    <div>
      <VianeoPersonaExplorer data={data} />
    </div>
  );
}

/**
 * Example 5: Converting Persona Builder output to dashboard format
 *
 * After generating personas with the Vianeo Persona Builder skill:
 * 1. Save the output as markdown
 * 2. Use the data transformer to convert to JSON
 * 3. Load the JSON into the dashboard
 */
export function ExampleWithPersonaBuilderOutput() {
  // This would typically happen in a build step or server-side
  // For now, we'll use sample data
  const data = createSampleDashboardData();

  return <VianeoPersonaExplorer data={data} />;
}
