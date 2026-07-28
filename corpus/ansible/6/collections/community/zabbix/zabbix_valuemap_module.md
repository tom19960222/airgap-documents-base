---
collection: ansible
version: "6"
title: "community.zabbix.zabbix_valuemap module – Create/update/delete Zabbix value maps"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/zabbix/zabbix_valuemap_module.html
fetched_at: 2026-07-27T17:24:26+00:00
---
# community.zabbix.zabbix_valuemap module – Create/update/delete Zabbix value maps

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
> see [Requirements](zabbix_valuemap_module.md#ansible-collections-community-zabbix-zabbix-valuemap-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_valuemap`.

- [Synopsis](zabbix_valuemap_module.md#synopsis)
- [Requirements](zabbix_valuemap_module.md#requirements)
- [Parameters](zabbix_valuemap_module.md#parameters)
- [Notes](zabbix_valuemap_module.md#notes)
- [Examples](zabbix_valuemap_module.md#examples)

## [Synopsis](zabbix_valuemap_module.md#id1)

- This module allows you to create, modify and delete Zabbix value maps.

## [Requirements](zabbix_valuemap_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](zabbix_valuemap_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **login_password**  string | Zabbix user password.  If not set the environment variable `ZABBIX_PASSWORD` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **login_user**  string | Zabbix user name.  If not set the environment variable `ZABBIX_USERNAME` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **mappings**  list / elements=dictionary | List of value mappings for the value map.  Required when *state=present*. |
| **map_to**  string / required | Value to which the original value is mapped to. |
| **value**  string / required | Original value. |
| **name**  string / required | Name of the value map. |
| **server_url**  aliases: url  string | URL of Zabbix server, with protocol (http or https). `url` is an alias for `server_url`.  If not set the environment variable `ZABBIX_SERVER` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **state**  string | State of the value map.  On `present`, it will create a value map if it does not exist or update the value map if the associated data is different.  On `absent`, it will remove the value map if it exists.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | The timeout of API request (seconds).  This option is deprecated with the move to httpapi connection and will be removed in the next release  Default: `10` |
| **validate_certs**  boolean | If set to False, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If not set the environment variable `ZABBIX_VALIDATE_CERTS` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release  Choices:   - `false` - `true` ← (default) |

## [Notes](zabbix_valuemap_module.md#id4)

> **Note:**
>
> - If you use *login_password=zabbix*, the word “zabbix” is replaced by “\*\*\*\*\*\*\*\*” in all module output, because *login_password* uses `no_log`. See [this FAQ](https://docs.ansible.com/ansible/latest/network/user_guide/faq.html#why-is-my-output-sometimes-replaced-with) for more information.

## [Examples](zabbix_valuemap_module.md#id5)

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

- name: Create a value map
  community.zabbix.zabbix_valuemap:
    name: Numbers
    mappings:
      - value: 1
        map_to: one
      - value: 2
        map_to: two
    state: present
```

### Authors

- Ruben Tsirunyan (@rubentsirunyan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
[Homepage](https://github.com/ansible-collections/community.zabbix)
[Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
