---
collection: ansible
version: "8"
title: "community.network.pn_role module – CLI command to create/delete/modify role"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/pn_role_module.html
fetched_at: 2026-07-28T01:57:34+00:00
---
# community.network.pn_role module – CLI command to create/delete/modify role

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
> To use it in a playbook, specify: `community.network.pn_role`.

- [Synopsis](pn_role_module.md#synopsis)
- [Parameters](pn_role_module.md#parameters)
- [Examples](pn_role_module.md#examples)
- [Return Values](pn_role_module.md#return-values)

## [Synopsis](pn_role_module.md#id1)

- This module can be used to create, delete and modify user roles.

Aliases: network.netvisor.pn_role

## [Parameters](pn_role_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_access**  string | type of access.  **Choices:**   - `"read-only"` - `"read-write"` |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_delete_from_users**  boolean | delete from users.  **Choices:**   - `false` - `true` |
| **pn_name**  string / required | role name. |
| **pn_running_config**  boolean | display running configuration of switch.  **Choices:**   - `false` - `true` |
| **pn_scope**  string | local or fabric.  **Choices:**   - `"local"` - `"fabric"` |
| **pn_shell**  boolean | allow shell command.  **Choices:**   - `false` - `true` |
| **pn_sudo**  boolean | allow sudo from shell.  **Choices:**   - `false` - `true` |
| **state**  string / required | State the action to perform. Use `present` to create role and `absent` to delete role and `update` to modify role.  **Choices:**   - `"present"` - `"absent"` - `"update"` |

## [Examples](pn_role_module.md#id3)

```yaml+jinja
- name: Role create
  community.network.pn_role:
    pn_cliswitch: 'sw01'
    state: 'present'
    pn_name: 'foo'
    pn_scope: 'local'
    pn_access: 'read-only'

- name: Role delete
  community.network.pn_role:
    pn_cliswitch: 'sw01'
    state: 'absent'
    pn_name: 'foo'

- name: Role modify
  community.network.pn_role:
    pn_cliswitch: 'sw01'
    state: 'update'
    pn_name: 'foo'
    pn_access: 'read-write'
    pn_sudo: true
    pn_shell: true
```

## [Return Values](pn_role_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  **Returned:** always |
| **command**  string | the CLI command run on the target node.  **Returned:** always |
| **stderr**  list / elements=string | set of error responses from the role command.  **Returned:** on error |
| **stdout**  list / elements=string | set of responses from the role command.  **Returned:** always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
