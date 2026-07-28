---
collection: ansible
version: "8"
title: "community.network.pn_dscp_map_pri_map module – CLI command to modify dscp-map-pri-map"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/pn_dscp_map_pri_map_module.html
fetched_at: 2026-07-28T01:57:26+00:00
---
# community.network.pn_dscp_map_pri_map module – CLI command to modify dscp-map-pri-map

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
> To use it in a playbook, specify: `community.network.pn_dscp_map_pri_map`.

- [Synopsis](pn_dscp_map_pri_map_module.md#synopsis)
- [Parameters](pn_dscp_map_pri_map_module.md#parameters)
- [Examples](pn_dscp_map_pri_map_module.md#examples)
- [Return Values](pn_dscp_map_pri_map_module.md#return-values)

## [Synopsis](pn_dscp_map_pri_map_module.md#id1)

- This module can be used to update priority mappings in tables.

Aliases: network.netvisor.pn_dscp_map_pri_map

## [Parameters](pn_dscp_map_pri_map_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_dsmap**  string | DSCP value(s). |
| **pn_name**  string | Name for the DSCP map. |
| **pn_pri**  string | CoS priority. |
| **state**  string / required | State the action to perform. Use `update` to modify the dscp-map-pri-map.  **Choices:**   - `"update"` |

## [Examples](pn_dscp_map_pri_map_module.md#id3)

```yaml+jinja
- name: Dscp map pri map modify
  community.network.pn_dscp_map_pri_map:
    pn_cliswitch: 'sw01'
    state: 'update'
    pn_name: 'foo'
    pn_pri: '0'
    pn_dsmap: '40'

- name: Dscp map pri map modify
  community.network.pn_dscp_map_pri_map:
    pn_cliswitch: 'sw01'
    state: 'update'
    pn_name: 'foo'
    pn_pri: '1'
    pn_dsmap: '8,10,12,14'
```

## [Return Values](pn_dscp_map_pri_map_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  **Returned:** always |
| **command**  string | the CLI command run on the target node.  **Returned:** always |
| **stderr**  list / elements=string | set of error responses from the dscp-map-pri-map command.  **Returned:** on error |
| **stdout**  list / elements=string | set of responses from the dscp-map-pri-map command.  **Returned:** always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
