---
collection: ansible
version: "8"
title: "ansible.builtin.nan test – is this not a number (NaN)"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/nan_test.html
fetched_at: 2026-07-28T01:08:52+00:00
---
# ansible.builtin.nan test – is this not a number (NaN)

> **Note:**
>
> This test plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `nan`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.nan` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same test plugin name.

- [Synopsis](nan_test.md#synopsis)
- [Input](nan_test.md#input)
- [Examples](nan_test.md#examples)
- [Return Value](nan_test.md#return-value)

## [Synopsis](nan_test.md#id1)

- Whether the input is a special floating point number called [not a number](https://en.wikipedia.org/wiki/NaN).

Aliases: is_file, isnan

## [Input](nan_test.md#id2)

This describes the input of the test, the value before `is ansible.builtin.nan` or `is not ansible.builtin.nan`.

| Parameter | Comments |
| --- | --- |
| **Input**  any / required | Possible number representation or string that can be converted into one. |

## [Examples](nan_test.md#id3)

```yaml+jinja
isnan: "{{ '42' is nan }}"
```

## [Return Value](nan_test.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  boolean | Returns `True` if the input is NaN, `False` if otherwise.  **Returned:** success |

### Authors

- Ansible Core

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
