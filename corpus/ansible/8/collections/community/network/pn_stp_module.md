---
collection: ansible
version: "8"
title: "community.network.pn_stp module – CLI command to modify stp"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/pn_stp_module.html
fetched_at: 2026-07-28T01:57:37+00:00
---
# community.network.pn_stp module – CLI command to modify stp

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
> To use it in a playbook, specify: `community.network.pn_stp`.

- [Synopsis](pn_stp_module.md#synopsis)
- [Parameters](pn_stp_module.md#parameters)
- [Examples](pn_stp_module.md#examples)
- [Return Values](pn_stp_module.md#return-values)

## [Synopsis](pn_stp_module.md#id1)

- This module can be used to modify Spanning Tree Protocol parameters.

Aliases: network.netvisor.pn_stp

## [Parameters](pn_stp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_bpdus_bridge_ports**  boolean | BPDU packets to bridge specific port.  **Choices:**   - `false` - `true` |
| **pn_bridge_id**  string | STP bridge id. |
| **pn_bridge_priority**  string | STP bridge priority.  **Default:** `"32768"` |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_enable**  boolean | enable or disable STP  **Choices:**   - `false` - `true` |
| **pn_forwarding_delay**  string | STP forwarding delay between 4 and 30 secs.  **Default:** `"15"` |
| **pn_hello_time**  string | STP hello time between 1 and 10 secs.  **Default:** `"2"` |
| **pn_max_age**  string | maximum age time between 6 and 40 secs.  **Default:** `"20"` |
| **pn_mst_config_name**  string | Name for MST Configuration Instance. |
| **pn_mst_max_hops**  string | maximum hop count for mstp bpdu.  **Default:** `"20"` |
| **pn_root_guard_wait_time**  string | root guard wait time between 0 and 300 secs. 0 to disable wait.  **Default:** `"20"` |
| **pn_stp_mode**  string | STP mode.  **Choices:**   - `"rstp"` - `"mstp"` |
| **state**  string / required | State the action to perform. Use `update` to stp.  **Choices:**   - `"update"` |

## [Examples](pn_stp_module.md#id3)

```yaml+jinja
- name: Modify stp
  community.network.pn_stp:
    pn_cliswitch: "sw01"
    state: "update"
    pn_hello_time: "3"
    pn_stp_mode: "rstp"
```

## [Return Values](pn_stp_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  **Returned:** always |
| **command**  string | the CLI command run on the target node.  **Returned:** always |
| **stderr**  list / elements=string | set of error responses from the stp command.  **Returned:** on error |
| **stdout**  list / elements=string | set of responses from the stp command.  **Returned:** always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
