/**
 * Main entry point for standalone HTML builds
 *
 * This file is used by Vite to create standalone HTML versions of the dashboard.
 * For library imports, use index.ts instead.
 */

import React from 'react'
import ReactDOM from 'react-dom/client'
import { VianeoPersonaExplorer } from './VianeoPersonaExplorer'
import { createSampleDashboardData } from './utils/dataTransformer'

// Create sample data for demonstration
const sampleData = createSampleDashboardData()

// Render the app
const root = ReactDOM.createRoot(document.getElementById('root')!)
root.render(
  <React.StrictMode>
    <VianeoPersonaExplorer data={sampleData} />
  </React.StrictMode>
)
