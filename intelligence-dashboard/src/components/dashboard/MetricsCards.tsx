import { ArrowUp, ArrowDown, Minus } from 'lucide-react';

interface MetricsCardsProps {
  metrics: {
    total_extractions_7d: number;
    avg_completeness_7d: number;
    avg_user_rating_7d: number;
    flagged_rate_7d: number;
    trend_extractions: number;
    trend_completeness: number;
    trend_rating: number;
  };
}

export default function MetricsCards({ metrics }: MetricsCardsProps) {
  const cards = [
    {
      title: 'Extractions (7d)',
      value: metrics.total_extractions_7d,
      trend: metrics.trend_extractions,
      format: 'number',
    },
    {
      title: 'Avg Completeness',
      value: metrics.avg_completeness_7d,
      trend: metrics.trend_completeness,
      format: 'percent',
    },
    {
      title: 'Avg User Rating',
      value: metrics.avg_user_rating_7d || 0,
      trend: metrics.trend_rating || 0,
      format: 'rating',
    },
    {
      title: 'Flagged Rate',
      value: metrics.flagged_rate_7d,
      trend: -metrics.flagged_rate_7d,
      format: 'percent',
      inverse: true,
    },
  ];

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      {cards.map((card) => (
        <div
          key={card.title}
          className="bg-white rounded-lg shadow hover:shadow-lg transition-shadow p-6"
        >
          <div className="flex items-center justify-between">
            <p className="text-sm font-medium text-gray-600">{card.title}</p>
            <TrendBadge trend={card.trend} inverse={card.inverse} />
          </div>
          <p className="mt-2 text-3xl font-semibold text-gray-900">
            {formatValue(card.value, card.format)}
          </p>
        </div>
      ))}
    </div>
  );
}

function TrendBadge({ trend, inverse = false }: { trend: number; inverse?: boolean }) {
  if (trend === 0 || isNaN(trend)) {
    return (
      <span className="inline-flex items-center text-gray-500">
        <Minus className="h-4 w-4" />
      </span>
    );
  }

  const isPositive = inverse ? trend < 0 : trend > 0;
  const color = isPositive ? 'text-green-600' : 'text-red-600';
  const Icon = isPositive ? ArrowUp : ArrowDown;

  return (
    <span className={`inline-flex items-center ${color}`}>
      <Icon className="h-4 w-4" />
      <span className="ml-1 text-sm font-medium">{Math.abs(trend).toFixed(1)}%</span>
    </span>
  );
}

function formatValue(value: number, format: string): string {
  if (isNaN(value) || value === null) {
    return '—';
  }

  switch (format) {
    case 'percent':
      return `${Math.round(value)}%`;
    case 'rating':
      return `${value.toFixed(1)}/5`;
    case 'number':
    default:
      return value.toString();
  }
}
