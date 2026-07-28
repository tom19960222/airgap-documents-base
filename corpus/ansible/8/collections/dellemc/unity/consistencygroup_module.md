---
collection: ansible
version: "8"
title: "dellemc.unity.consistencygroup module – Manage consistency groups on Unity storage system"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/unity/consistencygroup_module.html
fetched_at: 2026-07-28T02:05:21+00:00
---
# dellemc.unity.consistencygroup module – Manage consistency groups on Unity storage system

> **Note:**
>
> This module is part of the [dellemc.unity collection](https://galaxy.ansible.com/ui/repo/published/dellemc/unity/) (version 1.7.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.unity`.
> You need further requirements to be able to use this module,
> see [Requirements](consistencygroup_module.md#ansible-collections-dellemc-unity-consistencygroup-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.unity.consistencygroup`.

New in dellemc.unity 1.1.0

- [Synopsis](consistencygroup_module.md#synopsis)
- [Requirements](consistencygroup_module.md#requirements)
- [Parameters](consistencygroup_module.md#parameters)
- [Notes](consistencygroup_module.md#notes)
- [Examples](consistencygroup_module.md#examples)
- [Return Values](consistencygroup_module.md#return-values)

## [Synopsis](consistencygroup_module.md#id1)

- Managing the consistency group on the Unity storage system includes creating new consistency group, adding volumes to consistency group, removing volumes from consistency group, mapping hosts to consistency group, unmapping hosts from consistency group, renaming consistency group, modifying attributes of consistency group, enabling replication in consistency group, disabling replication in consistency group and deleting consistency group.

Aliases: dellemc_unity_consistencygroup

## [Requirements](consistencygroup_module.md#id2)

The below requirements are needed on the host that executes this module.

- A Dell Unity Storage device version 5.1 or later.
- Ansible-core 2.13 or later.
- Python 3.9, 3.10 or 3.11.
- Storops Python SDK 1.2.11.

## [Parameters](consistencygroup_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cg_id**  string | The ID of the consistency group.  It can be used only for get, modify, add/remove volumes, or delete operations. |
| **cg_name**  string | The name of the consistency group.  It is mandatory for the create operation.  Specify either *cg_name* or *cg_id* (but not both) for any operation. |
| **description**  string | Description of the consistency group. |
| **hosts**  list / elements=dictionary | This is a list of hosts.  Either the host ID or name must be provided for mapping/unmapping hosts for a consistency group.  If *hosts* are given, then *mapping_state* should also be specified.  Hosts cannot be mapped to a consistency group, if the consistency group has no volumes.  When a consistency group is being mapped to the host, users should not use the volume module to map the volumes in the consistency group to hosts. |
| **host_id**  string | The ID of the host. |
| **host_name**  string | The name of the host. |
| **mapping_state**  string | String variable, describes the state of hosts inside the consistency group.  If *hosts* are given, then *mapping_state* should also be specified.  **Choices:**   - `"mapped"` - `"unmapped"` |
| **new_cg_name**  string | The new name of the consistency group, used in rename operation. |
| **password**  string / required | The password of the Unity management server. |
| **port**  integer | Port number through which communication happens with Unity management server.  **Default:** `443` |
| **replication_params**  dictionary | Settings required for enabling replication. |
| **destination_cg_name**  string | Name of the destination consistency group.  Default value will be source consistency group name prefixed by ‘DR_’. |
| **destination_pool_id**  string | Id of pool to allocate destination Luns.  Mutually exclusive with *destination_pool_name*. |
| **destination_pool_name**  string | Name of pool to allocate destination Luns.  Mutually exclusive with *destination_pool_id*. |
| **remote_system**  dictionary | Details of remote system to which the replication is being configured.  The *remote_system* option should be specified if the *replication_type* is `remote`. |
| **remote_system_host**  string / required | IP or FQDN for remote Unity unisphere Host. |
| **remote_system_password**  string / required | Password of remote Unity unisphere Host. |
| **remote_system_port**  integer | Port at which remote Unity unisphere is hosted.  **Default:** `443` |
| **remote_system_username**  string / required | User name of remote Unity unisphere Host. |
| **remote_system_verifycert**  boolean | Boolean variable to specify whether or not to validate SSL certificate of remote Unity unisphere Host.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |
| **replication_mode**  string / required | The replication mode.  **Choices:**   - `"asynchronous"` - `"manual"` |
| **replication_type**  string | Type of replication.  **Choices:**   - `"local"` ← (default) - `"remote"` |
| **rpo**  integer | Maximum time to wait before the system syncs the source and destination LUNs.  Option *rpo* should be specified if the *replication_mode* is `asynchronous`.  The value should be in range of `5` to `1440`. |
| **replication_state**  string | State of the replication.  **Choices:**   - `"enable"` - `"disable"` |
| **snap_schedule**  string | Snapshot schedule assigned to the consistency group.  Specifying an empty string “” removes the existing snapshot schedule from consistency group. |
| **state**  string / required | Define whether the consistency group should exist or not.  **Choices:**   - `"absent"` - `"present"` |
| **tiering_policy**  string | Tiering policy choices for how the storage resource data will be distributed among the tiers available in the pool.  **Choices:**   - `"AUTOTIER_HIGH"` - `"AUTOTIER"` - `"HIGHEST"` - `"LOWEST"` |
| **unispherehost**  string / required | IP or FQDN of the Unity management server. |
| **username**  string / required | The username of the Unity management server. |
| **validate_certs**  aliases: verifycert  boolean | Boolean variable to specify whether or not to validate SSL certificate.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |
| **vol_state**  string | String variable, describes the state of volumes inside consistency group.  If *volumes* are given, then *vol_state* should also be specified.  **Choices:**   - `"present-in-group"` - `"absent-in-group"` |
| **volumes**  list / elements=dictionary | This is a list of volumes.  Either the volume ID or name must be provided for adding/removing existing volumes from consistency group.  If *volumes* are given, then *vol_state* should also be specified.  Volumes cannot be added/removed from consistency group, if the consistency group or the volume has snapshots. |
| **vol_id**  string | The ID of the volume. |
| **vol_name**  string | The name of the volume. |

## [Notes](consistencygroup_module.md#id4)

> **Note:**
>
> - The *check_mode* is not supported.
> - The modules present in this collection named as ‘dellemc.unity’ are built to support the Dell Unity storage platform.

## [Examples](consistencygroup_module.md#id5)

```yaml+jinja
- name: Create consistency group
  dellemc.unity.consistencygroup:
      unispherehost: "{{unispherehost}}"
      validate_certs: "{{validate_certs}}"
      username: "{{username}}"
      password: "{{password}}"
      cg_name: "{{cg_name}}"
      description: "{{description}}"
      snap_schedule: "{{snap_schedule1}}"
      state: "present"

- name: Get details of consistency group using id
  dellemc.unity.consistencygroup:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      validate_certs: "{{validate_certs}}"
      cg_id: "{{cg_id}}"
      state: "present"

- name: Add volumes to consistency group
  dellemc.unity.consistencygroup:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      validate_certs: "{{validate_certs}}"
      cg_id: "{{cg_id}}"
      volumes:
          - vol_name: "Ansible_Test-3"
          - vol_id: "sv_1744"
      vol_state: "{{vol_state_present}}"
      state: "present"

- name: Rename consistency group
  dellemc.unity.consistencygroup:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      validate_certs: "{{validate_certs}}"
      cg_name: "{{cg_name}}"
      new_cg_name: "{{new_cg_name}}"
      state: "present"

- name: Modify consistency group details
  dellemc.unity.consistencygroup:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      validate_certs: "{{validate_certs}}"
      cg_name: "{{new_cg_name}}"
      snap_schedule: "{{snap_schedule2}}"
      tiering_policy: "{{tiering_policy1}}"
      state: "present"

- name: Map hosts to a consistency group
  dellemc.unity.consistencygroup:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      validate_certs: "{{validate_certs}}"
      cg_id: "{{cg_id}}"
      hosts:
        - host_name: "10.226.198.248"
        - host_id: "Host_511"
      mapping_state: "mapped"
      state: "present"

- name: Unmap hosts from a consistency group
  dellemc.unity.consistencygroup:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      validate_certs: "{{validate_certs}}"
      cg_id: "{{cg_id}}"
      hosts:
        - host_id: "Host_511"
        - host_name: "10.226.198.248"
      mapping_state: "unmapped"
      state: "present"

- name: Remove volumes from consistency group
  dellemc.unity.consistencygroup:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      validate_certs: "{{validate_certs}}"
      cg_name: "{{new_cg_name}}"
      volumes:
        - vol_name: "Ansible_Test-3"
        - vol_id: "sv_1744"
      vol_state: "{{vol_state_absent}}"
      state: "present"

- name: Delete consistency group
  dellemc.unity.consistencygroup:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      validate_certs: "{{validate_certs}}"
      cg_name: "{{new_cg_name}}"
      state: "absent"

- name: Enable replication for consistency group
  dellemc.unity.consistencygroup:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      validate_certs: "{{validate_certs}}"
      cg_id: "cg_id_1"
      replication_params:
        destination_cg_name: "destination_cg_1"
        replication_mode: "asynchronous"
        rpo: 60
        replication_type: "remote"
        remote_system:
          remote_system_host: '10.1.2.3'
          remote_system_verifycert: false
          remote_system_username: 'username'
          remote_system_password: 'password'
        destination_pool_name: "pool_test_1"
      replication_state: "enable"
      state: "present"

- name: Disable replication for consistency group
  dellemc.unity.consistencygroup:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      validate_certs: "{{validate_certs}}"
      cg_name: "dis_repl_ans_source"
      replication_state: "disable"
      state: "present"
```

## [Return Values](consistencygroup_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether or not the resource has changed.  **Returned:** always  **Sample:** `true` |
| **consistency_group_details**  dictionary | Details of the consistency group.  **Returned:** When consistency group exists  **Sample:** `{"advanced_dedup_status": "DedupStatusEnum.DISABLED", "block_host_access": null, "cg_replication_enabled": false, "data_reduction_percent": 0, "data_reduction_ratio": 1.0, "data_reduction_size_saved": 0, "data_reduction_status": "DataReductionStatusEnum.DISABLED", "datastores": null, "dedup_status": null, "description": "Ansible testing", "esx_filesystem_block_size": null, "esx_filesystem_major_version": null, "existed": true, "filesystem": null, "hash": 8776023812033, "health": {"UnityHealth": {"hash": 8776023811889}}, "host_v_vol_datastore": null, "id": "res_7477", "is_replication_destination": false, "is_snap_schedule_paused": null, "luns": null, "metadata_size": 0, "metadata_size_allocated": 0, "name": "Ansible_CG_Testing", "per_tier_size_used": null, "pools": null, "relocation_policy": "TieringPolicyEnum.MIXED", "replication_type": "ReplicationTypeEnum.NONE", "size_allocated": 0, "size_total": 0, "size_used": null, "snap_count": 0, "snap_schedule": null, "snaps_size_allocated": 0, "snaps_size_total": 0, "snapshots": [], "thin_status": "ThinStatusEnum.FALSE", "type": "StorageResourceTypeEnum.CONSISTENCY_GROUP", "virtual_volumes": null, "vmware_uuid": null}` |
| **block_host_access**  dictionary | Details of hosts mapped to the consistency group.  **Returned:** success |
| **UnityBlockHostAccessList**  list / elements=string | List of hosts mapped to consistency group.  **Returned:** success |
| **UnityBlockHostAccess**  dictionary | Details of host.  **Returned:** success |
| **id**  string | The ID of the host.  **Returned:** success |
| **name**  string | The name of the host.  **Returned:** success |
| **cg_replication_enabled**  boolean | Whether or not the replication is enabled..  **Returned:** success |
| **id**  string | The system ID given to the consistency group.  **Returned:** success |
| **luns**  dictionary | Details of volumes part of consistency group.  **Returned:** success |
| **UnityLunList**  list / elements=string | List of volumes part of consistency group.  **Returned:** success |
| **UnityLun**  dictionary | Detail of volume.  **Returned:** success |
| **id**  string | The system ID given to volume.  **Returned:** success |
| **name**  string | The name of the volume.  **Returned:** success |
| **relocation_policy**  string | FAST VP tiering policy for the consistency group.  **Returned:** success |
| **snap_schedule**  dictionary | Snapshot schedule applied to consistency group.  **Returned:** success |
| **UnitySnapSchedule**  dictionary | Snapshot schedule applied to consistency group.  **Returned:** success |
| **id**  string | The system ID given to the snapshot schedule.  **Returned:** success |
| **name**  string | The name of the snapshot schedule.  **Returned:** success |
| **snapshots**  list / elements=string | List of snapshots of consistency group.  **Returned:** success |
| **creation_time**  string | Date and time on which the snapshot was taken.  **Returned:** success |
| **expirationTime**  string | Date and time after which the snapshot will expire.  **Returned:** success |
| **name**  string | Name of the snapshot.  **Returned:** success |
| **storageResource**  dictionary | Storage resource for which the snapshot was taken.  **Returned:** success |
| **UnityStorageResource**  dictionary | Details of the storage resource.  **Returned:** success |
| **id**  string | The id of the storage resource.  **Returned:** success |

### Authors

- Akash Shendge (@shenda1)

### Collection links

- [Issue Tracker](https://www.dell.com/community/Automation/bd-p/Automation)
- [Repository (Sources)](https://github.com/dell/ansible-unity/tree/1.7.1)
