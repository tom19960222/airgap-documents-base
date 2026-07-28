---
collection: ansible
version: "6"
title: "community.network.pn_stp_port module – CLI command to modify stp-port."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/pn_stp_port_module.html
fetched_at: 2026-07-27T17:19:32+00:00
---
# community.network.pn_stp_port module – CLI command to modify stp-port.

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
> To use it in a playbook, specify: `community.network.pn_stp_port`.

- [Synopsis](pn_stp_port_module.md#synopsis)
- [Parameters](pn_stp_port_module.md#parameters)
- [Examples](pn_stp_port_module.md#examples)
- [Return Values](pn_stp_port_module.md#return-values)

## [Synopsis](pn_stp_port_module.md#id1)

- This module can be used modify Spanning Tree Protocol (STP) parameters on ports.

## [Parameters](pn_stp_port_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_block**  boolean | Specify if a STP port blocks BPDUs.  Choices:   - `false` - `true` |
| **pn_bpdu_guard**  boolean | STP port BPDU guard.  Choices:   - `false` - `true` |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_cost**  string | STP port cost from 1 to 200000000.  Default: `"2000"` |
| **pn_edge**  boolean | STP port is an edge port.  Choices:   - `false` - `true` |
| **pn_filter**  boolean | STP port filters BPDUs.  Choices:   - `false` - `true` |
| **pn_port**  string | STP port. |
| **pn_priority**  string | STP port priority from 0 to 240.  Default: `"128"` |
| **pn_root_guard**  boolean | STP port Root guard.  Choices:   - `false` - `true` |
| **state**  string / required | State the action to perform. Use `update` to update stp-port.  Choices:   - `"update"` |

## [Examples](pn_stp_port_module.md#id3)

```yaml+jinja
- name: Modify stp port
  community.network.pn_stp_port:
    pn_cliswitch: "sw01"
    state: "update"
    pn_port: "1"
    pn_filter: True
    pn_priority: '144'

- name: Modify stp port
  community.network.pn_stp_port:
    pn_cliswitch: "sw01"
    state: "update"
    pn_port: "1"
    pn_cost: "200"

- name: Modify stp port
  community.network.pn_stp_port:
    pn_cliswitch: "sw01"
    state: "update"
    pn_port: "1"
    pn_edge: True
    pn_cost: "200"
```

## [Return Values](pn_stp_port_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  Returned: always |
| **command**  string | the CLI command run on the target node.  Returned: always |
| **stderr**  list / elements=string | set of error responses from the stp-port command.  Returned: on error |
| **stdout**  list / elements=string | set of responses from the stp-port command.  Returned: always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
