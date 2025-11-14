import React from 'react';
import { EvidenceQuoteProps } from '../types';

/**
 * EvidenceQuote Component
 *
 * Displays a quote with attribution and source information
 */
export const EvidenceQuote: React.FC<EvidenceQuoteProps> = ({ quote, colors }) => {
  return (
    <div
      style={{
        background: '#ffffff',
        border: '1px solid #e7e5e4',
        padding: '18px 20px',
        marginBottom: '10px',
        borderRadius: '6px'
      }}
      role="figure"
      aria-label="Evidence quote"
    >
      <blockquote
        style={{
          fontSize: '14px',
          lineHeight: '1.7',
          color: '#44403c',
          marginBottom: '12px',
          fontStyle: 'italic',
          margin: 0
        }}
      >
        "{quote.text}"
      </blockquote>

      <div
        style={{
          display: 'flex',
          justifyContent: 'space-between',
          fontSize: '12px',
          marginTop: '12px'
        }}
      >
        <cite
          style={{
            color: colors.stat,
            fontWeight: '500',
            fontStyle: 'normal'
          }}
        >
          {quote.author}
        </cite>
        <span style={{ color: '#a8a29e' }}>{quote.source}</span>
      </div>
    </div>
  );
};
