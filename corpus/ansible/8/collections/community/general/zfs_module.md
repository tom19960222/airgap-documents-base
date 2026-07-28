---
collection: ansible
version: "8"
title: "community.general.zfs module – Manage zfs"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/zfs_module.html
fetched_at: 2026-07-28T01:51:38+00:00
---
# community.general.zfs module – Manage zfs

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.zfs`.

- [Synopsis](zfs_module.md#synopsis)
- [Parameters](zfs_module.md#parameters)
- [Attributes](zfs_module.md#attributes)
- [Examples](zfs_module.md#examples)

## [Synopsis](zfs_module.md#id1)

- Manages ZFS file systems, volumes, clones and snapshots

Aliases: storage.zfs.zfs

## [Parameters](zfs_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **extra_zfs_properties**  dictionary | A dictionary of zfs properties to be set.  See the zfs(8) man page for more information.  **Default:** `{}` |
| **name**  string / required | File system, snapshot or volume name, for example `rpool/myfs`. |
| **origin**  string | Snapshot from which to create a clone. |
| **state**  string / required | Whether to create (`present`), or remove (`absent`) a file system, snapshot or volume. All parents/children will be created/destroyed as needed to reach the desired state.  **Choices:**   - `"absent"` - `"present"` |

## [Attributes](zfs_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **partial**  In certain situations it may report a task as changed that will not be reported as changed when `check_mode` is disabled.  For example, this might occur when the zpool `altroot` option is set or when a size is written using human-readable notation, such as `1M` or `1024K`, instead of as an unqualified byte count, such as `1048576`. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](zfs_module.md#id4)

```yaml+jinja
- name: Create a new file system called myfs in pool rpool with the setuid property turned off
  community.general.zfs:
    name: rpool/myfs
    state: present
    extra_zfs_properties:
      setuid: 'off'

- name: Create a new volume called myvol in pool rpool.
  community.general.zfs:
    name: rpool/myvol
    state: present
    extra_zfs_properties:
      volsize: 10M

- name: Create a snapshot of rpool/myfs file system.
  community.general.zfs:
    name: rpool/myfs@mysnapshot
    state: present

- name: Create a new file system called myfs2 with snapdir enabled
  community.general.zfs:
    name: rpool/myfs2
    state: present
    extra_zfs_properties:
      snapdir: enabled

- name: Create a new file system by cloning a snapshot
  community.general.zfs:
    name: rpool/cloned_fs
    state: present
    origin: rpool/myfs@mysnapshot

- name: Destroy a filesystem
  community.general.zfs:
    name: rpool/myfs
    state: absent
```

### Authors

- Johan Wiren (@johanwiren)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
