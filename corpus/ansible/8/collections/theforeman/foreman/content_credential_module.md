---
collection: ansible
version: "8"
title: "theforeman.foreman.content_credential module – Manage Content Credentials"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/content_credential_module.html
fetched_at: 2026-07-28T02:55:40+00:00
---
# theforeman.foreman.content_credential module – Manage Content Credentials

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
> see [Requirements](content_credential_module.md#ansible-collections-theforeman-foreman-content-credential-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.content_credential`.

New in theforeman.foreman 1.0.0

- [Synopsis](content_credential_module.md#synopsis)
- [Requirements](content_credential_module.md#requirements)
- [Parameters](content_credential_module.md#parameters)
- [Attributes](content_credential_module.md#attributes)
- [Examples](content_credential_module.md#examples)
- [Return Values](content_credential_module.md#return-values)

## [Synopsis](content_credential_module.md#id1)

- Create and manage content credentials

Aliases: katello_content_credential

## [Requirements](content_credential_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](content_credential_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **content**  string | Content of the content credential  Required when creating a new credential |
| **content_type**  string | Type of credential  Required when creating a new credential  **Choices:**   - `"gpg_key"` - `"cert"` |
| **name**  string / required | Name of the content credential |
| **organization**  string / required | Organization that the entity is in |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](content_credential_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Examples](content_credential_module.md#id5)

```yaml+jinja
- name: "Create katello client GPG key"
  theforeman.foreman.content_credential:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "RPM-GPG-KEY-my-repo"
    content_type: gpg_key
    organization: "Default Organization"
    content: "{{ lookup('file', 'RPM-GPG-KEY-my-repo') }}"
```

## [Return Values](content_credential_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  **Returned:** success |
| **content_credentials**  list / elements=dictionary | List of content credentials.  **Returned:** success |

### Authors

- Baptiste Agasse (@bagasse)

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
