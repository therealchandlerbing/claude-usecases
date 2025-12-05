/**
 * Tests for Supabase service functions
 */

import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest'

// Mock Supabase
vi.mock('@supabase/supabase-js', () => ({
  createClient: vi.fn(() => ({
    from: vi.fn(() => ({
      select: vi.fn().mockReturnThis(),
      eq: vi.fn().mockReturnThis(),
      gt: vi.fn().mockReturnThis(),
      lt: vi.fn().mockReturnThis(),
      in: vi.fn().mockReturnThis(),
      is: vi.fn().mockReturnThis(),
      not: vi.fn().mockReturnThis(),
      order: vi.fn().mockReturnThis(),
      update: vi.fn().mockReturnThis(),
      insert: vi.fn().mockReturnThis(),
    })),
    rpc: vi.fn(),
  })),
}))

describe('Supabase Service', () => {
  beforeEach(() => {
    vi.resetModules()
  })

  afterEach(() => {
    vi.clearAllMocks()
  })

  describe('getMockActionData', () => {
    it('should return correctly structured mock action data', async () => {
      // Set env vars to empty to force mock data
      const originalUrl = process.env.NEXT_PUBLIC_SUPABASE_URL
      const originalKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY
      process.env.NEXT_PUBLIC_SUPABASE_URL = ''
      process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY = ''

      // Re-import to get new module with empty env vars
      const { fetchActionData } = await import('../src/services/supabase.js')
      const data = await fetchActionData()

      expect(data).toHaveProperty('pending')
      expect(data).toHaveProperty('attention')
      expect(data.pending).toHaveProperty('relationships')
      expect(data.pending).toHaveProperty('service_interests')
      expect(data.pending).toHaveProperty('commitments_ours')
      expect(data.pending).toHaveProperty('commitments_theirs')
      expect(data.pending).toHaveProperty('objections')
      expect(data.pending).toHaveProperty('signals')
      expect(data.attention).toHaveProperty('cooling')
      expect(data.attention).toHaveProperty('overdue_ours')
      expect(data.attention).toHaveProperty('overdue_theirs')

      // Restore env vars
      process.env.NEXT_PUBLIC_SUPABASE_URL = originalUrl
      process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY = originalKey
    })
  })

  describe('getMockIntelligenceData', () => {
    it('should return correctly structured mock intelligence data', async () => {
      // Set env vars to empty to force mock data
      const originalUrl = process.env.NEXT_PUBLIC_SUPABASE_URL
      const originalKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY
      process.env.NEXT_PUBLIC_SUPABASE_URL = ''
      process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY = ''

      const { fetchIntelligenceData } = await import('../src/services/supabase.js')
      const data = await fetchIntelligenceData()

      expect(data).toHaveProperty('personas')
      expect(data).toHaveProperty('services')
      expect(data).toHaveProperty('competitors')
      expect(data).toHaveProperty('objection_patterns')
      expect(Array.isArray(data.personas)).toBe(true)
      expect(Array.isArray(data.services)).toBe(true)
      expect(Array.isArray(data.competitors)).toBe(true)
      expect(Array.isArray(data.objection_patterns)).toBe(true)

      // Restore env vars
      process.env.NEXT_PUBLIC_SUPABASE_URL = originalUrl
      process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY = originalKey
    })
  })

  describe('updatePushStatus mock mode', () => {
    it('should return success in mock mode', async () => {
      const originalUrl = process.env.NEXT_PUBLIC_SUPABASE_URL
      const originalKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY
      process.env.NEXT_PUBLIC_SUPABASE_URL = ''
      process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY = ''

      const { updatePushStatus } = await import('../src/services/supabase.js')
      const result = await updatePushStatus('relationships', '123', 'approved')

      expect(result).toEqual({ success: true })

      process.env.NEXT_PUBLIC_SUPABASE_URL = originalUrl
      process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY = originalKey
    })
  })

  describe('pushToAsana mock mode', () => {
    it('should return success in mock mode', async () => {
      const originalUrl = process.env.NEXT_PUBLIC_SUPABASE_URL
      const originalKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY
      process.env.NEXT_PUBLIC_SUPABASE_URL = ''
      process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY = ''

      const { pushToAsana } = await import('../src/services/supabase.js')
      const result = await pushToAsana({
        id: '123',
        table: 'relationships',
        name: 'Test Contact'
      })

      expect(result).toEqual({ success: true })

      process.env.NEXT_PUBLIC_SUPABASE_URL = originalUrl
      process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY = originalKey
    })
  })

  describe('resolveCommitment mock mode', () => {
    it('should return success in mock mode', async () => {
      const originalUrl = process.env.NEXT_PUBLIC_SUPABASE_URL
      const originalKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY
      process.env.NEXT_PUBLIC_SUPABASE_URL = ''
      process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY = ''

      const { resolveCommitment } = await import('../src/services/supabase.js')
      const result = await resolveCommitment('123')

      expect(result).toEqual({ success: true })

      process.env.NEXT_PUBLIC_SUPABASE_URL = originalUrl
      process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY = originalKey
    })
  })

  describe('logReachOut mock mode', () => {
    it('should return success in mock mode', async () => {
      const originalUrl = process.env.NEXT_PUBLIC_SUPABASE_URL
      const originalKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY
      process.env.NEXT_PUBLIC_SUPABASE_URL = ''
      process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY = ''

      const { logReachOut } = await import('../src/services/supabase.js')
      const result = await logReachOut('123')

      expect(result).toEqual({ success: true })

      process.env.NEXT_PUBLIC_SUPABASE_URL = originalUrl
      process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY = originalKey
    })
  })

  describe('saveToPlaybook', () => {
    it('should return success', async () => {
      const { saveToPlaybook } = await import('../src/services/supabase.js')
      const result = await saveToPlaybook({
        type: 'pricing',
        count: 5
      })

      expect(result).toEqual({ success: true })
    })
  })
})
