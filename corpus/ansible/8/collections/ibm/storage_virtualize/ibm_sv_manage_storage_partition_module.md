---
collection: ansible
version: "8"
title: "ibm.storage_virtualize.ibm_sv_manage_storage_partition module – This module manages storage partition on IBM Storage Virtualize family systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/storage_virtualize/ibm_sv_manage_storage_partition_module.html
fetched_at: 2026-07-28T02:35:21+00:00
---
# ibm.storage_virtualize.ibm_sv_manage_storage_partition module – This module manages storage partition on IBM Storage Virtualize family systems

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
> To use it in a playbook, specify: `ibm.storage_virtualize.ibm_sv_manage_storage_partition`.

New in ibm.storage_virtualize 2.1.0

- [Synopsis](ibm_sv_manage_storage_partition_module.md#synopsis)
- [Parameters](ibm_sv_manage_storage_partition_module.md#parameters)
- [Notes](ibm_sv_manage_storage_partition_module.md#notes)
- [Examples](ibm_sv_manage_storage_partition_module.md#examples)

## [Synopsis](ibm_sv_manage_storage_partition_module.md#id1)

- This Ansible module provides the interface to manage syslog servers through ‘mksyslogserver’, ‘chsyslogserver’ and ‘rmsyslogserver’ Storage Virtualize commands.
- The Policy based High Availability (HA) solution uses Storage Partitions. These partitions contain volumes, volume groups, host and host-to-volume mappings.

## [Parameters](ibm_sv_manage_storage_partition_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clustername**  string / required | The hostname or management IP of the Storage Virtualize system. |
| **deletenonpreferredmanagementobjects**  boolean | If the storage partition has a replication policy and associated objects, such as volumes, volumes groups, hosts or host mappings, one of the two *deletenonpreferredmanagementobjects* or *deletepreferredmanagementobjects* parmeters is required. If specified, the command is only permitted on the active management system, and requires that the active management system is the same as the preferred management system.  Applies when *state=absent*.  **Choices:**   - `false` - `true` |
| **deletepreferredmanagementcopy**  boolean | This parameter is to be used along with *noreplicationpolicy* parameter and active management system must NOT be the same as the preferred management system.  **Choices:**   - `false` - `true` |
| **deletepreferredmanagementobjects**  boolean | If the storage partition has a replication policy and associated objects, such as volumes, volumes groups, hosts or host mappings, one of the two *deletenonpreferredmanagementobjects* or *deletepreferredmanagementobjects* parmeters is required. If the storage partition cannot be managed at the preferred management system then *deletepreferredmanagementobjects* to be used to remove the storage partition and unassign the replication policy.  Applies when *state=absent*.  **Choices:**   - `false` - `true` |
| **domain**  string | Domain for the Storage Virtualize system.  Valid when hostname is used for the parameter *clustername*. |
| **log_path**  string | Path of debug log file. |
| **name**  string / required | Specifies the name of a storage partition. |
| **noreplicationpolicy**  boolean | Unassigns the current replication policy from the volume group. This parameter, if used without *deletepreferredmanagementcopy* parameter, is allowed only on active management system.  **Choices:**   - `false` - `true` |
| **password**  string | REST API password for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **preferredmanagementsystem**  string | Changes the preferred management system for the storage partition.  Permitted only from the system which is the active management system. |
| **replicationpolicy**  string | Specifies the replication policy for the storage partition. |
| **state**  string / required | Creates, updates (`present`) or deletes (`absent`) a storage partition.  **Choices:**   - `"present"` - `"absent"` |
| **token**  string | The authentication token to verify a user on the Storage Virtualize system.  To generate a token, use the [ibm.storage_virtualize.ibm_svc_auth](ibm_svc_auth_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-auth-module) module. |
| **username**  string | REST API username for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](ibm_sv_manage_storage_partition_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_sv_manage_storage_partition_module.md#id4)

```yaml+jinja
- name: Create Storage Partition
  ibm.storage_virtualize.ibm_sv_manage_storage_partition:
   clustername: '{{clustername}}'
   username: '{{username}}'
   password: '{{password}}'
   name: partition1
   state: present
   replicationpolicy: ha_policy_1
- name: Delete the storage partition
  ibm.storage_virtualize.ibm_sv_manage_storage_partition:
   clustername: '{{clustername}}'
   username: '{{username}}'
   password: '{{password}}'
   name: partition1
   state: absent
```

### Authors

- Shilpi Jain (@Shilpi-J)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.storage_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.storage_virtualize)
- [Report an issue](https://github.com/ansible-collections/community.REPO_NAME/issues/new/choose)
- [Communication](index.md#communication-for-ibm-storage-virtualize)
