/**
 * Unit tests for dataTransformer utilities
 *
 * These tests validate the markdown parsing and data transformation logic.
 */

import { describe, it, expect } from 'vitest'
import {
  parsePersonaType,
  parseValidationStatus,
  extractQuotes,
  extractBulletPoints,
  parseQualityScore,
  parseInterviewCount,
  exportToJSON,
  importFromJSON,
  ImportValidationError,
} from '../src/utils/dataTransformer'

describe('dataTransformer - Persona Type Parsing', () => {
  it('should parse partner type correctly', () => {
    expect(parsePersonaType('Strategic Partner Organization')).toBe('partner')
    expect(parsePersonaType('PARTNER')).toBe('partner')
    expect(parsePersonaType('This is a partner persona')).toBe('partner')
  })

  it('should parse innovator type correctly', () => {
    expect(parsePersonaType('Academic Innovator')).toBe('innovator')
    expect(parsePersonaType('INNOVATOR')).toBe('innovator')
  })

  it('should parse stakeholder type correctly', () => {
    expect(parsePersonaType('Key Stakeholder')).toBe('stakeholder')
    expect(parsePersonaType('STAKEHOLDER')).toBe('stakeholder')
  })

  it('should parse beneficiary type correctly', () => {
    expect(parsePersonaType('Program Beneficiary')).toBe('beneficiary')
    expect(parsePersonaType('BENEFICIARY')).toBe('beneficiary')
  })

  it('should default to partner for unknown types', () => {
    expect(parsePersonaType('Unknown Type')).toBe('partner')
    expect(parsePersonaType('')).toBe('partner')
  })
})

describe('dataTransformer - Validation Status Parsing', () => {
  it('should parse validated status correctly', () => {
    expect(parseValidationStatus('Validated')).toBe('validated')
    expect(parseValidationStatus('Status: Validated')).toBe('validated')
    expect(parseValidationStatus('VALIDATED')).toBe('validated')
  })

  it('should parse inferred status correctly', () => {
    expect(parseValidationStatus('Inferred')).toBe('inferred')
    expect(parseValidationStatus('Not yet validated')).toBe('inferred')
    expect(parseValidationStatus('INFERRED')).toBe('inferred')
  })

  it('should parse hybrid status correctly', () => {
    expect(parseValidationStatus('Hybrid')).toBe('hybrid')
    expect(parseValidationStatus('Partial validation')).toBe('hybrid')
    expect(parseValidationStatus('HYBRID')).toBe('hybrid')
  })

  it('should not confuse "not validated" with "validated"', () => {
    expect(parseValidationStatus('Not validated')).toBe('inferred')
  })

  it('should default to inferred for unknown statuses', () => {
    expect(parseValidationStatus('Unknown')).toBe('inferred')
    expect(parseValidationStatus('')).toBe('inferred')
  })
})

describe('dataTransformer - Quote Extraction', () => {
  it('should extract quotes with author and source', () => {
    const markdown = '"This is a great quote" - Dr. Smith, Interview #1'
    const quotes = extractQuotes(markdown)

    expect(quotes).toHaveLength(1)
    expect(quotes[0].text).toBe('This is a great quote')
    expect(quotes[0].author).toBe('Dr. Smith')
    expect(quotes[0].source).toBe('Interview #1')
  })

  it('should extract quotes with en-dash separator', () => {
    const markdown = '"Another quote" – Jane Doe, Meeting Notes'
    const quotes = extractQuotes(markdown)

    expect(quotes).toHaveLength(1)
    expect(quotes[0].text).toBe('Another quote')
    expect(quotes[0].author).toBe('Jane Doe')
  })

  it('should default source to "Interview" when not provided', () => {
    const markdown = '"Quote without source" - Author Name'
    const quotes = extractQuotes(markdown)

    expect(quotes).toHaveLength(1)
    expect(quotes[0].source).toBe('Interview')
  })

  it('should extract multiple quotes from text', () => {
    const markdown = `
      "First quote" - Author One, Source A
      Some text in between
      "Second quote" - Author Two, Source B
    `
    const quotes = extractQuotes(markdown)

    expect(quotes).toHaveLength(2)
    expect(quotes[0].text).toBe('First quote')
    expect(quotes[1].text).toBe('Second quote')
  })

  it('should return empty array when no quotes found', () => {
    const markdown = 'Text without any quotes'
    const quotes = extractQuotes(markdown)

    expect(quotes).toHaveLength(0)
  })
})

