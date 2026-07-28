---
collection: ansible
version: "8"
title: "ansible.builtin.win_basename filter – Get a Windows path’s base name"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/win_basename_filter.html
fetched_at: 2026-07-28T01:08:24+00:00
---
# ansible.builtin.win_basename filter – Get a Windows path’s base name

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `win_basename`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.win_basename` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](win_basename_filter.md#synopsis)
- [Input](win_basename_filter.md#input)
- [See Also](win_basename_filter.md#see-also)
- [Examples](win_basename_filter.md#examples)
- [Return Value](win_basename_filter.md#return-value)

## [Synopsis](win_basename_filter.md#id1)

- Returns the last name component of a Windows path, what is left in the string that is not ‘win_dirname’.

## [Input](win_basename_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.win_basename`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | A Windows path. |

## [See Also](win_basename_filter.md#id3)

> **See also:**
>
> [ansible.builtin.win_dirname](win_dirname_filter.md#ansible-collections-ansible-builtin-win-dirname-filter) filter plugin
> :   Get a Windows path’s directory.

## [Examples](win_basename_filter.md#id4)

```yaml+jinja
# To get the last name of a file Windows path, like 'foo.txt' out of 'C:\Users\asdf\foo.txt'
{{ mypath | win_basename }}
```

## [Return Value](win_basename_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  string | The base name from the Windows path provided.  **Returned:** success |

### Authors

- ansible core team

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
