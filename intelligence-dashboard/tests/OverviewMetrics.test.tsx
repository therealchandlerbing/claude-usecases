import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import OverviewMetrics from '../src/components/partnership/OverviewMetrics';
import { PartnerMetrics } from '../src/components/partnership/data/partnerTypes';

describe('OverviewMetrics', () => {
  const defaultMetrics: PartnerMetrics = {
    explored: 15,
    closed: 9,
    successRate: 60,
    avgTimeline: 6.8,
    approach: 'Relationship-first, hierarchy-aware',
    decisionStyle: 'Consensus-building with oversight',
  };

  it('renders all six metric cards', () => {
    render(<OverviewMetrics metrics={defaultMetrics} />);

    expect(screen.getByText('Explored')).toBeInTheDocument();
    expect(screen.getByText('Closed')).toBeInTheDocument();
    expect(screen.getByText('Success Rate')).toBeInTheDocument();
    expect(screen.getByText('Avg Timeline')).toBeInTheDocument();
    expect(screen.getByText('Approach & Style')).toBeInTheDocument();
  });

  it('displays explored count', () => {
    render(<OverviewMetrics metrics={defaultMetrics} />);

    expect(screen.getByText('15')).toBeInTheDocument();
  });

  it('displays closed count', () => {
    render(<OverviewMetrics metrics={defaultMetrics} />);

    expect(screen.getByText('9')).toBeInTheDocument();
  });

  it('displays success rate as percentage', () => {
    render(<OverviewMetrics metrics={defaultMetrics} />);

    expect(screen.getByText('60%')).toBeInTheDocument();
  });

  it('displays average timeline with months suffix', () => {
    render(<OverviewMetrics metrics={defaultMetrics} />);

    expect(screen.getByText('6.8mo')).toBeInTheDocument();
  });

  it('displays approach text', () => {
    render(<OverviewMetrics metrics={defaultMetrics} />);

    expect(screen.getByText('Relationship-first, hierarchy-aware')).toBeInTheDocument();
  });

  it('displays decision style text', () => {
    render(<OverviewMetrics metrics={defaultMetrics} />);

    expect(screen.getByText('Consensus-building with oversight')).toBeInTheDocument();
  });

  it('displays helper text for explored metric', () => {
    render(<OverviewMetrics metrics={defaultMetrics} />);

    expect(screen.getByText('Last 18-24 months')).toBeInTheDocument();
  });

  it('displays helper text for timeline metric', () => {
    render(<OverviewMetrics metrics={defaultMetrics} />);

    expect(screen.getByText('First contact to launch')).toBeInTheDocument();
  });

  it('applies green styling for high success rate', () => {
    const highSuccessMetrics = {
      ...defaultMetrics,
      successRate: 60,
    };

    const { container } = render(<OverviewMetrics metrics={highSuccessMetrics} />);

    const greenIndicator = container.querySelector('.bg-green-500');
    expect(greenIndicator).toBeInTheDocument();
  });

  it('applies yellow styling for medium success rate', () => {
    const mediumSuccessMetrics = {
      ...defaultMetrics,
      successRate: 35,
    };

    const { container } = render(<OverviewMetrics metrics={mediumSuccessMetrics} />);

    const yellowIndicator = container.querySelector('.bg-yellow-500');
    expect(yellowIndicator).toBeInTheDocument();
  });

  it('applies orange styling for low success rate', () => {
    const lowSuccessMetrics = {
      ...defaultMetrics,
      successRate: 20,
    };

    const { container } = render(<OverviewMetrics metrics={lowSuccessMetrics} />);

    const orangeIndicator = container.querySelector('.bg-orange-500');
    expect(orangeIndicator).toBeInTheDocument();
  });

  it('renders in a responsive grid layout', () => {
    const { container } = render(<OverviewMetrics metrics={defaultMetrics} />);

    const grid = container.querySelector('.grid');
    expect(grid).toHaveClass('grid-cols-2');
    expect(grid).toHaveClass('lg:grid-cols-6');
  });

  it('applies hover effects on cards', () => {
    const { container } = render(<OverviewMetrics metrics={defaultMetrics} />);

    const cards = container.querySelectorAll('.hover\\:shadow-md');
    expect(cards.length).toBeGreaterThan(0);
  });

  it('renders with different partner type metrics', () => {
    const jvMetrics: PartnerMetrics = {
      explored: 8,
      closed: 2,
      successRate: 25,
      avgTimeline: 11.5,
      approach: 'Co-creation, shared equity/revenue',
      decisionStyle: 'Strategic fit over speed',
    };

    render(<OverviewMetrics metrics={jvMetrics} />);

    expect(screen.getByText('8')).toBeInTheDocument();
    expect(screen.getByText('2')).toBeInTheDocument();
    expect(screen.getByText('25%')).toBeInTheDocument();
    expect(screen.getByText('11.5mo')).toBeInTheDocument();
    expect(screen.getByText('Co-creation, shared equity/revenue')).toBeInTheDocument();
  });
});
