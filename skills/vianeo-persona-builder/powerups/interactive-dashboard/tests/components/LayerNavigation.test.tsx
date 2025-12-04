/**
 * Unit tests for LayerNavigation component
 */

import { describe, it, expect, vi } from 'vitest'
import { render, screen, fireEvent } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { LayerNavigation } from '../../src/components/LayerNavigation'
import { PERSONA_TYPE_COLORS } from '../../src/constants'
import type { LayerMeta, PersonaColors } from '../../src/types'

describe('LayerNavigation', () => {
  const defaultLayers: LayerMeta[] = [
    { id: 'layer1', number: '1', title: 'Requester', subtitle: 'Who They Are' },
    { id: 'layer2', number: '2', title: 'Field of Application', subtitle: 'Their World' },
    { id: 'layer3', number: '3', title: 'Activities & Challenges', subtitle: 'What They Do' },
    { id: 'layer4', number: '4', title: 'Current Solutions', subtitle: 'What They Use' },
  ]

  const defaultColors: PersonaColors = PERSONA_TYPE_COLORS.partner
  const mockOnLayerClick = vi.fn()

  const renderLayerNavigation = (
    layers = defaultLayers,
    activeLayer: string | null = null,
    colors = defaultColors,
    onLayerClick = mockOnLayerClick
  ) => {
    return render(
      <LayerNavigation
        layers={layers}
        activeLayer={activeLayer}
        onLayerClick={onLayerClick}
        colors={colors}
      />
    )
  }

  beforeEach(() => {
    mockOnLayerClick.mockClear()
  })

  describe('Rendering', () => {
    it('should render section title', () => {
      renderLayerNavigation()

      expect(screen.getByText('Vianeo Four-Layer Structure')).toBeInTheDocument()
    })

    it('should render all four layers', () => {
      renderLayerNavigation()

      expect(screen.getByText('Layer 1')).toBeInTheDocument()
      expect(screen.getByText('Layer 2')).toBeInTheDocument()
      expect(screen.getByText('Layer 3')).toBeInTheDocument()
      expect(screen.getByText('Layer 4')).toBeInTheDocument()
    })

    it('should render layer titles', () => {
      renderLayerNavigation()

      expect(screen.getByText('Requester')).toBeInTheDocument()
      expect(screen.getByText('Field of Application')).toBeInTheDocument()
      expect(screen.getByText('Activities & Challenges')).toBeInTheDocument()
      expect(screen.getByText('Current Solutions')).toBeInTheDocument()
    })

    it('should render layer subtitles', () => {
      renderLayerNavigation()

      expect(screen.getByText('Who They Are')).toBeInTheDocument()
      expect(screen.getByText('Their World')).toBeInTheDocument()
      expect(screen.getByText('What They Do')).toBeInTheDocument()
      expect(screen.getByText('What They Use')).toBeInTheDocument()
    })
  })

  describe('Click handling', () => {
    it('should call onLayerClick when layer is clicked', async () => {
      renderLayerNavigation()

      const buttons = screen.getAllByRole('button')
      await userEvent.click(buttons[0])

      expect(mockOnLayerClick).toHaveBeenCalledWith('layer1')
    })

    it('should call onLayerClick with correct layer id for each layer', async () => {
      renderLayerNavigation()

      const buttons = screen.getAllByRole('button')

      await userEvent.click(buttons[1])
      expect(mockOnLayerClick).toHaveBeenCalledWith('layer2')

      await userEvent.click(buttons[2])
      expect(mockOnLayerClick).toHaveBeenCalledWith('layer3')

      await userEvent.click(buttons[3])
      expect(mockOnLayerClick).toHaveBeenCalledWith('layer4')
    })

    it('should call onLayerClick when Enter key is pressed', () => {
      renderLayerNavigation()

      const buttons = screen.getAllByRole('button')
      fireEvent.keyPress(buttons[0], { key: 'Enter', code: 'Enter', charCode: 13 })

      expect(mockOnLayerClick).toHaveBeenCalledWith('layer1')
    })

    it('should call onLayerClick when Space key is pressed', () => {
      renderLayerNavigation()

      const buttons = screen.getAllByRole('button')
      fireEvent.keyPress(buttons[0], { key: ' ', code: 'Space', charCode: 32 })

      expect(mockOnLayerClick).toHaveBeenCalledWith('layer1')
    })

    it('should not call onLayerClick for other keys', () => {
      renderLayerNavigation()

      const buttons = screen.getAllByRole('button')
      fireEvent.keyPress(buttons[0], { key: 'a', code: 'KeyA', charCode: 65 })

      expect(mockOnLayerClick).not.toHaveBeenCalled()
    })
  })

  describe('Accessibility', () => {
    it('should have navigation role', () => {
      renderLayerNavigation()

      expect(screen.getByRole('navigation')).toBeInTheDocument()
    })

    it('should have aria-label for navigation', () => {
      renderLayerNavigation()

      expect(
        screen.getByLabelText('Persona layers navigation')
      ).toBeInTheDocument()
    })

    it('should have role="button" for each layer', () => {
      renderLayerNavigation()

      expect(screen.getAllByRole('button')).toHaveLength(4)
    })

    it('should have tabIndex="0" for each layer', () => {
      renderLayerNavigation()

      const buttons = screen.getAllByRole('button')
      buttons.forEach((button) => {
        expect(button).toHaveAttribute('tabindex', '0')
      })
    })

    it('should have aria-pressed="false" for inactive layers', () => {
      renderLayerNavigation(defaultLayers, null)

      const buttons = screen.getAllByRole('button')
      buttons.forEach((button) => {
        expect(button).toHaveAttribute('aria-pressed', 'false')
      })
    })

    it('should have aria-pressed="true" for active layer', () => {
      renderLayerNavigation(defaultLayers, 'layer2')

      const buttons = screen.getAllByRole('button')
      expect(buttons[0]).toHaveAttribute('aria-pressed', 'false')
      expect(buttons[1]).toHaveAttribute('aria-pressed', 'true')
      expect(buttons[2]).toHaveAttribute('aria-pressed', 'false')
      expect(buttons[3]).toHaveAttribute('aria-pressed', 'false')
    })

    it('should have descriptive aria-label for each layer', () => {
      renderLayerNavigation()

      expect(screen.getByLabelText('View Requester')).toBeInTheDocument()
      expect(screen.getByLabelText('View Field of Application')).toBeInTheDocument()
      expect(screen.getByLabelText('View Activities & Challenges')).toBeInTheDocument()
      expect(screen.getByLabelText('View Current Solutions')).toBeInTheDocument()
    })
  })

  describe('Active state styling', () => {
    it('should apply active styles to active layer', () => {
      renderLayerNavigation(defaultLayers, 'layer1')

      const buttons = screen.getAllByRole('button')
      expect(buttons[0]).toHaveStyle({
        background: defaultColors.accent,
      })
    })

    it('should not apply active styles to inactive layers', () => {
      renderLayerNavigation(defaultLayers, 'layer1')

      const buttons = screen.getAllByRole('button')
      expect(buttons[1]).toHaveStyle({
        background: '#fafaf9',
      })
      expect(buttons[2]).toHaveStyle({
        background: '#fafaf9',
      })
      expect(buttons[3]).toHaveStyle({
        background: '#fafaf9',
      })
    })
  })

  describe('Different persona colors', () => {
    const personaTypes = ['partner', 'innovator', 'stakeholder', 'beneficiary'] as const

    personaTypes.forEach((type) => {
      it(`should apply ${type} colors correctly`, () => {
        const colors = PERSONA_TYPE_COLORS[type]
        renderLayerNavigation(defaultLayers, 'layer1', colors)

        const buttons = screen.getAllByRole('button')
        expect(buttons[0]).toHaveStyle({
          background: colors.accent,
        })
      })
    })
  })

  describe('Edge cases', () => {
    it('should handle empty layers array', () => {
      renderLayerNavigation([])

      expect(screen.getByText('Vianeo Four-Layer Structure')).toBeInTheDocument()
      expect(screen.queryAllByRole('button')).toHaveLength(0)
    })

    it('should handle single layer', () => {
      const singleLayer = [defaultLayers[0]]
      renderLayerNavigation(singleLayer)

      expect(screen.getByText('Layer 1')).toBeInTheDocument()
      expect(screen.queryByText('Layer 2')).not.toBeInTheDocument()
    })

    it('should handle null activeLayer', () => {
      renderLayerNavigation(defaultLayers, null)

      const buttons = screen.getAllByRole('button')
      buttons.forEach((button) => {
        expect(button).toHaveAttribute('aria-pressed', 'false')
      })
    })

    it('should handle activeLayer not in layers array', () => {
      renderLayerNavigation(defaultLayers, 'nonexistent-layer')

      const buttons = screen.getAllByRole('button')
      buttons.forEach((button) => {
        expect(button).toHaveAttribute('aria-pressed', 'false')
      })
    })
  })
})
