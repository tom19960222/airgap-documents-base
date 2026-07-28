---
collection: ansible
version: "8"
title: "ibm.spectrum_virtualize.ibm_sv_manage_snapshot module – This module manages snapshots (PiT image of a volume) on IBM Spectrum Virtualize family storage systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/spectrum_virtualize/ibm_sv_manage_snapshot_module.html
fetched_at: 2026-07-28T02:34:43+00:00
---
# ibm.spectrum_virtualize.ibm_sv_manage_snapshot module – This module manages snapshots (PiT image of a volume) on IBM Spectrum Virtualize family storage systems

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
> To use it in a playbook, specify: `ibm.spectrum_virtualize.ibm_sv_manage_snapshot`.

New in ibm.spectrum_virtualize 1.9.0

- [Synopsis](ibm_sv_manage_snapshot_module.md#synopsis)
- [Parameters](ibm_sv_manage_snapshot_module.md#parameters)
- [Notes](ibm_sv_manage_snapshot_module.md#notes)
- [Examples](ibm_sv_manage_snapshot_module.md#examples)

## [Synopsis](ibm_sv_manage_snapshot_module.md#id1)

- In this implementation, a snapshot is a mutually consistent image of the volumes in a volume group or a list of independent volume(s).
- This Ansible module provides the interface to manage snapshots through ‘addsnapshot’, ‘chsnapshot’ and ‘rmsnapshot’ Spectrum Virtualize commands.

## [Parameters](ibm_sv_manage_snapshot_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clustername**  string / required | The hostname or management IP of the Spectrum Virtualize storage system. |
| **domain**  string | Domain for the Spectrum Virtualize storage system.  Valid when hostname is used for the parameter *clustername*. |
| **ignorelegacy**  boolean | Specifies the addition of the volume snapshots although there are already legacy FlashCopy mappings using the volume as a source.  **Choices:**   - `false` ← (default) - `true` |
| **log_path**  string | Path of debug log file. |
| **name**  string | Specifies the name of a snapshot. |
| **old_name**  string | Specifies the old name of a snapshot.  Valid when *state=present*, to rename the existing snapshot. |
| **ownershipgroup**  string | Specifies the name of the ownershipgroup.  Valid when *state=present*, to update an existing snapshot. |
| **password**  string | REST API password for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **retentiondays**  integer  *added in ibm.spectrum_virtualize 1.10.0* | Specifies the retention period in days.  *safeguarded* and *retentiondays* are required together.  Applies, when *state=present* to create a safeguarded snapshot. |
| **safeguarded**  boolean  *added in ibm.spectrum_virtualize 1.10.0* | Flag to create a safeguarded snapshot.  *safeguarded* and *retentiondays* are required together.  Supported in SV build 8.5.2.0 or later.  **Choices:**   - `false` - `true` |
| **snapshot_pool**  string | Specifies the name of child pool within which the snapshot is being created. |
| **src_volume_names**  string | Specifies the name of the volumes for which the snapshots are to be created.  List of volume names can be specified with the delimiter colon.  Valid when *state=present*, to create a snapshot. |
| **src_volumegroup_name**  string | Specifies the name of the source volume group for which the snapshot is being created.  *src_volumegroup_name* and *src_volume_names* are mutually exclusive.  Required one of *src_volumegroup_name* or *src_volume_names* for creation of snapshot. |
| **state**  string / required | Creates, updates (`present`) or deletes (`absent`) a snapshot.  **Choices:**   - `"present"` - `"absent"` |
| **token**  string | The authentication token to verify a user on the Spectrum Virtualize storage system.  To generate a token, use the [ibm.spectrum_virtualize.ibm_svc_auth](ibm_svc_auth_module.md#ansible-collections-ibm-spectrum-virtualize-ibm-svc-auth-module) module. |
| **username**  string | REST API username for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](ibm_sv_manage_snapshot_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.
> - This module automates the new Snapshot function, implemented by Spectrum Virtualize, which is using a simplified management model. Any user requiring the flexibility available with legacy FlashCopy can continue to use the existing module [ibm.spectrum_virtualize.ibm_svc_manage_flashcopy](ibm_svc_manage_flashcopy_module.md#ansible-collections-ibm-spectrum-virtualize-ibm-svc-manage-flashcopy-module).
> - Snapshots created by this Ansible module are not directly accessible from the hosts. To create a new group of host accessible volumes from a snapshot, use [ibm.spectrum_virtualize.ibm_svc_manage_volumegroup](ibm_svc_manage_volumegroup_module.md#ansible-collections-ibm-spectrum-virtualize-ibm-svc-manage-volumegroup-module) module.

## [Examples](ibm_sv_manage_snapshot_module.md#id4)

```yaml+jinja
- name: Create volumegroup snapshot
  ibm.spectrum_virtualize.ibm_sv_manage_snapshot:
   clustername: '{{clustername}}'
   username: '{{username}}'
   password: '{{password}}'
   name: ansible_1
   src_volumegroup_name: volumegroup1
   snapshot_pool: Pool0Childpool0
   state: present
- name: Create volumes snapshot
  ibm.spectrum_virtualize.ibm_sv_manage_snapshot:
   clustername: '{{clustername}}'
   username: '{{username}}'
   password: '{{password}}'
   name: ansible_2
   src_volume_names: vdisk0:vdisk1
   snapshot_pool: Pool0Childpool0
   state: present
- name: Create safeguarded snapshot
  ibm.spectrum_virtualize.ibm_sv_manage_snapshot:
   clustername: '{{clustername}}'
   username: '{{username}}'
   password: '{{password}}'
   name: ansible_2
   src_volume_names: vdisk0:vdisk1
   safeguarded: true
   retentiondays: 1
   snapshot_pool: Pool0Childpool0
   state: present
- name: Update snapshot ansible_2
  ibm.spectrum_virtualize.ibm_sv_manage_snapshot:
   clustername: '{{clustername}}'
   username: '{{username}}'
   password: '{{password}}'
   name: ansible_new
   old_name: ansible_2
   ownershipgroup: ownershipgroup0
   state: present
- name: Delete volumegroup snapshot
  ibm.spectrum_virtualize.ibm_sv_manage_snapshot:
   clustername: '{{clustername}}'
   username: '{{username}}'
   password: '{{password}}'
   name: ansible_1
   src_volumegroup_name: volumegroup1
   state: absent
- name: Delete volume snapshot
  ibm.spectrum_virtualize.ibm_sv_manage_snapshot:
   clustername: '{{clustername}}'
   username: '{{username}}'
   password: '{{password}}'
   name: ansible_new
   state: absent
```

### Authors

- Sanjaikumaar M (@sanjaikumaar)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.spectrum_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.spectrum_virtualize)
