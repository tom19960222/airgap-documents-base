---
collection: ansible
version: "8"
title: "theforeman.foreman.os_default_template module – Manage Default Template Associations To Operating Systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/os_default_template_module.html
fetched_at: 2026-07-28T02:56:18+00:00
---
# theforeman.foreman.os_default_template module – Manage Default Template Associations To Operating Systems

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
> see [Requirements](os_default_template_module.md#ansible-collections-theforeman-foreman-os-default-template-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.os_default_template`.

New in theforeman.foreman 1.0.0

- [Synopsis](os_default_template_module.md#synopsis)
- [Requirements](os_default_template_module.md#requirements)
- [Parameters](os_default_template_module.md#parameters)
- [Attributes](os_default_template_module.md#attributes)
- [Examples](os_default_template_module.md#examples)
- [Return Values](os_default_template_module.md#return-values)

## [Synopsis](os_default_template_module.md#id1)

- Manage OSDefaultTemplate Entities

Aliases: foreman_os_default_template

## [Requirements](os_default_template_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](os_default_template_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **operatingsystem**  string / required | Operating systems are looked up by their title which is composed as “<name> <major>.<minor>”.  You can omit the version part as long as you only have one operating system by that name. |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **provisioning_template**  string | name of provisioning template |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  `present_with_defaults` will ensure the entity exists, but won’t update existing ones  **Choices:**   - `"present"` ← (default) - `"present_with_defaults"` - `"absent"` |
| **template_kind**  string / required | name of the template kind  **Choices:**   - `"Bootdisk"` - `"cloud-init"` - `"finish"` - `"host_init_config"` - `"iPXE"` - `"job_template"` - `"kexec"` - `"POAP"` - `"provision"` - `"PXEGrub"` - `"PXEGrub2"` - `"PXELinux"` - `"registration"` - `"script"` - `"user_data"` - `"ZTP"` |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](os_default_template_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Examples](os_default_template_module.md#id5)

```yaml+jinja
- name: "Create an Association"
  theforeman.foreman.os_default_template:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    operatingsystem: "CoolOS"
    template_kind: "finish"
    provisioning_template: "CoolOS finish"
    state: present

- name: "Delete an Association"
  theforeman.foreman.os_default_template:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    operatingsystem: "CoolOS"
    template_kind: "finish"
    state: absent
```

## [Return Values](os_default_template_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  **Returned:** success |
| **os_default_templates**  list / elements=dictionary | List of operatingsystem default templates.  **Returned:** success |

### Authors

- Matthias M Dellweg (@mdellweg) ATIX AG

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
