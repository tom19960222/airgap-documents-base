---
collection: ansible
version: "8"
title: "ibm.storage_virtualize.ibm_sv_manage_cloud_backups module – This module configures and manages cloud backups on IBM Storage Virtualize family systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/storage_virtualize/ibm_sv_manage_cloud_backups_module.html
fetched_at: 2026-07-28T02:35:13+00:00
---
# ibm.storage_virtualize.ibm_sv_manage_cloud_backups module – This module configures and manages cloud backups on IBM Storage Virtualize family systems

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
> To use it in a playbook, specify: `ibm.storage_virtualize.ibm_sv_manage_cloud_backups`.

New in ibm.storage_virtualize 1.11.0

- [Synopsis](ibm_sv_manage_cloud_backups_module.md#synopsis)
- [Parameters](ibm_sv_manage_cloud_backups_module.md#parameters)
- [Notes](ibm_sv_manage_cloud_backups_module.md#notes)
- [Examples](ibm_sv_manage_cloud_backups_module.md#examples)

## [Synopsis](ibm_sv_manage_cloud_backups_module.md#id1)

- Ansible interface to manage backupvolume, backupvolumegroup, and rmvolumebackupgeneration commands.

## [Parameters](ibm_sv_manage_cloud_backups_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **all**  boolean | Specifies to delete all cloud backup generations.  Applies when *state=absent* to delete a backup.  The parameters *all* and *generation* are mutually exclusive.  Either *generation* or *all* is required to delete cloud backup.  **Choices:**   - `false` - `true` |
| **clustername**  string / required | The hostname or management IP of the Storage Virtualize system. |
| **domain**  string | Domain for the Storage Virtualize system.  Valid when hostname is used for the parameter *clustername*. |
| **full**  boolean | Specifies that the snapshot generation for the volume should be a full snapshot.  Applies when *state=present*.  **Choices:**   - `false` - `true` |
| **generation**  integer | Specifies the snapshot generation ID that needs to be deleted for the volume.  If the specified generation is for a snapshot operation that is in progress, that snapshot operation is canceled.  Applies when *state=absent* to delete a generation of a volume backup.  The parameters *all* and *generation* are mutually exclusive.  Either *generation* or *all* is required to delete cloud backup. |
| **log_path**  string | Path of debug log file. |
| **password**  string | REST API password for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **state**  string / required | Creates (`present`) or deletes (`absent`) a cloud backup.  **Choices:**   - `"present"` - `"absent"` |
| **token**  string | The authentication token to verify a user on the Storage Virtualize system.  To generate a token, use the [ibm.storage_virtualize.ibm_svc_auth](ibm_svc_auth_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-auth-module) module. |
| **username**  string | REST API username for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |
| **volume_name**  string | Specifies the volume name for the volume being backed up.  The parameters *volume_name* and *volumegroup_name* are mutually exclusive. |
| **volume_UID**  string | Specifies the volume UID to delete a cloud backup of the volume.  The value for a volume UID must be a value in the range 0-32.  The parameters *volume_UID* and *volume_name* are mutually exclusive.  Applies when *state=absent* to delete cloud backups. |
| **volumegroup_name**  string | Specifies the volumegroup name for the volume to back up.  The parameters *volume_name* and *volumegroup_name* are mutually exclusive.  Applies when *state=present* to create cloud backups of all the volume group members.  Cloud backup must be enabled on all the volume group members to execute this. |

## [Notes](ibm_sv_manage_cloud_backups_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_sv_manage_cloud_backups_module.md#id4)

```yaml+jinja
- name: Create cloud backup of volume
  ibm.storage_virtualize.ibm_sv_manage_cloud_backups:
    clustername: "{{cluster}}"
    username: "{{username}}"
    password: "{{password}}"
    volume_name: vol1
    full: true
    state: present
- name: Create cloud backup of volumegroup
  ibm.storage_virtualize.ibm_sv_manage_cloud_backups:
    clustername: "{{cluster}}"
    username: "{{username}}"
    password: "{{password}}"
    volumegroup_name: VG1
    full: true
    state: present
- name: Delete cloud backup
  ibm.storage_virtualize.ibm_sv_manage_cloud_backups:
    clustername: "{{cluster}}"
    username: "{{username}}"
    password: "{{password}}"
    volume_UID: 6005076400B70038E00000000000001C
    all: true
    state: absent
```

### Authors

- Sanjaikumaar M (@sanjaikumaar)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.storage_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.storage_virtualize)
- [Report an issue](https://github.com/ansible-collections/community.REPO_NAME/issues/new/choose)
- [Communication](index.md#communication-for-ibm-storage-virtualize)
