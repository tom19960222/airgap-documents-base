---
collection: ansible
version: "8"
title: "ansible.builtin.mandatory filter – make a variable’s existance mandatory"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/mandatory_filter.html
fetched_at: 2026-07-28T01:08:09+00:00
---
# ansible.builtin.mandatory filter – make a variable’s existance mandatory

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `mandatory`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.mandatory` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](mandatory_filter.md#synopsis)
- [Input](mandatory_filter.md#input)
- [Examples](mandatory_filter.md#examples)
- [Return Value](mandatory_filter.md#return-value)

## [Synopsis](mandatory_filter.md#id1)

- Depending on context undefined variables can be ignored or skipped, this ensures they force an error.

## [Input](mandatory_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.mandatory`.

| Parameter | Comments |
| --- | --- |
| **Input**  any / required | Mandatory expression. |

## [Examples](mandatory_filter.md#id3)

```yaml+jinja
# results in a Filter Error
{{ notdefined | mandatory }}
```

## [Return Value](mandatory_filter.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  any | The input if defined, otherwise an error.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
