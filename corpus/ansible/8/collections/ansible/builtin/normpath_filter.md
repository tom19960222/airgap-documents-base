---
collection: ansible
version: "8"
title: "ansible.builtin.normpath filter – Normalize a pathname"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/normpath_filter.html
fetched_at: 2026-07-28T01:08:11+00:00
---
# ansible.builtin.normpath filter – Normalize a pathname

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `normpath`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.normpath` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

New in ansible-core 2.15

- [Synopsis](normpath_filter.md#synopsis)
- [Input](normpath_filter.md#input)
- [See Also](normpath_filter.md#see-also)
- [Examples](normpath_filter.md#examples)
- [Return Value](normpath_filter.md#return-value)

## [Synopsis](normpath_filter.md#id1)

- Returns the normalized pathname by collapsing redundant separators and up-level references.

## [Input](normpath_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.normpath`.

| Parameter | Comments |
| --- | --- |
| **Input**  path / required | A path. |

## [See Also](normpath_filter.md#id3)

> **See also:**
>
> [ansible.builtin.basename](basename_filter.md#ansible-collections-ansible-builtin-basename-filter) filter plugin
> :   get a path’s base name.

## [Examples](normpath_filter.md#id4)

```yaml+jinja
# To get a normalized path (ex. '/foo/bar') from the path (ex. '/foo//bar')
{{ path | normpath }}
```

## [Return Value](normpath_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  path | The normalized path from the path given.  **Returned:** success |

### Authors

- Shivam Durgbuns

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
