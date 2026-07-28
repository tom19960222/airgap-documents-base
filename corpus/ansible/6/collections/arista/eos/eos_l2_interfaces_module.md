---
collection: ansible
version: "6"
title: "arista.eos.eos_l2_interfaces module – L2 interfaces resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/arista/eos/eos_l2_interfaces_module.html
fetched_at: 2026-07-27T16:45:10+00:00
---
# arista.eos.eos_l2_interfaces module – L2 interfaces resource module

> **Note:**
>
> This module is part of the [arista.eos collection](https://galaxy.ansible.com/arista/eos) (version 5.0.1).
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

## [Parameters](eos_l2_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of Layer-2 interface options |
| **access**  dictionary | Switchport mode access command to configure the interface as a layer 2 access. |
| **vlan**  integer | Configure given VLAN in access port. It’s used as the access VLAN ID. |
| **mode**  string | Mode in which interface needs to be configured.  Access mode is not shown in interface facts, so idempotency will not be maintained for switchport mode access and every time the output will come as changed=True.  Choices:   - `"access"` - `"trunk"` |
| **name**  string / required | Full name of interface, e.g. Ethernet1. |
| **trunk**  dictionary | Switchport mode trunk command to configure the interface as a Layer 2 trunk. |
| **native_vlan**  integer | Native VLAN to be configured in trunk port. It is used as the trunk native VLAN ID. |
| **trunk_allowed_vlans**  list / elements=string | List of allowed VLANs in a given trunk port. These are the only VLANs that will be configured on the trunk. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the EOS device by executing the command **show running-config | section ^interface**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"parsed"` - `"rendered"` - `"gathered"` |

## [Notes](eos_l2_interfaces_module.md#id3)

> **Note:**
>
> - Tested against Arista EOS 4.24.6F
> - This module works with connection `network_cli`. See the [EOS Platform Options](../network/user_guide/platform_eos.md).

## [Examples](eos_l2_interfaces_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
#
# veos#show running-config | section interface
# interface Ethernet1
#    switchport access vlan 20
# !
# interface Ethernet2
#    switchport trunk native vlan 20
#    switchport mode trunk
# !
# interface Management1
#    ip address dhcp
#    ipv6 address auto-config
# !

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

# After state:
# ------------
#
# veos#show running-config | section interface
# interface Ethernet1
#    switchport trunk native vlan 10
#    switchport mode trunk
# !
# interface Ethernet2
#    switchport access vlan 30
# !
# interface Management1
#    ip address dhcp
#    ipv6 address auto-config
# !

# Using replaced

# Before state:
# -------------
#
# veos2#show running-config | s int
# interface Ethernet1
#    switchport access vlan 20
# !
# interface Ethernet2
#    switchport trunk native vlan 20
#    switchport mode trunk
# !
# interface Management1
#    ip address dhcp
#    ipv6 address auto-config
# !

- name: Replace device configuration of specified L2 interfaces with provided configuration.
  arista.eos.eos_l2_interfaces:
    config:
    - name: Ethernet1
      mode: trunk
      trunk:
        native_vlan: 20
        trunk_allowed_vlans: 5-10, 15
    state: replaced

# After state:
# ------------
#
# veos#show running-config | section interface
# interface Ethernet1
#    switchport trunk native vlan 20
#    switchport trunk allowed vlan 5-10,15
#    switchport mode trunk
# !
# interface Ethernet2
#    switchport trunk native vlan 20
#    switchport mode trunk
# !
# interface Management1
#    ip address dhcp
#    ipv6 address auto-config
# !

# Using overridden

# Before state:
# -------------
#
# veos#show running-config | section interface
# interface Ethernet1
#    switchport access vlan 20
# !
# interface Ethernet2
#    switchport trunk native vlan 20
#    switchport mode trunk
# !
# interface Management1
#    ip address dhcp
#    ipv6 address auto-config
# !

- name: Override device configuration of all L2 interfaces on device with provided
    configuration.
  arista.eos.eos_l2_interfaces:
    config:
    - name: Ethernet2
      mode: access
      access:
        vlan: 30
    state: overridden

# After state:
# ------------
#
# veos#show running-config | section interface
# interface Ethernet1
# !
# interface Ethernet2
#    switchport access vlan 30
# !
# interface Management1
#    ip address dhcp
#    ipv6 address auto-config
# !

# Using deleted

# Before state:
# -------------
#
# veos#show running-config | section interface
# interface Ethernet1
#    switchport access vlan 20
# !
# interface Ethernet2
#    switchport trunk native vlan 20
#    switchport mode trunk
# !
# interface Management1
#    ip address dhcp
#    ipv6 address auto-config
# !

- name: Delete EOS L2 interfaces as in given arguments.
  arista.eos.eos_l2_interfaces:
    config:
    - name: Ethernet1
    - name: Ethernet2
    state: deleted

# After state:
# ------------
#
# veos#show running-config | section interface
# interface Ethernet1
# !
# interface Ethernet2
# !
# interface Management1
#    ip address dhcp
#    ipv6 address auto-config

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
    state: merged

# Output :
# ------------
#
# - "interface Ethernet1"
# - "switchport trunk native vlan 10"
# - "switchport mode trunk"
# - "interface Ethernet2"
# - "switchport access vlan 30"
# - "interface Management1"
# - "ip address dhcp"
# - "ipv6 address auto-config"

# using parsed

# parsed.cfg

# interface Ethernet1
#    switchport trunk native vlan 10
#    switchport mode trunk
# !
# interface Ethernet2
#    switchport access vlan 30
# !

- name: Use parsed to convert native configs to structured data
  arista.eos.l2_interfaces:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Output:
#   parsed:
#      - name: Ethernet1
#        mode: trunk
#        trunk:
#          native_vlan: 10
#      - name: Ethernet2
#        mode: access
#        access:
#          vlan: 30

# Using gathered:
# Existing config on the device:
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
# output:
#   gathered:
#      - name: Ethernet1
#        mode: trunk
#        trunk:
#          native_vlan: 10
#      - name: Ethernet2
#        mode: access
#        access:
#          vlan: 30
```

## [Return Values](eos_l2_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  Returned: when changed  Sample: `["The configuration returned will always be in the same format of the parameters above."]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format of the parameters above."]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["interface Ethernet2", "switchport access vlan 20"]` |

### Authors

- Nathaniel Case (@qalthos)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
[Repository (Sources)](https://github.com/ansible-collections/arista.eos)
