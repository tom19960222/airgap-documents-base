---
collection: ansible
version: "8"
title: "community.network.pn_snmp_trap_sink module – CLI command to create/delete snmp-trap-sink"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/pn_snmp_trap_sink_module.html
fetched_at: 2026-07-28T01:57:36+00:00
---
# community.network.pn_snmp_trap_sink module – CLI command to create/delete snmp-trap-sink

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
> To use it in a playbook, specify: `community.network.pn_snmp_trap_sink`.

- [Synopsis](pn_snmp_trap_sink_module.md#synopsis)
- [Parameters](pn_snmp_trap_sink_module.md#parameters)
- [Examples](pn_snmp_trap_sink_module.md#examples)
- [Return Values](pn_snmp_trap_sink_module.md#return-values)

## [Synopsis](pn_snmp_trap_sink_module.md#id1)

- This module can be used to create a SNMP trap sink and delete a SNMP trap sink.

Aliases: network.netvisor.pn_snmp_trap_sink

## [Parameters](pn_snmp_trap_sink_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_community**  string | community type. |
| **pn_dest_host**  string | destination host. |
| **pn_dest_port**  string | destination port.  **Default:** `"162"` |
| **pn_type**  string | trap type.  **Choices:**   - `"TRAP_TYPE_V1_TRAP"` - `"TRAP_TYPE_V2C_TRAP"` ← (default) - `"TRAP_TYPE_V2_INFORM"` |
| **state**  string / required | State the action to perform. Use `present` to create snmp-trap-sink and `absent` to delete snmp-trap-sink.  **Choices:**   - `"present"` - `"absent"` |

## [Examples](pn_snmp_trap_sink_module.md#id3)

```yaml+jinja
- name: Snmp trap sink functionality
  community.network.pn_snmp_trap_sink:
    pn_cliswitch: "sw01"
    state: "present"
    pn_community: "foo"
    pn_type: "TRAP_TYPE_V2_INFORM"
    pn_dest_host: "192.168.67.8"

- name: Snmp trap sink functionality
  community.network.pn_snmp_trap_sink:
    pn_cliswitch: "sw01"
    state: "absent"
    pn_community: "foo"
    pn_type: "TRAP_TYPE_V2_INFORM"
    pn_dest_host: "192.168.67.8"
```

## [Return Values](pn_snmp_trap_sink_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  **Returned:** always |
| **command**  string | the CLI command run on the target node.  **Returned:** always |
| **stderr**  list / elements=string | set of error responses from the snmp-trap-sink command.  **Returned:** on error |
| **stdout**  list / elements=string | set of responses from the snmp-trap-sink command.  **Returned:** always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
