import React, { useState } from 'react';
import { DashboardData, PersonaColors, PersonaType } from './types';
import { PersonaCard } from './components/PersonaCard';
import { LayerNavigation } from './components/LayerNavigation';
import { LayerContent } from './components/LayerContent';

/**
 * VianeoPersonaExplorer
 *
 * Interactive dashboard for exploring Vianeo persona data.
 * Displays personas with 4-layer structure, evidence tracking, and validation status.
 *
 * @param data - Dashboard data containing personas and layer content
 */

interface VianeoPersonaExplorerProps {
  data: DashboardData;
}

// Color schemes for different persona types
const personaTypeColors: Record<PersonaType, PersonaColors> = {
  partner: {
    border: '#64748b',
    accent: '#f8fafc',
    stat: '#475569',
    subtle: '#e2e8f0'
  },
  innovator: {
    border: '#059669',
    accent: '#f0fdf4',
    stat: '#047857',
    subtle: '#d1fae5'
  },
  stakeholder: {
    border: '#7c3aed',
    accent: '#faf5ff',
    stat: '#6d28d9',
    subtle: '#e9d5ff'
  },
  beneficiary: {
    border: '#d97706',
    accent: '#fffbeb',
    stat: '#b45309',
    subtle: '#fde68a'
  }
};

export const VianeoPersonaExplorer: React.FC<VianeoPersonaExplorerProps> = ({ data }) => {
  const [activePersona, setActivePersona] = useState<string | null>(null);
  const [activeLayer, setActiveLayer] = useState<string | null>(null);

  const handlePersonaClick = (personaId: string) => {
    setActivePersona(personaId);
    setActiveLayer(null); // Reset layer when switching personas
  };

  const handleLayerClick = (layerId: string) => {
    setActiveLayer(layerId);
  };

  return (
    <div
      style={{
        fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
        background: 'linear-gradient(135deg, #fafaf9 0%, #f5f5f4 100%)',
        padding: '40px 20px',
        minHeight: '100vh',
        color: '#1a1a1a'
      }}
    >
      <div style={{ maxWidth: '1400px', margin: '0 auto' }}>
        {/* Header */}
        <header
          style={{
            textAlign: 'center',
            marginBottom: '48px',
            paddingBottom: '32px',
            borderBottom: '2px solid #e7e5e4'
          }}
        >
          <div
            style={{
              textTransform: 'uppercase',
              letterSpacing: '3px',
              fontSize: '11px',
              fontWeight: '500',
              color: '#78716c',
              marginBottom: '12px'
            }}
          >
            Vianeo Business Validation Framework
          </div>

          <h1
            style={{
              fontSize: '42px',
              fontWeight: '300',
              letterSpacing: '-0.5px',
              marginBottom: '16px',
              color: '#292524',
              margin: '0 0 16px 0'
            }}
          >
            Stakeholder Persona Explorer
          </h1>

          <p
            style={{
              fontSize: '16px',
              color: '#57534e',
              maxWidth: '700px',
              margin: '0 auto',
              lineHeight: '1.7'
            }}
          >
            Navigate through validated stakeholder personas built from research data.
            Each persona follows the Vianeo four-layer structure with evidence tracking.
          </p>

          {/* Metadata */}
          {data.metadata && (
            <div
              style={{
                marginTop: '20px',
                fontSize: '13px',
                color: '#78716c'
              }}
            >
              {data.metadata.projectName && (
                <span style={{ marginRight: '20px' }}>
                  <strong>Project:</strong> {data.metadata.projectName}
                </span>
              )}
              {data.metadata.createdDate && (
                <span>
                  <strong>Created:</strong> {data.metadata.createdDate}
                </span>
              )}
            </div>
          )}
        </header>

        {/* Persona Cards Grid */}
        <div
          style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
            gap: '20px',
            marginBottom: '48px'
          }}
        >
          {Object.entries(data.personas).map(([id, persona]) => {
            const colors = personaTypeColors[persona.type];
            const isActive = activePersona === id;

            return (
              <PersonaCard
                key={id}
                id={id}
                persona={persona}
                isActive={isActive}
                onClick={() => handlePersonaClick(id)}
                colors={colors}
              />
            );
          })}
        </div>

        {/* Active Persona Detail */}
        {activePersona && data.personas[activePersona] && (
          <div
            style={{
              background: '#ffffff',
              border: `2px solid ${personaTypeColors[data.personas[activePersona].type].border}`,
              borderRadius: '8px',
              padding: '32px',
              marginBottom: '32px'
            }}
          >
            <h2
              style={{
                fontSize: '32px',
                fontWeight: '300',
                color: personaTypeColors[data.personas[activePersona].type].border,
                marginBottom: '12px',
                margin: '0 0 12px 0'
              }}
            >
              {data.personas[activePersona].title}
            </h2>

            <p
              style={{
                fontSize: '16px',
                color: '#57534e',
                marginBottom: '20px',
                margin: '0 0 20px 0'
              }}
            >
              {data.personas[activePersona].evidenceSummary}
            </p>

            {/* Layer Navigation */}
            <LayerNavigation
              layers={data.personas[activePersona].layers}
              activeLayer={activeLayer}
              onLayerClick={handleLayerClick}
              colors={personaTypeColors[data.personas[activePersona].type]}
            />

            {/* Layer Content */}
            {activeLayer && data.layerContent[activeLayer] && (
              <LayerContent
                layerId={activeLayer}
                content={data.layerContent[activeLayer]}
                colors={personaTypeColors[data.personas[activePersona].type]}
              />
            )}
          </div>
        )}

        {/* Empty State */}
        {!activePersona && (
          <div
            style={{
              textAlign: 'center',
              padding: '60px 20px',
              color: '#78716c'
            }}
          >
            <p style={{ fontSize: '18px', marginBottom: '10px', margin: '0 0 10px 0' }}>
              Select a persona above to explore their four-layer structure
            </p>
            <p style={{ fontSize: '14px', margin: 0 }}>
              Click on any persona card to view detailed information and evidence
            </p>
          </div>
        )}

        {/* Footer */}
        <footer
          style={{
            marginTop: '60px',
            paddingTop: '30px',
            borderTop: '1px solid #e7e5e4',
            textAlign: 'center',
            fontSize: '12px',
            color: '#a8a29e'
          }}
        >
          <p style={{ margin: 0 }}>
            Generated with Vianeo Persona Builder • Interactive Dashboard v1.0
          </p>
        </footer>
      </div>
    </div>
  );
};

export default VianeoPersonaExplorer;
