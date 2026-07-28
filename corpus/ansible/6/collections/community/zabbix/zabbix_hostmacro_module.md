---
collection: ansible
version: "6"
title: "community.zabbix.zabbix_hostmacro module – Create/update/delete Zabbix host macros"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/zabbix/zabbix_hostmacro_module.html
fetched_at: 2026-07-27T17:24:14+00:00
---
# community.zabbix.zabbix_hostmacro module – Create/update/delete Zabbix host macros

> **Note:**
>
> This module is part of the [community.zabbix collection](https://galaxy.ansible.com/community/zabbix) (version 1.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.zabbix`.
> You need further requirements to be able to use this module,
> see [Requirements](zabbix_hostmacro_module.md#ansible-collections-community-zabbix-zabbix-hostmacro-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_hostmacro`.

- [Synopsis](zabbix_hostmacro_module.md#synopsis)
- [Requirements](zabbix_hostmacro_module.md#requirements)
- [Parameters](zabbix_hostmacro_module.md#parameters)
- [Notes](zabbix_hostmacro_module.md#notes)
- [Examples](zabbix_hostmacro_module.md#examples)

## [Synopsis](zabbix_hostmacro_module.md#id1)

- manages Zabbix host macros, it can create, update or delete them.

## [Requirements](zabbix_hostmacro_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](zabbix_hostmacro_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **force**  boolean | Only updates an existing macro if set to `yes`.  Choices:   - `false` - `true` ← (default) |
| **host_name**  string / required | Name of the host. |
| **login_password**  string | Zabbix user password.  If not set the environment variable `ZABBIX_PASSWORD` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **login_user**  string | Zabbix user name.  If not set the environment variable `ZABBIX_USERNAME` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **macro_name**  string / required | Name of the host macro in zabbix native format `{$MACRO}` or simple format `MACRO`. |
| **macro_type**  string | Type of the host macro.  text (default)  secret (Works only with Zabbix >= 5.0)  vault (Works only with Zabbix >= 5.2)  Choices:   - `"text"` ← (default) - `"secret"` - `"vault"` |
| **macro_value**  string | Value of the host macro.  Required if *state=present*. |
| **server_url**  aliases: url  string | URL of Zabbix server, with protocol (http or https). `url` is an alias for `server_url`.  If not set the environment variable `ZABBIX_SERVER` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **state**  string | State of the macro.  On `present`, it will create if macro does not exist or update the macro if the associated data is different.  On `absent` will remove a macro if it exists.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | The timeout of API request (seconds).  This option is deprecated with the move to httpapi connection and will be removed in the next release  Default: `10` |
| **validate_certs**  boolean | If set to False, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If not set the environment variable `ZABBIX_VALIDATE_CERTS` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release  Choices:   - `false` - `true` ← (default) |

## [Notes](zabbix_hostmacro_module.md#id4)

> **Note:**
>
> - If you use *login_password=zabbix*, the word “zabbix” is replaced by “\*\*\*\*\*\*\*\*” in all module output, because *login_password* uses `no_log`. See [this FAQ](https://docs.ansible.com/ansible/latest/network/user_guide/faq.html#why-is-my-output-sometimes-replaced-with) for more information.

## [Examples](zabbix_hostmacro_module.md#id5)

```yaml+jinja
# Set following variables for Zabbix Server host in play or inventory
- name: Set connection specific variables
  set_fact:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 80
    ansible_httpapi_use_ssl: false
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: 'zabbixeu'  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu

# If you want to use Username and Password to be authenticated by Zabbix Server
- name: Set credentials to access Zabbix Server API
  set_fact:
    ansible_user: Admin
    ansible_httpapi_pass: zabbix

# If you want to use API token to be authenticated by Zabbix Server
# https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/administration/general#api-tokens
- name: Set API token
  set_fact:
    ansible_zabbix_auth_key: 8ec0d52432c15c91fcafe9888500cf9a607f44091ab554dbee860f6b44fac895

- name: Create new host macro or update an existing macro's value
  community.zabbix.zabbix_hostmacro:
    host_name: ExampleHost
    macro_name: EXAMPLE.MACRO
    macro_value: Example value
    state: present

# Values with curly brackets need to be quoted otherwise they will be interpreted as a dictionary
- name: Create new host macro in Zabbix native format
  community.zabbix.zabbix_hostmacro:
    host_name: ExampleHost
    macro_name: "{$EXAMPLE.MACRO}"
    macro_value: Example value
    state: present

- name: Delete existing host macro
  community.zabbix.zabbix_hostmacro:
    host_name: ExampleHost
    macro_name: "{$EXAMPLE.MACRO}"
    state: absent
```

### Authors

- Cove (@cove)
- Dean Hailin Song

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
[Homepage](https://github.com/ansible-collections/community.zabbix)
[Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
