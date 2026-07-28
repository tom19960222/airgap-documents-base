---
collection: ansible
version: "6"
title: "theforeman.foreman.host_errata_info module – Fetch information about Host Errata"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/host_errata_info_module.html
fetched_at: 2026-07-28T00:20:46+00:00
---
# theforeman.foreman.host_errata_info module – Fetch information about Host Errata

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
> see [Requirements](host_errata_info_module.md#ansible-collections-theforeman-foreman-host-errata-info-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.host_errata_info`.

New in theforeman.foreman 2.1.0

- [Synopsis](host_errata_info_module.md#synopsis)
- [Requirements](host_errata_info_module.md#requirements)
- [Parameters](host_errata_info_module.md#parameters)
- [Examples](host_errata_info_module.md#examples)
- [Return Values](host_errata_info_module.md#return-values)

## [Synopsis](host_errata_info_module.md#id1)

- Fetch information about Host Errata

## [Requirements](host_errata_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](host_errata_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **content_view**  string | Calculate Applicable Errata based on a particular Content View.  Required together with *lifecycle_environment*.  If this is set, *organization* also needs to be set. |
| **host**  string / required | Name of the host to fetch errata for. |
| **lifecycle_environment**  string | Calculate Applicable Errata based on a particular Lifecycle Environment.  Required together with *content_view*.  If this is set, *organization* also needs to be set. |
| **location**  string | Label of the Location to scope the search for. |
| **organization**  string | Name of the Organization to scope the search for. |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **search**  string | Search query to use  If None, all resources are returned. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Examples](host_errata_info_module.md#id4)

```yaml+jinja
- name: "List installable errata for host"
  theforeman.foreman.host_errata_info:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    host: "host.example.com"

- name: "List applicable errata for host"
  theforeman.foreman.host_errata_info:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    organization: "Default Organization"
    host: "host.example.com"
    lifecycle_environment: "Library"
    content_view: "Default Organization View"
```

## [Return Values](host_errata_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **host_errata**  list / elements=dictionary | List of all found errata for the host and their details  Returned: success |

### Authors

- Evgeni Golov (@evgeni)

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
