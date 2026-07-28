---
collection: ansible
version: "8"
title: "community.network.ce_evpn_bd_vni module – Manages EVPN VXLAN Network Identifier (VNI) on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_evpn_bd_vni_module.html
fetched_at: 2026-07-28T01:55:23+00:00
---
# community.network.ce_evpn_bd_vni module – Manages EVPN VXLAN Network Identifier (VNI) on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_evpn_bd_vni`.

- [Synopsis](ce_evpn_bd_vni_module.md#synopsis)
- [Parameters](ce_evpn_bd_vni_module.md#parameters)
- [Notes](ce_evpn_bd_vni_module.md#notes)
- [Examples](ce_evpn_bd_vni_module.md#examples)
- [Return Values](ce_evpn_bd_vni_module.md#return-values)

## [Synopsis](ce_evpn_bd_vni_module.md#id1)

- Manages Ethernet Virtual Private Network (EVPN) VXLAN Network Identifier (VNI) configurations on HUAWEI CloudEngine switches.

Aliases: network.cloudengine.ce_evpn_bd_vni

## [Parameters](ce_evpn_bd_vni_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bridge_domain_id**  string / required | Specify an existed bridge domain (BD).The value is an integer ranging from 1 to 16777215. |
| **evpn**  string | Create or delete an EVPN instance for a VXLAN in BD view.  **Choices:**   - `"enable"` ← (default) - `"disable"` |
| **route_distinguisher**  string | Configures a route distinguisher (RD) for a BD EVPN instance. The format of an RD can be as follows   1. 2-byte AS number:4-byte user-defined number, for example, 1:3. An AS number is an integer ranging from 0 to 65535, and a user-defined number is an integer ranging from 0 to 4294967295. The AS and user-defined numbers cannot be both 0s. This means that an RD cannot be 0:0. 2. Integral 4-byte AS number:2-byte user-defined number, for example, 65537:3. An AS number is an integer ranging from 65536 to 4294967295, and a user-defined number is an integer ranging from 0 to 65535. 3. 4-byte AS number in dotted notation:2-byte user-defined number, for example, 0.0:3 or 0.1:0. A 4-byte AS number in dotted notation is in the format of x.y, where x and y are integers ranging from 0 to 65535. 4. A user-defined number is an integer ranging from 0 to 65535. The AS and user-defined numbers cannot be both 0s. This means that an RD cannot be 0.0:0. 5. 32-bit IP address:2-byte user-defined number. For example, 192.168.122.15:1. An IP address ranges from 0.0.0.0 to 255.255.255.255, and a user-defined number is an integer ranging from 0 to 65535. 6. ‘auto’ specifies the RD that is automatically generated. |
| **state**  string | Manage the state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **vpn_target_both**  string | Add VPN targets to both the import and export VPN target lists of a BD EVPN instance. The format is the same as route_distinguisher. |
| **vpn_target_export**  string | Add VPN targets to the export VPN target list of a BD EVPN instance. The format is the same as route_distinguisher. |
| **vpn_target_import**  string / required | Add VPN targets to the import VPN target list of a BD EVPN instance. The format is the same as route_distinguisher. |

## [Notes](ce_evpn_bd_vni_module.md#id3)

> **Note:**
>
> - Ensure that EVPN has been configured to serve as the VXLAN control plane when state is present.
> - Ensure that a bridge domain (BD) has existed when state is present.
> - Ensure that a VNI has been created and associated with a broadcast domain (BD) when state is present.
> - If you configure evpn:false to delete an EVPN instance, all configurations in the EVPN instance are deleted.
> - After an EVPN instance has been created in the BD view, you can configure an RD using route_distinguisher parameter in BD-EVPN instance view.
> - Before configuring VPN targets for a BD EVPN instance, ensure that an RD has been configured for the BD EVPN instance
> - If you unconfigure route_distinguisher, all VPN target attributes for the BD EVPN instance will be removed at the same time.
> - When using state:absent, evpn is not supported and it will be ignored.
> - When using state:absent to delete VPN target attributes, ensure the configuration of VPN target attributes has existed and otherwise it will report an error.
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_evpn_bd_vni_module.md#id4)

```yaml+jinja
- name: EVPN BD VNI test
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

  - name: "Configure an EVPN instance for a VXLAN in BD view"
    community.network.ce_evpn_bd_vni:
      bridge_domain_id: 20
      evpn: enable
      provider: "{{ cli }}"

  - name: "Configure a route distinguisher (RD) for a BD EVPN instance"
    community.network.ce_evpn_bd_vni:
      bridge_domain_id: 20
      route_distinguisher: '22:22'
      provider: "{{ cli }}"

  - name: "Configure VPN targets to both the import and export VPN target lists of a BD EVPN instance"
    community.network.ce_evpn_bd_vni:
      bridge_domain_id: 20
      vpn_target_both: 22:100,22:101
      provider: "{{ cli }}"

  - name: "Configure VPN targets to the import VPN target list of a BD EVPN instance"
    community.network.ce_evpn_bd_vni:
      bridge_domain_id: 20
      vpn_target_import: 22:22,22:23
      provider: "{{ cli }}"

  - name: "Configure VPN targets to the export VPN target list of a BD EVPN instance"
    community.network.ce_evpn_bd_vni:
      bridge_domain_id: 20
      vpn_target_export: 22:38,22:39
      provider: "{{ cli }}"

  - name: "Unconfigure VPN targets to both the import and export VPN target lists of a BD EVPN instance"
    community.network.ce_evpn_bd_vni:
      bridge_domain_id: 20
      vpn_target_both: '22:100'
      state: absent
      provider: "{{ cli }}"

  - name: "Unconfigure VPN targets to the import VPN target list of a BD EVPN instance"
    community.network.ce_evpn_bd_vni:
      bridge_domain_id: 20
      vpn_target_import: '22:22'
      state: absent
      provider: "{{ cli }}"

  - name: "Unconfigure VPN targets to the export VPN target list of a BD EVPN instance"
    community.network.ce_evpn_bd_vni:
      bridge_domain_id: 20
      vpn_target_export: '22:38'
      state: absent
      provider: "{{ cli }}"

  - name: "Unconfigure a route distinguisher (RD) of a BD EVPN instance"
    community.network.ce_evpn_bd_vni:
      bridge_domain_id: 20
      route_distinguisher: '22:22'
      state: absent
      provider: "{{ cli }}"

  - name: "Unconfigure an EVPN instance for a VXLAN in BD view"
    community.network.ce_evpn_bd_vni:
      bridge_domain_id: 20
      evpn: disable
      provider: "{{ cli }}"
```

## [Return Values](ce_evpn_bd_vni_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of end attributes on the device  **Returned:** always  **Sample:** `{"bridge_domain_id": "2", "evpn": "enable", "route_distinguisher": "22:22", "vpn_target_both": ["22:100", "22:101"], "vpn_target_export": ["22:38", "22:39"], "vpn_target_import": ["22:22", "22:23"]}` |
| **existing**  dictionary | k/v pairs of existing attributes on the device  **Returned:** always  **Sample:** `{"bridge_domain_id": "2", "evpn": "disable", "route_distinguisher": null, "vpn_target_both": [], "vpn_target_export": [], "vpn_target_import": []}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** always  **Sample:** `{"bridge_domain_id": "2", "evpn": "enable", "route_distinguisher": "22:22", "state": "present", "vpn_target_both": ["22:100", "22:101"], "vpn_target_export": ["22:38", "22:39"], "vpn_target_import": ["22:22", "22:23"]}` |
| **updates**  list / elements=string | command list sent to the device  **Returned:** always  **Sample:** `["bridge-domain 2", "  evpn", "    route-distinguisher 22:22", "    vpn-target 22:38 export-extcommunity", "    vpn-target 22:39 export-extcommunity", "    vpn-target 22:100 export-extcommunity", "    vpn-target 22:101 export-extcommunity", "    vpn-target 22:22 import-extcommunity", "    vpn-target 22:23 import-extcommunity", "    vpn-target 22:100 import-extcommunity", "    vpn-target 22:101 import-extcommunity"]` |

### Authors

- Zhijin Zhou (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
