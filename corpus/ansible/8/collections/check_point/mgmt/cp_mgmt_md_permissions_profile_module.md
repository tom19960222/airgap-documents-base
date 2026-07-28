---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_md_permissions_profile module – Manages md-permissions-profile objects on Checkpoint over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_md_permissions_profile_module.html
fetched_at: 2026-07-28T01:16:47+00:00
---
# check_point.mgmt.cp_mgmt_md_permissions_profile module – Manages md-permissions-profile objects on Checkpoint over Web Services API

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_md_permissions_profile`.

New in check_point.mgmt 3.0.0

- [Synopsis](cp_mgmt_md_permissions_profile_module.md#synopsis)
- [Parameters](cp_mgmt_md_permissions_profile_module.md#parameters)
- [Examples](cp_mgmt_md_permissions_profile_module.md#examples)
- [Return Values](cp_mgmt_md_permissions_profile_module.md#return-values)

## [Synopsis](cp_mgmt_md_permissions_profile_module.md#id1)

- Manages md-permissions-profile objects on Checkpoint devices including creating, updating and removing objects.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_md_permissions_profile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  **Choices:**   - `false` - `true` |
| **cme_operations**  string | Permission to read / edit the Cloud Management Extension (CME) configuration.  **Choices:**   - `"read"` - `"write"` - `"disabled"` |
| **color**  string | Color of the object. Should be one of existing colors.  **Choices:**   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **default_profile_global_domains**  string | Name or UID of the required default profile for all global domains. |
| **default_profile_local_domains**  string | Name or UID of the required default profile for all local domains. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **domains_to_process**  list / elements=string | Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from the System Domain only and with ignore-warnings true. Valid values are, CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER. |
| **enable_default_profile_for_global_domains**  boolean | Enable the option to specify a default profile for all global domains.  **Choices:**   - `false` - `true` |
| **enable_default_profile_for_local_domains**  boolean | Enable the option to specify a default profile for all local domains.  **Choices:**   - `false` - `true` |
| **global_vpn_management**  boolean | Lets the administrator select Enable global use for a Security Gateway shown in the MDS Gateways & Servers view.<br>Only a ‘Manager’ permission-level profile can edit this permission.  **Choices:**   - `false` - `true` |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **manage_admins**  boolean | Create and manage Multi-Domain Security Management administrators with the same or lower permission level. For example, a Domain manager cannot create Superusers or global managers.<br>Only a ‘Manager’ permission-level profile can edit this permission.  **Choices:**   - `false` - `true` |
| **manage_global_assignments**  boolean | Controls the ability to create, edit and delete global assignment and not the ability to reassign, which is set according to the specific Domain’s permission profile.  **Choices:**   - `false` - `true` |
| **manage_sessions**  boolean | Connect/disconnect Domain sessions, publish changes, and delete other administrator sessions.<br>Only a ‘Manager’ permission-level profile can edit this permission.  **Choices:**   - `false` - `true` |
| **management_api_login**  boolean | Permission to log in to the Security Management Server and run API commands using these tools, mgmt_cli (Linux and Windows binaries), Gaia CLI (clish) and Web Services (REST). Useful if you want to prevent administrators from running automatic scripts on the Management.<br>Note, This permission is not required to run commands from within the API terminal in SmartConsole.  **Choices:**   - `false` - `true` |
| **mds_provisioning**  boolean | Create and manage Multi-Domain Servers and Multi-Domain Log Servers.<br>Only a “Super User” permission-level profile can select this option.  **Choices:**   - `false` - `true` |
| **name**  string / required | Object name. |
| **permission_level**  string | The level of the Multi Domain Permissions Profile.<br>The level cannot be changed after creation.  **Choices:**   - `"super user"` - `"manager"` - `"domain level only"` |
| **state**  string | State of the access rule (present or absent). Defaults to present.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=string | Collection of tag identifiers. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **view_global_objects_in_domain**  boolean | Lets an administrator with no global objects permissions view the global objects in the domain. This option is required for valid domain management.  **Choices:**   - `false` - `true` |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_md_permissions_profile_module.md#id3)

```yaml+jinja
- name: add-md-permissions-profile
  cp_mgmt_md_permissions_profile:
    name: manager profile
    state: present

- name: set-md-permissions-profile
  cp_mgmt_md_permissions_profile:
    default_profile_global_domains: read write all
    name: manager profile
    permission_level: domain level only
    state: present

- name: delete-md-permissions-profile
  cp_mgmt_md_permissions_profile:
    name: profile
    state: absent
```

## [Return Values](cp_mgmt_md_permissions_profile_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_md_permissions_profile**  dictionary | The checkpoint object created or updated.  **Returned:** always, except when deleting the object. |

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
