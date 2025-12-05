/**
 * Accessibility Tests for Vianeo Persona Dashboard
 *
 * Tests WCAG 2.1 AA compliance using jest-axe.
 * These tests verify that the dashboard components meet
 * accessibility standards as documented in design-director requirements.
 */

import React from 'react'
import { render, screen } from '@testing-library/react'
import { describe, it, expect } from 'vitest'
import { axe, toHaveNoViolations } from 'jest-axe'

// Extend expect with axe matchers
expect.extend(toHaveNoViolations)

// Import components
import { VianeoPersonaExplorer } from '../src/VianeoPersonaExplorer'
import { PersonaCard } from '../src/components/PersonaCard'
import { LayerNavigation } from '../src/components/LayerNavigation'
import { LayerContent } from '../src/components/LayerContent'
import { EvidenceQuote } from '../src/components/EvidenceQuote'
import { ValidationBadge } from '../src/components/ValidationBadge'
import { createSampleDashboardData } from '../src/utils/dataTransformer'
import type { Persona, PersonaColors, ValidationConfig, LayerMeta, Layer1Content } from '../src/types'

// Sample data for testing
const sampleData = createSampleDashboardData()

const mockColors: PersonaColors = {
  border: '#3B82F6',
  accent: '#2563EB',
  stat: '#1D4ED8',
  subtle: '#DBEAFE'
}

const mockPersona: Persona = {
  type: 'partner',
  title: 'Test Persona',
  subtitle: 'Test subtitle',
  validationStatus: 'validated',
  interviewCount: 5,
  qualityScore: 4,
  evidenceSummary: 'Based on 5 interviews',
  layers: [
    { id: 'layer1', number: '1', title: 'Layer 1', subtitle: 'Who They Are' },
    { id: 'layer2', number: '2', title: 'Layer 2', subtitle: 'Their World' },
    { id: 'layer3', number: '3', title: 'Layer 3', subtitle: 'Challenges' },
    { id: 'layer4', number: '4', title: 'Layer 4', subtitle: 'Solutions' }
  ]
}

const mockValidatedConfig: ValidationConfig = {
  label: 'Validated',
  color: '#059669',
  bgColor: '#D1FAE5',
  icon: '✓'
}

const mockLayerContent: Layer1Content = {
  title: 'Layer 1: Who They Are',
  fields: [
    { label: 'Name', content: 'Dr. Maria', source: 'Interview #1' },
    { label: 'Role', content: 'Director', source: 'Interview #2' }
  ],
  quotes: [
    { text: 'Test quote', author: 'Dr. Maria', source: 'Interview #1' }
  ]
}

