---
collection: ansible
version: "6"
title: "dellemc.enterprise_sonic.sonic_l3_interfaces module – Configure the IPv4 and IPv6 parameters on Interfaces such as, Eth, LAG, VLAN, and loopback"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/enterprise_sonic/sonic_l3_interfaces_module.html
fetched_at: 2026-07-27T17:24:55+00:00
---
# dellemc.enterprise_sonic.sonic_l3_interfaces module – Configure the IPv4 and IPv6 parameters on Interfaces such as, Eth, LAG, VLAN, and loopback

> **Note:**
>
> This module is part of the [dellemc.enterprise_sonic collection](https://galaxy.ansible.com/dellemc/enterprise_sonic) (version 1.1.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.enterprise_sonic`.
>
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_l3_interfaces`.

New in dellemc.enterprise_sonic 1.0.0

- [Synopsis](sonic_l3_interfaces_module.md#synopsis)
- [Parameters](sonic_l3_interfaces_module.md#parameters)
- [Notes](sonic_l3_interfaces_module.md#notes)
- [Examples](sonic_l3_interfaces_module.md#examples)
- [Return Values](sonic_l3_interfaces_module.md#return-values)

## [Synopsis](sonic_l3_interfaces_module.md#id1)

- Configures Layer 3 interface settings on devices running Enterprise SONiC Distribution by Dell Technologies. This module provides configuration management of IPv4 and IPv6 parameters on Ethernet interfaces of devices running Enterprise SONiC.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](sonic_l3_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of l3_interfaces configurations. |
| **ipv4**  dictionary | ipv4 configurations to be set for the Layer 3 interface mentioned in name option. |
| **addresses**  list / elements=dictionary | List of IPv4 addresses to be set. |
| **address**  string | IPv4 address to be set in the format <ipv4 address>/<mask> for example, 192.0.2.1/24. |
| **secondary**  boolean | secondary flag of the ip address.  Choices:   - `false` ← (default) - `true` |
| **anycast_addresses**  list / elements=string | List of IPv4 addresses to be set for anycast. |
| **ipv6**  dictionary | ipv6 configurations to be set for the Layer 3 interface mentioned in name option. |
| **addresses**  list / elements=dictionary | List of IPv6 addresses to be set. |
| **address**  string | IPv6 address to be set in the address format is <ipv6 address>/<mask> for example, 2001:db8:2201:1::1/64. |
| **enabled**  boolean | enabled flag of the ipv6.  Choices:   - `false` - `true` |
| **name**  string / required | Full name of the interface, for example, Eth1/3. |
| **state**  string | The state that the configuration should be left in.  Choices:   - `"merged"` ← (default) - `"deleted"` |

## [Notes](sonic_l3_interfaces_module.md#id3)

> **Note:**
>
> - Tested against Enterprise SONiC Distribution by Dell Technologies.
> - Supports `check_mode`.

## [Examples](sonic_l3_interfaces_module.md#id4)

```yaml+jinja
# Using deleted
#
# Before state:
# -------------
#
#rno-dctor-1ar01c01sw02# show running-configuration interface
#!
#interface Ethernet20
# mtu 9100
# speed 100000
# shutdown
# ip address 83.1.1.1/16
# ip address 84.1.1.1/16 secondary
# ipv6 address 83::1/16
# ipv6 address 84::1/16
# ipv6 enable
#!
#interface Ethernet24
# mtu 9100
# speed 100000
# shutdown
# ip address 91.1.1.1/16
# ip address 92.1.1.1/16 secondary
# ipv6 address 90::1/16
# ipv6 address 91::1/16
# ipv6 address 92::1/16
# ipv6 address 93::1/16
#!
#interface Vlan501
# ip anycast-address 11.12.13.14/12
# ip anycast-address 1.2.3.4/22
#!
#
#
- name: delete one l3 interface.
  dellemc.enterprise_sonic.sonic_l3_interfaces:
    config:
      - name: Ethernet20
        ipv4:
          addresses:
            - address: 83.1.1.1/16
            - address: 84.1.1.1/16
      - name: Ethernet24
        ipv6:
          enabled: true
          addresses:
            - address: 91::1/16
      - name: Vlan501
        ipv4:
          anycast_addresses:
            - 11.12.13.14/12
    state: deleted

# After state:
# ------------
#
#rno-dctor-1ar01c01sw02# show running-configuration interface
#!
#interface Ethernet20
# mtu 9100
# speed 100000
# shutdown
# ipv6 address 83::1/16
# ipv6 address 84::1/16
# ipv6 enable
#!
#interface Ethernet24
# mtu 9100
# speed 100000
# shutdown
# ip address 91.1.1.1/16
# ip address 92.1.1.1/16 secondary
# ipv6 address 90::1/16
# ipv6 address 92::1/16
# ipv6 address 93::1/16
#!
#interface Vlan501
# ip anycast-address 1.2.3.4/22
#!
#
# Using deleted
#
# Before state:
# -------------
#
#rno-dctor-1ar01c01sw02# show running-configuration interface
#!
#interface Ethernet20
# mtu 9100
# speed 100000
# shutdown
# ip address 83.1.1.1/16
# ip address 84.1.1.1/16 secondary
# ipv6 address 83::1/16
# ipv6 address 84::1/16
# ipv6 enable
#!
#interface Ethernet24
# mtu 9100
# speed 100000
# shutdown
# ip address 91.1.1.1/16
# ipv6 address 90::1/16
# ipv6 address 91::1/16
# ipv6 address 92::1/16
# ipv6 address 93::1/16
#!
#interface Vlan501
# ip anycast-address 11.12.13.14/12
# ip anycast-address 1.2.3.4/22
#!
#
#
- name: delete all l3 interface
  dellemc.enterprise_sonic.sonic_l3_interfaces:
    config:
    state: deleted
#
# After state:
# ------------
#
#rno-dctor-1ar01c01sw02# show running-configuration interface
#!
#interface Ethernet20
# mtu 9100
# speed 100000
# shutdown
#!
#interface Ethernet24
# mtu 9100
# speed 100000
# shutdown
#!
#interface Vlan501
#!
#
# Using merged
#
# Before state:
# -------------
#
#rno-dctor-1ar01c01sw02# show running-configuration interface
#!
#interface Ethernet20
# mtu 9100
# speed 100000
# shutdown
#!
#interface Ethernet24
# mtu 9100
# speed 100000
# shutdown
#!
#interface Vlan501
# ip anycast-address 1.2.3.4/22
#!
#
- name: Add l3 interface configurations
  dellemc.enterprise_sonic.sonic_l3_interfaces:
    config:
      - name: Ethernet20
        ipv4:
          addresses:
            - address: 83.1.1.1/16
            - address: 84.1.1.1/16
              secondary: True
        ipv6:
          enabled: true
          addresses:
            - address: 83::1/16
            - address: 84::1/16
              secondary: True
      - name: Ethernet24
        ipv4:
          addresses:
            - address: 91.1.1.1/16
        ipv6:
          addresses:
            - address: 90::1/16
            - address: 91::1/16
            - address: 92::1/16
            - address: 93::1/16
      - name: Vlan501
        ipv4:
          anycast_addresses:
            - 11.12.13.14/12
    state: merged
#
# After state:
# ------------
#
#rno-dctor-1ar01c01sw02# show running-configuration interface
#!
#interface Ethernet20
# mtu 9100
# speed 100000
# shutdown
# ip address 83.1.1.1/16
# ip address 84.1.1.1/16 secondary
# ipv6 address 83::1/16
# ipv6 address 84::1/16
# ipv6 enable
#!
#interface Ethernet24
# mtu 9100
# speed 100000
# shutdown
# ip address 91.1.1.1/16
# ipv6 address 90::1/16
# ipv6 address 91::1/16
# ipv6 address 92::1/16
# ipv6 address 93::1/16
#!
#interface Vlan501
# ip anycast-address 1.2.3.4/22
# ip anycast-address 11.12.13.14/12
#!
#
#
```

## [Return Values](sonic_l3_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  Returned: when changed  Sample: `["The configuration returned is always in the same format of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  Returned: always  Sample: `["The configuration returned is always in the same format of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["command 1", "command 2", "command 3"]` |

### Authors

- Kumaraguru Narayanan (@nkumaraguru)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
[Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
