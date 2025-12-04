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
 * Import dashboard data from JSON string
 */
export function importFromJSON(jsonString: string): DashboardData {
  return JSON.parse(jsonString);
}
