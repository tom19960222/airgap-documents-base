---
collection: ansible
version: "6"
title: "check_point.mgmt.cp_mgmt_network module – Manages network objects on Check Point over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/check_point/mgmt/cp_mgmt_network_module.html
fetched_at: 2026-07-27T16:48:14+00:00
---
# check_point.mgmt.cp_mgmt_network module – Manages network objects on Check Point over Web Services API

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_network`.

New in check_point.mgmt 2.9

- [Synopsis](cp_mgmt_network_module.md#synopsis)
- [Parameters](cp_mgmt_network_module.md#parameters)
- [Examples](cp_mgmt_network_module.md#examples)
- [Return Values](cp_mgmt_network_module.md#return-values)

## [Synopsis](cp_mgmt_network_module.md#id1)

- Manages network objects on Check Point devices including creating, updating and removing objects.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_network_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  Choices:   - `false` - `true` |
| **broadcast**  string | Allow broadcast address inclusion.  Choices:   - `"disallow"` - `"allow"` |
| **color**  string | Color of the object. Should be one of existing colors.  Choices:   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  Choices:   - `"uid"` - `"standard"` - `"full"` |
| **groups**  list / elements=string | Collection of group identifiers. |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  Choices:   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  Choices:   - `false` - `true` |
| **mask_length**  integer | IPv4 or IPv6 network mask length. If both masks are required use mask-length4 and mask-length6 fields explicitly. Instead of IPv4 mask length it is possible to specify IPv4 mask itself in subnet-mask field. |
| **mask_length4**  integer | IPv4 network mask length. |
| **mask_length6**  integer | IPv6 network mask length. |
| **name**  string / required | Object name. |
| **nat_settings**  dictionary | NAT settings. |
| **auto_rule**  boolean | Whether to add automatic address translation rules.  Choices:   - `false` - `true` |
| **hide_behind**  string | Hide behind method. This parameter is not required in case “method” parameter is “static”.  Choices:   - `"gateway"` - `"ip-address"` |
| **install_on**  string | Which gateway should apply the NAT translation. |
| **ip_address**  string | IPv4 or IPv6 address. If both addresses are required use ipv4-address and ipv6-address fields explicitly. This parameter is not required in case “method” parameter is “hide” and “hide-behind” parameter is “gateway”. |
| **ipv4_address**  string | IPv4 address. |
| **ipv6_address**  string | IPv6 address. |
| **method**  string | NAT translation method.  Choices:   - `"hide"` - `"static"` |
| **state**  string | State of the access rule (present or absent). Defaults to present.  Choices:   - `"present"` ← (default) - `"absent"` |
| **subnet**  string | IPv4 or IPv6 network address. If both addresses are required use subnet4 and subnet6 fields explicitly. |
| **subnet4**  string | IPv4 network address. |
| **subnet6**  string | IPv6 network address. |
| **subnet_mask**  string | IPv4 network mask. |
| **tags**  list / elements=string | Collection of tag identifiers. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  Choices:   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  Default: `30` |

## [Examples](cp_mgmt_network_module.md#id3)

```yaml+jinja
- name: add-network
  cp_mgmt_network:
    name: New Network 1
    state: present
    subnet: 192.0.2.0
    subnet_mask: 255.255.255.0

- name: set-network
  cp_mgmt_network:
    color: green
    mask_length: 16
    name: New Network 1
    new_name: New Network 2
    state: present
    subnet: 192.0.0.0

- name: delete-network
  cp_mgmt_network:
    name: New Network 2
    state: absent
```

## [Return Values](cp_mgmt_network_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_network**  dictionary | The checkpoint object created or updated.  Returned: always, except when deleting the object. |

### Authors

- Or Soffer (@chkp-orso)

### Collection links

[Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
[Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
