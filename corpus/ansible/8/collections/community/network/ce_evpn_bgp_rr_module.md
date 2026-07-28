---
collection: ansible
version: "8"
title: "community.network.ce_evpn_bgp_rr module – Manages RR for the VXLAN Network on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_evpn_bgp_rr_module.html
fetched_at: 2026-07-28T01:55:24+00:00
---
# community.network.ce_evpn_bgp_rr module – Manages RR for the VXLAN Network on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_evpn_bgp_rr`.

- [Synopsis](ce_evpn_bgp_rr_module.md#synopsis)
- [Parameters](ce_evpn_bgp_rr_module.md#parameters)
- [Notes](ce_evpn_bgp_rr_module.md#notes)
- [Examples](ce_evpn_bgp_rr_module.md#examples)
- [Return Values](ce_evpn_bgp_rr_module.md#return-values)

## [Synopsis](ce_evpn_bgp_rr_module.md#id1)

- Configure an RR in BGP-EVPN address family view on HUAWEI CloudEngine switches.

Aliases: network.cloudengine.ce_evpn_bgp_rr

## [Parameters](ce_evpn_bgp_rr_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **as_number**  string / required | Specifies the number of the AS, in integer format. The value is an integer that ranges from 1 to 4294967295. |
| **bgp_evpn_enable**  string | Enable or disable the BGP-EVPN address family.  **Choices:**   - `"enable"` ← (default) - `"disable"` |
| **bgp_instance**  string | Specifies the name of a BGP instance. The value of instance-name can be an integer 1 or a string of 1 to 31. |
| **peer**  string | Specifies the IPv4 address or the group name of a peer. |
| **peer_type**  string | Specify the peer type.  **Choices:**   - `"group_name"` - `"ipv4_address"` |
| **policy_vpn_target**  string | Enable or disable the VPN-Target filtering.  **Choices:**   - `"enable"` - `"disable"` |
| **reflect_client**  string | Configure the local device as the route reflector and the peer or peer group as the client of the route reflector.  **Choices:**   - `"enable"` - `"disable"` |

## [Notes](ce_evpn_bgp_rr_module.md#id3)

> **Note:**
>
> - Ensure that BGP view is existed.
> - The peer, peer_type, and reflect_client arguments must all exist or not exist.
> - Recommended connection is `network_cli`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_evpn_bgp_rr_module.md#id4)

```yaml+jinja
- name: BGP RR test
  hosts: cloudengine
  connection: local
  gather_facts: false
  vars:
    cli:
      host: "{{ inventory_hostname }}"
      port: "{{ ansible_ssh_port }}"
      username: "{{ username }}"
      password: "{{ password }}"
      transport: cli

  tasks:

  - name: "Configure BGP-EVPN address family view and ensure that BGP view has existed."
    community.network.ce_evpn_bgp_rr:
      as_number: 20
      bgp_evpn_enable: enable
      provider: "{{ cli }}"

  - name: "Configure reflect client and ensure peer has existed."
    community.network.ce_evpn_bgp_rr:
      as_number: 20
      peer_type: ipv4_address
      peer: 192.8.3.3
      reflect_client: enable
      provider: "{{ cli }}"

  - name: "Configure the VPN-Target filtering."
    community.network.ce_evpn_bgp_rr:
      as_number: 20
      policy_vpn_target: enable
      provider: "{{ cli }}"

  - name: "Configure an RR in BGP-EVPN address family view."
    community.network.ce_evpn_bgp_rr:
      as_number: 20
      bgp_evpn_enable: enable
      peer_type: ipv4_address
      peer: 192.8.3.3
      reflect_client: enable
      policy_vpn_target: disable
      provider: "{{ cli }}"
```

## [Return Values](ce_evpn_bgp_rr_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of end attributes on the device  **Returned:** always  **Sample:** `{"as_number": "20", "bgp_evpn_enable": "enable", "bgp_instance": null, "peer": "192.8.3.3", "peer_type": "ipv4_address", "policy_vpn_target": "disable", "reflect_client": "enable"}` |
| **existing**  dictionary | k/v pairs of existing attributes on the device  **Returned:** always  **Sample:** `{"as_number": "20", "bgp_evpn_enable": "disable", "bgp_instance": null, "peer": null, "peer_type": null, "policy_vpn_target": "disable", "reflect_client": "disable"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** always  **Sample:** `{"as_number": "20", "bgp_evpn_enable": "enable", "bgp_instance": null, "peer": "192.8.3.3", "peer_type": "ipv4_address", "policy_vpn_target": "disable", "reflect_client": "enable"}` |
| **updates**  list / elements=string | command list sent to the device  **Returned:** always  **Sample:** `["bgp 20", "  l2vpn-family evpn", "    peer 192.8.3.3 enable", "    peer 192.8.3.3 reflect-client", "    undo policy vpn-target"]` |

### Authors

- Zhijin Zhou (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
