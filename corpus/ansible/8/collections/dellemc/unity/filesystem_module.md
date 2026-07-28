---
collection: ansible
version: "8"
title: "dellemc.unity.filesystem module – Manage filesystem on Unity storage system"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/unity/filesystem_module.html
fetched_at: 2026-07-28T02:05:21+00:00
---
# dellemc.unity.filesystem module – Manage filesystem on Unity storage system

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
> see [Requirements](filesystem_module.md#ansible-collections-dellemc-unity-filesystem-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.unity.filesystem`.

New in dellemc.unity 1.1.0

- [Synopsis](filesystem_module.md#synopsis)
- [Requirements](filesystem_module.md#requirements)
- [Parameters](filesystem_module.md#parameters)
- [Notes](filesystem_module.md#notes)
- [Examples](filesystem_module.md#examples)
- [Return Values](filesystem_module.md#return-values)

## [Synopsis](filesystem_module.md#id1)

- Managing filesystem on Unity storage system includes Create new filesystem, Modify snapschedule attribute of filesystem, Modify filesystem attributes, Display filesystem details, Display filesystem snapshots, Display filesystem snapschedule, Delete snapschedule associated with the filesystem, Delete filesystem, Create new filesystem with quota configuration, Enable, modify and disable replication.

Aliases: dellemc_unity_filesystem

## [Requirements](filesystem_module.md#id2)

The below requirements are needed on the host that executes this module.

- A Dell Unity Storage device version 5.1 or later.
- Ansible-core 2.13 or later.
- Python 3.9, 3.10 or 3.11.
- Storops Python SDK 1.2.11.

## [Parameters](filesystem_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_policy**  string | Access policy of a filesystem.  **Choices:**   - `"NATIVE"` - `"UNIX"` - `"WINDOWS"` |
| **cap_unit**  string | The unit of the filesystem size. It defaults to `GB`, if not specified.  **Choices:**   - `"GB"` - `"TB"` |
| **data_reduction**  boolean | Boolean variable, specifies whether or not to enable compression. Compression is supported only for thin filesystem.  **Choices:**   - `false` - `true` |
| **description**  string | Description about the filesystem.  Description can be removed by passing empty string (“”). |
| **filesystem_id**  string | The id of the filesystem.  It can be used only for get, modify, or delete operations.  It is mutually exclusive with *filesystem_name*. |
| **filesystem_name**  string | The name of the filesystem. Mandatory only for the create operation. All the operations are supported through *filesystem_name*.  It is mutually exclusive with *filesystem_id*. |
| **is_thin**  boolean | Boolean variable, specifies whether or not it is a thin filesystem.  **Choices:**   - `false` - `true` |
| **locking_policy**  string | File system locking policies. These policy choices control whether the NFSv4 range locks must be honored.  **Choices:**   - `"ADVISORY"` - `"MANDATORY"` |
| **nas_server_id**  string | ID of the NAS server on which filesystem will be hosted. |
| **nas_server_name**  string | Name of the NAS server on which filesystem will be hosted. |
| **password**  string / required | The password of the Unity management server. |
| **pool_id**  string | This is the ID of the pool where the filesystem will be created.  Either the *pool_name* or *pool_id* must be provided to create a new filesystem. |
| **pool_name**  string | This is the name of the pool where the filesystem will be created.  Either the *pool_name* or *pool_id* must be provided to create a new filesystem. |
| **port**  integer | Port number through which communication happens with Unity management server.  **Default:** `443` |
| **quota_config**  dictionary | Configuration for quota management. It contains optional parameters. |
| **cap_unit**  string | Unit of *default_soft_limit* and *default_hard_limit* size.  Default unit is `GB`.  **Choices:**   - `"MB"` - `"GB"` - `"TB"` |
| **default_hard_limit**  integer | Default hard limit for user quotas and tree quotas.  If *default_hard_limit* is not set while creation of filesystem, it will be set to `0B` by default. |
| **default_soft_limit**  integer | Default soft limit for user quotas and tree quotas.  If *default_soft_limit* is not set while creation of filesystem, it will be set to `0B` by default. |
| **grace_period**  integer | Grace period set in quota configuration after soft limit is reached.  If *grace_period* is not set during creation of filesystem, it will be set to `7 days` by default. |
| **grace_period_unit**  string | Unit of grace period.  Default unit is `days`.  **Choices:**   - `"minutes"` - `"hours"` - `"days"` |
| **is_user_quota_enabled**  boolean | Indicates whether the user quota is enabled.  If *is_user_quota_enabled* is not set while creation of filesystem, it will be set to `false` by default.  Parameters *is_user_quota_enabled* and *quota_policy* are mutually exclusive.  **Choices:**   - `false` - `true` |
| **quota_policy**  string | Quota policy set in quota configuration.  If *quota_policy* is not set while creation of filesystem, it will be set to `FILE_SIZE` by default.  Parameters *is_user_quota_enabled* and *quota_policy* are mutually exclusive.  **Choices:**   - `"FILE_SIZE"` - `"BLOCKS"` |
| **replication_params**  dictionary | Settings required for enabling or modifying replication. |
| **destination_pool_id**  string | ID of pool to allocate destination filesystem. |
| **destination_pool_name**  string | Name of pool to allocate destination filesystem. |
| **new_replication_name**  string | Replication name to rename the session to. |
| **remote_system**  dictionary | Details of remote system to which the replication is being configured.  The *remote_system* option should be specified if the *replication_type* is `remote`. |
| **remote_system_host**  string / required | IP or FQDN for remote Unity unisphere Host. |
| **remote_system_password**  string / required | Password of remote Unity unisphere Host. |
| **remote_system_port**  integer | Port at which remote Unity unisphere is hosted.  **Default:** `443` |
| **remote_system_username**  string / required | User name of remote Unity unisphere Host. |
| **remote_system_verifycert**  boolean | Boolean variable to specify whether or not to validate SSL certificate of remote Unity unisphere Host.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |
| **replication_mode**  string | The replication mode.  This is a mandatory field while creating a replication session.  **Choices:**   - `"synchronous"` - `"asynchronous"` - `"manual"` |
| **replication_name**  string | Name of the replication session. |
| **replication_type**  string | Type of replication.  **Choices:**   - `"local"` - `"remote"` |
| **rpo**  integer | Maximum time to wait before the system syncs the source and destination LUNs.  The *rpo* option should be specified if the *replication_mode* is `asynchronous`.  The value should be in range of `5` to `1440` for `asynchronous`, `0` for `synchronous` and `-1` for `manual`. |
| **replication_state**  string | State of the replication.  **Choices:**   - `"enable"` - `"disable"` |
| **size**  integer | The size of the filesystem. |
| **smb_properties**  dictionary | Advance settings for SMB. It contains optional candidate variables. |
| **is_smb_notify_on_access_enabled**  boolean | Indicates whether notifications of changes to directory file structure are enabled.  **Choices:**   - `false` - `true` |
| **is_smb_notify_on_write_enabled**  boolean | Indicates whether file write notifications are enabled on the file system.  **Choices:**   - `false` - `true` |
| **is_smb_op_locks_enabled**  boolean | Indicates whether opportunistic file locking is enabled on the file system.  **Choices:**   - `false` - `true` |
| **is_smb_sync_writes_enabled**  boolean | Indicates whether the synchronous writes option is enabled on the file system.  **Choices:**   - `false` - `true` |
| **smb_notify_on_change_dir_depth**  integer | Integer variable, determines the lowest directory level to which the enabled notifications apply.  Minimum value is `1`. |
| **snap_schedule_id**  string | This is the id of an existing snapshot schedule which is to be associated with the filesystem.  This is mutually exclusive with *snapshot_schedule_name*. |
| **snap_schedule_name**  string | This is the name of an existing snapshot schedule which is to be associated with the filesystem.  This is mutually exclusive with *snapshot_schedule_id*. |
| **state**  string / required | State variable to determine whether filesystem will exist or not.  **Choices:**   - `"absent"` - `"present"` |
| **supported_protocols**  string | Protocols supported by the file system.  It will be overridden by NAS server configuration if NAS Server is `Multiprotocol`.  **Choices:**   - `"NFS"` - `"CIFS"` - `"MULTIPROTOCOL"` |
| **tiering_policy**  string | Tiering policy choices for how the storage resource data will be distributed among the tiers available in the pool.  **Choices:**   - `"AUTOTIER_HIGH"` - `"AUTOTIER"` - `"HIGHEST"` - `"LOWEST"` |
| **unispherehost**  string / required | IP or FQDN of the Unity management server. |
| **username**  string / required | The username of the Unity management server. |
| **validate_certs**  aliases: verifycert  boolean | Boolean variable to specify whether or not to validate SSL certificate.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](filesystem_module.md#id4)

> **Note:**
>
> - SMB shares, NFS exports, and snapshots associated with filesystem need to be deleted prior to deleting a filesystem.
> - The *quota_config* parameter can be used to update default hard limit and soft limit values to limit the maximum space that can be used. By default they both are set to 0 during filesystem creation which means unlimited.
> - The *check_mode* is not supported.
> - The modules present in this collection named as ‘dellemc.unity’ are built to support the Dell Unity storage platform.

## [Examples](filesystem_module.md#id5)

```yaml+jinja
- name: Create FileSystem
  dellemc.unity.filesystem:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    filesystem_name: "ansible_test_fs"
    nas_server_name: "lglap761"
    pool_name: "pool_1"
    size: 5
    state: "present"

- name: Create FileSystem with quota configuration
  dellemc.unity.filesystem:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    filesystem_name: "ansible_test_fs"
    nas_server_name: "lglap761"
    pool_name: "pool_1"
    size: 5
    quota_config:
        grace_period: 8
        grace_period_unit: "days"
        default_soft_limit: 10
        is_user_quota_enabled: false
    state: "present"

- name: Expand FileSystem size
  dellemc.unity.filesystem:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    filesystem_name: "ansible_test_fs"
    nas_server_name: "lglap761"
    size: 10
    state: "present"

- name: Expand FileSystem size
  dellemc.unity.filesystem:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    filesystem_name: "ansible_test_fs"
    nas_server_name: "lglap761"
    size: 10
    state: "present"

- name: Modify FileSystem smb_properties
  dellemc.unity.filesystem:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    filesystem_name: "ansible_test_fs"
    nas_server_name: "lglap761"
    smb_properties:
      is_smb_op_locks_enabled: true
      smb_notify_on_change_dir_depth: 5
      is_smb_notify_on_access_enabled: true
    state: "present"

- name: Modify FileSystem Snap Schedule
  dellemc.unity.filesystem:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    filesystem_id: "fs_141"
    snap_schedule_id: "{{snap_schedule_id}}"
    state: "{{state_present}}"

- name: Get details of FileSystem using id
  dellemc.unity.filesystem:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    filesystem_id: "rs_405"
    state: "present"

- name: Delete a FileSystem using id
  dellemc.unity.filesystem:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    filesystem_id: "rs_405"
    state: "absent"

- name: Enable replication on the fs
  dellemc.unity.filesystem:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    filesystem_id: "rs_405"
    replication_params:
      replication_name: "test_repl"
      replication_type: "remote"
      replication_mode: "asynchronous"
      rpo: 60
      remote_system:
        remote_system_host: '0.1.2.3'
        remote_system_verifycert: false
        remote_system_username: 'username'
        remote_system_password: 'password'
      destination_pool_name: "pool_test_1"
    replication_state: "enable"
    state: "present"

- name: Modify replication on the fs
  dellemc.unity.filesystem:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    filesystem_id: "rs_405"
    replication_params:
      replication_name: "test_repl"
      new_replication_name: "test_repl_updated"
      replication_mode: "asynchronous"
      rpo: 50
    replication_state: "enable"
    state: "present"

- name: Disable replication on the fs
  dellemc.unity.filesystem:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    filesystem_id: "rs_405"
    replication_state: "disable"
    state: "present"

- name: Disable replication by specifying replication_name on the fs
  dellemc.unity.filesystem:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    filesystem_id: "rs_405"
    replication_params:
        replication_name: "test_replication"
    replication_state: "disable"
    state: "present"
```

## [Return Values](filesystem_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether or not the resource has changed.  **Returned:** always  **Sample:** `true` |
| **filesystem_details**  dictionary | Details of the filesystem.  **Returned:** When filesystem exists  **Sample:** `{"access_policy": "AccessPolicyEnum.UNIX", "cifs_notify_on_change_dir_depth": 512, "cifs_share": null, "data_reduction_percent": 0, "data_reduction_ratio": 1.0, "data_reduction_size_saved": 0, "description": "", "existed": true, "folder_rename_policy": "FSRenamePolicyEnum.SMB_RENAME_FORBIDDEN", "format": "FSFormatEnum.UFS64", "hash": 8735427610152, "health": {"UnityHealth": {"hash": 8735427614928}}, "host_io_size": "HostIOSizeEnum.GENERAL_8K", "id": "fs_65916", "is_advanced_dedup_enabled": false, "is_cifs_notify_on_access_enabled": false, "is_cifs_notify_on_write_enabled": false, "is_cifs_op_locks_enabled": false, "is_cifs_sync_writes_enabled": false, "is_data_reduction_enabled": false, "is_read_only": false, "is_smbca": false, "is_thin_enabled": true, "locking_policy": "FSLockingPolicyEnum.MANDATORY", "metadata_size": 11274289152, "metadata_size_allocated": 4294967296, "min_size_allocated": 0, "name": "test_fs", "nas_server": {"id": "nas_18", "name": "test_nas1"}, "nfs_share": null, "per_tier_size_used": [6979321856, 0, 0], "pool": {"id": "pool_7", "name": "pool 7"}, "pool_full_policy": "ResourcePoolFullPolicyEnum.FAIL_WRITES", "quota_config": {"default_hard_limit": "0B", "default_soft_limit": "0B", "grace_period": "7.0 days", "id": "quotaconfig_171798760421_0", "is_user_quota_enabled": false, "quota_policy": "QuotaPolicyEnum.FILE_SIZE"}, "replication_sessions": {"current_transfer_est_remain_time": 0, "id": "***", "last_sync_time": "2022-05-12 11:20:38+00:00", "local_role": "ReplicationSessionReplicationRoleEnum.SOURCE", "max_time_out_of_sync": 60, "members": null, "name": "local_repl_new", "network_status": "ReplicationSessionNetworkStatusEnum.OK", "remote_system": {"UnityRemoteSystem": {"hash": 8735426929707}}, "replication_resource_type": "ReplicationEndpointResourceTypeEnum.FILESYSTEM", "src_resource_id": "res_66444", "src_status": "ReplicationSessionStatusEnum.OK", "status": "ReplicationOpStatusEnum.AUTO_SYNC_CONFIGURED", "sync_progress": 0, "sync_state": "ReplicationSessionSyncStateEnum.IDLE"}, "size_allocated": 283148288, "size_allocated_total": 4578148352, "size_preallocated": 2401173504, "size_total": 10737418240, "size_total_with_unit": "10.0 GB", "size_used": 1620312064, "snap_count": 2, "snaps_size": 21474869248, "snaps_size_allocated": 32768, "snapshots": [], "supported_protocols": "FSSupportedProtocolEnum.NFS", "tiering_policy": "TieringPolicyEnum.AUTOTIER_HIGH", "type": "FilesystemTypeEnum.FILESYSTEM"}` |
| **cifs_notify_on_change_dir_depth**  integer | Indicates the lowest directory level to which the enabled notifications apply, if any.  **Returned:** success |
| **description**  string | Description about the filesystem.  **Returned:** success |
| **id**  string | The system generated ID given to the filesystem.  **Returned:** success |
| **is_cifs_notify_on_access_enabled**  boolean | Indicates whether the system generates a notification when a user accesses the file system.  **Returned:** success |
| **is_cifs_notify_on_write_enabled**  boolean | Indicates whether the system generates a notification when the file system is written to.  **Returned:** success |
| **is_cifs_op_locks_enabled**  boolean | Indicates whether opportunistic file locks are enabled for the file system.  **Returned:** success |
| **is_cifs_sync_writes_enabled**  boolean | Indicates whether the CIFS synchronous writes option is enabled for the file system.  **Returned:** success |
| **is_data_reduction_enabled**  boolean | Whether or not compression enabled on this filesystem.  **Returned:** success |
| **is_thin_enabled**  boolean | Indicates whether thin provisioning is enabled for this filesystem.  **Returned:** success |
| **name**  string | Name of the filesystem.  **Returned:** success |
| **nas_server**  dictionary | The NAS Server details on which this filesystem is hosted.  **Returned:** success |
| **id**  string | The system ID given to the NAS Server.  **Returned:** success |
| **name**  string | The name of the NAS Server.  **Returned:** success |
| **pool**  dictionary | The pool in which this filesystem is allocated.  **Returned:** success |
| **id**  string | The system ID given to the pool.  **Returned:** success |
| **name**  string | The name of the storage pool.  **Returned:** success |
| **quota_config**  dictionary | Details of quota configuration of the filesystem created.  **Returned:** success |
| **default_hard_limit**  integer | Default hard limit for user quotas and tree quotas.  **Returned:** success |
| **default_soft_limit**  integer | Default soft limit for user quotas and tree quotas.  **Returned:** success |
| **grace_period**  string | Grace period set in quota configuration after soft limit is reached.  **Returned:** success |
| **is_user_quota_enabled**  boolean | Indicates whether the user quota is enabled.  **Returned:** success |
| **quota_policy**  string | Quota policy set in quota configuration.  **Returned:** success |
| **replication_sessions**  dictionary | List of replication sessions if replication is enabled.  **Returned:** success |
| **id**  string | ID of replication session  **Returned:** success |
| **name**  string | Name of replication session  **Returned:** success |
| **remote_system**  dictionary | Remote system  **Returned:** success |
| **id**  string | ID of remote system  **Returned:** success |
| **size_total_with_unit**  string | Size of the filesystem with actual unit.  **Returned:** success |
| **snap_schedule_id**  string | Indicates the id of the snap schedule associated with the filesystem.  **Returned:** success |
| **snap_schedule_name**  string | Indicates the name of the snap schedule associated with the filesystem.  **Returned:** success |
| **snapshots**  list / elements=string | The list of snapshots of this filesystem.  **Returned:** success |
| **id**  string | The system ID given to the filesystem snapshot.  **Returned:** success |
| **name**  string | The name of the filesystem snapshot.  **Returned:** success |
| **tiering_policy**  string | Tiering policy applied to this filesystem.  **Returned:** success |

### Authors

- Arindam Datta (@dattaarindam)
- Meenakshi Dembi (@dembim)
- Spandita Panigrahi (@panigs7)

### Collection links

- [Issue Tracker](https://www.dell.com/community/Automation/bd-p/Automation)
- [Repository (Sources)](https://github.com/dell/ansible-unity/tree/1.7.1)
