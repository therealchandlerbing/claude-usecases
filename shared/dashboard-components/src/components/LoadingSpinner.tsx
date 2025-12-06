'use client';

import React from 'react';

export interface LoadingSpinnerProps {
  size?: 'sm' | 'md' | 'lg' | 'xl';
  color?: 'primary' | 'secondary' | 'white';
  label?: string;
  className?: string;
}

const sizeClasses = {
  sm: 'h-4 w-4',
  md: 'h-8 w-8',
  lg: 'h-12 w-12',
  xl: 'h-16 w-16',
};

const colorClasses = {
  primary: 'text-blue-600',
  secondary: 'text-gray-600',
  white: 'text-white',
};

/**
 * LoadingSpinner component for indicating loading states.
 *
 * @example
 * // Basic usage
 * <LoadingSpinner />
 *
 * @example
 * // With size and label
 * <LoadingSpinner size="lg" label="Loading data..." />
 *
 * @example
 * // Custom color
 * <LoadingSpinner color="white" />
 */
export function LoadingSpinner({
  size = 'md',
  color = 'primary',
  label,
  className = '',
}: LoadingSpinnerProps) {
  return (
    <div className={`flex flex-col items-center justify-center ${className}`}>
      <svg
        className={`animate-spin ${sizeClasses[size]} ${colorClasses[color]}`}
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        aria-hidden="true"
      >
        <circle
          className="opacity-25"
          cx="12"
          cy="12"
          r="10"
          stroke="currentColor"
          strokeWidth="4"
        />
        <path
          className="opacity-75"
          fill="currentColor"
          d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
        />
      </svg>
      {label && (
        <span className={`mt-2 text-sm ${colorClasses[color]}`}>{label}</span>
      )}
    </div>
  );
}

/**
 * Full-page loading overlay
 */
export function LoadingOverlay({ label }: { label?: string }) {
  return (
    <div className="fixed inset-0 bg-white/80 backdrop-blur-sm flex items-center justify-center z-50">
      <LoadingSpinner size="xl" label={label || 'Loading...'} />
    </div>
  );
}

/**
 * Inline loading indicator for smaller sections
 */
export function LoadingInline({ label }: { label?: string }) {
  return (
    <div className="flex items-center gap-2 text-gray-600">
      <LoadingSpinner size="sm" color="secondary" />
      {label && <span className="text-sm">{label}</span>}
    </div>
  );
}

export default LoadingSpinner;
