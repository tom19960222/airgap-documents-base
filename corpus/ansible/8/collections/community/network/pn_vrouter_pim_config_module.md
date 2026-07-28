---
collection: ansible
version: "8"
title: "community.network.pn_vrouter_pim_config module – CLI command to modify vrouter-pim-config"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/pn_vrouter_pim_config_module.html
fetched_at: 2026-07-28T01:57:45+00:00
---
# community.network.pn_vrouter_pim_config module – CLI command to modify vrouter-pim-config

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
> To use it in a playbook, specify: `community.network.pn_vrouter_pim_config`.

- [Synopsis](pn_vrouter_pim_config_module.md#synopsis)
- [Parameters](pn_vrouter_pim_config_module.md#parameters)
- [Examples](pn_vrouter_pim_config_module.md#examples)
- [Return Values](pn_vrouter_pim_config_module.md#return-values)

## [Synopsis](pn_vrouter_pim_config_module.md#id1)

- This module can be used to modify pim parameters.

Aliases: network.netvisor.pn_vrouter_pim_config

## [Parameters](pn_vrouter_pim_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_hello_interval**  string | hello interval in seconds. |
| **pn_querier_timeout**  string | igmp querier timeout in seconds. |
| **pn_query_interval**  string | igmp query interval in seconds. |
| **pn_vrouter_name**  string | name of service config. |
| **state**  string / required | State the action to perform. Use `update` to modify the vrouter-pim-config.  **Choices:**   - `"update"` |

## [Examples](pn_vrouter_pim_config_module.md#id3)

```yaml+jinja
- name: Pim config modify
  community.network.pn_vrouter_pim_config:
    pn_cliswitch: '192.168.1.1'
    pn_query_interval: '10'
    pn_querier_timeout: '30'
    state: 'update'
    pn_vrouter_name: 'ansible-spine1-vrouter'
```

## [Return Values](pn_vrouter_pim_config_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  **Returned:** always |
| **command**  string | the CLI command run on the target node.  **Returned:** always |
| **stderr**  list / elements=string | set of error responses from the vrouter-pim-config command.  **Returned:** on error |
| **stdout**  list / elements=string | set of responses from the vrouter-pim-config command.  **Returned:** always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
