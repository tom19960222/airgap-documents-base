---
collection: ansible
version: "8"
title: "theforeman.foreman.hardware_model module – Manage Hardware Models"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/hardware_model_module.html
fetched_at: 2026-07-28T02:55:59+00:00
---
# theforeman.foreman.hardware_model module – Manage Hardware Models

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
> see [Requirements](hardware_model_module.md#ansible-collections-theforeman-foreman-hardware-model-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.hardware_model`.

New in theforeman.foreman 1.0.0

- [Synopsis](hardware_model_module.md#synopsis)
- [Requirements](hardware_model_module.md#requirements)
- [Parameters](hardware_model_module.md#parameters)
- [Attributes](hardware_model_module.md#attributes)
- [Examples](hardware_model_module.md#examples)
- [Return Values](hardware_model_module.md#return-values)

## [Synopsis](hardware_model_module.md#id1)

- Manage hardware models

Aliases: foreman_model

## [Requirements](hardware_model_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](hardware_model_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **hardware_model**  string | The class of CPU supplied in this machine.  This is primarily used by Sparc Solaris builds and can be left blank for other architectures. |
| **info**  string | General description of the hardware model |
| **name**  string / required | Name of the hardware model |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |
| **vendor_class**  string | The class of the machine as reported by the OpenBoot PROM.  This is primarily used by Solaris SPARC builds and can be left blank for other architectures. |

## [Attributes](hardware_model_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Examples](hardware_model_module.md#id5)

```yaml+jinja
- name: "Create ACME Laptop model"
  theforeman.foreman.hardware_model:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "acme laptop"
    info: "this is the acme laptop"
    state: present
```

## [Return Values](hardware_model_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  **Returned:** success |
| **hardware_models**  list / elements=dictionary | List of hardware models.  **Returned:** success |

### Authors

- Evgeni Golov (@evgeni)

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
