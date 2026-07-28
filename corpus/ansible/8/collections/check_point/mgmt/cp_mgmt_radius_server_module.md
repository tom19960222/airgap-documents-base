---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_radius_server module – Manages radius-server objects on Checkpoint over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_radius_server_module.html
fetched_at: 2026-07-28T01:17:01+00:00
---
# check_point.mgmt.cp_mgmt_radius_server module – Manages radius-server objects on Checkpoint over Web Services API

> **Note:**
>
> This module is part of the [check_point.mgmt collection](https://galaxy.ansible.com/ui/repo/published/check_point/mgmt/) (version 5.1.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install check_point.mgmt`.
>
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_radius_server`.

New in check_point.mgmt 5.0.0

- [Synopsis](cp_mgmt_radius_server_module.md#synopsis)
- [Parameters](cp_mgmt_radius_server_module.md#parameters)
- [Examples](cp_mgmt_radius_server_module.md#examples)
- [Return Values](cp_mgmt_radius_server_module.md#return-values)

## [Synopsis](cp_mgmt_radius_server_module.md#id1)

- Manages radius-server objects on Checkpoint devices including creating, updating and removing objects.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_radius_server_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **accounting**  dictionary | Accounting settings. |
| **accounting_service**  string | The UID or Name of the the accounting interface to notify the server when users login and logout which will then lock and release the IP addresses that the server allocated to those users. |
| **enable_ip_pool_management**  boolean | IP pool management, enables Accounting service.  **Choices:**   - `false` - `true` |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  **Choices:**   - `false` - `true` |
| **color**  string | Color of the object. Should be one of existing colors.  **Choices:**   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **groups**  list / elements=string | Collection of group identifiers. |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **name**  string / required | Object name. |
| **priority**  integer | The priority of the RADIUS Server in case it is a member of a RADIUS Group. |
| **protocol**  string | The type of authentication protocol that will be used when authenticating the user to the RADIUS server.  **Choices:**   - `"PAP"` - `"MS_CHAP2"` |
| **server**  string | The UID or Name of the host that is the RADIUS Server. |
| **server_version**  string | The version can be either RADIUS Version 1.0, which is RFC 2138 compliant, and RADIUS Version 2.0 which is RFC 2865 compliant.  **Choices:**   - `"RADIUS Ver. 1.0"` - `"RADIUS Ver. 2.0"` |
| **service**  string | The UID or Name of the Service to which the RADIUS server listens. |
| **shared_secret**  string | The secret between the RADIUS server and the Security Gateway. |
| **state**  string | State of the access rule (present or absent). Defaults to present.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=string | Collection of tag identifiers. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_radius_server_module.md#id3)

```yaml+jinja
- name: add-radius-server
  cp_mgmt_radius_server:
    name: radServer
    server: hostRad
    shared_secret: '123'
    state: present

- name: set-radius-server
  cp_mgmt_radius_server:
    name: t4
    server: hostRadius
    state: present

- name: delete-radius-server
  cp_mgmt_radius_server:
    ignore_warnings: 'true'
    name: radiusServer
    state: absent
```

## [Return Values](cp_mgmt_radius_server_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_radius_server**  dictionary | The checkpoint object created or updated.  **Returned:** always, except when deleting the object. |

### Authors

- Shiran Golzar (@chkp-shirango)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
