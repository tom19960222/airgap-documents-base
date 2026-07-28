---
collection: ansible
version: "8"
title: "community.network.ce_vrf_interface module – Manages interface specific VPN configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_vrf_interface_module.html
fetched_at: 2026-07-28T01:56:00+00:00
---
# community.network.ce_vrf_interface module – Manages interface specific VPN configuration on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_vrf_interface`.

- [Synopsis](ce_vrf_interface_module.md#synopsis)
- [Parameters](ce_vrf_interface_module.md#parameters)
- [Notes](ce_vrf_interface_module.md#notes)
- [Examples](ce_vrf_interface_module.md#examples)
- [Return Values](ce_vrf_interface_module.md#return-values)

## [Synopsis](ce_vrf_interface_module.md#id1)

- Manages interface specific VPN configuration of HUAWEI CloudEngine switches.

Aliases: network.cloudengine.ce_vrf_interface

## [Parameters](ce_vrf_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **state**  string | Manage the state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **vpn_interface**  string / required | An interface that can binding VPN instance, i.e. 40GE1/0/22, Vlanif10. Must be fully qualified interface name. Interface types, such as 10GE, 40GE, 100GE, LoopBack, MEth, Tunnel, Vlanif…. |
| **vrf**  string / required | VPN instance, the length of vrf name is 1 ~ 31, i.e. “test”, but can not be `_public_`. |

## [Notes](ce_vrf_interface_module.md#id3)

> **Note:**
>
> - Ensure that a VPN instance has been created and the IPv4 address family has been enabled for the VPN instance.
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_vrf_interface_module.md#id4)

```yaml+jinja
- name: VRF interface test
  hosts: cloudengine
  connection: local
  gather_facts: false

  tasks:

  - name: "Configure a VPN instance for the interface"
    community.network.ce_vrf_interface:
      vpn_interface: 40GE1/0/2
      vrf: test
      state: present

  - name: "Disable the association between a VPN instance and an interface"
    community.network.ce_vrf_interface:
      vpn_interface: 40GE1/0/2
      vrf: test
      state: absent
```

## [Return Values](ce_vrf_interface_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of end attributes on the interface  **Returned:** verbose mode  **Sample:** `{"vpn_interface": "40GE2/0/17", "vrf": "jss"}` |
| **existing**  dictionary | k/v pairs of existing attributes on the interface  **Returned:** verbose mode  **Sample:** `{"vpn_interface": "40GE2/0/17", "vrf": null}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** verbose mode  **Sample:** `{"state": "present", "vpn_interface": "40GE2/0/17", "vrf": "jss"}` |
| **updates**  list / elements=string | command list sent to the device  **Returned:** always  **Sample:** `["ip binding vpn-instance jss"]` |

### Authors

- Zhijin Zhou (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
