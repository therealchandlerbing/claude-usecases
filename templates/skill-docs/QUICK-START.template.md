# {{ skill.name }} - Quick Start

Get started with {{ skill.name }} in under 5 minutes.

## TL;DR

```
{{ skill.trigger_phrase }}
```

## Prerequisites Checklist

{% for prereq in skill.prerequisites %}
- [ ] {{ prereq }}
{% endfor %}
{% if not skill.prerequisites %}
- [ ] No special prerequisites
{% endif %}

## Quick Decision Tree

```
{{ skill.decision_tree | default('Start → Provide Input → Execute → Review Output') }}
```

## Minimal Example

{% if skill.minimal_example %}
{{ skill.minimal_example }}
{% else %}
1. Trigger the skill with: "{{ skill.trigger_phrase }}"
2. Provide the required input data
3. Review and validate the output
{% endif %}

## Common Workflows

{% for workflow in skill.common_workflows %}
### {{ workflow.name }}

{{ workflow.description }}

{% for step in workflow.steps %}
{{ loop.index }}. {{ step }}
{% endfor %}

{% endfor %}

## Quick Reference

| Action | Command/Trigger |
|--------|-----------------|
{% for action in skill.quick_actions %}
| {{ action.name }} | {{ action.trigger }} |
{% endfor %}

## Troubleshooting Quick Fixes

{% for fix in skill.quick_fixes %}
| Issue | Fix |
|-------|-----|
| {{ fix.issue }} | {{ fix.solution }} |
{% endfor %}

## Next Steps

- Read the [full documentation](./SKILL.md)
{% if skill.has_implementation_guide %}
- Review the [implementation guide](./IMPLEMENTATION-GUIDE.md)
{% endif %}
{% if skill.has_examples %}
- Explore [more examples](./EXAMPLES.md)
{% endif %}

---

*Quick Start Guide v1.0*
