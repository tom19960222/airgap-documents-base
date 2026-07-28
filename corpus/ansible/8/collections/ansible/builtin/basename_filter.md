---
collection: ansible
version: "8"
title: "ansible.builtin.basename filter – get a path’s base name"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/basename_filter.html
fetched_at: 2026-07-28T01:07:57+00:00
---
# ansible.builtin.basename filter – get a path’s base name

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `basename`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.basename` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](basename_filter.md#synopsis)
- [Input](basename_filter.md#input)
- [Notes](basename_filter.md#notes)
- [See Also](basename_filter.md#see-also)
- [Examples](basename_filter.md#examples)
- [Return Value](basename_filter.md#return-value)

## [Synopsis](basename_filter.md#id1)

- Returns the last name component of a path, what is left in the string that is not ‘dirname’.

## [Input](basename_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.basename`.

| Parameter | Comments |
| --- | --- |
| **Input**  path / required | A path. |

## [Notes](basename_filter.md#id3)

> **Note:**
>
> - The result of this filter is different from the Unix basename program; where basename for `/foo/bar/` returns `bar`, the basename filter returns an empty string (`''`).

## [See Also](basename_filter.md#id4)

> **See also:**
>
> [ansible.builtin.dirname](dirname_filter.md#ansible-collections-ansible-builtin-dirname-filter) filter plugin
> :   get a path’s directory name.

## [Examples](basename_filter.md#id5)

```yaml+jinja
# To get the last name of a file path, like 'foo.txt' out of '/etc/asdf/foo.txt'.
{{ mypath | basename }}
```

## [Return Value](basename_filter.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  string | The base name from the path provided.  **Returned:** success |

### Authors

- ansible core team

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
