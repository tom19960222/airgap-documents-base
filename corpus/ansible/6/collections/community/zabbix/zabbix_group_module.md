---
collection: ansible
version: "6"
title: "community.zabbix.zabbix_group module – Create/delete Zabbix host groups"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/zabbix/zabbix_group_module.html
fetched_at: 2026-07-27T17:24:10+00:00
---
# community.zabbix.zabbix_group module – Create/delete Zabbix host groups

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
> see [Requirements](zabbix_group_module.md#ansible-collections-community-zabbix-zabbix-group-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_group`.

- [Synopsis](zabbix_group_module.md#synopsis)
- [Requirements](zabbix_group_module.md#requirements)
- [Parameters](zabbix_group_module.md#parameters)
- [Notes](zabbix_group_module.md#notes)
- [Examples](zabbix_group_module.md#examples)

## [Synopsis](zabbix_group_module.md#id1)

- Create host groups if they do not exist.
- Delete existing host groups if they exist.

## [Requirements](zabbix_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](zabbix_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **host_groups**  aliases: host_group  list / elements=string / required | List of host groups to create or delete. |
| **login_password**  string | Zabbix user password.  If not set the environment variable `ZABBIX_PASSWORD` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **login_user**  string | Zabbix user name.  If not set the environment variable `ZABBIX_USERNAME` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **server_url**  aliases: url  string | URL of Zabbix server, with protocol (http or https). `url` is an alias for `server_url`.  If not set the environment variable `ZABBIX_SERVER` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **state**  string | Create or delete host group.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | The timeout of API request (seconds).  This option is deprecated with the move to httpapi connection and will be removed in the next release  Default: `10` |
| **validate_certs**  boolean | If set to False, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If not set the environment variable `ZABBIX_VALIDATE_CERTS` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release  Choices:   - `false` - `true` ← (default) |

## [Notes](zabbix_group_module.md#id4)

> **Note:**
>
> - Too many concurrent updates to the same group may cause Zabbix to return errors, see examples for a workaround if needed.
> - If you use *login_password=zabbix*, the word “zabbix” is replaced by “\*\*\*\*\*\*\*\*” in all module output, because *login_password* uses `no_log`. See [this FAQ](https://docs.ansible.com/ansible/latest/network/user_guide/faq.html#why-is-my-output-sometimes-replaced-with) for more information.

## [Examples](zabbix_group_module.md#id5)

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

# Base create host groups example
- name: Create host groups
  community.zabbix.zabbix_group:
    state: present
    host_groups:
      - Example group1
      - Example group2

# Limit the Zabbix group creations to one host since Zabbix can return an error when doing concurrent updates
- name: Create host groups
  community.zabbix.zabbix_group:
    state: present
    host_groups:
      - Example group1
      - Example group2
  when: inventory_hostname==groups['group_name'][0]
```

### Authors

- Cove (@cove)
- Tony Minfei Ding
- Harrison Gu (@harrisongu)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
[Homepage](https://github.com/ansible-collections/community.zabbix)
[Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
