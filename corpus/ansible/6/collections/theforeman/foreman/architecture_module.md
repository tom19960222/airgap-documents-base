---
collection: ansible
version: "6"
title: "theforeman.foreman.architecture module – Manage Architectures"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/architecture_module.html
fetched_at: 2026-07-28T00:20:28+00:00
---
# theforeman.foreman.architecture module – Manage Architectures

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
> see [Requirements](architecture_module.md#ansible-collections-theforeman-foreman-architecture-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.architecture`.

New in theforeman.foreman 1.0.0

- [Synopsis](architecture_module.md#synopsis)
- [Requirements](architecture_module.md#requirements)
- [Parameters](architecture_module.md#parameters)
- [Examples](architecture_module.md#examples)
- [Return Values](architecture_module.md#return-values)

## [Synopsis](architecture_module.md#id1)

- Create, update, and delete Architectures

## [Requirements](architecture_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](architecture_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **name**  string / required | Name of architecture |
| **operatingsystems**  list / elements=string | List of operating systems the entity should be assigned to.  Operating systems are looked up by their title which is composed as “<name> <major>.<minor>”.  You can omit the version part as long as you only have one operating system by that name. |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  Choices:   - `"present"` ← (default) - `"absent"` |
| **updated_name**  string | New architecture name. When this parameter is set, the module will not be idempotent. |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Examples](architecture_module.md#id4)

```yaml+jinja
- name: "Create an Architecture"
  theforeman.foreman.architecture:
    name: "i386"
    operatingsystems:
      - "TestOS1"
      - "TestOS2"
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: present

- name: "Update an Architecture"
  theforeman.foreman.architecture:
    name: "i386"
    operatingsystems:
      - "TestOS3"
      - "TestOS4"
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: present

- name: "Delete an Architecture"
  theforeman.foreman.architecture:
    name: "i386"
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: absent
```

## [Return Values](architecture_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  Returned: success |
| **architectures**  list / elements=dictionary | List of architectures.  Returned: success |
| **id**  integer | Database id of the architecture.  Returned: success |
| **name**  string | Name of the architecture.  Returned: success |
| **operatinsystem_ids**  list / elements=integer | Database ids of associated operatingsystems.  Returned: success |

### Authors

- Manisha Singhal (@Manisha15) ATIX AG

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
