---
collection: ansible
version: "6"
title: "check_point.mgmt.cp_mgmt_trusted_client module – Manages trusted-client objects on Checkpoint over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/check_point/mgmt/cp_mgmt_trusted_client_module.html
fetched_at: 2026-07-27T16:48:51+00:00
---
# check_point.mgmt.cp_mgmt_trusted_client module – Manages trusted-client objects on Checkpoint over Web Services API

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_trusted_client`.

New in check_point.mgmt 2.9

- [Synopsis](cp_mgmt_trusted_client_module.md#synopsis)
- [Parameters](cp_mgmt_trusted_client_module.md#parameters)
- [Examples](cp_mgmt_trusted_client_module.md#examples)
- [Return Values](cp_mgmt_trusted_client_module.md#return-values)

## [Synopsis](cp_mgmt_trusted_client_module.md#id1)

- Manages trusted-client objects on Checkpoint devices including creating, updating and removing objects.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_trusted_client_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  Choices:   - `false` - `true` |
| **color**  string | Color of the object. Should be one of existing colors.  Choices:   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  Choices:   - `"uid"` - `"standard"` - `"full"` |
| **domains_assignment**  list / elements=string | Domains to be added to this profile. Use domain name only. See example below, “add-trusted-client (with domain)”. |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  Choices:   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  Choices:   - `false` - `true` |
| **ip_address**  string | IPv4 or IPv6 address. If both addresses are required use ipv4-address and ipv6-address fields explicitly. |
| **ip_address_first**  string | First IP address in the range. If both IPv4 and IPv6 address ranges are required, use the ipv4-address-first and the ipv6-address-first fields instead. |
| **ip_address_last**  string | Last IP address in the range. If both IPv4 and IPv6 address ranges are required, use the ipv4-address-first and the ipv6-address-first fields instead. |
| **ipv4_address**  string | IPv4 address. |
| **ipv4_address_first**  string | First IPv4 address in the range. |
| **ipv4_address_last**  string | Last IPv4 address in the range. |
| **ipv6_address**  string | IPv6 address. |
| **ipv6_address_first**  string | First IPv6 address in the range. |
| **ipv6_address_last**  string | Last IPv6 address in the range. |
| **mask_length**  integer | IPv4 or IPv6 mask length. If both masks are required use mask-length4 and mask-length6 fields explicitly. |
| **mask_length4**  integer | IPv4 mask length. |
| **mask_length6**  integer | IPv6 mask length. |
| **multi_domain_server_trusted_client**  boolean | Let this trusted client connect to all Multi-Domain Servers in the deployment.  Choices:   - `false` - `true` |
| **name**  string / required | Object name. |
| **state**  string | State of the access rule (present or absent). Defaults to present.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=string | Collection of tag identifiers. |
| **type**  string | Trusted client type.  Choices:   - `"any"` - `"domain"` - `"ipv4 address"` - `"ipv4 address range"` - `"ipv4 netmask"` - `"ipv6 address"` - `"ipv6 address range"` - `"ipv6 netmask"` - `"name"` - `"wild cards (ip only)"` |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  Choices:   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  Default: `30` |
| **wild_card**  string | IP wild card (e.g. 192.0.2.\*). |

## [Examples](cp_mgmt_trusted_client_module.md#id3)

```yaml+jinja
- name: add-trusted-client
  cp_mgmt_trusted_client:
    name: my client
    state: present
    type: ANY

- name: set-trusted-client
  cp_mgmt_trusted_client:
    ip_address: 192.0.2.1
    mask_length: '24'
    name: my client
    state: present
    type: NETMASK

- name: delete-trusted-client
  cp_mgmt_trusted_client:
    name: my client
    state: absent
```

## [Return Values](cp_mgmt_trusted_client_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_trusted_client**  dictionary | The checkpoint object created or updated.  Returned: always, except when deleting the object. |

### Authors

- Or Soffer (@chkp-orso)

### Collection links

[Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
[Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
