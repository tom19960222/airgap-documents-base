---
collection: ansible
version: "6"
title: "theforeman.foreman.status_info module – Get status info"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/status_info_module.html
fetched_at: 2026-07-28T00:21:12+00:00
---
# theforeman.foreman.status_info module – Get status info

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
> see [Requirements](status_info_module.md#ansible-collections-theforeman-foreman-status-info-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.status_info`.

New in theforeman.foreman 1.3.0

- [Synopsis](status_info_module.md#synopsis)
- [Requirements](status_info_module.md#requirements)
- [Parameters](status_info_module.md#parameters)
- [Examples](status_info_module.md#examples)
- [Return Values](status_info_module.md#return-values)

## [Synopsis](status_info_module.md#id1)

- Get status information from the server

## [Requirements](status_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](status_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Examples](status_info_module.md#id4)

```yaml+jinja
- name: status
  theforeman.foreman.status_info:
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
```

## [Return Values](status_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ping**  dictionary | Detailed service status.  Returned: if supported by server |
| **status**  dictionary | Basic status of the server.  Returned: always |

### Authors

- Evgeni Golov (@evgeni)

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
