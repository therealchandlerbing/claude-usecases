import React from 'react';
import { ValidationBadgeProps } from '../types';

/**
 * ValidationBadge Component
 *
 * Displays validation status with icon and label
 */
export const ValidationBadge: React.FC<ValidationBadgeProps> = ({ status, config }) => {
  return (
    <div
      style={{
        fontSize: '10px',
        padding: '4px 8px',
        background: config.bgColor,
        color: config.color,
        borderRadius: '3px',
        fontWeight: '600',
        display: 'flex',
        alignItems: 'center',
        gap: '4px'
      }}
      role="status"
      aria-label={`Validation status: ${config.label}`}
    >
      <span aria-hidden="true">{config.icon}</span>
      <span>{config.label}</span>
    </div>
  );
};
