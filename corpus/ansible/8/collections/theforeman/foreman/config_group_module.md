---
collection: ansible
version: "8"
title: "theforeman.foreman.config_group module – Manage (Puppet) Config Groups"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/config_group_module.html
fetched_at: 2026-07-28T02:55:38+00:00
---
# theforeman.foreman.config_group module – Manage (Puppet) Config Groups

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
> see [Requirements](config_group_module.md#ansible-collections-theforeman-foreman-config-group-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.config_group`.

New in theforeman.foreman 1.0.0

- [Synopsis](config_group_module.md#synopsis)
- [Requirements](config_group_module.md#requirements)
- [Parameters](config_group_module.md#parameters)
- [Attributes](config_group_module.md#attributes)
- [Examples](config_group_module.md#examples)
- [Return Values](config_group_module.md#return-values)

## [Synopsis](config_group_module.md#id1)

- Create, update, and delete (Puppet) config groups

Aliases: foreman_config_group

## [Requirements](config_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](config_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **name**  string / required | The config group name |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **puppetclasses**  list / elements=string | List of puppet classes to include in this group |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **updated_name**  string | New config group name. When this parameter is set, the module will not be idempotent. |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](config_group_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Examples](config_group_module.md#id5)

```yaml+jinja
- name: create new config group
  theforeman.foreman.config_group:
    name: "My config group"
    puppetclasses:
      - ntp
      - mymodule::myclass
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: present
```

## [Return Values](config_group_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  **Returned:** success |
| **config_groups**  list / elements=dictionary | List of config groups.  **Returned:** success |

### Authors

- Baptiste Agasse (@bagasse)

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
