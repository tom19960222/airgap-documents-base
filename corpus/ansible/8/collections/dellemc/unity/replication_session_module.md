---
collection: ansible
version: "8"
title: "dellemc.unity.replication_session module – Manage replication session on Unity storage system"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/unity/replication_session_module.html
fetched_at: 2026-07-28T02:05:28+00:00
---
# dellemc.unity.replication_session module – Manage replication session on Unity storage system

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
> see [Requirements](replication_session_module.md#ansible-collections-dellemc-unity-replication-session-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.unity.replication_session`.

New in dellemc.unity 1.7.0

- [Synopsis](replication_session_module.md#synopsis)
- [Requirements](replication_session_module.md#requirements)
- [Parameters](replication_session_module.md#parameters)
- [Notes](replication_session_module.md#notes)
- [Examples](replication_session_module.md#examples)
- [Return Values](replication_session_module.md#return-values)

## [Synopsis](replication_session_module.md#id1)

- Managing replication session on Unity storage system includes getting details, pause, resume, sync, failover, failback and deleting the replication session.

## [Requirements](replication_session_module.md#id2)

The below requirements are needed on the host that executes this module.

- A Dell Unity Storage device version 5.1 or later.
- Ansible-core 2.13 or later.
- Python 3.9, 3.10 or 3.11.
- Storops Python SDK 1.2.11.

## [Parameters](replication_session_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **failback**  boolean | Failback a replication session.  **Choices:**   - `false` - `true` |
| **failover_with_sync**  boolean | If `true`, Sync the source and destination resources before failing over the asynchronous replication session or keep them in sync after failing over the synchronous replication session.  If `false`, Failover a replication session.  **Choices:**   - `false` - `true` |
| **force**  boolean | Skip pre-checks on file system(s) replication sessions of a NAS server when a replication failover is issued from the source NAS server.  **Choices:**   - `false` - `true` |
| **force_full_copy**  boolean | Indicates whether to sync back all data from the destination SP to the source SP during the failback session. Needed during resume operation when replication session goes out of sync due to a fault.  **Choices:**   - `false` - `true` |
| **password**  string / required | The password of the Unity management server. |
| **pause**  boolean | Pause or resume replication session.  **Choices:**   - `false` - `true` |
| **port**  integer | Port number through which communication happens with Unity management server.  **Default:** `443` |
| **session_id**  string | ID of replication session. |
| **session_name**  string | Name of replication session. |
| **state**  string | State variable to determine whether replication session will exist or not.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **sync**  boolean | Sync a replication session.  **Choices:**   - `false` - `true` |
| **unispherehost**  string / required | IP or FQDN of the Unity management server. |
| **username**  string / required | The username of the Unity management server. |
| **validate_certs**  aliases: verifycert  boolean | Boolean variable to specify whether or not to validate SSL certificate.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](replication_session_module.md#id4)

> **Note:**
>
> - The *check_mode* is supported.
> - The modules present in this collection named as ‘dellemc.unity’ are built to support the Dell Unity storage platform.

## [Examples](replication_session_module.md#id5)

```yaml+jinja
- name: Get replication session details
  dellemc.unity.replication_session:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    session_name: "fs_replication"

- name: Get replication session details based on session_id
  dellemc.unity.replication_session:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    session_id: "103079215114_APM00213404195_0000_103079215274_APM00213404194_0000"

- name: Pause a replication session
  dellemc.unity.replication_session:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    session_name: "fs_replication"
    pause: true

- name: Resume a replication session
  dellemc.unity.replication_session:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    session_name: "fs_replication"
    pause: false
    force_full_copy: true

- name: Sync a replication session
  dellemc.unity.replication_session:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    session_name: "fs_replication"
    sync: true

- name: Failover with sync a replication session
  dellemc.unity.replication_session:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    session_name: "fs_replication"
    failover_with_sync: true
    force: true

- name: Failover a replication session
  dellemc.unity.replication_session:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    session_name: "fs_replication"
    failover_with_sync: false

- name: Failback a replication session
  dellemc.unity.replication_session:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    session_name: "fs_replication"
    failback: true
    force_full_copy: true

- name: Delete a replication session
  dellemc.unity.replication_session:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    session_name: "fs_replication"
    state: "absent"
```

## [Return Values](replication_session_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether or not the resource has changed.  **Returned:** always  **Sample:** `true` |
| **replication_session_details**  dictionary | Details of the replication session.  **Returned:** When replication session exists.  **Sample:** `{"current_transfer_est_remain_time": 0, "daily_snap_replication_policy": null, "dst_resource_id": "nas_8", "dst_spa_interface": {"UnityRemoteInterface": {"hash": 8771253398547, "id": "APM00213404195:if_181"}}, "dst_spb_interface": {"UnityRemoteInterface": {"hash": 8771253424144, "id": "APM00213404195:if_180"}}, "dst_status": "ReplicationSessionStatusEnum.OK", "existed": true, "hash": 8771259012271, "health": {"UnityHealth": {"hash": 8771253424168}}, "hourly_snap_replication_policy": null, "id": "103079215114_APM00213404195_0000_103079215274_APM00213404194_0000", "last_sync_time": "2023-04-18 10:35:25+00:00", "local_role": "ReplicationSessionReplicationRoleEnum.DESTINATION", "max_time_out_of_sync": 0, "members": null, "name": "rep_sess_nas", "network_status": "ReplicationSessionNetworkStatusEnum.OK", "remote_system": {"UnityRemoteSystem": {"hash": 8771253380142}}, "replication_resource_type": "ReplicationEndpointResourceTypeEnum.NASSERVER", "src_resource_id": "nas_213", "src_spa_interface": {"UnityRemoteInterface": {"hash": 8771253475010, "id": "APM00213404194:if_195"}}, "src_spb_interface": {"UnityRemoteInterface": {"hash": 8771253374169, "id": "APM00213404194:if_194"}}, "src_status": "ReplicationSessionStatusEnum.OK", "status": "ReplicationOpStatusEnum.ACTIVE", "sync_progress": 0, "sync_state": "ReplicationSessionSyncStateEnum.IN_SYNC"}` |
| **currentTransferEstRemainTime**  integer | Estimated time left for the replication synchronization to complete.  **Returned:** success |
| **dstResourceId**  string | Identifier of the destination resource.  **Returned:** success |
| **dstStatus**  string | Status of the destination end of the replication session.  **Returned:** success |
| **id**  string | Unique identifier of the replicationSession instance.  **Returned:** success |
| **lastSyncTime**  string | Date and time of the last replication synchronization.  **Returned:** success |
| **maxTimeOutOfSync**  integer | Maximum time to wait before the system syncs the source and destination resources.  **Returned:** success |
| **name**  string | User-specified replication session name.  **Returned:** success |
| **networkStatus**  string | Status of the network connection used by the replication session.  **Returned:** success |
| **remoteSystem**  dictionary | Specifies the remote system to use as the destination for the replication session.  **Returned:** success |
| **UnityRemoteSystem**  dictionary | Information about remote storage system.  **Returned:** success |
| **id**  string | Unique identifier of the remote system instance.  **Returned:** success |
| **serialNumber**  string | Serial number of the remote system.  **Returned:** success |
| **replicationResourceType**  string | Replication resource type of replication session endpoints.  **Returned:** success |
| **srcStatus**  string | Status of the source end of the session.  **Returned:** success |
| **status**  string | Replication status of the replication session.  **Returned:** success |
| **syncProgress**  integer | Synchronization completion percentage between source and destination resources of the replication session.  **Returned:** success |
| **syncState**  string | Synchronization state between source and destination resource of the replication session.  **Returned:** success |

### Authors

- Jennifer John (@Jennifer-John)

### Collection links

- [Issue Tracker](https://www.dell.com/community/Automation/bd-p/Automation)
- [Repository (Sources)](https://github.com/dell/ansible-unity/tree/1.7.1)
