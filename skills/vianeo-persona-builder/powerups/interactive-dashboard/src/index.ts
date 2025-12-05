/**
 * Vianeo Persona Interactive Dashboard
 *
 * Main export file for the interactive dashboard powerup.
 * Import this file to use the dashboard in your application.
 */

// Main component
export { VianeoPersonaExplorer } from './VianeoPersonaExplorer';
export { default } from './VianeoPersonaExplorer';

// Component exports
export { PersonaCard } from './components/PersonaCard';
export { LayerNavigation } from './components/LayerNavigation';
export { LayerContent } from './components/LayerContent';
export { ValidationBadge } from './components/ValidationBadge';
export { EvidenceQuote } from './components/EvidenceQuote';

// Type exports
export type {
  PersonaType,
  ValidationStatus,
  PersonaColors,
  ValidationConfig,
  LayerMeta,
  PersonaField,
  PersonaSection,
  Quote,
  Layer1Content,
  Layer2Content,
  Layer3Content,
  Layer4Content,
  LayerContent,
  Persona,
  LayerContentMap,
  DashboardData,
  PersonaCardProps,
  LayerNavigationProps,
  LayerContentProps,
  EvidenceQuoteProps,
  ValidationBadgeProps,
  ExportOptions
} from './types';

// Utility exports
export {
  parsePersonaType,
  parseValidationStatus,
  extractQuotes,
  extractBulletPoints,
  parseQualityScore,
  parseInterviewCount,
  createSampleDashboardData,
  exportToJSON,
  importFromJSON,
  ImportValidationError
} from './utils/dataTransformer';

// Type guards
export {
  isLayer1Content,
  isLayer2Content,
  isLayer3Content,
  isLayer4Content
} from './types';
