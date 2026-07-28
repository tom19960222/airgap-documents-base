---
collection: ansible
version: "8"
title: "ansible.builtin.bool filter – cast into a boolean"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/bool_filter.html
fetched_at: 2026-07-28T01:07:58+00:00
---
# ansible.builtin.bool filter – cast into a boolean

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `bool`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.bool` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](bool_filter.md#synopsis)
- [Input](bool_filter.md#input)
- [Examples](bool_filter.md#examples)
- [Return Value](bool_filter.md#return-value)

## [Synopsis](bool_filter.md#id1)

- Attempt to cast the input into a boolean (`True` or `False`) value.

Aliases: formerly_core_filter, formerly_core_masked_filter

## [Input](bool_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.bool`.

| Parameter | Comments |
| --- | --- |
| **Input**  any / required | Data to cast. |

## [Examples](bool_filter.md#id3)

```yaml+jinja
# simply encrypt my key in a vault
vars:
  isbool: "{{ (a == b)|bool }} "
  otherbool: "{{ anothervar|bool }} "

# in a task
...
when: some_string_value | bool
```

## [Return Value](bool_filter.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  boolean | The boolean resulting of casting the input expression into a `True` or `False` value.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
