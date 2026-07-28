---
collection: ansible
version: "6"
title: "community.general.filesystem module – Makes a filesystem"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/filesystem_module.html
fetched_at: 2026-07-27T17:08:54+00:00
---
# community.general.filesystem module – Makes a filesystem

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](filesystem_module.md#ansible-collections-community-general-filesystem-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.filesystem`.

- [Synopsis](filesystem_module.md#synopsis)
- [Requirements](filesystem_module.md#requirements)
- [Parameters](filesystem_module.md#parameters)
- [Notes](filesystem_module.md#notes)
- [See Also](filesystem_module.md#see-also)
- [Examples](filesystem_module.md#examples)

## [Synopsis](filesystem_module.md#id1)

- This module creates a filesystem.

## [Requirements](filesystem_module.md#id2)

The below requirements are needed on the host that executes this module.

- Uses specific tools related to the *fstype* for creating or resizing a filesystem (from packages e2fsprogs, xfsprogs, dosfstools, and so on).
- Uses generic tools mostly related to the Operating System (Linux or FreeBSD) or available on both, as `blkid`.
- On FreeBSD, either `util-linux` or `e2fsprogs` package is required.

## [Parameters](filesystem_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dev**  aliases: device  path / required | Target path to block device (Linux) or character device (FreeBSD) or regular file (both).  When setting Linux-specific filesystem types on FreeBSD, this module only works when applying to regular files, aka disk images.  Currently `lvm` (Linux-only) and `ufs` (FreeBSD-only) don’t support a regular file as their target *dev*.  Support for character devices on FreeBSD has been added in community.general 3.4.0. |
| **force**  boolean | If `true`, allows to create new filesystem on devices that already has filesystem.  Choices:   - `false` ← (default) - `true` |
| **fstype**  aliases: type  string | Filesystem type to be created. This option is required with *state=present* (or if *state* is omitted).  ufs support has been added in community.general 3.4.0.  Choices:   - `"btrfs"` - `"ext2"` - `"ext3"` - `"ext4"` - `"ext4dev"` - `"f2fs"` - `"lvm"` - `"ocfs2"` - `"reiserfs"` - `"xfs"` - `"vfat"` - `"swap"` - `"ufs"` |
| **opts**  string | List of options to be passed to `mkfs` command. |
| **resizefs**  boolean | If `true`, if the block device and filesystem size differ, grow the filesystem into the space.  Supported for `btrfs`, `ext2`, `ext3`, `ext4`, `ext4dev`, `f2fs`, `lvm`, `xfs`, `ufs` and `vfat` filesystems. Attempts to resize other filesystem types will fail.  XFS Will only grow if mounted. Currently, the module is based on commands from `util-linux` package to perform operations, so resizing of XFS is not supported on FreeBSD systems.  vFAT will likely fail if `fatresize < 1.04`.  Choices:   - `false` ← (default) - `true` |
| **state**  string  added in community.general 1.3.0 | If *state=present*, the filesystem is created if it doesn’t already exist, that is the default behaviour if *state* is omitted.  If *state=absent*, filesystem signatures on *dev* are wiped if it contains a filesystem (as known by `blkid`).  When *state=absent*, all other options but *dev* are ignored, and the module doesn’t fail if the device *dev* doesn’t actually exist.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](filesystem_module.md#id4)

> **Note:**
>
> - Potential filesystems on *dev* are checked using `blkid`. In case `blkid` is unable to detect a filesystem (and in case `fstyp` on FreeBSD is also unable to detect a filesystem), this filesystem is overwritten even if *force* is `false`.
> - On FreeBSD systems, both `e2fsprogs` and `util-linux` packages provide a `blkid` command that is compatible with this module. However, these packages conflict with each other, and only the `util-linux` package provides the command required to not fail when *state=absent*.
> - This module supports *check_mode*.

## [See Also](filesystem_module.md#id5)

> **See also:**
>
> [community.general.filesize](filesize_module.md#ansible-collections-community-general-filesize-module)
> :   Create a file with a given size, or resize it if it exists.
>
> [ansible.posix.mount](../../ansible/posix/mount_module.md#ansible-collections-ansible-posix-mount-module)
> :   Control active and configured mount points.

## [Examples](filesystem_module.md#id6)

```yaml+jinja
- name: Create a ext2 filesystem on /dev/sdb1
  community.general.filesystem:
    fstype: ext2
    dev: /dev/sdb1

- name: Create a ext4 filesystem on /dev/sdb1 and check disk blocks
  community.general.filesystem:
    fstype: ext4
    dev: /dev/sdb1
    opts: -cc

- name: Blank filesystem signature on /dev/sdb1
  community.general.filesystem:
    dev: /dev/sdb1
    state: absent

- name: Create a filesystem on top of a regular file
  community.general.filesystem:
    dev: /path/to/disk.img
    fstype: vfat
```

### Authors

- Alexander Bulimov (@abulimov)
- quidame (@quidame)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
