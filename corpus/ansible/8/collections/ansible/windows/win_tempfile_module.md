---
collection: ansible
version: "8"
title: "ansible.windows.win_tempfile module – Creates temporary files and directories"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/windows/win_tempfile_module.html
fetched_at: 2026-07-28T01:10:51+00:00
---
# ansible.windows.win_tempfile module – Creates temporary files and directories

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
> To use it in a playbook, specify: `ansible.windows.win_tempfile`.

- [Synopsis](win_tempfile_module.md#synopsis)
- [Parameters](win_tempfile_module.md#parameters)
- [See Also](win_tempfile_module.md#see-also)
- [Examples](win_tempfile_module.md#examples)
- [Return Values](win_tempfile_module.md#return-values)

## [Synopsis](win_tempfile_module.md#id1)

- Creates temporary files and directories.
- For non-Windows targets, please use the [ansible.builtin.tempfile](../builtin/tempfile_module.md#ansible-collections-ansible-builtin-tempfile-module) module instead.

## [Parameters](win_tempfile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **path**  aliases: dest  path | Location where temporary file or directory should be created.  If path is not specified default system temporary directory (%TEMP%) will be used.  **Default:** `"%TEMP%"` |
| **prefix**  string | Prefix of file/directory name created by module.  **Default:** `"ansible."` |
| **state**  string | Whether to create file or directory.  **Choices:**   - `"directory"` - `"file"` ← (default) |
| **suffix**  string | Suffix of file/directory name created by module. |

## [See Also](win_tempfile_module.md#id3)

> **See also:**
>
> [ansible.builtin.tempfile](../builtin/tempfile_module.md#ansible-collections-ansible-builtin-tempfile-module)
> :   Creates temporary files and directories.

## [Examples](win_tempfile_module.md#id4)

```yaml+jinja
- name: Create temporary build directory
  ansible.windows.win_tempfile:
    state: directory
    suffix: build

- name: Create temporary file
  ansible.windows.win_tempfile:
    state: file
    suffix: temp
```

## [Return Values](win_tempfile_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **path**  string | The absolute path to the created file or directory.  **Returned:** success  **Sample:** `"C:\\Users\\Administrator\\AppData\\Local\\Temp\\ansible.bMlvdk"` |

### Authors

- Dag Wieers (@dagwieers)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
- [Communication](index.md#communication-for-ansible-windows)
