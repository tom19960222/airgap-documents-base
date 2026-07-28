---
collection: ansible
version: "8"
title: "community.general.ibm_sa_vol_map module – Handles volume mapping on IBM Spectrum Accelerate Family storage systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/ibm_sa_vol_map_module.html
fetched_at: 2026-07-28T01:46:19+00:00
---
# community.general.ibm_sa_vol_map module – Handles volume mapping on IBM Spectrum Accelerate Family storage systems

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
> see [Requirements](ibm_sa_vol_map_module.md#ansible-collections-community-general-ibm-sa-vol-map-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.ibm_sa_vol_map`.

- [Synopsis](ibm_sa_vol_map_module.md#synopsis)
- [Requirements](ibm_sa_vol_map_module.md#requirements)
- [Parameters](ibm_sa_vol_map_module.md#parameters)
- [Attributes](ibm_sa_vol_map_module.md#attributes)
- [Notes](ibm_sa_vol_map_module.md#notes)
- [Examples](ibm_sa_vol_map_module.md#examples)

## [Synopsis](ibm_sa_vol_map_module.md#id1)

- This module maps volumes to or unmaps them from the hosts on IBM Spectrum Accelerate Family storage systems.

Aliases: storage.ibm.ibm_sa_vol_map

## [Requirements](ibm_sa_vol_map_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- pyxcli

## [Parameters](ibm_sa_vol_map_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cluster**  string | Maps the volume to a cluster. |
| **endpoints**  string / required | The hostname or management IP of Spectrum Accelerate storage system. |
| **host**  string | Maps the volume to a host. |
| **lun**  string | The LUN identifier. |
| **override**  string | Overrides the existing volume mapping. |
| **password**  string / required | Password for username on the spectrum accelerate storage system. |
| **state**  string | When the state is present the volume is mapped. When the state is absent, the volume is meant to be unmapped.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **username**  string / required | Management user on the spectrum accelerate storage system. |
| **vol**  string / required | Volume name. |

## [Attributes](ibm_sa_vol_map_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](ibm_sa_vol_map_module.md#id5)

> **Note:**
>
> - This module requires pyxcli python library. Use ‘pip install pyxcli’ in order to get pyxcli.

## [Examples](ibm_sa_vol_map_module.md#id6)

```yaml+jinja
- name: Map volume to host.
  community.general.ibm_sa_vol_map:
    vol: volume_name
    lun: 1
    host: host_name
    username: admin
    password: secret
    endpoints: hostdev-system
    state: present

- name: Map volume to cluster.
  community.general.ibm_sa_vol_map:
    vol: volume_name
    lun: 1
    cluster: cluster_name
    username: admin
    password: secret
    endpoints: hostdev-system
    state: present

- name: Unmap volume.
  community.general.ibm_sa_vol_map:
    host: host_name
    username: admin
    password: secret
    endpoints: hostdev-system
    state: absent
```

### Authors

- Tzur Eliyahu (@tzure)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
