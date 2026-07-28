---
collection: ansible
version: "8"
title: "ansible.builtin.expanduser filter – Returns a path with ~ translation."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/expanduser_filter.html
fetched_at: 2026-07-28T01:08:02+00:00
---
# ansible.builtin.expanduser filter – Returns a path with `~` translation.

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `expanduser`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.expanduser` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](expanduser_filter.md#synopsis)
- [Input](expanduser_filter.md#input)
- [Examples](expanduser_filter.md#examples)
- [Return Value](expanduser_filter.md#return-value)

## [Synopsis](expanduser_filter.md#id1)

- Translates `~` in a path to the proper user’s home directory.

## [Input](expanduser_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.expanduser`.

| Parameter | Comments |
| --- | --- |
| **Input**  path / required | A string that contains a path. |

## [Examples](expanduser_filter.md#id3)

```yaml+jinja
# To get '/home/myuser/stuff.txt' from '~/stuff.txt'.
{{ mypath | expanduser }}
```

## [Return Value](expanduser_filter.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  path | The translated path.  **Returned:** success |

### Authors

- ansible core team

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
