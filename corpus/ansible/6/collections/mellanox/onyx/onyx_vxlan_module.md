---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_vxlan module – Configures Vxlan"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_vxlan_module.html
fetched_at: 2026-07-27T17:55:45+00:00
---
# mellanox.onyx.onyx_vxlan module – Configures Vxlan

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
> To use it in a playbook, specify: `mellanox.onyx.onyx_vxlan`.

- [Synopsis](onyx_vxlan_module.md#synopsis)
- [Parameters](onyx_vxlan_module.md#parameters)
- [Notes](onyx_vxlan_module.md#notes)
- [Examples](onyx_vxlan_module.md#examples)
- [Return Values](onyx_vxlan_module.md#return-values)

## [Synopsis](onyx_vxlan_module.md#id1)

- This module provides declarative management of Vxlan configuration on Mellanox ONYX network devices.

## [Parameters](onyx_vxlan_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **arp_suppression**  boolean | A flag telling if to configure arp suppression.  Choices:   - `false` ← (default) - `true` |
| **bgp**  boolean | configure bgp on nve interface.  Choices:   - `false` - `true` ← (default) |
| **loopback_id**  string | loopback interface ID. |
| **mlag_tunnel_ip**  string | vxlan Mlag tunnel IP |
| **nve_id**  string / required | nve interface ID. |
| **vni_vlan_list**  string | Each item in the list has two attributes vlan_id, vni_id. |

## [Notes](onyx_vxlan_module.md#id3)

> **Note:**
>
> - Tested on ONYX evpn_dev.031.
> - nve protocol must be enabled.

## [Examples](onyx_vxlan_module.md#id4)

```yaml+jinja
- name: Configure Vxlan
  onyx_vxlan:
    nve_id: 1
    loopback_id: 1
    bgp: yes
    mlag-tunnel-ip: 100.0.0.1
    vni_vlan_list:
      - vlan_id: 10
        vni_id: 10010
      - vlan_id: 6
        vni_id: 10060
    arp_suppression: yes
```

## [Return Values](onyx_vxlan_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device.  Returned: always  Sample: `["interface nve 1", "interface nve 1 vxlan source interface loopback 1", "interface nve 1 nve controller bgp", "interface nve 1 vxlan mlag-tunnel-ip 100.0.0.1", "interface nve 1 nve vni 10010 vlan 10", "interface nve 1 nve vni 10060 vlan 6", "interface nve 1 nve neigh-suppression", "interface vlan 6", "interface vlan 10"]` |

### Authors

- Anas Badaha (@anasb)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
