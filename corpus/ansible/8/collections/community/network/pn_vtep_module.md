---
collection: ansible
version: "8"
title: "community.network.pn_vtep module – CLI command to create/delete vtep"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/pn_vtep_module.html
fetched_at: 2026-07-28T01:57:46+00:00
---
# community.network.pn_vtep module – CLI command to create/delete vtep

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
> To use it in a playbook, specify: `community.network.pn_vtep`.

- [Synopsis](pn_vtep_module.md#synopsis)
- [Parameters](pn_vtep_module.md#parameters)
- [Examples](pn_vtep_module.md#examples)
- [Return Values](pn_vtep_module.md#return-values)

## [Synopsis](pn_vtep_module.md#id1)

- This module can be used to create a vtep and delete a vtep.

Aliases: network.netvisor.pn_vtep

## [Parameters](pn_vtep_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_ip**  string | Primary IP address. |
| **pn_location**  string | switch name. |
| **pn_name**  string | vtep name. |
| **pn_switch_in_cluster**  boolean | Tells whether switch in cluster or not.  **Choices:**   - `false` - `true` ← (default) |
| **pn_virtual_ip**  string | Virtual/Secondary IP address. |
| **pn_vrouter_name**  string | name of the vrouter service. |
| **state**  string | vtep configuration command.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Examples](pn_vtep_module.md#id3)

```yaml+jinja
- name: Create vtep
  community.network.pn_vtep:
    pn_cliswitch: 'sw01'
    pn_name: 'foo'
    pn_vrouter_name: 'foo-vrouter'
    pn_ip: '22.22.22.2'
    pn_location: 'sw01'
    pn_virtual_ip: "22.22.22.1"

- name: Delete vtep
  community.network.pn_vtep:
    pn_cliswitch: 'sw01'
    state: 'absent'
    pn_name: 'foo'
```

## [Return Values](pn_vtep_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  **Returned:** always |
| **command**  string | the CLI command run on the target node.  **Returned:** always |
| **stderr**  list / elements=string | set of error responses from the vtep command.  **Returned:** on error |
| **stdout**  list / elements=string | set of responses from the vtep command.  **Returned:** always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
