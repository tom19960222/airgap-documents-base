---
collection: ansible
version: "8"
title: "community.network.pn_user module – CLI command to create/modify/delete user"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/pn_user_module.html
fetched_at: 2026-07-28T01:57:39+00:00
---
# community.network.pn_user module – CLI command to create/modify/delete user

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
> To use it in a playbook, specify: `community.network.pn_user`.

- [Synopsis](pn_user_module.md#synopsis)
- [Parameters](pn_user_module.md#parameters)
- [Examples](pn_user_module.md#examples)
- [Return Values](pn_user_module.md#return-values)

## [Synopsis](pn_user_module.md#id1)

- This module can be used to create a user and apply a role, update a user and delete a user.

Aliases: network.netvisor.pn_user

## [Parameters](pn_user_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_initial_role**  string | initial role for user. |
| **pn_name**  string | username. |
| **pn_password**  string | plain text password. |
| **pn_scope**  string | local or fabric.  **Choices:**   - `"local"` - `"fabric"` |
| **state**  string / required | State the action to perform. Use `present` to create user and `absent` to delete user `update` to update user.  **Choices:**   - `"present"` - `"absent"` - `"update"` |

## [Examples](pn_user_module.md#id3)

```yaml+jinja
- name: Create user
  community.network.pn_user:
    pn_cliswitch: "sw01"
    state: "present"
    pn_scope: "fabric"
    pn_password: "foo123"
    pn_name: "foo"

- name: Delete user
  community.network.pn_user:
    pn_cliswitch: "sw01"
    state: "absent"
    pn_name: "foo"

- name: Modify user
  community.network.pn_user:
    pn_cliswitch: "sw01"
    state: "update"
    pn_password: "test1234"
    pn_name: "foo"
```

## [Return Values](pn_user_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  **Returned:** always |
| **command**  string | the CLI command run on the target node.  **Returned:** always |
| **stderr**  list / elements=string | set of error responses from the user command.  **Returned:** on error |
| **stdout**  list / elements=string | set of responses from the user command.  **Returned:** always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
