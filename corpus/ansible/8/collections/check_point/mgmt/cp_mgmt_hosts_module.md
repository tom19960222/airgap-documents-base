---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_hosts module – Manages HOSTS resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_hosts_module.html
fetched_at: 2026-07-28T01:16:26+00:00
---
# check_point.mgmt.cp_mgmt_hosts module – Manages HOSTS resource module

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_hosts`.

New in check_point.mgmt 5.0.0

- [Synopsis](cp_mgmt_hosts_module.md#synopsis)
- [Parameters](cp_mgmt_hosts_module.md#parameters)
- [Examples](cp_mgmt_hosts_module.md#examples)
- [Return Values](cp_mgmt_hosts_module.md#return-values)

## [Synopsis](cp_mgmt_hosts_module.md#id1)

- This resource module allows for addition, deletion, or modification of CP MGMT Hosts.
- This resource module also takes care of gathering Hosts config facts

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](cp_mgmt_hosts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dictionary of HOSTS options |
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
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes.  If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **mask_length**  integer | IPv4 or IPv6 network mask length. If both masks are required use mask-length4 and mask-length6 fields explicitly.  Instead of IPv4 mask length it is possible to specify IPv4 mask itself in subnet-mask field. |
| **mask_length4**  integer | IPv4 network mask length. |
| **mask_length6**  integer | IPv6 network mask length. |
| **name**  string | Interface name. |
| **subnet**  string | IPv4 or IPv6 network address.  If both addresses are required use subnet4 and subnet6 fields explicitly. |
| **subnet4**  string | IPv4 network address. |
| **subnet6**  string | IPv6 network address. |
| **subnet_mask**  string | IPv4 network mask. |
| **ip_address**  string | IPv4 or IPv6 address. If both addresses are required use ipv4-address and ipv6-address fields explicitly. |
| **ipv4_address**  string | IPv4 address. |
| **ipv6_address**  string | IPv4 address. |
| **limit**  integer | The maximal number of returned results.  NOTE, this parameter is a valid parameter only for the GATHERED state, for config states like, MERGED, REPLACED, and DELETED state it won’t be applicable. |
| **name**  string | Object name. Must be unique in the domain. |
| **nat_settings**  dictionary | NAT settings. |
| **auto_rule**  boolean | Whether to add automatic address translation rules.  **Choices:**   - `false` - `true` |
| **hide_behind**  string | Hide behind method. This parameter is not required in case “method” parameter is “static”.  **Choices:**   - `"gateway"` - `"ip-address"` |
| **install_on**  string | Which gateway should apply the NAT translation. |
| **ip_address**  string | IPv4 or IPv6 address. If both addresses are required use ipv4-address and ipv6-address fields explicitly.  This parameter is not required in case “method” parameter is “hide” and “hide-behind” parameter is “gateway”. |
| **ipv4_address**  string | IPv4 address. |
| **ipv6_address**  string | IPv6 address. |
| **method**  string | NAT translation method.  **Choices:**   - `"hide"` - `"static"` |
| **offset**  integer | Number of the results to initially skip.  NOTE, this parameter is a valid parameter only for the GATHERED state, for config states like, MERGED, REPLACED, and DELETED state it won’t be applicable. |
| **order**  list / elements=dictionary | Sorts results by the given field. By default the results are sorted in the ascending order by name. This parameter is relevant only for getting few objects.  NOTE, this parameter is a valid parameter only for the GATHERED state, for config states like, MERGED, REPLACED, and DELETED state it won’t be applicable. |
| **ASC**  string | Sorts results by the given field in ascending order. |
| **DESC**  string | Sorts results by the given field in descending order. |
| **round_trip**  boolean | If set to True, the round trip will filter out the module parameters from the response param, which will enable the user to fire the config request using the structured gathered data.  NOTE, this parameter makes relevance only with the GATHERED state, as for config states like, MERGED, REPLACED, and DELETED state it won’t make any config updates, as it’s not a module config parameter.  **Choices:**   - `false` - `true` |
| **tags**  list / elements=string | Collection of tag identifiers. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **state**  string | The state the configuration should be left in  The state *gathered* will get the module API configuration from the device and transform it into structured data in the format as per the module argspec and the value is returned in the *gathered* key within the result.  **Choices:**   - `"merged"` - `"replaced"` - `"gathered"` - `"deleted"` |

## [Examples](cp_mgmt_hosts_module.md#id3)

```yaml+jinja
# Using MERGED state
# -------------------

- name: Merge MGMT Hosts config
  cp_mgmt_hosts:
    state: merged
    config:
      color: cyan
      ip_address: 192.0.2.1
      name: New Host 1
      auto_publish_session: true
      tags:
        - New Host
      round_trip: true

