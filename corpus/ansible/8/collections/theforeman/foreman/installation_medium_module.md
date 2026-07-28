---
collection: ansible
version: "8"
title: "theforeman.foreman.installation_medium module – Manage Installation Media"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/installation_medium_module.html
fetched_at: 2026-07-28T02:56:10+00:00
---
# theforeman.foreman.installation_medium module – Manage Installation Media

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
> see [Requirements](installation_medium_module.md#ansible-collections-theforeman-foreman-installation-medium-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.installation_medium`.

New in theforeman.foreman 1.0.0

- [Synopsis](installation_medium_module.md#synopsis)
- [Requirements](installation_medium_module.md#requirements)
- [Parameters](installation_medium_module.md#parameters)
- [Attributes](installation_medium_module.md#attributes)
- [Examples](installation_medium_module.md#examples)
- [Return Values](installation_medium_module.md#return-values)

## [Synopsis](installation_medium_module.md#id1)

- Create, update, and delete Installation Media

Aliases: foreman_installation_medium

## [Requirements](installation_medium_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](installation_medium_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **locations**  list / elements=string | List of locations the entity should be assigned to |
| **name**  string / required | The full installation medium name.  The special name “\*” (only possible as parameter) is used to perform bulk actions (modify, delete) on all existing partition tables. |
| **operatingsystems**  list / elements=string | List of operating systems the entity should be assigned to.  Operating systems are looked up by their title which is composed as “<name> <major>.<minor>”.  You can omit the version part as long as you only have one operating system by that name. |
| **organizations**  list / elements=string | List of organizations the entity should be assigned to |
| **os_family**  string | The OS family the template shall be assigned with.  If no os_family is set but a operatingsystem, the value will be derived from it.  **Choices:**   - `"AIX"` - `"Altlinux"` - `"Archlinux"` - `"Coreos"` - `"Debian"` - `"Fcos"` - `"Freebsd"` - `"Gentoo"` - `"Junos"` - `"NXOS"` - `"Rancheros"` - `"Redhat"` - `"Rhcos"` - `"Solaris"` - `"Suse"` - `"VRP"` - `"Windows"` - `"Xenserver"` |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **path**  string | Path to the installation medium |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  `present_with_defaults` will ensure the entity exists, but won’t update existing ones  **Choices:**   - `"present"` ← (default) - `"present_with_defaults"` - `"absent"` |
| **updated_name**  string | New full installation medium name. When this parameter is set, the module will not be idempotent. |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](installation_medium_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Examples](installation_medium_module.md#id5)

```yaml+jinja
- name: create new debian medium
  theforeman.foreman.installation_medium:
    name: "wheezy"
    locations:
      - "Munich"
    organizations:
      - "ACME"
    operatingsystems:
      - "Debian"
    path: "http://debian.org/mirror/"
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: present
```

## [Return Values](installation_medium_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  **Returned:** success |
| **media**  list / elements=dictionary | List of installation media.  **Returned:** success |

### Authors

- Manuel Bonk(@manuelbonk) ATIX AG

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
