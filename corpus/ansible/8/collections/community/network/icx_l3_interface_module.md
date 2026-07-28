---
collection: ansible
version: "8"
title: "community.network.icx_l3_interface module – Manage Layer-3 interfaces on Ruckus ICX 7000 series switches"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/icx_l3_interface_module.html
fetched_at: 2026-07-28T01:56:49+00:00
---
# community.network.icx_l3_interface module – Manage Layer-3 interfaces on Ruckus ICX 7000 series switches

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
> To use it in a playbook, specify: `community.network.icx_l3_interface`.

- [Synopsis](icx_l3_interface_module.md#synopsis)
- [Parameters](icx_l3_interface_module.md#parameters)
- [Notes](icx_l3_interface_module.md#notes)
- [Examples](icx_l3_interface_module.md#examples)
- [Return Values](icx_l3_interface_module.md#return-values)

## [Synopsis](icx_l3_interface_module.md#id1)

- This module provides declarative management of Layer-3 interfaces on ICX network devices.

Aliases: network.icx.icx_l3_interface

## [Parameters](icx_l3_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate**  list / elements=dictionary | List of Layer-3 interfaces definitions. Each of the entry in aggregate list should define name of interface `name` and a optional `ipv4` or `ipv6` address. |
| **check_running_config**  boolean | Check running configuration. This can be set as environment variable. Module will use environment variable value(default:True), unless it is overridden, by specifying it as module parameter.  **Choices:**   - `false` - `true` |
| **ipv4**  string | IPv4 address to be set for the Layer-3 interface mentioned in *name* option. The address format is <ipv4 address>/<mask>, the mask is number in range 0-32 eg. 192.168.0.1/24 |
| **ipv6**  string | IPv6 address to be set for the Layer-3 interface mentioned in *name* option. The address format is <ipv6 address>/<mask>, the mask is number in range 0-128 eg. fd5d:12c9:2201:1::1/64. |
| **mode**  string | Specifies if ipv4 address should be dynamic/advertise to ospf/not advertise to ospf. This should be specified only if ipv4 address is configured and if it is not secondary IP address.  **Choices:**   - `"dynamic"` - `"ospf-ignore"` - `"ospf-passive"` |
| **name**  string | Name of the Layer-3 interface to be configured eg. GigabitEthernet0/2, ve 10, ethernet 1/1/1 |
| **replace**  string | Replaces the configured primary IP address on the interface.  **Choices:**   - `"yes"` - `"no"` |
| **secondary**  string | Specifies that the configured address is a secondary IP address. If this keyword is omitted, the configured address is the primary IP address.  **Choices:**   - `"yes"` - `"no"` |
| **state**  string | State of the Layer-3 interface configuration. It indicates if the configuration should be present or absent on remote device.  **Choices:**   - `"present"` - `"absent"` |
| **check_running_config**  boolean | Check running configuration. This can be set as environment variable. Module will use environment variable value(default:True), unless it is overridden, by specifying it as module parameter.  **Choices:**   - `false` - `true` ← (default) |
| **ipv4**  string | IPv4 address to be set for the Layer-3 interface mentioned in *name* option. The address format is <ipv4 address>/<mask>, the mask is number in range 0-32 eg. 192.168.0.1/24 |
| **ipv6**  string | IPv6 address to be set for the Layer-3 interface mentioned in *name* option. The address format is <ipv6 address>/<mask>, the mask is number in range 0-128 eg. fd5d:12c9:2201:1::1/64. |
| **mode**  string | Specifies if ipv4 address should be dynamic/advertise to ospf/not advertise to ospf. This should be specified only if ipv4 address is configured and if it is not secondary IP address.  **Choices:**   - `"dynamic"` - `"ospf-ignore"` - `"ospf-passive"` |
| **name**  string | Name of the Layer-3 interface to be configured eg. GigabitEthernet0/2, ve 10, ethernet 1/1/1 |
| **replace**  string | Replaces the configured primary IP address on the interface.  **Choices:**   - `"yes"` - `"no"` |
| **secondary**  string | Specifies that the configured address is a secondary IP address. If this keyword is omitted, the configured address is the primary IP address.  **Choices:**   - `"yes"` - `"no"` |
| **state**  string | State of the Layer-3 interface configuration. It indicates if the configuration should be present or absent on remote device.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](icx_l3_interface_module.md#id3)

> **Note:**
>
> - Tested against ICX 10.1.
> - For information on using ICX platform, see [the ICX OS Platform Options guide](user_guide/platform_icx.md).

## [Examples](icx_l3_interface_module.md#id4)

```yaml+jinja
- name: Remove ethernet 1/1/1 IPv4 and IPv6 address
  community.network.icx_l3_interface:
    name: ethernet 1/1/1
    ipv4: 192.168.0.1/24
    ipv6: "fd5d:12c9:2201:1::1/64"
    state: absent

- name: Replace ethernet 1/1/1 primary IPv4 address
  community.network.icx_l3_interface:
    name: ethernet 1/1/1
    ipv4: 192.168.0.1/24
    replace: true
    state: absent

- name: Replace ethernet 1/1/1 dynamic IPv4 address
  community.network.icx_l3_interface:
    name: ethernet 1/1/1
    ipv4: 192.168.0.1/24
    mode: dynamic
    state: absent

- name: Set ethernet 1/1/1 secondary IPv4 address
  community.network.icx_l3_interface:
    name: ethernet 1/1/1
    ipv4: 192.168.0.1/24
    secondary: true
    state: absent

- name: Set ethernet 1/1/1 IPv4 address
  community.network.icx_l3_interface:
    name: ethernet 1/1/1
    ipv4: 192.168.0.1/24

- name: Set ethernet 1/1/1 IPv6 address
  community.network.icx_l3_interface:
    name: ethernet 1/1/1
    ipv6: "fd5d:12c9:2201:1::1/64"

- name: Set IP addresses on aggregate
  community.network.icx_l3_interface:
    aggregate:
      - { name: GigabitEthernet0/3, ipv4: 192.168.2.10/24 }
      - { name: GigabitEthernet0/3, ipv4: 192.168.3.10/24, ipv6: "fd5d:12c9:2201:1::1/64" }

- name: Remove IP addresses on aggregate
  community.network.icx_l3_interface:
    aggregate:
      - { name: GigabitEthernet0/3, ipv4: 192.168.2.10/24 }
      - { name: GigabitEthernet0/3, ipv4: 192.168.3.10/24, ipv6: "fd5d:12c9:2201:1::1/64" }
    state: absent

- name: Set the ipv4 and ipv6 of a virtual ethernet(ve)
  community.network.icx_l3_interface:
    name: ve 100
    ipv4: 192.168.0.1
    ipv6: "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
```

## [Return Values](icx_l3_interface_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  **Returned:** always, except for the platforms that use Netconf transport to manage the device.  **Sample:** `["interface ethernet 1/1/1", "ip address 192.168.0.1 255.255.255.0", "ipv6 address fd5d:12c9:2201:1::1/64"]` |

### Authors

- Ruckus Wireless (@Commscope)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
