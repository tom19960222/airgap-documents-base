---
collection: ansible
version: "8"
title: "dellemc.unity.filesystem_snapshot module – Manage filesystem snapshot on the Unity storage system"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/unity/filesystem_snapshot_module.html
fetched_at: 2026-07-28T02:05:22+00:00
---
# dellemc.unity.filesystem_snapshot module – Manage filesystem snapshot on the Unity storage system

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
> see [Requirements](filesystem_snapshot_module.md#ansible-collections-dellemc-unity-filesystem-snapshot-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.unity.filesystem_snapshot`.

New in dellemc.unity 1.1.0

- [Synopsis](filesystem_snapshot_module.md#synopsis)
- [Requirements](filesystem_snapshot_module.md#requirements)
- [Parameters](filesystem_snapshot_module.md#parameters)
- [Notes](filesystem_snapshot_module.md#notes)
- [Examples](filesystem_snapshot_module.md#examples)
- [Return Values](filesystem_snapshot_module.md#return-values)

## [Synopsis](filesystem_snapshot_module.md#id1)

- Managing Filesystem Snapshot on the Unity storage system includes create filesystem snapshot, get filesystem snapshot, modify filesystem snapshot and delete filesystem snapshot.

Aliases: dellemc_unity_filesystem_snapshot

## [Requirements](filesystem_snapshot_module.md#id2)

The below requirements are needed on the host that executes this module.

- A Dell Unity Storage device version 5.1 or later.
- Ansible-core 2.13 or later.
- Python 3.9, 3.10 or 3.11.
- Storops Python SDK 1.2.11.

## [Parameters](filesystem_snapshot_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auto_delete**  boolean | This option specifies whether or not the filesystem snapshot will be automatically deleted.  If set to `true`, the filesystem snapshot will expire based on the pool auto deletion policy.  If set to `false`, the filesystem snapshot will not be auto deleted based on the pool auto deletion policy.  Option *auto_delete* can not be set to `true`, if *expiry_time* is specified.  If during creation neither *auto_delete* nor *expiry_time* is mentioned then the filesystem snapshot will be created keeping *auto_delete* as `true`.  Once the *expiry_time* is set, then the filesystem snapshot cannot be assigned to the auto delete policy.  **Choices:**   - `false` - `true` |
| **description**  string | The additional information about the filesystem snapshot can be provided using this option.  The description can be removed by passing an empty string. |
| **expiry_time**  string | This option is for specifying the date and time after which the filesystem snapshot will expire.  The time is to be mentioned in UTC timezone.  The format is “MM/DD/YYYY HH:MM”. Year must be in 4 digits. |
| **filesystem_id**  string | The ID of the Filesystem for which snapshot is created.  For creation of filesystem snapshot either *filesystem_id* or *filesystem_name* is required.  Not required for other operations. |
| **filesystem_name**  string | The name of the Filesystem for which snapshot is created.  For creation of filesystem snapshot either *filesystem_name* or *filesystem_id* is required.  Not required for other operations. |
| **fs_access_type**  string | Access type of the filesystem snapshot.  Required only during creation of filesystem snapshot.  If not given, snapshot’s access type will be `Checkpoint`.  **Choices:**   - `"Checkpoint"` - `"Protocol"` |
| **nas_server_id**  string | The ID of the NAS server in which the Filesystem is created.  For creation of filesystem snapshot either *filesystem_id* or *filesystem_name* is required.  Not required for other operations. |
| **nas_server_name**  string | The name of the NAS server in which the Filesystem is created.  For creation of filesystem snapshot either *nas_server_name* or *nas_server_id* is required.  Not required for other operations. |
| **password**  string / required | The password of the Unity management server. |
| **port**  integer | Port number through which communication happens with Unity management server.  **Default:** `443` |
| **snapshot_id**  string | During creation snapshot_id is auto generated.  For all other operations either *snapshot_id* or *snapshot_name* is required. |
| **snapshot_name**  string | The name of the filesystem snapshot.  Mandatory parameter for creating a filesystem snapshot.  For all other operations either *snapshot_name* or *snapshot_id* is required. |
| **state**  string / required | The state option is used to mention the existence of the filesystem snapshot.  **Choices:**   - `"absent"` - `"present"` |
| **unispherehost**  string / required | IP or FQDN of the Unity management server. |
| **username**  string / required | The username of the Unity management server. |
| **validate_certs**  aliases: verifycert  boolean | Boolean variable to specify whether or not to validate SSL certificate.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](filesystem_snapshot_module.md#id4)

> **Note:**
>
> - Filesystem snapshot cannot be deleted, if it has nfs or smb share.
> - The *check_mode* is not supported.
> - The modules present in this collection named as ‘dellemc.unity’ are built to support the Dell Unity storage platform.

## [Examples](filesystem_snapshot_module.md#id5)

```yaml+jinja
- name: Create Filesystem Snapshot
  dellemc.unity.filesystem_snapshot:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    snapshot_name: "ansible_test_FS_snap"
    filesystem_name: "ansible_test_FS"
    nas_server_name: "lglad069"
    description: "Created using playbook"
    auto_delete: true
    fs_access_type: "Protocol"
    state: "present"

- name: Create Filesystem Snapshot with expiry time
  dellemc.unity.filesystem_snapshot:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    snapshot_name: "ansible_test_FS_snap_1"
    filesystem_name: "ansible_test_FS_1"
    nas_server_name: "lglad069"
    description: "Created using playbook"
    expiry_time: "04/15/2021 2:30"
    fs_access_type: "Protocol"
    state: "present"

- name: Get Filesystem Snapshot Details using Name
  dellemc.unity.filesystem_snapshot:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    snapshot_name: "ansible_test_FS_snap"
    state: "present"

- name: Get Filesystem Snapshot Details using ID
  dellemc.unity.filesystem_snapshot:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    snapshot_id: "10008000403"
    state: "present"

- name: Update Filesystem Snapshot attributes
  dellemc.unity.filesystem_snapshot:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    snapshot_name: "ansible_test_FS_snap"
    description: "Description updated"
    auto_delete: false
    expiry_time: "04/15/2021 5:30"
    state: "present"

- name: Update Filesystem Snapshot attributes using ID
  dellemc.unity.filesystem_snapshot:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    snapshot_id: "10008000403"
    expiry_time: "04/18/2021 8:30"
    state: "present"

- name: Delete Filesystem Snapshot using Name
  dellemc.unity.filesystem_snapshot:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    snapshot_name: "ansible_test_FS_snap"
    state: "absent"

- name: Delete Filesystem Snapshot using ID
  dellemc.unity.filesystem_snapshot:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    snapshot_id: "10008000403"
    state: "absent"
```

## [Return Values](filesystem_snapshot_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether or not the resource has changed.  **Returned:** always  **Sample:** `true` |
| **filesystem_snapshot_details**  dictionary | Details of the filesystem snapshot.  **Returned:** When filesystem snapshot exists  **Sample:** `{"access_type": "FilesystemSnapAccessTypeEnum.CHECKPOINT", "attached_wwn": null, "creation_time": "2022-10-21 04:42:53.951000+00:00", "creator_schedule": null, "creator_type": "SnapCreatorTypeEnum.USER_CUSTOM", "creator_user": {"id": "user_admin"}, "description": "Created using playbook", "existed": true, "expiration_time": null, "filesystem_id": "fs_137", "filesystem_name": "test", "hash": 8739894572587, "host_access": null, "id": "171798721695", "io_limit_policy": null, "is_auto_delete": true, "is_modifiable": false, "is_modified": false, "is_read_only": true, "is_system_snap": false, "last_writable_time": null, "lun": null, "name": "test_FS_snap_1", "nas_server_id": "nas_1", "nas_server_name": "lglad072", "parent_snap": null, "size": 107374182400, "snap_group": null, "state": "SnapStateEnum.READY"}` |
| **access_type**  string | Access type of filesystem snapshot.  **Returned:** success |
| **attached_wwn**  string | Attached WWN details.  **Returned:** success |
| **creation_time**  string | Creation time of filesystem snapshot.  **Returned:** success |
| **creator_schedule**  string | Creator schedule of filesystem snapshot.  **Returned:** success |
| **creator_type**  string | Creator type for filesystem snapshot.  **Returned:** success |
| **creator_user**  string | Creator user for filesystem snapshot.  **Returned:** success |
| **description**  string | Description of the filesystem snapshot.  **Returned:** success |
| **expiration_time**  string | Date and time after which the filesystem snapshot will expire.  **Returned:** success |
| **filesystem_id**  string | Id of the filesystem for which the snapshot exists.  **Returned:** success |
| **filesystem_name**  string | Name of the filesystem for which the snapshot exists.  **Returned:** success |
| **id**  string | Unique identifier of the filesystem snapshot instance.  **Returned:** success |
| **is_auto_delete**  boolean | Is the filesystem snapshot is auto deleted or not.  **Returned:** success |
| **name**  string | The name of the filesystem snapshot.  **Returned:** success |
| **nas_server_id**  string | Id of the NAS server on which filesystem exists.  **Returned:** success |
| **nas_server_name**  string | Name of the NAS server on which filesystem exists.  **Returned:** success |
| **size**  integer | Size of the filesystem snapshot.  **Returned:** success |

### Authors

- Rajshree Khare (@kharer5)

### Collection links

- [Issue Tracker](https://www.dell.com/community/Automation/bd-p/Automation)
- [Repository (Sources)](https://github.com/dell/ansible-unity/tree/1.7.1)
