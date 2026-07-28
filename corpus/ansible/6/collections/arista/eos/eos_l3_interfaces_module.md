---
collection: ansible
version: "6"
title: "arista.eos.eos_l3_interfaces module – L3 interfaces resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/arista/eos/eos_l3_interfaces_module.html
fetched_at: 2026-07-27T16:42:56+00:00
---
# arista.eos.eos_l3_interfaces module – L3 interfaces resource module

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
> To use it in a playbook, specify: `arista.eos.eos_l3_interfaces`.

New in arista.eos 1.0.0

- [Synopsis](eos_l3_interfaces_module.md#synopsis)
- [Parameters](eos_l3_interfaces_module.md#parameters)
- [Notes](eos_l3_interfaces_module.md#notes)
- [Examples](eos_l3_interfaces_module.md#examples)
- [Return Values](eos_l3_interfaces_module.md#return-values)

## [Synopsis](eos_l3_interfaces_module.md#id1)

- This module provides declarative management of Layer 3 interfaces on Arista EOS devices.

## [Parameters](eos_l3_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of Layer 3 interface options |
| **ipv4**  list / elements=dictionary | List of IPv4 addresses to be set for the Layer 3 interface mentioned in *name* option. |
| **address**  string | IPv4 address to be set in the format <ipv4 address>/<mask> eg. 192.0.2.1/24, or `dhcp` to query DHCP for an IP address. |
| **secondary**  boolean | Whether or not this address is a secondary address.  Choices:   - `false` - `true` |
| **virtual**  boolean | Whether or not this address is a virtual address.  Choices:   - `false` - `true` |
| **ipv6**  list / elements=dictionary | List of IPv6 addresses to be set for the Layer 3 interface mentioned in *name* option. |
| **address**  string | IPv6 address to be set in the address format is <ipv6 address>/<mask> eg. 2001:db8:2201:1::1/64 or `auto-config` to use SLAAC to chose an address. |
| **name**  string / required | Full name of the interface, i.e. Ethernet1. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the EOS device by executing the command **show running-config | section ^interface**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"parsed"` - `"gathered"` - `"rendered"` |

## [Notes](eos_l3_interfaces_module.md#id3)

> **Note:**
>
> - Tested against Arista EOS 4.24.6F
> - This module works with connection `network_cli`. See the [EOS Platform Options](../network/user_guide/platform_eos.md). ‘eos_l2_interfaces/eos_interfaces’ should be used for preparing the interfaces , before applying L3 configurations using this module (eos_l3_interfaces).

## [Examples](eos_l3_interfaces_module.md#id4)

```yaml+jinja
# Using deleted

# Before state:
# -------------
#
# veos#show running-config | section interface
# interface Ethernet1
#    ip address 192.0.2.12/24
# !
# interface Ethernet2
#    ipv6 address 2001:db8::1/64
# !
# interface Management1
#    ip address dhcp
#    ipv6 address auto-config

- name: Delete L3 attributes of given interfaces.
  arista.eos.eos_l3_interfaces:
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

# Using merged

# Before state:
# -------------
#
# veos#show running-config | section interface
# interface Ethernet1
#    ip address 192.0.2.12/24
# !
# interface Ethernet2
#    ipv6 address 2001:db8::1/64
# !
# interface Management1
#    ip address dhcp
#    ipv6 address auto-config

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

# After state:
# ------------
#
# veos#show running-config | section interface
# interface Ethernet1
#    ip address 198.51.100.14/24
# !
# interface Ethernet2
#    ip address 203.0.113.27/24
#    ipv6 address 2001:db8::1/64
# !
# interface Management1
#    ip address dhcp
#    ipv6 address auto-config

# Using overridden

# Before state:
# -------------
#
# veos#show running-config | section interface
# interface Ethernet1
#    ip address 192.0.2.12/24
# !
# interface Ethernet2
#    ipv6 address 2001:db8::1/64
# !
# interface Management1
#    ip address dhcp
#    ipv6 address auto-config

- name: Override device configuration of all L2 interfaces on device with provided
    configuration.
  arista.eos.eos_l3_interfaces:
    config:
    - name: Ethernet1
      ipv6:
      - address: 2001:db8:feed::1/96
    - name: Management1
      ipv4:
      - address: dhcp
    ipv6: auto-config
    state: overridden

# After state:
# ------------
#
# veos#show running-config | section interface
# interface Ethernet1
#    ipv6 address 2001:db8:feed::1/96
# !
# interface Ethernet2
# !
# interface Management1
#    ip address dhcp
#    ipv6 address auto-config

# Using replaced

# Before state:
# -------------
#
# veos#show running-config | section interface
# interface Ethernet1
#    ip address 192.0.2.12/24
# !
# interface Ethernet2
#    ipv6 address 2001:db8::1/64
# !
# interface Management1
#    ip address dhcp
#    ipv6 address auto-config

- name: Replace device configuration of specified L2 interfaces with provided configuration.
  arista.eos.eos_l3_interfaces:
    config:
    - name: Ethernet2
      ipv4:
      - address: 203.0.113.27/24
    state: replaced

# After state:
# ------------
#
# veos#show running-config | section interface
# interface Ethernet1
#    ip address 192.0.2.12/24
# !
# interface Ethernet2
#    ip address 203.0.113.27/24
# !
# interface Management1
#    ip address dhcp
#    ipv6 address auto-config

# Using parsed:

# parsed.cfg
# ------------
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

# Output:

# parsed:
#    - name: Ethernet1
#      ipv4:
#        - address: 198.51.100.14/24
#    - name: Ethernet2
#      ipv4:
#        - address: 203.0.113.27/24

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

# Output
# ------------
#rendered:
#   - "interface Ethernet1"
#   - "ip address 198.51.100.14/24"
#   - "interface Ethernet2"
#   - "ip address 203.0.113.27/24"

# using gathered:

# Native COnfig:
# veos#show running-config | section interface
# interface Ethernet1
#    ip address 198.51.100.14/24
# !
# interface Ethernet2
#    ip address 203.0.113.27/24
# !

- name: Gather l3 interfaces facts from the device
  arista.eos.l3_interfaces:
    state: gathered

#    gathered:
#      - name: Ethernet1
#        ipv4:
#          - address: 198.51.100.14/24
#      - name: Ethernet2
#        ipv4:
#          - address: 203.0.113.27/24
```

## [Return Values](eos_l3_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  Returned: when changed  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["interface Ethernet2", "ip address 192.0.2.12/24"]` |

### Authors

- Nathaniel Case (@qalthos)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
[Repository (Sources)](https://github.com/ansible-collections/arista.eos)
