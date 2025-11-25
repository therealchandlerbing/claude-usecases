import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import PatternDetection from '../src/components/partnership/PatternDetection';
import { Pattern } from '../src/components/partnership/data/partnerTypes';

describe('PatternDetection', () => {
  const defaultPatterns: Pattern[] = [
    { text: 'Successful JVs require 6-9 months relationship-building before structure discussions', frequency: '100%' },
    { text: 'Legal/operational complexity often underestimated (adds 3-4 months)', frequency: '85%' },
    { text: 'Best partnerships emerge from collaborative project work first', frequency: '90%' },
  ];

  it('renders the component header', () => {
    render(<PatternDetection patterns={defaultPatterns} />);

    expect(screen.getByText('Key Patterns')).toBeInTheDocument();
    expect(screen.getByText('Insights from historical partnerships')).toBeInTheDocument();
  });

  it('renders all patterns', () => {
    render(<PatternDetection patterns={defaultPatterns} />);

    expect(screen.getByText('Successful JVs require 6-9 months relationship-building before structure discussions')).toBeInTheDocument();
    expect(screen.getByText('Legal/operational complexity often underestimated (adds 3-4 months)')).toBeInTheDocument();
    expect(screen.getByText('Best partnerships emerge from collaborative project work first')).toBeInTheDocument();
  });

  it('displays frequency badges for each pattern', () => {
    render(<PatternDetection patterns={defaultPatterns} />);

    expect(screen.getByText('100%')).toBeInTheDocument();
    expect(screen.getByText('85%')).toBeInTheDocument();
    expect(screen.getByText('90%')).toBeInTheDocument();
  });

  it('renders empty list gracefully', () => {
    const { container } = render(<PatternDetection patterns={[]} />);

    // Header should still render
    expect(screen.getByText('Key Patterns')).toBeInTheDocument();

    // No pattern items should be present
    const patternItems = container.querySelectorAll('.space-y-3 > div');
    expect(patternItems.length).toBe(0);
  });

  it('renders single pattern correctly', () => {
    const singlePattern: Pattern[] = [
      { text: 'Single pattern text', frequency: '75%' },
    ];

    render(<PatternDetection patterns={singlePattern} />);

    expect(screen.getByText('Single pattern text')).toBeInTheDocument();
    expect(screen.getByText('75%')).toBeInTheDocument();
  });

  it('renders patterns with varying frequencies', () => {
    const variedPatterns: Pattern[] = [
      { text: 'Pattern one', frequency: '50%' },
      { text: 'Pattern two', frequency: '25%' },
      { text: 'Pattern three', frequency: '10%' },
    ];

    render(<PatternDetection patterns={variedPatterns} />);

    expect(screen.getByText('50%')).toBeInTheDocument();
    expect(screen.getByText('25%')).toBeInTheDocument();
    expect(screen.getByText('10%')).toBeInTheDocument();
  });

  it('applies hover styling on pattern items', () => {
    const { container } = render(<PatternDetection patterns={defaultPatterns} />);

    const hoverItems = container.querySelectorAll('.hover\\:border-blue-300');
    expect(hoverItems.length).toBe(3);
  });

  it('renders frequency badges with gradient styling', () => {
    const { container } = render(<PatternDetection patterns={defaultPatterns} />);

    const badges = container.querySelectorAll('.bg-gradient-to-r');
    // Each pattern should have a frequency badge with gradient
    expect(badges.length).toBeGreaterThanOrEqual(defaultPatterns.length);
  });

  it('renders with Brazil partner patterns', () => {
    const brazilPatterns: Pattern[] = [
      { text: 'Need 3-4 relationship-building meetings before contract discussions', frequency: '90%' },
      { text: 'Multiple stakeholder alignment required (technical + business + government)', frequency: '100%' },
      { text: 'Portuguese capability signals cultural competence and commitment', frequency: '85%' },
    ];

    render(<PatternDetection patterns={brazilPatterns} />);

    expect(screen.getByText('Need 3-4 relationship-building meetings before contract discussions')).toBeInTheDocument();
    expect(screen.getByText('Multiple stakeholder alignment required (technical + business + government)')).toBeInTheDocument();
  });

  it('renders container with shadow styling', () => {
    const { container } = render(<PatternDetection patterns={defaultPatterns} />);

    const shadowContainer = container.querySelector('.shadow-sm');
    expect(shadowContainer).toBeInTheDocument();
  });

  it('renders pattern items in correct order', () => {
    const { container } = render(<PatternDetection patterns={defaultPatterns} />);

    const patternTexts = container.querySelectorAll('.text-sm.text-gray-900');
    expect(patternTexts[0]).toHaveTextContent(defaultPatterns[0].text);
    expect(patternTexts[1]).toHaveTextContent(defaultPatterns[1].text);
    expect(patternTexts[2]).toHaveTextContent(defaultPatterns[2].text);
  });
});
