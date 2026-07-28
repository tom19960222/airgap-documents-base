---
collection: ansible
version: "6"
title: "community.network.pn_prefix_list module – CLI command to create/delete prefix-list"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/pn_prefix_list_module.html
fetched_at: 2026-07-27T17:19:27+00:00
---
# community.network.pn_prefix_list module – CLI command to create/delete prefix-list

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
> To use it in a playbook, specify: `community.network.pn_prefix_list`.

- [Synopsis](pn_prefix_list_module.md#synopsis)
- [Parameters](pn_prefix_list_module.md#parameters)
- [Examples](pn_prefix_list_module.md#examples)
- [Return Values](pn_prefix_list_module.md#return-values)

## [Synopsis](pn_prefix_list_module.md#id1)

- This module can be used to create or delete prefix list.

## [Parameters](pn_prefix_list_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_name**  string / required | Prefix List Name. |
| **pn_scope**  string | scope of prefix-list.  Choices:   - `"local"` - `"fabric"` |
| **state**  string | State the action to perform. Use `present` to create prefix-list and `absent` to delete prefix-list.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Examples](pn_prefix_list_module.md#id3)

```yaml+jinja
- name: Create prefix list
  community.network.pn_prefix_list:
    pn_cliswitch: "sw01"
    pn_name: "foo"
    pn_scope: "local"
    state: "present"

- name: Delete prefix list
  community.network.pn_prefix_list:
    pn_cliswitch: "sw01"
    pn_name: "foo"
    state: "absent"
```

## [Return Values](pn_prefix_list_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  Returned: always |
| **command**  string | the CLI command run on the target node.  Returned: always |
| **stderr**  list / elements=string | set of error responses from the prefix-list command.  Returned: on error |
| **stdout**  list / elements=string | set of responses from the prefix-list command.  Returned: always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
