/**
 * Unit tests for LayerContent component
 */

import { describe, it, expect } from 'vitest'
import { render, screen } from '@testing-library/react'
import { LayerContent } from '../../src/components/LayerContent'
import { PERSONA_TYPE_COLORS } from '../../src/constants'
import type {
  Layer1Content,
  Layer2Content,
  Layer3Content,
  Layer4Content,
  PersonaColors,
} from '../../src/types'

describe('LayerContent', () => {
  const defaultColors: PersonaColors = PERSONA_TYPE_COLORS.partner

  describe('Field-based layers (Layer 1 & 2)', () => {
    const layer1Content: Layer1Content = {
      title: 'Requester: Who They Are',
      fields: [
        {
          label: 'First Name',
          content: 'Maria',
          source: 'Interview #3',
          validation: 'validated',
        },
        {
          label: 'Role',
          content: 'Deputy Director',
          source: 'Interview #1',
          validation: 'inferred',
        },
      ],
      quotes: [
        {
          text: 'I want to see innovations help people',
          author: 'Maria Santos',
          source: 'Interview #3',
        },
      ],
    }

    it('should render layer title', () => {
      render(
        <LayerContent
          layerId="layer1"
          content={layer1Content}
          colors={defaultColors}
        />
      )

      expect(screen.getByText('Requester: Who They Are')).toBeInTheDocument()
    })

    it('should render field labels', () => {
      render(
        <LayerContent
          layerId="layer1"
          content={layer1Content}
          colors={defaultColors}
        />
      )

      expect(screen.getByText('First Name')).toBeInTheDocument()
      expect(screen.getByText('Role')).toBeInTheDocument()
    })

    it('should render field content', () => {
      render(
        <LayerContent
          layerId="layer1"
          content={layer1Content}
          colors={defaultColors}
        />
      )

      expect(screen.getByText('Maria')).toBeInTheDocument()
      expect(screen.getByText('Deputy Director')).toBeInTheDocument()
    })

    it('should render field evidence sources', () => {
      render(
        <LayerContent
          layerId="layer1"
          content={layer1Content}
          colors={defaultColors}
        />
      )

      // Use getAllByText since "Interview #3" appears in both field source and quote
      expect(screen.getAllByText(/Interview #3/).length).toBeGreaterThanOrEqual(1)
      expect(screen.getByText(/Interview #1/)).toBeInTheDocument()
    })

    it('should render validation badges for fields', () => {
      render(
        <LayerContent
          layerId="layer1"
          content={layer1Content}
          colors={defaultColors}
        />
      )

      expect(screen.getByText('✓ Validated')).toBeInTheDocument()
      expect(screen.getByText('⚠ Not Yet Validated')).toBeInTheDocument()
    })

    it('should render quotes section', () => {
      render(
        <LayerContent
          layerId="layer1"
          content={layer1Content}
          colors={defaultColors}
        />
      )

      expect(screen.getByText('Supporting Evidence')).toBeInTheDocument()
      expect(screen.getByText(/I want to see innovations/)).toBeInTheDocument()
    })

    it('should not render quotes section when no quotes', () => {
      const contentNoQuotes: Layer1Content = {
        ...layer1Content,
        quotes: undefined,
      }

      render(
        <LayerContent
          layerId="layer1"
          content={contentNoQuotes}
          colors={defaultColors}
        />
      )

      expect(screen.queryByText('Supporting Evidence')).not.toBeInTheDocument()
    })

    it('should handle layer 2 content identically', () => {
      const layer2Content: Layer2Content = {
        title: 'Field of Application: Their World',
        fields: [
          {
            label: 'Thinks/Feels',
            content: 'Worried about innovation loss',
            source: 'Survey',
          },
        ],
      }

      render(
        <LayerContent
          layerId="layer2"
          content={layer2Content}
          colors={defaultColors}
        />
      )

      expect(
        screen.getByText('Field of Application: Their World')
      ).toBeInTheDocument()
      expect(screen.getByText('Thinks/Feels')).toBeInTheDocument()
    })
  })

  describe('Section-based layer (Layer 3)', () => {
    const layer3Content: Layer3Content = {
      title: 'Activities & Challenges',
      sections: [
        {
          label: 'Tasks/Activities',
          items: [
            'Review partnership proposals',
            'Coordinate with legal department',
            'Maintain tracking systems',
          ],
          validation: 'validated',
        },
        {
          label: 'Pains/Lacks',
          items: [
            'Spends 10-12 hours on manual updates',
            'Lacks standardized templates',
          ],
          validation: 'hybrid',
        },
      ],
      quotes: [
        {
          text: 'Time tracking data confirms the hours',
          author: 'Research Team',
          source: 'Analysis Report',
        },
      ],
    }

    it('should render layer title', () => {
      render(
        <LayerContent
          layerId="layer3"
          content={layer3Content}
          colors={defaultColors}
        />
      )

      expect(screen.getByText('Activities & Challenges')).toBeInTheDocument()
    })

    it('should render section labels', () => {
      render(
        <LayerContent
          layerId="layer3"
          content={layer3Content}
          colors={defaultColors}
        />
      )

      expect(screen.getByText('Tasks/Activities')).toBeInTheDocument()
      expect(screen.getByText('Pains/Lacks')).toBeInTheDocument()
    })

    it('should render section items', () => {
      render(
        <LayerContent
          layerId="layer3"
          content={layer3Content}
          colors={defaultColors}
        />
      )

      expect(screen.getByText('• Review partnership proposals')).toBeInTheDocument()
      expect(screen.getByText('• Coordinate with legal department')).toBeInTheDocument()
      expect(screen.getByText('• Maintain tracking systems')).toBeInTheDocument()
    })

    it('should render validation badges for sections', () => {
      render(
        <LayerContent
          layerId="layer3"
          content={layer3Content}
          colors={defaultColors}
        />
      )

      expect(screen.getByText('✓ Validated')).toBeInTheDocument()
      expect(screen.getByText('◐ Partially Validated')).toBeInTheDocument()
    })

    it('should render quotes section', () => {
      render(
        <LayerContent
          layerId="layer3"
          content={layer3Content}
          colors={defaultColors}
        />
      )

      expect(screen.getByText('Supporting Evidence')).toBeInTheDocument()
    })
  })

  describe('Current solutions layer (Layer 4)', () => {
    const layer4Content: Layer4Content = {
      title: 'Current Solutions',
      content:
        'Maria uses Excel spreadsheets for project tracking with email for communication.',
      source: 'All 8 interviews mentioned this combination',
      validation: 'validated',
      gaps: [
        'Tools do not integrate with each other',
        'Manual data entry causes errors',
      ],
      quotes: [
        {
          text: 'Tools work but do not talk to each other',
          author: 'Maria',
          source: 'Interview #2',
        },
      ],
    }

    it('should render layer title', () => {
      render(
        <LayerContent
          layerId="layer4"
          content={layer4Content}
          colors={defaultColors}
        />
      )

      expect(screen.getByText('Current Solutions')).toBeInTheDocument()
    })

    it('should render main content', () => {
      render(
        <LayerContent
          layerId="layer4"
          content={layer4Content}
          colors={defaultColors}
        />
      )

      expect(
        screen.getByText(/Maria uses Excel spreadsheets/)
      ).toBeInTheDocument()
    })

    it('should render evidence source', () => {
      render(
        <LayerContent
          layerId="layer4"
          content={layer4Content}
          colors={defaultColors}
        />
      )

      expect(
        screen.getByText(/All 8 interviews mentioned/)
      ).toBeInTheDocument()
    })

    it('should render gaps section', () => {
      render(
        <LayerContent
          layerId="layer4"
          content={layer4Content}
          colors={defaultColors}
        />
      )

      expect(screen.getByText('⚠ Current Solution Gaps')).toBeInTheDocument()
      expect(
        screen.getByText('• Tools do not integrate with each other')
      ).toBeInTheDocument()
      expect(
        screen.getByText('• Manual data entry causes errors')
      ).toBeInTheDocument()
    })

    it('should have role="alert" for gaps section', () => {
      render(
        <LayerContent
          layerId="layer4"
          content={layer4Content}
          colors={defaultColors}
        />
      )

      expect(screen.getByRole('alert')).toBeInTheDocument()
    })

    it('should not render gaps section when no gaps', () => {
      const contentNoGaps: Layer4Content = {
        ...layer4Content,
        gaps: undefined,
      }

      render(
        <LayerContent
          layerId="layer4"
          content={contentNoGaps}
          colors={defaultColors}
        />
      )

      expect(
        screen.queryByText('⚠ Current Solution Gaps')
      ).not.toBeInTheDocument()
    })

    it('should not render gaps section when gaps array is empty', () => {
      const contentEmptyGaps: Layer4Content = {
        ...layer4Content,
        gaps: [],
      }

      render(
        <LayerContent
          layerId="layer4"
          content={contentEmptyGaps}
          colors={defaultColors}
        />
      )

      expect(
        screen.queryByText('⚠ Current Solution Gaps')
      ).not.toBeInTheDocument()
    })
  })

  describe('Edge cases', () => {
    it('should handle empty fields array', () => {
      const emptyFields: Layer1Content = {
        title: 'Empty Layer',
        fields: [],
      }

      render(
        <LayerContent
          layerId="layer1"
          content={emptyFields}
          colors={defaultColors}
        />
      )

      expect(screen.getByText('Empty Layer')).toBeInTheDocument()
    })

    it('should handle empty sections array', () => {
      const emptySections: Layer3Content = {
        title: 'Empty Sections',
        sections: [],
      }

      render(
        <LayerContent
          layerId="layer3"
          content={emptySections}
          colors={defaultColors}
        />
      )

      expect(screen.getByText('Empty Sections')).toBeInTheDocument()
    })

    it('should handle field without validation', () => {
      const noValidationField: Layer1Content = {
        title: 'Test',
        fields: [
          {
            label: 'No Validation Field',
            content: 'Some content',
            source: 'Source',
          },
        ],
      }

      render(
        <LayerContent
          layerId="layer1"
          content={noValidationField}
          colors={defaultColors}
        />
      )

      expect(screen.getByText('No Validation Field')).toBeInTheDocument()
      expect(screen.queryByText('✓ Validated')).not.toBeInTheDocument()
    })
  })

  describe('Different persona colors', () => {
    const layer1Content: Layer1Content = {
      title: 'Test Layer',
      fields: [
        {
          label: 'Test Field',
          content: 'Test content',
          source: 'Test source',
        },
      ],
    }

    const personaTypes = ['partner', 'innovator', 'stakeholder', 'beneficiary'] as const

    personaTypes.forEach((type) => {
      it(`should render with ${type} colors`, () => {
        const colors = PERSONA_TYPE_COLORS[type]

        render(
          <LayerContent
            layerId="layer1"
            content={layer1Content}
            colors={colors}
          />
        )

        expect(screen.getByText('Test Layer')).toBeInTheDocument()
      })
    })
  })
})
