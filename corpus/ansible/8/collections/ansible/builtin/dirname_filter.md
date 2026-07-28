---
collection: ansible
version: "8"
title: "ansible.builtin.dirname filter – get a path’s directory name"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/dirname_filter.html
fetched_at: 2026-07-28T01:08:01+00:00
---
# ansible.builtin.dirname filter – get a path’s directory name

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `dirname`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.dirname` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](dirname_filter.md#synopsis)
- [Input](dirname_filter.md#input)
- [Notes](dirname_filter.md#notes)
- [See Also](dirname_filter.md#see-also)
- [Examples](dirname_filter.md#examples)
- [Return Value](dirname_filter.md#return-value)

## [Synopsis](dirname_filter.md#id1)

- Returns the ‘head’ component of a path, basically everything that is not the ‘basename’.

## [Input](dirname_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.dirname`.

| Parameter | Comments |
| --- | --- |
| **Input**  path / required | A path. |

## [Notes](dirname_filter.md#id3)

> **Note:**
>
> - The result of this filter is different from the Unix dirname program; where dirname for `/foo/bar/` returns `/foo`, the dirname filter returns the full path (`/foo/bar/`).

## [See Also](dirname_filter.md#id4)

> **See also:**
>
> [ansible.builtin.basename](basename_filter.md#ansible-collections-ansible-builtin-basename-filter) filter plugin
> :   get a path’s base name.

## [Examples](dirname_filter.md#id5)

```yaml+jinja
# To get the dir name of a file path, like '/etc/asdf' out of '/etc/asdf/foo.txt'.
{{ mypath | dirname }}
```

## [Return Value](dirname_filter.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  path | The directory portion of the original path.  **Returned:** success |

### Authors

- ansible core team

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
