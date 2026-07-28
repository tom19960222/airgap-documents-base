---
collection: ansible
version: "8"
title: "ansible.windows.win_owner module – Set owner"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/windows/win_owner_module.html
fetched_at: 2026-07-28T01:10:41+00:00
---
# ansible.windows.win_owner module – Set owner

> **Note:**
>
> This module is part of the [ansible.windows collection](https://galaxy.ansible.com/ui/repo/published/ansible/windows/) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.windows`.
>
> To use it in a playbook, specify: `ansible.windows.win_owner`.

- [Synopsis](win_owner_module.md#synopsis)
- [Parameters](win_owner_module.md#parameters)
- [See Also](win_owner_module.md#see-also)
- [Examples](win_owner_module.md#examples)

## [Synopsis](win_owner_module.md#id1)

- Set owner of files or directories.

## [Parameters](win_owner_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **path**  path / required | Path to be used for changing owner. |
| **recurse**  boolean | Indicates if the owner should be changed recursively.  **Choices:**   - `false` ← (default) - `true` |
| **user**  string / required | Name to be used for changing owner. |

## [See Also](win_owner_module.md#id3)

> **See also:**
>
> [ansible.windows.win_acl](win_acl_module.md#ansible-collections-ansible-windows-win-acl-module)
> :   Set file/directory/registry permissions for a system user or group.
>
> [ansible.windows.win_file](win_file_module.md#ansible-collections-ansible-windows-win-file-module)
> :   Creates, touches or removes files or directories.
>
> [ansible.windows.win_stat](win_stat_module.md#ansible-collections-ansible-windows-win-stat-module)
> :   Get information about Windows files.

## [Examples](win_owner_module.md#id4)

```yaml+jinja
- name: Change owner of path
  ansible.windows.win_owner:
    path: C:\apache
    user: apache
    recurse: true

- name: Set the owner of root directory
  ansible.windows.win_owner:
    path: C:\apache
    user: SYSTEM
    recurse: false
```

### Authors

- Hans-Joachim Kliemeck (@h0nIg)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
- [Communication](index.md#communication-for-ansible-windows)
