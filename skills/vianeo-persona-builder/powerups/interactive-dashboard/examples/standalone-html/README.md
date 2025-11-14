# Standalone HTML Persona Explorer

**Zero-dependency, single-file implementation** - Just open in a browser and go!

## Overview

This is the simplest way to deploy the Vianeo Persona Explorer. Everything you need is in a single HTML file:
- All CSS styles embedded
- All JavaScript code embedded
- All persona data embedded
- No build tools required
- No package.json required
- No npm install required

Perfect for quick demos, client deliverables, and sharing via email or file sharing.

## Quick Start

### Option 1: Open Directly
1. Double-click `index.html`
2. It will open in your default browser
3. That's it!

### Option 2: Serve Locally (Optional)
If you prefer to run a local server:

```bash
# Using Python 3
python3 -m http.server 8000

# Using Node.js
npx serve .

# Using PHP
php -S localhost:8000
```

Then open `http://localhost:8000` in your browser.

## Customizing the Data

All persona data is embedded in the `<script>` section of `index.html`. To customize:

### 1. Edit Persona Information

Find the `personas` object (around line 448) and modify:

```javascript
const personas = {
  'your-persona-id': {
    type: 'partner',  // or 'innovator', 'stakeholder', 'beneficiary'
    title: 'Your Persona Name',
    subtitle: 'Role/Description',
    evidenceSummary: 'Based on X interviews...',
    interviewCount: 8,
    quality: 4,  // 1-5 scale
    validationStatus: 'validated',  // 'validated', 'hybrid', or 'inferred'
    layers: [
      { id: 'layer1-id', title: 'Layer 1 Title', subtitle: 'Subtitle' },
      // ... 3 more layers
    ]
  }
};
```

### 2. Edit Layer Content

Find the `layerContent` object (around line 511) and modify:

```javascript
const layerContent = {
  'layer1-id': {
    title: 'Layer Title',
    fields: [
      {
        label: 'Field Name',
        content: 'Field description or insight',
        evidence: '8/8 interviews',
        validation: 'validated'  // 'validated', 'hybrid', or 'inferred'
      }
    ],
    sections: [
      {
        label: 'Section Name',
        items: ['Item 1', 'Item 2', 'Item 3'],
        validation: 'validated'
      }
    ],
    quotes: [
      {
        text: 'Quote from interview',
        author: 'Role, Organization',
        source: 'Interview #1'
      }
    ],
    gaps: [
      'Research gap or limitation to note'
    ]
  }
};
```

### 3. Customize Colors

The color scheme is defined in `personaTypeColors` (around line 421):

```javascript
const personaTypeColors = {
  partner: {
    border: '#64748b',    // Border and accent color
    accent: '#f8fafc',    // Light background
    stat: '#475569',      // Dark text
    subtle: '#e2e8f0'     // Badge background
  }
  // ... other types
};
```

## Features

### Validation Tracking
Each field, section, and persona can be marked with validation status:
- ✓ **Validated**: Confirmed by research data
- ◐ **Hybrid**: Mix of validated and inferred data
- ⚠ **Inferred**: Extrapolated from limited evidence

### Quality Scoring
Personas show quality score (1-5) based on:
- Number of interviews
- Data completeness
- Validation coverage

### Evidence Quotes
Each layer can include direct quotes from interviews with:
- Quote text
- Source attribution (role/org)
- Interview reference number

### Research Gaps
Layer 4 can highlight areas needing additional research, displayed in a highlighted warning block.

## Browser Compatibility

Works in all modern browsers:
- Chrome/Edge (v90+)
- Firefox (v88+)
- Safari (v14+)
- Opera (v76+)

No Internet Explorer support (uses modern JavaScript features).

## File Size

The complete file is approximately **40KB** (uncompressed), which includes:
- 4 complete personas
- 16 layers of content
- All styling and functionality

This makes it easy to email, share via Slack/Teams, or host on simple file servers.

## Deployment Options

### Email Attachment
Just attach `index.html` to an email. Recipients can download and open it.

### Internal Wiki/SharePoint
Upload the file to your internal documentation system. Most wikis support HTML file uploads.

### Simple Hosting
Upload to:
- GitHub Pages (create a repo, upload the file)
- Netlify Drop (drag and drop the file)
- Any web hosting with FTP access

### Offline Access
Copy the file to a USB drive or shared network folder for offline presentations.

## Updating from Data Files

If you have persona data in other formats, you can convert it:

### From Markdown
Use the Vianeo Persona Builder skill to convert markdown personas:
```bash
# Run the skill with your markdown files
vianeo-persona-builder convert --input personas/ --output dashboard-data.json
```

Then manually copy the JSON data into the `personas` and `layerContent` objects in `index.html`.

### From JSON
If you already have JSON data:
1. Open `index.html` in a text editor
2. Replace the `personas` object with your data
3. Replace the `layerContent` object with your data
4. Save and test in browser

## Troubleshooting

### Fonts Not Loading
The file uses Google Fonts (Inter). If you need it to work completely offline:
1. Download the Inter font family
2. Convert the `<link>` tags to use local font files
3. Or remove the Google Fonts link and use system fonts

### Data Not Showing
1. Open browser developer console (F12)
2. Check for JavaScript errors
3. Verify your persona IDs match between `personas` and `layerContent`
4. Check that layer IDs are referenced correctly

### Styling Issues
All styles are in the `<style>` block. You can:
- Adjust colors
- Change font sizes
- Modify spacing
- Update the layout

Look for comments in the CSS to find specific sections.

## Comparison with Other Versions

| Feature | Standalone HTML | Portable JSX | Modular React |
|---------|----------------|--------------|---------------|
| Dependencies | None | React via CDN | React + build tools |
| Setup Time | 0 seconds | ~1 minute | ~5 minutes |
| Customization | Edit HTML file | Edit JSX file | Full codebase |
| Data Loading | Embedded | Embedded | External JSON |
| Best For | Quick demos | React prototypes | Production apps |
| File Count | 1 | 1 | 10+ |

## Example Use Cases

### Client Deliverable
Package your research findings in a single file that clients can explore interactively without any technical setup.

### Stakeholder Presentation
Email the file before a meeting so stakeholders can review personas in advance. Works great on projectors.

### Internal Documentation
Upload to your wiki or shared drive as a living document of persona research.

### Offline Workshops
Load the file on laptops for workshop participants to explore without needing Wi-Fi.

### Quick Prototyping
Test out persona structure and content before building a full production dashboard.

## Credits

Built with the **Vianeo Persona Builder** skill
Part of the **360 Innovation Toolkit**

Version: 2.0
Last Updated: 2025
