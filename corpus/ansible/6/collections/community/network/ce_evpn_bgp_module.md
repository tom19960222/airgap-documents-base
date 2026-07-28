---
collection: ansible
version: "6"
title: "community.network.ce_evpn_bgp module – Manages BGP EVPN configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_evpn_bgp_module.html
fetched_at: 2026-07-27T17:17:24+00:00
---
# community.network.ce_evpn_bgp module – Manages BGP EVPN configuration on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_evpn_bgp`.

- [Synopsis](ce_evpn_bgp_module.md#synopsis)
- [Parameters](ce_evpn_bgp_module.md#parameters)
- [Notes](ce_evpn_bgp_module.md#notes)
- [Examples](ce_evpn_bgp_module.md#examples)
- [Return Values](ce_evpn_bgp_module.md#return-values)

## [Synopsis](ce_evpn_bgp_module.md#id1)

- This module offers the ability to configure a BGP EVPN peer relationship on HUAWEI CloudEngine switches.

## [Parameters](ce_evpn_bgp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **advertise_l2vpn_evpn**  string | Enable or disable a device to advertise IP routes imported to a VPN instance to its EVPN instance.  Choices:   - `"enable"` - `"disable"` |
| **advertise_router_type**  string | Configures a device to advertise routes to its BGP EVPN peers.  Choices:   - `"arp"` - `"irb"` |
| **as_number**  string | Specifies integral AS number. The value is an integer ranging from 1 to 4294967295. |
| **bgp_instance**  string / required | Name of a BGP instance. The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |
| **peer_address**  string | Specifies the IPv4 address of a BGP EVPN peer. The value is in dotted decimal notation. |
| **peer_enable**  string | Enable or disable a BGP device to exchange routes with a specified peer or peer group in the address family view.  Choices:   - `"true"` - `"false"` |
| **peer_group_name**  string | Specify the name of a peer group that BGP peers need to join. The value is a string of 1 to 47 case-sensitive characters, spaces not supported. |
| **state**  string | Manage the state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **vpn_name**  string | Associates a specified VPN instance with the IPv4 address family. The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |

## [Notes](ce_evpn_bgp_module.md#id3)

> **Note:**
>
> - Recommended connection is `network_cli`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_evpn_bgp_module.md#id4)

```yaml+jinja
- name: Evpn bgp module test
  hosts: cloudengine
  connection: local
  gather_facts: no
  vars:
    cli:
      host: "{{ inventory_hostname }}"
      port: "{{ ansible_ssh_port }}"
      username: "{{ username }}"
      password: "{{ password }}"
      transport: cli

  tasks:

  - name: Enable peer address.
    community.network.ce_evpn_bgp:
      bgp_instance: 100
      peer_address: 1.1.1.1
      as_number: 100
      peer_enable: true
      provider: "{{ cli }}"

  - name: Enable peer group arp.
    community.network.ce_evpn_bgp:
      bgp_instance: 100
      peer_group_name: aaa
      advertise_router_type: arp
      provider: "{{ cli }}"

  - name: Enable advertise l2vpn evpn.
    community.network.ce_evpn_bgp:
      bgp_instance: 100
      vpn_name: aaa
      advertise_l2vpn_evpn: enable
      provider: "{{ cli }}"
```

## [Return Values](ce_evpn_bgp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of configuration after module execution  Returned: verbose mode  Sample: `{"advertise_l2vpn_evpn": "enable", "bgp_instance": "100", "vpn_name": "aaa"}` |
| **existing**  dictionary | k/v pairs of existing rollback  Returned: always  Sample: `{"bgp_instance": "100", "peer_group_advertise_type": []}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: always  Sample: `{"advertise_router_type": "arp", "bgp_instance": "100", "peer_group_name": "aaa", "state": "present"}` |
| **updates**  list / elements=string | command sent to the device  Returned: always  Sample: `["peer 1.1.1.1 enable", "peer aaa advertise arp"]` |

### Authors

- Li Yanfeng (@QijunPan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
