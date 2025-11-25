import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import PartnerTypeSelector from '../src/components/partnership/PartnerTypeSelector';
import { partnerTypes } from '../src/components/partnership/data/partnerTypes';

describe('PartnerTypeSelector', () => {
  const mockSetSelectedPartner = vi.fn();

  const defaultProps = {
    selectedPartner: 'jv' as const,
    setSelectedPartner: mockSetSelectedPartner,
    partnerTypes,
  };

  beforeEach(() => {
    mockSetSelectedPartner.mockClear();
  });

  it('renders all four partner type buttons', () => {
    render(<PartnerTypeSelector {...defaultProps} />);

    expect(screen.getByText('Joint Venture Partners')).toBeInTheDocument();
    expect(screen.getByText('Brazilian Tech Transfer Institutions')).toBeInTheDocument();
    expect(screen.getByText('US Corporate & VC Partners')).toBeInTheDocument();
    expect(screen.getByText('Foundation & Impact Investors')).toBeInTheDocument();
  });

  it('displays subtitles for each partner type', () => {
    render(<PartnerTypeSelector {...defaultProps} />);

    expect(screen.getByText('True partnership structures (like SpacePlan, GenIP)')).toBeInTheDocument();
    expect(screen.getByText('CNEN, NanoBioPlus, university tech transfer')).toBeInTheDocument();
    expect(screen.getByText('Corporate innovation groups, impact VCs, strategic partners')).toBeInTheDocument();
    expect(screen.getByText('Philanthropic foundations, impact funds, development finance')).toBeInTheDocument();
  });

  it('shows "Active" badge on selected partner', () => {
    render(<PartnerTypeSelector {...defaultProps} />);

    expect(screen.getByText('Active')).toBeInTheDocument();
  });

  it('calls setSelectedPartner when a button is clicked', () => {
    render(<PartnerTypeSelector {...defaultProps} />);

    const brazilButton = screen.getByText('Brazilian Tech Transfer Institutions').closest('button');
    fireEvent.click(brazilButton!);

    expect(mockSetSelectedPartner).toHaveBeenCalledWith('brazil');
  });

  it('calls setSelectedPartner with correct key for each partner type', () => {
    render(<PartnerTypeSelector {...defaultProps} />);

    // Click US Corporate
    const usCorpButton = screen.getByText('US Corporate & VC Partners').closest('button');
    fireEvent.click(usCorpButton!);
    expect(mockSetSelectedPartner).toHaveBeenCalledWith('uscorp');

    // Click Foundation
    const foundationButton = screen.getByText('Foundation & Impact Investors').closest('button');
    fireEvent.click(foundationButton!);
    expect(mockSetSelectedPartner).toHaveBeenCalledWith('foundation');
  });

  it('displays success rate for each partner type', () => {
    render(<PartnerTypeSelector {...defaultProps} />);

    // JV has 25% success rate
    expect(screen.getByText('25%')).toBeInTheDocument();
    // Brazil has 60% success rate
    expect(screen.getByText('60%')).toBeInTheDocument();
    // US Corp has 27% success rate
    expect(screen.getByText('27%')).toBeInTheDocument();
    // Foundation has 28% success rate
    expect(screen.getByText('28%')).toBeInTheDocument();
  });

  it('displays average timeline for each partner type', () => {
    render(<PartnerTypeSelector {...defaultProps} />);

    expect(screen.getByText('11.5mo avg')).toBeInTheDocument();
    expect(screen.getByText('6.8mo avg')).toBeInTheDocument();
    expect(screen.getByText('4.2mo avg')).toBeInTheDocument();
    expect(screen.getByText('8.5mo avg')).toBeInTheDocument();
  });

  it('applies selected styling to active partner', () => {
    render(<PartnerTypeSelector {...defaultProps} />);

    const jvButton = screen.getByText('Joint Venture Partners').closest('button');
    expect(jvButton).toHaveClass('border-blue-500');
  });

  it('changes selected partner on click', () => {
    const { rerender } = render(<PartnerTypeSelector {...defaultProps} />);

    // Click Brazil
    const brazilButton = screen.getByText('Brazilian Tech Transfer Institutions').closest('button');
    fireEvent.click(brazilButton!);

    // Simulate parent updating selectedPartner state
    rerender(
      <PartnerTypeSelector
        {...defaultProps}
        selectedPartner="brazil"
      />
    );

    // Brazil should now be selected
    expect(brazilButton).toHaveClass('border-blue-500');
  });

  it('renders in a responsive grid layout', () => {
    const { container } = render(<PartnerTypeSelector {...defaultProps} />);

    const grid = container.querySelector('.grid');
    expect(grid).toHaveClass('grid-cols-1');
    expect(grid).toHaveClass('sm:grid-cols-2');
    expect(grid).toHaveClass('lg:grid-cols-4');
  });

  it('renders color indicators based on success rate', () => {
    const { container } = render(<PartnerTypeSelector {...defaultProps} />);

    // Brazil with 60% should have green indicator
    const greenIndicators = container.querySelectorAll('.bg-green-500');
    expect(greenIndicators.length).toBeGreaterThan(0);

    // Lower success rates should have orange indicator
    const orangeIndicators = container.querySelectorAll('.bg-orange-500');
    expect(orangeIndicators.length).toBeGreaterThan(0);
  });
});
