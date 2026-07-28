---
collection: ansible
version: "8"
title: "ansible.builtin.realpath filter – Turn path into real path"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/realpath_filter.html
fetched_at: 2026-07-28T01:08:14+00:00
---
# ansible.builtin.realpath filter – Turn path into real path

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `realpath`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.realpath` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](realpath_filter.md#synopsis)
- [Input](realpath_filter.md#input)
- [Examples](realpath_filter.md#examples)
- [Return Value](realpath_filter.md#return-value)

## [Synopsis](realpath_filter.md#id1)

- Resolves/follows symliknks to return the ‘real path’ from a given path.
- Filters alwasy run on controller so this path is resolved using the controller’s filesystem.

## [Input](realpath_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.realpath`.

| Parameter | Comments |
| --- | --- |
| **Input**  path / required | A path. |

## [Examples](realpath_filter.md#id3)

```yaml+jinja
realpath: {{ '/path/to/synlink' | realpath }}
```

## [Return Value](realpath_filter.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  path | The canonical path.  **Returned:** success |

### Authors

- darkone23 (@darkone23)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
