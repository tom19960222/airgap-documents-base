---
collection: ansible
version: "6"
title: "check_point.mgmt.cp_mgmt_service_icmp module – Manages service-icmp objects on Check Point over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/check_point/mgmt/cp_mgmt_service_icmp_module.html
fetched_at: 2026-07-27T16:48:23+00:00
---
# check_point.mgmt.cp_mgmt_service_icmp module – Manages service-icmp objects on Check Point over Web Services API

> **Note:**
>
> This module is part of the [check_point.mgmt collection](https://galaxy.ansible.com/check_point/mgmt) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install check_point.mgmt`.
>
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_service_icmp`.

New in check_point.mgmt 2.9

- [Synopsis](cp_mgmt_service_icmp_module.md#synopsis)
- [Parameters](cp_mgmt_service_icmp_module.md#parameters)
- [Examples](cp_mgmt_service_icmp_module.md#examples)
- [Return Values](cp_mgmt_service_icmp_module.md#return-values)

## [Synopsis](cp_mgmt_service_icmp_module.md#id1)

- Manages service-icmp objects on Check Point devices including creating, updating and removing objects.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_service_icmp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  Choices:   - `false` - `true` |
| **color**  string | Color of the object. Should be one of existing colors.  Choices:   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  Choices:   - `"uid"` - `"standard"` - `"full"` |
| **groups**  list / elements=string | Collection of group identifiers. |
| **icmp_code**  integer | As listed in, <a href=”http,//www.iana.org/assignments/icmp-parameters” target=”_blank”>RFC 792</a>. |
| **icmp_type**  integer | As listed in, <a href=”http,//www.iana.org/assignments/icmp-parameters” target=”_blank”>RFC 792</a>. |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  Choices:   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  Choices:   - `false` - `true` |
| **keep_connections_open_after_policy_installation**  boolean | Keep connections open after policy has been installed even if they are not allowed under the new policy. This overrides the settings in the Connection Persistence page. If you change this property, the change will not affect open connections, but only future connections.  Choices:   - `false` - `true` |
| **name**  string / required | Object name. |
| **state**  string | State of the access rule (present or absent). Defaults to present.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=string | Collection of tag identifiers. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  Choices:   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  Default: `30` |

## [Examples](cp_mgmt_service_icmp_module.md#id3)

```yaml+jinja
- name: add-service-icmp
  cp_mgmt_service_icmp:
    icmp_code: 7
    icmp_type: 5
    name: Icmp1
    state: present

- name: set-service-icmp
  cp_mgmt_service_icmp:
    icmp_code: 13
    icmp_type: 45
    name: icmp1
    state: present

- name: delete-service-icmp
  cp_mgmt_service_icmp:
    name: icmp3
    state: absent
```

## [Return Values](cp_mgmt_service_icmp_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_service_icmp**  dictionary | The checkpoint object created or updated.  Returned: always, except when deleting the object. |

### Authors

- Or Soffer (@chkp-orso)

### Collection links

[Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
[Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
