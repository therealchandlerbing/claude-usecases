/**
 * Data Transformation Utilities
 *
 * Converts Vianeo Persona Builder markdown output to dashboard JSON format.
 * Supports both strategic and platform-ready versions.
 */

import {
  DashboardData,
  Persona,
  LayerContentMap,
  PersonaType,
  ValidationStatus
} from '../types';

/**
 * Parse persona type from text
 */
export function parsePersonaType(text: string): PersonaType {
  const normalized = text.toLowerCase();
  if (normalized.includes('partner')) return 'partner';
  if (normalized.includes('innovator')) return 'innovator';
  if (normalized.includes('stakeholder')) return 'stakeholder';
  if (normalized.includes('beneficiary')) return 'beneficiary';
  return 'partner'; // default
}

/**
 * Parse validation status from text
 */
export function parseValidationStatus(text: string): ValidationStatus {
  const normalized = text.toLowerCase();
  if (normalized.includes('validated') && !normalized.includes('not')) return 'validated';
  if (normalized.includes('inferred') || normalized.includes('not yet validated')) return 'inferred';
  if (normalized.includes('hybrid') || normalized.includes('partial')) return 'hybrid';
  return 'inferred'; // default to inferred if unclear
}

/**
 * Extract quotes from markdown sections
 */
export function extractQuotes(markdownText: string): Array<{ text: string; author: string; source: string }> {
  const quotes: Array<{ text: string; author: string; source: string }> = [];

  // Pattern: "Quote text" (Author, Source) or similar variations
  const quotePattern = /"([^"]+)"\s*[-–]\s*([^,\n]+)(?:,\s*(.+?))?(?:\n|$)/g;

  let match;
  while ((match = quotePattern.exec(markdownText)) !== null) {
    quotes.push({
      text: match[1].trim(),
      author: match[2].trim(),
      source: match[3]?.trim() || 'Interview'
    });
  }

  return quotes;
}

/**
 * Extract bullet points from markdown
 */
export function extractBulletPoints(markdownText: string): string[] {
  const bullets: string[] = [];
  const lines = markdownText.split('\n');

  for (const line of lines) {
    const trimmed = line.trim();
    if (trimmed.startsWith('- ') || trimmed.startsWith('* ')) {
      bullets.push(trimmed.substring(2).trim());
    } else if (/^\d+\.\s/.test(trimmed)) {
      bullets.push(trimmed.replace(/^\d+\.\s/, '').trim());
    }
  }

  return bullets;
}

/**
 * Parse quality score from text
 */
export function parseQualityScore(text: string): number {
  const scoreMatch = text.match(/score[:\s]+(\d+)/i);
  if (scoreMatch) {
    return parseInt(scoreMatch[1], 10);
  }

  // Try to extract from X/5 format
  const ratingMatch = text.match(/(\d+)\s*\/\s*5/);
  if (ratingMatch) {
    return parseInt(ratingMatch[1], 10);
  }

  return 3; // default
}

/**
 * Parse interview count from text
 */
export function parseInterviewCount(text: string): number {
  const countMatch = text.match(/(\d+)\s+interview/i);
  if (countMatch) {
    return parseInt(countMatch[1], 10);
  }
  return 0;
}

/**
 * Create sample dashboard data
 *
 * This is a helper function for testing and examples.
 * In production, use transformMarkdownToData() to convert actual persona builder output.
 */
