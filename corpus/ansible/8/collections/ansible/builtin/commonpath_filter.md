---
collection: ansible
version: "8"
title: "ansible.builtin.commonpath filter – gets the common path"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/commonpath_filter.html
fetched_at: 2026-07-28T01:08:00+00:00
---
# ansible.builtin.commonpath filter – gets the common path

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `commonpath`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.commonpath` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

New in ansible-core 2.15

- [Synopsis](commonpath_filter.md#synopsis)
- [Input](commonpath_filter.md#input)
- [See Also](commonpath_filter.md#see-also)
- [Examples](commonpath_filter.md#examples)
- [Return Value](commonpath_filter.md#return-value)

## [Synopsis](commonpath_filter.md#id1)

- Returns the longest common path from the given list of paths.

## [Input](commonpath_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.commonpath`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=path / required | A list of paths. |

## [See Also](commonpath_filter.md#id3)

> **See also:**
>
> [ansible.builtin.basename](basename_filter.md#ansible-collections-ansible-builtin-basename-filter) filter plugin
> :   get a path’s base name.

## [Examples](commonpath_filter.md#id4)

```yaml+jinja
# To get the longest common path (ex. '/foo/bar') from the given list of paths (ex. ['/foo/bar/foobar','/foo/bar'])
{{ listofpaths | commonpath }}
```

## [Return Value](commonpath_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  path | The longest common path from the given list of paths.  **Returned:** success |

### Authors

- Shivam Durgbuns

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
