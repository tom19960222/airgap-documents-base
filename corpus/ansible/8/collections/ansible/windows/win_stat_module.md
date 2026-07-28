---
collection: ansible
version: "8"
title: "ansible.windows.win_stat module – Get information about Windows files"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/windows/win_stat_module.html
fetched_at: 2026-07-28T01:10:50+00:00
---
# ansible.windows.win_stat module – Get information about Windows files

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
> To use it in a playbook, specify: `ansible.windows.win_stat`.

- [Synopsis](win_stat_module.md#synopsis)
- [Parameters](win_stat_module.md#parameters)
- [See Also](win_stat_module.md#see-also)
- [Examples](win_stat_module.md#examples)
- [Return Values](win_stat_module.md#return-values)

## [Synopsis](win_stat_module.md#id1)

- Returns information about a Windows file.
- For non-Windows targets, use the [ansible.builtin.stat](../builtin/stat_module.md#ansible-collections-ansible-builtin-stat-module) module instead.

## [Parameters](win_stat_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **checksum_algorithm**  string | Algorithm to determine checksum of file.  Will throw an error if the host is unable to use specified algorithm.  **Choices:**   - `"md5"` - `"sha1"` ← (default) - `"sha256"` - `"sha384"` - `"sha512"` |
| **follow**  boolean | Whether to follow symlinks or junction points.  In the case of `path` pointing to another link, then that will be followed until no more links are found.  **Choices:**   - `false` ← (default) - `true` |
| **get_checksum**  boolean | Whether to return a checksum of the file (default sha1)  **Choices:**   - `false` - `true` ← (default) |
| **get_size**  boolean  *added in ansible.windows 1.11.0* | Whether to return the size of a file or directory.  **Choices:**   - `false` - `true` ← (default) |
| **path**  aliases: dest, name  path / required | The full path of the file/object to get the facts of; both forward and back slashes are accepted. |

## [See Also](win_stat_module.md#id3)

> **See also:**
>
> [ansible.builtin.stat](../builtin/stat_module.md#ansible-collections-ansible-builtin-stat-module)
> :   Retrieve file or file system status.
>
> [ansible.windows.win_acl](win_acl_module.md#ansible-collections-ansible-windows-win-acl-module)
> :   Set file/directory/registry permissions for a system user or group.
>
> [ansible.windows.win_file](win_file_module.md#ansible-collections-ansible-windows-win-file-module)
> :   Creates, touches or removes files or directories.
>
> [ansible.windows.win_owner](win_owner_module.md#ansible-collections-ansible-windows-win-owner-module)
> :   Set owner.

## [Examples](win_stat_module.md#id4)

```yaml+jinja
- name: Obtain information about a file
  ansible.windows.win_stat:
    path: C:\foo.ini
  register: file_info

- name: Obtain information about a folder
  ansible.windows.win_stat:
    path: C:\bar
  register: folder_info

- name: Get MD5 checksum of a file
  ansible.windows.win_stat:
    path: C:\foo.ini
    get_checksum: true
    checksum_algorithm: md5
  register: md5_checksum

- debug:
    var: md5_checksum.stat.checksum

- name: Get SHA1 checksum of file
  ansible.windows.win_stat:
    path: C:\foo.ini
    get_checksum: true
  register: sha1_checksum

- debug:
    var: sha1_checksum.stat.checksum

- name: Get SHA256 checksum of file
  ansible.windows.win_stat:
    path: C:\foo.ini
    get_checksum: true
    checksum_algorithm: sha256
  register: sha256_checksum

- debug:
    var: sha256_checksum.stat.checksum
```

## [Return Values](win_stat_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether anything was changed  **Returned:** always  **Sample:** `true` |
| **stat**  complex | dictionary containing all the stat data  **Returned:** success |
| **attributes**  string | Attributes of the file at path in raw form.  **Returned:** success, path exists  **Sample:** `"Archive, Hidden"` |
| **checksum**  string | The checksum of a file based on checksum_algorithm specified.  **Returned:** success, path exist, path is a file, get_checksum == True checksum_algorithm specified is supported  **Sample:** `"09cb79e8fc7453c84a07f644e441fd81623b7f98"` |
| **creationtime**  float | The create time of the file represented in seconds since epoch.  **Returned:** success, path exists  **Sample:** `1477984205.15` |
| **exists**  boolean | If the path exists or not.  **Returned:** success  **Sample:** `true` |
| **extension**  string | The extension of the file at path.  **Returned:** success, path exists, path is a file  **Sample:** `".ps1"` |
| **filename**  string | The name of the file (without path).  **Returned:** success, path exists, path is a file  **Sample:** `"foo.ini"` |
| **hlnk_targets**  list / elements=string | List of other files pointing to the same file (hard links), excludes the current file.  **Returned:** success, path exists  **Sample:** `["C:\\temp\\file.txt", "C:\\Windows\\update.log"]` |
| **isarchive**  boolean | If the path is ready for archiving or not.  **Returned:** success, path exists  **Sample:** `true` |
| **isdir**  boolean | If the path is a directory or not.  **Returned:** success, path exists  **Sample:** `true` |
| **ishidden**  boolean | If the path is hidden or not.  **Returned:** success, path exists  **Sample:** `true` |
| **isjunction**  boolean | If the path is a junction point or not.  **Returned:** success, path exists  **Sample:** `true` |
| **islnk**  boolean | If the path is a symbolic link or not.  **Returned:** success, path exists  **Sample:** `true` |
| **isreadonly**  boolean | If the path is read only or not.  **Returned:** success, path exists  **Sample:** `true` |
| **isreg**  boolean | If the path is a regular file.  **Returned:** success, path exists  **Sample:** `true` |
| **isshared**  boolean | If the path is shared or not.  **Returned:** success, path exists  **Sample:** `true` |
| **lastaccesstime**  float | The last access time of the file represented in seconds since epoch.  **Returned:** success, path exists  **Sample:** `1477984205.15` |
| **lastwritetime**  float | The last modification time of the file represented in seconds since epoch.  **Returned:** success, path exists  **Sample:** `1477984205.15` |
| **lnk_source**  string | Target of the symlink normalized for the remote filesystem.  **Returned:** success, path exists and the path is a symbolic link or junction point  **Sample:** `"C:\\temp\\link"` |
| **lnk_target**  string | Target of the symlink. Note that relative paths remain relative.  **Returned:** success, path exists and the path is a symbolic link or junction point  **Sample:** `"..\\link"` |
| **nlink**  integer | Number of links to the file (hard links).  **Returned:** success, path exists  **Sample:** `1` |
| **owner**  string | The owner of the file.  **Returned:** success, path exists  **Sample:** `"BUILTIN\\Administrators"` |
| **path**  string | The full absolute path to the file.  **Returned:** success, path exists, file exists  **Sample:** `"C:\\foo.ini"` |
| **sharename**  string | The name of share if folder is shared.  **Returned:** success, path exists, file is a directory and isshared == True  **Sample:** `"file-share"` |
| **size**  integer | The size in bytes of a file or folder.  **Returned:** success, path exists, file is not a link, get_size == True  **Sample:** `1024` |

### Authors

- Chris Church (@cchurch)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
- [Communication](index.md#communication-for-ansible-windows)