# RUN output:
# -----------

# mgmt_hosts:
#   after:
#     color: cyan
#     comments: ''
#     groups: []
#     icon: Objects/host
#     interfaces: []
#     ipv4-address: 192.0.2.1
#     name: New Host 1
#     nat_settings: {}
#     tags:
#     - New Host
#   before: {}

# Using REPLACED state
# --------------------

- name: Replace MGMT Host config
  cp_mgmt_hosts:
    state: replaced
    config:
      name: New Host 1
      tags:
        - New Replaced Host
      color: aquamarine
      ip_address: 198.51.110.0
      comments: REPLACED description
      ignore_warnings: true
      ignore_errors: false
      auto_publish_session: true
      round_trip: true

# RUN output:
# -----------

# mgmt_hosts:
#   after:
#     color: aquamarine
#     comments: REPLACED description
#     groups: []
#     icon: Objects/host
#     interfaces: []
#     ipv4-address: 198.51.110.0
#     name: New Host 1
#     nat_settings: {}
#     tags:
#     - New Replaced Host
#   before:
#     color: cyan
#     comments: ''
#     groups: []
#     icon: Objects/host
#     interfaces: []
#     ipv4-address: 192.0.2.1
#     name: New Host 1
#     nat_settings: {}
#     tags:
#     - New Host

# Using GATHERED state
# --------------------

# 1. With Round Trip set to True

- name: Gather MGMT Host config by Name
  cp_mgmt_hosts:
    state: gathered
    config:
      name: New Host 1

# RUN output:
# -----------

# gathered:
#   color: cyan
#   comments: REPLACED description
#   domain: SMC User
#   groups: []
#   icon: Objects/host
#   interfaces: []
#   ipv4-address: 192.0.2.1
#   name: New Host 1
#   nat_settings: {}
#   read-only: false
#   tags:
#   - New Host
#   uid: 63b868bb-d300-47f4-b97a-c465a56fe9c7

# 2. With Round Trip set to False which is the default behaviour

- name: Gather MGMT Host config by Name
  cp_mgmt_hosts:
    state: gathered
    config:
      name: New Host 1

# RUN output:
# -----------

# gathered:
#   color: cyan
#   comments: ''
#   domain:
#     domain-type: domain
#     name: SMC User
#     uid: 41e821a0-3720-11e3-aa6e-0800200c9fde
#   groups: []
#   icon: Objects/host
#   interfaces: []
#   ipv4-address: 192.0.2.1
#   meta-info:
#     creation-time:
#       iso-8601: 2022-11-21T08:31+0000
#       posix: 1669019480328
#     creator: admin
#     last-modifier: admin
#     last-modify-time:
#       iso-8601: 2022-11-21T08:31+0000
#       posix: 1669019480328
#     lock: unlocked
#     validation-state: ok
#   name: New Host 1
#   nat_settings: {}
#   read-only: false
#   tags:
#   - domain:
#       domain-type: domain
#       name: SMC User
#       uid: 41e821a0-3720-11e3-aa6e-0800200c9fde
#     name: New Host
#     type: tag
#     uid: 94d53896-3cee-4e1f-a83b-3abac80bf512
#   type: host
#   uid: 8f23a44b-d9d2-4242-8a9e-2a4cbb6723ff

# 3. Gather ALL threat-layer config with DESC order filter

- name: Gather All hosts on the MGMT instance
  cp_mgmt_hosts:
    config:
      details_level: full
    state: gathered

# RUN output:
# -----------

# gathered:
#   - domain:
#       domain-type: domain
#       name: SMC User
#       uid: 41e821a0-3720-11e3-aa6e-0800200c9fde
#     ipv4-address: 192.0.2.1
#     name: New Host 1
#     type: host
#     uid: 8f23a44b-d9d2-4242-8a9e-2a4cbb6723ff

# Using DELETED state
# -------------------

- name: Delete MGMT Host config by Name
  cp_mgmt_hosts:
    state: deleted
    config:
      name: New Host 1
      round_trip: true

# RUN output:
# -----------

# mgmt_hosts:
#   after: {}
#   before:
#     color: cyan
#     comments: REPLACED description
#     groups: []
#     icon: Objects/host
#     interfaces: []
#     ipv4-address: 192.0.2.1
#     name: New Host 1
#     nat_settings: {}
#     tags:
#     - New Host
```

## [Return Values](cp_mgmt_hosts_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  **Returned:** when changed  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  **Returned:** when state is *merged*, *replaced*, *deleted*  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **gathered**  dictionary | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when state is *gathered*  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |

### Authors

- Ansible Team

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
