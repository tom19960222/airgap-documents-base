---
collection: ansible
version: "6"
title: "theforeman.foreman.role module – Manage Roles"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/role_module.html
fetched_at: 2026-07-28T00:21:05+00:00
---
# theforeman.foreman.role module – Manage Roles

> **Note:**
>
> This module is part of the [theforeman.foreman collection](https://galaxy.ansible.com/theforeman/foreman) (version 3.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install theforeman.foreman`.
> You need further requirements to be able to use this module,
> see [Requirements](role_module.md#ansible-collections-theforeman-foreman-role-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.role`.

New in theforeman.foreman 1.0.0

- [Synopsis](role_module.md#synopsis)
- [Requirements](role_module.md#requirements)
- [Parameters](role_module.md#parameters)
- [Examples](role_module.md#examples)
- [Return Values](role_module.md#return-values)

## [Synopsis](role_module.md#id1)

- Create, update, and delete Roles

## [Requirements](role_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](role_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  string | Description of the role |
| **filters**  list / elements=dictionary | Filters with permissions for this role |
| **permissions**  list / elements=string / required | List of permissions |
| **search**  string | Filter condition for the resources |
| **locations**  list / elements=string | List of locations the entity should be assigned to |
| **name**  string / required | The name of the role |
| **organizations**  list / elements=string | List of organizations the entity should be assigned to |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  Choices:   - `"present"` ← (default) - `"absent"` |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Examples](role_module.md#id4)

```yaml+jinja
- name: role
  theforeman.foreman.role:
    name: "Provisioner"
    description: "Only provision on libvirt"
    locations:
      - "Uppsala"
    organizations:
      - "ACME"
    filters:
      - permissions:
          - view_hosts
        search: "owner_type = Usergroup and owner_id = 4"
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: present
```

## [Return Values](role_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  Returned: success |
| **roles**  list / elements=dictionary | List of roles.  Returned: success |

### Authors

- Christoffer Reijer (@ephracis) Basalt AB

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
