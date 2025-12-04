/**
 * Unit tests for EvidenceQuote component
 */

import { describe, it, expect } from 'vitest'
import { render, screen } from '@testing-library/react'
import { EvidenceQuote } from '../../src/components/EvidenceQuote'
import { PERSONA_TYPE_COLORS } from '../../src/constants'
import type { Quote, PersonaColors } from '../../src/types'

describe('EvidenceQuote', () => {
  const defaultQuote: Quote = {
    text: 'This is a sample quote from an interview',
    author: 'Dr. Maria Santos',
    source: 'Interview #3',
  }

  const defaultColors: PersonaColors = PERSONA_TYPE_COLORS.partner

  describe('Rendering', () => {
    it('should render quote text', () => {
      render(<EvidenceQuote quote={defaultQuote} colors={defaultColors} />)

      expect(screen.getByText(/This is a sample quote/)).toBeInTheDocument()
    })

    it('should render author name', () => {
      render(<EvidenceQuote quote={defaultQuote} colors={defaultColors} />)

      expect(screen.getByText('Dr. Maria Santos')).toBeInTheDocument()
    })

    it('should render source', () => {
      render(<EvidenceQuote quote={defaultQuote} colors={defaultColors} />)

      expect(screen.getByText('Interview #3')).toBeInTheDocument()
    })

    it('should wrap quote in quotation marks', () => {
      render(<EvidenceQuote quote={defaultQuote} colors={defaultColors} />)

      const blockquote = screen.getByRole('figure').querySelector('blockquote')
      expect(blockquote).toBeInTheDocument()
      expect(blockquote?.textContent).toContain('"')
    })

    it('should use cite element for author', () => {
      render(<EvidenceQuote quote={defaultQuote} colors={defaultColors} />)

      const cite = screen.getByRole('figure').querySelector('cite')
      expect(cite).toBeInTheDocument()
      expect(cite?.textContent).toBe('Dr. Maria Santos')
    })
  })

  describe('Accessibility', () => {
    it('should have role="figure"', () => {
      render(<EvidenceQuote quote={defaultQuote} colors={defaultColors} />)

      expect(screen.getByRole('figure')).toBeInTheDocument()
    })

    it('should have aria-label for evidence quote', () => {
      render(<EvidenceQuote quote={defaultQuote} colors={defaultColors} />)

      expect(screen.getByLabelText('Evidence quote')).toBeInTheDocument()
    })
  })

  describe('Different persona type colors', () => {
    const personaTypes = ['partner', 'innovator', 'stakeholder', 'beneficiary'] as const

    personaTypes.forEach((type) => {
      it(`should apply ${type} colors to author`, () => {
        const colors = PERSONA_TYPE_COLORS[type]

        render(<EvidenceQuote quote={defaultQuote} colors={colors} />)

        const cite = screen.getByRole('figure').querySelector('cite')
        expect(cite).toHaveStyle({ color: colors.stat })
      })
    })
  })

  describe('Various quote content', () => {
    it('should handle long quotes', () => {
      const longQuote: Quote = {
        text: 'This is a very long quote that spans multiple lines and contains a lot of information about the stakeholder perspective and their experiences with the current solution implementation process.',
        author: 'John Smith',
        source: 'Focus Group Session 2',
      }

      render(<EvidenceQuote quote={longQuote} colors={defaultColors} />)

      expect(screen.getByText(/This is a very long quote/)).toBeInTheDocument()
    })

    it('should handle short quotes', () => {
      const shortQuote: Quote = {
        text: 'Yes, exactly.',
        author: 'Anonymous',
        source: 'Survey',
      }

      render(<EvidenceQuote quote={shortQuote} colors={defaultColors} />)

      expect(screen.getByText(/Yes, exactly/)).toBeInTheDocument()
    })

    it('should handle quotes with special characters', () => {
      const specialQuote: Quote = {
        text: "We've seen 50% improvement & better ROI",
        author: "O'Brien",
        source: 'Meeting Notes',
      }

      render(<EvidenceQuote quote={specialQuote} colors={defaultColors} />)

      expect(screen.getByText(/50% improvement/)).toBeInTheDocument()
      expect(screen.getByText("O'Brien")).toBeInTheDocument()
    })
  })

  describe('Styling', () => {
    it('should apply italic style to blockquote', () => {
      render(<EvidenceQuote quote={defaultQuote} colors={defaultColors} />)

      const blockquote = screen.getByRole('figure').querySelector('blockquote')
      expect(blockquote).toHaveStyle({ fontStyle: 'italic' })
    })

    it('should have rounded border', () => {
      render(<EvidenceQuote quote={defaultQuote} colors={defaultColors} />)

      const figure = screen.getByRole('figure')
      expect(figure).toHaveStyle({ borderRadius: '6px' })
    })
  })
})
