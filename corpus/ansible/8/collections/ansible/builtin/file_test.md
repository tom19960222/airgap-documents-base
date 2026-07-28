---
collection: ansible
version: "8"
title: "ansible.builtin.file test – does the path resolve to an existing file"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/file_test.html
fetched_at: 2026-07-28T01:08:48+00:00
---
# ansible.builtin.file test – does the path resolve to an existing file

> **Note:**
>
> This test plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `file`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.file` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same test plugin name.

- [Synopsis](file_test.md#synopsis)
- [Input](file_test.md#input)
- [Examples](file_test.md#examples)
- [Return Value](file_test.md#return-value)

## [Synopsis](file_test.md#id1)

- Check if the provided path maps to an existing file on the controller’s filesystem (localhost)

Aliases: is_file

## [Input](file_test.md#id2)

This describes the input of the test, the value before `is ansible.builtin.file` or `is not ansible.builtin.file`.

| Parameter | Comments |
| --- | --- |
| **Input**  path | A path. |

## [Examples](file_test.md#id3)

```yaml+jinja
vars:
  my_etc_hosts_is_a_file: "{{ '/etc/hosts' is file }}"
  list_of_files: "{{ list_of_paths | select('file') }}"
```

## [Return Value](file_test.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  boolean | Returns `True` if the path corresponds to an existing file on the filesystem on the controller, `False` if otherwise.  **Returned:** success |

### Authors

- Ansible Core

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
