---
collection: ansible
version: "8"
title: "ansible.builtin.fileglob filter – explode a path glob to matching files"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/fileglob_filter.html
fetched_at: 2026-07-28T01:08:04+00:00
---
# ansible.builtin.fileglob filter – explode a path glob to matching files

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `fileglob`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.fileglob` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](fileglob_filter.md#synopsis)
- [Input](fileglob_filter.md#input)
- [Examples](fileglob_filter.md#examples)
- [Return Value](fileglob_filter.md#return-value)

## [Synopsis](fileglob_filter.md#id1)

- Return a list of files that matches the supplied path glob pattern.
- Filters run on the controller, so the files are matched from the controller’s file system.

## [Input](fileglob_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.fileglob`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | Path glob pattern. |

## [Examples](fileglob_filter.md#id3)

```yaml+jinja
# found = ['/etc/hosts', '/etc/hasts']
found: "{{ '/etc/h?sts' | fileglob }}"
```

## [Return Value](fileglob_filter.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | List of files matched.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
