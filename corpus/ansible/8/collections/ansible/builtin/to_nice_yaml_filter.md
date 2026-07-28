---
collection: ansible
version: "8"
title: "ansible.builtin.to_nice_yaml filter – Convert variable to YAML string"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/to_nice_yaml_filter.html
fetched_at: 2026-07-28T01:04:46+00:00
---
# ansible.builtin.to_nice_yaml filter – Convert variable to YAML string

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `to_nice_yaml`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.to_nice_yaml` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](to_nice_yaml_filter.md#synopsis)
- [Input](to_nice_yaml_filter.md#input)
- [Keyword parameters](to_nice_yaml_filter.md#keyword-parameters)
- [Notes](to_nice_yaml_filter.md#notes)
- [Examples](to_nice_yaml_filter.md#examples)
- [Return Value](to_nice_yaml_filter.md#return-value)

## [Synopsis](to_nice_yaml_filter.md#id1)

- Converts an Ansible variable into a YAML string representation.
- This filter functions as a wrapper to the [Python PyYAML library](https://pypi.org/project/PyYAML/)‘s `yaml.dump` function.
- Ansible internally auto-converts YAML strings into variable structures so this plugin is used to force it into a YAML string.

## [Input](to_nice_yaml_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.to_nice_yaml`.

| Parameter | Comments |
| --- | --- |
| **Input**  any / required | A variable or expression that returns a data structure. |

## [Keyword parameters](to_nice_yaml_filter.md#id3)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.builtin.to_nice_yaml(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **indent**  integer | Number of spaces to indent Python structures, mainly used for display to humans. |
| **sort_keys**  boolean | Affects sorting of dictionary keys.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](to_nice_yaml_filter.md#id4)

> **Note:**
>
> - More options may be available, see [PyYAML documentation](https://pyyaml.org/wiki/PyYAMLDocumentation) for details.
> - These parameters to `yaml.dump` will be ignored, as they are overridden internally: *default_flow_style*

## [Examples](to_nice_yaml_filter.md#id5)

```yaml+jinja
# dump variable in a template to create a YAML document
{{ github_workflow | to_nice_yaml }}
```

## [Return Value](to_nice_yaml_filter.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  string | The YAML serialized string representing the variable structure inputted.  **Returned:** success |

### Authors

- core team

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
