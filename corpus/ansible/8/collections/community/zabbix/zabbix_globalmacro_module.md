---
collection: ansible
version: "8"
title: "community.zabbix.zabbix_globalmacro module – Create/update/delete Zabbix Global macros"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/zabbix/zabbix_globalmacro_module.html
fetched_at: 2026-07-28T02:02:41+00:00
---
# community.zabbix.zabbix_globalmacro module – Create/update/delete Zabbix Global macros

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
> see [Requirements](zabbix_globalmacro_module.md#ansible-collections-community-zabbix-zabbix-globalmacro-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_globalmacro`.

New in community.zabbix 1.4.0

- [Synopsis](zabbix_globalmacro_module.md#synopsis)
- [Requirements](zabbix_globalmacro_module.md#requirements)
- [Parameters](zabbix_globalmacro_module.md#parameters)
- [Notes](zabbix_globalmacro_module.md#notes)
- [Examples](zabbix_globalmacro_module.md#examples)

## [Synopsis](zabbix_globalmacro_module.md#id1)

- manages Zabbix Global macros, it can create, update or delete them.
- For macro_type Secret the value field cannot be validated and will always be overwritten due to the secret nature of the Text.

## [Requirements](zabbix_globalmacro_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.9

## [Parameters](zabbix_globalmacro_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **force**  boolean | Only updates an existing macro if set to `yes`.  **Choices:**   - `false` - `true` ← (default) |
| **http_login_password**  string | Basic Auth password |
| **http_login_user**  string | Basic Auth login |
| **macro_description**  string | Text Description of the global macro.  **Default:** `""` |
| **macro_name**  string / required | Name of the global macro in zabbix native format `{$MACRO}` or simple format `MACRO`. |
| **macro_type**  string | Type of the global macro Text or Secret Text.  Required if *state=present*.  text  secret - Secret Text Works only with Zabbix >= 5.0 and will default to Text in lower versions  vault - Vault Secret Works only with Zabbix >= 5.2 and will default to Text in lower versions  **Choices:**   - `"text"` ← (default) - `"secret"` - `"vault"` |
| **macro_value**  string | Value of the global macro.  Required if *state=present*. |
| **state**  string | State of the macro.  On `present`, it will create if macro does not exist or update the macro if the associated data is different.  On `absent` will remove a macro if it exists.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](zabbix_globalmacro_module.md#id4)

> **Note:**
>
> - This module returns changed=true when *macro_type=secret*.

## [Examples](zabbix_globalmacro_module.md#id5)

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

- name: Create new global macro or update an existing macro's value
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_globalmacro:
    macro_name: EXAMPLE.MACRO
    macro_value: Example value
    macro_type: 0
    macro_description: Example description
    state: present
# Values with curly brackets need to be quoted otherwise they will be interpreted as a dictionary
- name: Create new global macro in Zabbix native format with Secret Type
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_globalmacro:
    macro_name: "{$EXAMPLE.MACRO}"
    macro_value: Example value
    macro_type: 1
    macro_description: Example description
    state: present
- name: Delete existing global macro
  community.zabbix.zabbix_globalmacro:
    macro_name: "{$EXAMPLE.MACRO}"
    state: absent
```

### Authors

- Cove (@cove)
- Dean Hailin Song
- Timothy Test (@ttestscripting)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
- [Homepage](https://github.com/ansible-collections/community.zabbix)
- [Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
