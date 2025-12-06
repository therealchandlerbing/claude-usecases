/**
 * Shared Supabase client factory for dashboard applications.
 *
 * Usage:
 * 1. Set environment variables:
 *    - NEXT_PUBLIC_SUPABASE_URL
 *    - NEXT_PUBLIC_SUPABASE_ANON_KEY
 *
 * 2. Import and use:
 *    import { createSupabaseClient, getSupabaseClient } from '@claude-usecases/dashboard-components';
 *
 *    // Create new client
 *    const supabase = createSupabaseClient();
 *
 *    // Or use singleton
 *    const supabase = getSupabaseClient();
 */

import { createClient, SupabaseClient } from '@supabase/supabase-js';

// Singleton instance
let supabaseInstance: SupabaseClient | null = null;

export interface SupabaseConfig {
  url?: string;
  anonKey?: string;
  options?: {
    auth?: {
      autoRefreshToken?: boolean;
      persistSession?: boolean;
    };
    realtime?: {
      params?: {
        eventsPerSecond?: number;
      };
    };
  };
}

/**
 * Get Supabase configuration from environment variables.
 */
function getEnvConfig(): { url: string; anonKey: string } {
  const url = process.env.NEXT_PUBLIC_SUPABASE_URL;
  const anonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;

  if (!url || !anonKey) {
    throw new Error(
      'Missing Supabase configuration. Set NEXT_PUBLIC_SUPABASE_URL and NEXT_PUBLIC_SUPABASE_ANON_KEY environment variables.'
    );
  }

  return { url, anonKey };
}

/**
 * Create a new Supabase client instance.
 *
 * @param config - Optional configuration overrides
 * @returns Supabase client
 *
 * @example
 * // Use environment variables
 * const supabase = createSupabaseClient();
 *
 * @example
 * // With custom options
 * const supabase = createSupabaseClient({
 *   options: {
 *     realtime: { params: { eventsPerSecond: 10 } }
 *   }
 * });
 */
export function createSupabaseClient<T = any>(config?: SupabaseConfig): SupabaseClient<T> {
  const envConfig = getEnvConfig();

  const url = config?.url || envConfig.url;
  const anonKey = config?.anonKey || envConfig.anonKey;

  return createClient<T>(url, anonKey, {
    auth: {
      autoRefreshToken: true,
      persistSession: true,
      ...config?.options?.auth,
    },
    realtime: {
      params: {
        eventsPerSecond: 10,
        ...config?.options?.realtime?.params,
      },
    },
    ...config?.options,
  });
}

/**
 * Get the singleton Supabase client instance.
 * Creates the client on first call.
 *
 * @returns Supabase client singleton
 *
 * @example
 * const supabase = getSupabaseClient();
 * const { data } = await supabase.from('table').select('*');
 */
export function getSupabaseClient<T = any>(): SupabaseClient<T> {
  if (!supabaseInstance) {
    supabaseInstance = createSupabaseClient<T>();
  }
  return supabaseInstance as SupabaseClient<T>;
}

/**
 * Reset the singleton instance (useful for testing).
 */
export function resetSupabaseClient(): void {
  supabaseInstance = null;
}

/**
 * Check if Supabase is configured (environment variables are set).
 */
export function isSupabaseConfigured(): boolean {
  try {
    getEnvConfig();
    return true;
  } catch {
    return false;
  }
}
