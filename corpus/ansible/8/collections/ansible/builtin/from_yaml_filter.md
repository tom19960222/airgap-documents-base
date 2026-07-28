---
collection: ansible
version: "8"
title: "ansible.builtin.from_yaml filter – Convert YAML string into variable structure"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/from_yaml_filter.html
fetched_at: 2026-07-28T01:08:06+00:00
---
# ansible.builtin.from_yaml filter – Convert YAML string into variable structure

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `from_yaml`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.from_yaml` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](from_yaml_filter.md#synopsis)
- [Input](from_yaml_filter.md#input)
- [Notes](from_yaml_filter.md#notes)
- [Examples](from_yaml_filter.md#examples)
- [Return Value](from_yaml_filter.md#return-value)

## [Synopsis](from_yaml_filter.md#id1)

- Converts a YAML string representation into an equivalent structured Ansible variable.
- Ansible automatically converts YAML strings into variable structures in most contexts, use this plugin in contexts where automatic conversion does not happen.

## [Input](from_yaml_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.from_yaml`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | A YAML string. |

## [Notes](from_yaml_filter.md#id3)

> **Note:**
>
> - This filter functions as a wrapper to the [Python pyyaml library](https://pypi.org/project/PyYAML/)‘s `yaml.safe_load` function.

## [Examples](from_yaml_filter.md#id4)

```yaml+jinja
# variable from string variable containing a YAML document
{{ github_workflow | from_yaml}}

# variable from string JSON document
{{ '{"a": true, "b": 54, "c": [1,2,3]}' | from_yaml }}
```

## [Return Value](from_yaml_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  any | The variable resulting from deserializing the YAML document.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
