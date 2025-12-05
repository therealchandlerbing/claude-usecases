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
 * Transform Vianeo Persona Builder markdown output to dashboard data format.
 *
 * This function parses the standard markdown output from the Vianeo Persona Builder
 * skill and converts it into the DashboardData format used by the interactive dashboard.
 *
 * @param markdown - Raw markdown text from Vianeo Persona Builder output
 * @param personaId - Unique identifier for this persona (e.g., 'partner-maria')
 * @returns Partial<DashboardData> containing the parsed persona and layer content
 */
export function transformMarkdownToData(markdown: string, personaId: string): Partial<DashboardData> {
  // Extract persona metadata from header
  const personaName = extractPersonaName(markdown);
  const personaType = parsePersonaType(markdown);

  // Extract validation status line specifically to avoid false matches from other "not" occurrences
  const validationStatusLine = markdown.match(/\*\*Validation Status:\*\*\s*(.+?)[\n\r]/)?.[1] || markdown;
  const validationStatus = parseValidationStatus(validationStatusLine);

  const qualityScore = parseQualityScore(markdown);
  const interviewCount = parseInterviewCount(markdown);

  // Extract subtitle from context
  const subtitle = extractSubtitle(markdown);
  const evidenceSummary = extractEvidenceSummary(markdown);

  // Create layer IDs
  const layerIds = {
    layer1: `${personaId}-layer1`,
    layer2: `${personaId}-layer2`,
    layer3: `${personaId}-layer3`,
    layer4: `${personaId}-layer4`
  };

  // Define persona with layers
  const persona: Persona = {
    type: personaType,
    title: personaName,
    subtitle: subtitle,
    validationStatus: validationStatus,
    interviewCount: interviewCount,
    qualityScore: qualityScore,
    evidenceSummary: evidenceSummary,
    layers: [
      { id: layerIds.layer1, number: '1', title: 'Requester', subtitle: 'Who They Are' },
      { id: layerIds.layer2, number: '2', title: 'Field of Application', subtitle: 'Their World' },
      { id: layerIds.layer3, number: '3', title: 'Activities & Challenges', subtitle: 'What They Do' },
      { id: layerIds.layer4, number: '4', title: 'Current Solutions', subtitle: 'Present Reality' }
    ]
  };

  // Parse layer content
  const layerContent: LayerContentMap = {};

  // Layer 1: Who They Are (field-based)
  const layer1Content = extractLayer1Content(markdown);
  layerContent[layerIds.layer1] = {
    title: 'Layer 1: Who They Are',
    fields: layer1Content.fields,
    quotes: layer1Content.quotes
  };

  // Layer 2: Their World (field-based)
  const layer2Content = extractLayer2Content(markdown);
  layerContent[layerIds.layer2] = {
    title: 'Layer 2: Their World',
    fields: layer2Content.fields,
    quotes: layer2Content.quotes
  };

  // Layer 3: Activities & Challenges (section-based)
  const layer3Content = extractLayer3Content(markdown);
  layerContent[layerIds.layer3] = {
    title: 'Layer 3: Activities & Challenges',
    sections: layer3Content.sections,
    quotes: layer3Content.quotes
  };

  // Layer 4: Current Solutions (content-based)
  const layer4Content = extractLayer4Content(markdown);
  layerContent[layerIds.layer4] = {
    title: 'Layer 4: Current Solutions',
    content: layer4Content.content,
    source: layer4Content.source,
    gaps: layer4Content.gaps,
    quotes: layer4Content.quotes
  };

  return {
    personas: {
      [personaId]: persona
    },
    layerContent: layerContent,
    metadata: {
      createdDate: new Date().toISOString().split('T')[0],
      version: '1.0'
    }
  };
}

/**
 * Extract persona name from markdown
 */
