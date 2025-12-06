/**
 * Shared Dashboard Components
 *
 * Reusable React components and utilities for claude-usecases dashboards.
 *
 * @example
 * import {
 *   ErrorBoundary,
 *   LoadingSpinner,
 *   MetricsCard,
 *   createSupabaseClient
 * } from '@claude-usecases/dashboard-components';
 */

// Components
export {
  ErrorBoundary,
  type ErrorBoundaryProps,
} from './components/ErrorBoundary';

export {
  LoadingSpinner,
  LoadingOverlay,
  LoadingInline,
  type LoadingSpinnerProps,
} from './components/LoadingSpinner';

export {
  MetricsCard,
  MetricsGrid,
  type MetricsCardProps,
} from './components/MetricsCard';

// Supabase utilities
export {
  createSupabaseClient,
  getSupabaseClient,
  resetSupabaseClient,
  isSupabaseConfigured,
  type SupabaseConfig,
} from './lib/supabase';

// Hooks
export { useLocalStorage } from './hooks/useLocalStorage';
