---
collection: ansible
version: "8"
title: "dellemc.unity.smbshare module – Manage SMB shares on Unity storage system"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/unity/smbshare_module.html
fetched_at: 2026-07-28T02:05:29+00:00
---
# dellemc.unity.smbshare module – Manage SMB shares on Unity storage system

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
> see [Requirements](smbshare_module.md#ansible-collections-dellemc-unity-smbshare-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.unity.smbshare`.

New in dellemc.unity 1.1.0

- [Synopsis](smbshare_module.md#synopsis)
- [Requirements](smbshare_module.md#requirements)
- [Parameters](smbshare_module.md#parameters)
- [Notes](smbshare_module.md#notes)
- [Examples](smbshare_module.md#examples)
- [Return Values](smbshare_module.md#return-values)

## [Synopsis](smbshare_module.md#id1)

- Managing SMB Shares on Unity storage system includes create, get, modify, and delete the smb shares.

Aliases: dellemc_unity_smbshare

## [Requirements](smbshare_module.md#id2)

The below requirements are needed on the host that executes this module.

- A Dell Unity Storage device version 5.1 or later.
- Ansible-core 2.13 or later.
- Python 3.9, 3.10 or 3.11.
- Storops Python SDK 1.2.11.

## [Parameters](smbshare_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  string | Description for the SMB share.  Optional parameter when creating a share.  To modify, pass the new value in description field. |
| **filesystem_id**  string | The ID of the File System.  Either *filesystem_name* or *filesystem_id* is required for creation of the SMB share for filesystem.  If *filesystem_name* is specified, then *nas_server_name*/*nas_server_id* is required to uniquely identify the filesystem.  Options *filesystem_name* and *filesystem_id* are mutually exclusive parameters. |
| **filesystem_name**  string | The Name of the File System.  Either *filesystem_name* or *filesystem_id* is required for creation of the SMB share for filesystem.  If *filesystem_name* is specified, then *nas_server_name*/*nas_server_id* is required to uniquely identify the filesystem.  Options *filesystem_name* and *filesytem_id* are mutually exclusive parameters. |
| **is_abe_enabled**  boolean | Indicates whether Access-based Enumeration (ABE) for SMB share is enabled.  During creation, if not mentioned then default is `false`.  **Choices:**   - `false` - `true` |
| **is_branch_cache_enabled**  boolean | Indicates whether Branch Cache optimization for SMB share is enabled.  During creation, if not mentioned then default is `false`.  **Choices:**   - `false` - `true` |
| **is_continuous_availability_enabled**  boolean | Indicates whether continuous availability for SMB 3.0 is enabled.  During creation, if not mentioned then default is `false`.  **Choices:**   - `false` - `true` |
| **is_encryption_enabled**  boolean | Indicates whether encryption for SMB 3.0 is enabled at the shared folder level.  During creation, if not mentioned then default is `false`.  **Choices:**   - `false` - `true` |
| **nas_server_id**  string | The ID of the NAS Server.  It is not required if *share_id* is used. |
| **nas_server_name**  string | The Name of the NAS Server.  It is not required if *share_id* is used.  Options *nas_server_name* and *nas_server_id* are mutually exclusive parameters. |
| **offline_availability**  string | Defines valid states of Offline Availability.  `MANUAL`- Only specified files will be available offline.  `DOCUMENTS`- All files that users open will be available offline.  `PROGRAMS`- Program will preferably run from the offline cache even when connected to the network. All files that users open will be available offline.  `NONE`- Prevents clients from storing documents and programs in offline cache.  **Choices:**   - `"MANUAL"` - `"DOCUMENTS"` - `"PROGRAMS"` - `"NONE"` |
| **password**  string / required | The password of the Unity management server. |
| **path**  string | Local path to the file system/Snapshot or any existing sub-folder of the file system/Snapshot that is shared over the network.  Path is relative to the root of the filesystem.  Required for creation of the SMB share. |
| **port**  integer | Port number through which communication happens with Unity management server.  **Default:** `443` |
| **share_id**  string | ID of the SMB share.  Should not be specified during creation. Id is auto generated.  For all other operations either *share_name* or *share_id* is required.  If *share_id* is used then no need to pass nas_server/filesystem/snapshot/path. |
| **share_name**  string | Name of the SMB share.  Required during creation of the SMB share.  For all other operations either *share_name* or *share_id* is required. |
| **snapshot_id**  string | The ID of the Filesystem Snapshot.  Either *snapshot_name* or *snapshot_id* is required for creation of the SMB share for a snapshot.  If *snapshot_name* is specified, then *nas_server_name*/*nas_server_id* is required to uniquely identify the snapshot.  Options *snapshot_name* and *snapshot_id* are mutually exclusive parameters. |
| **snapshot_name**  string | The Name of the Filesystem Snapshot.  Either *snapshot_name* or *snapshot_id* is required for creation of the SMB share for a snapshot.  If *snapshot_name* is specified, then *nas_server_name*/*nas_server_id* is required to uniquely identify the snapshot.  Options *snapshot_name* and *snapshot_id* are mutually exclusive parameters. |
| **state**  string / required | Define whether the SMB share should exist or not.  Value `present` indicates that the share should exist on the system.  Value `absent` indicates that the share should not exist on the system.  **Choices:**   - `"absent"` - `"present"` |
| **umask**  string | The default UNIX umask for new files created on the SMB Share. |
| **unispherehost**  string / required | IP or FQDN of the Unity management server. |
| **username**  string / required | The username of the Unity management server. |
| **validate_certs**  aliases: verifycert  boolean | Boolean variable to specify whether or not to validate SSL certificate.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](smbshare_module.md#id4)

> **Note:**
>
> - When ID/Name of the filesystem/snapshot is passed then *nas_server* is not required. If passed, then filesystem/snapshot should exist for the mentioned *nas_server*, else the task will fail.
> - The *check_mode* is not supported.
> - The modules present in this collection named as ‘dellemc.unity’ are built to support the Dell Unity storage platform.

## [Examples](smbshare_module.md#id5)

```yaml+jinja
- name: Create SMB share for a filesystem
  dellemc.unity.smbshare:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    share_name: "sample_smb_share"
    filesystem_name: "sample_fs"
    nas_server_id: "NAS_11"
    path: "/sample_fs"
    description: "Sample SMB share created"
    is_abe_enabled: true
    is_branch_cache_enabled: true
    offline_availability: "DOCUMENTS"
    is_continuous_availability_enabled: true
    is_encryption_enabled: true
    umask: "777"
    state: "present"
- name: Modify Attributes of SMB share for a filesystem
  dellemc.unity.smbshare:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    share_name: "sample_smb_share"
    nas_server_name: "sample_nas_server"
    description: "Sample SMB share attributes updated"
    is_abe_enabled: false
    is_branch_cache_enabled: false
    offline_availability: "MANUAL"
    is_continuous_availability_enabled: "false"
    is_encryption_enabled: "false"
    umask: "022"
    state: "present"
- name: Create SMB share for a snapshot
  dellemc.unity.smbshare:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    share_name: "sample_snap_smb_share"
    snapshot_name: "sample_snapshot"
    nas_server_id: "NAS_11"
    path: "/sample_snapshot"
    description: "Sample SMB share created for snapshot"
    is_abe_enabled: true
    is_branch_cache_enabled: true
    is_continuous_availability_enabled: true
    is_encryption_enabled: true
    umask: "777"
    state: "present"
- name: Modify Attributes of SMB share for a snapshot
  dellemc.unity.smbshare:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    share_name: "sample_snap_smb_share"
    snapshot_name: "sample_snapshot"
    description: "Sample SMB share attributes updated for snapshot"
    is_abe_enabled: false
    is_branch_cache_enabled: false
    offline_availability: "MANUAL"
    is_continuous_availability_enabled: "false"
    is_encryption_enabled: "false"
    umask: "022"
    state: "present"
- name: Get details of SMB share
  dellemc.unity.smbshare:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    share_id: "{{smb_share_id}}"
    state: "present"
- name: Delete SMB share
  dellemc.unity.smbshare:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    share_id: "{{smb_share_id}}"
    state: "absent"
```

## [Return Values](smbshare_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether or not the resource has changed.  **Returned:** always  **Sample:** `true` |
| **smb_share_details**  dictionary | The SMB share details.  **Returned:** When share exists.  **Sample:** `{"creation_time": "2022-03-17 11:56:54.867000+00:00", "description": "", "existed": true, "export_paths": ["\\\\multi-prot-pie.extreme1.com\\multi-prot-hui", "\\\\10.230.24.26\\multi-prot-hui"], "filesystem": {"UnityFileSystem": {"hash": 8748426746492}}, "filesystem_id": "fs_140", "filesystem_name": "multi-prot-hui", "hash": 8748426746588, "id": "SMBShare_20", "is_abe_enabled": false, "is_ace_enabled": false, "is_branch_cache_enabled": false, "is_continuous_availability_enabled": false, "is_dfs_enabled": false, "is_encryption_enabled": false, "is_read_only": null, "modified_time": "2022-03-17 11:56:54.867000+00:00", "name": "multi-prot-hui", "nas_server_id": "nas_5", "nas_server_name": "multi-prot", "offline_availability": "CifsShareOfflineAvailabilityEnum.NONE", "path": "/", "snap": null, "type": "CIFSTypeEnum.CIFS_SHARE", "umask": "022"}` |
| **description**  string | Additional information about the share.  **Returned:** success  **Sample:** `"This share is created for demo purpose only."` |
| **filesystem_id**  string | The ID of the Filesystem.  **Returned:** success |
| **filesystem_name**  string | The Name of the filesystem  **Returned:** success |
| **id**  string | The ID of the SMB share.  **Returned:** success |
| **is_abe_enabled**  boolean | Whether Access Based enumeration is enforced or not.  **Returned:** success  **Sample:** `false` |
| **is_branch_cache_enabled**  boolean | Whether branch cache is enabled or not.  **Returned:** success  **Sample:** `false` |
| **is_continuous_availability_enabled**  boolean | Whether the share will be available continuously or not.  **Returned:** success  **Sample:** `false` |
| **is_encryption_enabled**  boolean | Whether encryption is enabled or not.  **Returned:** success  **Sample:** `false` |
| **name**  string | Name of the SMB share.  **Returned:** success  **Sample:** `"sample_smb_share"` |
| **nas_server_id**  string | The ID of the nas_server.  **Returned:** success |
| **nas_server_name**  string | The Name of the nas_server.  **Returned:** success |
| **snapshot_id**  string | The ID of the Snapshot.  **Returned:** success |
| **snapshot_name**  string | The Name of the Snapshot.  **Returned:** success |
| **umask**  string | Unix mask for the SMB share.  **Returned:** success |

### Authors

- P Srinivas Rao (@srinivas-rao5)

### Collection links

- [Issue Tracker](https://www.dell.com/community/Automation/bd-p/Automation)
- [Repository (Sources)](https://github.com/dell/ansible-unity/tree/1.7.1)
