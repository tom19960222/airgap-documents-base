---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_bgp module – Configures BGP on Mellanox ONYX network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_bgp_module.html
fetched_at: 2026-07-27T17:55:23+00:00
---
# mellanox.onyx.onyx_bgp module – Configures BGP on Mellanox ONYX network devices

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
> To use it in a playbook, specify: `mellanox.onyx.onyx_bgp`.

- [Synopsis](onyx_bgp_module.md#synopsis)
- [Parameters](onyx_bgp_module.md#parameters)
- [Notes](onyx_bgp_module.md#notes)
- [Examples](onyx_bgp_module.md#examples)
- [Return Values](onyx_bgp_module.md#return-values)

## [Synopsis](onyx_bgp_module.md#id1)

- This module provides declarative management of BGP router and neighbors on Mellanox ONYX network devices.

## [Parameters](onyx_bgp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **as_number**  string / required | Local AS number. |
| **ecmp_bestpath**  boolean | Enables ECMP across AS paths.  Choices:   - `false` - `true` |
| **evpn**  boolean | Configure evpn peer-group.  Choices:   - `false` - `true` |
| **fast_external_fallover**  boolean | will configure fast_external_fallover when it is True.  Choices:   - `false` - `true` |
| **max_paths**  string | Maximum bgp paths. |
| **neighbors**  string | List of neighbors. Required if *state=present*. |
| **multihop**  string | multihop number. |
| **neighbor**  string / required | Neighbor IP address. |
| **remote_as**  string / required | Remote AS number. |
| **networks**  string | List of advertised networks. |
| **purge**  boolean | will remove all neighbors when it is True.  Choices:   - `false` ← (default) - `true` |
| **router_id**  string | Router IP address. |
| **state**  string | BGP state.  Choices:   - `"present"` ← (default) - `"absent"` |
| **vrf**  string | vrf name. |

## [Notes](onyx_bgp_module.md#id3)

> **Note:**
>
> - Tested on ONYX 3.6.4000

## [Examples](onyx_bgp_module.md#id4)

```yaml+jinja
- name: Configure bgp
  onyx_bgp:
    as_number: 320
    router_id: 10.3.3.3
    neighbors:
      - remote_as: 321
        neighbor: 10.3.3.4
      - remote_as: 322
        neighbor: 10.3.3.5
        multihop: 250
    purge: True
    state: present
    networks:
      - 172.16.1.0/24
    vrf: default
    evpn: yes
    fast_external_fallover: yes
    max_paths: 32
    ecmp_bestpath: yes
```

## [Return Values](onyx_bgp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device.  Returned: always  Sample: `["router bgp 320 vrf default", "exit", "router bgp 320 router-id 10.3.3.3 force", "router bgp 320 vrf default bgp fast-external-fallover", "router bgp 320 vrf default maximum-paths 32", "router bgp 320 vrf default bestpath as-path multipath-relax force", "router bgp 320 vrf default neighbor evpn peer-group", "router bgp 320 vrf default neighbor evpn send-community extended", "router bgp 320 vrf default address-family l2vpn-evpn neighbor evpn next-hop-unchanged", "router bgp 320 vrf default address-family l2vpn-evpn neighbor evpn activate", "router bgp 320 vrf default address-family l2vpn-evpn auto-create", "router bgp 320 vrf default neighbor 10.3.3.4 remote-as 321", "router bgp 320 vrf default neighbor 10.3.3.4 ebgp-multihop 250", "router bgp 320 vrf default neighbor 10.3.3.5 remote-as 322", "router bgp 320 vrf default network 172.16.1.0 /24"]` |

### Authors

- Samer Deeb (@samerd), Anas Badaha (@anasb)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
