---
collection: ansible
version: "8"
title: "arista.eos.eos_l3_interfaces module – L3 interfaces resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/arista/eos/eos_l3_interfaces_module.html
fetched_at: 2026-07-28T01:04:30+00:00
---
# arista.eos.eos_l3_interfaces module – L3 interfaces resource module

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
> To use it in a playbook, specify: `arista.eos.eos_l3_interfaces`.

New in arista.eos 1.0.0

- [Synopsis](eos_l3_interfaces_module.md#synopsis)
- [Parameters](eos_l3_interfaces_module.md#parameters)
- [Notes](eos_l3_interfaces_module.md#notes)
- [Examples](eos_l3_interfaces_module.md#examples)
- [Return Values](eos_l3_interfaces_module.md#return-values)

## [Synopsis](eos_l3_interfaces_module.md#id1)

- This module provides declarative management of Layer 3 interfaces on Arista EOS devices.

Aliases: l3_interfaces

## [Parameters](eos_l3_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of Layer 3 interface options |
| **ipv4**  list / elements=dictionary | List of IPv4 addresses to be set for the Layer 3 interface mentioned in *name* option. |
| **address**  string | IPv4 address to be set in the format <ipv4 address>/<mask> eg. 192.0.2.1/24, or `dhcp` to query DHCP for an IP address. |
| **secondary**  boolean | Whether or not this address is a secondary address.  **Choices:**   - `false` - `true` |
| **virtual**  boolean | Whether or not this address is a virtual address.  **Choices:**   - `false` - `true` |
| **ipv6**  list / elements=dictionary | List of IPv6 addresses to be set for the Layer 3 interface mentioned in *name* option. |
| **address**  string | IPv6 address to be set in the address format is <ipv6 address>/<mask> eg. 2001:db8:2201:1::1/64 or `auto-config` to use SLAAC to chose an address. |
| **name**  string / required | Full name of the interface, i.e. Ethernet1. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the EOS device by executing the command **show running-config | section ^interface**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"parsed"` - `"gathered"` - `"rendered"` |

## [Notes](eos_l3_interfaces_module.md#id3)

> **Note:**
>
> - Tested against Arista EOS 4.24.6F
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_eos.html> ‘eos_l2_interfaces/eos_interfaces’ should be used for preparing the interfaces, before applying L3 configurations using this module (eos_l3_interfaces).

## [Examples](eos_l3_interfaces_module.md#id4)

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
  arista.eos.eos_l3_interfaces:
    config:
      - name: Ethernet1
        ipv4:
          - address: 198.51.100.14/24
      - name: Ethernet2
        ipv4:
          - address: 203.0.113.27/24
    state: merged

# Task Output
# -----------
#
# before:
# - name: Ethernet1
# - name: Ethernet2
# - ipv4:
#   - address: dhcp
#   name: Management1
# commands:
# - interface Ethernet1
# - ip address 198.51.100.14/24
# - interface Ethernet2
#   - ip address 203.0.113.27/24
# after:
# - ipv4:
#   - address: 198.51.100.14/24
#   name: Ethernet1
# - ipv4:
#   - address: 203.0.113.27/24
#   name: Ethernet2
# - ipv4:
#   - address: dhcp
#   name: Management1

# After state:
# ------------
#
# test#show running-config | section interface
# interface Ethernet1
#    ip address 198.51.100.14/24
# !
# interface Ethernet2
#    description Configured by Ansible
#    shutdown
#    ip address 203.0.113.27/24
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
#    ip address 198.51.100.14/24
# !
# interface Ethernet2
#    ip address 203.0.113.27/24
# !
# interface Management1
#    ip address dhcp
#    dhcp client accept default-route

- name: Override device configuration of all L2 interfaces on device with provided
    configuration.
  arista.eos.eos_l3_interfaces:
    config:
      - name: Ethernet1
        ipv6:
          - address: 2001:db8:feed::1/96
      - name: Ethernet2
        ipv4:
          - address: 203.0.113.27/24
      - ipv4:
          - address: dhcp
        name: Management1
    state: overridden

# Task Output
# -----------
#
# before:
# - ipv4:
#   - address: 198.51.100.14/24
#   name: Ethernet1
# - ipv4:
#   - address: 203.0.113.27/24
#   name: Ethernet2
# - ipv4:
#   - address: dhcp
#   name: Management1
# commands:
# - interface Ethernet1
# - ipv6 address 2001:db8:feed::1/96
# - no ip address
# after:
# - ipv6:
#   - address: 2001:db8:feed::1/96
#   name: Ethernet1
# - ipv4:
#   - address: 203.0.113.27/24
#   name: Ethernet2
# - ipv4:
#   - address: dhcp
#   name: Management1

# After state:
# ------------
#
# test#show running-config | section interface
# interface Ethernet1
#    ipv6 address 2001:db8:feed::1/96
# !
# interface Ethernet2
#    ip address 203.0.113.27/24
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
#    ipv6 address 2001:db8:feed::1/96
# !
# interface Ethernet2
#    ip address 203.0.113.27/24
# !
# interface Management1
#    ip address dhcp
#    dhcp client accept default-route

- name: Replace device configuration of specified L2 interfaces with provided configuration.
  arista.eos.eos_l3_interfaces:
    config:
      - name: Ethernet2
        ipv4:
          - address: 203.0.113.27/24
    state: replaced

# Task Output
# -----------
#
# before:
# - ipv6:
#   - address: 2001:db8:feed::1/96
#   name: Ethernet1
# - ipv4:
#   - address: 203.0.113.27/24
#   name: Ethernet2
# - ipv4:
#   - address: dhcp
#   name: Management1
# commands:
# - interface Ethernet2
# - ip address 203.0.113.28/24
# after:
# - ipv6:
#   - address: 2001:db8:feed::1/96
#   name: Ethernet1
# - ipv4:
#   - address: 203.0.113.28/24
#   name: Ethernet2
# - ipv4:
#   - address: dhcp
#   name: Management1

# After state:
# ------------
#
# test#show running-config | section interface
# interface Ethernet1
#    ipv6 address 2001:db8:feed::1/96
# !
# interface Ethernet2
#    ip address 203.0.113.28/24
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
#    ipv6 address 2001:db8:feed::1/96
# !
# interface Ethernet2
#    ip address 203.0.113.28/24
# !
# interface Management1
#    ip address dhcp
#    dhcp client accept default-route

- name: Delete L3 attributes of given interfaces.
  arista.eos.eos_l3_interfaces:
    config:
      - name: Ethernet1
      - name: Ethernet2
    state: deleted

# Task Output
# -----------
#
# before:
# - ipv6:
#   - address: 2001:db8:feed::1/96
#   name: Ethernet1
# - ipv4:
#   - address: 203.0.113.28/24
#   name: Ethernet2
# - ipv4:
#   - address: dhcp
#   name: Management1
# commands:
# - interface Ethernet1
# - no ipv6 address 2001:db8:feed::1/96
# - interface Ethernet2
# - no ip address
# after:
# - name: Ethernet1
# - name: Ethernet2
# - ipv4:
#   - address: dhcp
#   name: Management1

# After state:
# ------------
#
# test#show running-config | section interface
# interface Ethernet1
# !
# interface Ethernet2
# !
# interface Management1
#    ip address dhcp
#    dhcp client accept default-route

# Using Parsed

# File: parsed.cfg
# ----------------
#
# veos#show running-config | section interface
# interface Ethernet1
#    ip address 198.51.100.14/24
# !
# interface Ethernet2
#    ip address 203.0.113.27/24
# !

- name: Use parsed to convert native configs to structured data
  arista.eos.interfaces:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Module Execution Result:
# ------------------------
#
# parsed:
#  - name: Ethernet1
#    ipv4:
#      - address: 198.51.100.14/24
#  - name: Ethernet2
#    ipv4:
#      - address: 203.0.113.27/24

# Using rendered:

- name: Use Rendered to convert the structured data to native config
  arista.eos.eos_l3_interfaces:
    config:
      - name: Ethernet1
        ipv4:
          - address: 198.51.100.14/24
      - name: Ethernet2
        ipv4:
          - address: 203.0.113.27/24
    state: rendered

# Module Execution Result:
# ------------------------
#
# rendered:
# - interface Ethernet1
# - ip address 198.51.100.14/24
# - interface Ethernet2
# - ip address 203.0.113.27/24

# using gathered:

# Before state:
# -------------
#
# test#show running-config | section interface
# interface Ethernet1
#    ip address 198.51.100.14/24
# !
# interface Ethernet2
#    ip address 203.0.113.27/24
# !

- name: Gather l3 interfaces facts from the device
  arista.eos.l3_interfaces:
    state: gathered

# Module Execution Result:
# ------------------------
#
# gathered:
#  - name: Ethernet1
#    ipv4:
#      - address: 198.51.100.14/24
#  - name: Ethernet2
#    ipv4:
#      - address: 203.0.113.27/24
```

## [Return Values](eos_l3_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  **Returned:** when changed  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `["interface Ethernet1", "ip address 198.51.100.14/24", "ipv6 address 2001:db8:feed::1/96"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when *state* is `gathered`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when *state* is `parsed`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when *state* is `rendered`  **Sample:** `["interface Ethernet1", "ip address 198.51.100.14/24", "ipv6 address 2001:db8:feed::1/96"]` |

### Authors

- Nathaniel Case (@Qalthos)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/arista.eos)
