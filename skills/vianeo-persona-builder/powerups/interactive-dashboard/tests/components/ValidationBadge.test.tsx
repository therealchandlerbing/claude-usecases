/**
 * Unit tests for ValidationBadge component
 */

import { describe, it, expect } from 'vitest'
import { render, screen } from '@testing-library/react'
import { ValidationBadge } from '../../src/components/ValidationBadge'
import { VALIDATION_STATUS_CONFIG } from '../../src/constants'
import type { ValidationStatus } from '../../src/types'

describe('ValidationBadge', () => {
  describe('Rendering', () => {
    it('should render with validated status', () => {
      const config = VALIDATION_STATUS_CONFIG.validated

      render(<ValidationBadge status="validated" config={config} />)

      expect(screen.getByText('Validated')).toBeInTheDocument()
      expect(screen.getByText('✓')).toBeInTheDocument()
    })

    it('should render with inferred status', () => {
      const config = VALIDATION_STATUS_CONFIG.inferred

      render(<ValidationBadge status="inferred" config={config} />)

      expect(screen.getByText('Not Yet Validated')).toBeInTheDocument()
      expect(screen.getByText('⚠')).toBeInTheDocument()
    })

    it('should render with hybrid status', () => {
      const config = VALIDATION_STATUS_CONFIG.hybrid

      render(<ValidationBadge status="hybrid" config={config} />)

      expect(screen.getByText('Partially Validated')).toBeInTheDocument()
      expect(screen.getByText('◐')).toBeInTheDocument()
    })
  })

  describe('Accessibility', () => {
    it('should have role="status"', () => {
      const config = VALIDATION_STATUS_CONFIG.validated

      render(<ValidationBadge status="validated" config={config} />)

      expect(screen.getByRole('status')).toBeInTheDocument()
    })

    it('should have appropriate aria-label for validated status', () => {
      const config = VALIDATION_STATUS_CONFIG.validated

      render(<ValidationBadge status="validated" config={config} />)

      expect(
        screen.getByLabelText('Validation status: Validated')
      ).toBeInTheDocument()
    })

    it('should have appropriate aria-label for inferred status', () => {
      const config = VALIDATION_STATUS_CONFIG.inferred

      render(<ValidationBadge status="inferred" config={config} />)

      expect(
        screen.getByLabelText('Validation status: Not Yet Validated')
      ).toBeInTheDocument()
    })

    it('should have appropriate aria-label for hybrid status', () => {
      const config = VALIDATION_STATUS_CONFIG.hybrid

      render(<ValidationBadge status="hybrid" config={config} />)

      expect(
        screen.getByLabelText('Validation status: Partially Validated')
      ).toBeInTheDocument()
    })

    it('should mark icon as aria-hidden', () => {
      const config = VALIDATION_STATUS_CONFIG.validated

      render(<ValidationBadge status="validated" config={config} />)

      // The icon span should be hidden from screen readers
      const iconSpan = screen.getByText('✓')
      expect(iconSpan).toHaveAttribute('aria-hidden', 'true')
    })
  })

  describe('Styling', () => {
    it('should apply background color from config', () => {
      const config = VALIDATION_STATUS_CONFIG.validated

      render(<ValidationBadge status="validated" config={config} />)

      const badge = screen.getByRole('status')
      expect(badge).toHaveStyle({ background: config.bgColor })
    })

    it('should apply text color from config', () => {
      const config = VALIDATION_STATUS_CONFIG.inferred

      render(<ValidationBadge status="inferred" config={config} />)

      const badge = screen.getByRole('status')
      expect(badge).toHaveStyle({ color: config.color })
    })
  })

  describe('All status types', () => {
    const statuses: ValidationStatus[] = ['validated', 'inferred', 'hybrid']

    statuses.forEach((status) => {
      it(`should render correctly for ${status} status`, () => {
        const config = VALIDATION_STATUS_CONFIG[status]

        render(<ValidationBadge status={status} config={config} />)

        expect(screen.getByText(config.label)).toBeInTheDocument()
        expect(screen.getByText(config.icon)).toBeInTheDocument()
      })
    })
  })
})
