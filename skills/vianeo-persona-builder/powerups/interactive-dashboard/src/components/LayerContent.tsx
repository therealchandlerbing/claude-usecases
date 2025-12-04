import React from 'react';
import {
  LayerContentProps,
  Layer1Content,
  Layer2Content,
  Layer3Content,
  Layer4Content,
  PersonaField,
  PersonaSection,
  isFieldBasedLayer,
  isLayer3Content,
  isLayer4Content,
  ValidationStatus
} from '../types';
import { EvidenceQuote } from './EvidenceQuote';
import { VALIDATION_STATUS_CONFIG } from '../constants';

// Helper to format validation badge label with icon
const getValidationLabel = (status: ValidationStatus): string => {
  const config = VALIDATION_STATUS_CONFIG[status];
  return `${config.icon} ${config.label}`;
};

/**
 * LayerContent Component
 *
 * Dynamically renders layer content based on layer type (1-4)
 */
export const LayerContent: React.FC<LayerContentProps> = ({ layerId, content, colors }) => {
  // Layer 1 & 2: Field-based content (structurally identical)
  if (isFieldBasedLayer(content)) {
    return (
      <div style={{ paddingTop: '20px', borderTop: '1px solid #e7e5e4' }}>
        <h3
          style={{
            fontSize: '24px',
            fontWeight: '300',
            color: colors.border,
            marginBottom: '20px',
            margin: '0 0 20px 0'
          }}
        >
          {content.title}
        </h3>

        {/* Fields */}
        {content.fields.map((field, idx) => (
          <FieldDisplay key={idx} field={field} colors={colors} />
        ))}

        {/* Quotes */}
        {content.quotes && content.quotes.length > 0 && (
          <QuotesSection quotes={content.quotes} colors={colors} />
        )}
      </div>
    );
  }

  // Layer 3: Section-based content
  if (isLayer3Content(content)) {
    return (
      <div style={{ paddingTop: '20px', borderTop: '1px solid #e7e5e4' }}>
        <h3
          style={{
            fontSize: '24px',
            fontWeight: '300',
            color: colors.border,
            marginBottom: '20px',
            margin: '0 0 20px 0'
          }}
        >
          {content.title}
        </h3>

        {/* Sections */}
        {content.sections.map((section, idx) => (
          <SectionDisplay key={idx} section={section} colors={colors} />
        ))}

        {/* Quotes */}
        {content.quotes && content.quotes.length > 0 && (
          <QuotesSection quotes={content.quotes} colors={colors} />
        )}
      </div>
    );
  }

  // Layer 4: Current solutions content
  if (isLayer4Content(content)) {
    return (
      <div style={{ paddingTop: '20px', borderTop: '1px solid #e7e5e4' }}>
        <h3
          style={{
            fontSize: '24px',
            fontWeight: '300',
            color: colors.border,
            marginBottom: '20px',
            margin: '0 0 20px 0'
          }}
        >
          {content.title}
        </h3>

        {/* Main Content */}
        <div
          style={{
            background: '#fafaf9',
            border: '1px solid #e7e5e4',
            padding: '20px',
            marginBottom: '20px',
            borderRadius: '6px'
          }}
        >
          <p
            style={{
              fontSize: '14px',
              lineHeight: '1.7',
              color: '#44403c',
              marginBottom: '12px',
              margin: '0 0 12px 0'
            }}
          >
            {content.content}
          </p>

          <div
            style={{
              fontSize: '11px',
              color: '#a8a29e',
              background: '#ffffff',
              padding: '4px 10px',
              borderRadius: '3px',
              display: 'inline-block'
            }}
          >
            <strong>Evidence:</strong> {content.source}
          </div>
        </div>

        {/* Gaps */}
        {content.gaps && content.gaps.length > 0 && (
          <div
            style={{
              background: '#fef3c7',
              border: '1px solid #fde68a',
              borderLeft: '4px solid #d97706',
              padding: '16px 20px',
              marginBottom: '20px',
              borderRadius: '4px'
            }}
            role="alert"
          >
            <div
              style={{
                fontSize: '12px',
                textTransform: 'uppercase',
                letterSpacing: '1px',
                color: '#b45309',
                marginBottom: '10px',
                fontWeight: '600'
              }}
            >
              ⚠ Current Solution Gaps
            </div>
            {content.gaps.map((gap, idx) => (
              <div
                key={idx}
                style={{
                  fontSize: '13px',
                  lineHeight: '1.6',
                  color: '#78350f',
                  marginBottom: '6px'
                }}
              >
                • {gap}
              </div>
            ))}
          </div>
        )}

        {/* Quotes */}
        {content.quotes && content.quotes.length > 0 && (
          <QuotesSection quotes={content.quotes} colors={colors} />
        )}
      </div>
    );
  }

  return null;
};

