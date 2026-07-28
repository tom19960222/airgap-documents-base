---
collection: ansible
version: "6"
title: "community.general.aix_filesystem module – Configure LVM and NFS file systems for AIX"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/aix_filesystem_module.html
fetched_at: 2026-07-27T17:08:00+00:00
---
# community.general.aix_filesystem module – Configure LVM and NFS file systems for AIX

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.aix_filesystem`.

- [Synopsis](aix_filesystem_module.md#synopsis)
- [Parameters](aix_filesystem_module.md#parameters)
- [Notes](aix_filesystem_module.md#notes)
- [Examples](aix_filesystem_module.md#examples)
- [Return Values](aix_filesystem_module.md#return-values)

## [Synopsis](aix_filesystem_module.md#id1)

- This module creates, removes, mount and unmount LVM and NFS file system for AIX using `/etc/filesystems`.
- For LVM file systems is possible to resize a file system.

## [Parameters](aix_filesystem_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **account_subsystem**  boolean | Specifies whether the file system is to be processed by the accounting subsystem.  Choices:   - `false` ← (default) - `true` |
| **attributes**  list / elements=string | Specifies attributes for files system separated by comma.  Default: `["agblksize='4096'", "isnapshot='no'"]` |
| **auto_mount**  boolean | File system is automatically mounted at system restart.  Choices:   - `false` - `true` ← (default) |
| **device**  string | Logical volume (LV) device name or remote export device to create a NFS file system.  It is used to create a file system on an already existing logical volume or the exported NFS file system.  If not mentioned a new logical volume name will be created following AIX standards (LVM). |
| **filesystem**  string / required | Specifies the mount point, which is the directory where the file system will be mounted. |
| **fs_type**  string | Specifies the virtual file system type.  Default: `"jfs2"` |
| **mount_group**  string | Specifies the mount group. |
| **nfs_server**  string | Specifies a Network File System (NFS) server. |
| **permissions**  string | Set file system permissions. `rw` (read-write) or `ro` (read-only).  Choices:   - `"ro"` - `"rw"` ← (default) |
| **rm_mount_point**  boolean | Removes the mount point directory when used with state `absent`.  Choices:   - `false` ← (default) - `true` |
| **size**  string | Specifies the file system size.  For already `present` it will be resized.  512-byte blocks, Megabytes or Gigabytes. If the value has M specified it will be in Megabytes. If the value has G specified it will be in Gigabytes.  If no M or G the value will be 512-byte blocks.  If “+” is specified in begin of value, the value will be added.  If “-” is specified in begin of value, the value will be removed.  If “+” or “-” is not specified, the total value will be the specified.  Size will respects the LVM AIX standards. |
| **state**  string | Controls the file system state.  `present` check if file system exists, creates or resize.  `absent` removes existing file system if already `unmounted`.  `mounted` checks if the file system is mounted or mount the file system.  `unmounted` check if the file system is unmounted or unmount the file system.  Choices:   - `"absent"` - `"mounted"` - `"present"` ← (default) - `"unmounted"` |
| **vg**  string | Specifies an existing volume group (VG). |

## [Notes](aix_filesystem_module.md#id3)

> **Note:**
>
> - For more `attributes`, please check “crfs” AIX manual.

## [Examples](aix_filesystem_module.md#id4)

```yaml+jinja
- name: Create filesystem in a previously defined logical volume.
  community.general.aix_filesystem:
    device: testlv
    filesystem: /testfs
    state: present

- name: Creating NFS filesystem from nfshost.
  community.general.aix_filesystem:
    device: /home/ftp
    nfs_server: nfshost
    filesystem: /home/ftp
    state: present

- name: Creating a new file system without a previously logical volume.
  community.general.aix_filesystem:
    filesystem: /newfs
    size: 1G
    state: present
    vg: datavg

- name: Unmounting /testfs.
  community.general.aix_filesystem:
    filesystem: /testfs
    state: unmounted

- name: Resizing /mksysb to +512M.
  community.general.aix_filesystem:
    filesystem: /mksysb
    size: +512M
    state: present

- name: Resizing /mksysb to 11G.
  community.general.aix_filesystem:
    filesystem: /mksysb
    size: 11G
    state: present

- name: Resizing /mksysb to -2G.
  community.general.aix_filesystem:
    filesystem: /mksysb
    size: -2G
    state: present

- name: Remove NFS filesystem /home/ftp.
  community.general.aix_filesystem:
    filesystem: /home/ftp
    rm_mount_point: true
    state: absent

- name: Remove /newfs.
  community.general.aix_filesystem:
    filesystem: /newfs
    rm_mount_point: true
    state: absent
```

## [Return Values](aix_filesystem_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Return changed for aix_filesystems actions as true or false.  Returned: always |
| **msg**  string | Return message regarding the action.  Returned: always |

### Authors

- Kairo Araujo (@kairoaraujo)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
