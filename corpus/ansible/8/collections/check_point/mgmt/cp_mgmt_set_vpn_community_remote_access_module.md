---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_set_vpn_community_remote_access module – Edit existing Remote Access object. Using object name or uid is optional."
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_set_vpn_community_remote_access_module.html
fetched_at: 2026-07-28T01:17:35+00:00
---
# check_point.mgmt.cp_mgmt_set_vpn_community_remote_access module – Edit existing Remote Access object. Using object name or uid is optional.

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_set_vpn_community_remote_access`.

New in check_point.mgmt 5.0.0

- [Synopsis](cp_mgmt_set_vpn_community_remote_access_module.md#synopsis)
- [Parameters](cp_mgmt_set_vpn_community_remote_access_module.md#parameters)
- [Examples](cp_mgmt_set_vpn_community_remote_access_module.md#examples)
- [Return Values](cp_mgmt_set_vpn_community_remote_access_module.md#return-values)

## [Synopsis](cp_mgmt_set_vpn_community_remote_access_module.md#id1)

- Edit existing Remote Access object. Using object name or uid is optional.
- Add and Delete API commands for this object are unavailable since there is single object per domain.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_set_vpn_community_remote_access_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **color**  string | Color of the object. Should be one of existing colors.  **Choices:**   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **gateways**  list / elements=string | Collection of Gateway objects identified by the name or UID. |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **name**  string | Object name. |
| **tags**  list / elements=string | Collection of tag identifiers. |
| **user_groups**  list / elements=string | Collection of User group objects identified by the name or UID. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_set_vpn_community_remote_access_module.md#id3)

```yaml+jinja
- name: set-vpn-community-remote-access
  cp_mgmt_set_vpn_community_remote_access:
    gateways:
    - mygateway
    user_groups:
    - myusergroup
```

## [Return Values](cp_mgmt_set_vpn_community_remote_access_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_set_vpn_community_remote_access**  dictionary | The checkpoint set-vpn-community-remote-access output.  **Returned:** always. |

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
