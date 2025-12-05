/**
 * Unit tests for PersonaCard component
 */

import { describe, it, expect, vi } from 'vitest'
import { render, screen, fireEvent } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { PersonaCard } from '../../src/components/PersonaCard'
import { PERSONA_TYPE_COLORS } from '../../src/constants'
import type { Persona, PersonaColors } from '../../src/types'

describe('PersonaCard', () => {
  const defaultPersona: Persona = {
    type: 'partner',
    title: 'Maria Santos',
    subtitle: 'Deputy Director of Technology Transfer',
    validationStatus: 'validated',
    interviewCount: 8,
    qualityScore: 4,
    evidenceSummary: 'Based on interviews with university TTO staff',
    layers: [
      { id: 'layer1', number: '1', title: 'Requester', subtitle: 'Who They Are' },
      { id: 'layer2', number: '2', title: 'Field of Application', subtitle: 'Their World' },
      { id: 'layer3', number: '3', title: 'Activities & Challenges', subtitle: 'What They Do' },
      { id: 'layer4', number: '4', title: 'Current Solutions', subtitle: 'What They Use' },
    ],
  }

  const defaultColors: PersonaColors = PERSONA_TYPE_COLORS.partner
  const mockOnClick = vi.fn()

  const renderPersonaCard = (
    persona = defaultPersona,
    isActive = false,
    colors = defaultColors,
    onClick = mockOnClick
  ) => {
    return render(
      <PersonaCard
        id="test-persona"
        persona={persona}
        isActive={isActive}
        onClick={onClick}
        colors={colors}
      />
    )
  }

  beforeEach(() => {
    mockOnClick.mockClear()
  })

  describe('Rendering', () => {
    it('should render persona title', () => {
      renderPersonaCard()

      expect(screen.getByText('Maria Santos')).toBeInTheDocument()
    })

    it('should render persona subtitle', () => {
      renderPersonaCard()

      expect(
        screen.getByText('Deputy Director of Technology Transfer')
      ).toBeInTheDocument()
    })

    it('should render persona type badge', () => {
      renderPersonaCard()

      expect(screen.getByText('partner')).toBeInTheDocument()
    })

    it('should render validation badge', () => {
      renderPersonaCard()

      expect(screen.getByText('Validated')).toBeInTheDocument()
    })

    it('should render interview count', () => {
      renderPersonaCard()

      expect(screen.getByText('8')).toBeInTheDocument()
      expect(screen.getByText('Interviews')).toBeInTheDocument()
    })

    it('should render quality score', () => {
      renderPersonaCard()

      expect(screen.getByText('4/5')).toBeInTheDocument()
      expect(screen.getByText('Quality Score')).toBeInTheDocument()
    })
  })

  describe('Different persona types', () => {
    const personaTypes = ['partner', 'innovator', 'stakeholder', 'beneficiary'] as const

    personaTypes.forEach((type) => {
      it(`should render ${type} persona type correctly`, () => {
        const persona = { ...defaultPersona, type }
        const colors = PERSONA_TYPE_COLORS[type]

        render(
          <PersonaCard
            id={`${type}-persona`}
            persona={persona}
            isActive={false}
            onClick={mockOnClick}
            colors={colors}
          />
        )

        expect(screen.getByText(type)).toBeInTheDocument()
      })
    })
  })

  describe('Validation statuses', () => {
    it('should render validated status', () => {
      const persona = { ...defaultPersona, validationStatus: 'validated' as const }
      renderPersonaCard(persona)

      expect(screen.getByText('Validated')).toBeInTheDocument()
    })

    it('should render inferred status', () => {
      const persona = { ...defaultPersona, validationStatus: 'inferred' as const }
      renderPersonaCard(persona)

      expect(screen.getByText('Not Yet Validated')).toBeInTheDocument()
    })

    it('should render hybrid status', () => {
      const persona = { ...defaultPersona, validationStatus: 'hybrid' as const }
      renderPersonaCard(persona)

      expect(screen.getByText('Partially Validated')).toBeInTheDocument()
    })
  })

  describe('Click handling', () => {
    it('should call onClick when clicked', async () => {
      renderPersonaCard()

      const card = screen.getByRole('button')
      await userEvent.click(card)

      expect(mockOnClick).toHaveBeenCalledTimes(1)
    })

    it('should call onClick when Enter key pressed', () => {
      renderPersonaCard()

      const card = screen.getByRole('button')
      fireEvent.keyPress(card, { key: 'Enter', code: 'Enter', charCode: 13 })

      expect(mockOnClick).toHaveBeenCalledTimes(1)
    })

    it('should call onClick when Space key pressed', () => {
      renderPersonaCard()

      const card = screen.getByRole('button')
      fireEvent.keyPress(card, { key: ' ', code: 'Space', charCode: 32 })

      expect(mockOnClick).toHaveBeenCalledTimes(1)
    })

    it('should not call onClick for other keys', () => {
      renderPersonaCard()

      const card = screen.getByRole('button')
      fireEvent.keyPress(card, { key: 'a', code: 'KeyA', charCode: 65 })

      expect(mockOnClick).not.toHaveBeenCalled()
    })
  })

  describe('Accessibility', () => {
    it('should have role="button"', () => {
      renderPersonaCard()

      expect(screen.getByRole('button')).toBeInTheDocument()
    })

    it('should have tabIndex="0"', () => {
      renderPersonaCard()

      const card = screen.getByRole('button')
      expect(card).toHaveAttribute('tabindex', '0')
    })

    it('should have aria-pressed="false" when not active', () => {
      renderPersonaCard(defaultPersona, false)

      const card = screen.getByRole('button')
      expect(card).toHaveAttribute('aria-pressed', 'false')
    })

    it('should have aria-pressed="true" when active', () => {
      renderPersonaCard(defaultPersona, true)

      const card = screen.getByRole('button')
      expect(card).toHaveAttribute('aria-pressed', 'true')
    })

    it('should have descriptive aria-label', () => {
      renderPersonaCard()

      expect(
        screen.getByLabelText('Select Maria Santos persona')
      ).toBeInTheDocument()
    })

    it('should have aria-label for persona type', () => {
      renderPersonaCard()

      expect(screen.getByLabelText('Persona type: partner')).toBeInTheDocument()
    })

    it('should have aria-label for interview count', () => {
      renderPersonaCard()

      expect(
        screen.getByLabelText('8 interviews conducted')
      ).toBeInTheDocument()
    })

    it('should have aria-label for quality score', () => {
      renderPersonaCard()

      expect(
        screen.getByLabelText('Quality score: 4 out of 5')
      ).toBeInTheDocument()
    })
  })

  describe('Active state', () => {
    it('should apply active styles when active', () => {
      renderPersonaCard(defaultPersona, true)

      const card = screen.getByRole('button')
      expect(card).toHaveStyle({
        background: defaultColors.accent,
        transform: 'translateY(-2px)',
      })
    })

    it('should not apply active styles when inactive', () => {
      renderPersonaCard(defaultPersona, false)

      const card = screen.getByRole('button')
      expect(card).toHaveStyle({
        background: '#ffffff',
        transform: 'translateY(0)',
      })
    })
  })

  describe('Edge cases', () => {
    it('should handle zero interview count', () => {
      const persona = { ...defaultPersona, interviewCount: 0 }
      renderPersonaCard(persona)

      expect(screen.getByText('0')).toBeInTheDocument()
    })

    it('should handle maximum quality score', () => {
      const persona = { ...defaultPersona, qualityScore: 5 }
      renderPersonaCard(persona)

      expect(screen.getByText('5/5')).toBeInTheDocument()
    })

    it('should handle minimum quality score', () => {
      const persona = { ...defaultPersona, qualityScore: 1 }
      renderPersonaCard(persona)

      expect(screen.getByText('1/5')).toBeInTheDocument()
    })

    it('should handle long title', () => {
      const persona = {
        ...defaultPersona,
        title: 'Dr. Maria Elena Santos Rodriguez de la Cruz',
      }
      renderPersonaCard(persona)

      expect(
        screen.getByText('Dr. Maria Elena Santos Rodriguez de la Cruz')
      ).toBeInTheDocument()
    })

    it('should handle long subtitle', () => {
      const persona = {
        ...defaultPersona,
        subtitle:
          'Deputy Director of Technology Transfer and Innovation Partnerships Division',
      }
      renderPersonaCard(persona)

      expect(
        screen.getByText(
          'Deputy Director of Technology Transfer and Innovation Partnerships Division'
        )
      ).toBeInTheDocument()
    })
  })
})
