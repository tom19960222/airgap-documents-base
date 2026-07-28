---
collection: ansible
version: "8"
title: "community.zabbix.zabbix_user_info module – Gather information about Zabbix user"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/zabbix/zabbix_user_info_module.html
fetched_at: 2026-07-28T02:02:58+00:00
---
# community.zabbix.zabbix_user_info module – Gather information about Zabbix user

> **Note:**
>
> This module is part of the [community.zabbix collection](https://galaxy.ansible.com/ui/repo/published/community/zabbix/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.zabbix`.
> You need further requirements to be able to use this module,
> see [Requirements](zabbix_user_info_module.md#ansible-collections-community-zabbix-zabbix-user-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_user_info`.

- [Synopsis](zabbix_user_info_module.md#synopsis)
- [Requirements](zabbix_user_info_module.md#requirements)
- [Parameters](zabbix_user_info_module.md#parameters)
- [Examples](zabbix_user_info_module.md#examples)
- [Return Values](zabbix_user_info_module.md#return-values)

## [Synopsis](zabbix_user_info_module.md#id1)

- This module allows you to search for Zabbix user entries.

## [Requirements](zabbix_user_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.9

## [Parameters](zabbix_user_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **http_login_password**  string | Basic Auth password |
| **http_login_user**  string | Basic Auth login |
| **username**  string / required | User name.  sername is the unique identifier used and cannot be updated using this module. |

## [Examples](zabbix_user_info_module.md#id4)

```yaml+jinja
# If you want to use Username and Password to be authenticated by Zabbix Server
- name: Set credentials to access Zabbix Server API
  ansible.builtin.set_fact:
    ansible_user: Admin
    ansible_httpapi_pass: zabbix

# If you want to use API token to be authenticated by Zabbix Server
# https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/administration/general#api-tokens
- name: Set API token
  ansible.builtin.set_fact:
    ansible_zabbix_auth_key: 8ec0d52432c15c91fcafe9888500cf9a607f44091ab554dbee860f6b44fac895

- name: Get zabbix user info
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_user_info:
    username: example
```

## [Return Values](zabbix_user_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **zabbix_user**  dictionary | example  **Returned:** always  **Sample:** `{"attempt_clock": "0", "attempt_failed": "0", "attempt_ip": "", "autologin": "0", "autologout": "0", "debug_mode": "0", "gui_access": "0", "lang": "en_GB", "medias": [{"active": "0", "mediaid": "668", "mediatypeid": "1", "period": "1-7,00:00-24:00", "sendto": "example@example.com", "severity": "63", "userid": "660"}], "name": "user", "refresh": "30s", "rows_per_page": "50", "surname": "example", "theme": "default", "type": "1", "url": "", "userid": "660", "username": "example", "users_status": "0", "usrgrps": [{"debug_mode": "0", "gui_access": "0", "name": "Guests", "users_status": "0", "usrgrpid": "8"}]}` |

### Authors

- sky-joker (@sky-joker)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
- [Homepage](https://github.com/ansible-collections/community.zabbix)
- [Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
