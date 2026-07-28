---
collection: ansible
version: "8"
title: "ansible.builtin.stat module – Retrieve file or file system status"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/stat_module.html
fetched_at: 2026-07-28T01:07:44+00:00
---
# ansible.builtin.stat module – Retrieve file or file system status

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `stat` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.stat` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](stat_module.md#synopsis)
- [Parameters](stat_module.md#parameters)
- [Attributes](stat_module.md#attributes)
- [See Also](stat_module.md#see-also)
- [Examples](stat_module.md#examples)
- [Return Values](stat_module.md#return-values)

## [Synopsis](stat_module.md#id2)

- Retrieves facts for a file similar to the Linux/Unix ‘stat’ command.
- For Windows targets, use the [ansible.windows.win_stat](../windows/win_stat_module.md#ansible-collections-ansible-windows-win-stat-module) module instead.

## [Parameters](stat_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **checksum_algorithm**  aliases: checksum, checksum_algo  string | Algorithm to determine checksum of file.  Will throw an error if the host is unable to use specified algorithm.  The remote host has to support the hashing method specified, `md5` can be unavailable if the host is FIPS-140 compliant.  **Choices:**   - `"md5"` - `"sha1"` ← (default) - `"sha224"` - `"sha256"` - `"sha384"` - `"sha512"` |
| **follow**  boolean | Whether to follow symlinks.  **Choices:**   - `false` ← (default) - `true` |
| **get_attributes**  aliases: attr, attributes  boolean | Get file attributes using lsattr tool if present.  **Choices:**   - `false` - `true` ← (default) |
| **get_checksum**  boolean | Whether to return a checksum of the file.  **Choices:**   - `false` - `true` ← (default) |
| **get_mime**  aliases: mime, mime_type, mime-type  boolean | Use file magic and return data about the nature of the file. this uses the ‘file’ utility found on most Linux/Unix systems.  This will add both `mimetype` and `charset` fields to the return, if possible.  In Ansible 2.3 this option changed from *mime* to *get_mime* and the default changed to `true`.  **Choices:**   - `false` - `true` ← (default) |
| **path**  aliases: dest, name  path / required | The full path of the file/object to get the facts of. |

## [Attributes](stat_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platform:** **posix** | Target OS/families that can be operated against |

## [See Also](stat_module.md#id5)

> **See also:**
>
> [ansible.builtin.file](file_module.md#ansible-collections-ansible-builtin-file-module)
> :   Manage files and file properties.
>
> [ansible.windows.win_stat](../windows/win_stat_module.md#ansible-collections-ansible-windows-win-stat-module)
> :   Get information about Windows files.

## [Examples](stat_module.md#id6)

```yaml+jinja
# Obtain the stats of /etc/foo.conf, and check that the file still belongs
# to 'root'. Fail otherwise.
- name: Get stats of a file
  ansible.builtin.stat:
    path: /etc/foo.conf
  register: st
- name: Fail if the file does not belong to 'root'
  ansible.builtin.fail:
    msg: "Whoops! file ownership has changed"
  when: st.stat.pw_name != 'root'

# Determine if a path exists and is a symlink. Note that if the path does
# not exist, and we test sym.stat.islnk, it will fail with an error. So
# therefore, we must test whether it is defined.
# Run this to understand the structure, the skipped ones do not pass the
# check performed by 'when'
- name: Get stats of the FS object
  ansible.builtin.stat:
    path: /path/to/something
  register: sym

- name: Print a debug message
  ansible.builtin.debug:
    msg: "islnk isn't defined (path doesn't exist)"
  when: sym.stat.islnk is not defined

- name: Print a debug message
  ansible.builtin.debug:
    msg: "islnk is defined (path must exist)"
  when: sym.stat.islnk is defined

- name: Print a debug message
  ansible.builtin.debug:
    msg: "Path exists and is a symlink"
  when: sym.stat.islnk is defined and sym.stat.islnk

- name: Print a debug message
  ansible.builtin.debug:
    msg: "Path exists and isn't a symlink"
  when: sym.stat.islnk is defined and sym.stat.islnk == False

# Determine if a path exists and is a directory.  Note that we need to test
# both that p.stat.isdir actually exists, and also that it's set to true.
- name: Get stats of the FS object
  ansible.builtin.stat:
    path: /path/to/something
  register: p
- name: Print a debug message
  ansible.builtin.debug:
    msg: "Path exists and is a directory"
  when: p.stat.isdir is defined and p.stat.isdir

- name: Do not calculate the checksum
  ansible.builtin.stat:
    path: /path/to/myhugefile
    get_checksum: no

- name: Use sha256 to calculate the checksum
  ansible.builtin.stat:
    path: /path/to/something
    checksum_algorithm: sha256
