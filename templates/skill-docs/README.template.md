# {{ skill.name }}

{{ skill.description }}

{% if skill.badges %}
{% for badge in skill.badges %}
![{{ badge.label }}]({{ badge.url }}){% if not loop.last %} {% endif %}

{% endfor %}
{% endif %}

## Quick Links

- [Quick Start](./QUICK-START.md) - Get started in 5 minutes
- [Full Documentation](./SKILL.md) - Complete operational logic
{% if skill.has_implementation_guide %}
- [Implementation Guide](./IMPLEMENTATION-GUIDE.md) - Setup and deployment
{% endif %}
{% if skill.has_examples %}
- [Examples](./EXAMPLES.md) - Real-world usage examples
{% endif %}

## When to Use This Skill

{% if skill.use_cases %}
{% for use_case in skill.use_cases %}
- {{ use_case }}
{% endfor %}
{% else %}
Use this skill when you need to {{ skill.primary_action }}.
{% endif %}

## Features

{% for feature in skill.features %}
- **{{ feature.name }}**: {{ feature.description }}
{% endfor %}

## Prerequisites

{% if skill.prerequisites %}
{% for prereq in skill.prerequisites %}
- {{ prereq }}
{% endfor %}
{% else %}
No special prerequisites required.
{% endif %}

## Basic Usage

{% if skill.basic_usage %}
{{ skill.basic_usage }}
{% else %}
```
{{ skill.trigger_phrase }}
```
{% endif %}

## Output Formats

{% if skill.outputs %}
| Format | Description |
|--------|-------------|
{% for output in skill.outputs %}
| {{ output.format }} | {{ output.description }} |
{% endfor %}
{% endif %}

## Integration Points

{% if skill.integrations %}
{% for integration in skill.integrations %}
- **{{ integration.name }}**: {{ integration.description }}
{% endfor %}
{% endif %}

## Related Skills

{% if skill.related_skills %}
{% for related in skill.related_skills %}
- [{{ related.name }}]({{ related.link }}) - {{ related.description }}
{% endfor %}
{% endif %}

---

**Version**: {{ skill.version }}
**Category**: {{ skill.category }}
**Author**: {{ skill.author | default('360 Social Impact Studios') }}
**Last Updated**: {{ skill.last_updated | default('2024') }}
