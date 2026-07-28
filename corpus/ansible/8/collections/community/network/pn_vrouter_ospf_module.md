---
collection: ansible
version: "8"
title: "community.network.pn_vrouter_ospf module – CLI command to add/remove vrouter-ospf"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/pn_vrouter_ospf_module.html
fetched_at: 2026-07-28T01:57:43+00:00
---
# community.network.pn_vrouter_ospf module – CLI command to add/remove vrouter-ospf

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
> To use it in a playbook, specify: `community.network.pn_vrouter_ospf`.

- [Synopsis](pn_vrouter_ospf_module.md#synopsis)
- [Parameters](pn_vrouter_ospf_module.md#parameters)
- [Examples](pn_vrouter_ospf_module.md#examples)
- [Return Values](pn_vrouter_ospf_module.md#return-values)

## [Synopsis](pn_vrouter_ospf_module.md#id1)

- This module can be used to add OSPF protocol to vRouter and remove OSPF protocol from a vRouter

Aliases: network.netvisor.pn_vrouter_ospf

## [Parameters](pn_vrouter_ospf_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_netmask**  string | OSPF network IP address netmask. |
| **pn_network**  string / required | OSPF network IP address. |
| **pn_ospf_area**  string | stub area number for the configuration. |
| **pn_vrouter_name**  string / required | name of service config. |
| **state**  string | vrouter-ospf configuration command.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Examples](pn_vrouter_ospf_module.md#id3)

```yaml+jinja
- name: Add OSPF to vRouter
  community.network.pn_vrouter_ospf:
    state: 'present'
    pn_vrouter_name: 'sw01-vrouter'
    pn_network: '105.104.104.1'
    pn_netmask: '24'
    pn_ospf_area: '0'
- name: "Remove OSPF to vRouter"
  community.network.pn_vrouter_ospf:
    state: 'absent'
    pn_vrouter_name: 'sw01-vrouter'
    pn_network: '105.104.104.1'
```

## [Return Values](pn_vrouter_ospf_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  **Returned:** always |
| **command**  string | the CLI command run on the target node.  **Returned:** always |
| **stderr**  list / elements=string | set of error responses from the vrouter-ospf command.  **Returned:** on error |
| **stdout**  list / elements=string | set of responses from the vrouter-ospf command.  **Returned:** always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
