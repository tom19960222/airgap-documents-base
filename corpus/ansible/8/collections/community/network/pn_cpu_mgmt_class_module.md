---
collection: ansible
version: "8"
title: "community.network.pn_cpu_mgmt_class module – CLI command to modify cpu-mgmt-class"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/pn_cpu_mgmt_class_module.html
fetched_at: 2026-07-28T01:57:24+00:00
---
# community.network.pn_cpu_mgmt_class module – CLI command to modify cpu-mgmt-class

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
> To use it in a playbook, specify: `community.network.pn_cpu_mgmt_class`.

- [Synopsis](pn_cpu_mgmt_class_module.md#synopsis)
- [Parameters](pn_cpu_mgmt_class_module.md#parameters)
- [Examples](pn_cpu_mgmt_class_module.md#examples)
- [Return Values](pn_cpu_mgmt_class_module.md#return-values)

## [Synopsis](pn_cpu_mgmt_class_module.md#id1)

- This module can we used to update mgmt port ingress policers.

Aliases: network.netvisor.pn_cpu_mgmt_class

## [Parameters](pn_cpu_mgmt_class_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_burst_size**  string | ingress traffic burst size (bytes) or default. |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_name**  string | mgmt port ingress traffic class.  **Choices:**   - `"arp"` - `"icmp"` - `"ssh"` - `"snmp"` - `"fabric"` - `"bcast"` - `"nfs"` - `"web"` - `"web-ssl"` - `"net-api"` |
| **pn_rate_limit**  string | ingress rate limit on mgmt port(bps) or unlimited. |
| **state**  string / required | State the action to perform. Use `update` to modify cpu-mgmt-class.  **Choices:**   - `"update"` |

## [Examples](pn_cpu_mgmt_class_module.md#id3)

```yaml+jinja
- name: Cpu mgmt class modify ingress policers
  community.network.pn_cpu_mgmt_class:
    pn_cliswitch: "sw01"
    state: "update"
    pn_name: "icmp"
    pn_rate_limit: "10000"
    pn_burst_size: "14000"

- name: Cpu mgmt class modify ingress policers
  community.network.pn_cpu_mgmt_class:
    pn_cliswitch: "sw01"
    state: "update"
    pn_name: "snmp"
    pn_burst_size: "8000"
    pn_rate_limit: "100000"

- name: Cpu mgmt class modify ingress policers
  community.network.pn_cpu_mgmt_class:
    pn_cliswitch: "sw01"
    state: "update"
    pn_name: "web"
    pn_rate_limit: "10000"
    pn_burst_size: "1000"
```

## [Return Values](pn_cpu_mgmt_class_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  **Returned:** always |
| **command**  string | the CLI command run on the target node.  **Returned:** always |
| **stderr**  list / elements=string | set of error responses from the cpu-mgmt-class command.  **Returned:** on error |
| **stdout**  list / elements=string | set of responses from the cpu-mgmt-class command.  **Returned:** always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
