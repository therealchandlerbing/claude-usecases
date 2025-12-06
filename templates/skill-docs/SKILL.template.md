---
name: {{ skill.name }}
version: {{ skill.version }}
description: {{ skill.description }}
author: {{ skill.author | default('360 Social Impact Studios') }}
created: {{ skill.created | default('2024-01-01') }}
category: {{ skill.category }}
{% if skill.tags %}
tags:
{% for tag in skill.tags %}
  - {{ tag }}
{% endfor %}
{% endif %}
---

# {{ skill.name }}

{{ skill.description }}

## Overview

{{ skill.overview | default(skill.description) }}

## Trigger Conditions

This skill activates when:
{% for trigger in skill.triggers %}
- {{ trigger }}
{% endfor %}

## Workflow Phases

{% for phase in skill.phases %}
### Phase {{ loop.index }}: {{ phase.name }}

{{ phase.description }}

{% if phase.inputs %}
**Inputs:**
{% for input in phase.inputs %}
- `{{ input.name }}`: {{ input.description }}{% if input.required %} (required){% endif %}

{% endfor %}
{% endif %}

{% if phase.steps %}
**Steps:**
{% for step in phase.steps %}
{{ loop.index }}. {{ step }}
{% endfor %}
{% endif %}

{% if phase.outputs %}
**Outputs:**
{% for output in phase.outputs %}
- `{{ output.name }}`: {{ output.description }}
{% endfor %}
{% endif %}

{% endfor %}

## Configuration

{% if skill.config_options %}
| Option | Type | Default | Description |
|--------|------|---------|-------------|
{% for opt in skill.config_options %}
| `{{ opt.name }}` | {{ opt.type }} | {{ opt.default | default('-') }} | {{ opt.description }} |
{% endfor %}
{% endif %}

## Quality Criteria

{% if skill.quality_criteria %}
{% for criterion in skill.quality_criteria %}
- [ ] {{ criterion }}
{% endfor %}
{% else %}
- [ ] Output is accurate and complete
- [ ] Follows established patterns
- [ ] Includes proper error handling
{% endif %}

## Error Handling

{% if skill.error_handling %}
{% for error in skill.error_handling %}
### {{ error.type }}

{{ error.description }}

**Resolution**: {{ error.resolution }}

{% endfor %}
{% else %}
If errors occur during execution:
1. Check input data validity
2. Verify prerequisites are met
3. Review configuration settings
4. Consult troubleshooting section
{% endif %}

## Examples

{% if skill.examples %}
{% for example in skill.examples %}
### Example {{ loop.index }}: {{ example.title }}

{{ example.description }}

{% if example.input %}
**Input:**
```{{ example.input_format | default('json') }}
{{ example.input }}
```
{% endif %}

{% if example.output %}
**Output:**
```{{ example.output_format | default('json') }}
{{ example.output }}
```
{% endif %}

{% endfor %}
{% endif %}

## Troubleshooting

{% if skill.troubleshooting %}
{% for issue in skill.troubleshooting %}
### {{ issue.problem }}

{{ issue.solution }}

{% endfor %}
{% else %}
### Common Issues

1. **Missing prerequisites**: Ensure all required data is available
2. **Configuration errors**: Verify configuration file syntax
3. **Integration failures**: Check API credentials and connectivity
{% endif %}

---

*Generated from skill template v1.0*