describe('dataTransformer - Bullet Point Extraction', () => {
  it('should extract dash-style bullet points', () => {
    const markdown = `
- First bullet point
- Second bullet point
- Third bullet point
    `
    const bullets = extractBulletPoints(markdown)

    expect(bullets).toHaveLength(3)
    expect(bullets[0]).toBe('First bullet point')
    expect(bullets[1]).toBe('Second bullet point')
    expect(bullets[2]).toBe('Third bullet point')
  })

  it('should extract asterisk-style bullet points', () => {
    const markdown = `
* First item
* Second item
* Third item
    `
    const bullets = extractBulletPoints(markdown)

    expect(bullets).toHaveLength(3)
    expect(bullets[0]).toBe('First item')
  })

  it('should extract numbered list items', () => {
    const markdown = `
1. First numbered item
2. Second numbered item
3. Third numbered item
    `
    const bullets = extractBulletPoints(markdown)

    expect(bullets).toHaveLength(3)
    expect(bullets[0]).toBe('First numbered item')
    expect(bullets[1]).toBe('Second numbered item')
  })

  it('should handle mixed list styles', () => {
    const markdown = `
- Dash item
* Asterisk item
1. Numbered item
    `
    const bullets = extractBulletPoints(markdown)

    expect(bullets).toHaveLength(3)
  })

  it('should return empty array when no bullets found', () => {
    const markdown = 'Text without bullets'
    const bullets = extractBulletPoints(markdown)

    expect(bullets).toHaveLength(0)
  })
})

describe('dataTransformer - Quality Score Parsing', () => {
  it('should parse score from "score: X" format', () => {
    expect(parseQualityScore('Quality score: 4')).toBe(4)
    expect(parseQualityScore('Score 5')).toBe(5)
    expect(parseQualityScore('SCORE: 3')).toBe(3)
  })

  it('should parse score from "X/5" format', () => {
    expect(parseQualityScore('Rating: 4/5')).toBe(4)
    expect(parseQualityScore('3 / 5')).toBe(3)
  })

  it('should default to 3 when no score found', () => {
    expect(parseQualityScore('No score here')).toBe(3)
    expect(parseQualityScore('')).toBe(3)
  })
})

describe('dataTransformer - Interview Count Parsing', () => {
  it('should parse interview count correctly', () => {
    expect(parseInterviewCount('Based on 8 interviews')).toBe(8)
    expect(parseInterviewCount('5 interview sessions')).toBe(5)
    expect(parseInterviewCount('12 INTERVIEWS')).toBe(12)
  })

  it('should return 0 when no count found', () => {
    expect(parseInterviewCount('No interviews mentioned')).toBe(0)
    expect(parseInterviewCount('')).toBe(0)
  })
})

