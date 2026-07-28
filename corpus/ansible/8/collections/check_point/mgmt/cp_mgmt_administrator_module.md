---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_administrator module – Manages administrator objects on Checkpoint over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_administrator_module.html
fetched_at: 2026-07-28T01:15:47+00:00
---
# check_point.mgmt.cp_mgmt_administrator module – Manages administrator objects on Checkpoint over Web Services API

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_administrator`.

New in check_point.mgmt 1.0.0

- [Synopsis](cp_mgmt_administrator_module.md#synopsis)
- [Parameters](cp_mgmt_administrator_module.md#parameters)
- [Examples](cp_mgmt_administrator_module.md#examples)
- [Return Values](cp_mgmt_administrator_module.md#return-values)

## [Synopsis](cp_mgmt_administrator_module.md#id1)

- Manages administrator objects on Checkpoint devices including creating, updating and removing objects.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_administrator_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **authentication_method**  string | Authentication method.  **Choices:**   - `"undefined"` - `"check point password"` - `"os password"` - `"securid"` - `"radius"` - `"tacacs"` - `"ad authentication"` - `"api key"` |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  **Choices:**   - `false` - `true` |
| **color**  string | Color of the object. Should be one of existing colors.  **Choices:**   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **email**  string | Administrator email. |
| **expiration_date**  string | Format, YYYY-MM-DD, YYYY-mm-ddThh,mm,ss. |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **multi_domain_profile**  string | Administrator multi-domain profile. |
| **must_change_password**  boolean | True if administrator must change password on the next login.  **Choices:**   - `false` - `true` |
| **name**  string / required | Object name. |
| **password**  string | Administrator password. |
| **password_hash**  string | Administrator password hash. |
| **permissions_profile**  string | Permission profile |
| **permissions_profile_list**  list / elements=dictionary | Administrator permissions profile. Permissions profile should not be provided when multi-domain-profile is set to “Multi-Domain Super User” or “Domain Super User”. Used only in MDS. |
| **domain**  string | Domain. |
| **profile**  string | Permission profile. |
| **phone_number**  string | Administrator phone number. |
| **radius_server**  string | RADIUS server object identified by the name or UID. Must be set when “authentication-method” was selected to be “RADIUS”. |
| **state**  string | State of the access rule (present or absent). Defaults to present.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tacacs_server**  string | TACACS server object identified by the name or UID. Must be set when “authentication-method” was selected to be “TACACS”. |
| **tags**  list / elements=string | Collection of tag identifiers. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_administrator_module.md#id3)

```yaml+jinja
- name: add-administrator
  cp_mgmt_administrator:
    authentication_method: check point password
    email: admin@gmail.com
    must_change_password: false
    name: admin
    password: secret
    permissions_profile: read write all
    phone_number: 1800-800-800
    state: present

- name: set-administrator
  cp_mgmt_administrator:
    name: admin
    password: new secret
    permissions_profile: read only profile
    state: present

- name: delete-administrator
  cp_mgmt_administrator:
    name: admin
    state: absent

- name: add-administrator-in-MDS
  cp_mgmt_administrator:
    authentication_method: check point password
    email: admin@gmail.com
    must_change_password: false
    name: admin
    password: secret
    permissions_profile_list:
      profile: read write all
      domain: dom1
    phone_number: 1800-800-800
    state: present
```

## [Return Values](cp_mgmt_administrator_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_administrator**  dictionary | The checkpoint object created or updated.  **Returned:** always, except when deleting the object. |

### Authors

- Or Soffer (@chkp-orso)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
