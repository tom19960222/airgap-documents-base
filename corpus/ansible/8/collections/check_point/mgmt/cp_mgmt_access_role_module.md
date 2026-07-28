---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_access_role module – Manages access-role objects on Check Point over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_access_role_module.html
fetched_at: 2026-07-28T01:15:37+00:00
---
# check_point.mgmt.cp_mgmt_access_role module – Manages access-role objects on Check Point over Web Services API

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_access_role`.

New in check_point.mgmt 1.0.0

- [Synopsis](cp_mgmt_access_role_module.md#synopsis)
- [Parameters](cp_mgmt_access_role_module.md#parameters)
- [Examples](cp_mgmt_access_role_module.md#examples)
- [Return Values](cp_mgmt_access_role_module.md#return-values)

## [Synopsis](cp_mgmt_access_role_module.md#id1)

- Manages access-role objects on Check Point devices including creating, updating and removing objects.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_access_role_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  **Choices:**   - `false` - `true` |
| **color**  string | Color of the object. Should be one of existing colors.  **Choices:**   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **machines**  string | Any or All Identified.  **Choices:**   - `"any"` - `"all identified"` |
| **machines_list**  list / elements=dictionary | Machines that can access the system. |
| **base_dn**  string | When source is “Active Directory” use “base-dn” to refine the query in AD database. |
| **selection**  list / elements=string | Name or UID of an object selected from source. |
| **source**  string | Active Directory name or UID or Identity Tag. |
| **name**  string / required | Object name. |
| **networks**  list / elements=string | Collection of Network objects identified by the name or UID that can access the system. |
| **remote_access_clients**  string | Remote access clients identified by name or UID. |
| **state**  string | State of the access rule (present or absent). Defaults to present.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=string | Collection of tag identifiers. |
| **users**  string | Any or All Identified.  **Choices:**   - `"any"` - `"all identified"` |
| **users_list**  list / elements=dictionary | Users that can access the system. |
| **base_dn**  string | When source is “Active Directory” use “base-dn” to refine the query in AD database. |
| **selection**  list / elements=string | Name or UID of an object selected from source. |
| **source**  string | Active Directory name or UID or Identity Tag or Internal User Groups or LDAP groups or Guests. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_access_role_module.md#id3)

```yaml+jinja
- name: add-access-role
  cp_mgmt_access_role:
    name: New Access Role 1
    networks: any
    remote_access_clients: any
    state: present
    users: any

- name: set-access-role
  cp_mgmt_access_role:
    users_list:
        - source: "Internal User Groups"
          selection: usersGroup
    name: New Access Role 1
    state: present

- name: delete-access-role
  cp_mgmt_access_role:
    name: New Access Role 1
    state: absent
```

## [Return Values](cp_mgmt_access_role_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_access_role**  dictionary | The checkpoint object created or updated.  **Returned:** always, except when deleting the object. |

### Authors

- Or Soffer (@chkp-orso)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
