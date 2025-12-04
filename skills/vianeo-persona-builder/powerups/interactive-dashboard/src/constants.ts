/**
 * Shared constants for Vianeo Persona Interactive Dashboard
 *
 * Centralizes color schemes, validation configurations, and other
 * constants used across multiple components to ensure consistency
 * and eliminate duplication.
 */

import { PersonaType, PersonaColors, ValidationStatus } from './types';

/**
 * Color schemes for different persona types.
 * Each persona type has a coordinated color palette:
 * - border: Primary color for borders and emphasis
 * - accent: Light background color for cards and sections
 * - stat: Dark color for statistics and important numbers
 * - subtle: Very light color for subtle backgrounds
 */
export const PERSONA_TYPE_COLORS: Record<PersonaType, PersonaColors> = {
  partner: {
    border: '#64748b',  // Slate
    accent: '#f8fafc',
    stat: '#475569',
    subtle: '#e2e8f0'
  },
  innovator: {
    border: '#059669',  // Emerald
    accent: '#f0fdf4',
    stat: '#047857',
    subtle: '#d1fae5'
  },
  stakeholder: {
    border: '#7c3aed',  // Violet
    accent: '#faf5ff',
    stat: '#6d28d9',
    subtle: '#e9d5ff'
  },
  beneficiary: {
    border: '#d97706',  // Amber
    accent: '#fffbeb',
    stat: '#b45309',
    subtle: '#fde68a'
  }
} as const;

/**
 * Configuration for validation status badges.
 * Used to display evidence validation state throughout the dashboard.
 */
export interface ValidationStatusConfig {
  label: string;
  color: string;
  bgColor: string;
  icon: string;
}

export const VALIDATION_STATUS_CONFIG: Record<ValidationStatus, ValidationStatusConfig> = {
  validated: {
    label: 'Validated',
    color: '#059669',
    bgColor: '#d1fae5',
    icon: '✓'
  },
  inferred: {
    label: 'Not Yet Validated',
    color: '#dc2626',
    bgColor: '#fee2e2',
    icon: '⚠'
  },
  hybrid: {
    label: 'Partially Validated',
    color: '#d97706',
    bgColor: '#fef3c7',
    icon: '◐'
  }
} as const;

/**
 * Layer metadata configuration.
 * Defines the four layers of the Vianeo framework.
 */
export const LAYER_DEFINITIONS = {
  layer1: {
    number: '1',
    title: 'Requester',
    subtitle: 'Who They Are'
  },
  layer2: {
    number: '2',
    title: 'Field of Application',
    subtitle: 'Their World'
  },
  layer3: {
    number: '3',
    title: 'Activities & Challenges',
    subtitle: 'What They Do'
  },
  layer4: {
    number: '4',
    title: 'Current Solutions',
    subtitle: 'What They Use'
  }
} as const;

/**
 * Default font stack used throughout the dashboard
 */
export const FONT_FAMILY = "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif";

/**
 * Standard border colors used for UI elements
 */
export const BORDER_COLORS = {
  light: '#e7e5e4',
  medium: '#d6d3d1',
  dark: '#a8a29e'
} as const;

/**
 * Text colors for different purposes
 */
export const TEXT_COLORS = {
  primary: '#1a1a1a',
  secondary: '#44403c',
  tertiary: '#57534e',
  muted: '#78716c',
  subtle: '#a8a29e'
} as const;
