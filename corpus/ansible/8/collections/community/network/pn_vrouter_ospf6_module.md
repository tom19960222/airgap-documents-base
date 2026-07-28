---
collection: ansible
version: "8"
title: "community.network.pn_vrouter_ospf6 module – CLI command to add/remove vrouter-ospf6"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/pn_vrouter_ospf6_module.html
fetched_at: 2026-07-28T01:57:44+00:00
---
# community.network.pn_vrouter_ospf6 module – CLI command to add/remove vrouter-ospf6

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
> To use it in a playbook, specify: `community.network.pn_vrouter_ospf6`.

- [Synopsis](pn_vrouter_ospf6_module.md#synopsis)
- [Parameters](pn_vrouter_ospf6_module.md#parameters)
- [Examples](pn_vrouter_ospf6_module.md#examples)
- [Return Values](pn_vrouter_ospf6_module.md#return-values)

## [Synopsis](pn_vrouter_ospf6_module.md#id1)

- This module can be used to add interface ip to OSPF6 protocol or remove interface ip from OSPF6 protocol on vRouter.

Aliases: network.netvisor.pn_vrouter_ospf6

## [Parameters](pn_vrouter_ospf6_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_nic**  string | OSPF6 control for this interface. |
| **pn_ospf6_area**  string | area id for this interface in IPv4 address format. |
| **pn_vrouter_name**  string | name of service config. |
| **state**  string / required | State the action to perform. Use `present` to add vrouter-ospf6 and `absent` to remove interface from vrouter-ospf6.  **Choices:**   - `"present"` - `"absent"` |

## [Examples](pn_vrouter_ospf6_module.md#id3)

```yaml+jinja
- name: Add vrouter interface nic to ospf6
  community.network.pn_vrouter_ospf6:
    pn_cliswitch: "sw01"
    state: "present"
    pn_vrouter_name: "foo-vrouter"
    pn_nic: "eth0.4092"
    pn_ospf6_area: "0.0.0.0"

- name: Remove vrouter interface nic to ospf6
  community.network.pn_vrouter_ospf6:
    pn_cliswitch: "sw01"
    state: "absent"
    pn_vrouter_name: "foo-vrouter"
    pn_nic: "eth0.4092"
```

## [Return Values](pn_vrouter_ospf6_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  **Returned:** always |
| **command**  string | the CLI command run on the target node.  **Returned:** always |
| **stderr**  list / elements=string | set of error responses from the vrouter-ospf6 command.  **Returned:** on error |
| **stdout**  list / elements=string | set of responses from the vrouter-ospf6 command.  **Returned:** always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
