---
collection: ansible
version: "8"
title: "dellemc.unity.user_quota module – Manage user quota on the Unity storage system"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/unity/user_quota_module.html
fetched_at: 2026-07-28T02:05:33+00:00
---
# dellemc.unity.user_quota module – Manage user quota on the Unity storage system

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
> see [Requirements](user_quota_module.md#ansible-collections-dellemc-unity-user-quota-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.unity.user_quota`.

New in dellemc.unity 1.2.0

- [Synopsis](user_quota_module.md#synopsis)
- [Requirements](user_quota_module.md#requirements)
- [Parameters](user_quota_module.md#parameters)
- [Notes](user_quota_module.md#notes)
- [Examples](user_quota_module.md#examples)
- [Return Values](user_quota_module.md#return-values)

## [Synopsis](user_quota_module.md#id1)

- Managing User Quota on the Unity storage system includes Create user quota, Get user quota, Modify user quota, Delete user quota, Create user quota for quota tree, Modify user quota for quota tree and Delete user quota for quota tree.

Aliases: dellemc_unity_user_quota

## [Requirements](user_quota_module.md#id2)

The below requirements are needed on the host that executes this module.

- A Dell Unity Storage device version 5.1 or later.
- Ansible-core 2.13 or later.
- Python 3.9, 3.10 or 3.11.
- Storops Python SDK 1.2.11.

## [Parameters](user_quota_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cap_unit**  string | Unit of *soft_limit* and *hard_limit* size.  It defaults to `GB` if not specified.  **Choices:**   - `"MB"` - `"GB"` - `"TB"` |
| **filesystem_id**  string | The ID of the filesystem for which the user quota is created.  For creation of a user quota either *filesystem_id* or *filesystem_name* is required. |
| **filesystem_name**  string | The name of the filesystem for which the user quota is created.  For creation of a user quota either *filesystem_name* or *filesystem_id* is required. |
| **hard_limit**  integer | Hard limitation for a user on the total space available. If exceeded, user cannot write data.  Value `0` implies no limit.  One of the values of *soft_limit* and *hard_limit* can be `0`, however, both cannot be `0` during creation or modification of user quota. |
| **nas_server_id**  string | The ID of the NAS server in which the filesystem is created.  For creation of a user quota either *filesystem_id* or *filesystem_name* is required. |
| **nas_server_name**  string | The name of the NAS server in which the filesystem is created.  For creation of a user quota either *nas_server_name* or *nas_server_id* is required. |
| **password**  string / required | The password of the Unity management server. |
| **path**  string | The path to the quota tree.  Either *tree_quota_id* or *path* to quota tree is required to create/modify/delete user quota for a quota tree.  Path must start with a forward slash ‘/’. |
| **port**  integer | Port number through which communication happens with Unity management server.  **Default:** `443` |
| **soft_limit**  integer | Soft limitation for a user on the total space available. If exceeded, notification will be sent to the user for the grace period mentioned, beyond which the user cannot use space.  Value `0` implies no limit.  Both *soft_limit* and *hard_limit* cannot be `0` during creation or modification of user quota. |
| **state**  string / required | The *state* option is used to mention the existence of the user quota.  **Choices:**   - `"absent"` - `"present"` |
| **tree_quota_id**  string | The ID of the quota tree.  Either *tree_quota_id* or *path* to quota tree is required to create/modify/delete user quota for a quota tree. |
| **uid**  string | User ID of the user quota. |
| **unispherehost**  string / required | IP or FQDN of the Unity management server. |
| **user_name**  string | User name of the user quota when *user_type* is `Windows` or `Unix`.  Option *user_name* must be specified along with *win_domain* when *user_type* is `Windows`. |
| **user_quota_id**  string | User quota ID generated after creation of a user quota. |
| **user_type**  string | Type of user creating a user quota.  Mandatory while creating or modifying user quota.  **Choices:**   - `"Unix"` - `"Windows"` |
| **username**  string / required | The username of the Unity management server. |
| **validate_certs**  aliases: verifycert  boolean | Boolean variable to specify whether or not to validate SSL certificate.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |
| **win_domain**  string | Fully qualified or short domain name for Windows user type.  Mandatory when *user_type* is `Windows`. |

## [Notes](user_quota_module.md#id4)

> **Note:**
>
> - The *check_mode* is not supported.
> - The modules present in this collection named as ‘dellemc.unity’ are built to support the Dell Unity storage platform.

## [Examples](user_quota_module.md#id5)

```yaml+jinja
- name: Get user quota details by user quota id
  dellemc.unity.user_quota:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    user_quota_id: "userquota_171798700679_0_123"
    state: "present"

- name: Get user quota details by user quota uid/user name
  dellemc.unity.user_quota:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    filesystem_name: "fs_2171"
    nas_server_id: "nas_21"
    user_name: "test"
    state: "present"

- name: Create user quota for a filesystem with filesystem id
  dellemc.unity.user_quota:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    filesystem_id: "fs_2171"
    hard_limit: 6
    cap_unit: "TB"
    soft_limit: 5
    uid: "111"
    state: "present"

- name: Create user quota for a filesystem with filesystem name
  dellemc.unity.user_quota:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    filesystem_name: "Test_filesystem"
    nas_server_name: "lglad068"
    hard_limit: 6
    cap_unit: "TB"
    soft_limit:  5
    uid: "111"
    state: "present"

- name: Modify user quota limit usage by user quota id
  dellemc.unity.user_quota:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    user_quota_id: "userquota_171798700679_0_123"
    hard_limit: 10
    cap_unit: "TB"
    soft_limit: 8
    state: "present"

- name: Modify user quota by filesystem id and user quota uid/user_name
  dellemc.unity.user_quota:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    filesystem_id: "fs_2171"
    user_type: "Windows"
    win_domain: "prod"
    user_name: "sample"
    hard_limit: 12
    cap_unit: "TB"
    soft_limit: 10
    state: "present"

- name: Delete user quota
  dellemc.unity.user_quota:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    filesystem_id: "fs_2171"
    win_domain: "prod"
    user_name: "sample"
    state: "absent"

- name: Create user quota of a quota tree
  dellemc.unity.user_quota:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    tree_quota_id: "treequota_171798700679_4"
    user_type: "Windows"
    win_domain: "prod"
    user_name: "sample"
    soft_limit: 9
    cap_unit: "TB"
    state: "present"

- name: Create user quota of a quota tree by quota tree path
  dellemc.unity.user_quota:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    filesystem_id: "fs_2171"
    path: "/sample"
    user_type: "Unix"
    user_name: "test"
    hard_limit: 2
    cap_unit: "TB"
    state: "present"

- name: Modify user quota of a quota tree
  dellemc.unity.user_quota:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    tree_quota_id: "treequota_171798700679_4"
    user_type: "Windows"
    win_domain: "prod"
    user_name: "sample"
    soft_limit: 10
    cap_unit: "TB"
    state: "present"

- name: Modify user quota of a quota tree by quota tree path
  dellemc.unity.user_quota:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    filesystem_id: "fs_2171"
    path: "/sample"
    user_type: "Windows"
    win_domain: "prod"
    user_name: "sample"
    hard_limit: 12
    cap_unit: "TB"
    state: "present"

- name: Delete user quota of a quota tree by quota tree path
  dellemc.unity.user_quota:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    filesystem_id: "fs_2171"
    path: "/sample"
    win_domain: "prod"
    user_name: "sample"
    state: "absent"

- name: Delete user quota of a quota tree by quota tree id
  dellemc.unity.user_quota:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    tree_quota_id: "treequota_171798700679_4"
    win_domain: "prod"
    user_name: "sample"
    state: "absent"
```

## [Return Values](user_quota_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether or not the resource has changed.  **Returned:** always  **Sample:** `true` |
| **get_user_quota_details**  dictionary | Details of the user quota.  **Returned:** When user quota exists  **Sample:** `{"existed": true, "filesystem": {"UnityFileSystem": {"hash": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER", "id": "fs_120", "name": "nfs-multiprotocol", "nas_server": {"id": "nas_1", "name": "lglad072"}}}, "gp_left": null, "hard_limit": "10.0 GB", "hard_ratio": null, "hash": 8752448438089, "id": "userquota_171798694698_0_60000", "size_used": 0, "soft_limit": "10.0 GB", "soft_ratio": null, "state": 0, "tree_quota": null, "uid": 60000, "unix_name": null, "windows_names": null, "windows_sids": null}` |
| **filesystem**  dictionary | Filesystem details for which the user quota is created.  **Returned:** success |
| **UnityFileSystem**  dictionary | Filesystem details for which the user quota is created.  **Returned:** success |
| **id**  string | ID of the filesystem for which the user quota is created.  **Returned:** success |
| **name**  string | Name of filesystem.  **Returned:** success |
| **nas_server**  dictionary | Nasserver details where filesystem is created.  **Returned:** success |
| **id**  string | ID of nasserver.  **Returned:** success |
| **name**  string | Name of nasserver.  **Returned:** success |
| **gp_left**  integer | The grace period left after the soft limit for the user quota is exceeded.  **Returned:** success |
| **hard_limit**  integer | Hard limitation for a user on the total space available. If exceeded, user cannot write data.  **Returned:** success |
| **hard_ratio**  string | The hard ratio is the ratio between the hard limit size of the user quota and the amount of storage actually consumed.  **Returned:** success |
| **id**  string | User quota ID.  **Returned:** success |
| **size_used**  integer | Size of used space in the filesystem by the user files.  **Returned:** success |
| **soft_limit**  integer | Soft limitation for a user on the total space available. If exceeded, notification will be sent to user for the grace period mentioned, beyond which user cannot use space.  **Returned:** success |
| **soft_ratio**  string | The soft ratio is the ratio between the soft limit size of the user quota and the amount of storage actually consumed.  **Returned:** success |
| **state**  integer | State of the user quota.  **Returned:** success |
| **tree_quota**  dictionary | Quota tree details for which the user quota is created.  **Returned:** success |
| **UnityTreeQuota**  dictionary | Quota tree details for which the user quota is created.  **Returned:** success |
| **id**  string | ID of the quota tree.  **Returned:** success |
| **path**  string | Path to quota tree.  **Returned:** success |
| **uid**  integer | User ID of the user.  **Returned:** success |
| **unix_name**  string | Unix user name for this user quota’s uid.  **Returned:** success |
| **windows_names**  string | Windows user name that maps to this quota’s uid.  **Returned:** success |
| **windows_sids**  string | Windows SIDs that maps to this quota’s uid  **Returned:** success |

### Authors

- Spandita Panigrahi (@panigs7)

### Collection links

- [Issue Tracker](https://www.dell.com/community/Automation/bd-p/Automation)
- [Repository (Sources)](https://github.com/dell/ansible-unity/tree/1.7.1)
