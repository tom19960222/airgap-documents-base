---
collection: ansible
version: "6"
title: "community.network.ce_vxlan_arp module – Manages ARP attributes of VXLAN on HUAWEI CloudEngine devices."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_vxlan_arp_module.html
fetched_at: 2026-07-27T17:17:59+00:00
---
# community.network.ce_vxlan_arp module – Manages ARP attributes of VXLAN on HUAWEI CloudEngine devices.

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
> To use it in a playbook, specify: `community.network.ce_vxlan_arp`.

- [Synopsis](ce_vxlan_arp_module.md#synopsis)
- [Parameters](ce_vxlan_arp_module.md#parameters)
- [Notes](ce_vxlan_arp_module.md#notes)
- [Examples](ce_vxlan_arp_module.md#examples)
- [Return Values](ce_vxlan_arp_module.md#return-values)

## [Synopsis](ce_vxlan_arp_module.md#id1)

- Manages ARP attributes of VXLAN on HUAWEI CloudEngine devices.

## [Parameters](ce_vxlan_arp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **arp_collect_host**  string | Enables EVN BGP or BGP EVPN to collect host information.  Choices:   - `"enable"` - `"disable"` |
| **arp_suppress**  string | Enables ARP broadcast suppression in a BD.  Choices:   - `"enable"` - `"disable"` |
| **bridge_domain_id**  string | Specifies a BD(bridge domain) ID. The value is an integer ranging from 1 to 16777215. |
| **evn_bgp**  string | Enables EVN BGP.  Choices:   - `"enable"` - `"disable"` |
| **evn_peer_ip**  string | Specifies the IP address of an EVN BGP peer. The value is in dotted decimal notation. |
| **evn_reflect_client**  string | Configures the local device as the route reflector (RR) and its peer as the client.  Choices:   - `"enable"` - `"disable"` |
| **evn_server**  string | Configures the local device as the router reflector (RR) on the EVN network.  Choices:   - `"enable"` - `"disable"` |
| **evn_source_ip**  string | Specifies the source address of an EVN BGP peer. The value is in dotted decimal notation. |
| **host_collect_protocol**  string | Enables EVN BGP or BGP EVPN to advertise host information.  Choices:   - `"bgp"` - `"none"` |
| **state**  string | Determines whether the config should be present or not on the device.  Choices:   - `"present"` ← (default) - `"absent"` |
| **vbdif_name**  string | Full name of VBDIF interface, i.e. Vbdif100. |

## [Notes](ce_vxlan_arp_module.md#id3)

> **Note:**
>
> - Recommended connection is `network_cli`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_vxlan_arp_module.md#id4)

```yaml+jinja
- name: Vxlan arp module test
  hosts: ce128
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

  - name: Configure EVN BGP on Layer 2 and Layer 3 VXLAN gateways to establish EVN BGP peer relationships.
    community.network.ce_vxlan_arp:
      evn_bgp: enable
      evn_source_ip: 6.6.6.6
      evn_peer_ip: 7.7.7.7
      provider: "{{ cli }}"
  - name: Configure a Layer 3 VXLAN gateway as a BGP RR.
    community.network.ce_vxlan_arp:
      evn_bgp: enable
      evn_server: enable
      provider: "{{ cli }}"
  - name: Enable EVN BGP on a Layer 3 VXLAN gateway to collect host information.
    community.network.ce_vxlan_arp:
      vbdif_name: Vbdif100
      arp_collect_host: enable
      provider: "{{ cli }}"
  - name: Enable Layer 2 and Layer 3 VXLAN gateways to use EVN BGP to advertise host information.
    community.network.ce_vxlan_arp:
      host_collect_protocol: bgp
      provider: "{{ cli }}"
  - name: Enable ARP broadcast suppression on a Layer 2 VXLAN gateway.
    community.network.ce_vxlan_arp:
      bridge_domain_id: 100
      arp_suppress: enable
      provider: "{{ cli }}"
```

## [Return Values](ce_vxlan_arp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of configuration after module execution  Returned: verbose mode  Sample: `{"evn_bgp": "enable", "evn_peer_ip": ["7.7.7.7"], "evn_source_ip": "6.6.6.6"}` |
| **existing**  dictionary | k/v pairs of existing configuration  Returned: verbose mode  Sample: `{"evn_bgp": "disable", "evn_peer_ip": [], "evn_source_ip": null}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: verbose mode  Sample: `{"evn_bgp": "enable", "evn_peer_ip": "7.7.7.7", "evn_source_ip": "6.6.6.6", "state": "present"}` |
| **updates**  list / elements=string | commands sent to the device  Returned: always  Sample: `["evn bgp", "source-address 6.6.6.6", "peer 7.7.7.7"]` |

### Authors

- QijunPan (@QijunPan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
