---
collection: ansible
version: "8"
title: "cisco.ios.ios_l2_interfaces module – Resource module to configure L2 interfaces."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ios/ios_l2_interfaces_module.html
fetched_at: 2026-07-28T01:26:10+00:00
---
# cisco.ios.ios_l2_interfaces module – Resource module to configure L2 interfaces.

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
> To use it in a playbook, specify: `cisco.ios.ios_l2_interfaces`.

New in cisco.ios 1.0.0

- [Synopsis](ios_l2_interfaces_module.md#synopsis)
- [Parameters](ios_l2_interfaces_module.md#parameters)
- [Notes](ios_l2_interfaces_module.md#notes)
- [Examples](ios_l2_interfaces_module.md#examples)
- [Return Values](ios_l2_interfaces_module.md#return-values)

## [Synopsis](ios_l2_interfaces_module.md#id1)

- This module provides declarative management of Layer-2 interface on Cisco IOS devices.

Aliases: l2_interfaces

## [Parameters](ios_l2_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of Layer-2 interface options |
| **access**  dictionary | Switchport mode access command to configure the interface as a layer 2 access. |
| **vlan**  integer | Configure given VLAN in access port. It’s used as the access VLAN ID. |
| **vlan_name**  string | Set VLAN when interface is in access mode. |
| **mode**  string | Mode in which interface needs to be configured.  An interface whose trunk encapsulation is “Auto” can not be configured to “trunk” mode.  **Choices:**   - `"access"` - `"trunk"` - `"dot1q_tunnel"` - `"dynamic"` - `"dynamic_auto"` - `"dynamic_desirable"` - `"private_vlan_host"` - `"private_vlan_promiscuous"` - `"private_vlan_trunk"` |
| **name**  string / required | Full name of the interface excluding any logical unit number, i.e GigabitEthernet0/1. |
| **trunk**  dictionary | Switchport mode trunk command to configure the interface as a Layer 2 trunk. Note The encapsulation is always set to dot1q. |
| **allowed_vlans**  list / elements=string | List of allowed VLANs in a given trunk port. These are the only VLANs that will be configured on the trunk. |
| **encapsulation**  string | Trunking encapsulation when interface is in trunking mode.  **Choices:**   - `"dot1q"` - `"isl"` - `"negotiate"` |
| **native_vlan**  integer | Native VLAN to be configured in trunk port. It’s used as the trunk native VLAN ID. |
| **pruning_vlans**  list / elements=string | Pruning VLAN to be configured in trunk port. It’s used as the trunk pruning VLAN ID. |
| **voice**  dictionary | Switchport mode voice command to configure the interface with a voice vlan. |
| **vlan**  integer | Configure given voice VLAN on access port. It’s used as the voice VLAN ID. |
| **vlan_name**  string | Set VLAN when interface is in access mode. |
| **vlan_tag**  string | Set VLAN Tag. dot1p (Priority tagged on PVID) none (Don’t tell telephone about voice vlan) untagged (Untagged on PVID)  **Choices:**   - `"dot1p"` - `"none"` - `"untagged"` |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS device by executing the command **show running-config | section ^interface**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  The states *rendered*, *gathered* and *parsed* does not perform any change on the device.  The state *rendered* will transform the configuration in `config` option to platform specific CLI commands which will be returned in the *rendered* key within the result. For state *rendered* active connection to remote host is not required.  The state *gathered* will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the *gathered* key within the result.  The state *parsed* reads the configuration from `running_config` option and transforms it into JSON format as per the resource module parameters and the value is returned in the *parsed* key within the result. The value of `running_config` option should be the same format as the output of command *show running-config | include ip route|ipv6 route* executed on device. For state *parsed* active connection to remote host is not required.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"rendered"` - `"gathered"` - `"parsed"` |

## [Notes](ios_l2_interfaces_module.md#id3)

> **Note:**
>
> - Tested against Cisco IOSv Version 15.2 on CML.
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>
> - The module examples uses callback plugin (stdout_callback = yaml) to generate task output in yaml format.

## [Examples](ios_l2_interfaces_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
#
# viosl2#show running-config | section ^interface
# interface GigabitEthernet0/1
#  description Configured by Ansible
#  negotiation auto
# interface GigabitEthernet0/2
#  description This is test
#  switchport access vlan 20
#  media-type rj45
#  negotiation auto

- name: Merge provided configuration with device configuration
  cisco.ios.ios_l2_interfaces:
    config:
      - name: GigabitEthernet0/1
        mode: access
        access:
          vlan: 10
        voice:
          vlan: 40
      - name: GigabitEthernet0/2
        mode: trunk
        trunk:
          allowed_vlans: 10-20,40
          native_vlan: 20
          pruning_vlans: 10,20
          encapsulation: dot1q
    state: merged

# Task Output
# -----------
#
# before:
# - name: GigabitEthernet0/1
# - access:
#     vlan: 20
#   name: GigabitEthernet0/2
# commands:
# - interface GigabitEthernet0/1
# - switchport access vlan 10
# - switchport voice vlan 40
# - switchport mode access
# - interface GigabitEthernet0/2
# - switchport mode trunk
# - switchport trunk encapsulation dot1q
# - switchport trunk native vlan 20
# - switchport trunk allowed vlan 10-20,40
# - switchport trunk pruning vlan 10,20
# after:
# - access:
#     vlan: 10
#   mode: access
#   name: GigabitEthernet0/1
#   voice:
#     vlan: 40
# - mode: trunk
#   name: GigabitEthernet0/2
#   trunk:
#     allowed_vlans:
#     - 10-20
#     - '40'
#     encapsulation: dot1q
#     native_vlan: 20
#     pruning_vlans:
#     - '10'
#     - '20'

# After state:
# ------------
#
# viosl2#show running-config | section ^interface
# interface GigabitEthernet0/1
#  description Configured by Ansible
#  switchport access vlan 10
#  switchport voice vlan 40
#  switchport mode access
#  negotiation auto
# interface GigabitEthernet0/2
#  description This is test
#  switchport trunk allowed vlan 10-20,40
#  switchport trunk encapsulation dot1q
#  switchport trunk native vlan 20
#  switchport trunk pruning vlan 10,20
#  switchport mode trunk
#  media-type rj45
#  negotiation auto

# Using replaced

# Before state:
# -------------
#
# viosl2#show running-config | section ^interface
# interface GigabitEthernet0/1
#  description Configured by Ansible
#  switchport access vlan 20
#  negotiation auto
# interface GigabitEthernet0/2
#  description This is test
#  switchport access vlan 20
#  media-type rj45
#  negotiation auto

- name: Replaces device configuration with provided configuration
  cisco.ios.ios_l2_interfaces:
    config:
      - name: GigabitEthernet0/2
        trunk:
          allowed_vlans: 20-25,40
          native_vlan: 20
          pruning_vlans: 10
          encapsulation: isl
    state: replaced

# Task Output
# -----------
#
# before:
# - name: GigabitEthernet0/1
# - access:
#     vlan: 20
#   name: GigabitEthernet0/2
# commands:
# - interface GigabitEthernet0/2
# - no switchport access vlan
# - switchport trunk encapsulation isl
# - switchport trunk native vlan 20
# - switchport trunk allowed vlan 20-25,40
# - switchport trunk pruning vlan 10
# after:
# - access:
#     vlan: 20
#   name: GigabitEthernet0/1
# - name: GigabitEthernet0/2
#   trunk:
#     allowed_vlans:
#     - 20-25
#     - '40'
#     encapsulation: isl
#     native_vlan: 20
#     pruning_vlans:
#     - '10'

# After state:
# -------------
#
# viosl2#show running-config | section ^interface
# interface GigabitEthernet0/1
#  description Configured by Ansible
#  switchport access vlan 20
#  negotiation auto
# interface GigabitEthernet0/2
#  description This is test
#  switchport trunk allowed vlan 20-25,40
#  switchport trunk encapsulation isl
#  switchport trunk native vlan 20
#  switchport trunk pruning vlan 10
#  media-type rj45
#  negotiation auto

# Using overridden

# Before state:
# -------------
#
# viosl2#show running-config | section ^interface
# interface GigabitEthernet0/1
#  description Configured by Ansible
#  switchport trunk encapsulation dot1q
#  switchport trunk native vlan 20
#  negotiation auto
# interface GigabitEthernet0/2
#  description This is test
#  switchport access vlan 20
#  switchport trunk encapsulation dot1q
#  switchport trunk native vlan 20
#  media-type rj45
#  negotiation auto

- name: Override device configuration of all l2 interfaces with provided configuration
  cisco.ios.ios_l2_interfaces:
    config:
      - name: GigabitEthernet0/2
        access:
          vlan: 20
        voice:
          vlan: 40
    state: overridden

# Task Output
# -----------
#
# before:
# - name: GigabitEthernet0/1
#   trunk:
#     encapsulation: dot1q
#     native_vlan: 20
# - access:
#     vlan: 20
#   name: GigabitEthernet0/2
#   trunk:
#     encapsulation: dot1q
#     native_vlan: 20
# commands:
# - interface GigabitEthernet0/1
# - no switchport trunk encapsulation
# - no switchport trunk native vlan
# - interface GigabitEthernet0/2
# - switchport voice vlan 40
# - no switchport trunk encapsulation
# - no switchport trunk native vlan
# after:
# - name: GigabitEthernet0/1
# - access:
#     vlan: 20
#   name: GigabitEthernet0/2
#   voice:
#     vlan: 40

# After state:
# -------------
#
# viosl2#show running-config | section ^interface
# interface GigabitEthernet0/1
#  description Configured by Ansible
#  negotiation auto
# interface GigabitEthernet0/2
#  description This is test
#  switchport access vlan 20
#  switchport voice vlan 40
#  media-type rj45
#  negotiation auto

# Using deleted

# Before state:
# -------------
#
# viosl2#show running-config | section ^interface
# interface GigabitEthernet0/1
#  description Configured by Ansible
#  switchport access vlan 20
#  negotiation auto
# interface GigabitEthernet0/2
#  description This is test
#  switchport access vlan 20
#  switchport trunk allowed vlan 20-40,60,80
#  switchport trunk encapsulation dot1q
#  switchport trunk native vlan 10
#  switchport trunk pruning vlan 10
#  media-type rj45
#  negotiation auto

- name: Delete IOS L2 interfaces as in given arguments
  cisco.ios.ios_l2_interfaces:
    config:
      - name: GigabitEthernet0/1
    state: deleted

# Task Output
# -----------
#
# before:
# - access:
#     vlan: 20
#   name: GigabitEthernet0/1
# - access:
#     vlan: 20
#   name: GigabitEthernet0/2
#   trunk:
#     allowed_vlans:
#     - 20-40
#     - '60'
#     - '80'
#     encapsulation: dot1q
#     native_vlan: 10
#     pruning_vlans:
#     - '10'
# commands:
# - interface GigabitEthernet0/1
# - no switchport access vlan
# after:
# - name: GigabitEthernet0/1
# - access:
#     vlan: 20
#   name: GigabitEthernet0/2
#   trunk:
#     allowed_vlans:
#     - 20-40
#     - '60'
#     - '80'
#     encapsulation: dot1q
#     native_vlan: 10
#     pruning_vlans:
#     - '10'

# After state:
# -------------
#
# viosl2#show running-config | section ^interface
# interface GigabitEthernet0/1
#  description Configured by Ansible
#  negotiation auto
# interface GigabitEthernet0/2
#  description This is test
#  switchport access vlan 20
#  switchport trunk allowed vlan 20-40,60,80
#  switchport trunk encapsulation dot1q
#  switchport trunk native vlan 10
#  switchport trunk pruning vlan 10
#  media-type rj45
#  negotiation auto

# Using deleted without config - delete all configuration

# Before state:
# -------------
#
# viosl2#show running-config | section ^interface
# interface GigabitEthernet0/1
#  description Configured by Ansible
#  switchport access vlan 20
#  negotiation auto
# interface GigabitEthernet0/2
#  description This is test
#  switchport access vlan 20
#  switchport trunk allowed vlan 20-40,60,80
#  switchport trunk encapsulation dot1q
#  switchport trunk native vlan 10
#  switchport trunk pruning vlan 10
#  media-type rj45
#  negotiation auto

- name: Delete IOS L2 interfaces as in given arguments
  cisco.ios.ios_l2_interfaces:
    state: deleted

# Task Output
# -----------
#
# before:
# - access:
#     vlan: 20
#   name: GigabitEthernet0/1
# - access:
#     vlan: 20
#   name: GigabitEthernet0/2
#   trunk:
#     allowed_vlans:
#     - 20-40
#     - '60'
#     - '80'
#     encapsulation: dot1q
#     native_vlan: 10
#     pruning_vlans:
#     - '10'
# commands:
# - interface GigabitEthernet0/1
# - no switchport access vlan
# - interface GigabitEthernet0/2
# - no switchport access vlan
# - no switchport trunk encapsulation
# - no switchport trunk native vlan
# - no switchport trunk allowed vlan
# - no switchport trunk pruning vlan
# after:
# - name: GigabitEthernet0/1
# - name: GigabitEthernet0/2

# After state:
# -------------
#
# viosl2#show running-config | section ^interface
# interface GigabitEthernet0/1
#  description Configured by Ansible
#  negotiation auto
# interface GigabitEthernet0/2
#  description This is test
#  media-type rj45
#  negotiation auto

# Using gathered

# Before state:
# -------------
#
# vios#sh running-config | section ^interface
# interface GigabitEthernet0/1
#  description Configured by Ansible
#  switchport access vlan 20
#  negotiation auto
# interface GigabitEthernet0/2
#  description This is test
#  switchport access vlan 20
#  switchport trunk allowed vlan 20-40,60,80
#  switchport trunk encapsulation dot1q
#  switchport trunk native vlan 10
#  switchport trunk pruning vlan 10
#  media-type rj45
#  negotiation auto

- name: Gather facts for l2 interfaces
  cisco.ios.ios_l2_interfaces:
    config:
    state: gathered

# Task Output
# -----------
#
# gathered:
# - access:
#     vlan: 20
#   name: GigabitEthernet0/1
# - access:
#     vlan: 20
#   name: GigabitEthernet0/2
#   trunk:
#     allowed_vlans:
#     - 20-40
#     - '60'
#     - '80'
#     encapsulation: dot1q
#     native_vlan: 10
#     pruning_vlans:
#     - '10'

# Using rendered

- name: Render the commands for provided  configuration
  cisco.ios.ios_l2_interfaces:
    config:
      - name: GigabitEthernet0/1
        access:
          vlan: 30
      - name: GigabitEthernet0/2
        trunk:
          allowed_vlans: 10-20,40
          native_vlan: 20
          pruning_vlans: 10,20
          encapsulation: dot1q
    state: rendered

# Task Output
# -----------
#
# rendered:
# - interface GigabitEthernet0/1
# - switchport access vlan 30
# - interface GigabitEthernet0/2
# - switchport trunk encapsulation dot1q
# - switchport trunk native vlan 20
# - switchport trunk allowed vlan 10-20,40
# - switchport trunk pruning vlan 10,20

# Using Parsed

# File: parsed.cfg
# ----------------
#
# interface GigabitEthernet0/1
#  description Configured by Ansible
#  switchport access vlan 20
#  negotiation auto
# interface GigabitEthernet0/2
#  description This is test
#  switchport access vlan 20
#  switchport trunk allowed vlan 20-40,60,80
#  switchport trunk encapsulation dot1q
#  switchport trunk native vlan 10
#  switchport trunk pruning vlan 10
#  media-type rj45
#  negotiation auto

- name: Parse the commands for provided configuration
  cisco.ios.ios_l2_interfaces:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Task Output
# -----------
#
# parsed:
# - access:
#     vlan: 20
#   name: GigabitEthernet0/1
# - access:
#     vlan: 20
#   name: GigabitEthernet0/2
#   trunk:
#     allowed_vlans:
#     - 20-40
#     - '60'
#     - '80'
#     encapsulation: dot1q
#     native_vlan: 10
#     pruning_vlans:
#     - '10'
```

## [Return Values](ios_l2_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  **Returned:** when changed  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `["interface GigabitEthernet0/2", "switchport trunk allowed vlan 15-20,40", "switchport trunk encapsulation dot1q"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when *state* is `gathered`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when *state* is `parsed`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when *state* is `rendered`  **Sample:** `["interface GigabitEthernet0/1", "switchport access vlan 30", "switchport trunk encapsulation dot1q"]` |

### Authors

- Sagar Paul (@KB-petByte)
- Sumit Jaiswal (@justjais)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
