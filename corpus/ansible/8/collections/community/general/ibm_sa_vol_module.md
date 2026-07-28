---
collection: ansible
version: "8"
title: "community.general.ibm_sa_vol module – Handle volumes on IBM Spectrum Accelerate Family storage systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/ibm_sa_vol_module.html
fetched_at: 2026-07-28T01:46:19+00:00
---
# community.general.ibm_sa_vol module – Handle volumes on IBM Spectrum Accelerate Family storage systems

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
> see [Requirements](ibm_sa_vol_module.md#ansible-collections-community-general-ibm-sa-vol-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.ibm_sa_vol`.

- [Synopsis](ibm_sa_vol_module.md#synopsis)
- [Requirements](ibm_sa_vol_module.md#requirements)
- [Parameters](ibm_sa_vol_module.md#parameters)
- [Attributes](ibm_sa_vol_module.md#attributes)
- [Notes](ibm_sa_vol_module.md#notes)
- [Examples](ibm_sa_vol_module.md#examples)

## [Synopsis](ibm_sa_vol_module.md#id1)

- This module creates or deletes volumes to be used on IBM Spectrum Accelerate Family storage systems.

Aliases: storage.ibm.ibm_sa_vol

## [Requirements](ibm_sa_vol_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- pyxcli

## [Parameters](ibm_sa_vol_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **endpoints**  string / required | The hostname or management IP of Spectrum Accelerate storage system. |
| **password**  string / required | Password for username on the spectrum accelerate storage system. |
| **pool**  string | Volume pool. |
| **size**  string | Volume size. |
| **state**  string | Volume state.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **username**  string / required | Management user on the spectrum accelerate storage system. |
| **vol**  string / required | Volume name. |

## [Attributes](ibm_sa_vol_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](ibm_sa_vol_module.md#id5)

> **Note:**
>
> - This module requires pyxcli python library. Use ‘pip install pyxcli’ in order to get pyxcli.

## [Examples](ibm_sa_vol_module.md#id6)

```yaml+jinja
- name: Create a new volume.
  community.general.ibm_sa_vol:
    vol: volume_name
    pool: pool_name
    size: 17
    state: present
    username: admin
    password: secret
    endpoints: hostdev-system

- name: Delete an existing volume.
  community.general.ibm_sa_vol:
    vol: volume_name
    state: absent
    username: admin
    password: secret
    endpoints: hostdev-system
```

### Authors

- Tzur Eliyahu (@tzure)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
