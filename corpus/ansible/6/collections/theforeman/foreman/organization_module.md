---
collection: ansible
version: "6"
title: "theforeman.foreman.organization module – Manage Organizations"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/organization_module.html
fetched_at: 2026-07-28T00:20:54+00:00
---
# theforeman.foreman.organization module – Manage Organizations

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
> see [Requirements](organization_module.md#ansible-collections-theforeman-foreman-organization-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.organization`.

New in theforeman.foreman 1.0.0

- [Synopsis](organization_module.md#synopsis)
- [Requirements](organization_module.md#requirements)
- [Parameters](organization_module.md#parameters)
- [Examples](organization_module.md#examples)
- [Return Values](organization_module.md#return-values)

## [Synopsis](organization_module.md#id1)

- Manage Organizations

## [Requirements](organization_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](organization_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  string | Description of the Organization |
| **label**  string | Label of the Organization |
| **name**  string / required | Name of the Organization |
| **parameters**  list / elements=dictionary | Entity domain specific host parameters |
| **name**  string / required | Name of the parameter |
| **parameter_type**  string | Type of the parameter  Choices:   - `"string"` ← (default) - `"boolean"` - `"integer"` - `"real"` - `"array"` - `"hash"` - `"yaml"` - `"json"` |
| **value**  any / required | Value of the parameter |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  Choices:   - `"present"` ← (default) - `"absent"` |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Examples](organization_module.md#id4)

```yaml+jinja
- name: "Create CI Organization"
  theforeman.foreman.organization:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "My Cool New Organization"
    state: present
```

## [Return Values](organization_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  Returned: success |
| **organizations**  list / elements=dictionary | List of organizations.  Returned: success |

### Authors

- Eric D Helms (@ehelms)
- Matthias M Dellweg (@mdellweg) ATIX AG

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
