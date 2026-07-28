---
collection: ansible
version: "8"
title: "theforeman.foreman.global_parameter module – Manage Global Parameters"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/global_parameter_module.html
fetched_at: 2026-07-28T02:55:58+00:00
---
# theforeman.foreman.global_parameter module – Manage Global Parameters

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
> see [Requirements](global_parameter_module.md#ansible-collections-theforeman-foreman-global-parameter-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.global_parameter`.

New in theforeman.foreman 1.0.0

- [Synopsis](global_parameter_module.md#synopsis)
- [Requirements](global_parameter_module.md#requirements)
- [Parameters](global_parameter_module.md#parameters)
- [Attributes](global_parameter_module.md#attributes)
- [Notes](global_parameter_module.md#notes)
- [Examples](global_parameter_module.md#examples)
- [Return Values](global_parameter_module.md#return-values)

## [Synopsis](global_parameter_module.md#id1)

- Manage Global Parameter Entities

Aliases: foreman_global_parameter

## [Requirements](global_parameter_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](global_parameter_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **hidden_value**  boolean | Whether the value should be hidden in the GUI  **Choices:**   - `false` - `true` |
| **name**  string / required | Name of the Global Parameter |
| **parameter_type**  string | Type of value  **Choices:**   - `"string"` ← (default) - `"boolean"` - `"integer"` - `"real"` - `"array"` - `"hash"` - `"yaml"` - `"json"` |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  `present_with_defaults` will ensure the entity exists, but won’t update existing ones  **Choices:**   - `"present"` ← (default) - `"present_with_defaults"` - `"absent"` |
| **updated_name**  string | New name of the Global Parameter. When this parameter is set, the module will not be idempotent. |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |
| **value**  any | Value of the Global Parameter |

## [Attributes](global_parameter_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Notes](global_parameter_module.md#id5)

> **Note:**
>
> - The *parameter_type* only has an effect on Foreman >= 1.22

## [Examples](global_parameter_module.md#id6)

```yaml+jinja
- name: "Create a Global Parameter"
  theforeman.foreman.global_parameter:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "TheAnswer"
    value: "42"
    state: present_with_defaults

- name: "Update a Global Parameter"
  theforeman.foreman.global_parameter:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "TheAnswer"
    value: "43"
    state: present

- name: "Delete a Global Parameter"
  theforeman.foreman.global_parameter:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "TheAnswer"
    state: absent
```

## [Return Values](global_parameter_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  **Returned:** success |
| **global_parameters**  list / elements=dictionary | List of global parameters.  **Returned:** success |

### Authors

- Bernhard Hopfenmueller (@Fobhep) ATIX AG
- Matthias Dellweg (@mdellweg) ATIX AG
- Manisha Singhal (@manisha15) ATIX AG

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
