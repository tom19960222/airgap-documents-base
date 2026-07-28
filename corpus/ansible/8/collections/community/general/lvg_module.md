---
collection: ansible
version: "8"
title: "community.general.lvg module – Configure LVM volume groups"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/lvg_module.html
fetched_at: 2026-07-28T01:47:36+00:00
---
# community.general.lvg module – Configure LVM volume groups

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
> To use it in a playbook, specify: `community.general.lvg`.

- [Synopsis](lvg_module.md#synopsis)
- [Parameters](lvg_module.md#parameters)
- [Attributes](lvg_module.md#attributes)
- [Notes](lvg_module.md#notes)
- [See Also](lvg_module.md#see-also)
- [Examples](lvg_module.md#examples)

## [Synopsis](lvg_module.md#id1)

- This module creates, removes or resizes volume groups.

Aliases: system.lvg

## [Parameters](lvg_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **force**  boolean | If `true`, allows to remove volume group with logical volumes.  **Choices:**   - `false` ← (default) - `true` |
| **pesize**  string | The size of the physical extent. `pesize` must be a power of 2 of at least 1 sector (where the sector size is the largest sector size of the PVs currently used in the VG), or at least 128KiB.  Since Ansible 2.6, pesize can be optionally suffixed by a UNIT (k/K/m/M/g/G), default unit is megabyte.  **Default:** `"4"` |
| **pv_options**  string | Additional options to pass to `pvcreate` when creating the volume group.  **Default:** `""` |
| **pvresize**  boolean  *added in community.general 0.2.0* | If `true`, resize the physical volume to the maximum available size.  **Choices:**   - `false` ← (default) - `true` |
| **pvs**  list / elements=string | List of comma-separated devices to use as physical devices in this volume group.  Required when creating or resizing volume group.  The module will take care of running pvcreate if needed. |
| **reset_pv_uuid**  boolean  *added in community.general 7.1.0* | Whether the volume group’s physical volumes’ UUIDs are regenerated.  This is **not idempotent**. Specifying this parameter always results in a change.  **Choices:**   - `false` ← (default) - `true` |
| **reset_vg_uuid**  boolean  *added in community.general 7.1.0* | Whether the volume group’s UUID is regenerated.  This is **not idempotent**. Specifying this parameter always results in a change.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | Control if the volume group exists and it’s state.  The states `active` and `inactive` implies `present` state. Added in 7.1.0  If `active` or `inactive`, the module manages the VG’s logical volumes current state. The module also handles the VG’s autoactivation state if supported unless when creating a volume group and the autoactivation option specified in `vg_options`.  **Choices:**   - `"absent"` - `"present"` ← (default) - `"active"` - `"inactive"` |
| **vg**  string / required | The name of the volume group. |
| **vg_options**  string | Additional options to pass to `vgcreate` when creating the volume group.  **Default:** `""` |

## [Attributes](lvg_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](lvg_module.md#id4)

> **Note:**
>
> - This module does not modify PE size for already present volume group.

## [See Also](lvg_module.md#id5)

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

## [Examples](lvg_module.md#id6)

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

- name: Deactivate a volume group
  community.general.lvg:
    state: inactive
    vg: vg.services

- name: Activate a volume group
  community.general.lvg:
    state: active
    vg: vg.services

- name: Reset a volume group UUID
  community.general.lvg:
    state: inactive
    vg: vg.services
    reset_vg_uuid: true

- name: Reset both volume group and pv UUID
  community.general.lvg:
    state: inactive
    vg: vg.services
    pvs: /dev/sdb1,/dev/sdc5
    reset_vg_uuid: true
    reset_pv_uuid: true
```

### Authors

- Alexander Bulimov (@abulimov)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
