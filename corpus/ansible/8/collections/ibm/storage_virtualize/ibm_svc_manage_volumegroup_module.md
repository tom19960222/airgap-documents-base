---
collection: ansible
version: "8"
title: "ibm.storage_virtualize.ibm_svc_manage_volumegroup module – This module manages volume groups on IBM Storage Virtualize family systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/storage_virtualize/ibm_svc_manage_volumegroup_module.html
fetched_at: 2026-07-28T02:35:40+00:00
---
# ibm.storage_virtualize.ibm_svc_manage_volumegroup module – This module manages volume groups on IBM Storage Virtualize family systems

> **Note:**
>
> This module is part of the [ibm.storage_virtualize collection](https://galaxy.ansible.com/ui/repo/published/ibm/storage_virtualize/) (version 2.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ibm.storage_virtualize`.
>
> To use it in a playbook, specify: `ibm.storage_virtualize.ibm_svc_manage_volumegroup`.

New in ibm.storage_virtualize 1.6.0

- [Synopsis](ibm_svc_manage_volumegroup_module.md#synopsis)
- [Parameters](ibm_svc_manage_volumegroup_module.md#parameters)
- [Notes](ibm_svc_manage_volumegroup_module.md#notes)
- [Examples](ibm_svc_manage_volumegroup_module.md#examples)

## [Synopsis](ibm_svc_manage_volumegroup_module.md#id1)

- Ansible interface to manage ‘mkvolumegroup’, ‘chvolumegroup’, and ‘rmvolumegroup’ commands.

## [Parameters](ibm_svc_manage_volumegroup_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clustername**  string / required | The hostname or management IP of the Storage Virtualize system. |
| **domain**  string | Domain for the Storage Virtualize system.  Valid when hostname is used for the parameter *clustername*. |
| **fromsourcegroup**  string  *added in ibm.storage_virtualize 1.9.0* | Specifies the parent volume group of the snapshot. This is used to prepopulate the new volume in the new volume group.  Valid during creation of host accessible volume group from an existing snapshot. |
| **ignoreuserfcmaps**  string  *added in ibm.storage_virtualize 1.10.0* | Allows user to create snapshots through the scheduler or manually with `addsnapshot`. This can only be used if a volume in the volume group is used as a source of a user legacy FlashCopy mapping.  Valid during creation and update of a volume group.  Supported from Storage Virtualize family systems 8.5.2.0 or later.  **Choices:**   - `"yes"` - `"no"` |
| **iogrp**  string  *added in ibm.storage_virtualize 1.9.0* | Specifies the I/O group for new volumes.  Valid during creation of host accessible volume group from an existing snapshot. |
| **log_path**  string | Path of debug log file. |
| **name**  string / required | Specifies the name for the volume group. |
| **noownershipgroup**  boolean | If specified `True`, the object is removed from the ownership group to which it belongs.  Parameters *ownershipgroup* and *noownershipgroup* are mutually exclusive.  Applies when *state=present* to modify an existing volume group.  **Choices:**   - `false` - `true` |
| **nopartition**  boolean  *added in ibm.storage_virtualize 2.1.0* | If specified `True`, removes the volume group from the storage partition.  Parameters *partition* and *nopartition* are mutually exclusive.  Applies when *state=present* to modify an existing volume group.  Supported from Storage Virtualize family systems 8.6.1.0 or later.  **Choices:**   - `false` - `true` |
| **noreplicationpolicy**  boolean  *added in ibm.storage_virtualize 1.10.0* | If specified `True`, removes the replication policy assigned to the volume group.  Parameters *replicationpolicy* and *noreplicationpolicy* are mutually exclusive.  Applies when *state=present* to modify an existing volume group.  Supported from Storage Virtualize family systems 8.5.2.1 or later.  **Choices:**   - `false` - `true` |
| **nosafeguardpolicy**  boolean | If specified `True`, removes the Safeguarded policy assigned to the volume group.  Parameters *safeguardpolicyname* and *nosafeguardpolicy* are mutually exclusive.  Applies when *state=present* to modify an existing volume group.  **Choices:**   - `false` - `true` |
| **nosnapshotpolicy**  boolean  *added in ibm.storage_virtualize 1.9.0* | If specified `True`, removes the snapshot policy assigned to the volume group.  Parameters *snapshotpolicy* and *nosnapshotpolicy* are mutually exclusive.  Applies when *state=present* to modify an existing volume group.  **Choices:**   - `false` - `true` |
| **old_name**  string  *added in ibm.storage_virtualize 2.0.0* | Specifies the old name of the volume group during renaming.  Valid when *state=present*, to rename an existing volume group. |
| **ownershipgroup**  string | Specifies the name of the ownership group to which the object is being added.  *ownershipgroup* is mutually exclusive with parameters *safeguardpolicyname* and *noownershipgroup*.  Applies when *state=present*. |
| **partition**  string  *added in ibm.storage_virtualize 2.1.0* | Specifies the name of the storage partition to be assigned to the volume group.  Applies when *state=present*.  Supported from Storage Virtualize family systems 8.6.1.0 or later. |
| **password**  string | REST API password for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **policystarttime**  string | Specifies the time when the first Safeguarded backup is to be taken.  This parameter can also be associated with snapshot policy.  *safeguardpolicyname* is required when using *policystarttime*.  The accepted format is YYMMDDHHMM.  Applies when *state=present*. |
| **pool**  string  *added in ibm.storage_virtualize 1.9.0* | Specifies the pool name where the target volumes are to be created.  Valid during creation of host accessible volume group from an existing snapshot. |
| **replicationpolicy**  string  *added in ibm.storage_virtualize 1.10.0* | Specifies the name of the replication policy to be assigned to the volume group.  Applies when *state=present*.  Supported from Storage Virtualize family systems 8.5.2.1 or later. |
| **safeguarded**  boolean  *added in ibm.storage_virtualize 1.10.0* | If specified, the snapshot policy creates safeguarded snapshots.  Should be specified along with *snapshotpolicy*.  Valid during creation and update of a volume group.  Supported from Storage Virtualize family systems 8.5.2.0 or later.  **Choices:**   - `false` ← (default) - `true` |
| **safeguardpolicyname**  string | The name of the Safeguarded policy to be assigned to the volume group.  *safeguardpolicyname* is mutually exclusive with parameters *nosafeguardpolicy* and *ownershipgroup*.  Applies when *state=present*. |
| **snapshot**  string  *added in ibm.storage_virtualize 1.9.0* | Specifies the name of the snapshot used to prepopulate the new volumes in the new volume group.  Required when creating a host accessible volume group from an existing snapshot. |
| **snapshotpolicy**  string  *added in ibm.storage_virtualize 1.9.0* | The name of the snapshot policy to be assigned to the volume group.  *snapshotpolicy* is mutually exclusive with parameters *nosnapshotpolicy* and *ownershipgroup*.  Applies when *state=present*. |
| **snapshotpolicysuspended**  string  *added in ibm.storage_virtualize 1.9.0* | Specifies whether to suspend (`yes`) or resume (`no`) the snapshot policy on this volume group.  Applies when *state=present* to modify an existing volume group.  **Choices:**   - `"yes"` - `"no"` |
| **state**  string / required | Creates or updates (`present`) or removes (`absent`) a volume group.  **Choices:**   - `"absent"` - `"present"` |
| **token**  string | The authentication token to verify a user on the Storage Virtualize system.  To generate a token, use the [ibm.storage_virtualize.ibm_svc_auth](ibm_svc_auth_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-auth-module) module. |
| **type**  string  *added in ibm.storage_virtualize 1.9.0* | Specifies the type of volume group to be created from the snapshot.  Valid during creation of host accessible volume group from an existing snapshot.  **Choices:**   - `"clone"` - `"thinclone"` |
| **username**  string | REST API username for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](ibm_svc_manage_volumegroup_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.
> - Safeguarded policy and snapshot policy cannot be used at the same time. Therefore, the parameters *snapshotpolicy* and *safeguardpolicyname* are mutually exclusive.

## [Examples](ibm_svc_manage_volumegroup_module.md#id4)

```yaml+jinja
- name: Create a new volume group
  ibm.storage_virtualize.ibm_svc_manage_volumegroup:
    clustername: "{{ clustername }}"
    domain: "{{ domain }}"
    username: "{{ username }}"
    password: "{{ password }}"
    log_path: /tmp/playbook.debug
    name: vg0
    state: present
- name: Delete a volume group
  ibm.storage_virtualize.ibm_svc_manage_volumegroup:
    clustername: "{{ clustername }}"
    domain: "{{ domain }}"
    username: "{{ username }}"
    password: "{{ password }}"
    log_path: /tmp/playbook.debug
    name: vg0
    state: absent
- name: Update existing volume group to remove ownershipgroup and attach a safeguardpolicy to it
  ibm.storage_virtualize.ibm_svc_manage_volumegroup:
    clustername: "{{ clustername }}"
    domain: "{{ domain }}"
    username: "{{ username }}"
    password: "{{ password }}"
    log_path: /tmp/playbook.debug
    name: vg0
    state: present
    noownershipgroup: True
    safeguardpolicyname: sg1
- name: Update volumegroup with snapshot policy and remove safeguarded policy
  ibm.storage_virtualize.ibm_svc_manage_volumegroup:
    clustername: "{{ clustername }}"
    domain: "{{ domain }}"
    username: "{{ username }}"
    password: "{{ password }}"
    log_path: /tmp/playbook.debug
    name: vg0
    nosafeguardpolicy: true
    snapshotpolicy: sp1
    state: present
- name: Update volumegroup with safeguarded snapshot policy and ignoreuserfcmaps
  ibm.storage_virtualize.ibm_svc_manage_volumegroup:
    clustername: "{{ clustername }}"
    domain: "{{ domain }}"
    username: "{{ username }}"
    password: "{{ password }}"
    log_path: /tmp/playbook.debug
    name: vg0
    safeguarded: true
    snapshotpolicy: sp1
    ignoreuserfcmaps: yes
    state: present
- name: Suspend snapshot policy in an existing volume group
  ibm.storage_virtualize.ibm_svc_manage_volumegroup:
    clustername: "{{ clustername }}"
    domain: "{{ domain }}"
    username: "{{ username }}"
    password: "{{ password }}"
    log_path: /tmp/playbook.debug
    name: vg0
    snapshotpolicysuspended: true
    state: present
- name: Create host accessible volume group from an existing snapshot
  ibm.storage_virtualize.ibm_svc_manage_volumegroup:
    clustername: "{{ clustername }}"
    domain: "{{ domain }}"
    username: "{{ username }}"
    password: "{{ password }}"
    log_path: /tmp/playbook.debug
    name: host_accessible_vg
    type: clone
    snapshot: snapshot0
    fromsourcegroup: vg0
    pool: Pool0
    state: present
```

### Authors

- Shilpi Jain(@Shilpi-J)
- Sanjaikumaar M (@sanjaikumaar)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.storage_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.storage_virtualize)
- [Report an issue](https://github.com/ansible-collections/community.REPO_NAME/issues/new/choose)
- [Communication](index.md#communication-for-ibm-storage-virtualize)
