---
collection: ansible
version: "8"
title: "community.network.pn_snmp_community module – CLI command to create/modify/delete snmp-community"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/pn_snmp_community_module.html
fetched_at: 2026-07-28T01:57:35+00:00
---
# community.network.pn_snmp_community module – CLI command to create/modify/delete snmp-community

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
> To use it in a playbook, specify: `community.network.pn_snmp_community`.

- [Synopsis](pn_snmp_community_module.md#synopsis)
- [Parameters](pn_snmp_community_module.md#parameters)
- [Examples](pn_snmp_community_module.md#examples)
- [Return Values](pn_snmp_community_module.md#return-values)

## [Synopsis](pn_snmp_community_module.md#id1)

- This module can be used to create SNMP communities for SNMPv1 or delete SNMP communities for SNMPv1 or modify SNMP communities for SNMPv1.

Aliases: network.netvisor.pn_snmp_community

## [Parameters](pn_snmp_community_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_community_string**  string | community name. |
| **pn_community_type**  string | community type.  **Choices:**   - `"read-only"` - `"read-write"` |
| **state**  string / required | State the action to perform. Use `present` to create snmp-community and `absent` to delete snmp-community `update` to update snmp-community.  **Choices:**   - `"present"` - `"absent"` - `"update"` |

## [Examples](pn_snmp_community_module.md#id3)

```yaml+jinja
- name: Create snmp community
  community.network.pn_snmp_community:
    pn_cliswitch: "sw01"
    state: "present"
    pn_community_string: "foo"
    pn_community_type: "read-write"

- name: Delete snmp community
  community.network.pn_snmp_community:
    pn_cliswitch: "sw01"
    state: "absent"
    pn_community_string: "foo"

- name: Modify snmp community
  community.network.pn_snmp_community:
    pn_cliswitch: "sw01"
    state: "update"
    pn_community_string: "foo"
    pn_community_type: "read-only"
```

## [Return Values](pn_snmp_community_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  **Returned:** always |
| **command**  string | the CLI command run on the target node.  **Returned:** always |
| **stderr**  list / elements=string | set of error responses from the snmp-community command.  **Returned:** on error |
| **stdout**  list / elements=string | set of responses from the snmp-community command.  **Returned:** always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