function extractPersonaName(markdown: string): string {
  // Try "## Persona: Name" format
  const personaMatch = markdown.match(/##\s*Persona:\s*(.+?)[\n\r]/);
  if (personaMatch) return personaMatch[1].trim();

  // Try "**Name:** Value" format
  const nameMatch = markdown.match(/\*\*Name:\*\*\s*(.+?)[\n\r]/);
  if (nameMatch) return nameMatch[1].trim();

  // Try title
  const titleMatch = markdown.match(/^#\s+(?:Example:\s*)?(.+?)[\n\r]/m);
  if (titleMatch) return titleMatch[1].trim();

  return 'Unknown Persona';
}

/**
 * Extract subtitle/context from markdown
 */
function extractSubtitle(markdown: string): string {
  const contextMatch = markdown.match(/\*\*Geographic Context:\*\*\s*(.+?)[\n\r]/);
  if (contextMatch) return contextMatch[1].trim();

  const sourcesMatch = markdown.match(/\*\*Sources?:\*\*\s*(.+?)[\n\r]/);
  if (sourcesMatch) return sourcesMatch[1].trim();

  return 'Evidence-based persona';
}

/**
 * Extract evidence summary from markdown
 */
function extractEvidenceSummary(markdown: string): string {
  const sourcesMatch = markdown.match(/\*\*Sources?:\*\*\s*(.+?)[\n\r]/);
  if (sourcesMatch) return `Based on ${sourcesMatch[1].trim()}`;

  const interviewCount = parseInterviewCount(markdown);
  if (interviewCount > 0) {
    return `Based on ${interviewCount} interviews`;
  }

  return 'Evidence-based persona';
}

/**
 * Extract Layer 1 content (Who They Are)
 */
function extractLayer1Content(markdown: string): { fields: Array<{ label: string; content: string; source: string }>; quotes: Array<{ text: string; author: string; source: string }> } {
  const section = extractSection(markdown, ['Layer 1', 'Requester']);
  const fields: Array<{ label: string; content: string; source: string }> = [];

  // Extract Name
  const nameMatch = section.match(/\*\*Name:\*\*\s*(.+?)[\n\r]/);
  if (nameMatch) {
    fields.push({ label: 'First Name', content: nameMatch[1].trim(), source: 'Interview data' });
  }

  // Extract Age
  const ageMatch = section.match(/\*\*Age:\*\*\s*(.+?)[\n\r]/);
  if (ageMatch) {
    fields.push({ label: 'Age', content: ageMatch[1].trim(), source: 'Interview data' });
  }

  // Extract Life/Motivations
  const lifeMatch = extractFieldContent(section, 'Life / Motivations');
  if (lifeMatch) {
    fields.push({ label: 'Life/Motivations', content: lifeMatch, source: 'Interview data' });
  }

  // Extract Personality/Values
  const personalityMatch = extractFieldContent(section, 'Personality / Values');
  if (personalityMatch) {
    fields.push({ label: 'Personality/Values', content: personalityMatch, source: 'Interview data' });
  }

  const quotes = extractQuotes(section);

  return { fields, quotes };
}

/**
 * Extract Layer 2 content (Their World)
 */
function extractLayer2Content(markdown: string): { fields: Array<{ label: string; content: string; source: string }>; quotes: Array<{ text: string; author: string; source: string }> } {
  const section = extractSection(markdown, ['Layer 2', 'Field of Application']);
  const fields: Array<{ label: string; content: string; source: string }> = [];

  // Extract Thinks/Feels
  const thinksMatch = extractFieldContent(section, 'Thinks / Feels');
  if (thinksMatch) {
    fields.push({ label: 'Thinks/Feels', content: thinksMatch, source: 'Interview data' });
  }

  // Extract Observes
  const observesMatch = extractFieldContent(section, 'Observes');
  if (observesMatch) {
    fields.push({ label: 'Observes', content: observesMatch, source: 'Interview data' });
  }

  // Extract Does
  const doesMatch = extractFieldContent(section, 'Does');
  if (doesMatch) {
    fields.push({ label: 'Does', content: doesMatch, source: 'Interview data' });
  }

  // Extract Others Say
  const othersSayMatch = extractFieldContent(section, 'Others Say');
  if (othersSayMatch) {
    fields.push({ label: 'Others Say', content: othersSayMatch, source: 'Interview data' });
  }

  const quotes = extractQuotes(section);

  return { fields, quotes };
}

/**
 * Extract Layer 3 content (Activities & Challenges)
 */
function extractLayer3Content(markdown: string): { sections: Array<{ label: string; items: string[] }>; quotes: Array<{ text: string; author: string; source: string }> } {
  const section = extractSection(markdown, ['Layer 3', 'Activities and Challenges', 'Activities & Challenges']);
  const sections: Array<{ label: string; items: string[] }> = [];

  // Extract Tasks/Activities
  const tasksSection = extractListSection(section, 'Tasks / Activities');
  if (tasksSection.length > 0) {
    sections.push({ label: 'Tasks/Activities', items: tasksSection });
  }

  // Extract Pains/Lacks
  const painsSection = extractListSection(section, 'Pains / Lacks');
  if (painsSection.length > 0) {
    sections.push({ label: 'Pains/Lacks', items: painsSection });
  }

  // Extract Expectations/Hopes
  const hopesSection = extractListSection(section, 'Expectations / Hopes');
  if (hopesSection.length > 0) {
    sections.push({ label: 'Expectations/Hopes', items: hopesSection });
  }

  const quotes = extractQuotes(section);

  return { sections, quotes };
}

/**
 * Extract Layer 4 content (Current Solutions)
 */
function extractLayer4Content(markdown: string): { content: string; source: string; gaps: string[]; quotes: Array<{ text: string; author: string; source: string }> } {
  const section = extractSection(markdown, ['Layer 4', 'Current Solutions']);

  // Extract main content
  const contentMatch = extractFieldContent(section, 'Current Solutions');
  const content = contentMatch || section.replace(/\*\*Evidence Notes:\*\*[\s\S]*$/, '').trim() || 'Current solutions not specified';

  // Extract evidence notes as source
  const evidenceMatch = section.match(/\*\*Evidence Notes:\*\*[\s\S]*?(?=---|\n##|$)/);
  const source = evidenceMatch
    ? extractBulletPoints(evidenceMatch[0]).join('; ')
    : 'Interview data';

  // Extract gaps (often found in evidence notes or as bullet points)
  const gapsSection = extractListSection(section, 'Gaps');
  const gaps = gapsSection.length > 0 ? gapsSection : [];

  const quotes = extractQuotes(section);

  return { content, source, gaps, quotes };
}

/**
 * Extract a section from markdown by heading
 */
function extractSection(markdown: string, headingKeywords: string[]): string {
  for (const keyword of headingKeywords) {
    const pattern = new RegExp(`###?\\s*.*${keyword}.*[\\n\\r]([\\s\\S]*?)(?=###|---|$)`, 'i');
    const match = markdown.match(pattern);
    if (match) return match[1];
  }
  return '';
}

/**
 * Extract field content from bold label format
 */
function extractFieldContent(section: string, fieldName: string): string | null {
  const pattern = new RegExp(`\\*\\*${fieldName}:?\\*\\*[\\s\\n]*([\\s\\S]*?)(?=\\*\\*[A-Z]|\\*\\*Evidence|---|\n###|$)`, 'i');
  const match = section.match(pattern);
  if (match) {
    return match[1].trim().replace(/\n+/g, ' ');
  }
  return null;
}

/**
 * Extract list section content
 */
function extractListSection(section: string, sectionName: string): string[] {
  const pattern = new RegExp(`\\*\\*${sectionName}:?\\*\\*[\\s\\n]*([\\s\\S]*?)(?=\\*\\*[A-Z]|\\*\\*Evidence|---|\n###|$)`, 'i');
  const match = section.match(pattern);
  if (match) {
    return extractBulletPoints(match[1]);
  }
  return [];
}

/**
 * Export dashboard data to JSON file
 */
export function exportToJSON(data: DashboardData): string {
  return JSON.stringify(data, null, 2);
}

/**
 * Validation error for JSON import
 */
export class DashboardDataValidationError extends Error {
  constructor(message: string, public readonly path: string) {
    super(`Invalid DashboardData at ${path}: ${message}`);
    this.name = 'DashboardDataValidationError';
  }
}

/**
 * Validate a Quote object
 */
function validateQuote(quote: unknown, path: string): boolean {
  if (typeof quote !== 'object' || quote === null) {
    throw new DashboardDataValidationError('Quote must be an object', path);
  }
  const q = quote as Record<string, unknown>;
  if (typeof q.text !== 'string') {
    throw new DashboardDataValidationError('Quote.text must be a string', `${path}.text`);
  }
  if (typeof q.author !== 'string') {
    throw new DashboardDataValidationError('Quote.author must be a string', `${path}.author`);
  }
  if (typeof q.source !== 'string') {
    throw new DashboardDataValidationError('Quote.source must be a string', `${path}.source`);
  }
  return true;
}

/**
 * Validate a Persona object
 */
function validatePersona(persona: unknown, path: string): boolean {
  if (typeof persona !== 'object' || persona === null) {
    throw new DashboardDataValidationError('Persona must be an object', path);
  }
  const p = persona as Record<string, unknown>;

  // Required string fields
  const requiredStrings = ['type', 'title', 'subtitle', 'validationStatus', 'evidenceSummary'] as const;
  for (const field of requiredStrings) {
    if (typeof p[field] !== 'string') {
      throw new DashboardDataValidationError(`Persona.${field} must be a string`, `${path}.${field}`);
    }
  }

  // Validate type is valid PersonaType
  const validTypes = ['partner', 'innovator', 'stakeholder', 'beneficiary'];
  if (!validTypes.includes(p.type as string)) {
    throw new DashboardDataValidationError(
      `Persona.type must be one of: ${validTypes.join(', ')}`,
      `${path}.type`
    );
  }

  // Validate validationStatus
  const validStatuses = ['validated', 'inferred', 'hybrid'];
  if (!validStatuses.includes(p.validationStatus as string)) {
    throw new DashboardDataValidationError(
      `Persona.validationStatus must be one of: ${validStatuses.join(', ')}`,
      `${path}.validationStatus`
    );
  }

  // Required number fields
  if (typeof p.interviewCount !== 'number') {
    throw new DashboardDataValidationError('Persona.interviewCount must be a number', `${path}.interviewCount`);
  }
  if (typeof p.qualityScore !== 'number') {
    throw new DashboardDataValidationError('Persona.qualityScore must be a number', `${path}.qualityScore`);
  }

  // Validate layers array
  if (!Array.isArray(p.layers)) {
    throw new DashboardDataValidationError('Persona.layers must be an array', `${path}.layers`);
  }
  for (let i = 0; i < p.layers.length; i++) {
    const layer = p.layers[i] as Record<string, unknown>;
    if (typeof layer.id !== 'string') {
      throw new DashboardDataValidationError('Layer.id must be a string', `${path}.layers[${i}].id`);
    }
    if (typeof layer.number !== 'string') {
      throw new DashboardDataValidationError('Layer.number must be a string', `${path}.layers[${i}].number`);
    }
    if (typeof layer.title !== 'string') {
      throw new DashboardDataValidationError('Layer.title must be a string', `${path}.layers[${i}].title`);
    }
    if (typeof layer.subtitle !== 'string') {
      throw new DashboardDataValidationError('Layer.subtitle must be a string', `${path}.layers[${i}].subtitle`);
    }
  }

  return true;
}

/**
 * Validate LayerContent (any type)
 */
function validateLayerContent(content: unknown, path: string): boolean {
  if (typeof content !== 'object' || content === null) {
    throw new DashboardDataValidationError('LayerContent must be an object', path);
  }
  const c = content as Record<string, unknown>;

  if (typeof c.title !== 'string') {
    throw new DashboardDataValidationError('LayerContent.title must be a string', `${path}.title`);
  }

  // Validate quotes if present
  if (c.quotes !== undefined) {
    if (!Array.isArray(c.quotes)) {
      throw new DashboardDataValidationError('LayerContent.quotes must be an array', `${path}.quotes`);
    }
    for (let i = 0; i < c.quotes.length; i++) {
      validateQuote(c.quotes[i], `${path}.quotes[${i}]`);
    }
  }

  // Validate field-based layers (Layer 1 & 2)
  if ('fields' in c) {
    if (!Array.isArray(c.fields)) {
      throw new DashboardDataValidationError('fields must be an array', `${path}.fields`);
    }
    for (let i = 0; i < c.fields.length; i++) {
      const field = c.fields[i] as Record<string, unknown>;
      if (typeof field.label !== 'string') {
        throw new DashboardDataValidationError('Field.label must be a string', `${path}.fields[${i}].label`);
      }
      if (typeof field.content !== 'string') {
        throw new DashboardDataValidationError('Field.content must be a string', `${path}.fields[${i}].content`);
      }
      if (typeof field.source !== 'string') {
        throw new DashboardDataValidationError('Field.source must be a string', `${path}.fields[${i}].source`);
      }
    }
  }

  // Validate section-based layers (Layer 3)
  if ('sections' in c) {
    if (!Array.isArray(c.sections)) {
      throw new DashboardDataValidationError('sections must be an array', `${path}.sections`);
    }
    for (let i = 0; i < c.sections.length; i++) {
      const section = c.sections[i] as Record<string, unknown>;
      if (typeof section.label !== 'string') {
        throw new DashboardDataValidationError('Section.label must be a string', `${path}.sections[${i}].label`);
      }
      if (!Array.isArray(section.items)) {
        throw new DashboardDataValidationError('Section.items must be an array', `${path}.sections[${i}].items`);
      }
    }
  }

  // Validate content-based layers (Layer 4)
  if ('content' in c && typeof c.content === 'string') {
    if (typeof c.source !== 'string') {
      throw new DashboardDataValidationError('source must be a string', `${path}.source`);
    }
    if (c.gaps !== undefined && !Array.isArray(c.gaps)) {
      throw new DashboardDataValidationError('gaps must be an array', `${path}.gaps`);
    }
  }

  return true;
}

/**
 * Validate DashboardData structure
 */
export function validateDashboardData(data: unknown): data is DashboardData {
  if (typeof data !== 'object' || data === null) {
    throw new DashboardDataValidationError('DashboardData must be an object', 'root');
  }

  const d = data as Record<string, unknown>;

  // Validate personas
  if (typeof d.personas !== 'object' || d.personas === null) {
    throw new DashboardDataValidationError('personas must be an object', 'personas');
  }
  for (const [personaId, persona] of Object.entries(d.personas as Record<string, unknown>)) {
    validatePersona(persona, `personas.${personaId}`);
  }

  // Validate layerContent
  if (typeof d.layerContent !== 'object' || d.layerContent === null) {
    throw new DashboardDataValidationError('layerContent must be an object', 'layerContent');
  }
  for (const [layerId, content] of Object.entries(d.layerContent as Record<string, unknown>)) {
    validateLayerContent(content, `layerContent.${layerId}`);
  }

  // Validate metadata if present (optional)
  if (d.metadata !== undefined) {
    if (typeof d.metadata !== 'object' || d.metadata === null) {
      throw new DashboardDataValidationError('metadata must be an object', 'metadata');
    }
  }

  return true;
}

/**
 * Import dashboard data from JSON string with validation
 *
 * @throws {SyntaxError} If JSON is malformed
 * @throws {DashboardDataValidationError} If data structure is invalid
 */
export function importFromJSON(jsonString: string): DashboardData {
  const data = JSON.parse(jsonString);
  validateDashboardData(data);
  return data as DashboardData;
}
