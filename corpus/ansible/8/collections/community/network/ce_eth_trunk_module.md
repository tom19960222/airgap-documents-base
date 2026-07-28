---
collection: ansible
version: "8"
title: "community.network.ce_eth_trunk module – Manages Eth-Trunk interfaces on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_eth_trunk_module.html
fetched_at: 2026-07-28T01:55:22+00:00
---
# community.network.ce_eth_trunk module – Manages Eth-Trunk interfaces on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_eth_trunk`.

- [Synopsis](ce_eth_trunk_module.md#synopsis)
- [Parameters](ce_eth_trunk_module.md#parameters)
- [Notes](ce_eth_trunk_module.md#notes)
- [Examples](ce_eth_trunk_module.md#examples)
- [Return Values](ce_eth_trunk_module.md#return-values)

## [Synopsis](ce_eth_trunk_module.md#id1)

- Manages Eth-Trunk specific configuration parameters on HUAWEI CloudEngine switches.

Aliases: network.cloudengine.ce_eth_trunk

## [Parameters](ce_eth_trunk_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **force**  boolean | When true it forces Eth-Trunk members to match what is declared in the members param. This can be used to remove members.  **Choices:**   - `false` ← (default) - `true` |
| **hash_type**  string | Hash algorithm used for load balancing among Eth-Trunk member interfaces.  **Choices:**   - `"src-dst-ip"` - `"src-dst-mac"` - `"enhanced"` - `"dst-ip"` - `"dst-mac"` - `"src-ip"` - `"src-mac"` |
| **members**  string | List of interfaces that will be managed in a given Eth-Trunk. The interface name must be full name. |
| **min_links**  string | Specifies the minimum number of Eth-Trunk member links in the Up state. The value is an integer ranging from 1 to the maximum number of interfaces that can be added to a Eth-Trunk interface. |
| **mode**  string | Specifies the working mode of an Eth-Trunk interface.  **Choices:**   - `"manual"` - `"lacp-dynamic"` - `"lacp-static"` |
| **state**  string | Manage the state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **trunk_id**  string / required | Eth-Trunk interface number. The value is an integer. The value range depends on the assign forward eth-trunk mode command. When 256 is specified, the value ranges from 0 to 255. When 512 is specified, the value ranges from 0 to 511. When 1024 is specified, the value ranges from 0 to 1023. |

## [Notes](ce_eth_trunk_module.md#id3)

> **Note:**
>
> - `state=absent` removes the Eth-Trunk config and interface if it already exists. If members to be removed are not explicitly passed, all existing members (if any), are removed, and Eth-Trunk removed.
> - Members must be a list.
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_eth_trunk_module.md#id4)

```yaml+jinja
- name: Eth_trunk module test
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
  - name: Ensure Eth-Trunk100 is created, add two members, and set to mode lacp-static
    community.network.ce_eth_trunk:
      trunk_id: 100
      members: ['10GE1/0/24','10GE1/0/25']
      mode: 'lacp-static'
      state: present
      provider: '{{ cli }}'
```

## [Return Values](ce_eth_trunk_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of Eth-Trunk info after module execution  **Returned:** always  **Sample:** `{"hash_type": "mac", "members_detail": [{"memberIfName": "10GE1/0/24", "memberIfState": "Down"}, {"memberIfName": "10GE1/0/25", "memberIfState": "Down"}], "min_links": "1", "mode": "lacp-static", "trunk_id": "100"}` |
| **existing**  dictionary | k/v pairs of existing Eth-Trunk  **Returned:** always  **Sample:** `{"hash_type": "mac", "members_detail": [{"memberIfName": "10GE1/0/25", "memberIfState": "Down"}], "min_links": "1", "mode": "manual", "trunk_id": "100"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** always  **Sample:** `{"members": ["10GE1/0/24", "10GE1/0/25"], "mode": "lacp-static", "trunk_id": "100"}` |
| **updates**  list / elements=string | command sent to the device  **Returned:** always  **Sample:** `["interface Eth-Trunk 100", "mode lacp-static", "interface 10GE1/0/25", "eth-trunk 100"]` |

### Authors

- QijunPan (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
