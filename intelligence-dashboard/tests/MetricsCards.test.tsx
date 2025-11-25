import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import MetricsCards from '../src/components/dashboard/MetricsCards';

describe('MetricsCards', () => {
  const defaultMetrics = {
    total_extractions_7d: 42,
    avg_completeness_7d: 87,
    avg_user_rating_7d: 4.2,
    flagged_rate_7d: 5,
    trend_extractions: 12.5,
    trend_completeness: 3.2,
    trend_rating: 0.8,
  };

  it('renders all four metric cards', () => {
    render(<MetricsCards metrics={defaultMetrics} />);

    expect(screen.getByText('Extractions (7d)')).toBeInTheDocument();
    expect(screen.getByText('Avg Completeness')).toBeInTheDocument();
    expect(screen.getByText('Avg User Rating')).toBeInTheDocument();
    expect(screen.getByText('Flagged Rate')).toBeInTheDocument();
  });

  it('displays extraction count correctly', () => {
    render(<MetricsCards metrics={defaultMetrics} />);

    expect(screen.getByText('42')).toBeInTheDocument();
  });

  it('displays completeness as percentage', () => {
    render(<MetricsCards metrics={defaultMetrics} />);

    expect(screen.getByText('87%')).toBeInTheDocument();
  });

  it('displays user rating with decimal and /5', () => {
    render(<MetricsCards metrics={defaultMetrics} />);

    expect(screen.getByText('4.2/5')).toBeInTheDocument();
  });

  it('displays flagged rate as percentage', () => {
    render(<MetricsCards metrics={defaultMetrics} />);

    expect(screen.getByText('5%')).toBeInTheDocument();
  });

  it('displays positive trend with percentage', () => {
    render(<MetricsCards metrics={defaultMetrics} />);

    // Should show the positive trend value
    expect(screen.getByText('12.5%')).toBeInTheDocument();
  });

  it('handles zero rating gracefully', () => {
    const metricsWithZeroRating = {
      ...defaultMetrics,
      avg_user_rating_7d: 0,
      trend_rating: 0,
    };

    render(<MetricsCards metrics={metricsWithZeroRating} />);

    expect(screen.getByText('0.0/5')).toBeInTheDocument();
  });

  it('handles null/undefined rating by defaulting to zero', () => {
    // Note: The component uses `|| 0` fallback which converts null/undefined to 0
    const metricsWithNullRating = {
      ...defaultMetrics,
      avg_user_rating_7d: null as unknown as number,
      trend_rating: null as unknown as number,
    };

    render(<MetricsCards metrics={metricsWithNullRating} />);

    // Component defaults null to 0, displaying 0.0/5
    expect(screen.getByText('0.0/5')).toBeInTheDocument();
  });

  it('handles NaN values with dash', () => {
    const metricsWithNaN = {
      ...defaultMetrics,
      avg_completeness_7d: NaN,
    };

    render(<MetricsCards metrics={metricsWithNaN} />);

    expect(screen.getByText('—')).toBeInTheDocument();
  });

  it('renders trend indicators for non-zero trends', () => {
    render(<MetricsCards metrics={defaultMetrics} />);

    // Check that trend percentages are displayed
    expect(screen.getByText('12.5%')).toBeInTheDocument();
    expect(screen.getByText('3.2%')).toBeInTheDocument();
    expect(screen.getByText('0.8%')).toBeInTheDocument();
  });

  it('handles zero trends without crash', () => {
    const metricsWithZeroTrends = {
      ...defaultMetrics,
      trend_extractions: 0,
      trend_completeness: 0,
      trend_rating: 0,
    };

    render(<MetricsCards metrics={metricsWithZeroTrends} />);

    // Component should still render
    expect(screen.getByText('Extractions (7d)')).toBeInTheDocument();
  });

  it('applies correct grid layout classes', () => {
    const { container } = render(<MetricsCards metrics={defaultMetrics} />);

    const grid = container.querySelector('.grid');
    expect(grid).toHaveClass('grid-cols-1');
    expect(grid).toHaveClass('md:grid-cols-2');
    expect(grid).toHaveClass('lg:grid-cols-4');
  });

  it('renders cards with shadow styling', () => {
    const { container } = render(<MetricsCards metrics={defaultMetrics} />);

    const cards = container.querySelectorAll('.shadow');
    expect(cards.length).toBe(4);
  });
});
