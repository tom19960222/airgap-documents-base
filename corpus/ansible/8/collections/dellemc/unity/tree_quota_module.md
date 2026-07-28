---
collection: ansible
version: "8"
title: "dellemc.unity.tree_quota module – Manage quota tree on the Unity storage system"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/unity/tree_quota_module.html
fetched_at: 2026-07-28T02:05:32+00:00
---
# dellemc.unity.tree_quota module – Manage quota tree on the Unity storage system

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
> see [Requirements](tree_quota_module.md#ansible-collections-dellemc-unity-tree-quota-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.unity.tree_quota`.

New in dellemc.unity 1.2.0

- [Synopsis](tree_quota_module.md#synopsis)
- [Requirements](tree_quota_module.md#requirements)
- [Parameters](tree_quota_module.md#parameters)
- [Notes](tree_quota_module.md#notes)
- [Examples](tree_quota_module.md#examples)
- [Return Values](tree_quota_module.md#return-values)

## [Synopsis](tree_quota_module.md#id1)

- Managing Quota tree on the Unity storage system includes Create quota tree, Get quota tree, Modify quota tree and Delete quota tree.

Aliases: dellemc_unity_tree_quota

## [Requirements](tree_quota_module.md#id2)

The below requirements are needed on the host that executes this module.

- A Dell Unity Storage device version 5.1 or later.
- Ansible-core 2.13 or later.
- Python 3.9, 3.10 or 3.11.
- Storops Python SDK 1.2.11.

## [Parameters](tree_quota_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cap_unit**  string | Unit of *soft_limit* and *hard_limit* size.  It defaults to `GB` if not specified.  **Choices:**   - `"MB"` - `"GB"` - `"TB"` |
| **description**  string | Description of a quota tree. |
| **filesystem_id**  string | The ID of the filesystem for which the quota tree is created.  For creation of a quota tree either *filesystem_id* or *filesystem_name* is required. |
| **filesystem_name**  string | The name of the filesystem for which quota tree is created.  For creation or modification of a quota tree either *filesystem_name* or *filesystem_id* is required. |
| **hard_limit**  integer | Hard limitation for a quota tree on the total space available. If exceeded, users in quota tree cannot write data.  Value `0` implies no limit.  One of the values of *soft_limit* and *hard_limit* can be `0`, however, both cannot be both `0` during creation of a quota tree. |
| **nas_server_id**  string | The ID of the NAS server in which the filesystem is created.  For creation of a quota tree either *filesystem_id* or *filesystem_name* is required. |
| **nas_server_name**  string | The name of the NAS server in which the filesystem is created.  For creation of a quota tree either *nas_server_name* or *nas_server_id* is required. |
| **password**  string / required | The password of the Unity management server. |
| **path**  string | The path to the quota tree.  Either *tree_quota_id* or *path* to quota tree is required to create/view/modify/delete a quota tree.  Path must start with a forward slash ‘/’. |
| **port**  integer | Port number through which communication happens with Unity management server.  **Default:** `443` |
| **soft_limit**  integer | Soft limitation for a quota tree on the total space available. If exceeded, notification will be sent to users in the quota tree for the grace period mentioned, beyond which users cannot use space.  Value `0` implies no limit.  Both *soft_limit* and *hard_limit* cannot be `0` during creation of quota tree. |
| **state**  string / required | The state option is used to mention the existence of the filesystem quota tree.  **Choices:**   - `"absent"` - `"present"` |
| **tree_quota_id**  string | The ID of the quota tree.  Either *tree_quota_id* or *path* to quota tree is required to view/modify/delete quota tree. |
| **unispherehost**  string / required | IP or FQDN of the Unity management server. |
| **username**  string / required | The username of the Unity management server. |
| **validate_certs**  aliases: verifycert  boolean | Boolean variable to specify whether or not to validate SSL certificate.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](tree_quota_module.md#id4)

> **Note:**
>
> - The *check_mode* is not supported.
> - The modules present in this collection named as ‘dellemc.unity’ are built to support the Dell Unity storage platform.

## [Examples](tree_quota_module.md#id5)

```yaml+jinja
- name: Get quota tree details by quota tree id
  dellemc.unity.tree_quota:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    tree_quota_id: "treequota_171798700679_10"
    state: "present"

- name: Get quota tree details by quota tree path
  dellemc.unity.tree_quota:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    filesystem_name: "fs_2171"
    nas_server_id: "nas_21"
    path: "/test"
    state: "present"

- name: Create quota tree for a filesystem with filesystem id
  dellemc.unity.tree_quota:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    filesystem_id: "fs_2171"
    hard_limit: 6
    cap_unit: "TB"
    soft_limit: 5
    path: "/test_new"
    state: "present"

- name: Create quota tree for a filesystem with filesystem name
  dellemc.unity.tree_quota:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    filesystem_name: "Test_filesystem"
    nas_server_name: "lglad068"
    hard_limit: 6
    cap_unit: "TB"
    soft_limit:  5
    path: "/test_new"
    state: "present"

- name: Modify quota tree limit usage by quota tree path
  dellemc.unity.tree_quota:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    path: "/test_new"
    hard_limit: 10
    cap_unit: "TB"
    soft_limit: 8
    state: "present"

- name: Modify quota tree by quota tree id
  dellemc.unity.tree_quota:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    filesystem_id: "fs_2171"
    tree_quota_id: "treequota_171798700679_10"
    hard_limit: 12
    cap_unit: "TB"
    soft_limit: 10
    state: "present"

- name: Delete quota tree by quota tree id
  dellemc.unity.tree_quota:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    filesystem_id: "fs_2171"
    tree_quota_id: "treequota_171798700679_10"
    state: "absent"

- name: Delete quota tree by path
  dellemc.unity.tree_quota:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    filesystem_id: "fs_2171"
    path: "/test_new"
    state: "absent"
```

## [Return Values](tree_quota_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether or not the resource has changed.  **Returned:** always  **Sample:** `true` |
| **get_tree_quota_details**  dictionary | Details of the quota tree.  **Returned:** When quota tree exists  **Sample:** `{"description": "", "existed": true, "filesystem": {"UnityFileSystem": {"hash": 8788549469862, "id": "fs_137", "name": "test", "nas_server": {"id": "nas_1", "name": "lglad072"}}}, "gp_left": null, "hard_limit": "6.0 TB", "hash": 8788549497558, "id": "treequota_171798694897_1", "path": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER", "size_used": 0, "soft_limit": "5.0 TB", "state": 0}` |
| **description**  string | Description of the quota tree.  **Returned:** success |
| **filesystem**  dictionary | Filesystem details for which the quota tree is created.  **Returned:** success |
| **UnityFileSystem**  dictionary | Filesystem details for which the quota tree is created.  **Returned:** success |
| **id**  string | ID of the filesystem for which the quota tree is create.  **Returned:** success |
| **gp_left**  integer | The grace period left after the soft limit for the user quota is exceeded.  **Returned:** success |
| **hard_limit**  integer | Hard limit of quota tree. If the quota tree’s space usage exceeds the hard limit, users in quota tree cannot write data.  **Returned:** success |
| **id**  string | Quota tree ID.  **Returned:** success |
| **path**  string | Path to quota tree. A valid path must start with a forward slash ‘/’. It is mandatory while creating a quota tree.  **Returned:** success |
| **size_used**  integer | Size of used space in the filesystem by the user files.  **Returned:** success |
| **soft_limit**  integer | Soft limit of the quota tree. If the quota tree’s space usage exceeds the soft limit, the storage system starts to count down based on the specified grace period.  **Returned:** success |
| **state**  integer | State of the quota tree.  **Returned:** success |

### Authors

- Spandita Panigrahi (@panigs7)

### Collection links

- [Issue Tracker](https://www.dell.com/community/Automation/bd-p/Automation)
- [Repository (Sources)](https://github.com/dell/ansible-unity/tree/1.7.1)
