---
collection: ansible
version: "8"
title: "ansible.builtin.from_yaml_all filter – Convert a series of YAML documents into a variable structure"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/from_yaml_all_filter.html
fetched_at: 2026-07-28T01:04:47+00:00
---
# ansible.builtin.from_yaml_all filter – Convert a series of YAML documents into a variable structure

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `from_yaml_all`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.from_yaml_all` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](from_yaml_all_filter.md#synopsis)
- [Input](from_yaml_all_filter.md#input)
- [Notes](from_yaml_all_filter.md#notes)
- [Examples](from_yaml_all_filter.md#examples)
- [Return Value](from_yaml_all_filter.md#return-value)

## [Synopsis](from_yaml_all_filter.md#id1)

- Converts a YAML documents in a string representation into an equivalent structured Ansible variable.
- Ansible internally auto-converts YAML strings into variable structures in most contexts, but by default does not handle ‘multi document’ YAML files or strings.
- If multiple YAML documents are not supplied, this is the equivalend of using `from_yaml`.

## [Input](from_yaml_all_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.from_yaml_all`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | A YAML string. |

## [Notes](from_yaml_all_filter.md#id3)

> **Note:**
>
> - This filter functions as a wrapper to the Python `yaml.safe_load_all` function, part of the [pyyaml Python library](https://pypi.org/project/PyYAML/).
> - Possible conflicts in variable names from the mulitple documents are resolved directly by the pyyaml library.

## [Examples](from_yaml_all_filter.md#id4)

```yaml+jinja
# variable from string variable containing YAML documents
{{ multidoc_yaml_string | from_yaml_all }}

# variable from multidocument YAML string
{{ '---\n{"a": true, "b": 54, "c": [1,2,3]}\n...\n---{"x": 1}\n...\n' | from_yaml_all}}
```

## [Return Value](from_yaml_all_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  any | The variable resulting from deserializing the YAML documents.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
