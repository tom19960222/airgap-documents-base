---
collection: ansible
version: "6"
title: "community.general.lvg module – Configure LVM volume groups"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/lvg_module.html
fetched_at: 2026-07-27T17:10:37+00:00
---
# community.general.lvg module – Configure LVM volume groups

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
> To use it in a playbook, specify: `community.general.lvg`.

- [Synopsis](lvg_module.md#synopsis)
- [Parameters](lvg_module.md#parameters)
- [Notes](lvg_module.md#notes)
- [See Also](lvg_module.md#see-also)
- [Examples](lvg_module.md#examples)

## [Synopsis](lvg_module.md#id1)

- This module creates, removes or resizes volume groups.

## [Parameters](lvg_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **force**  boolean | If `true`, allows to remove volume group with logical volumes.  Choices:   - `false` ← (default) - `true` |
| **pesize**  string | The size of the physical extent. *pesize* must be a power of 2 of at least 1 sector (where the sector size is the largest sector size of the PVs currently used in the VG), or at least 128KiB.  Since Ansible 2.6, pesize can be optionally suffixed by a UNIT (k/K/m/M/g/G), default unit is megabyte.  Default: `"4"` |
| **pv_options**  string | Additional options to pass to `pvcreate` when creating the volume group.  Default: `""` |
| **pvresize**  boolean  added in community.general 0.2.0 | If `true`, resize the physical volume to the maximum available size.  Choices:   - `false` ← (default) - `true` |
| **pvs**  list / elements=string | List of comma-separated devices to use as physical devices in this volume group.  Required when creating or resizing volume group.  The module will take care of running pvcreate if needed. |
| **state**  string | Control if the volume group exists.  Choices:   - `"absent"` - `"present"` ← (default) |
| **vg**  string / required | The name of the volume group. |
| **vg_options**  string | Additional options to pass to `vgcreate` when creating the volume group.  Default: `""` |

## [Notes](lvg_module.md#id3)

> **Note:**
>
> - This module does not modify PE size for already present volume group.

## [See Also](lvg_module.md#id4)

> **See also:**
>
> [community.general.filesystem](filesystem_module.md#ansible-collections-community-general-filesystem-module)
> :   Makes a filesystem.
>
> [community.general.lvol](lvol_module.md#ansible-collections-community-general-lvol-module)
> :   Configure LVM logical volumes.
>
> [community.general.parted](parted_module.md#ansible-collections-community-general-parted-module)
> :   Configure block device partitions.

## [Examples](lvg_module.md#id5)

```yaml+jinja
- name: Create a volume group on top of /dev/sda1 with physical extent size = 32MB
  community.general.lvg:
    vg: vg.services
    pvs: /dev/sda1
    pesize: 32

- name: Create a volume group on top of /dev/sdb with physical extent size = 128KiB
  community.general.lvg:
    vg: vg.services
    pvs: /dev/sdb
    pesize: 128K

# If, for example, we already have VG vg.services on top of /dev/sdb1,
# this VG will be extended by /dev/sdc5.  Or if vg.services was created on
# top of /dev/sda5, we first extend it with /dev/sdb1 and /dev/sdc5,
# and then reduce by /dev/sda5.
- name: Create or resize a volume group on top of /dev/sdb1 and /dev/sdc5.
  community.general.lvg:
    vg: vg.services
    pvs: /dev/sdb1,/dev/sdc5

- name: Remove a volume group with name vg.services
  community.general.lvg:
    vg: vg.services
    state: absent

- name: Create a volume group on top of /dev/sda3 and resize the volume group /dev/sda3 to the maximum possible
  community.general.lvg:
    vg: resizableVG
    pvs: /dev/sda3
    pvresize: true
```

### Authors

- Alexander Bulimov (@abulimov)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
