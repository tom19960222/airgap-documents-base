---
collection: ansible
version: "6"
title: "community.windows.win_zip module – Compress file or directory as zip archive on the Windows node"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_zip_module.html
fetched_at: 2026-07-27T17:24:05+00:00
---
# community.windows.win_zip module – Compress file or directory as zip archive on the Windows node

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/community/windows) (version 1.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
> You need further requirements to be able to use this module,
> see [Requirements](win_zip_module.md#ansible-collections-community-windows-win-zip-module-requirements) for details.
>
> To use it in a playbook, specify: `community.windows.win_zip`.

- [Synopsis](win_zip_module.md#synopsis)
- [Requirements](win_zip_module.md#requirements)
- [Parameters](win_zip_module.md#parameters)
- [Notes](win_zip_module.md#notes)
- [See Also](win_zip_module.md#see-also)
- [Examples](win_zip_module.md#examples)

## [Synopsis](win_zip_module.md#id1)

- Compress file or directory as zip archive.
- For non-Windows targets, use the [community.general.archive](../general/archive_module.md#ansible-collections-community-general-archive-module) module instead.

## [Requirements](win_zip_module.md#id2)

The below requirements are needed on the host that executes this module.

- .NET Framework 4.5 or later

## [Parameters](win_zip_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dest**  path / required | Destination path of zip file (provide absolute path of zip file on the target node). |
| **src**  string / required | File or directory path to be zipped (provide absolute path on the target node).  When a directory path the directory is zipped as the root entry in the archive.  Specify `\*` to the end of *src* to zip the contents of the directory and not the directory itself. |

## [Notes](win_zip_module.md#id4)

> **Note:**
>
> - The filenames in the zip are encoded using UTF-8.

## [See Also](win_zip_module.md#id5)

> **See also:**
>
> [community.general.archive](../general/archive_module.md#ansible-collections-community-general-archive-module)
> :   Creates a compressed archive of one or more files or trees.

## [Examples](win_zip_module.md#id6)

```yaml+jinja
- name: Compress a file
  community.windows.win_zip:
    src: C:\Users\hiyoko\log.txt
    dest: C:\Users\hiyoko\log.zip

- name: Compress a directory as the root of the archive
  community.windows.win_zip:
    src: C:\Users\hiyoko\log
    dest: C:\Users\hiyoko\log.zip

- name: Compress the directories contents
  community.windows.win_zip:
    src: C:\Users\hiyoko\log\*
    dest: C:\Users\hiyoko\log.zip
```

### Authors

- Kento Yagisawa (@hiyoko_taisa)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
