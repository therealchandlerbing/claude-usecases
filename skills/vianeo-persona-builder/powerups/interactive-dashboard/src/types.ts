/**
 * Type definitions for Vianeo Persona Interactive Dashboard
 *
 * These types align with the Vianeo four-layer persona structure
 * and support validation tracking, evidence attribution, and quality scoring.
 */

// Persona Types
export type PersonaType = 'partner' | 'innovator' | 'stakeholder' | 'beneficiary';

// Validation Status
export type ValidationStatus = 'validated' | 'inferred' | 'hybrid';

// Color Configuration
export interface PersonaColors {
  border: string;
  accent: string;
  stat: string;
  subtle: string;
}

// Validation Status Configuration
export interface ValidationConfig {
  label: string;
  color: string;
  bgColor: string;
  icon: string;
}

// Layer Definitions
export interface LayerMeta {
  id: string;
  number: string;
  title: string;
  subtitle: string;
}

// Field with Evidence (for Layers 1 & 2)
export interface PersonaField {
  label: string;
  content: string;
  source: string;
  validation?: ValidationStatus;
}

// Section with Items (for Layer 3)
export interface PersonaSection {
  label: string;
  items: string[];
  validation?: ValidationStatus;
}

// Quote/Evidence
export interface Quote {
  text: string;
  author: string;
  source: string;
}

// Layer 1: Requester (Who They Are)
export interface Layer1Content {
  title: string;
  fields: PersonaField[];
  quotes?: Quote[];
}

// Layer 2: Field of Application (Their World)
export interface Layer2Content {
  title: string;
  fields: PersonaField[];
  quotes?: Quote[];
}

// Layer 3: Activities & Challenges
export interface Layer3Content {
  title: string;
  sections: PersonaSection[];
  quotes?: Quote[];
}

// Layer 4: Current Solutions
export interface Layer4Content {
  title: string;
  content: string;
  source: string;
  validation?: ValidationStatus;
  gaps?: string[];
  quotes?: Quote[];
}

// Union type for all layer content
export type LayerContent = Layer1Content | Layer2Content | Layer3Content | Layer4Content;

// Persona Definition
export interface Persona {
  type: PersonaType;
  title: string;
  subtitle: string;
  validationStatus: ValidationStatus;
  interviewCount: number;
  qualityScore: number;
  evidenceSummary: string;
  layers: LayerMeta[];
}

// Complete Layer Content Map
export interface LayerContentMap {
  [layerId: string]: LayerContent;
}

// Dashboard Data Structure
export interface DashboardData {
  personas: {
    [personaId: string]: Persona;
  };
  layerContent: LayerContentMap;
  metadata?: {
    projectName?: string;
    createdDate?: string;
    version?: string;
  };
}

// Component Props
export interface PersonaCardProps {
  id: string;
  persona: Persona;
  isActive: boolean;
  onClick: () => void;
  colors: PersonaColors;
}

export interface LayerNavigationProps {
  layers: LayerMeta[];
  activeLayer: string | null;
  onLayerClick: (layerId: string) => void;
  colors: PersonaColors;
}

export interface LayerContentProps {
  layerId: string;
  content: LayerContent;
  colors: PersonaColors;
}

export interface EvidenceQuoteProps {
  quote: Quote;
  colors: PersonaColors;
}

export interface ValidationBadgeProps {
  status: ValidationStatus;
  config: ValidationConfig;
}

// Export/Import Types
export interface ExportOptions {
  format: 'json' | 'markdown' | 'html';
  includeEvidence?: boolean;
  selectedPersonas?: string[];
}

// Utility type guards

/**
 * Checks if content is field-based (Layer 1 or Layer 2).
 *
 * Note: Layer1Content and Layer2Content are structurally identical
 * (both have `fields` array), so they cannot be distinguished at runtime.
 * This combined guard handles both layer types together.
 */
export function isFieldBasedLayer(content: LayerContent): content is Layer1Content | Layer2Content {
  return 'fields' in content && Array.isArray((content as Layer1Content).fields);
}

/**
 * @deprecated Use isFieldBasedLayer() instead - Layer1 and Layer2 are structurally identical
 */
export function isLayer1Content(content: LayerContent): content is Layer1Content {
  return isFieldBasedLayer(content);
}

/**
 * @deprecated Use isFieldBasedLayer() instead - Layer1 and Layer2 are structurally identical
 */
export function isLayer2Content(content: LayerContent): content is Layer2Content {
  return isFieldBasedLayer(content);
}

export function isLayer3Content(content: LayerContent): content is Layer3Content {
  return 'sections' in content && Array.isArray((content as Layer3Content).sections);
}

export function isLayer4Content(content: LayerContent): content is Layer4Content {
  return 'content' in content && typeof (content as Layer4Content).content === 'string' && 'gaps' in content;
}
