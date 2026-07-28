---
collection: ansible
version: "8"
title: "community.general.ss_3par_cpg module – Manage HPE StoreServ 3PAR CPG"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/ss_3par_cpg_module.html
fetched_at: 2026-07-28T01:50:45+00:00
---
# community.general.ss_3par_cpg module – Manage HPE StoreServ 3PAR CPG

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
> see [Requirements](ss_3par_cpg_module.md#ansible-collections-community-general-ss-3par-cpg-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.ss_3par_cpg`.

- [Synopsis](ss_3par_cpg_module.md#synopsis)
- [Requirements](ss_3par_cpg_module.md#requirements)
- [Parameters](ss_3par_cpg_module.md#parameters)
- [Attributes](ss_3par_cpg_module.md#attributes)
- [Examples](ss_3par_cpg_module.md#examples)

## [Synopsis](ss_3par_cpg_module.md#id1)

- Create and delete CPG on HPE 3PAR.

Aliases: storage.hpe3par.ss_3par_cpg

## [Requirements](ss_3par_cpg_module.md#id2)

The below requirements are needed on the host that executes this module.

- hpe3par_sdk >= 1.0.2. Install using `pip install hpe3par_sdk`.
- WSAPI service should be enabled on the 3PAR storage array.

## [Parameters](ss_3par_cpg_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cpg_name**  string / required | Name of the CPG. |
| **disk_type**  string | Specifies that physical disks must have the specified device type.  **Choices:**   - `"FC"` - `"NL"` - `"SSD"` |
| **domain**  string | Specifies the name of the domain in which the object will reside. |
| **growth_increment**  string | Specifies the growth increment(in MiB, GiB or TiB) the amount of logical disk storage created on each auto-grow operation. |
| **growth_limit**  string | Specifies that the autogrow operation is limited to the specified storage amount that sets the growth limit(in MiB, GiB or TiB). |
| **growth_warning**  string | Specifies that the threshold(in MiB, GiB or TiB) of used logical disk space when exceeded results in a warning alert. |
| **high_availability**  string | Specifies that the layout must support the failure of one port pair, one cage, or one magazine.  **Choices:**   - `"PORT"` - `"CAGE"` - `"MAG"` |
| **raid_type**  string | Specifies the RAID type for the logical disk.  **Choices:**   - `"R0"` - `"R1"` - `"R5"` - `"R6"` |
| **secure**  boolean | Specifies whether the certificate needs to be validated while communicating.  **Choices:**   - `false` ← (default) - `true` |
| **set_size**  integer | Specifies the set size in the number of chunklets. |
| **state**  string / required | Whether the specified CPG should exist or not.  **Choices:**   - `"present"` - `"absent"` |
| **storage_system_ip**  string / required | The storage system IP address. |
| **storage_system_password**  string / required | The storage system password. |
| **storage_system_username**  string / required | The storage system user name. |

## [Attributes](ss_3par_cpg_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](ss_3par_cpg_module.md#id5)

```yaml+jinja
- name: Create CPG sample_cpg
  community.general.ss_3par_cpg:
    storage_system_ip: 10.10.10.1
    storage_system_username: username
    storage_system_password: password
    state: present
    cpg_name: sample_cpg
    domain: sample_domain
    growth_increment: 32000 MiB
    growth_limit: 64000 MiB
    growth_warning: 48000 MiB
    raid_type: R6
    set_size: 8
    high_availability: MAG
    disk_type: FC
    secure: false

- name: Delete CPG sample_cpg
  community.general.ss_3par_cpg:
    storage_system_ip: 10.10.10.1
    storage_system_username: username
    storage_system_password: password
    state: absent
    cpg_name: sample_cpg
    secure: false
```

### Authors

- Farhan Nomani (@farhan7500)
- Gautham P Hegde (@gautamphegde)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
