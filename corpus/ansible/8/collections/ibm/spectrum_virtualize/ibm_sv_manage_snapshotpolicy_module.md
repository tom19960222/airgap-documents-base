---
collection: ansible
version: "8"
title: "ibm.spectrum_virtualize.ibm_sv_manage_snapshotpolicy module – This module manages snapshot policy configuration on IBM Spectrum Virtualize family storage systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/spectrum_virtualize/ibm_sv_manage_snapshotpolicy_module.html
fetched_at: 2026-07-28T02:34:44+00:00
---
# ibm.spectrum_virtualize.ibm_sv_manage_snapshotpolicy module – This module manages snapshot policy configuration on IBM Spectrum Virtualize family storage systems

> **Note:**
>
> This module is part of the [ibm.spectrum_virtualize collection](https://galaxy.ansible.com/ui/repo/published/ibm/spectrum_virtualize/) (version 1.12.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ibm.spectrum_virtualize`.
>
> To use it in a playbook, specify: `ibm.spectrum_virtualize.ibm_sv_manage_snapshotpolicy`.

New in ibm.spectrum_virtualize 1.9.0

- [Synopsis](ibm_sv_manage_snapshotpolicy_module.md#synopsis)
- [Parameters](ibm_sv_manage_snapshotpolicy_module.md#parameters)
- [Notes](ibm_sv_manage_snapshotpolicy_module.md#notes)
- [Examples](ibm_sv_manage_snapshotpolicy_module.md#examples)

## [Synopsis](ibm_sv_manage_snapshotpolicy_module.md#id1)

- Ansible interface to manage ‘mksnapshotpolicy’ and ‘rmsnapshotpolicy’ snapshot policy commands.
- Snapshot policy is introduced in IBM Spectrum Virtualize 8.5.1.0.

## [Parameters](ibm_sv_manage_snapshotpolicy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **backupinterval**  string | Specifies the backup interval.  Applies when *state=present*. |
| **backupstarttime**  string | Specifies the start time of backup in the format YYMMDDHHMM.  Applies when *state=present*. |
| **backupunit**  string | Specifies the backup unit in mentioned metric.  Applies when *state=present*.  **Choices:**   - `"minute"` - `"hour"` - `"day"` - `"week"` - `"month"` |
| **clustername**  string / required | The hostname or management IP of the Spectrum Virtualize storage system. |
| **domain**  string | Domain for the Spectrum Virtualize storage system.  Valid when hostname is used for the parameter *clustername*. |
| **log_path**  string | Path of debug log file. |
| **name**  string | Specifies a unique name of the snapshot policy.  Not applicable when *state=suspend* or *state=resume*. |
| **password**  string | REST API password for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **removefromvolumegroups**  boolean | Specify to remove the volume group association from the snapshot policy.  Applies when *state=absent*.  This option is allowed only for SecurityAdmin users.  **Choices:**   - `false` - `true` |
| **retentiondays**  string | Specifies the retention days for the backup.  Applies when *state=present*. |
| **state**  string / required | Creates (`present`) or deletes (`absent`) a snapshot policy.  Resume (`resume`) or suspend (`suspend`) the snapshot policy, system-wide.  **Choices:**   - `"present"` - `"absent"` - `"suspend"` - `"resume"` |
| **token**  string | The authentication token to verify a user on the Spectrum Virtualize storage system.  To generate a token, use the [ibm.spectrum_virtualize.ibm_svc_auth](ibm_svc_auth_module.md#ansible-collections-ibm-spectrum-virtualize-ibm-svc-auth-module) module. |
| **username**  string | REST API username for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](ibm_sv_manage_snapshotpolicy_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_sv_manage_snapshotpolicy_module.md#id4)

```yaml+jinja
- name: Create snapshot policy
  ibm.spectrum_virtualize.ibm_sv_manage_snapshotpolicy:
    clustername: "{{cluster}}"
    username: "{{username}}"
    password: "{{password}}"
    name: policy0
    backupunit: day
    backupinterval: 1
    backupstarttime: 2102281800
    retentiondays: 15
    state: present
- name: Suspend snapshot policy functionality
  ibm.spectrum_virtualize.ibm_sv_manage_snapshotpolicy:
    clustername: "{{cluster}}"
    username: "{{username}}"
    password: "{{password}}"
    state: suspend
- name: Resume snapshot policy functionality
  ibm.spectrum_virtualize.ibm_sv_manage_snapshotpolicy:
    clustername: "{{cluster}}"
    username: "{{username}}"
    password: "{{password}}"
    state: resume
- name: Delete snapshot policy
  ibm.spectrum_virtualize.ibm_sv_manage_snapshotpolicy:
    clustername: "{{cluster}}"
    username: "{{username}}"
    password: "{{password}}"
    name: policy0
    state: absent
```

### Authors

- Shilpi Jain(@Shilpi-J)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.spectrum_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.spectrum_virtualize)
