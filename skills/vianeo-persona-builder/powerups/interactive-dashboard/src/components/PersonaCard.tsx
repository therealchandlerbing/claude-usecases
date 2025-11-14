import React from 'react';
import { PersonaCardProps, ValidationStatus } from '../types';
import { ValidationBadge } from './ValidationBadge';

// Validation status configuration
const validationStatusConfig: Record<ValidationStatus, { label: string; color: string; bgColor: string; icon: string }> = {
  validated: { label: 'Validated', color: '#059669', bgColor: '#d1fae5', icon: '✓' },
  inferred: { label: 'Not Yet Validated', color: '#dc2626', bgColor: '#fee2e2', icon: '⚠' },
  hybrid: { label: 'Partially Validated', color: '#d97706', bgColor: '#fef3c7', icon: '◐' }
};

/**
 * PersonaCard Component
 *
 * Displays a persona card with type, validation status, and key metrics
 */
export const PersonaCard: React.FC<PersonaCardProps> = ({
  id,
  persona,
  isActive,
  onClick,
  colors
}) => {
  const validation = validationStatusConfig[persona.validationStatus];

  return (
    <div
      onClick={onClick}
      onKeyPress={(e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          onClick();
        }
      }}
      tabIndex={0}
      role="button"
      aria-pressed={isActive}
      aria-label={`Select ${persona.title} persona`}
      style={{
        background: isActive ? colors.accent : '#ffffff',
        border: `2px solid ${isActive ? colors.border : '#e7e5e4'}`,
        borderRadius: '8px',
        padding: '24px',
        cursor: 'pointer',
        transition: 'all 0.3s ease',
        transform: isActive ? 'translateY(-2px)' : 'translateY(0)',
        boxShadow: isActive ? `0 8px 24px ${colors.border}25` : '0 1px 3px rgba(0,0,0,0.08)',
        outline: 'none'
      }}
    >
      {/* Badges */}
      <div style={{ display: 'flex', gap: '8px', marginBottom: '12px', flexWrap: 'wrap' }}>
        <div
          style={{
            fontSize: '10px',
            padding: '4px 8px',
            background: colors.subtle,
            color: colors.stat,
            borderRadius: '3px',
            fontWeight: '600',
            textTransform: 'uppercase'
          }}
          aria-label={`Persona type: ${persona.type}`}
        >
          {persona.type}
        </div>

        <ValidationBadge status={persona.validationStatus} config={validation} />
      </div>

      {/* Title */}
      <h3
        style={{
          fontSize: '20px',
          fontWeight: '500',
          color: colors.border,
          marginBottom: '6px',
          lineHeight: '1.3',
          margin: '0 0 6px 0'
        }}
      >
        {persona.title}
      </h3>

      {/* Subtitle */}
      <p
        style={{
          fontSize: '14px',
          color: '#78716c',
          marginBottom: '20px',
          lineHeight: '1.5',
          margin: '0 0 20px 0'
        }}
      >
        {persona.subtitle}
      </p>

      {/* Stats */}
      <div
        style={{
          display: 'flex',
          gap: '16px',
          paddingTop: '16px',
          borderTop: `1px solid ${colors.border}40`
        }}
      >
        <div style={{ flex: 1 }}>
          <div
            style={{
              fontSize: '11px',
              textTransform: 'uppercase',
              color: '#a8a29e',
              marginBottom: '4px'
            }}
          >
            Interviews
          </div>
          <div
            style={{
              fontSize: '24px',
              fontWeight: '300',
              color: colors.stat
            }}
            aria-label={`${persona.interviewCount} interviews conducted`}
          >
            {persona.interviewCount}
          </div>
        </div>
        <div style={{ flex: 1 }}>
          <div
            style={{
              fontSize: '11px',
              textTransform: 'uppercase',
              color: '#a8a29e',
              marginBottom: '4px'
            }}
          >
            Quality Score
          </div>
          <div
            style={{
              fontSize: '24px',
              fontWeight: '300',
              color: colors.stat
            }}
            aria-label={`Quality score: ${persona.qualityScore} out of 5`}
          >
            {persona.qualityScore}/5
          </div>
        </div>
      </div>
    </div>
  );
};
