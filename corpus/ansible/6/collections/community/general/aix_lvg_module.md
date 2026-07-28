---
collection: ansible
version: "6"
title: "community.general.aix_lvg module – Manage LVM volume groups on AIX"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/aix_lvg_module.html
fetched_at: 2026-07-27T17:08:01+00:00
---
# community.general.aix_lvg module – Manage LVM volume groups on AIX

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
> To use it in a playbook, specify: `community.general.aix_lvg`.

- [Synopsis](aix_lvg_module.md#synopsis)
- [Parameters](aix_lvg_module.md#parameters)
- [Notes](aix_lvg_module.md#notes)
- [Examples](aix_lvg_module.md#examples)

## [Synopsis](aix_lvg_module.md#id1)

- This module creates, removes or resize volume groups on AIX LVM.

## [Parameters](aix_lvg_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **force**  boolean | Force volume group creation.  Choices:   - `false` ← (default) - `true` |
| **pp_size**  integer | The size of the physical partition in megabytes. |
| **pvs**  list / elements=string | List of comma-separated devices to use as physical devices in this volume group.  Required when creating or extending (`present` state) the volume group.  If not informed reducing (`absent` state) the volume group will be removed. |
| **state**  string | Control if the volume group exists and volume group AIX state varyonvg `varyon` or varyoffvg `varyoff`.  Choices:   - `"absent"` - `"present"` ← (default) - `"varyoff"` - `"varyon"` |
| **vg**  string / required | The name of the volume group. |
| **vg_type**  string | The type of the volume group.  Choices:   - `"big"` - `"normal"` ← (default) - `"scalable"` |

## [Notes](aix_lvg_module.md#id3)

> **Note:**
>
> - AIX will permit remove VG only if all LV/Filesystems are not busy.
> - Module does not modify PP size for already present volume group.

## [Examples](aix_lvg_module.md#id4)

```yaml+jinja
- name: Create a volume group datavg
  community.general.aix_lvg:
    vg: datavg
    pp_size: 128
    vg_type: scalable
    state: present

- name: Removing a volume group datavg
  community.general.aix_lvg:
    vg: datavg
    state: absent

- name: Extending rootvg
  community.general.aix_lvg:
    vg: rootvg
    pvs: hdisk1
    state: present

- name: Reducing rootvg
  community.general.aix_lvg:
    vg: rootvg
    pvs: hdisk1
    state: absent
```

### Authors

- Kairo Araujo (@kairoaraujo)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
