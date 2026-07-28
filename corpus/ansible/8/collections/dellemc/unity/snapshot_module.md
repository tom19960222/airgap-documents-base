---
collection: ansible
version: "8"
title: "dellemc.unity.snapshot module – Manage snapshots on the Unity storage system"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/unity/snapshot_module.html
fetched_at: 2026-07-28T02:05:29+00:00
---
# dellemc.unity.snapshot module – Manage snapshots on the Unity storage system

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
> see [Requirements](snapshot_module.md#ansible-collections-dellemc-unity-snapshot-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.unity.snapshot`.

New in dellemc.unity 1.1.0

- [Synopsis](snapshot_module.md#synopsis)
- [Requirements](snapshot_module.md#requirements)
- [Parameters](snapshot_module.md#parameters)
- [Notes](snapshot_module.md#notes)
- [Examples](snapshot_module.md#examples)
- [Return Values](snapshot_module.md#return-values)

## [Synopsis](snapshot_module.md#id1)

- Managing snapshots on the Unity storage system includes create snapshot, delete snapshot, update snapshot, get snapshot, map host and unmap host.

Aliases: dellemc_unity_snapshot

## [Requirements](snapshot_module.md#id2)

The below requirements are needed on the host that executes this module.

- A Dell Unity Storage device version 5.1 or later.
- Ansible-core 2.13 or later.
- Python 3.9, 3.10 or 3.11.
- Storops Python SDK 1.2.11.

## [Parameters](snapshot_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auto_delete**  boolean | This option specifies whether the snapshot is auto deleted or not.  If set to `true`, snapshot will expire based on the pool auto deletion policy.  If set to (false), snapshot will not be auto deleted based on the pool auto deletion policy.  Option *auto_delete* can not be set to `true`, if *expiry_time* is specified.  If during creation neither *auto_delete* nor *expiry_time* is mentioned then snapshot will be created keeping *auto_delete* as `true`.  Once the *expiry_time* is set then snapshot cannot be assigned to the auto delete policy.  **Choices:**   - `false` - `true` |
| **cg_name**  string | The name of the Consistency Group for which snapshot is created.  For creation of a snapshot either *vol_name* or *cg_name* is required.  Not required for other operations. |
| **description**  string | The additional information about the snapshot can be provided using this option. |
| **expiry_time**  string | This option is for specifying the date and time after which the snapshot will expire.  The time is to be mentioned in UTC timezone.  The format is “MM/DD/YYYY HH:MM”. Year must be in 4 digits. |
| **host_id**  string | The id of the host.  Either *host_name* or *host_id* is required to map or unmap a snapshot from a host.  Snapshot can be attached to multiple hosts. |
| **host_name**  string | The name of the host.  Either *host_name* or *host_id* is required to map or unmap a snapshot from a host.  Snapshot can be attached to multiple hosts. |
| **host_state**  string | The *host_state* option is used to mention the existence of the host for snapshot.  It is required when a snapshot is mapped or unmapped from host.  **Choices:**   - `"mapped"` - `"unmapped"` |
| **new_snapshot_name**  string | New name for the snapshot. |
| **password**  string / required | The password of the Unity management server. |
| **port**  integer | Port number through which communication happens with Unity management server.  **Default:** `443` |
| **snapshot_id**  string | The id of the snapshot.  For all operations other than creation either *snapshot_name* or *snapshot_id* is required. |
| **snapshot_name**  string | The name of the snapshot.  Mandatory parameter for creating a snapshot.  For all other operations either *snapshot_name* or *snapshot_id* is required. |
| **state**  string / required | The *state* option is used to mention the existence of the snapshot.  **Choices:**   - `"absent"` - `"present"` |
| **unispherehost**  string / required | IP or FQDN of the Unity management server. |
| **username**  string / required | The username of the Unity management server. |
| **validate_certs**  aliases: verifycert  boolean | Boolean variable to specify whether or not to validate SSL certificate.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |
| **vol_name**  string | The name of the volume for which snapshot is created.  For creation of a snapshot either *vol_name* or *cg_name* is required.  Not required for other operations. |

## [Notes](snapshot_module.md#id4)

> **Note:**
>
> - The *check_mode* is not supported.
> - The modules present in this collection named as ‘dellemc.unity’ are built to support the Dell Unity storage platform.

## [Examples](snapshot_module.md#id5)

```yaml+jinja
- name: Create a Snapshot for a CG
  dellemc.unity.snapshot:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    cg_name: "{{cg_name}}"
    snapshot_name: "{{cg_snapshot_name}}"
    description: "{{description}}"
    auto_delete: false
    state: "present"

- name: Create a Snapshot for a volume with Host attached
  dellemc.unity.snapshot:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    vol_name: "{{vol_name}}"
    snapshot_name: "{{vol_snapshot_name}}"
    description: "{{description}}"
    expiry_time: "04/15/2025 16:30"
    host_name: "{{host_name}}"
    host_state: "mapped"
    state: "present"

- name: Unmap a host for a Snapshot
  dellemc.unity.snapshot:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    snapshot_name: "{{vol_snapshot_name}}"
    host_name: "{{host_name}}"
    host_state: "unmapped"
    state: "present"

- name: Map snapshot to a host
  dellemc.unity.snapshot:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    snapshot_name: "{{vol_snapshot_name}}"
    host_name: "{{host_name}}"
    host_state: "mapped"
    state: "present"

- name: Update attributes of a Snapshot for a volume
  dellemc.unity.snapshot:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    snapshot_name: "{{vol_snapshot_name}}"
    new_snapshot_name: "{{new_snapshot_name}}"
    description: "{{new_description}}"
    host_name: "{{host_name}}"
    host_state: "unmapped"
    state: "present"

- name: Delete Snapshot of CG
  dellemc.unity.snapshot:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    snapshot_name: "{{cg_snapshot_name}}"
    state: "absent"
```

## [Return Values](snapshot_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether or not the resource has changed.  **Returned:** always  **Sample:** `true` |
| **snapshot_details**  dictionary | Details of the snapshot.  **Returned:** When snapshot exists  **Sample:** `{"access_type": null, "attached_wwn": null, "creation_time": "2022-10-21 08:20:25.803000+00:00", "creator_schedule": null, "creator_type": "SnapCreatorTypeEnum.USER_CUSTOM", "creator_user": {"id": "user_admin"}, "description": "Test snap creation", "existed": true, "expiration_time": null, "hash": 8756689457056, "hosts_list": [], "id": "85899355291", "io_limit_policy": null, "is_auto_delete": true, "is_modifiable": false, "is_modified": false, "is_read_only": true, "is_system_snap": false, "last_writable_time": null, "lun": null, "name": "ansible_snap_cg_1_1", "parent_snap": null, "size": null, "snap_group": null, "state": "SnapStateEnum.READY", "storage_resource_id": "res_95", "storage_resource_name": "CG_ansible_test_2_new"}` |
| **expiration_time**  string | Date and time after which the snapshot will expire.  **Returned:** success |
| **hosts_list**  dictionary | Contains the name and id of the associated hosts.  **Returned:** success |
| **id**  string | Unique identifier of the snapshot instance.  **Returned:** success |
| **is_auto_delete**  string | Additional information mentioned for snapshot.  **Returned:** success |
| **name**  string | The name of the snapshot.  **Returned:** success |
| **storage_resource_id**  string | Id of the storage resource for which the snapshot exists.  **Returned:** success |
| **storage_resource_name**  string | Name of the storage resource for which the snapshot exists.  **Returned:** success |

### Authors

- P Srinivas Rao (@srinivas-rao5)

### Collection links

- [Issue Tracker](https://www.dell.com/community/Automation/bd-p/Automation)
- [Repository (Sources)](https://github.com/dell/ansible-unity/tree/1.7.1)
