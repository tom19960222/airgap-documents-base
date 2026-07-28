---
collection: ansible
version: "6"
title: "community.network.cnos_l3_interface module – Manage Layer-3 interfaces on Lenovo CNOS network devices."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/cnos_l3_interface_module.html
fetched_at: 2026-07-27T17:18:11+00:00
---
# community.network.cnos_l3_interface module – Manage Layer-3 interfaces on Lenovo CNOS network devices.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.cnos_l3_interface`.

- [Synopsis](cnos_l3_interface_module.md#synopsis)
- [Parameters](cnos_l3_interface_module.md#parameters)
- [Notes](cnos_l3_interface_module.md#notes)
- [Examples](cnos_l3_interface_module.md#examples)
- [Return Values](cnos_l3_interface_module.md#return-values)

## [Synopsis](cnos_l3_interface_module.md#id1)

- This module provides declarative management of Layer-3 interfaces on CNOS network devices.

## [Parameters](cnos_l3_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate**  string | List of Layer-3 interfaces definitions. Each of the entry in aggregate list should define name of interface `name` and a optional `ipv4` or `ipv6` address. |
| **ipv4**  string | IPv4 address to be set for the Layer-3 interface mentioned in *name* option. The address format is <ipv4 address>/<mask>, the mask is number in range 0-32 eg. 10.241.107.1/24 |
| **ipv6**  string | IPv6 address to be set for the Layer-3 interface mentioned in *name* option. The address format is <ipv6 address>/<mask>, the mask is number in range 0-128 eg. fd5d:12c9:2201:1::1/64 |
| **name**  string | Name of the Layer-3 interface to be configured eg. Ethernet1/2 |
| **state**  string | State of the Layer-3 interface configuration. It indicates if the configuration should be present or absent on remote device.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](cnos_l3_interface_module.md#id3)

> **Note:**
>
> - Tested against CNOS 10.8.1

## [Examples](cnos_l3_interface_module.md#id4)

```yaml+jinja
- name: Remove Ethernet1/33 IPv4 and IPv6 address
  community.network.cnos_l3_interface:
    name: Ethernet1/33
    state: absent

- name: Set Ethernet1/33 IPv4 address
  community.network.cnos_l3_interface:
    name: Ethernet1/33
    ipv4: 10.241.107.1/24

- name: Set Ethernet1/33 IPv6 address
  community.network.cnos_l3_interface:
    name: Ethernet1/33
    ipv6: "fd5d:12c9:2201:1::1/64"

- name: Set Ethernet1/33 in dhcp
  community.network.cnos_l3_interface:
    name: Ethernet1/33
    ipv4: dhcp
    ipv6: dhcp

- name: Set interface Vlan1 (SVI) IPv4 address
  community.network.cnos_l3_interface:
    name: Vlan1
    ipv4: 192.168.0.5/24

- name: Set IP addresses on aggregate
  community.network.cnos_l3_interface:
    aggregate:
      - { name: Ethernet1/33, ipv4: 10.241.107.1/24 }
      - { name: Ethernet1/44, ipv4: 10.240.106.1/24,
          ipv6: "fd5d:12c9:2201:1::1/64" }

- name: Remove IP addresses on aggregate
  community.network.cnos_l3_interface:
    aggregate:
      - { name: Ethernet1/33, ipv4: 10.241.107.1/24 }
      - { name: Ethernet1/44, ipv4: 10.240.106.1/24,
          ipv6: "fd5d:12c9:2201:1::1/64" }
    state: absent
```

## [Return Values](cnos_l3_interface_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always, except for the platforms that use Netconf transport to manage the device.  Sample: `["interface Ethernet1/33", "ip address 10.241.107.1 255.255.255.0", "ipv6 address fd5d:12c9:2201:1::1/64"]` |

### Authors

- Anil Kumar Muraleedharan (@amuraleedhar)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
