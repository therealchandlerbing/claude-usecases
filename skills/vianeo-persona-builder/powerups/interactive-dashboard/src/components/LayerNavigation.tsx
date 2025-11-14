import React from 'react';
import { LayerNavigationProps } from '../types';

/**
 * LayerNavigation Component
 *
 * Displays the 4-layer navigation grid for Vianeo persona structure
 */
export const LayerNavigation: React.FC<LayerNavigationProps> = ({
  layers,
  activeLayer,
  onLayerClick,
  colors
}) => {
  return (
    <>
      <div
        style={{
          fontSize: '11px',
          textTransform: 'uppercase',
          letterSpacing: '1.5px',
          color: '#78716c',
          marginBottom: '16px',
          marginTop: '32px',
          fontWeight: '600'
        }}
      >
        Vianeo Four-Layer Structure
      </div>

      <div
        style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
          gap: '14px',
          marginBottom: '32px'
        }}
        role="navigation"
        aria-label="Persona layers navigation"
      >
        {layers.map((layer) => {
          const isActiveLayer = activeLayer === layer.id;

          return (
            <div
              key={layer.id}
              onClick={() => onLayerClick(layer.id)}
              onKeyPress={(e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                  onLayerClick(layer.id);
                }
              }}
              tabIndex={0}
              role="button"
              aria-pressed={isActiveLayer}
              aria-label={`View ${layer.title}`}
              style={{
                background: isActiveLayer ? colors.accent : '#fafaf9',
                border: `2px solid ${isActiveLayer ? colors.border : '#e7e5e4'}`,
                borderRadius: '6px',
                padding: '18px',
                cursor: 'pointer',
                transition: 'all 0.2s ease',
                outline: 'none'
              }}
            >
              <div
                style={{
                  fontSize: '12px',
                  fontWeight: '600',
                  color: colors.stat,
                  marginBottom: '8px'
                }}
              >
                Layer {layer.number}
              </div>

              <div
                style={{
                  fontSize: '16px',
                  fontWeight: '500',
                  color: '#292524',
                  marginBottom: '4px'
                }}
              >
                {layer.title}
              </div>

              <div
                style={{
                  fontSize: '12px',
                  color: '#78716c'
                }}
              >
                {layer.subtitle}
              </div>
            </div>
          );
        })}
      </div>
    </>
  );
};
