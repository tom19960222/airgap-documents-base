---
collection: ansible
version: "6"
title: "cisco.iosxr.iosxr_l2_interfaces module – Resource Module to configure L2 interfaces."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/iosxr/iosxr_l2_interfaces_module.html
fetched_at: 2026-07-27T16:55:44+00:00
---
# cisco.iosxr.iosxr_l2_interfaces module – Resource Module to configure L2 interfaces.

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
> To use it in a playbook, specify: `cisco.iosxr.iosxr_l2_interfaces`.

New in cisco.iosxr 1.0.0

- [Synopsis](iosxr_l2_interfaces_module.md#synopsis)
- [Parameters](iosxr_l2_interfaces_module.md#parameters)
- [Notes](iosxr_l2_interfaces_module.md#notes)
- [Examples](iosxr_l2_interfaces_module.md#examples)
- [Return Values](iosxr_l2_interfaces_module.md#return-values)

## [Synopsis](iosxr_l2_interfaces_module.md#id1)

- This module manages the Layer-2 interface attributes on Cisco IOS-XR devices.

## [Parameters](iosxr_l2_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of Layer-2 interface options |
| **encapsulation**  dictionary | Specify which packets will be matched by this sub-interface. |
| **dot1q**  integer | IEEE 802.1Q VLAN-tagged packets. |
| **second_dot1q**  integer | IEEE 802.1Q VLAN-tagged packets. |
| **l2protocol**  list / elements=dictionary | Configures Layer 2 protocol tunneling and protocol data unit (PDU) filtering on an interface. |
| **cdp**  string | Cisco Discovery Protocol (CDP) tunneling and data unit parameters.  Choices:   - `"drop"` - `"forward"` - `"tunnel"` |
| **cpsv**  string | CDP, PVST+, STP, and VTP protocols.  Choices:   - `"drop"` - `"reverse-tunnel"` - `"tunnel"` |
| **pvst**  string | Configures the per-VLAN Spanning Tree Protocol (PVST) tunneling and data unit parameters.  Choices:   - `"drop"` - `"forward"` - `"tunnel"` |
| **stp**  string | Spanning Tree Protocol (STP) tunneling and data unit parameters.  Choices:   - `"drop"` - `"forward"` - `"tunnel"` |
| **vtp**  string | VLAN Trunk Protocol (VTP) tunneling and data unit parameters.  Choices:   - `"drop"` - `"forward"` - `"tunnel"` |
| **l2transport**  boolean | Switchport mode access command to configure the interface as a layer 2 access  Choices:   - `false` - `true` |
| **name**  string / required | Full name of the interface/sub-interface excluding any logical unit number, e.g. GigabitEthernet0/0/0/1 or GigabitEthernet0/0/0/1.100. |
| **native_vlan**  integer | Configure a native VLAN ID for the trunk |
| **propagate**  boolean | Propagate Layer 2 transport events. Note that it will work only when the *l2tranport* option is set to TRUE  Choices:   - `false` - `true` |
| **q_vlan**  list / elements=integer | 802.1Q VLAN configuration. Note that it can accept either 2 VLAN IDs when configuring Q-in-Q VLAN, or it will accept 1 VLAN ID and ‘any’ as input list when configuring Q-in-any vlan as input. Note, that this option is valid only with respect to Sub-Interface and is not valid when configuring for Interface. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS-XR device by executing the command **show running-config interface**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"rendered"` - `"gathered"` - `"parsed"` |

## [Notes](iosxr_l2_interfaces_module.md#id3)

> **Note:**
>
> - This module works with connection `network_cli`. See [the IOS-XR Platform Options](../network/user_guide/platform_iosxr.md).

## [Examples](iosxr_l2_interfaces_module.md#id4)

```yaml+jinja
# Using merged
#
# Before state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/3
#  description Ansible Network
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  duplex half
#  shutdown
# !
# interface GigabitEthernet0/0/0/4
#  description Test description
# !

- name: Merge provided configuration with device configuration
  cisco.iosxr.iosxr_l2_interfaces:
    config:
    - name: GigabitEthernet0/0/0/3
      native_vlan: 20
    - name: GigabitEthernet0/0/0/4
      native_vlan: 40
      l2transport: true
      l2protocol:
      - stp: tunnel
    - name: GigabitEthernet0/0/0/3.900
      l2transport: true
      q_vlan:
      - 20
      - 40
    state: merged

# After state:
# ------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/3
#  description Ansible Network
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  duplex half
#  shutdown
#  dot1q native vlan 20
# !
# interface GigabitEthernet0/0/0/4
# description Test description
#  dot1q native vlan 10
#  l2transport
#   l2protocol stp tunnel
#  !
# !
# interface GigabitEthernet0/0/0/3.900 l2transport
#  dot1q vlan 20 40
# !

# Using replaced
#
# Before state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/3
#  description Ansible Network
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  duplex half
#  shutdown
#  dot1q native vlan 20
# !
# interface GigabitEthernet0/0/0/4
# description Test description
#  dot1q native vlan 10
#  l2transport
#   l2protocol stp tunnel
#  !
# !
# interface GigabitEthernet0/0/0/3.900 l2transport
#  dot1q vlan 20 40
# !

- name: Replaces device configuration of listed interfaces with provided configuration
  cisco.iosxr.iosxr_l2_interfaces:
    config:
    - name: GigabitEthernet0/0/0/4
      native_vlan: 40
      l2transport: true
      l2protocol:
      - stp: forward
    - name: GigabitEthernet0/0/0/3.900
      q_vlan:
      - 20
      - any
    state: replaced

# After state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/3
#  description Ansible Network
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  duplex half
#  shutdown
#  dot1q native vlan 20
# !
# interface GigabitEthernet0/0/0/4
# description Test description
#  dot1q native vlan 40
#  l2transport
#   l2protocol stp forward
#  !
# !
# interface GigabitEthernet0/0/0/3.900 l2transport
#  dot1q vlan 20 any
# !

# Using overridden
#
# Before state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/3
#  description Ansible Network
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  duplex half
#  shutdown
#  dot1q native vlan 20
# !
# interface GigabitEthernet0/0/0/4
# description Test description
#  dot1q native vlan 10
#  l2transport
#   l2protocol stp tunnel
#  !
# !
# interface GigabitEthernet0/0/0/3.900 l2transport
#  dot1q vlan 20 40
# !

- name: Override device configuration of all interfaces with provided configuration
  cisco.iosxr.iosxr_l2_interfaces:
    config:
    - name: GigabitEthernet0/0/0/4
      native_vlan: 40
      l2transport: true
      l2protocol:
      - stp: forward
    - name: GigabitEthernet0/0/0/3.900
      q_vlan:
      - 20
      - any
    state: overridden

# After state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/3
#  description Ansible Network
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  duplex half
#  shutdown
# !
# interface GigabitEthernet0/0/0/4
# description Test description
#  dot1q native vlan 40
#  l2transport
#   l2protocol stp forward
#  !
# !
# interface GigabitEthernet0/0/0/3.900
#  dot1q vlan 20 any
# !

# Using deleted
#
# Before state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/3
#  description Ansible Network
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  duplex half
#  shutdown
#  dot1q native vlan 20
# !
# interface GigabitEthernet0/0/0/4
#  description Test description
#  dot1q native vlan 10
#  l2transport
#   l2protocol stp tunnel
#  !
# !
#

- name: "Delete L2 attributes of given interfaces (Note: This won't delete the interface itself)"
  cisco.iosxr.iosxr_l2_interfaces:
    config:
    - name: GigabitEthernet0/0/0/4
    state: deleted

# After state:
# ------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/3
#  description Ansible Network
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  duplex half
#  shutdown
#  dot1q native vlan 20
# !
# interface GigabitEthernet0/0/0/4
#  description Test description
# !

# Using Deleted without any config passed
# "(NOTE: This will delete all of configured resource module attributes from each configured interface)"
#
# Before state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/3
#  description Ansible Network
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  duplex half
#  shutdown
#  dot1q native vlan 20
# !
# interface GigabitEthernet0/0/0/4
#  description Test description
#  dot1q native vlan 10
#  l2transport
#   l2protocol stp tunnel
#  !
# !

- name: "Delete L2 attributes of all interfaces (Note: This won't delete the interface itself)"
  cisco.iosxr.iosxr_l2_interfaces:
    state: deleted

# After state:
# ------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/3
#  description Ansible Network
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  duplex half
#  shutdown
# !
# interface GigabitEthernet0/0/0/4
#  description Test description
# !

# Using parsed
# parsed.cfg
# ------------
#
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 10.8.38.70 255.255.255.0
# !
# interface GigabitEthernet0/0/0/0
#  description Configured and Merged by Ansible-Network
#  mtu 110
#  ipv4 address 172.31.1.1 255.255.255.0
#  duplex half
# !
# interface GigabitEthernet0/0/0/1
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
# interface GigabitEthernet0/0/0/3.900
#  encapsulation dot1q 20 second-dot1q 40
# !
# interface GigabitEthernet0/0/0/4
#  shutdown
#  dot1q native vlan 40
# !
- name: Convert L2 interfaces config to argspec without connecting to the appliance
  cisco.iosxr.iosxr_l2_interfaces:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed
# Task Output (redacted)
# -----------------------
# "parsed": [
#         {
#             "name": "GigabitEthernet0/0/0/0"
#         },
#         {
#             "l2protocol": [
#                 {
#                     "cdp": "forward"
#                 },
#                 {
#                     "pvst": "tunnel"
#                 }
#             ],
#             "l2transport": true,
#             "name": "GigabitEthernet0/0/0/1",
#             "native_vlan": 10,
#             "propagate": true
#         },
#         {
#             "name": "GigabitEthernet0/0/0/3"
#         },
#         {
#             "name": "GigabitEthernet0/0/0/3.900",
#             "q_vlan": [
#                 20,
#                 40
#             ]
#         },
#         {
#             "name": "GigabitEthernet0/0/0/4",
#             "native_vlan": 40
#         }
#     ]

# Using rendered
- name: Render platform specific commands from task input using rendered state
  cisco.iosxr.iosxr_l2_interfaces:
    config:

    - name: GigabitEthernet0/0/0/1
      native_vlan: 10
      l2transport: true
      l2protocol:

      - pvst: tunnel

      - cdp: forward
      propagate: true

    - name: GigabitEthernet0/0/0/3.900
      q_vlan:
      - 20
      - 40

    - name: GigabitEthernet0/0/0/4
      native_vlan: 40
    state: rendered
# Task Output (redacted)
# -----------------------
# "rendered": [
#         "interface GigabitEthernet0/0/0/1",
#         "dot1q native vlan 10",
#         "l2transport l2protocol pvst tunnel",
#         "l2transport l2protocol cdp forward",
#         "l2transport propagate remote-status",
#         "interface GigabitEthernet0/0/0/3.900",
#         "dot1q vlan 20 40",
#         "interface GigabitEthernet0/0/0/4",
#         "dot1q native vlan 40"
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
#  mtu 110
#  ipv4 address 172.31.1.1 255.255.255.0
#  duplex half
# !
# interface GigabitEthernet0/0/0/1
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
# interface GigabitEthernet0/0/0/3.900
#  encapsulation dot1q 20 second-dot1q 40
# !
# interface GigabitEthernet0/0/0/4
#  shutdown
#  dot1q native vlan 40
# !
- name: Gather IOSXR l2 interfaces as in given arguments
  cisco.iosxr.iosxr_l2_interfaces:
    config:
    state: gathered
# Task Output (redacted)
# -----------------------
#
# "gathered": [
#         {
#             "name": "GigabitEthernet0/0/0/0"
#         },
#         {
#             "l2protocol": [
#                 {
#                     "cdp": "forward"
#                 },
#                 {
#                     "pvst": "tunnel"
#                 }
#             ],
#             "l2transport": true,
#             "name": "GigabitEthernet0/0/0/1",
#             "native_vlan": 10,
#             "propagate": true
#         },
#         {
#             "name": "GigabitEthernet0/0/0/3"
#         },
#         {
#             "name": "GigabitEthernet0/0/0/3.900",
#             "q_vlan": [
#                 20,
#                 40
#             ]
#         },
#         {
#             "name": "GigabitEthernet0/0/0/4",
#             "native_vlan": 40
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
#  mtu 110
#  ipv4 address 172.31.1.1 255.255.255.0
#  duplex half
# !
# interface GigabitEthernet0/0/0/1
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
# interface GigabitEthernet0/0/0/3.900
#  encapsulation dot1q 20 second-dot1q 40
# !
# interface GigabitEthernet0/0/0/4
#  shutdown
#  dot1q native vlan 40
# !
```

## [Return Values](iosxr_l2_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  Returned: when changed  Sample: `["The configuration returned will always be in the same format of the parameters above."]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format of the parameters above."]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device  Returned: always  Sample: `["interface GigabitEthernet0/0/0/2", "l2transport l2protocol pvst tunnel"]` |

### Authors

- Sumit Jaiswal (@justjais)
- Rohit Thakur (@rohitthakur2590)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
