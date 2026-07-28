---
collection: ansible
version: "8"
title: "ibm.spectrum_virtualize.ibm_sv_restore_cloud_backup module – This module restores the cloud backup on IBM Spectrum Virtualize family storage systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/spectrum_virtualize/ibm_sv_restore_cloud_backup_module.html
fetched_at: 2026-07-28T02:34:46+00:00
---
# ibm.spectrum_virtualize.ibm_sv_restore_cloud_backup module – This module restores the cloud backup on IBM Spectrum Virtualize family storage systems

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
> To use it in a playbook, specify: `ibm.spectrum_virtualize.ibm_sv_restore_cloud_backup`.

New in ibm.spectrum_virtualize 1.11.0

- [Synopsis](ibm_sv_restore_cloud_backup_module.md#synopsis)
- [Parameters](ibm_sv_restore_cloud_backup_module.md#parameters)
- [Notes](ibm_sv_restore_cloud_backup_module.md#notes)
- [Examples](ibm_sv_restore_cloud_backup_module.md#examples)

## [Synopsis](ibm_sv_restore_cloud_backup_module.md#id1)

- Ansible interface to manage restorevolume command.

## [Parameters](ibm_sv_restore_cloud_backup_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cancel**  boolean | Specifies to cancel the restore operation.  **Choices:**   - `false` - `true` |
| **clustername**  string / required | The hostname or management IP of the Spectrum Virtualize storage system. |
| **deletelatergenerations**  boolean | Specifies that all backup generations should be deleted after the generation is restored.  **Choices:**   - `false` - `true` |
| **domain**  string | Domain for the Spectrum Virtualize storage system.  Valid when hostname is used for the parameter *clustername*. |
| **generation**  integer | Specifies the snapshot generation to restore. The value must be a number. |
| **log_path**  string | Path of debug log file. |
| **password**  string | REST API password for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **restoreuid**  boolean | Specifies the UID of the restored volume should be set to the UID of the volume snapshot that is being restored.  This parameter can be used only with *source_volume_uid*.  The *restoreuid* parameter is not supported if cloud account is in import mode.  **Choices:**   - `false` - `true` |
| **source_volume_uid**  string | Specifies the volume snapshot to restore (specified by volume UID).  This parameter is required to restore a backup from a different volume.  Specified UID must be different from the UID of the volume being restored. |
| **target_volume_name**  string / required | Specifies the volume name to restore onto. |
| **token**  string | The authentication token to verify a user on the Spectrum Virtualize storage system.  To generate a token, use the [ibm.spectrum_virtualize.ibm_svc_auth](ibm_svc_auth_module.md#ansible-collections-ibm-spectrum-virtualize-ibm-svc-auth-module) module. |
| **username**  string | REST API username for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](ibm_sv_restore_cloud_backup_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_sv_restore_cloud_backup_module.md#id4)

```yaml+jinja
- name: Restore cloud backup
  ibm.spectrum_virtualize.ibm_sv_restore_cloud_backup:
    clustername: "{{cluster_A}}"
    username: "{{username_A}}"
    password: "{{password_A}}"
    target_volume_name: vol1
    source_volume_uid: 6005076400B70038E00000000000001C
    generation: 1
- name: Restore cloud backup to different cluster
  ibm.spectrum_virtualize.ibm_sv_restore_cloud_backup:
    clustername: "{{cluster_B}}"
    username: "{{username_B}}"
    password: "{{password_B}}"
    target_volume_name: vol2
    source_volume_uid: 6005076400B70038E00000000000001C
    generation: 1
- name: Cancel restore operation
  ibm.spectrum_virtualize.ibm_sv_restore_cloud_backup:
    clustername: "{{cluster_A}}"
    username: "{{username_A}}"
    password: "{{password_A}}"
    target_volume_name: vol1
    cancel: true
```

### Authors

- Sanjaikumaar M (@sanjaikumaar)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.spectrum_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.spectrum_virtualize)
