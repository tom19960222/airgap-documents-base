---
collection: ansible
version: "6"
title: "check_point.mgmt.cp_mgmt_add_domain module – Create new object"
source_url: https://docs.ansible.com/projects/ansible/6/collections/check_point/mgmt/cp_mgmt_add_domain_module.html
fetched_at: 2026-07-27T16:47:36+00:00
---
# check_point.mgmt.cp_mgmt_add_domain module – Create new object

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_add_domain`.

New in check_point.mgmt 2.9

- [Synopsis](cp_mgmt_add_domain_module.md#synopsis)
- [Parameters](cp_mgmt_add_domain_module.md#parameters)
- [Examples](cp_mgmt_add_domain_module.md#examples)
- [Return Values](cp_mgmt_add_domain_module.md#return-values)

## [Synopsis](cp_mgmt_add_domain_module.md#id1)

- Create new object
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_add_domain_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **color**  string | Color of the object. Should be one of existing colors.  Choices:   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  Choices:   - `"uid"` - `"standard"` - `"full"` |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  Choices:   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  Choices:   - `false` - `true` |
| **name**  string / required | Object name. |
| **servers**  list / elements=string | Domain servers. When this field is provided, ‘set-domain’ command is executed asynchronously. |
| **active**  boolean | Activate domain server. Only one domain server is allowed to be active  Choices:   - `false` - `true` |
| **ip_address**  string | IPv4 or IPv6 address. If both addresses are required use ipv4-address and ipv6-address fields explicitly. |
| **ipv4_address**  string | IPv4 address. |
| **ipv6_address**  string | IPv6 address. |
| **multi_domain_server**  string | Multi Domain server name or UID. |
| **name**  string | Object name. Must be unique in the domain. |
| **skip_start_domain_server**  boolean | Set this value to be true to prevent starting the new created domain.  Choices:   - `false` - `true` |
| **type**  string | Domain server type.  Choices:   - `"management server"` - `"log server"` - `"smc"` |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  Choices:   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  Default: `30` |

## [Examples](cp_mgmt_add_domain_module.md#id3)

```yaml+jinja
- name: add-domain
  cp_mgmt_add_domain:
    name: domain1
    servers:
      ip_address: 192.0.2.1
      multi_domain_server: MDM_Server
      name: domain1_ManagementServer_1
```

## [Return Values](cp_mgmt_add_domain_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_domain**  dictionary | The checkpoint add-domain output.  Returned: always. |

### Authors

- Or Soffer (@chkp-orso)

### Collection links

[Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
[Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
