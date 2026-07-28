---
collection: ansible
version: "8"
title: "community.network.ce_vxlan_vap module – Manages VXLAN virtual access point on HUAWEI CloudEngine Devices."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_vxlan_vap_module.html
fetched_at: 2026-07-28T01:56:04+00:00
---
# community.network.ce_vxlan_vap module – Manages VXLAN virtual access point on HUAWEI CloudEngine Devices.

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
> To use it in a playbook, specify: `community.network.ce_vxlan_vap`.

- [Synopsis](ce_vxlan_vap_module.md#synopsis)
- [Parameters](ce_vxlan_vap_module.md#parameters)
- [Notes](ce_vxlan_vap_module.md#notes)
- [Examples](ce_vxlan_vap_module.md#examples)
- [Return Values](ce_vxlan_vap_module.md#return-values)

## [Synopsis](ce_vxlan_vap_module.md#id1)

- Manages VXLAN Virtual access point on HUAWEI CloudEngine Devices.

Aliases: network.cloudengine.ce_vxlan_vap

## [Parameters](ce_vxlan_vap_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bind_vlan_id**  string | Specifies the VLAN binding to a BD(Bridge Domain). The value is an integer ranging ranging from 1 to 4094. |
| **bridge_domain_id**  string | Specifies a bridge domain ID. The value is an integer ranging from 1 to 16777215. |
| **ce_vid**  string | When *encapsulation* is ‘dot1q’, specifies a VLAN ID in the outer VLAN tag. When *encapsulation* is ‘qinq’, specifies an outer VLAN ID for double-tagged packets to be received by a Layer 2 sub-interface. The value is an integer ranging from 1 to 4094. |
| **encapsulation**  string | Specifies an encapsulation type of packets allowed to pass through a Layer 2 sub-interface.  **Choices:**   - `"dot1q"` - `"default"` - `"untag"` - `"qinq"` - `"none"` |
| **l2_sub_interface**  string | Specifies an Sub-Interface full name, i.e. “10GE1/0/41.1”. The value is a string of 1 to 63 case-insensitive characters, spaces supported. |
| **pe_vid**  string | When *encapsulation* is ‘qinq’, specifies an inner VLAN ID for double-tagged packets to be received by a Layer 2 sub-interface. The value is an integer ranging from 1 to 4094. |
| **state**  string | Determines whether the config should be present or not on the device.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](ce_vxlan_vap_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_vxlan_vap_module.md#id4)

```yaml+jinja
- name: Vxlan vap module test
  hosts: ce128
  connection: local
  gather_facts: false

  tasks:

  - name: Create a mapping between a VLAN and a BD
    community.network.ce_vxlan_vap:
      bridge_domain_id: 100
      bind_vlan_id: 99

  - name: Bind a Layer 2 sub-interface to a BD
    community.network.ce_vxlan_vap:
      bridge_domain_id: 100
      l2_sub_interface: 10GE2/0/20.1

  - name: Configure an encapsulation type on a Layer 2 sub-interface
    community.network.ce_vxlan_vap:
      l2_sub_interface: 10GE2/0/20.1
      encapsulation: dot1q
```

## [Return Values](ce_vxlan_vap_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of configuration after module execution  **Returned:** verbose mode  **Sample:** `{"bind_intf_list": ["110GE2/0/20.1", "10GE2/0/20.2"], "bind_vlan_list": ["99"], "bridge_domain_id": "100"}` |
| **existing**  dictionary | k/v pairs of existing configuration  **Returned:** verbose mode  **Sample:** `{"bind_intf_list": ["10GE2/0/20.1", "10GE2/0/20.2"], "bind_vlan_list": [], "bridge_domain_id": "100"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** verbose mode  **Sample:** `{"bind_vlan_id": "99", "bridge_domain_id": "100", "state=\"present\"": null}` |
| **updates**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["bridge-domain 100", "l2 binding vlan 99"]` |

### Authors

- QijunPan (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
