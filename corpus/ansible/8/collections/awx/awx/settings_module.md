---
collection: ansible
version: "8"
title: "awx.awx.settings module – Modify Automation Platform Controller settings."
source_url: https://docs.ansible.com/projects/ansible/8/collections/awx/awx/settings_module.html
fetched_at: 2026-07-28T01:11:43+00:00
---
# awx.awx.settings module – Modify Automation Platform Controller settings.

> **Note:**
>
> This module is part of the [awx.awx collection](https://galaxy.ansible.com/ui/repo/published/awx/awx/) (version 22.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install awx.awx`.
> You need further requirements to be able to use this module,
> see [Requirements](settings_module.md#ansible-collections-awx-awx-settings-module-requirements) for details.
>
> To use it in a playbook, specify: `awx.awx.settings`.

- [Synopsis](settings_module.md#synopsis)
- [Requirements](settings_module.md#requirements)
- [Parameters](settings_module.md#parameters)
- [Notes](settings_module.md#notes)
- [Examples](settings_module.md#examples)

## [Synopsis](settings_module.md#id1)

- Modify Automation Platform Controller settings. See <https://www.ansible.com/tower> for an overview.

Aliases: tower_settings

## [Requirements](settings_module.md#id2)

The below requirements are needed on the host that executes this module.

- pyyaml

## [Parameters](settings_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **controller_config_file**  aliases: tower_config_file  path | Path to the controller config file.  If provided, the other locations for config files will not be considered. |
| **controller_host**  aliases: tower_host  string | URL to your Automation Platform Controller instance.  If value not set, will try environment variable `CONTROLLER_HOST` and then config files  If value not specified by any means, the value of `127.0.0.1` will be used |
| **controller_oauthtoken**  aliases: tower_oauthtoken  any  *added in awx.awx 3.7.0* | The OAuth token to use.  This value can be in one of two formats.  A string which is the token itself. (i.e. bqV5txm97wqJqtkxlMkhQz0pKhRMMX)  A dictionary structure as returned by the token module.  If value not set, will try environment variable `CONTROLLER_OAUTH_TOKEN` and then config files |
| **controller_password**  aliases: tower_password  string | Password for your controller instance.  If value not set, will try environment variable `CONTROLLER_PASSWORD` and then config files |
| **controller_username**  aliases: tower_username  string | Username for your controller instance.  If value not set, will try environment variable `CONTROLLER_USERNAME` and then config files |
| **name**  string | Name of setting to modify |
| **request_timeout**  float | Specify the timeout Ansible should use in requests to the controller host.  Defaults to 10s, but this is handled by the shared module_utils code |
| **settings**  dictionary | A data structure to be sent into the settings endpoint |
| **validate_certs**  aliases: tower_verify_ssl  boolean | Whether to allow insecure connections to AWX.  If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  If value not set, will try environment variable `CONTROLLER_VERIFY_SSL` and then config files  **Choices:**   - `false` - `true` |
| **value**  string | Value to be modified for given setting.  If given a non-string type, will make best effort to cast it to type API expects.  For better control over types, use the `settings` param instead. |

## [Notes](settings_module.md#id4)

> **Note:**
>
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](settings_module.md#id5)

```yaml+jinja
- name: Set the value of AWX_ISOLATION_BASE_PATH
  settings:
    name: AWX_ISOLATION_BASE_PATH
    value: "/tmp"
  register: testing_settings

- name: Set the value of AWX_ISOLATION_SHOW_PATHS
  settings:
    name: "AWX_ISOLATION_SHOW_PATHS"
    value: "'/var/lib/awx/projects/', '/tmp'"
  register: testing_settings

- name: Set the LDAP Auth Bind Password
  settings:
    name: "AUTH_LDAP_BIND_PASSWORD"
    value: "Password"
  no_log: true

- name: Set all the LDAP Auth Bind Params
  settings:
    settings:
      AUTH_LDAP_BIND_PASSWORD: "password"
      AUTH_LDAP_USER_ATTR_MAP:
        email: "mail"
        first_name: "givenName"
        last_name: "surname"
```

### Authors

- Nikhil Jain (@jainnikhil30)

### Collection links

- [Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
- [Homepage](https://www.ansible.com/)
- [Repository (Sources)](https://github.com/ansible/awx)
