---
collection: ansible
version: "8"
title: "community.network.slxos_l3_interface module – Manage L3 interfaces on Extreme Networks SLX-OS network devices."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/slxos_l3_interface_module.html
fetched_at: 2026-07-28T01:57:50+00:00
---
# community.network.slxos_l3_interface module – Manage L3 interfaces on Extreme Networks SLX-OS network devices.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.slxos_l3_interface`.

- [Synopsis](slxos_l3_interface_module.md#synopsis)
- [Parameters](slxos_l3_interface_module.md#parameters)
- [Notes](slxos_l3_interface_module.md#notes)
- [Examples](slxos_l3_interface_module.md#examples)
- [Return Values](slxos_l3_interface_module.md#return-values)

## [Synopsis](slxos_l3_interface_module.md#id1)

- This module provides declarative management of L3 interfaces on slxos network devices.

Aliases: network.slxos.slxos_l3_interface

## [Parameters](slxos_l3_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate**  string | List of L3 interfaces definitions. Each of the entry in aggregate list should define name of interface `name` and a optional `ipv4` or `ipv6` address. |
| **ipv4**  string | IPv4 address to be set for the L3 interface mentioned in *name* option. The address format is <ipv4 address>/<mask>, the mask is number in range 0-32 eg. 192.168.0.1/24 |
| **ipv6**  string | IPv6 address to be set for the L3 interface mentioned in *name* option. The address format is <ipv6 address>/<mask>, the mask is number in range 0-128 eg. fd5d:12c9:2201:1::1/64 |
| **name**  string | Name of the L3 interface to be configured eg. Ethernet 0/2 |
| **state**  string | State of the L3 interface configuration. It indicates if the configuration should be present or absent on remote device.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](slxos_l3_interface_module.md#id3)

> **Note:**
>
> - Tested against slxos 15.2

## [Examples](slxos_l3_interface_module.md#id4)

```yaml+jinja
- name: Remove Ethernet 0/3 IPv4 and IPv6 address
  community.network.slxos_l3_interface:
    name: Ethernet 0/3
    state: absent

- name: Set Ethernet 0/3 IPv4 address
  community.network.slxos_l3_interface:
    name: Ethernet 0/3
    ipv4: 192.168.0.1/24

- name: Set Ethernet 0/3 IPv6 address
  community.network.slxos_l3_interface:
    name: Ethernet 0/3
    ipv6: "fd5d:12c9:2201:1::1/64"

- name: Set IP addresses on aggregate
  community.network.slxos_l3_interface:
    aggregate:
      - { name: Ethernet 0/3, ipv4: 192.168.2.10/24 }
      - { name: Ethernet 0/3, ipv4: 192.168.3.10/24, ipv6: "fd5d:12c9:2201:1::1/64" }

- name: Remove IP addresses on aggregate
  community.network.slxos_l3_interface:
    aggregate:
      - { name: Ethernet 0/3, ipv4: 192.168.2.10/24 }
      - { name: Ethernet 0/3, ipv4: 192.168.3.10/24, ipv6: "fd5d:12c9:2201:1::1/64" }
    state: absent
```

## [Return Values](slxos_l3_interface_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  **Returned:** always, except for the platforms that use Netconf transport to manage the device.  **Sample:** `["interface Ethernet 0/2", "ip address 192.168.0.1/24", "ipv6 address fd5d:12c9:2201:1::1/64"]` |

### Authors

- Matthew Stone (@bigmstone)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
