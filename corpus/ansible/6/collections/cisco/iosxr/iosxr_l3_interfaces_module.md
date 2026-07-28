---
collection: ansible
version: "6"
title: "cisco.iosxr.iosxr_l3_interfaces module – Resource module to configure L3 interfaces."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/iosxr/iosxr_l3_interfaces_module.html
fetched_at: 2026-07-27T16:55:45+00:00
---
# cisco.iosxr.iosxr_l3_interfaces module – Resource module to configure L3 interfaces.

> **Note:**
>
> This module is part of the [cisco.iosxr collection](https://galaxy.ansible.com/cisco/iosxr) (version 3.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.iosxr`.
>
> To use it in a playbook, specify: `cisco.iosxr.iosxr_l3_interfaces`.

New in cisco.iosxr 1.0.0

- [Synopsis](iosxr_l3_interfaces_module.md#synopsis)
- [Parameters](iosxr_l3_interfaces_module.md#parameters)
- [Notes](iosxr_l3_interfaces_module.md#notes)
- [Examples](iosxr_l3_interfaces_module.md#examples)
- [Return Values](iosxr_l3_interfaces_module.md#return-values)

## [Synopsis](iosxr_l3_interfaces_module.md#id1)

- This module provides declarative management of Layer-3 interface on Cisco IOS-XR devices.

## [Parameters](iosxr_l3_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of Layer-3 interface options |
| **ipv4**  list / elements=dictionary | IPv4 address to be set for the Layer-3 interface mentioned in *name* option.  The address format is <ipv4 address>/<mask>, the mask is number in range 0-32 eg. 192.168.0.1/24 |
| **address**  string | Configures the IPv4 address for Interface. |
| **secondary**  boolean | Configures the IP address as a secondary address.  Choices:   - `false` - `true` |
| **ipv6**  list / elements=dictionary | IPv6 address to be set for the Layer-3 interface mentioned in *name* option.  The address format is <ipv6 address>/<mask>, the mask is number in range 0-128 eg. fd5d:12c9:2201:1::1/64 |
| **address**  string | Configures the IPv6 address for Interface. |
| **name**  string / required | Full name of the interface excluding any logical unit number, i.e. GigabitEthernet0/1. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS-XR device by executing the command **show running-config interface**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"parsed"` - `"rendered"` - `"gathered"` |

## [Notes](iosxr_l3_interfaces_module.md#id3)

> **Note:**
>
> - This module works with connection `network_cli`. See [the IOS-XR Platform Options](../network/user_guide/platform_iosxr.md).

## [Examples](iosxr_l3_interfaces_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  shutdown
# !
# interface GigabitEthernet0/0/0/3
#  ipv4 address 192.168.0.2 255.255.255.0
#  shutdown
# !
# interface GigabitEthernet0/0/0/3.700
# !
# interface GigabitEthernet0/0/0/4
#  ipv6 address fd5d:12c9:2201:1::1/64
#  shutdown
# !

- name: Merge provided configuration with device configuration
  cisco.iosxr.iosxr_l3_interfaces:
    config:
    - name: GigabitEthernet0/0/0/2
      ipv4:
      - address: 192.168.0.1/24
    - name: GigabitEthernet0/0/0/3
      ipv4:
      - address: 192.168.2.1/24
        secondary: true
    state: merged

# After state:
# ------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  ipv4 address 192.168.0.1 255.255.255.0
#  shutdown
# !
# interface GigabitEthernet0/0/0/3
#  ipv4 address 192.168.1.0 255.255.255.0
#  ipv4 address 192.168.2.1 255.255.255.0 secondary
#  shutdown
# !
# interface GigabitEthernet0/0/0/3.700
# !
# interface GigabitEthernet0/0/0/4
#  ipv6 address fd5d:12c9:2201:1::1/64
#  shutdown
# !

# Using overridden

# Before state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  ipv4 address 192.168.0.1 255.255.255.0
#  shutdown
# !
# interface GigabitEthernet0/0/0/3
#  ipv4 address 192.168.1.0 255.255.255.0
#  shutdown
# !
# interface GigabitEthernet0/0/0/3.700
# !
# interface GigabitEthernet0/0/0/4
#  ipv6 address fd5d:12c9:2201:1::1/64
#  shutdown
# !

- name: Override device configuration of all interfaces with provided configuration
  cisco.iosxr.iosxr_l3_interfaces:
    config:
    - name: GigabitEthernet0/0/0/3
      ipv4:
      - address: 192.168.0.1/24
    - name: GigabitEthernet0/0/0/3.700
      ipv4:
      - address: 192.168.0.2/24
      - address: 192.168.2.1/24
        secondary: true
    state: overridden

# After state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  shutdown
# !
# interface GigabitEthernet0/0/0/3
#  ipv4 address 192.168.0.1 255.255.255.0
#  shutdown
# !
# interface GigabitEthernet0/0/0/3.700
#  ipv4 address 192.168.0.2 255.255.255.0
#  ipv4 address 192.168.2.1 255.255.255.0 secondary
# !
# interface GigabitEthernet0/0/0/4
#  shutdown
# !

# Using replaced

# Before state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  shutdown
# !
# interface GigabitEthernet0/0/0/3
#  ipv4 address 192.168.0.2 255.255.255.0
#  shutdown
# !
# interface GigabitEthernet0/0/0/3.700
#  ipv4 address 192.168.0.1 255.255.255.0
# !
# interface GigabitEthernet0/0/0/4
#  ipv6 address fd5d:12c9:2201:1::1/64
#  shutdown
# !

- name: Replaces device configuration of listed interfaces with provided configuration
  cisco.iosxr.iosxr_l3_interfaces:
    config:
    - name: GigabitEthernet0/0/0/3
      ipv6:
      - address: fd5d:12c9:2201:1::1/64
    - name: GigabitEthernet0/0/0/4
      ipv4:
      - address: 192.168.0.2/24
    state: replaced

# After state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  shutdown
# !
# interface GigabitEthernet0/0/0/3
#  ipv6 address fd5d:12c9:2201:1::1/64
#  shutdown
# !
# interface GigabitEthernet0/0/0/3.700
#  ipv4 address 192.168.0.1 255.255.255.0
# !
# interface GigabitEthernet0/0/0/4
#  ipv4 address 192.168.0.2 255.255.255.0
#  shutdown
# !

# Using deleted

# Before state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  ipv4 address 192.168.2.1 255.255.255.0
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  ipv4 address 192.168.3.1 255.255.255.0
#  shutdown
# !
# interface GigabitEthernet0/0/0/3
#  ipv4 address 192.168.0.2 255.255.255.0
#  shutdown
# !
# interface GigabitEthernet0/0/0/3.700
#  ipv4 address 192.168.0.1 255.255.255.0
# !
# interface GigabitEthernet0/0/0/4
#  ipv6 address fd5d:12c9:2201:1::1/64
#  shutdown
# !

- name: "Delete L3 attributes of given interfaces (Note: This won't delete the interface itself)"
  cisco.iosxr.iosxr_l3_interfaces:
    config:
    - name: GigabitEthernet0/0/0/3
    - name: GigabitEthernet0/0/0/4
    - name: GigabitEthernet0/0/0/3.700
    state: deleted

# After state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  ipv4 address 192.168.2.1 255.255.255.0
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  ipv4 address 192.168.3.1 255.255.255.0
#  shutdown
# !
# interface GigabitEthernet0/0/0/3
#  shutdown
# !
# interface GigabitEthernet0/0/0/3.700
# !
# interface GigabitEthernet0/0/0/4
#  shutdown
# !

# Using Deleted without any config passed
# "(NOTE: This will delete all of configured resource module attributes from each configured interface)"

# Before state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  ipv4 address 192.168.2.1 255.255.255.0
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  ipv4 address 192.168.3.1 255.255.255.0
#  shutdown
# !
# interface GigabitEthernet0/0/0/3
#  ipv4 address 192.168.0.2 255.255.255.0
#  shutdown
# !
# interface GigabitEthernet0/0/0/3.700
#  ipv4 address 192.168.0.1 255.255.255.0
# !
# interface GigabitEthernet0/0/0/4
#  ipv6 address fd5d:12c9:2201:1::1/64
#  shutdown
# !

- name: "Delete L3 attributes of all interfaces (Note: This won't delete the interface itself)"
  cisco.iosxr.iosxr_l3_interfaces:
    state: deleted

# After state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  shutdown
# !
# interface GigabitEthernet0/0/0/3
#  shutdown
# !
# interface GigabitEthernet0/0/0/3.700
# !
# interface GigabitEthernet0/0/0/4
#  shutdown
# !

# Using parsed
# parsed.cfg
# ------------
#
# nterface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 10.8.38.70 255.255.255.0
# !
# interface GigabitEthernet0/0/0/0
#  description Configured and Merged by Ansible-Network
#  mtu 66
#  ipv4 address 192.0.2.1 255.255.255.0
#  ipv4 address 192.0.2.2 255.255.255.0 secondary
#  ipv6 address 2001:db8:0:3::/64
#  duplex half
# !
# interface GigabitEthernet0/0/0/1
#  description Configured and Merged by Ansible-Network
#  mtu 66
#  speed 100
#  duplex full
#  dot1q native vlan 10
#  l2transport
#   l2protocol cdp forward
#   l2protocol pvst tunnel
#   propagate remote-status
#  !
# !
# interface GigabitEthernet0/0/0/3
#  ipv4 address 192.0.22.1 255.255.255.0
#  ipv4 address 192.0.23.1 255.255.255.0
# !
# - name: Convert L3 interfaces config to argspec without connecting to the appliance
#   cisco.iosxr.iosxr_l3_interfaces:
#     running_config: "{{ lookup('file', './parsed.cfg') }}"
#     state: parsed
# Task Output (redacted)
# -----------------------
# "parsed": [
#         {
#             "ipv4": [
#                 {
#                     "address": "192.0.2.1 255.255.255.0"
#                 },
#                 {
#                     "address": "192.0.2.2 255.255.255.0",
#                     "secondary": true
#                 }
#             ],
#             "ipv6": [
#                 {
#                     "address": "2001:db8:0:3::/64"
#                 }
#             ],
#             "name": "GigabitEthernet0/0/0/0"
#         },
#         {
#             "name": "GigabitEthernet0/0/0/1"
#         },
#         {
#             "ipv4": [
#                 {
#                     "address": "192.0.22.1 255.255.255.0"
#                 },
#                 {
#                     "address": "192.0.23.1 255.255.255.0"
#                 }
#             ],
#             "name": "GigabitEthernet0/0/0/3"
#         }
#     ]

# Using rendered
- name: Render platform specific commands from task input using rendered state
  cisco.iosxr.iosxr_l3_interfaces:
    config:

    - name: GigabitEthernet0/0/0/0
      ipv4:

      - address: 198.51.100.1/24

    - name: GigabitEthernet0/0/0/1
      ipv6:

      - address: 2001:db8:0:3::/64
      ipv4:

      - address: 192.0.2.1/24

      - address: 192.0.2.2/24
        secondary: true
    state: rendered
# Task Output (redacted)
# -----------------------
# "rendered": [
#         "interface GigabitEthernet0/0/0/0",
#         "ipv4 address 198.51.100.1 255.255.255.0",
#         "interface GigabitEthernet0/0/0/1",
#         "ipv4 address 192.0.2.2 255.255.255.0 secondary",
#         "ipv4 address 192.0.2.1 255.255.255.0",
#         "ipv6 address 2001:db8:0:3::/64"
#     ]
# Using gathered
# Before state:
# ------------
#
# RP/0/0/CPU0:an-iosxr-02#show running-config  interface
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 10.8.38.70 255.255.255.0
# !
# interface GigabitEthernet0/0/0/0
#  description Configured and Merged by Ansible-Network
#  mtu 66
#  ipv4 address 192.0.2.1 255.255.255.0
#  ipv4 address 192.0.2.2 255.255.255.0 secondary
#  ipv6 address 2001:db8:0:3::/64
#  duplex half
# !
# interface GigabitEthernet0/0/0/1
#  description Configured and Merged by Ansible-Network
#  mtu 66
#  speed 100
#  duplex full
#  dot1q native vlan 10
#  l2transport
#   l2protocol cdp forward
#   l2protocol pvst tunnel
#   propagate remote-status
#  !
# !
# interface GigabitEthernet0/0/0/3
#  shutdown
# !
# interface GigabitEthernet0/0/0/4
#  shutdown
#  dot1q native vlan 40
# !
- name: Gather IOSXR l3 interfaces as in given arguments
  cisco.iosxr.iosxr_l3_interfaces:
    config:
    state: gathered
# Task Output (redacted)
# -----------------------
#
# "gathered": [
#         {
#             "name": "Loopback888"
#         },
#         {
#             "ipv4": [
#                 {
#                     "address": "192.0.2.1 255.255.255.0"
#                 },
#                 {
#                     "address": "192.0.2.2 255.255.255.0",
#                     "secondary": true
#                 }
#             ],
#             "ipv6": [
#                 {
#                     "address": "2001:db8:0:3::/64"
#                 }
#             ],
#             "name": "GigabitEthernet0/0/0/0"
#         },
#         {
#             "name": "GigabitEthernet0/0/0/1"
#         },
#         {
#             "name": "GigabitEthernet0/0/0/3"
#         },
#         {
#             "name": "GigabitEthernet0/0/0/4"
#         }
#     ]
# After state:
# ------------
#
# RP/0/0/CPU0:an-iosxr-02#show running-config  interface
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 10.8.38.70 255.255.255.0
# !
# interface GigabitEthernet0/0/0/0
#  description Configured and Merged by Ansible-Network
#  mtu 66
#  ipv4 address 192.0.2.1 255.255.255.0
#  ipv4 address 192.0.2.2 255.255.255.0 secondary
#  ipv6 address 2001:db8:0:3::/64
#  duplex half
# !
# interface GigabitEthernet0/0/0/1
#  description Configured and Merged by Ansible-Network
#  mtu 66
#  speed 100
#  duplex full
#  dot1q native vlan 10
#  l2transport
#   l2protocol cdp forward
#   l2protocol pvst tunnel
#   propagate remote-status
#  !
# !
# interface GigabitEthernet0/0/0/3
#  shutdown
# !
# interface GigabitEthernet0/0/0/4
#  shutdown
#  dot1q native vlan 40
# !
```

## [Return Values](iosxr_l3_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  Returned: when changed  Sample: `["The configuration returned will always be in the same format of the parameters above."]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format of the parameters above."]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device  Returned: always  Sample: `["interface GigabitEthernet0/0/0/1", "ipv4 address 192.168.0.1 255.255.255.0"]` |

### Authors

- Sumit Jaiswal (@justjais)
- Rohit Thakur (@rohitthakur2590)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
