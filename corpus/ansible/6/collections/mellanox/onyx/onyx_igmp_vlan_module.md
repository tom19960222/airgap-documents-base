---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_igmp_vlan module – Configures IGMP Vlan parameters"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_igmp_vlan_module.html
fetched_at: 2026-07-27T17:55:28+00:00
---
# mellanox.onyx.onyx_igmp_vlan module – Configures IGMP Vlan parameters

> **Note:**
>
> This module is part of the [mellanox.onyx collection](https://galaxy.ansible.com/mellanox/onyx) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install mellanox.onyx`.
>
> To use it in a playbook, specify: `mellanox.onyx.onyx_igmp_vlan`.

- [Synopsis](onyx_igmp_vlan_module.md#synopsis)
- [Parameters](onyx_igmp_vlan_module.md#parameters)
- [Notes](onyx_igmp_vlan_module.md#notes)
- [Examples](onyx_igmp_vlan_module.md#examples)
- [Return Values](onyx_igmp_vlan_module.md#return-values)

## [Synopsis](onyx_igmp_vlan_module.md#id1)

- This module provides declarative management of IGMP vlan configuration on Mellanox ONYX network devices.

## [Parameters](onyx_igmp_vlan_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **mrouter**  string | Configure ip igmp snooping mrouter port on vlan |
| **name**  string / required | Configure mrouter interface |
| **state**  string | Enable IGMP snooping mrouter on vlan interface.  Choices:   - `"enabled"` ← (default) - `"disabled"` |
| **querier**  string | Configure the IGMP querier parameters |
| **address**  string | Update IP address for the querier |
| **interval**  string | Update time interval between querier queries, range 60-600 |
| **state**  string | Enable IGMP snooping querier on vlan in the switch.  Choices:   - `"enabled"` ← (default) - `"disabled"` |
| **state**  string | IGMP state.  Choices:   - `"enabled"` ← (default) - `"disabled"` |
| **static_groups**  string | List of IGMP static groups. |
| **multicast_ip_address**  string / required | Configure static IP multicast group, range 224.0.1.0-239.255.255.25. |
| **name**  string | interface name to configure static groups on it. |
| **sources**  string | List of IP sources to be configured |
| **version**  string | IGMP snooping operation version on this vlan  Choices:   - `"V2"` - `"V3"` |
| **vlan_id**  string / required | VLAN ID, vlan should exist. |

## [Notes](onyx_igmp_vlan_module.md#id3)

> **Note:**
>
> - Tested on ONYX 3.7.0932-01

## [Examples](onyx_igmp_vlan_module.md#id4)

```yaml+jinja
- name: Configure igmp vlan
  onyx_igmp_vlan:
    state: enabled
    vlan_id: 10
    version:
      V2
    querier:
      state: enabled
      interval: 70
      address: 10.11.121.13
    mrouter:
      state: disabled
      name: Eth1/2
    static_groups:
      - multicast_ip_address: 224.5.5.8
        name: Eth1/1
        sources:
          - 1.1.1.1
          - 1.1.1.2
```

## [Return Values](onyx_igmp_vlan_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device.  Returned: always  Sample: `["vlan 10 ip igmp snooping", "vlan 10 ip igmp snooping static-group 224.5.5.5 interface ethernet 1/1"]` |

### Authors

- Anas Badaha (@anasbadaha)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
