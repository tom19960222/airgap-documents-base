---
collection: ansible
version: "6"
title: "theforeman.foreman.realm module – Manage Realms"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/realm_module.html
fetched_at: 2026-07-28T00:20:59+00:00
---
# theforeman.foreman.realm module – Manage Realms

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
> see [Requirements](realm_module.md#ansible-collections-theforeman-foreman-realm-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.realm`.

New in theforeman.foreman 1.0.0

- [Synopsis](realm_module.md#synopsis)
- [Requirements](realm_module.md#requirements)
- [Parameters](realm_module.md#parameters)
- [Examples](realm_module.md#examples)
- [Return Values](realm_module.md#return-values)

## [Synopsis](realm_module.md#id1)

- Manage Realms

## [Requirements](realm_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](realm_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **locations**  list / elements=string | List of locations the entity should be assigned to |
| **name**  string / required | Name of the realm |
| **organizations**  list / elements=string | List of organizations the entity should be assigned to |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **realm_proxy**  string / required | Proxy to use for this realm |
| **realm_type**  string / required | Realm type  Choices:   - `"Red Hat Identity Management"` - `"FreeIPA"` - `"Active Directory"` |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  Choices:   - `"present"` ← (default) - `"absent"` |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Examples](realm_module.md#id4)

```yaml+jinja
- name: "Create EXAMPLE.LOCAL Realm"
  theforeman.foreman.realm:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "EXAMPLE.COM"
    realm_proxy: "foreman.example.com"
    realm_type: "Red Hat Identity Management"
    state: present
```

## [Return Values](realm_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  Returned: success |
| **realms**  list / elements=dictionary | List of realms.  Returned: success |

### Authors

- Lester R Claudio (@claudiol1)

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
