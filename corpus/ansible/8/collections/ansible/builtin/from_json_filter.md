---
collection: ansible
version: "8"
title: "ansible.builtin.from_json filter – Convert JSON string into variable structure"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/from_json_filter.html
fetched_at: 2026-07-28T01:08:05+00:00
---
# ansible.builtin.from_json filter – Convert JSON string into variable structure

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `from_json`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.from_json` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](from_json_filter.md#synopsis)
- [Input](from_json_filter.md#input)
- [Notes](from_json_filter.md#notes)
- [Examples](from_json_filter.md#examples)
- [Return Value](from_json_filter.md#return-value)

## [Synopsis](from_json_filter.md#id1)

- Converts a JSON string representation into an equivalent structured Ansible variable.
- Ansible automatically converts JSON strings into variable structures in most contexts, use this plugin in contexts where automatic conversion does not happen.

## [Input](from_json_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.from_json`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | A JSON string. |

## [Notes](from_json_filter.md#id3)

> **Note:**
>
> - This filter functions as a wrapper to the Python `json.loads` function.

## [Examples](from_json_filter.md#id4)

```yaml+jinja
# variable from string variable containing a JSON document
{{ docker_config | from_json }}

# variable from string JSON document
{{ '{"a": true, "b": 54, "c": [1,2,3]}' | from_json }}
```

## [Return Value](from_json_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  any | The variable resulting from deserialization of the JSON document.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
