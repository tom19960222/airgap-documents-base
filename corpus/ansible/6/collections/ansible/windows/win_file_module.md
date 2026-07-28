---
collection: ansible
version: "6"
title: "ansible.windows.win_file module – Creates, touches or removes files or directories"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/windows/win_file_module.html
fetched_at: 2026-07-27T16:44:56+00:00
---
# ansible.windows.win_file module – Creates, touches or removes files or directories

> **Note:**
>
> This module is part of the [ansible.windows collection](https://galaxy.ansible.com/ansible/windows) (version 1.12.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.windows`.
>
> To use it in a playbook, specify: `ansible.windows.win_file`.

- [Synopsis](win_file_module.md#synopsis)
- [Parameters](win_file_module.md#parameters)
- [See Also](win_file_module.md#see-also)
- [Examples](win_file_module.md#examples)

## [Synopsis](win_file_module.md#id1)

- Creates (empty) files, updates file modification stamps of existing files, and can create or remove directories.
- Unlike [ansible.builtin.file](../builtin/file_module.md#ansible-collections-ansible-builtin-file-module), does not modify ownership, permissions or manipulate links.
- For non-Windows targets, use the [ansible.builtin.file](../builtin/file_module.md#ansible-collections-ansible-builtin-file-module) module instead.

## [Parameters](win_file_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **path**  aliases: dest, name  path / required | Path to the file being managed. |
| **state**  string | If `directory`, all immediate subdirectories will be created if they do not exist.  If `file`, the file will NOT be created if it does not exist, see the [ansible.windows.win_copy](win_copy_module.md#ansible-collections-ansible-windows-win-copy-module) or [ansible.windows.win_template](win_template_module.md#ansible-collections-ansible-windows-win-template-module) module if you want that behavior.  If `absent`, directories will be recursively deleted, and files will be removed.  If `touch`, an empty file will be created if the `path` does not exist, while an existing file or directory will receive updated file access and modification times (similar to the way `touch` works from the command line).  Choices:   - `"absent"` - `"directory"` - `"file"` - `"touch"` |

## [See Also](win_file_module.md#id3)

> **See also:**
>
> [ansible.builtin.file](../builtin/file_module.md#ansible-collections-ansible-builtin-file-module)
> :   Manage files and file properties.
>
> [ansible.windows.win_acl](win_acl_module.md#ansible-collections-ansible-windows-win-acl-module)
> :   Set file/directory/registry permissions for a system user or group.
>
> [ansible.windows.win_acl_inheritance](win_acl_inheritance_module.md#ansible-collections-ansible-windows-win-acl-inheritance-module)
> :   Change ACL inheritance.
>
> [ansible.windows.win_owner](win_owner_module.md#ansible-collections-ansible-windows-win-owner-module)
> :   Set owner.
>
> [ansible.windows.win_stat](win_stat_module.md#ansible-collections-ansible-windows-win-stat-module)
> :   Get information about Windows files.

## [Examples](win_file_module.md#id4)

```yaml+jinja
- name: Touch a file (creates if not present, updates modification time if present)
  ansible.windows.win_file:
    path: C:\Temp\foo.conf
    state: touch

- name: Remove a file, if present
  ansible.windows.win_file:
    path: C:\Temp\foo.conf
    state: absent

- name: Create directory structure
  ansible.windows.win_file:
    path: C:\Temp\folder\subfolder
    state: directory

- name: Remove directory structure
  ansible.windows.win_file:
    path: C:\Temp
    state: absent
```

### Authors

- Jon Hawkesworth (@jhawkesworth)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
[Communication](index.md#communication-for-ansible-windows)
