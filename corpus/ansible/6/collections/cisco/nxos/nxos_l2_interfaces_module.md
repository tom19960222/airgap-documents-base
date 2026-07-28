---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_l2_interfaces module – L2 interfaces resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_l2_interfaces_module.html
fetched_at: 2026-07-27T17:01:58+00:00
---
# cisco.nxos.nxos_l2_interfaces module – L2 interfaces resource module

> **Note:**
>
> This module is part of the [cisco.nxos collection](https://galaxy.ansible.com/cisco/nxos) (version 3.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nxos`.
>
> To use it in a playbook, specify: `cisco.nxos.nxos_l2_interfaces`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_l2_interfaces_module.md#synopsis)
- [Parameters](nxos_l2_interfaces_module.md#parameters)
- [Notes](nxos_l2_interfaces_module.md#notes)
- [Examples](nxos_l2_interfaces_module.md#examples)
- [Return Values](nxos_l2_interfaces_module.md#return-values)

## [Synopsis](nxos_l2_interfaces_module.md#id1)

- This module manages Layer-2 interfaces attributes of NX-OS Interfaces.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](nxos_l2_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of Layer-2 interface options |
| **access**  dictionary | Switchport mode access command to configure the interface as a Layer-2 access. |
| **vlan**  integer | Configure given VLAN in access port. It’s used as the access VLAN ID. |
| **mode**  string | Mode in which interface needs to be configured.  Access mode is not shown in interface facts, so idempotency will not be maintained for switchport mode access and every time the output will come as changed=True.  Choices:   - `"access"` - `"trunk"` - `"fex-fabric"` - `"fabricpath"` |
| **name**  string / required | Full name of interface, i.e. Ethernet1/1. |
| **trunk**  dictionary | Switchport mode trunk command to configure the interface as a Layer-2 trunk. |
| **allowed_vlans**  string | List of allowed VLANs in a given trunk port. These are the only VLANs that will be configured on the trunk. |
| **native_vlan**  integer | Native VLAN to be configured in trunk port. It is used as the trunk native VLAN ID. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the NX-OS device by executing the command **show running-config | section ^interface**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](nxos_l2_interfaces_module.md#id3)

> **Note:**
>
> - Tested against NXOS 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS

## [Examples](nxos_l2_interfaces_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
#
# interface Ethernet1/1
#   switchport access vlan 20
# interface Ethernet1/2
#   switchport trunk native vlan 20
# interface mgmt0
#   ip address dhcp
#   ipv6 address auto-config

- name: Merge provided configuration with device configuration.
  cisco.nxos.nxos_l2_interfaces:
    config:
    - name: Ethernet1/1
      trunk:
        native_vlan: 10
        allowed_vlans: 2,4,15
    - name: Ethernet1/2
      access:
        vlan: 30
    state: merged

# After state:
# ------------
#
# interface Ethernet1/1
#   switchport trunk native vlan 10
#   switchport trunk allowed vlans 2,4,15
# interface Ethernet1/2
#   switchport access vlan 30
# interface mgmt0
#   ip address dhcp
#   ipv6 address auto-config

# Using replaced

# Before state:
# -------------
#
# interface Ethernet1/1
#   switchport access vlan 20
# interface Ethernet1/2
#   switchport trunk native vlan 20
# interface mgmt0
#   ip address dhcp
#   ipv6 address auto-config

- name: Replace device configuration of specified L2 interfaces with provided configuration.
  cisco.nxos.nxos_l2_interfaces:
    config:
    - name: Ethernet1/1
      trunk:
        native_vlan: 20
        allowed_vlans: 5-10, 15
    state: replaced

# After state:
# ------------
#
# interface Ethernet1/1
#   switchport trunk native vlan 20
#   switchport trunk allowed vlan 5-10,15
# interface Ethernet1/2
#   switchport trunk native vlan 20
#   switchport mode trunk
# interface mgmt0
#   ip address dhcp
#   ipv6 address auto-config

# Using overridden

# Before state:
# -------------
#
# interface Ethernet1/1
#   switchport access vlan 20
# interface Ethernet1/2
#   switchport trunk native vlan 20
# interface mgmt0
#   ip address dhcp
#   ipv6 address auto-config

- name: Override device configuration of all L2 interfaces on device with provided
    configuration.
  cisco.nxos.nxos_l2_interfaces:
    config:
    - name: Ethernet1/2
      access:
        vlan: 30
    state: overridden

# After state:
# ------------
#
# interface Ethernet1/1
# interface Ethernet1/2
#   switchport access vlan 30
# interface mgmt0
#   ip address dhcp
#   ipv6 address auto-config

# Using deleted

# Before state:
# -------------
#
# interface Ethernet1/1
#   switchport access vlan 20
# interface Ethernet1/2
#   switchport trunk native vlan 20
# interface mgmt0
#   ip address dhcp
#   ipv6 address auto-config

- name: Delete L2 attributes of given interfaces (Note This won't delete the interface
    itself).
  cisco.nxos.nxos_l2_interfaces:
    config:
    - name: Ethernet1/1
    - name: Ethernet1/2
    state: deleted

# After state:
# ------------
#
# interface Ethernet1/1
# interface Ethernet1/2
# interface mgmt0
#   ip address dhcp
#   ipv6 address auto-config

# Using rendered

- name: Render platform specific configuration lines (without connecting to the device)
  cisco.nxos.nxos_l2_interfaces:
    config:
    - name: Ethernet1/1
      trunk:
        native_vlan: 10
        allowed_vlans: 2,4,15
    - name: Ethernet1/2
      access:
        vlan: 30
    - name: Ethernet1/3
      trunk:
        native_vlan: 20
        allowed_vlans: 5-10, 15
    state: rendered

# Task Output (redacted)
# -----------------------

# rendered:
#  - "interface Ethernet1/1"
#  - "switchport trunk allowed vlan 2,4,15"
#  - "switchport trunk native vlan 10"
#  - "interface Ethernet1/2"
#  - "switchport access vlan 30"
#  - "interface Ethernet1/3"
#  - "switchport trunk allowed vlan 5,6,7,8,9,10,15"
#  - "switchport trunk native vlan 20"

# Using parsed

# parsed.cfg
# ------------
# interface Ethernet1/800
#   switchport access vlan 18
#   switchport trunk allowed vlan 210
# interface Ethernet1/801
#   switchport trunk allowed vlan 2,4,15

- name: Use parsed state to convert externally supplied config to structured format
  cisco.nxos.nxos_l2_interfaces:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Task output (redacted)
# -----------------------
# parsed:
#  - name: Ethernet1/800
#    access:
#      vlan: 18
#    trunk:
#      allowed_vlans: "210"
#  - name: Ethernet1/801
#    trunk:
#      allowed_vlans: "2,4,15"

# Using gathered

# Existing device config state
# -------------------------------
# Nexus9kvI5# sh running-config | section ^interface
# interface Ethernet1/1
#   switchport access vlan 6
#   switchport trunk allowed vlan 200
# interface Ethernet1/2
#   switchport trunk native vlan 10

- name: Gather l2_interfaces facts from the device using nxos_l2_interfaces
  cisco.nxos.nxos_l2_interfaces:
    state: gathered

# Task output (redacted)
# -----------------------
# gathered:
#  - name: "Ethernet1/1"
#    access:
#      vlan: 6
#    trunk:
#      allowed_vlans: "200"
#
#  - name: "Ethernet1/2"
#    trunk:
#      native_vlan: 10
```

## [Return Values](nxos_l2_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  Returned: when changed  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["interface Ethernet1/1", "switchport trunk allowed vlan 2,4,15", "switchport trunk native vlan 10", "interface Ethernet1/2", "switchport access vlan 30", "interface Ethernet1/3", "switchport trunk allowed vlan 5,6,7,8,9,10,15", "switchport trunk native vlan 20"]` |

### Authors

- Trishna Guha (@trishnaguha)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