export function createSampleDashboardData(): DashboardData {
  return {
    personas: {
      'university-partner': {
        type: 'partner',
        title: 'Research University Tech Transfer Office',
        subtitle: 'Major Brazilian public university with active R&D portfolio',
        validationStatus: 'validated',
        interviewCount: 8,
        qualityScore: 4,
        evidenceSummary: 'Based on 8 stakeholder interviews, 12 partnership meetings',
        layers: [
          { id: 'layer1', number: '1', title: 'Requester', subtitle: 'Who They Are' },
          { id: 'layer2', number: '2', title: 'Field of Application', subtitle: 'Their World' },
          { id: 'layer3', number: '3', title: 'Activities & Challenges', subtitle: 'What They Do' },
          { id: 'layer4', number: '4', title: 'Current Solutions', subtitle: 'Present Reality' }
        ]
      },
      'early-innovator': {
        type: 'innovator',
        title: 'Academic Researcher Seeking Commercialization',
        subtitle: 'PhD researcher with novel biotech platform',
        validationStatus: 'hybrid',
        interviewCount: 5,
        qualityScore: 3,
        evidenceSummary: 'Based on 5 researcher interviews and 8 months engagement',
        layers: [
          { id: 'layer1-i', number: '1', title: 'Requester', subtitle: 'Who They Are' },
          { id: 'layer2-i', number: '2', title: 'Field of Application', subtitle: 'Their World' },
          { id: 'layer3-i', number: '3', title: 'Activities & Challenges', subtitle: 'What They Do' },
          { id: 'layer4-i', number: '4', title: 'Current Solutions', subtitle: 'Present Reality' }
        ]
      }
    },
    layerContent: {
      'layer1': {
        title: 'Layer 1: Who They Are',
        fields: [
          {
            label: 'First Name',
            content: 'Dr. Maria',
            source: 'Interview #1, #3, #5'
          },
          {
            label: 'Age',
            content: '47',
            source: 'Interview #1'
          },
          {
            label: 'Life/Motivations',
            content: 'Leads the technology transfer office at a major public research university in São Paulo. Came to the role five years ago after 15 years as faculty researcher. Success means increasing commercialization rate while maintaining the university\'s social mission.',
            source: 'Interview #1, #2, #5'
          },
          {
            label: 'Personality/Values',
            content: 'Highly strategic and relationship-focused, believing partnerships succeed through trust built over time. Values transparency and becomes skeptical when partners seem more interested in IP acquisition than collaborative development.',
            source: 'Interview #1, #3, #5, Meeting observations'
          }
        ],
        quotes: [
          {
            text: 'Our researchers want partners who understand the social impact potential and will develop it with Brazilian communities in mind.',
            author: 'Dr. Maria, Interview #1',
            source: 'Interview March 2024'
          }
        ]
      },
      'layer2': {
        title: 'Layer 2: Their World',
        fields: [
          {
            label: 'Thinks/Feels',
            content: 'Constantly balancing pressure to increase commercialization rates with need to protect faculty relationships and university reputation. Frustrated when potential partners treat the university as a simple IP vendor rather than collaborative partner.',
            source: 'Interview #2, #5, #7'
          },
          {
            label: 'Observes',
            content: 'Watches other Brazilian universities struggle with similar challenges, noting that those who rush into partnerships often regret it later. Sees international partners increasingly interested in Latin American innovation but notes cultural mismatches in communication style.',
            source: 'Interview #1, #3, #6'
          },
          {
            label: 'Does',
            content: 'Spends 40% of time building relationships with potential partners before any formal discussions begin. Maintains detailed records of every partner interaction to demonstrate progress to university administration.',
            source: 'Interview #2, #4, Calendar analysis'
          },
          {
            label: 'Others Say',
            content: 'Faculty inventors praise her patience and strategic thinking but sometimes wish processes moved faster. University administration values her relationship-building but pressures her to show more concrete commercialization numbers.',
            source: 'Interview #3, #6, #8'
          }
        ],
        quotes: [
          {
            text: 'When I explain to US partners that we need three months to get faculty alignment, they think we\'re being difficult. But that\'s how you build partnerships that last 10 years.',
            author: 'Dr. Maria, Interview #3',
            source: 'Interview April 2024'
          }
        ]
      },
      'layer3': {
        title: 'Layer 3: Activities & Challenges',
        sections: [
          {
            label: 'Tasks/Activities',
            items: [
              'Evaluate 40+ technologies for commercialization potential and social impact alignment',
              'Build and maintain relationships with 20-30 potential partner organizations globally',
              'Coordinate between faculty inventors, university administration, and external partners',
              'Review and negotiate partnership agreements ensuring IP protection and mission alignment',
              'Track portfolio progress and report metrics to university leadership quarterly'
            ]
          },
          {
            label: 'Pains/Lacks',
            items: [
              'No systematic way to assess which partners are genuinely committed vs. exploring options',
              'Faculty inventors often lack business context, requiring extensive education for each partnership',
              'University bureaucracy creates 90-120 day decision cycles that lose impatient partners',
              'Limited budget for market validation, forcing reliance on partner resources',
              'Difficulty finding partners who understand both technology and Brazilian market context'
            ]
          },
          {
            label: 'Expectations/Hopes',
            items: [
              'Reduce time spent on non-serious partners from 40% to under 20%',
              'Increase faculty engagement with commercialization from reluctant to enthusiastic',
              'Find validation frameworks that both university and partners trust and respect',
              'Build repeatable partnership models that don\'t require reinventing process each time',
              'Double commercialization rate while maintaining 100% social impact alignment'
            ]
          }
        ],
        quotes: [
          {
            text: 'I spend so much time on partnerships that go nowhere because the partner was never really committed. I need better ways to qualify serious partners early.',
            author: 'Dr. Maria, Interview #5',
            source: 'Interview July 2024'
          }
        ]
      },
      'layer4': {
        title: 'Layer 4: Current Solutions',
        content: 'Currently uses a combination of informal relationship-building, manual technology assessment spreadsheets, and ad-hoc partnership processes that vary by partner and technology. Relies heavily on personal network and reputation rather than systematic evaluation frameworks. The university\'s legal team handles contract negotiations using templates that require extensive customization for each partnership. Technology validation happens through partner-funded pilots or research grants, creating misaligned incentives. The system works for established relationships but breaks down when trying to scale or engage with new partners who don\'t yet have trust built up.',
        source: 'Interview #2, #4, #6, Process documentation',
        gaps: [
          'No systematic partner qualification framework',
          'No standardized technology validation methodology',
          'No scalable partnership templates beyond basic legal agreements',
          'No objective metrics for assessing partnership readiness'
        ],
        quotes: [
          {
            text: 'We have spreadsheets and email threads, but nothing that gives us or partners a clear, objective view of where a technology stands. It\'s all relationship-based, which doesn\'t scale.',
            author: 'Dr. Maria, Interview #4',
            source: 'Interview May 2024'
          }
        ]
      },
      // Innovator persona layers would be similar...
      'layer1-i': {
        title: 'Layer 1: Who They Are',
        fields: [
          {
            label: 'First Name',
            content: 'Dr. João',
            source: 'Interview #1, Project records'
          },
          {
            label: 'Age',
            content: '34',
            source: 'Interview #1'
          }
        ]
      },
      'layer2-i': {
        title: 'Layer 2: Their World',
        fields: []
      },
      'layer3-i': {
        title: 'Layer 3: Activities & Challenges',
        sections: []
      },
      'layer4-i': {
        title: 'Layer 4: Current Solutions',
        content: 'Currently relying on university technology transfer office for partnership identification and support.',
        source: 'Interview #2, #3, #4',
        validation: 'hybrid',
        gaps: []
      }
    },
    metadata: {
      projectName: 'Brazilian University Innovation Partnerships',
      createdDate: '2024-11-14',
      version: '1.0'
    }
  };
}

