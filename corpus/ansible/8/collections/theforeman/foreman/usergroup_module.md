---
collection: ansible
version: "8"
title: "theforeman.foreman.usergroup module – Manage User Groups"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/usergroup_module.html
fetched_at: 2026-07-28T02:56:48+00:00
---
# theforeman.foreman.usergroup module – Manage User Groups

> **Note:**
>
> This module is part of the [theforeman.foreman collection](https://galaxy.ansible.com/ui/repo/published/theforeman/foreman/) (version 3.15.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install theforeman.foreman`.
> You need further requirements to be able to use this module,
> see [Requirements](usergroup_module.md#ansible-collections-theforeman-foreman-usergroup-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.usergroup`.

New in theforeman.foreman 1.0.0

- [Synopsis](usergroup_module.md#synopsis)
- [Requirements](usergroup_module.md#requirements)
- [Parameters](usergroup_module.md#parameters)
- [Attributes](usergroup_module.md#attributes)
- [Examples](usergroup_module.md#examples)
- [Return Values](usergroup_module.md#return-values)

## [Synopsis](usergroup_module.md#id1)

- Create, update, and delete user groups

Aliases: foreman_usergroup

## [Requirements](usergroup_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](usergroup_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **admin**  boolean | Whether or not the users in this group are administrators  **Choices:**   - `false` ← (default) - `true` |
| **name**  string / required | Name of the group |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **roles**  list / elements=string | List of roles assigned to the group |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **updated_name**  string | New user group name. When this parameter is set, the module will not be idempotent. |
| **usergroups**  list / elements=string | List of other groups assigned to the group |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **users**  list / elements=string | List of users assigned to the group |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](usergroup_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Examples](usergroup_module.md#id5)

```yaml+jinja
- name: Create a user group
  theforeman.foreman.usergroup:
    name: test
    admin: false
    roles:
      - Manager
    users:
      - myuser1
      - myuser2
    usergroups:
      - mynestedgroup
    state: present
```

## [Return Values](usergroup_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  **Returned:** success |
| **usergroups**  list / elements=dictionary | List of usergroups.  **Returned:** success |

### Authors

- Baptiste Agasse (@bagasse)

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
