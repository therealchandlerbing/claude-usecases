/**
 * Unit tests for Supabase client
 *
 * These tests validate the Supabase client configuration.
 */

import { describe, it, expect } from 'vitest'
import { supabase, createSupabaseClient } from '../src/lib/supabase'

describe('Supabase Client', () => {
  it('should create a supabase client instance', () => {
    expect(supabase).toBeDefined()
    expect(supabase.auth).toBeDefined()
    expect(supabase.from).toBeDefined()
  })

  it('should create a new supabase client with createSupabaseClient', () => {
    const client = createSupabaseClient()
    expect(client).toBeDefined()
    expect(client.auth).toBeDefined()
    expect(client.from).toBeDefined()
  })

  it('should have environment variables configured', () => {
    expect(process.env.NEXT_PUBLIC_SUPABASE_URL).toBeDefined()
    expect(process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY).toBeDefined()
  })
})
