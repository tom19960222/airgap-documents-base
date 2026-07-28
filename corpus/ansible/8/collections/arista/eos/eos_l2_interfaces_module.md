---
collection: ansible
version: "8"
title: "arista.eos.eos_l2_interfaces module – L2 interfaces resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/arista/eos/eos_l2_interfaces_module.html
fetched_at: 2026-07-28T01:11:03+00:00
---
# arista.eos.eos_l2_interfaces module – L2 interfaces resource module

> **Note:**
>
> This module is part of the [arista.eos collection](https://galaxy.ansible.com/ui/repo/published/arista/eos/) (version 6.2.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install arista.eos`.
>
> To use it in a playbook, specify: `arista.eos.eos_l2_interfaces`.

New in arista.eos 1.0.0

- [Synopsis](eos_l2_interfaces_module.md#synopsis)
- [Parameters](eos_l2_interfaces_module.md#parameters)
- [Notes](eos_l2_interfaces_module.md#notes)
- [Examples](eos_l2_interfaces_module.md#examples)
- [Return Values](eos_l2_interfaces_module.md#return-values)

## [Synopsis](eos_l2_interfaces_module.md#id1)

- This module provides declarative management of Layer-2 interface on Arista EOS devices.

Aliases: l2_interfaces

## [Parameters](eos_l2_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of Layer-2 interface options |
| **access**  dictionary | Switchport mode access command to configure the interface as a layer 2 access. |
| **vlan**  integer | Configure given VLAN in access port. It’s used as the access VLAN ID. |
| **mode**  string | Mode in which interface needs to be configured.  Access mode is not shown in interface facts, so idempotency will not be maintained for switchport mode access and every time the output will come as changed=True.  **Choices:**   - `"access"` - `"trunk"` |
| **name**  string / required | Full name of interface, e.g. Ethernet1. |
| **trunk**  dictionary | Switchport mode trunk command to configure the interface as a Layer 2 trunk. |
| **native_vlan**  integer | Native VLAN to be configured in trunk port. It is used as the trunk native VLAN ID. |
| **trunk_allowed_vlans**  list / elements=string | List of allowed VLANs in a given trunk port. These are the only VLANs that will be configured on the trunk. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the EOS device by executing the command **show running-config | section ^interface**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"parsed"` - `"rendered"` - `"gathered"` |

## [Notes](eos_l2_interfaces_module.md#id3)

> **Note:**
>
> - Tested against Arista EOS 4.24.6F
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_eos.html>

## [Examples](eos_l2_interfaces_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
#
# test#show running-config | section interface
# interface Ethernet1
# !
# interface Ethernet2
#    description Configured by Ansible
#    shutdown
# !
# interface Management1
#    ip address dhcp
#    dhcp client accept default-route

- name: Merge provided configuration with device configuration.
  arista.eos.eos_l2_interfaces:
    config:
      - name: Ethernet1
        mode: trunk
        trunk:
          native_vlan: 10
      - name: Ethernet2
        mode: access
        access:
          vlan: 30
    state: merged

# Task Output
# -----------
#
# before:
# - name: Ethernet1
# - name: Ethernet2
# - name: Management1
# commands:
# - interface Ethernet1
# - switchport mode trunk
# - switchport trunk native vlan 10
# - interface Ethernet2
# - switchport mode access
# - switchport access vlan 30
# after:
# - mode: trunk
#   name: Ethernet1
#   trunk:
#     native_vlan: 10
# - access:
#     vlan: 30
#   name: Ethernet2
# - name: Management1

# After state:
# ------------
#
# test#show running-config | section interface
# interface Ethernet1
#    switchport trunk native vlan 10
#    switchport mode trunk
# !
# interface Ethernet2
#    description Configured by Ansible
#    shutdown
#    switchport access vlan 30
# !
# interface Management1
#    ip address dhcp
#    dhcp client accept default-route

# Using replaced

# Before state:
# -------------
#
# test#show running-config | section interface
# interface Ethernet1
#    switchport trunk native vlan 10
#    switchport mode trunk
# !
# interface Ethernet2
#    description Configured by Ansible
#    shutdown
#    switchport access vlan 30
# !
# interface Management1
#    ip address dhcp
#    dhcp client accept default-route

- name: Replace device configuration of specified L2 interfaces with provided configuration.
  arista.eos.eos_l2_interfaces:
    config:
      - name: Ethernet1
        mode: trunk
        trunk:
          native_vlan: 20
          trunk_allowed_vlans: 5-10, 15
    state: replaced

# Task Output
# -----------
#
# before:
# - mode: trunk
#   name: Ethernet1
#   trunk:
#     native_vlan: 10
# - access:
#     vlan: 30
#   name: Ethernet2
# - name: Management1
# commands:
# - interface Ethernet1
# - switchport trunk native vlan 20
# - switchport trunk allowed vlan 10,15,5,6,7,8,9
# after:
# - mode: trunk
#   name: Ethernet1
#   trunk:
#     native_vlan: 20
#     trunk_allowed_vlans:
#     - 5-10
#     - '15'
# - access:
#     vlan: 30
#   name: Ethernet2
# - name: Management1

# After state:
# ------------
#
# test#show running-config | section interface
# interface Ethernet1
#    switchport trunk native vlan 20
#    switchport trunk allowed vlan 5-10,15
#    switchport mode trunk
# !
# interface Ethernet2
#    description Configured by Ansible
#    shutdown
#    switchport access vlan 30
# !
# interface Management1
#    ip address dhcp
#    dhcp client accept default-route

# Using overridden

# Before state:
# -------------
#
# test#show running-config | section interface
# interface Ethernet1
#    switchport trunk native vlan 20
#    switchport trunk allowed vlan 5-10,15
#    switchport mode trunk
# !
# interface Ethernet2
#    description Configured by Ansible
#    shutdown
#    switchport access vlan 30
# !
# interface Management1
#    ip address dhcp
#    dhcp client accept default-route

- name: Override device configuration of all L2 interfaces on device with provided
    configuration.
  arista.eos.eos_l2_interfaces:
    config:
      - name: Ethernet2
        mode: access
        access:
          vlan: 30
    state: overridden

# Task Output
# -----------
#
# before:
# - mode: trunk
#   name: Ethernet1
#   trunk:
#     native_vlan: 20
#     trunk_allowed_vlans:
#     - 5-10
#     - '15'
# - access:
#     vlan: 30
#   name: Ethernet2
# - name: Management1
# commands:
# - interface Ethernet1
# - no switchport mode
# - no switchport trunk allowed vlan
# - no switchport trunk native vlan
# - interface Ethernet2
# - switchport mode access
# after:
# - name: Ethernet1
# - access:
#     vlan: 30
#   name: Ethernet2
# - name: Management1

# After state:
# ------------
#
# test#show running-config | section interface
# interface Ethernet1
# !
# interface Ethernet2
#    description Configured by Ansible
#    shutdown
#    switchport access vlan 30
# !
# interface Management1
#    ip address dhcp
#    dhcp client accept default-route

# Using deleted

# Before state:
# -------------
#
# test#show running-config | section interface
# interface Ethernet1
# !
# interface Ethernet2
#    description Configured by Ansible
#    shutdown
#    switchport access vlan 30
# !
# interface Management1
#    ip address dhcp
#    dhcp client accept default-route

- name: Delete EOS L2 interfaces as in given arguments.
  arista.eos.eos_l2_interfaces:
    config:
      - name: Ethernet1
      - name: Ethernet2
    state: deleted

# Task Output
# -----------
#
# before:
# - name: Ethernet1
# - access:
#     vlan: 30
#   name: Ethernet2
# - name: Management1
# commands:
# - interface Ethernet2
# - no switchport access vlan
# after:
# - name: Ethernet1
# - name: Ethernet2
# - name: Management1

# After state:
# ------------
#
# test#show running-config | section interface
# interface Ethernet1
# !
# interface Ethernet2
#    description Configured by Ansible
#    shutdown
# !
# interface Management1
#    ip address dhcp
#    dhcp client accept default-route

# using rendered

- name: Use Rendered to convert the structured data to native config
  arista.eos.eos_l2_interfaces:
    config:
      - name: Ethernet1
        mode: trunk
        trunk:
          native_vlan: 10
      - name: Ethernet2
        mode: access
        access:
          vlan: 30
    state: rendered

# Module Execution Result:
# ------------------------
#
# rendered:
# - interface Ethernet1
# - switchport mode trunk
# - switchport trunk native vlan 10
# - interface Ethernet2
# - switchport mode access
# - switchport access vlan 30

# Using parsed

# File: parsed.cfg
# ----------------
#
# interface Ethernet1
#    switchport trunk native vlan 10
#    switchport mode trunk
# !
# interface Ethernet2
#    switchport access vlan 30
# !

- name: Parse the commands for provided configuration
  arista.eos.l2_interfaces:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Module Execution Result:
# ------------------------
#
# parsed:
#  - name: Ethernet1
#    mode: trunk
#    trunk:
#      native_vlan: 10
#  - name: Ethernet2
#    mode: access
#    access:
#      vlan: 30

# Using gathered

# Before state:
# -------------
#
# veos#show running-config | section interface
# interface Ethernet1
#    switchport trunk native vlan 10
#    switchport mode trunk
# !
# interface Ethernet2
#    switchport access vlan 30
# !

- name: Gather interfaces facts from the device
  arista.eos.l2_interfaces:
    state: gathered

# Module Execution Result:
# ------------------------
#
# gathered:
# - name: Ethernet1
#   mode: trunk
#   trunk:
#     native_vlan: 10
# - name: Ethernet2
#   mode: access
#   access:
#     vlan: 30
```

## [Return Values](eos_l2_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  **Returned:** when changed  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `["interface Ethernet1", "switchport mode trunk", "switchport access vlan 20"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when *state* is `gathered`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when *state* is `parsed`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when *state* is `rendered`  **Sample:** `["interface Ethernet1", "switchport mode trunk", "switchport access vlan 20"]` |

### Authors

- Nathaniel Case (@Qalthos)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/arista.eos)
