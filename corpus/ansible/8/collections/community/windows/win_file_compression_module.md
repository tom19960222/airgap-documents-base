---
collection: ansible
version: "8"
title: "community.windows.win_file_compression module – Alters the compression of files and directories on NTFS partitions."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_file_compression_module.html
fetched_at: 2026-07-28T02:01:54+00:00
---
# community.windows.win_file_compression module – Alters the compression of files and directories on NTFS partitions.

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
> To use it in a playbook, specify: `community.windows.win_file_compression`.

- [Synopsis](win_file_compression_module.md#synopsis)
- [Parameters](win_file_compression_module.md#parameters)
- [Notes](win_file_compression_module.md#notes)
- [Examples](win_file_compression_module.md#examples)
- [Return Values](win_file_compression_module.md#return-values)

## [Synopsis](win_file_compression_module.md#id1)

- This module sets the compressed attribute for files and directories on a filesystem that supports it like NTFS.
- NTFS compression can be used to save disk space.

## [Parameters](win_file_compression_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **force**  boolean | This option only has an effect when *recurse* is `true`  If `true`, will check the compressed state of all subdirectories and files and make a change if any are different from *compressed*.  If `false`, will only make a change if the compressed state of *path* is different from *compressed*.  If the folder structure is complex or contains a lot of files, it is recommended to set this option to `false` so that not every file has to be checked.  **Choices:**   - `false` - `true` ← (default) |
| **path**  path / required | The full path of the file or directory to modify.  The path must exist on file system that supports compression like NTFS. |
| **recurse**  boolean | Whether to recursively apply changes to all subdirectories and files.  This option only has an effect when *path* is a directory.  When set to `false`, only applies changes to *path*.  When set to `true`, applies changes to *path* and all subdirectories and files.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | Set to `present` to ensure the *path* is compressed.  Set to `absent` to ensure the *path* is not compressed.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Notes](win_file_compression_module.md#id3)

> **Note:**
>
> - [community.windows.win_file_compression](win_file_compression_module.md#ansible-collections-community-windows-win-file-compression-module) sets the file system’s compression state, it does not create a zip archive file.
> - For more about NTFS Compression, see <http://www.ntfs.com/ntfs-compressed.htm>

## [Examples](win_file_compression_module.md#id4)

```yaml+jinja
- name: Compress log files directory
  community.windows.win_file_compression:
    path: C:\Logs
    state: present

- name: Decompress log files directory
  community.windows.win_file_compression:
    path: C:\Logs
    state: absent

- name: Compress reports directory and all subdirectories
  community.windows.win_file_compression:
    path: C:\business\reports
    state: present
    recurse: yes

# This will only check C:\business\reports for the compressed state
# If C:\business\reports is compressed, it will not make a change
# even if one of the child items is uncompressed

- name: Compress reports directory and all subdirectories (quick)
  community.windows.win_file_compression:
    path: C:\business\reports
    compressed: yes
    recurse: yes
    force: no
```

## [Return Values](win_file_compression_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **rc**  integer | The return code of the compress/uncompress operation.  If no changes are made or the operation is successful, rc is 0.  **Returned:** always  **Sample:** `0` |

### Authors

- Micah Hunsberger (@mhunsber)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
