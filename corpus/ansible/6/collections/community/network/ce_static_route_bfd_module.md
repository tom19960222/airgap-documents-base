---
collection: ansible
version: "6"
title: "community.network.ce_static_route_bfd module – Manages static route configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_static_route_bfd_module.html
fetched_at: 2026-07-27T17:17:54+00:00
---
# community.network.ce_static_route_bfd module – Manages static route configuration on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_static_route_bfd`.

New in community.network 0.2.0

- [Synopsis](ce_static_route_bfd_module.md#synopsis)
- [Parameters](ce_static_route_bfd_module.md#parameters)
- [Notes](ce_static_route_bfd_module.md#notes)
- [Examples](ce_static_route_bfd_module.md#examples)
- [Return Values](ce_static_route_bfd_module.md#return-values)

## [Synopsis](ce_static_route_bfd_module.md#id1)

- Manages the static routes on HUAWEI CloudEngine switches.

## [Parameters](ce_static_route_bfd_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aftype**  string / required | Destination ip address family type of static route.  Choices:   - `"v4"` - `"v6"` |
| **bfd_session_name**  string | bfd name (range 1-15). |
| **commands**  list / elements=string | Incoming command line is used to send sys,undo ip route-static default-bfd,commit. |
| **description**  string | Name of the route. Used with the name parameter on the CLI. |
| **destvrf**  string | VPN instance of next hop ip address. |
| **detect_multiplier**  integer | Configure the BFD multiplier (range 3-50). |
| **function_flag**  string / required | Used to distinguish between command line functions.  Choices:   - `"globalBFD"` - `"singleBFD"` - `"dynamicBFD"` - `"staticBFD"` |
| **mask**  string | Destination ip mask of static route. |
| **min_rx_interval**  integer | Set the minimum BFD receive interval (range 50-1000). |
| **min_tx_interval**  integer | Set the minimum BFD session sending interval (range 50-1000). |
| **next_hop**  string | Next hop address of static route. |
| **nhp_interface**  string | Next hop interface full name of static route. |
| **pref**  integer | Preference or administrative difference of route (range 1-255). |
| **prefix**  string / required | Destination ip address of static route. |
| **state**  string | Specify desired state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tag**  integer | Route tag value (numeric). |
| **vrf**  string | VPN instance of destination ip address. |

## [Notes](ce_static_route_bfd_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.
> - If no vrf is supplied, vrf is set to default.
> - If *state=absent*, the route configuration will be removed, regardless of the non-required parameters.

## [Examples](ce_static_route_bfd_module.md#id4)

```yaml+jinja
#ip route-static bfd interface-type interface-number nexthop-address [ local-address address ]
#[ min-rx-interval min-rx-interval | min-tx-interval min-tx-interval | detect-multiplier multiplier ]
- name: Config an ip route-static bfd 10GE1/0/1 3.3.3.3 min-rx-interval 50 min-tx-interval 50 detect-multiplier 5
  community.network.ce_static_route_bfd:
    function_flag: 'singleBFD'
    nhp_interface: 10GE1/0/1
    next_hop: 3.3.3.3
    min_tx_interval: 50
    min_rx_interval: 50
    detect_multiplier: 5
    aftype: v4
    state: present

#undo ip route-static bfd [ interface-type interface-number | vpn-instance vpn-instance-name ] nexthop-address
- name: Undo ip route-static bfd 10GE1/0/1 3.3.3.4
  community.network.ce_static_route_bfd:
    function_flag: 'singleBFD'
    nhp_interface: 10GE1/0/1
    next_hop: 3.3.3.4
    aftype: v4
    state: absent

#ip route-static default-bfd { min-rx-interval {min-rx-interval} | min-tx-interval {min-tx-interval} | detect-multiplier {multiplier}}
- name: Config an ip route-static default-bfd min-rx-interval 50 min-tx-interval 50 detect-multiplier 6
  community.network.ce_static_route_bfd:
    function_flag: 'globalBFD'
    min_tx_interval: 50
    min_rx_interval: 50
    detect_multiplier: 6
    aftype: v4
    state: present

- name: Undo ip route-static default-bfd
  community.network.ce_static_route_bfd:
    function_flag: 'globalBFD'
    aftype: v4
    state: absent
    commands: 'sys,undo ip route-static default-bfd,commit'

- name: Config an ipv4 static route 2.2.2.0/24 2.2.2.1 preference 1 tag 2 description test for staticBFD
  community.network.ce_static_route_bfd:
    function_flag: 'staticBFD'
    prefix: 2.2.2.2
    mask: 24
    next_hop: 2.2.2.1
    tag: 2
    description: test
    pref: 1
    aftype: v4
    bfd_session_name: btoa
    state: present
```

## [Return Values](ce_static_route_bfd_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of switchport after module execution  Returned: always  Sample: `{"bfd_session_name": "btoa", "description": "testing", "function_flag": "staticBFD", "mask": "24", "next_hop": "3.3.3.3", "pref": "100", "prefix": "192.168.20.0", "tag": "null"}` |
| **existing**  dictionary | k/v pairs of existing switchport  Returned: always  Sample: `{"bfd_session_name": "btoa", "description": "testing", "function_flag": "", "mask": "24", "next_hop": "", "pref": "101", "prefix": "192.168.20.0", "tag": "null"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: always  Sample: `{"bfd_session_name": "btoa", "description": "testing", "function_flag": "staticBFD", "mask": "24", "next_hop": "3.3.3.3", "pref": "100", "prefix": "192.168.20.642", "vrf": "_public_"}` |
| **updates**  list / elements=string | command list sent to the device  Returned: always  Sample: `["ip route-static 192.168.20.0 255.255.255.0 3.3.3.3 preference 100 description testing"]` |

### Authors

- xuxiaowei0512 (@CloudEngine-Ansible)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