describe('Accessibility Tests', () => {
  describe('VianeoPersonaExplorer', () => {
    it('should have no accessibility violations', async () => {
      const { container } = render(<VianeoPersonaExplorer data={sampleData} />)
      const results = await axe(container)
      expect(results).toHaveNoViolations()
    })
  })

  describe('PersonaCard', () => {
    it('should have no accessibility violations', async () => {
      const { container } = render(
        <PersonaCard
          id="test-persona"
          persona={mockPersona}
          isActive={false}
          onClick={() => {}}
          colors={mockColors}
        />
      )
      const results = await axe(container)
      expect(results).toHaveNoViolations()
    })

    it('should have no violations when active', async () => {
      const { container } = render(
        <PersonaCard
          id="test-persona"
          persona={mockPersona}
          isActive={true}
          onClick={() => {}}
          colors={mockColors}
        />
      )
      const results = await axe(container)
      expect(results).toHaveNoViolations()
    })
  })

  describe('LayerNavigation', () => {
    it('should have no accessibility violations', async () => {
      const layers: LayerMeta[] = mockPersona.layers
      const { container } = render(
        <LayerNavigation
          layers={layers}
          activeLayer="layer1"
          onLayerClick={() => {}}
          colors={mockColors}
        />
      )
      const results = await axe(container)
      expect(results).toHaveNoViolations()
    })

    it('should have no violations with no active layer', async () => {
      const layers: LayerMeta[] = mockPersona.layers
      const { container } = render(
        <LayerNavigation
          layers={layers}
          activeLayer={null}
          onLayerClick={() => {}}
          colors={mockColors}
        />
      )
      const results = await axe(container)
      expect(results).toHaveNoViolations()
    })
  })

  describe('LayerContent', () => {
    it('should have no accessibility violations for field-based layers', async () => {
      const { container } = render(
        <LayerContent
          layerId="layer1"
          content={mockLayerContent}
          colors={mockColors}
        />
      )
      const results = await axe(container)
      expect(results).toHaveNoViolations()
    })

    it('should have no violations for section-based layers', async () => {
      const sectionContent = {
        title: 'Layer 3: Challenges',
        sections: [
          { label: 'Tasks', items: ['Task 1', 'Task 2'] },
          { label: 'Pains', items: ['Pain 1', 'Pain 2'] }
        ]
      }
      const { container } = render(
        <LayerContent
          layerId="layer3"
          content={sectionContent}
          colors={mockColors}
        />
      )
      const results = await axe(container)
      expect(results).toHaveNoViolations()
    })

    it('should have no violations for content-based layers', async () => {
      const contentBasedLayer = {
        title: 'Layer 4: Solutions',
        content: 'Current solutions description',
        source: 'Interview data',
        gaps: ['Gap 1', 'Gap 2']
      }
      const { container } = render(
        <LayerContent
          layerId="layer4"
          content={contentBasedLayer}
          colors={mockColors}
        />
      )
      const results = await axe(container)
      expect(results).toHaveNoViolations()
    })
  })

  describe('EvidenceQuote', () => {
    it('should have no accessibility violations', async () => {
      const { container } = render(
        <EvidenceQuote
          quote={{ text: 'Test quote', author: 'Author', source: 'Interview #1' }}
          colors={mockColors}
        />
      )
      const results = await axe(container)
      expect(results).toHaveNoViolations()
    })
  })

  describe('ValidationBadge', () => {
    it('should have no accessibility violations for validated status', async () => {
      const { container } = render(
        <ValidationBadge
          status="validated"
          config={mockValidatedConfig}
        />
      )
      const results = await axe(container)
      expect(results).toHaveNoViolations()
    })

    it('should have no violations for inferred status', async () => {
      const inferredConfig: ValidationConfig = {
        label: 'Inferred',
        color: '#D97706',
        bgColor: '#FEF3C7',
        icon: '?'
      }
      const { container } = render(
        <ValidationBadge
          status="inferred"
          config={inferredConfig}
        />
      )
      const results = await axe(container)
      expect(results).toHaveNoViolations()
    })

    it('should have no violations for hybrid status', async () => {
      const hybridConfig: ValidationConfig = {
        label: 'Hybrid',
        color: '#6366F1',
        bgColor: '#E0E7FF',
        icon: '~'
      }
      const { container } = render(
        <ValidationBadge
          status="hybrid"
          config={hybridConfig}
        />
      )
      const results = await axe(container)
      expect(results).toHaveNoViolations()
    })
  })
})

describe('Semantic Structure Tests', () => {
  it('VianeoPersonaExplorer should have proper heading hierarchy', () => {
    render(<VianeoPersonaExplorer data={sampleData} />)

    // Should have h1 as the main title
    const h1 = screen.getByRole('heading', { level: 1 })
    expect(h1).toBeInTheDocument()
  })

  it('VianeoPersonaExplorer should have semantic landmarks', () => {
    render(<VianeoPersonaExplorer data={sampleData} />)

    // Should have header, main content areas
    expect(screen.getByRole('banner')).toBeInTheDocument() // header
  })

  it('PersonaCard should be focusable with keyboard', () => {
    render(
      <PersonaCard
        id="test-persona"
        persona={mockPersona}
        isActive={false}
        onClick={() => {}}
        colors={mockColors}
      />
    )

    const card = screen.getByRole('button')
    expect(card).toHaveAttribute('tabIndex', '0')
  })

  it('LayerNavigation buttons should be keyboard accessible', () => {
    const layers: LayerMeta[] = mockPersona.layers
    render(
      <LayerNavigation
        layers={layers}
        activeLayer="layer1"
        onLayerClick={() => {}}
        colors={mockColors}
      />
    )

    const buttons = screen.getAllByRole('button')
    buttons.forEach(button => {
      expect(button).toHaveAttribute('tabIndex', '0')
    })
  })

  it('ValidationBadge should have status role for screen readers', () => {
    render(
      <ValidationBadge
        status="validated"
        config={mockValidatedConfig}
      />
    )

    expect(screen.getByRole('status')).toBeInTheDocument()
  })

  it('EvidenceQuote should use figure/figcaption semantics', () => {
    render(
      <EvidenceQuote
        quote={{ text: 'Test quote', author: 'Author', source: 'Interview #1' }}
        colors={mockColors}
      />
    )

    expect(screen.getByRole('figure')).toBeInTheDocument()
  })
})
