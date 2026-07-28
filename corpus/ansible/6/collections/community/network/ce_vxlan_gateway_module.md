---
collection: ansible
version: "6"
title: "community.network.ce_vxlan_gateway module – Manages gateway for the VXLAN network on HUAWEI CloudEngine devices."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_vxlan_gateway_module.html
fetched_at: 2026-07-27T17:18:00+00:00
---
# community.network.ce_vxlan_gateway module – Manages gateway for the VXLAN network on HUAWEI CloudEngine devices.

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
> To use it in a playbook, specify: `community.network.ce_vxlan_gateway`.

- [Synopsis](ce_vxlan_gateway_module.md#synopsis)
- [Parameters](ce_vxlan_gateway_module.md#parameters)
- [Notes](ce_vxlan_gateway_module.md#notes)
- [Examples](ce_vxlan_gateway_module.md#examples)
- [Return Values](ce_vxlan_gateway_module.md#return-values)

## [Synopsis](ce_vxlan_gateway_module.md#id1)

- Configuring Centralized All-Active Gateways or Distributed Gateway for the VXLAN Network on HUAWEI CloudEngine devices.

## [Parameters](ce_vxlan_gateway_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **arp_direct_route**  string | Enable VLINK direct route on VBDIF interface.  Choices:   - `"enable"` - `"disable"` |
| **arp_distribute_gateway**  string | Enable the distributed gateway function on VBDIF interface.  Choices:   - `"enable"` - `"disable"` |
| **dfs_all_active**  string | Creates all-active gateways.  Choices:   - `"enable"` - `"disable"` |
| **dfs_id**  string | Specifies the ID of a DFS group. The value must be 1. |
| **dfs_peer_ip**  string | Configure the IP address of an all-active gateway peer. The value is in dotted decimal notation. |
| **dfs_peer_vpn**  string | Specifies the name of the VPN instance that is associated with all-active gateway peer. The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. The value `_public_` is reserved and cannot be used as the VPN instance name. |
| **dfs_source_ip**  string | Specifies the IPv4 address bound to a DFS group. The value is in dotted decimal notation. |
| **dfs_source_vpn**  string | Specifies the name of a VPN instance bound to a DFS group. The value is a string of 1 to 31 case-sensitive characters without spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. The value `_public_` is reserved and cannot be used as the VPN instance name. |
| **dfs_udp_port**  string | Specifies the UDP port number of the DFS group. The value is an integer that ranges from 1025 to 65535. |
| **state**  string | Determines whether the config should be present or not on the device.  Choices:   - `"present"` ← (default) - `"absent"` |
| **vbdif_bind_vpn**  string | Specifies the name of the VPN instance that is associated with the interface. The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. The value `_public_` is reserved and cannot be used as the VPN instance name. |
| **vbdif_mac**  string | Specifies a MAC address for a VBDIF interface. The value is in the format of H-H-H. Each H is a 4-digit hexadecimal number, such as `00e0` or `fc01`. If an H contains less than four digits, 0s are added ahead. For example, `e0` is equal to `00e0`. A MAC address cannot be all 0s or 1s or a multicast MAC address. |
| **vbdif_name**  string | Full name of VBDIF interface, i.e. Vbdif100. |
| **vpn_instance**  string | Specifies the name of a VPN instance. The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. The value `_public_` is reserved and cannot be used as the VPN instance name. |
| **vpn_vni**  string | Specifies a VNI ID. Binds a VXLAN network identifier (VNI) to a virtual private network (VPN) instance. The value is an integer ranging from 1 to 16000000. |

## [Notes](ce_vxlan_gateway_module.md#id3)

> **Note:**
>
> - Ensure All-Active Gateways or Distributed Gateway for the VXLAN Network can not configure at the same time.
> - Recommended connection is `network_cli`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_vxlan_gateway_module.md#id4)

```yaml+jinja
- name: Vxlan gateway module test
  hosts: ce128
  connection: local
  gather_facts: no

  tasks:

  - name: Configuring Centralized All-Active Gateways for the VXLAN Network
    community.network.ce_vxlan_gateway:
      dfs_id: 1
      dfs_source_ip: 6.6.6.6
      dfs_all_active: enable
      dfs_peer_ip: 7.7.7.7
  - name: Bind the VPN instance to a Layer 3 gateway, enable distributed gateway, and configure host route advertisement.
    community.network.ce_vxlan_gateway:
      vbdif_name: Vbdif100
      vbdif_bind_vpn: vpn1
      arp_distribute_gateway: enable
      arp_direct_route: enable
  - name: Assign a VNI to a VPN instance.
    community.network.ce_vxlan_gateway:
      vpn_instance: vpn1
      vpn_vni: 100
```

## [Return Values](ce_vxlan_gateway_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of configuration after module execution  Returned: verbose mode  Sample: `{"dfs_all_active": "enable", "dfs_id": "1", "evn_peers": [{"ip": "7.7.7.7", "vpn": ""}], "evn_source_ip": "6.6.6.6", "evn_source_vpn": null}` |
| **existing**  dictionary | k/v pairs of existing configuration  Returned: verbose mode  Sample: `{"dfs_all_active": "disable", "dfs_id": "1", "dfs_source_ip": null, "evn_peer_ip": []}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: verbose mode  Sample: `{"dfs_all_active": "enable", "dfs_id": "1", "dfs_peer_ip": "7.7.7.7", "dfs_source_ip": "6.6.6.6"}` |
| **updates**  list / elements=string | commands sent to the device  Returned: always  Sample: `["dfs-group 1", "source ip 6.6.6.6", "active-active-gateway", "peer 7.7.7.7"]` |

### Authors

- QijunPan (@QijunPan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
