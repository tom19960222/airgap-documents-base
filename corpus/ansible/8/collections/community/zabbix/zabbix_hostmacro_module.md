---
collection: ansible
version: "8"
title: "community.zabbix.zabbix_hostmacro module – Create/update/delete Zabbix host macros"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/zabbix/zabbix_hostmacro_module.html
fetched_at: 2026-07-28T02:02:47+00:00
---
# community.zabbix.zabbix_hostmacro module – Create/update/delete Zabbix host macros

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
> see [Requirements](zabbix_hostmacro_module.md#ansible-collections-community-zabbix-zabbix-hostmacro-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_hostmacro`.

- [Synopsis](zabbix_hostmacro_module.md#synopsis)
- [Requirements](zabbix_hostmacro_module.md#requirements)
- [Parameters](zabbix_hostmacro_module.md#parameters)
- [Examples](zabbix_hostmacro_module.md#examples)

## [Synopsis](zabbix_hostmacro_module.md#id1)

- manages Zabbix host macros, it can create, update or delete them.

## [Requirements](zabbix_hostmacro_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.9

## [Parameters](zabbix_hostmacro_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **force**  boolean | Only updates an existing macro if set to `yes`.  **Choices:**   - `false` - `true` ← (default) |
| **host_name**  string / required | Name of the host. |
| **http_login_password**  string | Basic Auth password |
| **http_login_user**  string | Basic Auth login |
| **macro_description**  string | Text Description of the global macro.  **Default:** `""` |
| **macro_name**  string / required | Name of the host macro in zabbix native format `{$MACRO}` or simple format `MACRO`. |
| **macro_type**  string | Type of the host macro.  text (default)  **Choices:**   - `"text"` ← (default) - `"secret"` - `"vault"` |
| **macro_value**  string | Value of the host macro.  Required if *state=present*. |
| **state**  string | State of the macro.  On `present`, it will create if macro does not exist or update the macro if the associated data is different.  On `absent` will remove a macro if it exists.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Examples](zabbix_hostmacro_module.md#id4)

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

- name: Create new host macro or update an existing macro's value
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_hostmacro:
    host_name: ExampleHost
    macro_name: EXAMPLE.MACRO
    macro_value: Example value
    macro_description: Example description
    state: present

# Values with curly brackets need to be quoted otherwise they will be interpreted as a dictionary
- name: Create new host macro in Zabbix native format
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_hostmacro:
    host_name: ExampleHost
    macro_name: "{$EXAMPLE.MACRO}"
    macro_value: Example value
    macro_description: Example description
    state: present

- name: Delete existing host macro
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_hostmacro:
    host_name: ExampleHost
    macro_name: "{$EXAMPLE.MACRO}"
    state: absent
```

### Authors

- Cove (@cove)
- Dean Hailin Song

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
- [Homepage](https://github.com/ansible-collections/community.zabbix)
- [Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
