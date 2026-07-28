---
collection: ansible
version: "8"
title: "ansible.builtin.exists test – does the path exist, follow symlinks"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/exists_test.html
fetched_at: 2026-07-28T01:08:46+00:00
---
# ansible.builtin.exists test – does the path exist, follow symlinks

> **Note:**
>
> This test plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `exists`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.exists` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same test plugin name.

- [Synopsis](exists_test.md#synopsis)
- [Input](exists_test.md#input)
- [Examples](exists_test.md#examples)
- [Return Value](exists_test.md#return-value)

## [Synopsis](exists_test.md#id1)

- Check if the provided path maps to an existing filesystem object on the controller (localhost).
- Follows symlinks and checks the target of the symlink instead of the link itself, use the `link` or `link_exists` tests to check on the link.

## [Input](exists_test.md#id2)

This describes the input of the test, the value before `is ansible.builtin.exists` or `is not ansible.builtin.exists`.

| Parameter | Comments |
| --- | --- |
| **Input**  path | a path |

## [Examples](exists_test.md#id3)

```yaml+jinja
vars:
  my_etc_hosts_exists: "{{ '/etc/hosts' is exist }}"
  list_of_local_files_to_copy_to_remote: "{{ list_of_all_possible_files | select('exists') }}"
```

## [Return Value](exists_test.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  boolean | Returns `True` if the path corresponds to an existing filesystem object on the controller (after following symlinks), `False` if otherwise.  **Returned:** success |

### Authors

- Ansible Core

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
