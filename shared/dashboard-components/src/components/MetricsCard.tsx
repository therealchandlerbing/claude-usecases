'use client';

import React, { ReactNode } from 'react';

export interface MetricsCardProps {
  title: string;
  value: string | number;
  subtitle?: string;
  icon?: ReactNode;
  trend?: {
    value: number;
    direction: 'up' | 'down' | 'neutral';
    label?: string;
  };
  variant?: 'default' | 'success' | 'warning' | 'error' | 'info';
  className?: string;
  onClick?: () => void;
}

const variantStyles = {
  default: {
    container: 'bg-white',
    title: 'text-gray-500',
    value: 'text-gray-900',
    icon: 'text-gray-400',
  },
  success: {
    container: 'bg-green-50',
    title: 'text-green-700',
    value: 'text-green-900',
    icon: 'text-green-500',
  },
  warning: {
    container: 'bg-yellow-50',
    title: 'text-yellow-700',
    value: 'text-yellow-900',
    icon: 'text-yellow-500',
  },
  error: {
    container: 'bg-red-50',
    title: 'text-red-700',
    value: 'text-red-900',
    icon: 'text-red-500',
  },
  info: {
    container: 'bg-blue-50',
    title: 'text-blue-700',
    value: 'text-blue-900',
    icon: 'text-blue-500',
  },
};

const trendColors = {
  up: 'text-green-600',
  down: 'text-red-600',
  neutral: 'text-gray-500',
};

const trendIcons = {
  up: (
    <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 10l7-7m0 0l7 7m-7-7v18" />
    </svg>
  ),
  down: (
    <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 14l-7 7m0 0l-7-7m7 7V3" />
    </svg>
  ),
  neutral: (
    <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 12h14" />
    </svg>
  ),
};

/**
 * MetricsCard component for displaying key metrics with optional trends.
 *
 * @example
 * // Basic usage
 * <MetricsCard title="Total Users" value={1234} />
 *
 * @example
 * // With trend
 * <MetricsCard
 *   title="Revenue"
 *   value="$45,231"
 *   trend={{ value: 12.5, direction: 'up', label: 'vs last month' }}
 * />
 *
 * @example
 * // With variant and icon
 * <MetricsCard
 *   title="Errors"
 *   value={3}
 *   variant="error"
 *   icon={<AlertIcon />}
 * />
 */
export function MetricsCard({
  title,
  value,
  subtitle,
  icon,
  trend,
  variant = 'default',
  className = '',
  onClick,
}: MetricsCardProps) {
  const styles = variantStyles[variant];
  const isClickable = !!onClick;

  return (
    <div
      className={`
        rounded-lg border border-gray-200 p-6 shadow-sm
        ${styles.container}
        ${isClickable ? 'cursor-pointer hover:shadow-md transition-shadow' : ''}
        ${className}
      `}
      onClick={onClick}
      role={isClickable ? 'button' : undefined}
      tabIndex={isClickable ? 0 : undefined}
    >
      <div className="flex items-start justify-between">
        <div className="flex-1">
          <p className={`text-sm font-medium ${styles.title}`}>{title}</p>
          <p className={`mt-2 text-3xl font-semibold ${styles.value}`}>
            {typeof value === 'number' ? value.toLocaleString() : value}
          </p>
          {subtitle && (
            <p className="mt-1 text-sm text-gray-500">{subtitle}</p>
          )}
          {trend && (
            <div className={`mt-2 flex items-center gap-1 ${trendColors[trend.direction]}`}>
              {trendIcons[trend.direction]}
              <span className="text-sm font-medium">
                {trend.value > 0 ? '+' : ''}{trend.value}%
              </span>
              {trend.label && (
                <span className="text-sm text-gray-500 ml-1">{trend.label}</span>
              )}
            </div>
          )}
        </div>
        {icon && (
          <div className={`p-2 rounded-lg bg-white/50 ${styles.icon}`}>
            {icon}
          </div>
        )}
      </div>
    </div>
  );
}

/**
 * Grid container for MetricsCards
 */
export function MetricsGrid({
  children,
  columns = 4,
  className = '',
}: {
  children: ReactNode;
  columns?: 2 | 3 | 4;
  className?: string;
}) {
  const gridCols = {
    2: 'grid-cols-1 md:grid-cols-2',
    3: 'grid-cols-1 md:grid-cols-2 lg:grid-cols-3',
    4: 'grid-cols-1 md:grid-cols-2 lg:grid-cols-4',
  };

  return (
    <div className={`grid gap-4 ${gridCols[columns]} ${className}`}>
      {children}
    </div>
  );
}

export default MetricsCard;
