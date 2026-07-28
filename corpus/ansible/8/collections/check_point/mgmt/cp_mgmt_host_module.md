---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_host module – Manages host objects on Check Point over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_host_module.html
fetched_at: 2026-07-28T01:16:25+00:00
---
# check_point.mgmt.cp_mgmt_host module – Manages host objects on Check Point over Web Services API

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_host`.

New in check_point.mgmt 1.0.0

- [DEPRECATED](cp_mgmt_host_module.md#deprecated)
- [Synopsis](cp_mgmt_host_module.md#synopsis)
- [Parameters](cp_mgmt_host_module.md#parameters)
- [Examples](cp_mgmt_host_module.md#examples)
- [Return Values](cp_mgmt_host_module.md#return-values)
- [Status](cp_mgmt_host_module.md#status)

## [DEPRECATED](cp_mgmt_host_module.md#id1)

Removed in:
:   major release after 2024-11-01

Why:
:   Newer and updated modules released with more functionality.

Alternative:
:   cp_mgmt_hosts

## [Synopsis](cp_mgmt_host_module.md#id2)

- Manages host objects on Check Point devices including creating, updating and removing objects.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_host_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  **Choices:**   - `false` - `true` |
| **color**  string | Color of the object. Should be one of existing colors.  **Choices:**   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **groups**  list / elements=string | Collection of group identifiers. |
| **host_servers**  dictionary | Servers Configuration. |
| **dns_server**  boolean | Gets True if this server is a DNS Server.  **Choices:**   - `false` - `true` |
| **mail_server**  boolean | Gets True if this server is a Mail Server.  **Choices:**   - `false` - `true` |
| **web_server**  boolean | Gets True if this server is a Web Server.  **Choices:**   - `false` - `true` |
| **web_server_config**  dictionary | Web Server configuration. |
| **additional_ports**  list / elements=string | Server additional ports. |
| **application_engines**  list / elements=string | Application engines of this web server. |
| **listen_standard_port**  boolean | Whether server listens to standard port.  **Choices:**   - `false` - `true` |
| **operating_system**  string | Operating System.  **Choices:**   - `"sparc linux"` - `"windows"` - `"other"` - `"x86 linux"` - `"sparc solaris"` |
| **protected_by**  string | Network object which protects this server identified by the name or UID. |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **interfaces**  list / elements=dictionary | Host interfaces. |
| **color**  string | Color of the object. Should be one of existing colors.  **Choices:**   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **mask_length**  integer | IPv4 or IPv6 network mask length. If both masks are required use mask-length4 and mask-length6 fields explicitly. Instead of IPv4 mask length it is possible to specify IPv4 mask itself in subnet-mask field. |
| **mask_length4**  integer | IPv4 network mask length. |
| **mask_length6**  integer | IPv6 network mask length. |
| **name**  string | Interface name. |
| **subnet**  string | IPv4 or IPv6 network address. If both addresses are required use subnet4 and subnet6 fields explicitly. |
| **subnet4**  string | IPv4 network address. |
| **subnet6**  string | IPv6 network address. |
| **subnet_mask**  string | IPv4 network mask. |
| **ip_address**  string | IPv4 or IPv6 address. If both addresses are required use ipv4-address and ipv6-address fields explicitly. |
| **ipv4_address**  string | IPv4 address. |
| **ipv6_address**  string | IPv6 address. |
| **name**  string / required | Object name. |
| **nat_settings**  dictionary | NAT settings. |
| **auto_rule**  boolean | Whether to add automatic address translation rules.  **Choices:**   - `false` - `true` |
| **hide_behind**  string | Hide behind method. This parameter is not required in case “method” parameter is “static”.  **Choices:**   - `"gateway"` - `"ip-address"` |
| **install_on**  string | Which gateway should apply the NAT translation. |
| **ip_address**  string | IPv4 or IPv6 address. If both addresses are required use ipv4-address and ipv6-address fields explicitly. This parameter is not required in case “method” parameter is “hide” and “hide-behind” parameter is “gateway”. |
| **ipv4_address**  string | IPv4 address. |
| **ipv6_address**  string | IPv6 address. |
| **method**  string | NAT translation method.  **Choices:**   - `"hide"` - `"static"` |
| **state**  string | State of the access rule (present or absent). Defaults to present.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=string | Collection of tag identifiers. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_host_module.md#id4)

```yaml+jinja
- name: add-host
  cp_mgmt_host:
    ip_address: 192.0.2.1
    name: New Host 1
    state: present

- name: set-host
  cp_mgmt_host:
    color: green
    ipv4_address: 192.0.2.2
    name: New Host 1
    state: present

- name: delete-host
  cp_mgmt_host:
    name: New Host 1
    state: absent
```

## [Return Values](cp_mgmt_host_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_host**  dictionary | The checkpoint object created or updated.  **Returned:** always, except when deleting the object. |

## [Status](cp_mgmt_host_module.md#id6)

- This module will be removed in a major release after 2024-11-01.
  *[deprecated]*
- For more information see [DEPRECATED](cp_mgmt_host_module.md#deprecated).

### Authors

- Or Soffer (@chkp-orso)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
