---
collection: ansible
version: "8"
title: "community.network.pn_prefix_list_network module – CLI command to add/remove prefix-list-network"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/pn_prefix_list_network_module.html
fetched_at: 2026-07-28T01:57:33+00:00
---
# community.network.pn_prefix_list_network module – CLI command to add/remove prefix-list-network

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
> To use it in a playbook, specify: `community.network.pn_prefix_list_network`.

- [Synopsis](pn_prefix_list_network_module.md#synopsis)
- [Parameters](pn_prefix_list_network_module.md#parameters)
- [Examples](pn_prefix_list_network_module.md#examples)
- [Return Values](pn_prefix_list_network_module.md#return-values)

## [Synopsis](pn_prefix_list_network_module.md#id1)

- This module is used to add network associated with prefix list and remove networks associated with prefix list.

Aliases: network.netvisor.pn_prefix_list_network

## [Parameters](pn_prefix_list_network_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_name**  string | Prefix List Name. |
| **pn_netmask**  string | netmask of the network associated the prefix list. |
| **pn_network**  string | network associated with the prefix list. |
| **state**  string / required | State the action to perform. Use `present` to create prefix-list-network and `absent` to delete prefix-list-network.  **Choices:**   - `"present"` - `"absent"` |

## [Examples](pn_prefix_list_network_module.md#id3)

```yaml+jinja
- name: Prefix list network add
  community.network.pn_prefix_list_network:
    pn_cliswitch: "sw01"
    pn_name: "foo"
    pn_network: "172.16.3.1"
    pn_netmask: "24"
    state: "present"

- name: Prefix list network remove
  community.network.pn_prefix_list_network:
    pn_cliswitch: "sw01"
    state: "absent"
    pn_name: "foo"
    pn_network: "172.16.3.1"
    pn_netmask: "24"
```

## [Return Values](pn_prefix_list_network_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  **Returned:** always |
| **command**  string | the CLI command run on the target node.  **Returned:** always |
| **stderr**  list / elements=string | set of error responses from the prefix-list-network command.  **Returned:** on error |
| **stdout**  list / elements=string | set of responses from the prefix-list-network command.  **Returned:** always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
