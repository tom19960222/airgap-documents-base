---
collection: ansible
version: "8"
title: "community.network.pn_vrouter_interface_ip module – CLI command to add/remove vrouter-interface-ip"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/pn_vrouter_interface_ip_module.html
fetched_at: 2026-07-28T01:57:42+00:00
---
# community.network.pn_vrouter_interface_ip module – CLI command to add/remove vrouter-interface-ip

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
> To use it in a playbook, specify: `community.network.pn_vrouter_interface_ip`.

- [Synopsis](pn_vrouter_interface_ip_module.md#synopsis)
- [Parameters](pn_vrouter_interface_ip_module.md#parameters)
- [Examples](pn_vrouter_interface_ip_module.md#examples)
- [Return Values](pn_vrouter_interface_ip_module.md#return-values)

## [Synopsis](pn_vrouter_interface_ip_module.md#id1)

- This module can be used to add an IP address on interface from a vRouter or remove an IP address on interface from a vRouter.

Aliases: network.netvisor.pn_vrouter_interface_ip

## [Parameters](pn_vrouter_interface_ip_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_bd**  string | interface Bridge Domain. |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_ip**  string | IP address. |
| **pn_netmask**  string | netmask. |
| **pn_nic**  string | virtual NIC assigned to interface. |
| **pn_vnet**  string | interface VLAN VNET. |
| **pn_vrouter_name**  string | name of service config. |
| **state**  string / required | State the action to perform. Use `present` to addvrouter-interface-ip and `absent` to remove vrouter-interface-ip.  **Choices:**   - `"present"` - `"absent"` |

## [Examples](pn_vrouter_interface_ip_module.md#id3)

```yaml+jinja
- name: Add vrouter interface to nic
  community.network.pn_vrouter_interface_ip:
    state: "present"
    pn_cliswitch: "sw01"
    pn_vrouter_name: "foo-vrouter"
    pn_ip: "2620:0:1651:1::30"
    pn_netmask: "127"
    pn_nic: "eth0.4092"

- name: Remove vrouter interface to nic
  community.network.pn_vrouter_interface_ip:
    state: "absent"
    pn_cliswitch: "sw01"
    pn_vrouter_name: "foo-vrouter"
    pn_ip: "2620:0:1651:1::30"
    pn_nic: "eth0.4092"
```

## [Return Values](pn_vrouter_interface_ip_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  **Returned:** always |
| **command**  string | the CLI command run on the target node.  **Returned:** always |
| **stderr**  list / elements=string | set of error responses from the vrouter-interface-ip command.  **Returned:** on error |
| **stdout**  list / elements=string | set of responses from the vrouter-interface-ip command.  **Returned:** always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
