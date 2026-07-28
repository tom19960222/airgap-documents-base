---
collection: ansible
version: "6"
title: "theforeman.foreman.setting module – Manage Settings"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/setting_module.html
fetched_at: 2026-07-28T00:21:08+00:00
---
# theforeman.foreman.setting module – Manage Settings

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
> see [Requirements](setting_module.md#ansible-collections-theforeman-foreman-setting-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.setting`.

New in theforeman.foreman 1.0.0

- [Synopsis](setting_module.md#synopsis)
- [Requirements](setting_module.md#requirements)
- [Parameters](setting_module.md#parameters)
- [Examples](setting_module.md#examples)
- [Return Values](setting_module.md#return-values)

## [Synopsis](setting_module.md#id1)

- Manage Settings

## [Requirements](setting_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](setting_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **name**  string / required | Name of the Setting |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |
| **value**  any | value to set the Setting to  if missing, reset to default |

## [Examples](setting_module.md#id4)

```yaml+jinja
- name: "Set a Setting"
  theforeman.foreman.setting:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "http_proxy"
    value: "http://localhost:8088"

- name: "Reset a Setting"
  theforeman.foreman.setting:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "http_proxy"
```

## [Return Values](setting_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  Returned: success |
| **settings**  list / elements=dictionary | List of settings.  Returned: success |
| **foreman_setting**  dictionary | Created / Updated state of the setting (deprecated)  Returned: success |

### Authors

- Matthias M Dellweg (@mdellweg) ATIX AG

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