// Helper Components

const FieldDisplay: React.FC<{ field: PersonaField; colors: any }> = ({ field, colors }) => (
  <div
    style={{
      background: '#fafaf9',
      border: '1px solid #e7e5e4',
      padding: '18px 20px',
      marginBottom: '12px',
      borderRadius: '6px'
    }}
  >
    <div
      style={{
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        marginBottom: '8px',
        flexWrap: 'wrap',
        gap: '8px'
      }}
    >
      <div
        style={{
          fontSize: '13px',
          textTransform: 'uppercase',
          color: colors.stat,
          fontWeight: '600'
        }}
      >
        {field.label}
      </div>
      {field.validation && (
        <div
          style={{
            fontSize: '10px',
            padding: '3px 8px',
            background: VALIDATION_STATUS_CONFIG[field.validation].bgColor,
            color: VALIDATION_STATUS_CONFIG[field.validation].color,
            borderRadius: '3px',
            fontWeight: '500'
          }}
          role="status"
          aria-label={`Validation: ${VALIDATION_STATUS_CONFIG[field.validation].label}`}
        >
          {getValidationLabel(field.validation)}
        </div>
      )}
    </div>

    <p
      style={{
        fontSize: '14px',
        lineHeight: '1.7',
        color: '#44403c',
        marginBottom: '10px',
        margin: '0 0 10px 0'
      }}
    >
      {field.content}
    </p>

    <div
      style={{
        fontSize: '11px',
        color: '#a8a29e',
        background: '#ffffff',
        padding: '4px 10px',
        borderRadius: '3px',
        display: 'inline-block'
      }}
    >
      <strong>Evidence:</strong> {field.source}
    </div>
  </div>
);

const SectionDisplay: React.FC<{ section: PersonaSection; colors: any }> = ({ section, colors }) => (
  <div style={{ marginBottom: '28px' }}>
    <div
      style={{
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        marginBottom: '14px',
        flexWrap: 'wrap',
        gap: '8px'
      }}
    >
      <div
        style={{
          fontSize: '13px',
          textTransform: 'uppercase',
          letterSpacing: '1px',
          color: '#78716c',
          fontWeight: '600'
        }}
      >
        {section.label}
      </div>
      {section.validation && (
        <div
          style={{
            fontSize: '10px',
            padding: '4px 10px',
            background: VALIDATION_STATUS_CONFIG[section.validation].bgColor,
            color: VALIDATION_STATUS_CONFIG[section.validation].color,
            borderRadius: '3px',
            fontWeight: '600'
          }}
          role="status"
          aria-label={`Validation: ${VALIDATION_STATUS_CONFIG[section.validation].label}`}
        >
          {getValidationLabel(section.validation)}
        </div>
      )}
    </div>
    {section.items.map((item, itemIdx) => (
      <div
        key={itemIdx}
        style={{
          background: '#ffffff',
          padding: '12px 16px',
          marginBottom: '8px',
          fontSize: '14px',
          lineHeight: '1.6',
          color: '#292524',
          borderRadius: '4px',
          border: '1px solid #e7e5e4'
        }}
      >
        • {item}
      </div>
    ))}
  </div>
);

const QuotesSection: React.FC<{ quotes: any[]; colors: any }> = ({ quotes, colors }) => (
  <div style={{ marginTop: '24px' }}>
    <div
      style={{
        fontSize: '13px',
        textTransform: 'uppercase',
        letterSpacing: '1.5px',
        color: '#78716c',
        marginBottom: '14px',
        fontWeight: '600'
      }}
    >
      Supporting Evidence
    </div>

    {quotes.map((quote, idx) => (
      <EvidenceQuote key={idx} quote={quote} colors={colors} />
    ))}
  </div>
);