```

## [Return Values](stat_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **stat**  complex | Dictionary containing all the stat data, some platforms might add additional fields.  **Returned:** success |
| **atime**  float | Time of last access  **Returned:** success, path exists and user can read stats  **Sample:** `1424348972.575` |
| **attributes**  list / elements=string | list of file attributes  **Returned:** success, path exists and user can execute the path  **Sample:** `["immutable", "extent"]` |
| **charset**  string | file character set or encoding  **Returned:** success, path exists and user can read stats and installed python supports it and the *get_mime* option was true, will return `unknown` on error.  **Sample:** `"us-ascii"` |
| **checksum**  string | hash of the file  **Returned:** success, path exists, user can read stats, path supports hashing and supplied checksum algorithm is available  **Sample:** `"50ba294cdf28c0d5bcde25708df53346825a429f"` |
| **ctime**  float | Time of last metadata update or creation (depends on OS)  **Returned:** success, path exists and user can read stats  **Sample:** `1424348972.575` |
| **dev**  integer | Device the inode resides on  **Returned:** success, path exists and user can read stats  **Sample:** `33` |
| **executable**  boolean | Tells you if the invoking user has execute permission on the path  **Returned:** success, path exists and user can execute the path  **Sample:** `false` |
| **exists**  boolean | If the destination path actually exists or not  **Returned:** success  **Sample:** `true` |
| **gid**  integer | Numeric id representing the group of the owner  **Returned:** success, path exists and user can read stats  **Sample:** `1003` |
| **gr_name**  string | Group name of owner  **Returned:** success, path exists, user can read stats, owner group can be looked up and installed python supports it  **Sample:** `"www-data"` |
| **inode**  integer | Inode number of the path  **Returned:** success, path exists and user can read stats  **Sample:** `12758` |
| **isblk**  boolean | Tells you if the path is a block device  **Returned:** success, path exists and user can read stats  **Sample:** `false` |
| **ischr**  boolean | Tells you if the path is a character device  **Returned:** success, path exists and user can read stats  **Sample:** `false` |
| **isdir**  boolean | Tells you if the path is a directory  **Returned:** success, path exists and user can read stats  **Sample:** `false` |
| **isfifo**  boolean | Tells you if the path is a named pipe  **Returned:** success, path exists and user can read stats  **Sample:** `false` |
| **isgid**  boolean | Tells you if the invoking user’s group id matches the owner’s group id  **Returned:** success, path exists and user can read stats  **Sample:** `false` |
| **islnk**  boolean | Tells you if the path is a symbolic link  **Returned:** success, path exists and user can read stats  **Sample:** `false` |
| **isreg**  boolean | Tells you if the path is a regular file  **Returned:** success, path exists and user can read stats  **Sample:** `true` |
| **issock**  boolean | Tells you if the path is a unix domain socket  **Returned:** success, path exists and user can read stats  **Sample:** `false` |
| **isuid**  boolean | Tells you if the invoking user’s id matches the owner’s id  **Returned:** success, path exists and user can read stats  **Sample:** `false` |
| **lnk_source**  string | Target of the symlink normalized for the remote filesystem  **Returned:** success, path exists and user can read stats and the path is a symbolic link  **Sample:** `"/home/foobar/21102015-1445431274-908472971"` |
| **lnk_target**  string | Target of the symlink. Note that relative paths remain relative  **Returned:** success, path exists and user can read stats and the path is a symbolic link  **Sample:** `"../foobar/21102015-1445431274-908472971"` |
| **md5**  string | md5 hash of the file; this will be removed in Ansible 2.9 in favor of the checksum return value  **Returned:** success, path exists and user can read stats and path supports hashing and md5 is supported  **Sample:** `"f88fa92d8cf2eeecf4c0a50ccc96d0c0"` |
| **mimetype**  string | file magic data or mime-type  **Returned:** success, path exists and user can read stats and installed python supports it and the *get_mime* option was true, will return `unknown` on error.  **Sample:** `"application/pdf; charset=binary"` |
| **mode**  string | Unix permissions of the file in octal representation as a string  **Returned:** success, path exists and user can read stats  **Sample:** `"1755"` |
| **mtime**  float | Time of last modification  **Returned:** success, path exists and user can read stats  **Sample:** `1424348972.575` |
| **nlink**  integer | Number of links to the inode (hard links)  **Returned:** success, path exists and user can read stats  **Sample:** `1` |
| **path**  string | The full path of the file/object to get the facts of  **Returned:** success and if path exists  **Sample:** `"/path/to/file"` |
| **pw_name**  string | User name of owner  **Returned:** success, path exists, user can read stats, owner name can be looked up and installed python supports it  **Sample:** `"httpd"` |
| **readable**  boolean | Tells you if the invoking user has the right to read the path  **Returned:** success, path exists and user can read the path  **Sample:** `false` |
| **rgrp**  boolean | Tells you if the owner’s group has read permission  **Returned:** success, path exists and user can read stats  **Sample:** `true` |
| **roth**  boolean | Tells you if others have read permission  **Returned:** success, path exists and user can read stats  **Sample:** `true` |
| **rusr**  boolean | Tells you if the owner has read permission  **Returned:** success, path exists and user can read stats  **Sample:** `true` |
| **size**  integer | Size in bytes for a plain file, amount of data for some special files  **Returned:** success, path exists and user can read stats  **Sample:** `203` |
| **uid**  integer | Numeric id representing the file owner  **Returned:** success, path exists and user can read stats  **Sample:** `1003` |
| **version**  string | The version/generation attribute of a file according to the filesystem  **Returned:** success, path exists, user can execute the path, lsattr is available and filesystem supports  **Sample:** `"381700746"` |
| **wgrp**  boolean | Tells you if the owner’s group has write permission  **Returned:** success, path exists and user can read stats  **Sample:** `false` |
| **woth**  boolean | Tells you if others have write permission  **Returned:** success, path exists and user can read stats  **Sample:** `false` |
| **writeable**  boolean | Tells you if the invoking user has the right to write the path  **Returned:** success, path exists and user can write the path  **Sample:** `false` |
| **wusr**  boolean | Tells you if the owner has write permission  **Returned:** success, path exists and user can read stats  **Sample:** `true` |
| **xgrp**  boolean | Tells you if the owner’s group has execute permission  **Returned:** success, path exists and user can read stats  **Sample:** `true` |
| **xoth**  boolean | Tells you if others have execute permission  **Returned:** success, path exists and user can read stats  **Sample:** `true` |
| **xusr**  boolean | Tells you if the owner has execute permission  **Returned:** success, path exists and user can read stats  **Sample:** `true` |

### Authors

- Bruce Pennypacker (@bpennypacker)

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
