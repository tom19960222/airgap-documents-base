---
collection: ansible
version: "6"
title: "community.network.ce_vxlan_tunnel module – Manages VXLAN tunnel configuration on HUAWEI CloudEngine devices."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_vxlan_tunnel_module.html
fetched_at: 2026-07-27T17:18:01+00:00
---
# community.network.ce_vxlan_tunnel module – Manages VXLAN tunnel configuration on HUAWEI CloudEngine devices.

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
> To use it in a playbook, specify: `community.network.ce_vxlan_tunnel`.

- [Synopsis](ce_vxlan_tunnel_module.md#synopsis)
- [Parameters](ce_vxlan_tunnel_module.md#parameters)
- [Notes](ce_vxlan_tunnel_module.md#notes)
- [Examples](ce_vxlan_tunnel_module.md#examples)
- [Return Values](ce_vxlan_tunnel_module.md#return-values)

## [Synopsis](ce_vxlan_tunnel_module.md#id1)

- This module offers the ability to set the VNI and mapped to the BD, and configure an ingress replication list on HUAWEI CloudEngine devices.

## [Parameters](ce_vxlan_tunnel_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bridge_domain_id**  string | Specifies a bridge domain ID. The value is an integer ranging from 1 to 16777215. |
| **nve_mode**  string | Specifies the working mode of an NVE interface.  Choices:   - `"mode-l2"` - `"mode-l3"` |
| **nve_name**  string | Specifies the number of an NVE interface. The value ranges from 1 to 2. |
| **peer_list_ip**  string | Specifies the IP address of a remote VXLAN tunnel endpoints (VTEP). The value is in dotted decimal notation. |
| **protocol_type**  string | The operation type of routing protocol.  Choices:   - `"bgp"` - `"null"` |
| **source_ip**  string | Specifies an IP address for a source VTEP. The value is in dotted decimal notation. |
| **state**  string | Manage the state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **vni_id**  string | Specifies a VXLAN network identifier (VNI) ID. The value is an integer ranging from 1 to 16000000. |

## [Notes](ce_vxlan_tunnel_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_vxlan_tunnel_module.md#id4)

```yaml+jinja
- name: Vxlan tunnel module test
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

  - name: Make sure nve_name is exist, ensure vni_id and protocol_type is configured on Nve1 interface.
    community.network.ce_vxlan_tunnel:
      nve_name: Nve1
      vni_id: 100
      protocol_type: bgp
      state: present
      provider: "{{ cli }}"
```

## [Return Values](ce_vxlan_tunnel_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of configuration after module execution  Returned: always  Sample: `{"nve_interface_name\"": "Nve1", "nve_mode\"": "mode-l3", "source_ip": "0.0.0.0"}` |
| **existing**  dictionary | k/v pairs of existing rollback  Returned: always  Sample: `{"nve_interface_name\"": "Nve1", "nve_mode\"": "mode-l3", "source_ip": "0.0.0.0"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: always  Sample: `{"nve_interface_name\"": "Nve1", "nve_mode\"": "mode-l2", "source_ip": "0.0.0.0"}` |
| **updates**  list / elements=string | command sent to the device  Returned: always  Sample: `["interface Nve1", "mode l3"]` |

### Authors

- Li Yanfeng (@QijunPan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
