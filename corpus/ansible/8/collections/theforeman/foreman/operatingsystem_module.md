---
collection: ansible
version: "8"
title: "theforeman.foreman.operatingsystem module – Manage Operating Systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/operatingsystem_module.html
fetched_at: 2026-07-28T02:56:15+00:00
---
# theforeman.foreman.operatingsystem module – Manage Operating Systems

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
> see [Requirements](operatingsystem_module.md#ansible-collections-theforeman-foreman-operatingsystem-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.operatingsystem`.

New in theforeman.foreman 1.0.0

- [Synopsis](operatingsystem_module.md#synopsis)
- [Requirements](operatingsystem_module.md#requirements)
- [Parameters](operatingsystem_module.md#parameters)
- [Attributes](operatingsystem_module.md#attributes)
- [Examples](operatingsystem_module.md#examples)
- [Return Values](operatingsystem_module.md#return-values)

## [Synopsis](operatingsystem_module.md#id1)

- Manage Operating Systems

Aliases: foreman_operatingsystem

## [Requirements](operatingsystem_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](operatingsystem_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **architectures**  list / elements=string | architectures, the operating system can be installed on |
| **description**  string | Description of the Operating System |
| **major**  string | major version of the Operating System |
| **media**  list / elements=string | list of installation media |
| **minor**  string | minor version of the Operating System |
| **name**  string / required | Name of the Operating System |
| **os_family**  aliases: family  string | Distribution family of the Operating System  **Choices:**   - `"AIX"` - `"Altlinux"` - `"Archlinux"` - `"Coreos"` - `"Debian"` - `"Fcos"` - `"Freebsd"` - `"Gentoo"` - `"Junos"` - `"NXOS"` - `"Rancheros"` - `"Redhat"` - `"Rhcos"` - `"Solaris"` - `"Suse"` - `"VRP"` - `"Windows"` - `"Xenserver"` |
| **parameters**  list / elements=dictionary | Operating System specific host parameters |
| **name**  string / required | Name of the parameter |
| **parameter_type**  string | Type of the parameter  **Choices:**   - `"string"` ← (default) - `"boolean"` - `"integer"` - `"real"` - `"array"` - `"hash"` - `"yaml"` - `"json"` |
| **value**  any / required | Value of the parameter |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **password_hash**  string | hashing algorithm for passwd  **Choices:**   - `"MD5"` - `"SHA256"` - `"SHA512"` - `"Base64"` - `"Base64-Windows"` |
| **provisioning_templates**  list / elements=string | List of provisioning templates that are associated with the operating system.  Specify the full list of template names you want to associate with your OS.  For example [“Kickstart default”, “Kickstart default finish”, “Kickstart default iPXE”, “custom”].  After specifying the template associations, you can set the default association in  the [theforeman.foreman.os_default_template](os_default_template_module.md#ansible-collections-theforeman-foreman-os-default-template-module) module. |
| **ptables**  list / elements=string | list of partitioning tables |
| **release_name**  string | Release name of the operating system (recommended for debian) |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  `present_with_defaults` will ensure the entity exists, but won’t update existing ones  **Choices:**   - `"present"` ← (default) - `"present_with_defaults"` - `"absent"` |
| **updated_name**  string | New operating system name. When this parameter is set, the module will not be idempotent. |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](operatingsystem_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Examples](operatingsystem_module.md#id5)

```yaml+jinja
- name: "Create an Operating System"
  theforeman.foreman.operatingsystem:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: Debian
    release_name: stretch
    family: Debian
    major: 9
    parameters:
      - name: additional-packages
        value: python vim
    state: present

- name: "Ensure existence of an Operating System (provide default values)"
  theforeman.foreman.operatingsystem:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: Centos
    family: Redhat
    major: 7
    password_hash: SHA256
    state: present_with_defaults

- name: "Delete an Operating System"
  theforeman.foreman.operatingsystem:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: Debian
    family: Debian
    major: 9
    state: absent
```

## [Return Values](operatingsystem_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  **Returned:** success |
| **operatinsystems**  list / elements=dictionary | List of operatinsystems.  **Returned:** success |

### Authors

- Matthias M Dellweg (@mdellweg) ATIX AG
- Bernhard Hopfenmüller (@Fobhep) ATIX AG

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
