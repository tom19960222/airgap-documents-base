---
collection: ansible
version: "8"
title: "community.network.pn_access_list module – CLI command to create/delete access-list"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/pn_access_list_module.html
fetched_at: 2026-07-28T01:57:19+00:00
---
# community.network.pn_access_list module – CLI command to create/delete access-list

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
> To use it in a playbook, specify: `community.network.pn_access_list`.

- [Synopsis](pn_access_list_module.md#synopsis)
- [Parameters](pn_access_list_module.md#parameters)
- [Examples](pn_access_list_module.md#examples)
- [Return Values](pn_access_list_module.md#return-values)

## [Synopsis](pn_access_list_module.md#id1)

- This module can be used to create and delete an access list.

Aliases: network.netvisor.pn_access_list

## [Parameters](pn_access_list_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_name**  string | Access List Name. |
| **pn_scope**  string | scope. Available valid values - local or fabric.  **Choices:**   - `"local"` - `"fabric"` |
| **state**  string / required | State the action to perform. Use ‘present’ to create access-list and ‘absent’ to delete access-list.  **Choices:**   - `"present"` - `"absent"` |

## [Examples](pn_access_list_module.md#id3)

```yaml+jinja
- name: Access list functionality
  community.network.pn_access_list:
    pn_cliswitch: "sw01"
    pn_name: "foo"
    pn_scope: "local"
    state: "present"

- name: Access list functionality
  community.network.pn_access_list:
    pn_cliswitch: "sw01"
    pn_name: "foo"
    pn_scope: "local"
    state: "absent"

- name: Access list functionality
  community.network.pn_access_list:
    pn_cliswitch: "sw01"
    pn_name: "foo"
    pn_scope: "fabric"
    state: "present"
```

## [Return Values](pn_access_list_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  **Returned:** always |
| **command**  string | the CLI command run on the target node.  **Returned:** always |
| **stderr**  list / elements=string | set of error responses from the access-list command.  **Returned:** on error |
| **stdout**  list / elements=string | set of responses from the access-list command.  **Returned:** always |

### Authors

- Pluribus Networks (@amitsi)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
