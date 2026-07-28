---
collection: ansible
version: "8"
title: "community.general.lvol module – Configure LVM logical volumes"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/lvol_module.html
fetched_at: 2026-07-28T01:47:38+00:00
---
# community.general.lvol module – Configure LVM logical volumes

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
> To use it in a playbook, specify: `community.general.lvol`.

- [Synopsis](lvol_module.md#synopsis)
- [Parameters](lvol_module.md#parameters)
- [Attributes](lvol_module.md#attributes)
- [Notes](lvol_module.md#notes)
- [Examples](lvol_module.md#examples)

## [Synopsis](lvol_module.md#id1)

- This module creates, removes or resizes logical volumes.

Aliases: system.lvol

## [Parameters](lvol_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **active**  boolean | Whether the volume is active and visible to the host.  **Choices:**   - `false` - `true` ← (default) |
| **force**  boolean | Shrink or remove operations of volumes requires this switch. Ensures that that filesystems get never corrupted/destroyed by mistake.  **Choices:**   - `false` ← (default) - `true` |
| **lv**  string | The name of the logical volume. |
| **opts**  string | Free-form options to be passed to the lvcreate command. |
| **pvs**  string | Comma separated list of physical volumes (e.g. /dev/sda,/dev/sdb). |
| **resizefs**  boolean | Resize the underlying filesystem together with the logical volume.  Supported for `ext2`, `ext3`, `ext4`, `reiserfs` and `XFS` filesystems. Attempts to resize other filesystem types will fail.  **Choices:**   - `false` ← (default) - `true` |
| **shrink**  boolean | Shrink if current size is higher than size requested.  **Choices:**   - `false` - `true` ← (default) |
| **size**  string | The size of the logical volume, according to lvcreate(8) –size, by default in megabytes or optionally with one of [bBsSkKmMgGtTpPeE] units; or according to lvcreate(8) –extents as a percentage of [VG|PVS|FREE|ORIGIN]; Float values must begin with a digit.  When resizing, apart from specifying an absolute size you may, according to lvextend(8)|lvreduce(8) `--size`, specify the amount to extend the logical volume with the prefix `+` or the amount to reduce the logical volume by with prefix `-`.  Resizing using `+` or `-` was not supported prior to community.general 3.0.0.  Please note that when using `+`, `-`, or percentage of FREE, the module is **not idempotent**. |
| **snapshot**  string | The name of a snapshot volume to be configured. When creating a snapshot volume, the `lv` parameter specifies the origin volume. |
| **state**  string | Control if the logical volume exists. If `present` and the volume does not already exist then the `size` option is required.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **thinpool**  string | The thin pool volume name. When you want to create a thin provisioned volume, specify a thin pool volume name. |
| **vg**  string / required | The volume group this logical volume is part of. |

## [Attributes](lvol_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](lvol_module.md#id4)

> **Note:**
>
> - You must specify lv (when managing the state of logical volumes) or thinpool (when managing a thin provisioned volume).

## [Examples](lvol_module.md#id5)

```yaml+jinja
- name: Create a logical volume of 512m
  community.general.lvol:
    vg: firefly
    lv: test
    size: 512

- name: Create a logical volume of 512m with disks /dev/sda and /dev/sdb
  community.general.lvol:
    vg: firefly
    lv: test
    size: 512
    pvs: /dev/sda,/dev/sdb

- name: Create cache pool logical volume
  community.general.lvol:
    vg: firefly
    lv: lvcache
    size: 512m
    opts: --type cache-pool

- name: Create a logical volume of 512g.
  community.general.lvol:
    vg: firefly
    lv: test
    size: 512g

- name: Create a logical volume the size of all remaining space in the volume group
  community.general.lvol:
    vg: firefly
    lv: test
    size: 100%FREE

- name: Create a logical volume with special options
  community.general.lvol:
    vg: firefly
    lv: test
    size: 512g
    opts: -r 16

- name: Extend the logical volume to 1024m.
  community.general.lvol:
    vg: firefly
    lv: test
    size: 1024

- name: Extend the logical volume to consume all remaining space in the volume group
  community.general.lvol:
    vg: firefly
    lv: test
    size: +100%FREE

- name: Extend the logical volume by given space
  community.general.lvol:
    vg: firefly
    lv: test
    size: +512M

- name: Extend the logical volume to take all remaining space of the PVs and resize the underlying filesystem
  community.general.lvol:
    vg: firefly
    lv: test
    size: 100%PVS
    resizefs: true

- name: Resize the logical volume to % of VG
  community.general.lvol:
    vg: firefly
    lv: test
    size: 80%VG
    force: true

- name: Reduce the logical volume to 512m
  community.general.lvol:
    vg: firefly
    lv: test
    size: 512
    force: true

- name: Reduce the logical volume by given space
  community.general.lvol:
    vg: firefly
    lv: test
    size: -512M
    force: true

- name: Set the logical volume to 512m and do not try to shrink if size is lower than current one
  community.general.lvol:
    vg: firefly
    lv: test
    size: 512
    shrink: false

- name: Remove the logical volume.
  community.general.lvol:
    vg: firefly
    lv: test
    state: absent
    force: true

- name: Create a snapshot volume of the test logical volume.
  community.general.lvol:
    vg: firefly
    lv: test
    snapshot: snap1
    size: 100m

- name: Deactivate a logical volume
  community.general.lvol:
    vg: firefly
    lv: test
    active: false

- name: Create a deactivated logical volume
  community.general.lvol:
    vg: firefly
    lv: test
    size: 512g
    active: false

- name: Create a thin pool of 512g
  community.general.lvol:
    vg: firefly
    thinpool: testpool
    size: 512g

- name: Create a thin volume of 128g
  community.general.lvol:
    vg: firefly
    lv: test
    thinpool: testpool
    size: 128g
```

### Authors

- Jeroen Hoekx (@jhoekx)
- Alexander Bulimov (@abulimov)
- Raoul Baudach (@unkaputtbar112)
- Ziga Kern (@zigaSRC)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
