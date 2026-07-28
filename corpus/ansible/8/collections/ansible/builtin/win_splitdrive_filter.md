---
collection: ansible
version: "8"
title: "ansible.builtin.win_splitdrive filter – Split a Windows path by the drive letter"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/win_splitdrive_filter.html
fetched_at: 2026-07-28T01:08:25+00:00
---
# ansible.builtin.win_splitdrive filter – Split a Windows path by the drive letter

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `win_splitdrive`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.win_splitdrive` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](win_splitdrive_filter.md#synopsis)
- [Input](win_splitdrive_filter.md#input)
- [Examples](win_splitdrive_filter.md#examples)
- [Return Value](win_splitdrive_filter.md#return-value)

## [Synopsis](win_splitdrive_filter.md#id1)

- Returns a list with the first component being the drive letter and the second, the rest of the path.

## [Input](win_splitdrive_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.win_splitdrive`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | A Windows path. |

## [Examples](win_splitdrive_filter.md#id3)

```yaml+jinja
# To get the last name of a file Windows path, like ['C', '\Users\asdf\foo.txt'] out of 'C:\Users\asdf\foo.txt'
{{ mypath | win_splitdrive }}

# just the drive letter
{{ mypath | win_splitdrive | first }}

# path w/o drive letter
{{ mypath | win_splitdrive | last }}
```

## [Return Value](win_splitdrive_filter.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | List in which the first element is the drive letter and the second the rest of the path.  **Returned:** success |

### Authors

- ansible core team

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
