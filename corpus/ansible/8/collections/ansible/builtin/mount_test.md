---
collection: ansible
version: "8"
title: "ansible.builtin.mount test – does the path resolve to mount point"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/mount_test.html
fetched_at: 2026-07-28T01:08:52+00:00
---
# ansible.builtin.mount test – does the path resolve to mount point

> **Note:**
>
> This test plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `mount`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.mount` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same test plugin name.

- [Synopsis](mount_test.md#synopsis)
- [Input](mount_test.md#input)
- [Examples](mount_test.md#examples)
- [Return Value](mount_test.md#return-value)

## [Synopsis](mount_test.md#id1)

- Check if the provided path maps to a filesystem mount point on the controller (localhost).

Aliases: is_mount

## [Input](mount_test.md#id2)

This describes the input of the test, the value before `is ansible.builtin.mount` or `is not ansible.builtin.mount`.

| Parameter | Comments |
| --- | --- |
| **Input**  path | A path. |

## [Examples](mount_test.md#id3)

```yaml+jinja
vars:
  ihopefalse: "{{ '/etc/hosts' is mount }}"
  normallytrue: "{{ '/tmp' is mount }}"
```

## [Return Value](mount_test.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  boolean | Returns `True` if the path corresponds to a mount point on the controller, `False` if otherwise.  **Returned:** success |

### Authors

- Ansible Core

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
