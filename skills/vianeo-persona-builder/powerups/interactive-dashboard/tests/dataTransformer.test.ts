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
  transformMarkdownToData,
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
    expect(importedData.metadata.projectName).toBe('Test Project')
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

describe('dataTransformer - transformMarkdownToData', () => {
  const sampleMarkdown = `
# Example: Partner Persona (Validated)

## Persona: Maria

**Type:** Partner
**Validation Status:** Validated - Strong Quality (Score 4)
**Sources:** 8 interviews with university tech transfer office staff
**Geographic Context:** Brazilian university system

---

### Layer 1: Requester (Who They Are)

**Name:** Maria
**Age:** 42

**Life / Motivations:**
Maria serves as Deputy Director of a university technology transfer office.

**Personality / Values:**
Maria is pragmatic and relationship-oriented.

**Evidence Notes:**
- "I want to see our innovations help people" (Interview 3)

---

### Layer 2: Field of Application (Their World)

**Thinks / Feels:**
Maria worries that valuable university innovations are being lost.

**Observes:**
Maria sees researchers with promising technologies give up.

**Does:**
Maria spends her days reviewing partnership proposals.

**Others Say:**
Colleagues describe Maria as "the person who actually gets things done".

**Evidence Notes:**
- All 8 interviews mentioned spreadsheet tracking system

---

### Layer 3: Activities and Challenges (What They Do and Struggle With)

**Tasks / Activities:**
- Review and process 15-20 partnership proposals monthly
- Coordinate between university legal department and partners
- Maintain tracking systems for all active partnerships

**Pains / Lacks:**
- Spends 10-12 hours weekly on manual status updates
- Lacks standardized templates for common partnership types

**Expectations / Hopes:**
- Reduce partnership approval timeline from 6-8 weeks to 2-3 weeks
- Have clear qualification criteria

**Evidence Notes:**
- 10-12 hour figure from time tracking data

---

### Layer 4: Current Solutions (Their Present Reality)

**Current Solutions:**
Maria currently uses a combination of Excel spreadsheets for project tracking.

**Evidence Notes:**
- Excel + email + DocuSign combination mentioned in all 8 interviews
- "Tools work but don't talk to each other" (Interview 2)
`

  it('should extract persona name correctly', () => {
    const result = transformMarkdownToData(sampleMarkdown, 'partner-maria')
    expect(result.personas).toBeDefined()
    expect(result.personas!['partner-maria'].title).toBe('Maria')
  })

  it('should extract persona type correctly', () => {
    const result = transformMarkdownToData(sampleMarkdown, 'partner-maria')
    expect(result.personas!['partner-maria'].type).toBe('partner')
  })

  it('should extract validation status correctly', () => {
    const result = transformMarkdownToData(sampleMarkdown, 'partner-maria')
    expect(result.personas!['partner-maria'].validationStatus).toBe('validated')
  })

  it('should extract quality score correctly', () => {
    const result = transformMarkdownToData(sampleMarkdown, 'partner-maria')
    expect(result.personas!['partner-maria'].qualityScore).toBe(4)
  })

  it('should extract interview count correctly', () => {
    const result = transformMarkdownToData(sampleMarkdown, 'partner-maria')
    expect(result.personas!['partner-maria'].interviewCount).toBe(8)
  })

  it('should create four layers for the persona', () => {
    const result = transformMarkdownToData(sampleMarkdown, 'partner-maria')
    expect(result.personas!['partner-maria'].layers).toHaveLength(4)
    expect(result.personas!['partner-maria'].layers[0].number).toBe('1')
    expect(result.personas!['partner-maria'].layers[3].number).toBe('4')
  })

  it('should extract Layer 1 fields', () => {
    const result = transformMarkdownToData(sampleMarkdown, 'partner-maria')
    const layer1Id = result.personas!['partner-maria'].layers[0].id
    const layer1 = result.layerContent![layer1Id]

    expect(layer1).toBeDefined()
    expect('fields' in layer1).toBe(true)
    if ('fields' in layer1) {
      expect(layer1.fields.length).toBeGreaterThan(0)
      const nameField = layer1.fields.find(f => f.label === 'First Name')
      expect(nameField).toBeDefined()
      expect(nameField?.content).toBe('Maria')
    }
  })

  it('should extract Layer 2 fields', () => {
    const result = transformMarkdownToData(sampleMarkdown, 'partner-maria')
    const layer2Id = result.personas!['partner-maria'].layers[1].id
    const layer2 = result.layerContent![layer2Id]

    expect(layer2).toBeDefined()
    expect('fields' in layer2).toBe(true)
    if ('fields' in layer2) {
      expect(layer2.fields.length).toBeGreaterThan(0)
      const thinksField = layer2.fields.find(f => f.label === 'Thinks/Feels')
      expect(thinksField).toBeDefined()
    }
  })

  it('should extract Layer 3 sections with items', () => {
    const result = transformMarkdownToData(sampleMarkdown, 'partner-maria')
    const layer3Id = result.personas!['partner-maria'].layers[2].id
    const layer3 = result.layerContent![layer3Id]

    expect(layer3).toBeDefined()
    expect('sections' in layer3).toBe(true)
    if ('sections' in layer3) {
      expect(layer3.sections.length).toBeGreaterThan(0)
      const tasksSection = layer3.sections.find(s => s.label === 'Tasks/Activities')
      expect(tasksSection).toBeDefined()
      expect(tasksSection?.items.length).toBeGreaterThan(0)
    }
  })

  it('should extract Layer 4 content', () => {
    const result = transformMarkdownToData(sampleMarkdown, 'partner-maria')
    const layer4Id = result.personas!['partner-maria'].layers[3].id
    const layer4 = result.layerContent![layer4Id]

    expect(layer4).toBeDefined()
    expect('content' in layer4).toBe(true)
    if ('content' in layer4) {
      expect(layer4.content).toContain('Excel')
    }
  })

  it('should include metadata with current date', () => {
    const result = transformMarkdownToData(sampleMarkdown, 'partner-maria')
    expect(result.metadata).toBeDefined()
    expect(result.metadata!.version).toBe('1.0')
    expect(result.metadata!.createdDate).toMatch(/^\d{4}-\d{2}-\d{2}$/)
  })

  it('should handle minimal markdown gracefully', () => {
    const minimalMarkdown = `
# Simple Persona
**Type:** innovator
`
    const result = transformMarkdownToData(minimalMarkdown, 'minimal')
    expect(result.personas).toBeDefined()
    expect(result.personas!['minimal'].type).toBe('innovator')
    expect(result.personas!['minimal'].layers).toHaveLength(4)
  })

  it('should use personaId for layer IDs', () => {
    const result = transformMarkdownToData(sampleMarkdown, 'test-id')
    const layers = result.personas!['test-id'].layers
    expect(layers[0].id).toBe('test-id-layer1')
    expect(layers[1].id).toBe('test-id-layer2')
    expect(layers[2].id).toBe('test-id-layer3')
    expect(layers[3].id).toBe('test-id-layer4')
  })
})
