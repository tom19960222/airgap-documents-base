---
collection: ansible
version: "6"
title: "cisco.iosxr.iosxr_lldp_interfaces module – Resource module to configure LLDP interfaces."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/iosxr/iosxr_lldp_interfaces_module.html
fetched_at: 2026-07-27T16:55:48+00:00
---
# cisco.iosxr.iosxr_lldp_interfaces module – Resource module to configure LLDP interfaces.

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
> To use it in a playbook, specify: `cisco.iosxr.iosxr_lldp_interfaces`.

New in cisco.iosxr 1.0.0

- [Synopsis](iosxr_lldp_interfaces_module.md#synopsis)
- [Parameters](iosxr_lldp_interfaces_module.md#parameters)
- [Notes](iosxr_lldp_interfaces_module.md#notes)
- [Examples](iosxr_lldp_interfaces_module.md#examples)
- [Return Values](iosxr_lldp_interfaces_module.md#return-values)

## [Synopsis](iosxr_lldp_interfaces_module.md#id1)

- This module manages Link Layer Discovery Protocol (LLDP) attributes of interfaces on IOS-XR devices.

## [Parameters](iosxr_lldp_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of LLDP interfaces options. |
| **destination**  dictionary | Specifies LLDP destination configuration on the interface. |
| **mac_address**  string | Specifies the LLDP destination mac address on the interface.  Choices:   - `"ieee-nearest-bridge"` - `"ieee-nearest-non-tmpr-bridge"` |
| **name**  string | Name/Identifier of the interface or Ether-Bundle. |
| **receive**  boolean | Enable/disable LLDP RX on an interface.  Choices:   - `false` - `true` |
| **transmit**  boolean | Enable/disable LLDP TX on an interface.  Choices:   - `false` - `true` |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS-XR device by executing the command **show running-config int**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"parsed"` - `"rendered"` - `"gathered"` |

## [Notes](iosxr_lldp_interfaces_module.md#id3)

> **Note:**
>
> - This module works with connection `network_cli`. See [the IOS-XR Platform Options](../network/user_guide/platform_iosxr.md).

## [Examples](iosxr_lldp_interfaces_module.md#id4)

```yaml+jinja
# Using merged
#
#
# ------------
# Before state
# ------------
#
#
# RP/0/RP0/CPU0:ios#sh run int
# Mon Aug 12 12:40:23.104 UTC
# interface TenGigE0/0/0/0
#  ipv4 address 192.0.2.11 255.255.255.192
# !
# interface preconfigure GigabitEthernet0/0/0/1
# !
# interface preconfigure GigabitEthernet0/0/0/2
# !
#
#

- name: Merge provided configuration with running configuration
  cisco.iosxr.iosxr_lldp_interfaces:
    config:
    - name: GigabitEthernet0/0/0/1
      destination:
        mac_address: ieee-nearest-non-tmpr-bridge
      transmit: false

    - name: GigabitEthernet0/0/0/2
      destination:
        mac_address: ieee-nearest-bridge
      receive: false
    state: merged

#
#
# ------------------------
# Module Execution Result
# ------------------------
#
#
# "before": [
#        {
#            "name": "TenGigE0/0/0/0"
#        },
#        {
#            "name": "GigabitEthernet0/0/0/1"
#        },
#        {
#            "name": "GigabitEthernet0/0/0/2"
#        }
# ]
#
# "commands": [
#        "interface GigabitEthernet0/0/0/2",
#        "lldp destination mac-address ieee-nearest-non-tmpr-bridge",
#        "lldp transmit disable",
#        "interface GigabitEthernet0/0/0/1",
#        "lldp receive disable",
#        "lldp destination mac-address ieee-nearest-bridge"
# ]
#
# "after": [
#        {
#            "name": "TenGigE0/0/0/0"
#        },
#        {
#            "destination": {
#                "mac_address": "ieee-nearest-bridge"
#            },
#            "name": "GigabitEthernet0/0/0/1",
#            "receive": false
#        },
#        {
#            "destination": {
#                "mac_address": "ieee-nearest-non-tmpr-bridge"
#            },
#            "name": "GigabitEthernet0/0/0/2",
#            "transmit": false
#        }
# ]
#
#
# ------------
# After state
# ------------
#
#
# RP/0/RP0/CPU0:ios#sh run int
# Mon Aug 12 12:49:51.517 UTC
# interface TenGigE0/0/0/0
#  ipv4 address 192.0.2.11 255.255.255.192
# !
# interface preconfigure GigabitEthernet0/0/0/1
#  lldp
#   receive disable
#   destination mac-address
#    ieee-nearest-bridge
#   !
#  !
# !
# interface preconfigure GigabitEthernet0/0/0/2
#  lldp
#   transmit disable
#   destination mac-address
#    ieee-nearest-non-tmpr-bridge
#   !
#  !
# !
#
#

# Using replaced
#
#
# -------------
# Before state
# -------------
#
#
# RP/0/RP0/CPU0:ios#sh run int
# Mon Aug 12 12:49:51.517 UTC
# interface TenGigE0/0/0/0
#  ipv4 address 192.0.2.11 255.255.255.192
# !
# interface preconfigure GigabitEthernet0/0/0/1
#  lldp
#   receive disable
#   destination mac-address
#    ieee-nearest-bridge
#   !
#  !
# !
# interface preconfigure GigabitEthernet0/0/0/2
#  lldp
#   transmit disable
#   destination mac-address
#    ieee-nearest-non-tmpr-bridge
#   !
#  !
# !
#
#

- name: Replace existing LLDP configurations of specified interfaces with provided
    configuration
  cisco.iosxr.iosxr_lldp_interfaces:
    config:
    - name: GigabitEthernet0/0/0/1
      destination:
        mac_address: ieee-nearest-non-tmpr-bridge
    state: replaced

#
#
# ------------------------
# Module Execution Result
# ------------------------
#
# "before": [
#        {
#            "name": "TenGigE0/0/0/0"
#        },
#        {
#            "destination": {
#                "mac_address": "ieee-nearest-bridge"
#            },
#            "name": "GigabitEthernet0/0/0/1",
#            "receive": false
#        },
#        {
#            "destination": {
#                "mac_address": "ieee-nearest-non-tmpr-bridge"
#            },
#            "name": "GigabitEthernet0/0/0/2",
#            "transmit": false
#        }
# ]
#
#
# "commands": [
#        "interface GigabitEthernet0/0/0/1",
#        "no lldp receive disable",
#        "lldp destination mac-address ieee-nearest-non-tmpr-bridge"
# ]
#
#
# "after": [
#        {
#            "name": "TenGigE0/0/0/0"
#        },
#        {
#            "destination": {
#                "mac_address": "ieee-nearest-non-tmpr-bridge"
#            },
#            "name": "GigabitEthernet0/0/0/1"
#        },
#        {
#            "destination": {
#                "mac_address": "ieee-nearest-non-tmpr-bridge"
#            },
#            "name": "GigabitEthernet0/0/0/2",
#            "transmit": false
#        }
# ]
#
#
# ------------
# After state
# ------------
#
#
# RP/0/RP0/CPU0:ios#sh run int
# Mon Aug 12 13:02:57.062 UTC
# interface TenGigE0/0/0/0
#  ipv4 address 192.0.2.11 255.255.255.192
# !
# interface preconfigure GigabitEthernet0/0/0/1
#  lldp
#   destination mac-address
#    ieee-nearest-non-tmpr-bridge
#   !
#  !
# !
# interface preconfigure GigabitEthernet0/0/0/2
#  lldp
#   transmit disable
#   destination mac-address
#    ieee-nearest-non-tmpr-bridge
#   !
#  !
# !
#
#

# Using overridden
#
#
# -------------
# Before state
# -------------
#
#
# RP/0/RP0/CPU0:ios#sh run int
# Mon Aug 12 13:15:40.465 UTC
# interface TenGigE0/0/0/0
#  ipv4 address 192.0.2.11 255.255.255.192
# !
# interface preconfigure GigabitEthernet0/0/0/1
#  lldp
#   receive disable
#   destination mac-address
#    ieee-nearest-bridge
#   !
#  !
# !
# interface preconfigure GigabitEthernet0/0/0/2
#  lldp
#   transmit disable
#   destination mac-address
#    ieee-nearest-non-tmpr-bridge
#   !
#  !
# !
#
#

- name: Override the LLDP configurations of all the interfaces with provided configurations
  cisco.iosxr.iosxr_lldp_interfaces:
    config:
    - name: GigabitEthernet0/0/0/1
      transmit: false
    state: overridden

#
#
# ------------------------
# Module Execution Result
# ------------------------
#
#
# "before": [
#        {
#            "name": "TenGigE0/0/0/0"
#        },
#        {
#            "destination": {
#                "mac_address": "ieee-nearest-bridge"
#            },
#            "name": "GigabitEthernet0/0/0/1",
#            "receive": false
#        },
#        {
#            "destination": {
#                "mac_address": "ieee-nearest-non-tmpr-bridge"
#            },
#            "name": "GigabitEthernet0/0/0/2",
#            "transmit": false
#        }
# ]
#
# "commands": [
#        "interface GigabitEthernet0/0/0/2",
#        "no lldp destination mac-address ieee-nearest-non-tmpr-bridge",
#        "no lldp transmit disable",
#        "interface GigabitEthernet0/0/0/1",
#        "no lldp destination mac-address ieee-nearest-bridge",
#        "no lldp receive disable",
#        "lldp transmit disable"
# ]
#
#
# "after": [
#        {
#            "name": "TenGigE0/0/0/0"
#        },
#        {
#            "name": "GigabitEthernet0/0/0/1",
#            "transmit": false
#        },
#        {
#            "name": "GigabitEthernet0/0/0/2"
#        }
# ]
#
#
# ------------
# After state
# ------------
#
#
# RP/0/RP0/CPU0:ios#sh run int
# Mon Aug 12 13:22:25.604 UTC
# interface TenGigE0/0/0/0
#  ipv4 address 192.0.2.11 255.255.255.192
# !
# interface preconfigure GigabitEthernet0/0/0/1
#  lldp
#   transmit disable
#  !
# !
# interface preconfigure GigabitEthernet0/0/0/2
# !
#
#

# Using deleted
#
#
# -------------
# Before state
# -------------
#
#
# RP/0/RP0/CPU0:ios#sh run int
# Mon Aug 12 13:26:21.498 UTC
# interface TenGigE0/0/0/0
#  ipv4 address 192.0.2.11 255.255.255.192
# !
# interface preconfigure GigabitEthernet0/0/0/1
#  lldp
#   receive disable
#   destination mac-address
#    ieee-nearest-bridge
#   !
#  !
# !
# interface preconfigure GigabitEthernet0/0/0/2
#  lldp
#   transmit disable
#   destination mac-address
#    ieee-nearest-non-tmpr-bridge
#   !
#  !
# !
#
#

- name: Delete LLDP configurations of all interfaces (Note - This won't delete the
    interfaces themselves)
  cisco.iosxr.iosxr_lldp_interfaces:
    state: deleted

#
#
#
# ------------------------
# Module Execution Result
# ------------------------
#
#
# "before": [
#        {
#            "name": "TenGigE0/0/0/0"
#        },
#        {
#            "destination": {
#                "mac_address": "ieee-nearest-bridge"
#            },
#            "name": "GigabitEthernet0/0/0/1",
#            "receive": false
#        },
#        {
#            "destination": {
#                "mac_address": "ieee-nearest-non-tmpr-bridge"
#            },
#            "name": "GigabitEthernet0/0/0/2",
#            "transmit": false
#        }
# ]
#
#
# "commands": [
#        "interface GigabitEthernet0/0/0/1",
#        "no lldp destination mac-address ieee-nearest-bridge",
#        "no lldp receive disable",
#        "interface GigabitEthernet0/0/0/2",
#        "no lldp destination mac-address ieee-nearest-non-tmpr-bridge",
#        "no lldp transmit disable"
# ]
#
#
# "after": [
#        {
#            "name": "TenGigE0/0/0/0"
#        },
#        {
#            "name": "GigabitEthernet0/0/0/1"
#        },
#        {
#            "name": "GigabitEthernet0/0/0/2"
#        }
# ]
#
#
# ------------
# After state
# ------------
#
#
# RP/0/RP0/CPU0:ios#sh run int
# Mon Aug 12 13:30:14.618 UTC
# interface TenGigE0/0/0/0
#  ipv4 address 192.0.2.11 255.255.255.192
# !
# interface preconfigure GigabitEthernet0/0/0/1
# !
# interface preconfigure GigabitEthernet0/0/0/2
# !
#
#
# Using parsed:
# parsed.cfg

# interface TenGigE0/0/0/0
#  ipv4 address 192.0.2.11 255.255.255.192
# !
# interface preconfigure GigabitEthernet0/0/0/1
#  lldp
#   receive disable
#   destination mac-address
#    ieee-nearest-bridge
#   !
#  !
# !
# interface preconfigure GigabitEthernet0/0/0/2
#  lldp
#   transmit disable
#   destination mac-address
#    ieee-nearest-non-tmpr-bridge

- name: Convert lacp interfaces config to argspec without connecting to the appliance
  cisco.iosxr.iosxr_lldp_interfaces:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed

# ------------------------
# Module Execution Result
# ------------------------

# parsed: [
#   - name: GigabitEthernet0/0/0/1
#       destination:
#         mac_address: ieee-nearest-non-tmpr-bridge
#       transmit: False

#     - name: GigabitEthernet0/0/0/2
#       destination:
#         mac_address: ieee-nearest-bridge
#       receive: False
#   ]

# Using gathered:
# Device config:

# RP/0/RP0/CPU0:ios#sh run int
# Mon Aug 12 12:49:51.517 UTC
# interface TenGigE0/0/0/0
#  ipv4 address 192.0.2.11 255.255.255.192
# !
# interface preconfigure GigabitEthernet0/0/0/1
#  lldp
#   receive disable
#   destination mac-address
#    ieee-nearest-bridge
#   !
#  !
# !
# interface preconfigure GigabitEthernet0/0/0/2
#  lldp
#   transmit disable
#   destination mac-address
#    ieee-nearest-non-tmpr-bridge

- name: Gather IOSXR lldp interfaces configuration
  cisco.iosxr.iosxr_lldp_interfaces:
    config:
    state: gathered

# ------------------------
# Module Execution Result
# ------------------------

#   gathered:
#     - name: GigabitEthernet0/0/0/1
#       destination:
#         mac_address: ieee-nearest-non-tmpr-bridge
#       transmit: False

#     - name: GigabitEthernet0/0/0/2
#       destination:
#         mac_address: ieee-nearest-bridge
#       receive: False

# Using rendred:
- name: Render platform specific commands from task input using rendered state
  cisco.iosxr.iosxr_lldp_interfaces:
    config:
    - name: GigabitEthernet0/0/0/1
      destination:
        mac_address: ieee-nearest-non-tmpr-bridge
      transmit: false

    - name: GigabitEthernet0/0/0/2
      destination:
        mac_address: ieee-nearest-bridge
      receive: false
    state: rendered

# ------------------------
# Module Execution Result
# ------------------------

# "rendered": [
#        "interface GigabitEthernet0/0/0/2",
#        "lldp destination mac-address ieee-nearest-non-tmpr-bridge",
#        "lldp transmit disable",
#        "interface GigabitEthernet0/0/0/1",
#        "lldp receive disable",
#        "lldp destination mac-address ieee-nearest-bridge"
# ]
```

## [Return Values](iosxr_lldp_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  Returned: when changed  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["interface GigabitEthernet0/0/0/1", "lldp destination mac-address ieee-nearest-non-tmpr-bridge", "no lldp transmit disable"]` |

### Authors

- Nilashish Chakraborty (@nilashishc)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
