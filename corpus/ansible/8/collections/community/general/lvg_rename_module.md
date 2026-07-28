---
collection: ansible
version: "8"
title: "community.general.lvg_rename module – Renames LVM volume groups"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/lvg_rename_module.html
fetched_at: 2026-07-28T01:47:37+00:00
---
# community.general.lvg_rename module – Renames LVM volume groups

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
> To use it in a playbook, specify: `community.general.lvg_rename`.

New in community.general 7.1.0

- [Synopsis](lvg_rename_module.md#synopsis)
- [Parameters](lvg_rename_module.md#parameters)
- [Attributes](lvg_rename_module.md#attributes)
- [Notes](lvg_rename_module.md#notes)
- [See Also](lvg_rename_module.md#see-also)
- [Examples](lvg_rename_module.md#examples)

## [Synopsis](lvg_rename_module.md#id1)

- This module renames volume groups using the `vgchange` command.

## [Parameters](lvg_rename_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **vg**  string / required | The name or UUID of the source VG.  See `vgrename(8)` for valid values. |
| **vg_new**  string / required | The new name of the VG.  See `lvm(8)` for valid names. |

## [Attributes](lvg_rename_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](lvg_rename_module.md#id4)

> **Note:**
>
> - This module does not modify VG renaming-related configurations like `fstab` entries or boot parameters.

## [See Also](lvg_rename_module.md#id5)

> **See also:**
>
> [community.general.lvg](lvg_module.md#ansible-collections-community-general-lvg-module)
> :   Configure LVM volume groups.

## [Examples](lvg_rename_module.md#id6)

```yaml+jinja
- name: Rename a VG by name
  community.general.lvg_rename:
    vg: vg_orig_name
    vg_new: vg_new_name

- name: Rename a VG by UUID
  community.general.lvg_rename:
    vg_uuid: SNgd0Q-rPYa-dPB8-U1g6-4WZI-qHID-N7y9Vj
    vg_new: vg_new_name
```

### Authors

- Laszlo Szomor (@lszomor)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
