---
collection: ansible
version: "6"
title: "theforeman.foreman.setting_info module – Fetch information about Settings"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/setting_info_module.html
fetched_at: 2026-07-28T00:21:09+00:00
---
# theforeman.foreman.setting_info module – Fetch information about Settings

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
> see [Requirements](setting_info_module.md#ansible-collections-theforeman-foreman-setting-info-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.setting_info`.

New in theforeman.foreman 2.1.0

- [Synopsis](setting_info_module.md#synopsis)
- [Requirements](setting_info_module.md#requirements)
- [Parameters](setting_info_module.md#parameters)
- [Examples](setting_info_module.md#examples)
- [Return Values](setting_info_module.md#return-values)

## [Synopsis](setting_info_module.md#id1)

- Fetch information about Settings

## [Requirements](setting_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](setting_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **location**  string | Label of the Location to scope the search for. |
| **name**  string | Name of the resource to fetch information for.  Mutually exclusive with *search*. |
| **organization**  string | Name of the Organization to scope the search for. |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **search**  string | Search query to use  If None, and *name* is not set, all resources are returned.  Mutually exclusive with *name*. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Examples](setting_info_module.md#id4)

```yaml+jinja
- name: "Show a setting"
  theforeman.foreman.setting_info:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "http_proxy"

- name: "Show all settings with proxy"
  theforeman.foreman.setting_info:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    search: "name = proxy"
```

## [Return Values](setting_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **setting**  dictionary | Details about the found setting  Returned: success and *name* was passed |
| **settings**  list / elements=dictionary | List of all found settings and their details  Returned: success and *search* was passed |

### Authors

- Eric Helms (@ehelms)

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