/**
 * Export dashboard data to JSON file
 */
export function exportToJSON(data: DashboardData): string {
  return JSON.stringify(data, null, 2);
}

/**
 * Validation error class for JSON import
 */
export class ImportValidationError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'ImportValidationError';
  }
}

/**
 * Validate persona object structure
 */
function validatePersona(id: string, persona: unknown): void {
  if (!persona || typeof persona !== 'object') {
    throw new ImportValidationError(`Invalid persona "${id}": must be an object`);
  }

  const p = persona as Record<string, unknown>;

  if (!p.type || typeof p.type !== 'string') {
    throw new ImportValidationError(`Invalid persona "${id}": missing or invalid "type" field`);
  }

  const validTypes: PersonaType[] = ['partner', 'innovator', 'stakeholder', 'beneficiary'];
  if (!validTypes.includes(p.type as PersonaType)) {
    throw new ImportValidationError(`Invalid persona "${id}": type must be one of: ${validTypes.join(', ')}`);
  }

  if (!p.title || typeof p.title !== 'string') {
    throw new ImportValidationError(`Invalid persona "${id}": missing or invalid "title" field`);
  }

  if (!p.layers || !Array.isArray(p.layers)) {
    throw new ImportValidationError(`Invalid persona "${id}": missing or invalid "layers" array`);
  }
}

/**
 * Validate layer content structure
 */
function validateLayerContent(id: string, content: unknown): void {
  if (!content || typeof content !== 'object') {
    throw new ImportValidationError(`Invalid layer content "${id}": must be an object`);
  }

  const c = content as Record<string, unknown>;

  if (!c.title || typeof c.title !== 'string') {
    throw new ImportValidationError(`Invalid layer content "${id}": missing or invalid "title" field`);
  }

  // Layer 1, 2 should have fields array
  // Layer 3 should have sections array
  // Layer 4 should have content string
  // At least one of these should be present
  const hasFields = Array.isArray(c.fields);
  const hasSections = Array.isArray(c.sections);
  const hasContent = typeof c.content === 'string';

  if (!hasFields && !hasSections && !hasContent) {
    throw new ImportValidationError(
      `Invalid layer content "${id}": must have "fields", "sections", or "content"`
    );
  }
}

/**
 * Import dashboard data from JSON string with validation
 */
export function importFromJSON(jsonString: string): DashboardData {
  // Parse JSON
  let data: unknown;
  try {
    data = JSON.parse(jsonString);
  } catch (e) {
    throw new ImportValidationError(
      `Invalid JSON: ${e instanceof Error ? e.message : 'parse error'}`
    );
  }

  // Validate root structure
  if (!data || typeof data !== 'object') {
    throw new ImportValidationError('Invalid DashboardData: must be an object');
  }

  const d = data as Record<string, unknown>;

  // Validate personas object
  if (!d.personas || typeof d.personas !== 'object' || Array.isArray(d.personas)) {
    throw new ImportValidationError('Invalid DashboardData: missing or invalid "personas" object');
  }

  // Validate layerContent object
  if (!d.layerContent || typeof d.layerContent !== 'object' || Array.isArray(d.layerContent)) {
    throw new ImportValidationError('Invalid DashboardData: missing or invalid "layerContent" object');
  }

  // Validate each persona
  const personas = d.personas as Record<string, unknown>;
  for (const [id, persona] of Object.entries(personas)) {
    validatePersona(id, persona);
  }

  // Validate each layer content
  const layerContent = d.layerContent as Record<string, unknown>;
  for (const [id, content] of Object.entries(layerContent)) {
    validateLayerContent(id, content);
  }

  // Validate metadata if present
  if (d.metadata !== undefined && (typeof d.metadata !== 'object' || Array.isArray(d.metadata))) {
    throw new ImportValidationError('Invalid DashboardData: "metadata" must be an object if present');
  }

  return data as DashboardData;
}
