---
collection: ansible
version: "6"
title: "community.network.ce_mlag_interface module – Manages MLAG interfaces on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_mlag_interface_module.html
fetched_at: 2026-07-27T17:17:38+00:00
---
# community.network.ce_mlag_interface module – Manages MLAG interfaces on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_mlag_interface`.

- [Synopsis](ce_mlag_interface_module.md#synopsis)
- [Parameters](ce_mlag_interface_module.md#parameters)
- [Notes](ce_mlag_interface_module.md#notes)
- [Examples](ce_mlag_interface_module.md#examples)
- [Return Values](ce_mlag_interface_module.md#return-values)

## [Synopsis](ce_mlag_interface_module.md#id1)

- Manages MLAG interface attributes on HUAWEI CloudEngine switches.

## [Parameters](ce_mlag_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **dfs_group_id**  string | ID of a DFS group.The value is 1.  Default: `"present"` |
| **eth_trunk_id**  string | Name of the local M-LAG interface. The value is ranging from 0 to 511. |
| **interface**  string | Name of the interface that enters the Error-Down state when the peer-link fails. The value is a string of 1 to 63 characters. |
| **mlag_error_down**  string | Configure the interface on the slave device to enter the Error-Down state.  Choices:   - `"enable"` - `"disable"` |
| **mlag_id**  string | ID of the M-LAG. The value is an integer that ranges from 1 to 2048. |
| **mlag_priority_id**  string | M-LAG global LACP system priority. The value is an integer ranging from 0 to 65535. The default value is 32768. |
| **mlag_system_id**  string | M-LAG global LACP system MAC address. The value is a string of 0 to 255 characters. The default value is the MAC address of the Ethernet port of MPU. |
| **state**  string | Specify desired state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](ce_mlag_interface_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_mlag_interface_module.md#id4)

```yaml+jinja
- name: Mlag interface module test
  hosts: cloudengine
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

  - name: Set interface mlag error down
    community.network.ce_mlag_interface:
      interface: 10GE2/0/1
      mlag_error_down: enable
      provider: "{{ cli }}"
  - name: Create mlag
    community.network.ce_mlag_interface:
      eth_trunk_id: 1
      dfs_group_id: 1
      mlag_id: 4
      provider: "{{ cli }}"
  - name: Set mlag global attribute
    community.network.ce_mlag_interface:
      mlag_system_id: 0020-1409-0407
      mlag_priority_id: 5
      provider: "{{ cli }}"
  - name: Set mlag interface attribute
    community.network.ce_mlag_interface:
      eth_trunk_id: 1
      mlag_system_id: 0020-1409-0400
      mlag_priority_id: 3
      provider: "{{ cli }}"
```

## [Return Values](ce_mlag_interface_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of aaa params after module execution  Returned: always  Sample: `{}` |
| **existing**  dictionary | k/v pairs of existing aaa server  Returned: always  Sample: `{"mlagErrorDownInfos": [{"dfsgroupId": "1", "portName": "Eth-Trunk1"}]}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: always  Sample: `{"interface": "eth-trunk1", "mlag_error_down": "disable", "state": "present"}` |
| **updates**  list / elements=string | command sent to the device  Returned: always  Sample: `{"interface eth-trunk1": null, "undo m-lag unpaired-port suspend": null}` |

### Authors

- Li Yanfeng (@QijunPan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