describe('dataTransformer - JSON Export/Import', () => {
  it('should export dashboard data to JSON string', () => {
    const data = {
      personas: {},
      layerContent: {},
      metadata: {
        projectName: 'Test Project',
        createdDate: '2024-11-20',
        version: '1.0',
      },
    }

    const json = exportToJSON(data)
    expect(typeof json).toBe('string')
    expect(json).toContain('Test Project')
  })

  it('should import dashboard data from JSON string', () => {
    const originalData = {
      personas: {},
      layerContent: {},
      metadata: {
        projectName: 'Test Project',
        createdDate: '2024-11-20',
        version: '1.0',
      },
    }

    const json = JSON.stringify(originalData)
    const importedData = importFromJSON(json)

    expect(importedData).toEqual(originalData)
    expect(importedData.metadata?.projectName).toBe('Test Project')
  })

  // Validation tests
  describe('importFromJSON validation', () => {
    it('should throw ImportValidationError for invalid JSON', () => {
      expect(() => importFromJSON('not valid json')).toThrow(ImportValidationError)
      expect(() => importFromJSON('not valid json')).toThrow(/Invalid JSON/)
    })

    it('should throw ImportValidationError for non-object root', () => {
      expect(() => importFromJSON('null')).toThrow(ImportValidationError)
      expect(() => importFromJSON('null')).toThrow(/must be an object/)
      expect(() => importFromJSON('"string"')).toThrow(/must be an object/)
    })

    it('should throw ImportValidationError for array root', () => {
      // Array is technically an object but should fail validation for missing personas
      expect(() => importFromJSON('[]')).toThrow(/missing or invalid "personas" object/)
    })

    it('should throw ImportValidationError for missing personas', () => {
      const data = { layerContent: {} }
      expect(() => importFromJSON(JSON.stringify(data))).toThrow(/missing or invalid "personas" object/)
    })

    it('should throw ImportValidationError for missing layerContent', () => {
      const data = { personas: {} }
      expect(() => importFromJSON(JSON.stringify(data))).toThrow(/missing or invalid "layerContent" object/)
    })

    it('should throw ImportValidationError for array personas', () => {
      const data = { personas: [], layerContent: {} }
      expect(() => importFromJSON(JSON.stringify(data))).toThrow(/missing or invalid "personas" object/)
    })

    it('should throw ImportValidationError for array layerContent', () => {
      const data = { personas: {}, layerContent: [] }
      expect(() => importFromJSON(JSON.stringify(data))).toThrow(/missing or invalid "layerContent" object/)
    })

    it('should throw ImportValidationError for invalid persona type', () => {
      const data = {
        personas: {
          'test': {
            type: 'invalid_type',
            title: 'Test',
            layers: []
          }
        },
        layerContent: {}
      }
      expect(() => importFromJSON(JSON.stringify(data))).toThrow(/type must be one of/)
    })

    it('should throw ImportValidationError for missing persona title', () => {
      const data = {
        personas: {
          'test': {
            type: 'partner',
            layers: []
          }
        },
        layerContent: {}
      }
      expect(() => importFromJSON(JSON.stringify(data))).toThrow(/missing or invalid "title" field/)
    })

    it('should throw ImportValidationError for missing persona layers', () => {
      const data = {
        personas: {
          'test': {
            type: 'partner',
            title: 'Test'
          }
        },
        layerContent: {}
      }
      expect(() => importFromJSON(JSON.stringify(data))).toThrow(/missing or invalid "layers" array/)
    })

    it('should throw ImportValidationError for invalid layer content', () => {
      const data = {
        personas: {},
        layerContent: {
          'layer1': {
            title: 'Layer 1'
            // missing fields, sections, or content
          }
        }
      }
      expect(() => importFromJSON(JSON.stringify(data))).toThrow(/must have "fields", "sections", or "content"/)
    })

    it('should throw ImportValidationError for layer content missing title', () => {
      const data = {
        personas: {},
        layerContent: {
          'layer1': {
            fields: []
          }
        }
      }
      expect(() => importFromJSON(JSON.stringify(data))).toThrow(/missing or invalid "title" field/)
    })

    it('should throw ImportValidationError for invalid metadata type', () => {
      const data = {
        personas: {},
        layerContent: {},
        metadata: 'invalid'
      }
      expect(() => importFromJSON(JSON.stringify(data))).toThrow(/"metadata" must be an object/)
    })

    it('should accept valid complete data', () => {
      const data = {
        personas: {
          'test-persona': {
            type: 'partner',
            title: 'Test Partner',
            subtitle: 'Test',
            validationStatus: 'validated',
            interviewCount: 3,
            qualityScore: 4,
            evidenceSummary: 'Test evidence',
            layers: [{ id: 'layer1', number: '1', title: 'L1', subtitle: 'Layer 1' }]
          }
        },
        layerContent: {
          'layer1': {
            title: 'Layer 1: Test',
            fields: [{ label: 'Name', content: 'Test', source: 'Interview' }]
          }
        },
        metadata: {
          projectName: 'Test',
          createdDate: '2024-01-01',
          version: '1.0'
        }
      }
      const result = importFromJSON(JSON.stringify(data))
      expect(result).toEqual(data)
    })

    it('should accept valid layer content with sections', () => {
      const data = {
        personas: {},
        layerContent: {
          'layer3': {
            title: 'Layer 3: Activities',
            sections: [{ label: 'Tasks', items: ['Task 1', 'Task 2'] }]
          }
        }
      }
      const result = importFromJSON(JSON.stringify(data))
      expect(result).toEqual(data)
    })

    it('should accept valid layer content with content string', () => {
      const data = {
        personas: {},
        layerContent: {
          'layer4': {
            title: 'Layer 4: Solutions',
            content: 'Current solution description',
            source: 'Interview'
          }
        }
      }
      const result = importFromJSON(JSON.stringify(data))
      expect(result).toEqual(data)
    })
  })

  it('should round-trip export and import correctly', () => {
    const originalData = {
      personas: {
        'test-persona': {
          type: 'partner' as const,
          title: 'Test Partner',
          subtitle: 'Test Subtitle',
          validationStatus: 'validated' as const,
          interviewCount: 5,
          qualityScore: 4,
          evidenceSummary: 'Test evidence',
          layers: [],
        },
      },
      layerContent: {},
      metadata: {
        projectName: 'Round Trip Test',
        createdDate: '2024-11-20',
        version: '1.0',
      },
    }

    const json = exportToJSON(originalData)
    const importedData = importFromJSON(json)

    expect(importedData).toEqual(originalData)
  })
})
