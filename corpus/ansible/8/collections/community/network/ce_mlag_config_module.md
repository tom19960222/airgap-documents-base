---
collection: ansible
version: "8"
title: "community.network.ce_mlag_config module – Manages MLAG configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_mlag_config_module.html
fetched_at: 2026-07-28T01:55:38+00:00
---
# community.network.ce_mlag_config module – Manages MLAG configuration on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_mlag_config`.

- [Synopsis](ce_mlag_config_module.md#synopsis)
- [Parameters](ce_mlag_config_module.md#parameters)
- [Notes](ce_mlag_config_module.md#notes)
- [Examples](ce_mlag_config_module.md#examples)
- [Return Values](ce_mlag_config_module.md#return-values)

## [Synopsis](ce_mlag_config_module.md#id1)

- Manages MLAG configuration on HUAWEI CloudEngine switches.

Aliases: network.cloudengine.ce_mlag_config

## [Parameters](ce_mlag_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **dfs_group_id**  string | ID of a DFS group. The value is 1.  **Default:** `"present"` |
| **eth_trunk_id**  string | Name of the peer-link interface. The value is in the range from 0 to 511. |
| **ip_address**  string | IP address bound to the DFS group. The value is in dotted decimal notation. |
| **nickname**  string | The nickname bound to a DFS group. The value is an integer that ranges from 1 to 65471. |
| **peer_link_id**  string | Number of the peer-link interface. The value is 1. |
| **priority_id**  string | Priority of a DFS group. The value is an integer that ranges from 1 to 254. The default value is 100. |
| **pseudo_nickname**  string | A pseudo nickname of a DFS group. The value is an integer that ranges from 1 to 65471. |
| **pseudo_priority**  string | The priority of a pseudo nickname. The value is an integer that ranges from 128 to 255. The default value is 192. A larger value indicates a higher priority. |
| **state**  string | Specify desired state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **vpn_instance_name**  string | Name of the VPN instance bound to the DFS group. The value is a string of 1 to 31 case-sensitive characters without spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. The value _public_ is reserved and cannot be used as the VPN instance name. |

## [Notes](ce_mlag_config_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_mlag_config_module.md#id4)

```yaml+jinja
- name: Mlag config module test
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

  - name: Create DFS Group id
    community.network.ce_mlag_config:
      dfs_group_id: 1
      provider: "{{ cli }}"
  - name: Set dfs-group priority
    community.network.ce_mlag_config:
      dfs_group_id: 1
      priority_id: 3
      state: present
      provider: "{{ cli }}"
  - name: Set pseudo nickname
    community.network.ce_mlag_config:
      dfs_group_id: 1
      pseudo_nickname: 3
      pseudo_priority: 130
      state: present
      provider: "{{ cli }}"
  - name: Set ip
    community.network.ce_mlag_config:
      dfs_group_id: 1
      ip_address: 11.1.1.2
      vpn_instance_name: 6
      provider: "{{ cli }}"
  - name: Set peer link
    community.network.ce_mlag_config:
      eth_trunk_id: 3
      peer_link_id: 2
      state: present
      provider: "{{ cli }}"
```

## [Return Values](ce_mlag_config_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of aaa params after module execution  **Returned:** always  **Sample:** `{"eth_trunk_id": "Eth-Trunk3", "peer_link_id": "1"}` |
| **existing**  dictionary | k/v pairs of existing aaa server  **Returned:** always  **Sample:** `{}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** always  **Sample:** `{"eth_trunk_id": "3", "peer_link_id": "1", "state": "present"}` |
| **updates**  list / elements=string | command sent to the device  **Returned:** always  **Sample:** `{"peer-link 1": null}` |

### Authors

- Li Yanfeng (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
