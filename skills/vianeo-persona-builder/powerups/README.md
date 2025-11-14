# Vianeo Persona Builder - Powerups

This directory contains optional powerups and add-ons for the Vianeo Persona Builder skill. Powerups extend the core functionality with additional features, visualizations, and integrations.

## What are Powerups?

Powerups are optional enhancements that complement the core Vianeo Persona Builder skill. They are:

- **Optional** - Use them when you need specific functionality
- **Modular** - Each powerup is self-contained
- **Compatible** - Designed to work with persona builder output
- **Extensible** - Easy to customize and modify

## Available Powerups

### Interactive Dashboard

**Location:** `interactive-dashboard/`
**Status:** ✅ Available
**Version:** 1.0.0

An interactive React-based dashboard for exploring Vianeo persona data with beautiful UI, evidence tracking, and validation indicators.

**Key Features:**
- Interactive navigation through personas and layers
- Visual validation status indicators
- Evidence quotes and source attribution
- Responsive, accessible design
- TypeScript support

**When to Use:**
- Presenting personas to stakeholders
- Team collaboration and exploration
- Building a persona reference library
- Demonstrating validation depth

**Quick Start:**
```bash
cd interactive-dashboard
npm install
```

See [Interactive Dashboard README](interactive-dashboard/README.md) for full documentation.

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
| Interactive Dashboard 1.0 | 1.0+ | ✅ Compatible |

---

## License

All powerups follow the same license as the main Vianeo Persona Builder skill.

---

**Created for the Vianeo Persona Builder**
**Part of the 360 Innovation Toolkit**
