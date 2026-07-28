---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_vxlans module – Manage VxLAN EVPN and its parameters"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_vxlans_module.html
fetched_at: 2026-07-28T02:03:54+00:00
---
# dellemc.enterprise_sonic.sonic_vxlans module – Manage VxLAN EVPN and its parameters

> **Note:**
>
> This module is part of the [dellemc.enterprise_sonic collection](https://galaxy.ansible.com/ui/repo/published/dellemc/enterprise_sonic/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.enterprise_sonic`.
>
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_vxlans`.

New in dellemc.enterprise_sonic 1.0.0

- [Synopsis](sonic_vxlans_module.md#synopsis)
- [Parameters](sonic_vxlans_module.md#parameters)
- [Notes](sonic_vxlans_module.md#notes)
- [Examples](sonic_vxlans_module.md#examples)
- [Return Values](sonic_vxlans_module.md#return-values)

## [Synopsis](sonic_vxlans_module.md#id1)

- Manages interface attributes of Enterprise SONiC interfaces.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](sonic_vxlans_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of VxLAN configurations. |
| **evpn_nvo**  string | EVPN nvo name |
| **name**  string / required | The name of the VxLAN. |
| **primary_ip**  string | The vtep mclag primary ip address for this node |
| **source_ip**  string | The source IP address of the VTEP. |
| **vlan_map**  list / elements=dictionary | The list of VNI map of VLAN. |
| **vlan**  integer | VLAN ID for VNI VLAN map. |
| **vni**  integer / required | Specifies the VNI ID. |
| **vrf_map**  list / elements=dictionary | list of VNI map of VRF. |
| **vni**  integer / required | Specifies the VNI ID. |
| **vrf**  string | VRF name for VNI VRF map. |
| **state**  string | The state of the configuration after module completion.  **Choices:**   - `"merged"` ← (default) - `"deleted"` - `"replaced"` - `"overridden"` |

## [Notes](sonic_vxlans_module.md#id3)

> **Note:**
>
> - Tested against Enterprise SONiC Distribution by Dell Technologies.
> - Supports `check_mode`.

## [Examples](sonic_vxlans_module.md#id4)

```yaml+jinja
# Using deleted
#
# Before state:
# -------------
#
# do show running-configuration
#
#interface vxlan vteptest1
# source-ip 1.1.1.1
# primary-ip 2.2.2.2
# map vni 101 vlan 11
# map vni 102 vlan 12
# map vni 101 vrf Vrfcheck1
# map vni 102 vrf Vrfcheck2
#!
#
- name: "Test vxlans deleted state 01"
  dellemc.enterprise_sonic.sonic_vxlans:
    config:
      - name: vteptest1
        source_ip: 1.1.1.1
        vlan_map:
          - vni: 101
            vlan: 11
        vrf_map:
          - vni: 101
            vrf: Vrfcheck1
    state: deleted
#
# After state:
# ------------
#
# do show running-configuration
#
#interface vxlan vteptest1
# source-ip 1.1.1.1
# map vni 102 vlan 12
# map vni 102 vrf Vrfcheck2
#!
#
# Using deleted
#
# Before state:
# -------------
#
# do show running-configuration
#
#interface vxlan vteptest1
# source-ip 1.1.1.1
# map vni 102 vlan 12
# map vni 102 vrf Vrfcheck2
#!
#
- name: "Test vxlans deleted state 02"
  dellemc.enterprise_sonic.sonic_vxlans:
    config:
    state: deleted
#
# After state:
# ------------
#
# do show running-configuration
#
#!
#
# Using merged
#
# Before state:
# -------------
#
# do show running-configuration
#
#!
#
- name: "Test vxlans merged state 01"
  dellemc.enterprise_sonic.sonic_vxlans:
    config:
      - name: vteptest1
        source_ip: 1.1.1.1
        primary_ip: 2.2.2.2
        evpn_nvo: nvo1
        vlan_map:
          - vni: 101
            vlan: 11
          - vni: 102
            vlan: 12
        vrf_map:
          - vni: 101
            vrf: Vrfcheck1
          - vni: 102
            vrf: Vrfcheck2
    state: merged
#
# After state:
# ------------
#
# do show running-configuration
#
#interface vxlan vteptest1
# source-ip 1.1.1.1
# primary-ip 2.2.2.2
# map vni 101 vlan 11
# map vni 102 vlan 12
# map vni 101 vrf Vrfcheck1
# map vni 102 vrf Vrfcheck2
#!
#
# Using overridden
#
# Before state:
# -------------
#
# do show running-configuration
#
#interface vxlan vteptest1
# source-ip 1.1.1.1
# primary-ip 2.2.2.2
# map vni 101 vlan 11
# map vni 102 vlan 12
# map vni 101 vrf Vrfcheck1
# map vni 102 vrf Vrfcheck2
#!
#
- name: "Test vxlans overridden state 01"
  dellemc.enterprise_sonic.sonic_vxlans:
    config:
      - name: vteptest2
        source_ip: 3.3.3.3
        primary_ip: 4.4.4.4
        evpn_nvo: nvo2
        vlan_map:
          - vni: 101
            vlan: 11
        vrf_map:
          - vni: 101
            vrf: Vrfcheck1
    state: overridden
#
# After state:
# ------------
#
# do show running-configuration
#
#interface vxlan vteptest2
# source-ip 3.3.3.3
# primary-ip 4.4.4.4
# map vni 101 vlan 11
# map vni 101 vrf Vrfcheck1
#!
#
# Using replaced
#
# Before state:
# -------------
#
# do show running-configuration
#
#interface vxlan vteptest2
# source-ip 3.3.3.3
# primary-ip 4.4.4.4
# map vni 101 vlan 11
# map vni 101 vrf Vrfcheck
#!
#
- name: "Test vxlans replaced state 01"
  dellemc.enterprise_sonic.sonic_vxlans:
    config:
      - name: vteptest2
        source_ip: 5.5.5.5
        vlan_map:
          - vni: 101
            vlan: 12
    state: replaced
#
# After state:
# ------------
#
# do show running-configuration
#
#interface vxlan vteptest2
# source-ip 5.5.5.5
# primary-ip 4.4.4.4
# map vni 101 vlan 12
# map vni 101 vrf Vrfcheck1
#!
#
```

## [Return Values](sonic_vxlans_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned is always in the same format of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned is always in the same format of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands that are pushed to the remote device.  **Returned:** always  **Sample:** `["command 1", "command 2", "command 3"]` |

### Authors

- Niraimadaiselvam M (@niraimadaiselvamm)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
