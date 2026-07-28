---
collection: ansible
version: "8"
title: "ansible.windows.win_find module – Return a list of files based on specific criteria"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/windows/win_find_module.html
fetched_at: 2026-07-28T01:10:37+00:00
---
# ansible.windows.win_find module – Return a list of files based on specific criteria

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
> To use it in a playbook, specify: `ansible.windows.win_find`.

- [Synopsis](win_find_module.md#synopsis)
- [Parameters](win_find_module.md#parameters)
- [Notes](win_find_module.md#notes)
- [Examples](win_find_module.md#examples)
- [Return Values](win_find_module.md#return-values)

## [Synopsis](win_find_module.md#id1)

- Return a list of files based on specified criteria.
- Multiple criteria are AND’d together.
- For non-Windows targets, use the [ansible.builtin.find](../builtin/find_module.md#ansible-collections-ansible-builtin-find-module) module instead.

## [Parameters](win_find_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **age**  string | Select files or folders whose age is equal to or greater than the specified time.  Use a negative age to find files equal to or less than the specified time.  You can choose seconds, minutes, hours, days or weeks by specifying the first letter of an of those words (e.g., “2s”, “10d”, 1w”). |
| **age_stamp**  string | Choose the file property against which we compare `age`.  The default attribute we compare with is the last modification time.  **Choices:**   - `"atime"` - `"ctime"` - `"mtime"` ← (default) |
| **checksum_algorithm**  string | Algorithm to determine the checksum of a file.  Will throw an error if the host is unable to use specified algorithm.  **Choices:**   - `"md5"` - `"sha1"` ← (default) - `"sha256"` - `"sha384"` - `"sha512"` |
| **file_type**  string | Type of file to search for.  **Choices:**   - `"directory"` - `"file"` ← (default) |
| **follow**  boolean | Set this to `true` to follow symlinks in the path.  This needs to be used in conjunction with `recurse`.  **Choices:**   - `false` ← (default) - `true` |
| **get_checksum**  boolean | Whether to return a checksum of the file in the return info (default sha1), use `checksum_algorithm` to change from the default.  **Choices:**   - `false` - `true` ← (default) |
| **hidden**  boolean | Set this to include hidden files or folders.  **Choices:**   - `false` ← (default) - `true` |
| **paths**  list / elements=string / required | List of paths of directories to search for files or folders in.  This can be supplied as a single path or a list of paths. |
| **patterns**  aliases: regex, regexp  list / elements=string | One or more (powershell or regex) patterns to compare filenames with.  The type of pattern matching is controlled by `use_regex` option.  The patterns restrict the list of files or folders to be returned based on the filenames.  For a file to be matched it only has to match with one pattern in a list provided. |
| **recurse**  boolean | Will recursively descend into the directory looking for files or folders.  **Choices:**   - `false` ← (default) - `true` |
| **size**  string | Select files or folders whose size is equal to or greater than the specified size.  Use a negative value to find files equal to or less than the specified size.  You can specify the size with a suffix of the byte type i.e. kilo = k, mega = m…  Size is not evaluated for symbolic links. |
| **use_regex**  boolean | Will set patterns to run as a regex check if set to `true`.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](win_find_module.md#id3)

> **Note:**
>
> - When scanning directories with a large number of files containing lots of data it is recommended to set `get_checksum=false`. This will speed up the time it takes to scan the folders as getting a checksum needs to read the contents of every file it returns.

## [Examples](win_find_module.md#id4)

```yaml+jinja
- name: Find files in path
  ansible.windows.win_find:
    paths: D:\Temp

- name: Find hidden files in path
  ansible.windows.win_find:
    paths: D:\Temp
    hidden: true

- name: Find files in multiple paths
  ansible.windows.win_find:
    paths:
    - C:\Temp
    - D:\Temp

- name: Find files in directory while searching recursively
  ansible.windows.win_find:
    paths: D:\Temp
    recurse: true

- name: Find files in directory while following symlinks
  ansible.windows.win_find:
    paths: D:\Temp
    recurse: true
    follow: true

- name: Find files with .log and .out extension using powershell wildcards
  ansible.windows.win_find:
    paths: D:\Temp
    patterns: [ '*.log', '*.out' ]

- name: Find files in path based on regex pattern
  ansible.windows.win_find:
    paths: D:\Temp
    patterns: out_\d{8}-\d{6}.log

- name: Find files older than 1 day
  ansible.windows.win_find:
    paths: D:\Temp
    age: 86400

- name: Find files older than 1 day based on create time
  ansible.windows.win_find:
    paths: D:\Temp
    age: 86400
    age_stamp: ctime

- name: Find files older than 1 day with unit syntax
  ansible.windows.win_find:
    paths: D:\Temp
    age: 1d

- name: Find files newer than 1 hour
  ansible.windows.win_find:
    paths: D:\Temp
    age: -3600

- name: Find files newer than 1 hour with unit syntax
  ansible.windows.win_find:
    paths: D:\Temp
    age: -1h

- name: Find files larger than 1MB
  ansible.windows.win_find:
    paths: D:\Temp
    size: 1048576

- name: Find files larger than 1GB with unit syntax
  ansible.windows.win_find:
    paths: D:\Temp
    size: 1g

- name: Find files smaller than 1MB
  ansible.windows.win_find:
    paths: D:\Temp
    size: -1048576

- name: Find files smaller than 1GB with unit syntax
  ansible.windows.win_find:
    paths: D:\Temp
    size: -1g

- name: Find folders/symlinks in multiple paths
  ansible.windows.win_find:
    paths:
    - C:\Temp
    - D:\Temp
    file_type: directory

- name: Find files and return SHA256 checksum of files found
  ansible.windows.win_find:
    paths: C:\Temp
    get_checksum: true
    checksum_algorithm: sha256

- name: Find files and do not return the checksum
  ansible.windows.win_find:
    paths: C:\Temp
    get_checksum: false
```

## [Return Values](win_find_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **examined**  integer | The number of files/folders that was checked.  **Returned:** always  **Sample:** `10` |
| **files**  complex | Information on the files/folders that match the criteria returned as a list of dictionary elements for each file matched. The entries are sorted by the path value alphabetically.  **Returned:** success |
| **attributes**  string | attributes of the file at path in raw form.  **Returned:** success, path exists  **Sample:** `"Archive, Hidden"` |
| **checksum**  string | The checksum of a file based on checksum_algorithm specified.  **Returned:** success, path exists, path is a file, get_checksum == True  **Sample:** `"09cb79e8fc7453c84a07f644e441fd81623b7f98"` |
| **creationtime**  float | The create time of the file represented in seconds since epoch.  **Returned:** success, path exists  **Sample:** `1477984205.15` |
| **exists**  boolean | Whether the file exists, will always be true for [ansible.windows.win_find](win_find_module.md#ansible-collections-ansible-windows-win-find-module).  **Returned:** success, path exists  **Sample:** `true` |
| **extension**  string | The extension of the file at path.  **Returned:** success, path exists, path is a file  **Sample:** `".ps1"` |
| **filename**  string | The name of the file.  **Returned:** success, path exists  **Sample:** `"temp"` |
| **hlnk_targets**  list / elements=string | List of other files pointing to the same file (hard links), excludes the current file.  **Returned:** success, path exists  **Sample:** `["C:\\temp\\file.txt", "C:\\Windows\\update.log"]` |
| **isarchive**  boolean | If the path is ready for archiving or not.  **Returned:** success, path exists  **Sample:** `true` |
| **isdir**  boolean | If the path is a directory or not.  **Returned:** success, path exists  **Sample:** `true` |
| **ishidden**  boolean | If the path is hidden or not.  **Returned:** success, path exists  **Sample:** `true` |
| **isjunction**  boolean | If the path is a junction point.  **Returned:** success, path exists  **Sample:** `true` |
| **islnk**  boolean | If the path is a symbolic link.  **Returned:** success, path exists  **Sample:** `true` |
| **isreadonly**  boolean | If the path is read only or not.  **Returned:** success, path exists  **Sample:** `true` |
| **isreg**  boolean | If the path is a regular file or not.  **Returned:** success, path exists  **Sample:** `true` |
| **isshared**  boolean | If the path is shared or not.  **Returned:** success, path exists  **Sample:** `true` |
| **lastaccesstime**  float | The last access time of the file represented in seconds since epoch.  **Returned:** success, path exists  **Sample:** `1477984205.15` |
| **lastwritetime**  float | The last modification time of the file represented in seconds since epoch.  **Returned:** success, path exists  **Sample:** `1477984205.15` |
| **lnk_source**  string | The target of the symlink normalized for the remote filesystem.  **Returned:** success, path exists, path is a symbolic link or junction point  **Sample:** `"C:\\temp"` |
| **lnk_target**  string | The target of the symlink. Note that relative paths remain relative, will return null if not a link.  **Returned:** success, path exists, path is a symbolic link or junction point  **Sample:** `"temp"` |
| **nlink**  integer | Number of links to the file (hard links)  **Returned:** success, path exists  **Sample:** `1` |
| **owner**  string | The owner of the file.  **Returned:** success, path exists  **Sample:** `"BUILTIN\\Administrators"` |
| **path**  string | The full absolute path to the file.  **Returned:** success, path exists  **Sample:** `"C:\\temp\\file.txt"` |
| **sharename**  string | The name of share if folder is shared.  **Returned:** success, path exists, path is a directory and isshared == True  **Sample:** `"file-share"` |
| **size**  integer | The size in bytes of the file.  **Returned:** success, path exists, path is a file  **Sample:** `1024` |
| **matched**  integer | The number of files/folders that match the criteria.  **Returned:** always  **Sample:** `2` |

### Authors

- Jordan Borean (@jborean93)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
- [Communication](index.md#communication-for-ansible-windows)
