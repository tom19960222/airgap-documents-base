---
collection: ansible
version: "6"
title: "cisco.iosxr.iosxr_interfaces module – Resource module to configure interfaces."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/iosxr/iosxr_interfaces_module.html
fetched_at: 2026-07-27T16:55:43+00:00
---
# cisco.iosxr.iosxr_interfaces module – Resource module to configure interfaces.

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
> To use it in a playbook, specify: `cisco.iosxr.iosxr_interfaces`.

New in cisco.iosxr 1.0.0

- [Synopsis](iosxr_interfaces_module.md#synopsis)
- [Parameters](iosxr_interfaces_module.md#parameters)
- [Notes](iosxr_interfaces_module.md#notes)
- [Examples](iosxr_interfaces_module.md#examples)
- [Return Values](iosxr_interfaces_module.md#return-values)

## [Synopsis](iosxr_interfaces_module.md#id1)

- This module manages the interface attributes on Cisco IOS-XR network devices.

## [Parameters](iosxr_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of interface options |
| **description**  string | Interface description. |
| **duplex**  string | Configures the interface duplex mode. Default is auto-negotiation when not configured.  Choices:   - `"full"` - `"half"` |
| **enabled**  boolean | Administrative state of the interface.  Set the value to `True` to administratively enable the interface or `False` to disable it.  Choices:   - `false` - `true` ← (default) |
| **mtu**  integer | Sets the MTU value for the interface. Applicable for Ethernet interfaces only.  Refer to vendor documentation for valid values. |
| **name**  string / required | Full name of the interface to configure in `type + path` format. e.g. `GigabitEthernet0/0/0/0` |
| **speed**  integer | Configure the speed for an interface. Default is auto-negotiation when not configured. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS-XR device by executing the command **show running-config interface**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion  Choices:   - `"merged"` ← (default) - `"parsed"` - `"deleted"` - `"replaced"` - `"rendered"` - `"gathered"` - `"overridden"` |

## [Notes](iosxr_interfaces_module.md#id3)

> **Note:**
>
> - This module works with connection `network_cli`. See [the IOS-XR Platform Options](../network/user_guide/platform_iosxr.md).

## [Examples](iosxr_interfaces_module.md#id4)

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
#  vrf custB
#  ipv4 address 178.18.169.23 255.255.255.0
#  dot1q native vlan 30
# !
# interface GigabitEthernet0/0/0/3
#  description Replaced by Ansible Team
#  mtu 2000
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  dot1q native vlan 1021
# !
- name: Configure Ethernet interfaces
  cisco.iosxr.iosxr_interfaces:
    config:
    - name: GigabitEthernet0/0/0/2
      description: Configured by Ansible
      enabled: true
    - name: GigabitEthernet0/0/0/3
      description: Configured by Ansible Network
      enabled: false
      duplex: full
    state: merged
# After state:
# ------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  description Configured and Merged by Ansible Network
#  vrf custB
#  ipv4 address 178.18.169.23 255.255.255.0
#  dot1q native vlan 30
# !
# interface GigabitEthernet0/0/0/3
#  description Configured and Merged by Ansible Network
#  mtu 2600
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  duplex full
#  shutdown
#  dot1q native vlan 1021
# !
# Using replaced
# Before state:
# ------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  description Configured by Ansible
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  description Test
#  vrf custB
#  ipv4 address 178.18.169.23 255.255.255.0
#  dot1q native vlan 30
# !
# interface GigabitEthernet0/0/0/3
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  dot1q native vlan 1021
# !
- name: Configure following interfaces and replace their existing config
  cisco.iosxr.iosxr_interfaces:
    config:
    - name: GigabitEthernet0/0/0/2
      description: Configured by Ansible
      enabled: true
      mtu: 2000
    - name: GigabitEthernet0/0/0/3
      description: Configured by Ansible Network
      enabled: false
      duplex: auto
    state: replaced
# After state:
# ------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  description Configured by Ansible
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  description Configured and Replaced by Ansible
#  mtu 2000
#  vrf custB
#  ipv4 address 178.18.169.23 255.255.255.0
#  dot1q native vlan 30
# !
# interface GigabitEthernet0/0/0/3
#  description Configured and Replaced by Ansible Network
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  duplex half
#  shutdown
#  dot1q native vlan 1021
# !
# Using overridden
# Before state:
# ------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  description Configured by Ansible
#  vrf custB
#  ipv4 address 178.18.169.23 255.255.255.0
#  dot1q native vlan 30
# !
# interface GigabitEthernet0/0/0/3
#  description Configured by Ansible
#  mtu 2600
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  duplex full
#  shutdown
#  dot1q native vlan 1021
# !
- name: Override interfaces
  cisco.iosxr.iosxr_interfaces:
    config:
    - name: GigabitEthernet0/0/0/2
      description: Configured by Ansible
      enabled: true
      duplex: auto
    - name: GigabitEthernet0/0/0/3
      description: Configured by Ansible Network
      enabled: false
      speed: 1000
    state: overridden
# After state:
# ------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  description Configured and Overridden by Ansible Network
#  vrf custB
#  ipv4 address 178.18.169.23 255.255.255.0
#  speed 1000
#  dot1q native vlan 30
# !
# interface GigabitEthernet0/0/0/3
#  description Configured and Overridden by Ansible Network
#  mtu 2000
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  duplex full
#  shutdown
#  dot1q native vlan 1021
# !
# Using deleted
# Before state:
# ------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  description Configured and Overridden by Ansible Network
#  vrf custB
#  ipv4 address 178.18.169.23 255.255.255.0
#  speed 1000
#  dot1q native vlan 30
# !
# interface GigabitEthernet0/0/0/3
#  description Configured and Overridden by Ansible Network
#  mtu 2000
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  duplex full
#  shutdown
#  dot1q native vlan 1021
# !
- name: Delete IOSXR interfaces as in given arguments
  cisco.iosxr.iosxr_interfaces:
    config:
    - name: GigabitEthernet0/0/0/2
    - name: GigabitEthernet0/0/0/3
    state: deleted
# After state:
# ------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  vrf custB
#  ipv4 address 178.18.169.23 255.255.255.0
#  dot1q native vlan 30
# !
# interface GigabitEthernet0/0/0/3
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  dot1q native vlan 1021
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
# interface GigabitEthernet0/0/0/3
#  shutdown
# !
# interface GigabitEthernet0/0/0/4
#  shutdown
# !
# - name: Convert ACL interfaces config to argspec without connecting to the appliance
#   cisco.iosxr.iosxr_interfaces:
#     running_config: "{{ lookup('file', './parsed.cfg') }}"
#     state: parsed
# Task Output (redacted)
# -----------------------
# "parsed": [
#        {
#            "name": "MgmtEth0/RP0/CPU0/0"
#        },
#        {
#            "access_groups": [
#                {
#                    "acls": [
#                        {
#                            "direction": "in",
#                            "name": "acl_1"
#                        },
#                        {
#                            "direction": "out",
#                            "name": "acl_2"
#                        }
#                    ],
#                    "afi": "ipv4"
#                },
#                {
#                    "acls": [
#                        {
#                            "direction": "in",
#                            "name": "acl6_1"
#                        },
#                        {
#                            "direction": "out",
#                            "name": "acl6_2"
#                        }
#                    ],
#                    "afi": "ipv6"
#                }
#            ],
#            "name": "GigabitEthernet0/0/0/0"
#        },
#        {
#            "access_groups": [
#                {
#                    "acls": [
#                        {
#                            "direction": "out",
#                            "name": "acl_1"
#                        }
#                    ],
#                    "afi": "ipv4"
#                }
#            ],
#            "name": "GigabitEthernet0/0/0/1"
#        }
#    ]
# }
# Using rendered
- name: Render platform specific commands from task input using rendered state
  cisco.iosxr.iosxr_interfaces:
    config:
    - name: GigabitEthernet0/0/0/0
      description: Configured and Merged by Ansible-Network
      mtu: 110
      enabled: true
      duplex: half
    - name: GigabitEthernet0/0/0/1
      description: Configured and Merged by Ansible-Network
      mtu: 2800
      enabled: false
      speed: 100
      duplex: full
    state: rendered
# Task Output (redacted)
# -----------------------
# "rendered": [
#         "interface GigabitEthernet0/0/0/0",
#         "description Configured and Merged by Ansible-Network",
#         "mtu 110",
#         "duplex half",
#         "no shutdown",
#         "interface GigabitEthernet0/0/0/1",
#         "description Configured and Merged by Ansible-Network",
#         "mtu 2800",
#         "speed 100",
#         "duplex full",
#         "shutdown"
#     ]
# Using gathered
# Before state:
# ------------
#
# RP/0/0/CPU0:an-iosxr-02#show running-config  interface
# interface Loopback888
# description test for ansible
# shutdown
# !
# interface MgmtEth0/0/CPU0/0
# ipv4 address 10.8.38.70 255.255.255.0
# !
# interface GigabitEthernet0/0/0/0
# description Configured and Merged by Ansible-Network
# mtu 110
# ipv4 address 172.31.1.1 255.255.255.0
# duplex half
# !
# interface GigabitEthernet0/0/0/3
# shutdown
# !
# interface GigabitEthernet0/0/0/4
# shutdown
# !
- name: Gather IOSXR interfaces as in given arguments
  cisco.iosxr.iosxr_interfaces:
    config:
    state: gathered
# Task Output (redacted)
# -----------------------
#
# "gathered": [
#         {
#             "description": "test for ansible",
#             "enabled": false,
#             "name": "Loopback888"
#         },
#         {
#             "description": "Configured and Merged by Ansible-Network",
#             "duplex": "half",
#             "enabled": true,
#             "mtu": 110,
#             "name": "GigabitEthernet0/0/0/0"
#         },
#         {
#             "enabled": false,
#             "name": "GigabitEthernet0/0/0/3"
#         },
#         {
#             "enabled": false,
#             "name": "GigabitEthernet0/0/0/4"
#         }
#     ]
# After state:
# ------------
#
# RP/0/0/CPU0:an-iosxr-02#show running-config  interface
# interface Loopback888
# description test for ansible
# shutdown
# !
# interface MgmtEth0/0/CPU0/0
# ipv4 address 10.8.38.70 255.255.255.0
# !
# interface GigabitEthernet0/0/0/0
# description Configured and Merged by Ansible-Network
# mtu 110
# ipv4 address 172.31.1.1 255.255.255.0
# duplex half
# !
# interface GigabitEthernet0/0/0/3
# shutdown
# !
# interface GigabitEthernet0/0/0/4
# shutdown
# !
```

## [Return Values](iosxr_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  Returned: when changed  Sample: `["The configuration returned will always be in the same format of the parameters above."]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format of the parameters above."]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device  Returned: always  Sample: `["interface GigabitEthernet0/0/0/2", "description: Configured by Ansible", "shutdown"]` |

### Authors

- Sumit Jaiswal (@justjais)
- Rohit Thakur (@rohitthakur2590)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
