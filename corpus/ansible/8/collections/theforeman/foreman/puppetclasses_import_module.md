---
collection: ansible
version: "8"
title: "theforeman.foreman.puppetclasses_import module – Import Puppet Classes from a Proxy"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/puppetclasses_import_module.html
fetched_at: 2026-07-28T02:56:23+00:00
---
# theforeman.foreman.puppetclasses_import module – Import Puppet Classes from a Proxy

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
> see [Requirements](puppetclasses_import_module.md#ansible-collections-theforeman-foreman-puppetclasses-import-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.puppetclasses_import`.

New in theforeman.foreman 2.0.0

- [Synopsis](puppetclasses_import_module.md#synopsis)
- [Requirements](puppetclasses_import_module.md#requirements)
- [Parameters](puppetclasses_import_module.md#parameters)
- [Attributes](puppetclasses_import_module.md#attributes)
- [Examples](puppetclasses_import_module.md#examples)
- [Return Values](puppetclasses_import_module.md#return-values)

## [Synopsis](puppetclasses_import_module.md#id1)

- Import Puppet Classes from a Proxy

## [Requirements](puppetclasses_import_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](puppetclasses_import_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **environment**  string | Puppet Environment to import Puppet Classes from |
| **except**  list / elements=string | Which types of Puppet Classes to exclude from the import.  **Choices:**   - `"new"` - `"updated"` - `"obsolete"` |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **smart_proxy**  string / required | Smart Proxy to import Puppet Classes from |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](puppetclasses_import_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Examples](puppetclasses_import_module.md#id5)

```yaml+jinja
- name: Import Puppet Classes
  theforeman.foreman.puppetclasses_import:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    smart_proxy: "foreman.example.com"
```

## [Return Values](puppetclasses_import_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  dictionary | Details about the Puppet Class import  **Returned:** success |
| **environments_ignored**  integer | Number of ignored Puppet Environments  **Returned:** when *environment* not specificed |
| **environments_obsolete**  integer | Number of Puppet Environments with removed Puppet Classes  **Returned:** when *environment* not specificed |
| **environments_updated_puppetclasses**  integer | Number of Puppet Environments with updated Puppet Classes  **Returned:** when *environment* not specificed |
| **environments_with_new_puppetclasses**  integer | Number of Puppet Environments with new Puppet Classes  **Returned:** when *environment* not specificed |
| **results**  list / elements=string | List of Puppet Environments and the changes made to them  **Returned:** success |

### Authors

- Evgeni Golov (@evgeni)

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
