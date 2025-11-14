# Vianeo Persona Builder - Powerups

This directory contains optional powerups and add-ons for the Vianeo Persona Builder skill. Powerups extend the core functionality with additional features, visualizations, and integrations.

## What are Powerups?

Powerups are optional enhancements that complement the core Vianeo Persona Builder skill. They are:

- **Optional** - Use them when you need specific functionality
- **Modular** - Each powerup is self-contained
- **Compatible** - Designed to work with persona builder output
- **Extensible** - Easy to customize and modify

## Available Powerups

### Interactive Dashboard v2.0

**Location:** `interactive-dashboard/`
**Status:** ✅ Production Ready
**Version:** 2.0.0

An interactive web-based dashboard for exploring Vianeo persona data with beautiful UI, evidence tracking, and validation indicators. Now available in three implementation options to suit any deployment scenario.

**Three Implementation Options:**

1. **Standalone HTML (Easiest)** - Zero dependencies, ~40KB file, just open in browser
2. **Portable JSX** - Single-file React component with embedded data
3. **Modular TypeScript** - Production component architecture with type safety

**Key Features (v2.0):**
- ⭐ **NEW:** Standalone HTML version with zero dependencies
- ⭐ **NEW:** Field-level validation tracking (✓ Validated, ◐ Partial, ⚠ Inferred)
- ⭐ **NEW:** Quality scores and interview counts displayed
- ⭐ **NEW:** Layer 4 research gaps visualization
- Interactive navigation through personas and layers
- Evidence quotes with source attribution
- Responsive, accessible design (WCAG 2.1 AA)
- Easy customization and branding

**When to Use:**
- Presenting personas to stakeholders
- Email attachments and offline sharing
- Team collaboration and exploration
- Building a persona reference library
- Demonstrating validation depth
- Client deliverables

**Quick Start:**

**Option 1 - Standalone HTML (No dependencies):**
```bash
cd interactive-dashboard/examples/standalone-html/
# Just double-click index.html to open in browser
```

**Option 2 - Portable JSX (React component):**
```bash
# Copy the single file to your project
cp examples/portable-version/VianeoPersonaExplorer.jsx your-project/
```

**Option 3 - Modular TypeScript (Production):**
```bash
cd interactive-dashboard
npm install
```

See [Interactive Dashboard v2.0 README](interactive-dashboard/README.md) for full documentation, customization guide, and deployment options.

---

## Future Powerups

Planned powerups for future releases:

### Persona Comparison Tool
**Status:** 🔄 Planned

Side-by-side comparison of multiple personas with gap analysis.

### Export to Figma
**Status:** 🔄 Planned

Convert personas to Figma frames for design collaboration.

### Journey Mapping Overlay
**Status:** 🔄 Planned

Map personas to customer journey stages with touchpoint analysis.

### API Integration
**Status:** 🔄 Planned

REST API for programmatic access to persona data.

---

## Using Powerups

### Installation

Each powerup has its own installation instructions. Generally:

1. Navigate to the powerup directory
2. Follow the README installation steps
3. Import/use as documented

### Integration with Persona Builder

All powerups are designed to work with output from the Vianeo Persona Builder skill:

1. Generate personas using the main skill
2. Convert output to powerup format (if needed)
3. Load data into the powerup
4. Use enhanced features

### Customization

Powerups are designed to be customizable:

- Modify styling and branding
- Add custom features
- Integrate with your tools
- Extend functionality

---

## Contributing Powerups

Want to create a powerup? Follow these guidelines:

### Structure

```
your-powerup/
├── README.md           # Documentation
├── package.json        # Dependencies (if applicable)
├── src/               # Source code
├── examples/          # Usage examples
└── tests/             # Tests (optional)
```

### Requirements

- **Documentation** - Clear README with installation and usage
- **Examples** - Working examples with sample data
- **Compatibility** - Works with persona builder output
- **Quality** - Well-tested and production-ready

### Submission Process

1. Create your powerup in a new directory
2. Include comprehensive documentation
3. Add examples and test data
4. Update this README with your powerup
5. Submit a pull request

---

## Support

For powerup-related questions:

1. Check the powerup's README
2. Review the examples
3. Consult the main [Vianeo Persona Builder documentation](../README.md)
4. Open an issue on GitHub

---

## Version Compatibility

| Powerup | Persona Builder Version | Status |
|---------|------------------------|--------|
| Interactive Dashboard 2.0 | 1.0+ | ✅ Compatible |
| Interactive Dashboard 1.0 | 1.0+ | ⚠️ Deprecated (use v2.0) |

---

## License

All powerups follow the same license as the main Vianeo Persona Builder skill.

---

**Created for the Vianeo Persona Builder**
**Part of the 360 Innovation Toolkit**
