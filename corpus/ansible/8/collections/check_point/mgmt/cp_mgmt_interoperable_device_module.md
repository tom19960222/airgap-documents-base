---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_interoperable_device module – Manages interoperable-device objects on Checkpoint over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_interoperable_device_module.html
fetched_at: 2026-07-28T01:16:38+00:00
---
# check_point.mgmt.cp_mgmt_interoperable_device module – Manages interoperable-device objects on Checkpoint over Web Services API

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_interoperable_device`.

New in check_point.mgmt 3.0.0

- [Synopsis](cp_mgmt_interoperable_device_module.md#synopsis)
- [Parameters](cp_mgmt_interoperable_device_module.md#parameters)
- [Examples](cp_mgmt_interoperable_device_module.md#examples)
- [Return Values](cp_mgmt_interoperable_device_module.md#return-values)

## [Synopsis](cp_mgmt_interoperable_device_module.md#id1)

- Manages interoperable-device objects on Checkpoint devices including creating, updating and removing objects.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_interoperable_device_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  **Choices:**   - `false` - `true` |
| **color**  string | Color of the object. Should be one of existing colors.  **Choices:**   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **domains_to_process**  list / elements=string | Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from the System Domain only and with ignore-warnings true. Valid values are, CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER. |
| **groups**  list / elements=string | Collection of group identifiers. |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **interfaces**  list / elements=dictionary | Network interfaces. |
| **color**  string | Color of the object. Should be one of existing colors.  **Choices:**   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **domains_to_process**  list / elements=string | Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from the System Domain only and with ignore-warnings true. Valid values are, CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER. |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **ip_address**  string | IPv4 or IPv6 address. If both addresses are required use ipv4-address and ipv6-address fields explicitly. |
| **ipv4_address**  string | IPv4 address. |
| **ipv4_mask_length**  string | IPv4 network mask length. |
| **ipv4_network_mask**  string | IPv4 network address. |
| **ipv6_address**  string | IPv6 address. |
| **ipv6_mask_length**  string | IPv6 network mask length. |
| **ipv6_network_mask**  string | IPv6 network address. |
| **mask_length**  string | IPv4 or IPv6 network mask length. |
| **name**  string | Object name. Must be unique in the domain. |
| **network_mask**  string | IPv4 or IPv6 network mask. If both masks are required use ipv4-network-mask and ipv6-network-mask fields explicitly. Instead of providing mask itself it is possible to specify IPv4 or IPv6 mask length in mask-length field. If both masks length are required use ipv4-mask-length and ipv6-mask-length fields explicitly. |
| **tags**  list / elements=string | Collection of tag identifiers. |
| **topology**  string | Topology configuration.  **Choices:**   - `"external"` - `"internal"` |
| **topology_settings**  dictionary | Internal topology settings. |
| **interface_leads_to_dmz**  boolean | Whether this interface leads to demilitarized zone (perimeter network).  **Choices:**   - `false` - `true` |
| **ip_address_behind_this_interface**  string | Network settings behind this interface.  **Choices:**   - `"not defined"` - `"network defined by the interface ip and net mask"` - `"network defined by routing"` - `"specific"` |
| **specific_network**  string | Network behind this interface. |
| **ip_address**  string | IPv4 or IPv6 address. |
| **ipv4_address**  string | IPv4 address of the Interoperable Device. |
| **ipv6_address**  string | IPv6 address of the Interoperable Device. |
| **name**  string / required | Object name. |
| **state**  string | State of the access rule (present or absent). Defaults to present.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=string | Collection of tag identifiers. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **vpn_settings**  dictionary | VPN domain properties for the Interoperable Device. |
| **vpn_domain**  string | Network group representing the customized encryption domain. Must be set when vpn-domain-type is set to ‘manual’ option. |
| **vpn_domain_exclude_external_ip_addresses**  boolean | Exclude the external IP addresses from the VPN domain of this Interoperable device.  **Choices:**   - `false` - `true` |
| **vpn_domain_type**  string | Indicates the encryption domain.  **Choices:**   - `"manual"` - `"addresses_behind_gw"` |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_interoperable_device_module.md#id3)

```yaml+jinja
- name: add-interoperable-device
  cp_mgmt_interoperable_device:
    ip_address: 192.168.1.6
    name: NewInteroperableDevice
    state: present

- name: set-interoperable-device
  cp_mgmt_interoperable_device:
    ip_address: 192.168.1.6
    name: NewInteroperableDevice
    state: present

- name: delete-interoperable-device
  cp_mgmt_interoperable_device:
    name: NewInteroperableDevice
    state: absent
```

## [Return Values](cp_mgmt_interoperable_device_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_interoperable_device**  dictionary | The checkpoint object created or updated.  **Returned:** always, except when deleting the object. |

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
