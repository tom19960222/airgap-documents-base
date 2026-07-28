---
collection: ansible
version: "8"
title: "ansible.builtin.type_debug filter – show input data type"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/type_debug_filter.html
fetched_at: 2026-07-28T01:04:42+00:00
---
# ansible.builtin.type_debug filter – show input data type

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `type_debug`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.type_debug` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](type_debug_filter.md#synopsis)
- [Input](type_debug_filter.md#input)
- [Examples](type_debug_filter.md#examples)
- [Return Value](type_debug_filter.md#return-value)

## [Synopsis](type_debug_filter.md#id1)

- Returns the equivalent of Python’s `type` function.

## [Input](type_debug_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.type_debug`.

| Parameter | Comments |
| --- | --- |
| **Input**  any / required | Variable or expression of which you want to determine type. |

## [Examples](type_debug_filter.md#id3)

```yaml+jinja
# get type of 'myvar'
{{ myvar | type_debug }}
```

## [Return Value](type_debug_filter.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  string | The Python ‘type’ of the *_input* provided.  **Returned:** success |

### Authors

- Adrian Likins (@alikins)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
