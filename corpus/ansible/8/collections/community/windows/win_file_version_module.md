---
collection: ansible
version: "8"
title: "community.windows.win_file_version module – Get DLL or EXE file build version"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_file_version_module.html
fetched_at: 2026-07-28T02:01:54+00:00
---
# community.windows.win_file_version module – Get DLL or EXE file build version

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/ui/repo/published/community/windows/) (version 1.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_file_version`.

- [Synopsis](win_file_version_module.md#synopsis)
- [Parameters](win_file_version_module.md#parameters)
- [Notes](win_file_version_module.md#notes)
- [See Also](win_file_version_module.md#see-also)
- [Examples](win_file_version_module.md#examples)
- [Return Values](win_file_version_module.md#return-values)

## [Synopsis](win_file_version_module.md#id1)

- Get DLL or EXE file build version.

## [Parameters](win_file_version_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **path**  path / required | File to get version.  Always provide absolute path. |

## [Notes](win_file_version_module.md#id3)

> **Note:**
>
> - This module will always return no change.

## [See Also](win_file_version_module.md#id4)

> **See also:**
>
> [ansible.windows.win_file](../../ansible/windows/win_file_module.md#ansible-collections-ansible-windows-win-file-module)
> :   Creates, touches or removes files or directories.

## [Examples](win_file_version_module.md#id5)

```yaml+jinja
- name: Get acm instance version
  community.windows.win_file_version:
    path: C:\Windows\System32\cmd.exe
  register: exe_file_version

- debug:
    msg: '{{ exe_file_version }}'
```

## [Return Values](win_file_version_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **file_build_part**  string | build number of the file.  **Returned:** no error |
| **file_major_part**  string | the major part of the version number.  **Returned:** no error |
| **file_minor_part**  string | the minor part of the version number of the file.  **Returned:** no error |
| **file_private_part**  string | file private part number.  **Returned:** no error |
| **file_version**  string | File version number..  **Returned:** no error |
| **path**  string | file path  **Returned:** always |
| **product_version**  string | The version of the product this file is distributed with.  **Returned:** no error |

### Authors

- Sam Liu (@SamLiu79)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
