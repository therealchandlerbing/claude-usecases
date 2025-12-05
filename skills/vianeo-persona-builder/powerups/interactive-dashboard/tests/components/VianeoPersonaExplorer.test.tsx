/**
 * Unit tests for VianeoPersonaExplorer main component
 */

import { describe, it, expect } from 'vitest'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { VianeoPersonaExplorer } from '../../src/VianeoPersonaExplorer'
import type { DashboardData, Layer1Content, Layer3Content } from '../../src/types'

describe('VianeoPersonaExplorer', () => {
  const createMockData = (): DashboardData => ({
    personas: {
      'partner-maria': {
        type: 'partner',
        title: 'Maria Santos',
        subtitle: 'Deputy Director of Technology Transfer',
        validationStatus: 'validated',
        interviewCount: 8,
        qualityScore: 4,
        evidenceSummary: 'Based on 8 interviews with university TTO staff',
        layers: [
          { id: 'partner-maria-layer1', number: '1', title: 'Requester', subtitle: 'Who They Are' },
          { id: 'partner-maria-layer2', number: '2', title: 'Field of Application', subtitle: 'Their World' },
          { id: 'partner-maria-layer3', number: '3', title: 'Activities & Challenges', subtitle: 'What They Do' },
          { id: 'partner-maria-layer4', number: '4', title: 'Current Solutions', subtitle: 'What They Use' },
        ],
      },
      'innovator-john': {
        type: 'innovator',
        title: 'Dr. John Chen',
        subtitle: 'Research Scientist',
        validationStatus: 'inferred',
        interviewCount: 3,
        qualityScore: 3,
        evidenceSummary: 'Based on 3 preliminary interviews',
        layers: [
          { id: 'innovator-john-layer1', number: '1', title: 'Requester', subtitle: 'Who They Are' },
          { id: 'innovator-john-layer2', number: '2', title: 'Field of Application', subtitle: 'Their World' },
          { id: 'innovator-john-layer3', number: '3', title: 'Activities & Challenges', subtitle: 'What They Do' },
          { id: 'innovator-john-layer4', number: '4', title: 'Current Solutions', subtitle: 'What They Use' },
        ],
      },
    },
    layerContent: {
      'partner-maria-layer1': {
        title: 'Layer 1: Requester',
        fields: [
          {
            label: 'First Name',
            content: 'Maria',
            source: 'Interview #3',
            validation: 'validated',
          },
        ],
      } as Layer1Content,
      'partner-maria-layer3': {
        title: 'Layer 3: Activities',
        sections: [
          {
            label: 'Tasks',
            items: ['Review proposals', 'Coordinate with legal'],
            validation: 'validated',
          },
        ],
      } as Layer3Content,
    },
    metadata: {
      projectName: 'Test Project',
      createdDate: '2024-11-20',
      version: '1.0',
    },
  })

  describe('Header rendering', () => {
    it('should render main header', () => {
      render(<VianeoPersonaExplorer data={createMockData()} />)

      expect(screen.getByText('Stakeholder Persona Explorer')).toBeInTheDocument()
    })

    it('should render framework subtitle', () => {
      render(<VianeoPersonaExplorer data={createMockData()} />)

      expect(
        screen.getByText('Vianeo Business Validation Framework')
      ).toBeInTheDocument()
    })

    it('should render description', () => {
      render(<VianeoPersonaExplorer data={createMockData()} />)

      expect(
        screen.getByText(/Navigate through validated stakeholder personas/)
      ).toBeInTheDocument()
    })

    it('should render project metadata', () => {
      render(<VianeoPersonaExplorer data={createMockData()} />)

      expect(screen.getByText(/Test Project/)).toBeInTheDocument()
      expect(screen.getByText(/2024-11-20/)).toBeInTheDocument()
    })

    it('should not render metadata when not provided', () => {
      const dataNoMeta = createMockData()
      delete dataNoMeta.metadata

      render(<VianeoPersonaExplorer data={dataNoMeta} />)

      expect(screen.queryByText('Project:')).not.toBeInTheDocument()
    })
  })

  describe('Persona cards rendering', () => {
    it('should render all persona cards', () => {
      render(<VianeoPersonaExplorer data={createMockData()} />)

      expect(screen.getByText('Maria Santos')).toBeInTheDocument()
      expect(screen.getByText('Dr. John Chen')).toBeInTheDocument()
    })

    it('should render persona subtitles', () => {
      render(<VianeoPersonaExplorer data={createMockData()} />)

      expect(
        screen.getByText('Deputy Director of Technology Transfer')
      ).toBeInTheDocument()
      expect(screen.getByText('Research Scientist')).toBeInTheDocument()
    })

    it('should render persona type badges', () => {
      render(<VianeoPersonaExplorer data={createMockData()} />)

      expect(screen.getByText('partner')).toBeInTheDocument()
      expect(screen.getByText('innovator')).toBeInTheDocument()
    })
  })

  describe('Empty state', () => {
    it('should render empty state message when no persona is selected', () => {
      render(<VianeoPersonaExplorer data={createMockData()} />)

      expect(
        screen.getByText('Select a persona above to explore their four-layer structure')
      ).toBeInTheDocument()
    })

    it('should render hint text in empty state', () => {
      render(<VianeoPersonaExplorer data={createMockData()} />)

      expect(
        screen.getByText('Click on any persona card to view detailed information and evidence')
      ).toBeInTheDocument()
    })
  })

  describe('Persona selection', () => {
    it('should show persona detail when persona is clicked', async () => {
      render(<VianeoPersonaExplorer data={createMockData()} />)

      // Click on Maria's card
      const mariaCard = screen.getByLabelText('Select Maria Santos persona')
      await userEvent.click(mariaCard)

      // Evidence summary should be visible in detail view
      expect(
        screen.getByText('Based on 8 interviews with university TTO staff')
      ).toBeInTheDocument()
    })

    it('should hide empty state when persona is selected', async () => {
      render(<VianeoPersonaExplorer data={createMockData()} />)

      const mariaCard = screen.getByLabelText('Select Maria Santos persona')
      await userEvent.click(mariaCard)

      expect(
        screen.queryByText('Select a persona above to explore their four-layer structure')
      ).not.toBeInTheDocument()
    })

    it('should show layer navigation when persona is selected', async () => {
      render(<VianeoPersonaExplorer data={createMockData()} />)

      const mariaCard = screen.getByLabelText('Select Maria Santos persona')
      await userEvent.click(mariaCard)

      expect(screen.getByText('Vianeo Four-Layer Structure')).toBeInTheDocument()
      expect(screen.getAllByText('Layer 1').length).toBeGreaterThanOrEqual(1)
    })

    it('should switch between personas', async () => {
      render(<VianeoPersonaExplorer data={createMockData()} />)

      // Select Maria first
      const mariaCard = screen.getByLabelText('Select Maria Santos persona')
      await userEvent.click(mariaCard)

      expect(
        screen.getByText('Based on 8 interviews with university TTO staff')
      ).toBeInTheDocument()

      // Now select John
      const johnCard = screen.getByLabelText('Select Dr. John Chen persona')
      await userEvent.click(johnCard)

      expect(
        screen.getByText('Based on 3 preliminary interviews')
      ).toBeInTheDocument()
    })
  })

  describe('Layer navigation', () => {
    it('should show layer content when layer is clicked', async () => {
      const mockData = createMockData()
      render(<VianeoPersonaExplorer data={mockData} />)

      // Select persona
      const mariaCard = screen.getByLabelText('Select Maria Santos persona')
      await userEvent.click(mariaCard)

      // Click on layer 1
      const layer1Button = screen.getByLabelText('View Requester')
      await userEvent.click(layer1Button)

      // Layer content should be visible
      expect(screen.getByText('Layer 1: Requester')).toBeInTheDocument()
    })

    it('should reset layer when switching personas', async () => {
      const mockData = createMockData()
      render(<VianeoPersonaExplorer data={mockData} />)

      // Select Maria and view a layer
      const mariaCard = screen.getByLabelText('Select Maria Santos persona')
      await userEvent.click(mariaCard)

      const layer1Button = screen.getByLabelText('View Requester')
      await userEvent.click(layer1Button)

      expect(screen.getByText('Layer 1: Requester')).toBeInTheDocument()

      // Switch to John - layer should reset
      const johnCard = screen.getByLabelText('Select Dr. John Chen persona')
      await userEvent.click(johnCard)

      // Layer content should not be visible anymore
      // (John's layer hasn't been clicked yet)
      expect(screen.queryByText('Layer 1: Requester')).not.toBeInTheDocument()
    })
  })

  describe('Footer', () => {
    it('should render footer with version info', () => {
      render(<VianeoPersonaExplorer data={createMockData()} />)

      expect(
        screen.getByText(/Generated with Vianeo Persona Builder/)
      ).toBeInTheDocument()
      expect(screen.getByText(/Interactive Dashboard v1.0/)).toBeInTheDocument()
    })
  })

  describe('Edge cases', () => {
    it('should handle empty personas object', () => {
      const emptyData: DashboardData = {
        personas: {},
        layerContent: {},
      }

      render(<VianeoPersonaExplorer data={emptyData} />)

      expect(screen.getByText('Stakeholder Persona Explorer')).toBeInTheDocument()
      expect(
        screen.getByText('Select a persona above to explore their four-layer structure')
      ).toBeInTheDocument()
    })

    it('should handle single persona', () => {
      const singlePersona: DashboardData = {
        personas: {
          'only-one': {
            type: 'stakeholder',
            title: 'Single Persona',
            subtitle: 'Only persona',
            validationStatus: 'validated',
            interviewCount: 1,
            qualityScore: 5,
            evidenceSummary: 'Single interview',
            layers: [],
          },
        },
        layerContent: {},
      }

      render(<VianeoPersonaExplorer data={singlePersona} />)

      expect(screen.getByText('Single Persona')).toBeInTheDocument()
    })

    it('should handle missing layer content gracefully', async () => {
      const mockData = createMockData()
      // Remove layer content
      mockData.layerContent = {}

      render(<VianeoPersonaExplorer data={mockData} />)

      // Select persona
      const mariaCard = screen.getByLabelText('Select Maria Santos persona')
      await userEvent.click(mariaCard)

      // Click layer (even though content doesn't exist)
      const layer1Button = screen.getByLabelText('View Requester')
      await userEvent.click(layer1Button)

      // Should not crash, navigation should still work
      expect(screen.getByLabelText('View Requester')).toBeInTheDocument()
    })

    it('should handle partial metadata', () => {
      const partialMeta: DashboardData = {
        ...createMockData(),
        metadata: {
          projectName: 'Project Only',
        },
      }

      render(<VianeoPersonaExplorer data={partialMeta} />)

      expect(screen.getByText(/Project Only/)).toBeInTheDocument()
      // Created date should not appear
      expect(screen.queryByText('Created:')).not.toBeInTheDocument()
    })
  })

  describe('Responsive layout', () => {
    it('should use grid layout for persona cards', () => {
      render(<VianeoPersonaExplorer data={createMockData()} />)

      // Find the grid container (parent of persona cards)
      const mariaCard = screen.getByText('Maria Santos').closest('[role="button"]')
      const gridContainer = mariaCard?.parentElement

      expect(gridContainer).toHaveStyle({ display: 'grid' })
    })
  })

  describe('Accessibility', () => {
    it('should have semantic header element', () => {
      render(<VianeoPersonaExplorer data={createMockData()} />)

      expect(screen.getByRole('banner')).toBeInTheDocument()
    })

    it('should have h1 heading', () => {
      render(<VianeoPersonaExplorer data={createMockData()} />)

      expect(
        screen.getByRole('heading', { level: 1, name: 'Stakeholder Persona Explorer' })
      ).toBeInTheDocument()
    })

    it('should have semantic footer element', () => {
      render(<VianeoPersonaExplorer data={createMockData()} />)

      expect(screen.getByRole('contentinfo')).toBeInTheDocument()
    })
  })
})
