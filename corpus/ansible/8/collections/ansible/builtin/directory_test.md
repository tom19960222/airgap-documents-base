---
collection: ansible
version: "8"
title: "ansible.builtin.directory test – does the path resolve to an existing directory"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/directory_test.html
fetched_at: 2026-07-28T01:08:46+00:00
---
# ansible.builtin.directory test – does the path resolve to an existing directory

> **Note:**
>
> This test plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `directory`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.directory` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same test plugin name.

- [Synopsis](directory_test.md#synopsis)
- [Input](directory_test.md#input)
- [Examples](directory_test.md#examples)
- [Return Value](directory_test.md#return-value)

## [Synopsis](directory_test.md#id1)

- Check if the provided path maps to an existing directory on the controller’s filesystem (localhost).

Aliases: is_dir

## [Input](directory_test.md#id2)

This describes the input of the test, the value before `is ansible.builtin.directory` or `is not ansible.builtin.directory`.

| Parameter | Comments |
| --- | --- |
| **Input**  path | A path. |

## [Examples](directory_test.md#id3)

```yaml+jinja
vars:
  my_etc_hosts_not_a_dir: "{{ '/etc/hosts' is directory}}"
  list_of_files: "{{ list_of_paths | reject('directory') }}"
```

## [Return Value](directory_test.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  boolean | Returns `True` if the path corresponds to an existing directory on the filesystem on the controller, c(False) if otherwise.  **Returned:** success |

### Authors

- Ansible Core

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
