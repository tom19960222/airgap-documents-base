---
collection: ansible
version: "8"
title: "cisco.ios.ios_acl_interfaces module – Resource module to configure ACL interfaces."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ios/ios_acl_interfaces_module.html
fetched_at: 2026-07-28T01:26:02+00:00
---
# cisco.ios.ios_acl_interfaces module – Resource module to configure ACL interfaces.

> **Note:**
>
> This module is part of the [cisco.ios collection](https://galaxy.ansible.com/ui/repo/published/cisco/ios/) (version 4.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ios`.
>
> To use it in a playbook, specify: `cisco.ios.ios_acl_interfaces`.

New in cisco.ios 1.0.0

- [Synopsis](ios_acl_interfaces_module.md#synopsis)
- [Parameters](ios_acl_interfaces_module.md#parameters)
- [Notes](ios_acl_interfaces_module.md#notes)
- [Examples](ios_acl_interfaces_module.md#examples)
- [Return Values](ios_acl_interfaces_module.md#return-values)

## [Synopsis](ios_acl_interfaces_module.md#id1)

- This module configures and manages the access-control (ACL) attributes of interfaces on IOS platforms.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: acl_interfaces

## [Parameters](ios_acl_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of ACL interfaces options |
| **access_groups**  list / elements=dictionary | Specify access-group for IP access list (standard or extended). |
| **acls**  list / elements=dictionary | Specifies the ACLs for the provided AFI. |
| **direction**  string / required | Specifies the direction of packets that the ACL will be applied on.  With one direction already assigned, other acl direction cannot be same.  **Choices:**   - `"in"` - `"out"` |
| **name**  string / required | Specifies the name of the IPv4/IPv4 ACL for the interface. |
| **afi**  string / required | Specifies the AFI for the ACLs to be configured on this interface.  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **name**  string / required | Full name of the interface excluding any logical unit number, i.e. GigabitEthernet0/1. |
| **running_config**  string | The module, by default, will connect to the remote device and retrieve the current running-config to use as a base for comparing against the contents of source. There are times when it is not desirable to have the task get the current running-config for every task in a playbook. The *running_config* argument allows the implementer to pass in the configuration to use as the base config for comparison. This value of this option should be the output received from device by executing command. |
| **state**  string | The state the configuration should be left in  The states *rendered*, *gathered* and *parsed* does not perform any change on the device.  The state *rendered* will transform the configuration in `config` option to platform specific CLI commands which will be returned in the *rendered* key within the result. For state *rendered* active connection to remote host is not required.  The state *gathered* will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the *gathered* key within the result.  The state *parsed* reads the configuration from `running_config` option and transforms it into JSON format as per the resource module parameters and the value is returned in the *parsed* key within the result. The value of `running_config` option should be the same format as the output of command *show running-config | include ^interface|ip access-group|ipv6 traffic-filter* executed on device. For state *parsed* active connection to remote host is not required.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"parsed"` - `"rendered"` |

## [Notes](ios_acl_interfaces_module.md#id3)

> **Note:**
>
> - Tested against Cisco IOSXE Version 17.3 on CML.
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>

## [Examples](ios_acl_interfaces_module.md#id4)

```yaml+jinja
# Using Merged

# Before state:
# -------------
#
# vios#sh running-config | include interface|ip access-group|ipv6 traffic-filter
# interface Loopback888
# interface GigabitEthernet0/0
# interface GigabitEthernet0/1
# interface GigabitEthernet0/2
#  ip access-group 123 out

- name: Merge module attributes of given access-groups
  cisco.ios.ios_acl_interfaces:
    config:
      - name: GigabitEthernet0/1
        access_groups:
          - afi: ipv4
            acls:
              - name: 110
                direction: in
              - name: 123
                direction: out
          - afi: ipv6
            acls:
              - name: test_v6
                direction: out
              - name: temp_v6
                direction: in
      - name: GigabitEthernet0/2
        access_groups:
          - afi: ipv4
            acls:
              - name: 100
                direction: in
    state: merged

# Commands Fired:
# ---------------
#
# interface GigabitEthernet0/1
#  ip access-group 110 in
#  ip access-group 123 out
#  ipv6 traffic-filter test_v6 out
#  ipv6 traffic-filter temp_v6 in
# interface GigabitEthernet0/2
#  ip access-group 100 in

# After state:
# -------------
#
# vios#sh running-config | include interface|ip access-group|ipv6 traffic-filter
# interface Loopback888
# interface GigabitEthernet0/0
# interface GigabitEthernet0/1
#  ip access-group 110 in
#  ip access-group 123 out
#  ipv6 traffic-filter test_v6 out
#  ipv6 traffic-filter temp_v6 in
# interface GigabitEthernet0/2
#  ip access-group 110 in
#  ip access-group 123 out

# Using Replaced

# Before state:
# -------------
#
# vios#sh running-config | include interface|ip access-group|ipv6 traffic-filter
# interface Loopback888
# interface GigabitEthernet0/0
# interface GigabitEthernet0/1
#  ip access-group 110 in
#  ip access-group 123 out
#  ipv6 traffic-filter test_v6 out
#  ipv6 traffic-filter temp_v6 in
# interface GigabitEthernet0/2
#  ip access-group 110 in
#  ip access-group 123 out

- name: Replace module attributes of given access-groups
  cisco.ios.ios_acl_interfaces:
    config:
      - name: GigabitEthernet0/1
        access_groups:
          - afi: ipv4
            acls:
              - name: 100
                direction: out
              - name: 110
                direction: in
    state: replaced

# Commands Fired:
# ---------------
#
# interface GigabitEthernet0/1
# no ip access-group 123 out
# no ipv6 traffic-filter temp_v6 in
# no ipv6 traffic-filter test_v6 out
# ip access-group 100 out

# After state:
# -------------
#
# vios#sh running-config | include interface|ip access-group|ipv6 traffic-filter
# interface Loopback888
# interface GigabitEthernet0/0
# interface GigabitEthernet0/1
#  ip access-group 100 out
#  ip access-group 110 in
# interface GigabitEthernet0/2
#  ip access-group 110 in
#  ip access-group 123 out

# Using Overridden

# Before state:
# -------------
#
# vios#sh running-config | include interface|ip access-group|ipv6 traffic-filter
# interface Loopback888
# interface GigabitEthernet0/0
# interface GigabitEthernet0/1
#  ip access-group 110 in
#  ip access-group 123 out
#  ipv6 traffic-filter test_v6 out
#  ipv6 traffic-filter temp_v6 in
# interface GigabitEthernet0/2
#  ip access-group 110 in
#  ip access-group 123 out

- name: Overridden module attributes of given access-groups
  cisco.ios.ios_acl_interfaces:
    config:
      - name: GigabitEthernet0/1
        access_groups:
          - afi: ipv4
            acls:
              - name: 100
                direction: out
              - name: 110
                direction: in
    state: overridden

# Commands Fired:
# ---------------
#
# interface GigabitEthernet0/1
# no ip access-group 123 out
# no ipv6 traffic-filter test_v6 out
# no ipv6 traffic-filter temp_v6 in
# ip access-group 100 out
# interface GigabitEthernet0/2
# no ip access-group 110 in
# no ip access-group 123 out

# After state:
# -------------
#
# vios#sh running-config | include interface|ip access-group|ipv6 traffic-filter
# interface Loopback888
# interface GigabitEthernet0/0
# interface GigabitEthernet0/1
#  ip access-group 100 out
#  ip access-group 110 in
# interface GigabitEthernet0/2

# Using Deleted

# Before state:
# -------------
#
# vios#sh running-config | include interface|ip access-group|ipv6 traffic-filter
# interface Loopback888
# interface GigabitEthernet0/0
# interface GigabitEthernet0/1
#  ip access-group 110 in
#  ip access-group 123 out
#  ipv6 traffic-filter test_v6 out
#  ipv6 traffic-filter temp_v6 in
# interface GigabitEthernet0/2
#  ip access-group 110 in
#  ip access-group 123 out

- name: Delete module attributes of given Interface
  cisco.ios.ios_acl_interfaces:
    config:
      - name: GigabitEthernet0/1
    state: deleted

# Commands Fired:
# ---------------
#
# interface GigabitEthernet0/1
# no ip access-group 110 in
# no ip access-group 123 out
# no ipv6 traffic-filter test_v6 out
# no ipv6 traffic-filter temp_v6 in

# After state:
# -------------
#
# vios#sh running-config | include interface|ip access-group|ipv6 traffic-filter
# interface Loopback888
# interface GigabitEthernet0/0
# interface GigabitEthernet0/1
# interface GigabitEthernet0/2
#  ip access-group 110 in
#  ip access-group 123 out

# Using DELETED without any config passed
#"(NOTE: This will delete all of configured resource module attributes from each configured interface)"

# Before state:
# -------------
#
# vios#sh running-config | include interface|ip access-group|ipv6 traffic-filter
# interface Loopback888
# interface GigabitEthernet0/0
# interface GigabitEthernet0/1
#  ip access-group 110 in
#  ip access-group 123 out
#  ipv6 traffic-filter test_v6 out
#  ipv6 traffic-filter temp_v6 in
# interface GigabitEthernet0/2
#  ip access-group 110 in
#  ip access-group 123 out

- name: Delete module attributes of given access-groups from ALL Interfaces
  cisco.ios.ios_acl_interfaces:
    config:
    state: deleted

# Commands Fired:
# ---------------
#
# interface GigabitEthernet0/1
# no ip access-group 110 in
# no ip access-group 123 out
# no ipv6 traffic-filter test_v6 out
# no ipv6 traffic-filter temp_v6 in
# interface GigabitEthernet0/2
# no ip access-group 110 out
# no ip access-group 123 out

# After state:
# -------------
#
# vios#sh running-config | include interface|ip access-group|ipv6 traffic-filter
# interface Loopback888
# interface GigabitEthernet0/0
# interface GigabitEthernet0/1
# interface GigabitEthernet0/2

# Using Gathered

# Before state:
# -------------
#
# vios#sh running-config | include interface|ip access-group|ipv6 traffic-filter
# interface Loopback888
# interface GigabitEthernet0/0
# interface GigabitEthernet0/1
#  ip access-group 110 in
#  ip access-group 123 out
#  ipv6 traffic-filter test_v6 out
#  ipv6 traffic-filter temp_v6 in
# interface GigabitEthernet0/2
#  ip access-group 110 in
#  ip access-group 123 out

- name: Gather listed acl interfaces with provided configurations
  cisco.ios.ios_acl_interfaces:
    config:
    state: gathered

# Module Execution Result:
# ------------------------
#
# "gathered": [
#         {
#             "name": "Loopback888"
#         },
#         {
#             "name": "GigabitEthernet0/0"
#         },
#         {
#             "access_groups": [
#                 {
#                     "acls": [
#                         {
#                             "direction": "in",
#                             "name": "110"
#                         },
#                         {
#                             "direction": "out",
#                             "name": "123"
#                         }
#                     ],
#                     "afi": "ipv4"
#                 },
#                 {
#                     "acls": [
#                         {
#                             "direction": "in",
#                             "name": "temp_v6"
#                         },
#                         {
#                             "direction": "out",
#                             "name": "test_v6"
#                         }
#                     ],
#                     "afi": "ipv6"
#                 }
#             ],
#             "name": "GigabitEthernet0/1"
#         },
#         {
#             "access_groups": [
#                 {
#                     "acls": [
#                         {
#                             "direction": "in",
#                             "name": "100"
#                         },
#                         {
#                             "direction": "out",
#                             "name": "123"
#                         }
#                     ],
#                     "afi": "ipv4"
#                 }
#             ],
#             "name": "GigabitEthernet0/2"
#         }
#     ]

# After state:
# ------------
#
# vios#sh running-config | include interface|ip access-group|ipv6 traffic-filter
# interface Loopback888
# interface GigabitEthernet0/0
# interface GigabitEthernet0/1
#  ip access-group 110 in
#  ip access-group 123 out
#  ipv6 traffic-filter test_v6 out
#  ipv6 traffic-filter temp_v6 in
# interface GigabitEthernet0/2
#  ip access-group 110 in
#  ip access-group 123 out

# Using Rendered

- name: Render the commands for provided  configuration
  cisco.ios.ios_acl_interfaces:
    config:
      - name: GigabitEthernet0/1
        access_groups:
          - afi: ipv4
            acls:
              - name: 110
                direction: in
              - name: 123
                direction: out
          - afi: ipv6
            acls:
              - name: test_v6
                direction: out
              - name: temp_v6
                direction: in
    state: rendered

# Module Execution Result:
# ------------------------
#
# "rendered": [
#         "interface GigabitEthernet0/1",
#         "ip access-group 110 in",
#         "ip access-group 123 out",
#         "ipv6 traffic-filter temp_v6 in",
#         "ipv6 traffic-filter test_v6 out"
#     ]

# Using Parsed

# File: parsed.cfg
# ----------------
#
# interface GigabitEthernet0/1
# ip access-group 110 in
# ip access-group 123 out
# ipv6 traffic-filter temp_v6 in
# ipv6 traffic-filter test_v6 out

- name: Parse the commands for provided configuration
  cisco.ios.ios_acl_interfaces:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Module Execution Result:
# ------------------------
#
# "parsed": [
#         {
#             "access_groups": [
#                 {
#                     "acls": [
#                         {
#                             "direction": "in",
#                             "name": "110"
#                         }
#                     ],
#                     "afi": "ipv4"
#                 },
#                 {
#                     "acls": [
#                         {
#                             "direction": "in",
#                             "name": "temp_v6"
#                         }
#                     ],
#                     "afi": "ipv6"
#                 }
#             ],
#             "name": "GigabitEthernet0/1"
#         }
#     ]
```

## [Return Values](ios_acl_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  **Returned:** when changed  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `["interface GigabitEthernet0/1", "no ip access-group 123 out", "no ipv6 traffic-filter test_v6 out"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when *state* is `gathered`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when *state* is `parsed`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when *state* is `rendered`  **Sample:** `["interface GigabitEthernet0/1", "no ip access-group 123 out", "no ipv6 traffic-filter test_v6 out"]` |

### Authors

- Sumit Jaiswal (@justjais)
- Sagar Paul (@KB-perByte)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
