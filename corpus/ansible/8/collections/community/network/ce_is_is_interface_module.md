---
collection: ansible
version: "8"
title: "community.network.ce_is_is_interface module – Manages isis interface configuration on HUAWEI CloudEngine devices."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_is_is_interface_module.html
fetched_at: 2026-07-28T01:55:33+00:00
---
# community.network.ce_is_is_interface module – Manages isis interface configuration on HUAWEI CloudEngine devices.

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
> To use it in a playbook, specify: `community.network.ce_is_is_interface`.

New in community.network 0.2.0

- [Synopsis](ce_is_is_interface_module.md#synopsis)
- [Parameters](ce_is_is_interface_module.md#parameters)
- [Notes](ce_is_is_interface_module.md#notes)
- [Examples](ce_is_is_interface_module.md#examples)
- [Return Values](ce_is_is_interface_module.md#return-values)

## [Synopsis](ce_is_is_interface_module.md#id1)

- Manages isis process id, creates a isis instance id or deletes a process id on HUAWEI CloudEngine devices.

Aliases: network.cloudengine.ce_is_is_interface

## [Parameters](ce_is_is_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bfdblocken**  boolean | Blocking interfaces to dynamically create BFD features. The value is a bool type.  **Choices:**   - `false` - `true` |
| **bfdstaticen**  boolean | Configure static BFD on a specific interface enabled with ISIS. The value is a bool type.  **Choices:**   - `false` - `true` |
| **ifname**  string / required | A L3 interface. |
| **instance_id**  integer / required | Specifies the id of a isis process. The value is a number of 1 to 4294967295. |
| **level1cost**  integer | Specifies the link cost of the interface when performing Level-1 SPF calculation. The value is a number of 0 to 16777215. |
| **level1dispriority**  integer | the dispriority of the level1. The value is a number of 1 to 127. |
| **level2cost**  integer | Specifies the link cost of the interface when performing Level-2 SPF calculation. The value is a number of 0 to 16777215. |
| **level2dispriority**  integer | the dispriority of the level1. The value is a number of 1 to 127. |
| **leveltype**  string | level type for three types.  **Choices:**   - `"level_1"` - `"level_2"` - `"level_1_2"` |
| **p2pnegotiationmode**  string | Set the P2P neighbor negotiation type.  **Choices:**   - `"2_way"` - `"3_way"` - `"3_wayonly"` |
| **p2ppeeripignore**  boolean | When the P2P hello packet is received, no IP address check is performed. The value is a bool type.  **Choices:**   - `false` - `true` |
| **ppposicpcheckenable**  boolean | Interface for setting PPP link protocol to check OSICP negotiation status. The value is a bool type.  **Choices:**   - `false` - `true` |
| **silentcost**  boolean | Specifies whether the routing cost of the silent interface is 0. The value is a bool type.  **Choices:**   - `false` - `true` |
| **silentenable**  boolean | enable the interface can send isis message. The value is a bool type.  **Choices:**   - `false` - `true` |
| **snpacheck**  boolean | Enable SNPA check for LSPs and SNPs. The value is a bool type.  **Choices:**   - `false` - `true` |
| **state**  string | Determines whether the config should be present or not on the device.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **typep2penable**  boolean | Simulate the network type of the interface as P2P. The value is a bool type.  **Choices:**   - `false` - `true` |

## [Notes](ce_is_is_interface_module.md#id3)

> **Note:**
>
> - Interface must already be a L3 port when using this module.
> - This module requires the netconf system service be enabled on the remote device being managed.
> - This module works with connection `netconf`.

## [Examples](ce_is_is_interface_module.md#id4)

```yaml+jinja
- name: "create vlan and config vlanif"
  ce_config:
    lines: 'vlan {{ test_vlan_id }},quit,interface {{test_intf_vlanif}},ip address {{test_vlanif_ip}} 24'
    match: none

- name: "create eth-trunk and config eth-trunk"
  ce_config:
    lines: 'interface {{test_intf_trunk}},undo portswitch,ip address {{test_trunk_ip}} 24'
    match: none

- name: "create vpn instance"
  ce_config:
    lines: 'ip vpn-instance {{test_vpn}},ipv4-family'
    match: none

- name: Set isis circuit-level
  community.network.ce_is_is_interface:
    instance_id: 3
    ifname: Eth-Trunk10
    leveltype: level_1_2
    state: present

- name: Set isis level1dispriority
  community.network.ce_is_is_interface:
    instance_id: 3
    ifname: Eth-Trunk10
    level1dispriority: 0
    state: present

- name: Set isis level2dispriority
  community.network.ce_is_is_interface:
    instance_id: 3
    ifname: Eth-Trunk10
    level2dispriority: 0
    state: present

- name: Set isis silentenable
  community.network.ce_is_is_interface:
    instance_id: 3
    ifname: Eth-Trunk10
    silentenable: true
    state: present

- name: Set vpn name
  ce_is_is_instance:
    instance_id: 22
    vpn_name: vpn1
    state: present
```

## [Return Values](ce_is_is_interface_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of configuration after module execution  **Returned:** always  **Sample:** `{"session": {"addrType": "IPV4", "createType": "SESS_STATIC", "destAddr": null, "outIfName": "10GE1/0/1", "sessName": "bfd_l2link", "srcAddr": null, "useDefaultIp": "true", "vrfName": null}}` |
| **existing**  dictionary | k/v pairs of existing configuration  **Returned:** always  **Sample:** `{"session": {}}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** always  **Sample:** `{"addr_type": null, "create_type": null, "dest_addr": null, "out_if_name": "10GE1/0/1", "session_name": "bfd_l2link", "src_addr": null, "state": "present", "use_default_ip": true, "vrf_name": null}` |
| **updates**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["bfd bfd_l2link bind peer-ip default-ip interface 10ge1/0/1"]` |

### Authors

- xuxiaowei0512 (@CloudEngine-Ansible)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
