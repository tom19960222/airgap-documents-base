---
collection: ansible
version: "8"
title: "community.general.archive module – Creates a compressed archive of one or more files or trees"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/archive_module.html
fetched_at: 2026-07-28T01:44:43+00:00
---
# community.general.archive module – Creates a compressed archive of one or more files or trees

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](archive_module.md#ansible-collections-community-general-archive-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.archive`.

- [Synopsis](archive_module.md#synopsis)
- [Requirements](archive_module.md#requirements)
- [Parameters](archive_module.md#parameters)
- [Attributes](archive_module.md#attributes)
- [Notes](archive_module.md#notes)
- [See Also](archive_module.md#see-also)
- [Examples](archive_module.md#examples)
- [Return Values](archive_module.md#return-values)

## [Synopsis](archive_module.md#id1)

- Creates or extends an archive.
- The source and archive are on the remote host, and the archive *is not* copied to the local host.
- Source files can be deleted after archival by specifying `remove=True`.

Aliases: files.archive

## [Requirements](archive_module.md#id2)

The below requirements are needed on the host that executes this module.

- Requires `lzma` (standard library of Python 3) or [backports.lzma](https://pypi.org/project/backports.lzma/) (Python 2) if using `xz` format.

## [Parameters](archive_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **attributes**  aliases: attr  string | The attributes the resulting filesystem object should have.  To get supported flags look at the man page for *chattr* on the target system.  This string should contain the attributes in the same order as the one displayed by *lsattr*.  The `=` operator is assumed as default, otherwise `+` or `-` operators need to be included in the string. |
| **dest**  path | The file name of the destination archive. The parent directory must exists on the remote host.  This is required when `path` refers to multiple files by either specifying a glob, a directory or multiple paths in a list.  If the destination archive already exists, it will be truncated and overwritten. |
| **exclude_path**  list / elements=path | Remote absolute path, glob, or list of paths or globs for the file or files to exclude from `path` list and glob expansion.  Use `exclusion_patterns` to instead exclude files or subdirectories below any of the paths from the `path` list.  **Default:** `[]` |
| **exclusion_patterns**  list / elements=path  *added in community.general 3.2.0* | Glob style patterns to exclude files or directories from the resulting archive.  This differs from `exclude_path` which applies only to the source paths from `path`. |
| **force_archive**  boolean | Allows you to force the module to treat this as an archive even if only a single file is specified.  By default when a single file is specified it is compressed only (not archived).  Enable this if you want to use [ansible.builtin.unarchive](../../ansible/builtin/unarchive_module.md#ansible-collections-ansible-builtin-unarchive-module) on an archive of a single file created with this module.  **Choices:**   - `false` ← (default) - `true` |
| **format**  string | The type of compression to use.  Support for xz was added in Ansible 2.5.  **Choices:**   - `"bz2"` - `"gz"` ← (default) - `"tar"` - `"xz"` - `"zip"` |
| **group**  string | Name of the group that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current group of the current user unless you are root, in which case it can preserve the previous ownership. |
| **mode**  any | The permissions the resulting filesystem object should have.  For those used to */usr/bin/chmod* remember that modes are actually octal numbers. You must give Ansible enough information to parse them correctly. For consistent results, quote octal numbers (for example, `'644'` or `'1777'`) so Ansible receives a string and can do its own conversion from string into number. Adding a leading zero (for example, `0755`) works sometimes, but can fail in loops and some other circumstances.  Giving Ansible a number without following either of these rules will end up with a decimal number which will have unexpected results.  As of Ansible 1.8, the mode may be specified as a symbolic mode (for example, `u+rwx` or `u=rw,g=r,o=r`).  If `mode` is not specified and the destination filesystem object **does not** exist, the default `umask` on the system will be used when setting the mode for the newly created filesystem object.  If `mode` is not specified and the destination filesystem object **does** exist, the mode of the existing filesystem object will be used.  Specifying `mode` is the best way to ensure filesystem objects are created with the correct permissions. See CVE-2020-1736 for further details. |
| **owner**  string | Name of the user that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current user unless you are root, in which case it can preserve the previous ownership.  Specifying a numeric username will be assumed to be a user ID and not a username. Avoid numeric usernames to avoid this confusion. |
| **path**  list / elements=path / required | Remote absolute path, glob, or list of paths or globs for the file or files to compress or archive. |
| **remove**  boolean | Remove any added source files and trees after adding to archive.  **Choices:**   - `false` ← (default) - `true` |
| **selevel**  string | The level part of the SELinux filesystem object context.  This is the MLS/MCS attribute, sometimes known as the `range`.  When set to `_default`, it will use the `level` portion of the policy if available. |
| **serole**  string | The role part of the SELinux filesystem object context.  When set to `_default`, it will use the `role` portion of the policy if available. |
| **setype**  string | The type part of the SELinux filesystem object context.  When set to `_default`, it will use the `type` portion of the policy if available. |
| **seuser**  string | The user part of the SELinux filesystem object context.  By default it uses the `system` policy, where applicable.  When set to `_default`, it will use the `user` portion of the policy if available. |
| **unsafe_writes**  boolean | Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target filesystem object.  By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target filesystem objects, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted filesystem objects, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.  This option allows Ansible to fall back to unsafe methods of updating filesystem objects when atomic operations fail (however, it doesn’t force Ansible to perform unsafe writes).  IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](archive_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](archive_module.md#id5)

> **Note:**
>
> - Can produce `gzip`, `bzip2`, `lzma`, and `zip` compressed files or archives.
> - This module uses `tarfile`, `zipfile`, `gzip`, and `bz2` packages on the target host to create archives. These are part of the Python standard library for Python 2 and 3.

## [See Also](archive_module.md#id6)

> **See also:**
>
> [ansible.builtin.unarchive](../../ansible/builtin/unarchive_module.md#ansible-collections-ansible-builtin-unarchive-module)
> :   Unpacks an archive after (optionally) copying it from the local machine.

## [Examples](archive_module.md#id7)

```yaml+jinja
- name: Compress directory /path/to/foo/ into /path/to/foo.tgz
  community.general.archive:
    path: /path/to/foo
    dest: /path/to/foo.tgz

- name: Compress regular file /path/to/foo into /path/to/foo.gz and remove it
  community.general.archive:
    path: /path/to/foo
    remove: true

- name: Create a zip archive of /path/to/foo
  community.general.archive:
    path: /path/to/foo
    format: zip

- name: Create a bz2 archive of multiple files, rooted at /path
  community.general.archive:
    path:
    - /path/to/foo
    - /path/wong/foo
    dest: /path/file.tar.bz2
    format: bz2

- name: Create a bz2 archive of a globbed path, while excluding specific dirnames
  community.general.archive:
    path:
    - /path/to/foo/*
    dest: /path/file.tar.bz2
    exclude_path:
    - /path/to/foo/bar
    - /path/to/foo/baz
    format: bz2

- name: Create a bz2 archive of a globbed path, while excluding a glob of dirnames
  community.general.archive:
    path:
    - /path/to/foo/*
    dest: /path/file.tar.bz2
    exclude_path:
    - /path/to/foo/ba*
    format: bz2

- name: Use gzip to compress a single archive (i.e don't archive it first with tar)
  community.general.archive:
    path: /path/to/foo/single.file
    dest: /path/file.gz
    format: gz

- name: Create a tar.gz archive of a single file.
  community.general.archive:
    path: /path/to/foo/single.file
    dest: /path/file.tar.gz
    format: gz
    force_archive: true
```

## [Return Values](archive_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **archived**  list / elements=string | Any files that were compressed or added to the archive.  **Returned:** success |
| **arcroot**  string | The archive root.  **Returned:** always |
| **dest_state**  string  *added in community.general 3.4.0* | The state of the `dest` file.  `absent` when the file does not exist.  `archive` when the file is an archive.  `compress` when the file is compressed, but not an archive.  `incomplete` when the file is an archive, but some files under `path` were not found.  **Returned:** success |
| **expanded_exclude_paths**  list / elements=string | The list of matching exclude paths from the exclude_path argument.  **Returned:** always |
| **expanded_paths**  list / elements=string | The list of matching paths from paths argument.  **Returned:** always |
| **missing**  list / elements=string | Any files that were missing from the source.  **Returned:** success |
| **state**  string | The state of the input `path`.  **Returned:** always |

### Authors

- Ben Doherty (@bendoh)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
