---
collection: ansible
version: "8"
title: "community.network.ce_vxlan_global module – Manages global attributes of VXLAN and bridge domain on HUAWEI CloudEngine devices."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_vxlan_global_module.html
fetched_at: 2026-07-28T01:56:03+00:00
---
# community.network.ce_vxlan_global module – Manages global attributes of VXLAN and bridge domain on HUAWEI CloudEngine devices.

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
> To use it in a playbook, specify: `community.network.ce_vxlan_global`.

- [Synopsis](ce_vxlan_global_module.md#synopsis)
- [Parameters](ce_vxlan_global_module.md#parameters)
- [Notes](ce_vxlan_global_module.md#notes)
- [Examples](ce_vxlan_global_module.md#examples)
- [Return Values](ce_vxlan_global_module.md#return-values)

## [Synopsis](ce_vxlan_global_module.md#id1)

- Manages global attributes of VXLAN and bridge domain on HUAWEI CloudEngine devices.

Aliases: network.cloudengine.ce_vxlan_global

## [Parameters](ce_vxlan_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bridge_domain_id**  string | Specifies a bridge domain ID. The value is an integer ranging from 1 to 16777215. |
| **nvo3_acl_extend**  string | Enabling or disabling the VXLAN ACL extension function.  **Choices:**   - `"enable"` - `"disable"` |
| **nvo3_ecmp_hash**  string | Load balancing of VXLAN packets through ECMP in optimized mode.  **Choices:**   - `"enable"` - `"disable"` |
| **nvo3_eth_trunk_hash**  string | Eth-Trunk from load balancing VXLAN packets in optimized mode.  **Choices:**   - `"enable"` - `"disable"` |
| **nvo3_gw_enhanced**  string | Configuring the Layer 3 VXLAN Gateway to Work in Non-loopback Mode.  **Choices:**   - `"l2"` - `"l3"` |
| **nvo3_prevent_loops**  string | Loop prevention of VXLAN traffic in non-enhanced mode. When the device works in non-enhanced mode, inter-card forwarding of VXLAN traffic may result in loops.  **Choices:**   - `"enable"` - `"disable"` |
| **nvo3_service_extend**  string | Enabling or disabling the VXLAN service extension function.  **Choices:**   - `"enable"` - `"disable"` |
| **state**  string | Determines whether the config should be present or not on the device.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tunnel_mode_vxlan**  string | Set the tunnel mode to VXLAN when configuring the VXLAN feature.  **Choices:**   - `"enable"` - `"disable"` |

## [Notes](ce_vxlan_global_module.md#id3)

> **Note:**
>
> - Recommended connection is `network_cli`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_vxlan_global_module.md#id4)

```yaml+jinja
- name: Vxlan global module test
  hosts: ce128
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

  - name: Create bridge domain and set tunnel mode to VXLAN
    community.network.ce_vxlan_global:
      bridge_domain_id: 100
      nvo3_acl_extend: enable
      provider: "{{ cli }}"
```

## [Return Values](ce_vxlan_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of configuration after module execution  **Returned:** verbose mode  **Sample:** `{"bridge_domain_id": {"100": null, "80": null, "90": null}, "nvo3_acl_extend": "enable"}` |
| **existing**  dictionary | k/v pairs of existing configuration  **Returned:** verbose mode  **Sample:** `{"bridge_domain": {"80": null, "90": null}, "nvo3_acl_extend": "disable"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** verbose mode  **Sample:** `{"bridge_domain_id": "100", "nvo3_acl_extend": "enable", "state=\"present\"": null}` |
| **updates**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["bridge-domain 100", "ip tunnel mode vxlan"]` |

### Authors

- QijunPan (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
