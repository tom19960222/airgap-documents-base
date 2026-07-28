---
collection: ansible
version: "8"
title: "community.general.aix_lvol module – Configure AIX LVM logical volumes"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/aix_lvol_module.html
fetched_at: 2026-07-28T01:44:35+00:00
---
# community.general.aix_lvol module – Configure AIX LVM logical volumes

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
> To use it in a playbook, specify: `community.general.aix_lvol`.

- [Synopsis](aix_lvol_module.md#synopsis)
- [Parameters](aix_lvol_module.md#parameters)
- [Attributes](aix_lvol_module.md#attributes)
- [Examples](aix_lvol_module.md#examples)
- [Return Values](aix_lvol_module.md#return-values)

## [Synopsis](aix_lvol_module.md#id1)

- This module creates, removes or resizes AIX logical volumes. Inspired by lvol module.

Aliases: system.aix_lvol

## [Parameters](aix_lvol_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **copies**  integer | The number of copies of the logical volume.  Maximum copies are 3.  **Default:** `1` |
| **lv**  string / required | The name of the logical volume. |
| **lv_type**  string | The type of the logical volume.  **Default:** `"jfs2"` |
| **opts**  string | Free-form options to be passed to the mklv command.  **Default:** `""` |
| **policy**  string | Sets the interphysical volume allocation policy.  `maximum` allocates logical partitions across the maximum number of physical volumes.  `minimum` allocates logical partitions across the minimum number of physical volumes.  **Choices:**   - `"maximum"` ← (default) - `"minimum"` |
| **pvs**  list / elements=string | A list of physical volumes, for example `hdisk1,hdisk2`.  **Default:** `[]` |
| **size**  string | The size of the logical volume with one of the [MGT] units. |
| **state**  string | Control if the logical volume exists. If `present` and the volume does not already exist then the `size` option is required.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **vg**  string / required | The volume group this logical volume is part of. |

## [Attributes](aix_lvol_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](aix_lvol_module.md#id4)

```yaml+jinja
- name: Create a logical volume of 512M
  community.general.aix_lvol:
    vg: testvg
    lv: testlv
    size: 512M

- name: Create a logical volume of 512M with disks hdisk1 and hdisk2
  community.general.aix_lvol:
    vg: testvg
    lv: test2lv
    size: 512M
    pvs: [ hdisk1, hdisk2 ]

- name: Create a logical volume of 512M mirrored
  community.general.aix_lvol:
    vg: testvg
    lv: test3lv
    size: 512M
    copies: 2

- name: Create a logical volume of 1G with a minimum placement policy
  community.general.aix_lvol:
    vg: rootvg
    lv: test4lv
    size: 1G
    policy: minimum

- name: Create a logical volume with special options like mirror pool
  community.general.aix_lvol:
    vg: testvg
    lv: testlv
    size: 512M
    opts: -p copy1=poolA -p copy2=poolB

- name: Extend the logical volume to 1200M
  community.general.aix_lvol:
    vg: testvg
    lv: test4lv
    size: 1200M

- name: Remove the logical volume
  community.general.aix_lvol:
    vg: testvg
    lv: testlv
    state: absent
```

## [Return Values](aix_lvol_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | A friendly message describing the task result.  **Returned:** always  **Sample:** `"Logical volume testlv created."` |

### Authors

- Alain Dejoux (@adejoux)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
