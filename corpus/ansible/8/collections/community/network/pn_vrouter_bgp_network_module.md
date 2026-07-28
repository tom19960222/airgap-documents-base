---
collection: ansible
version: "8"
title: "community.network.pn_vrouter_bgp_network module – CLI command to add/remove vrouter-bgp-network"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/pn_vrouter_bgp_network_module.html
fetched_at: 2026-07-28T01:57:41+00:00
---
# community.network.pn_vrouter_bgp_network module – CLI command to add/remove vrouter-bgp-network

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
> To use it in a playbook, specify: `community.network.pn_vrouter_bgp_network`.

- [Synopsis](pn_vrouter_bgp_network_module.md#synopsis)
- [Parameters](pn_vrouter_bgp_network_module.md#parameters)
- [Examples](pn_vrouter_bgp_network_module.md#examples)
- [Return Values](pn_vrouter_bgp_network_module.md#return-values)

## [Synopsis](pn_vrouter_bgp_network_module.md#id1)

- This module can be used to add Border Gateway Protocol network to a vRouter and remove Border Gateway Protocol network from a vRouter.

Aliases: network.netvisor.pn_vrouter_bgp_network

## [Parameters](pn_vrouter_bgp_network_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_netmask**  string | BGP network mask. |
| **pn_network**  string | IP address for BGP network. |
| **pn_vrouter_name**  string | name of service config. |
| **state**  string / required | State the action to perform. Use `present` to add bgp network and `absent` to remove bgp network.  **Choices:**   - `"present"` - `"absent"` |

## [Examples](pn_vrouter_bgp_network_module.md#id3)

```yaml+jinja
- name:  Add network to bgp
  community.network.pn_vrouter_bgp_network:
    pn_cliswitch: "sw01"
    state: "present"
    pn_vrouter_name: "foo-vrouter"
    pn_network: '10.10.10.10'
    pn_netmask: '31'

- name:  Remove network from bgp
  community.network.pn_vrouter_bgp_network:
    pn_cliswitch: "sw01"
    state: "absent"
    pn_vrouter_name: "foo-vrouter"
    pn_network: '10.10.10.10'
```

## [Return Values](pn_vrouter_bgp_network_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  **Returned:** always |
| **command**  string | the CLI command run on the target node.  **Returned:** always |
| **stderr**  list / elements=string | set of error responses from the vrouter-bgp-network command.  **Returned:** on error |
| **stdout**  list / elements=string | set of responses from the vrouter-bgp-network command.  **Returned:** always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
