---
collection: ansible
version: "8"
title: "community.zabbix.zabbix_token module – Create/Update/Generate/Delete Zabbix token."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/zabbix/zabbix_token_module.html
fetched_at: 2026-07-28T02:02:56+00:00
---
# community.zabbix.zabbix_token module – Create/Update/Generate/Delete Zabbix token.

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
> see [Requirements](zabbix_token_module.md#ansible-collections-community-zabbix-zabbix-token-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_token`.

New in community.zabbix 2.1.0

- [Synopsis](zabbix_token_module.md#synopsis)
- [Requirements](zabbix_token_module.md#requirements)
- [Parameters](zabbix_token_module.md#parameters)
- [Examples](zabbix_token_module.md#examples)
- [Return Values](zabbix_token_module.md#return-values)

## [Synopsis](zabbix_token_module.md#id1)

- This module allows you to create, update, generate and delete Zabbix token.

## [Requirements](zabbix_token_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.9

## [Parameters](zabbix_token_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  string | Description of the token. |
| **expires_at**  integer | A timestamp of the token will be expired.  The token will never expire if `0` |
| **generate_token**  boolean | New token string will be generated if `true`.  **Choices:**   - `false` ← (default) - `true` |
| **http_login_password**  string | Basic Auth password |
| **http_login_user**  string | Basic Auth login |
| **name**  string / required | Name of the token. |
| **state**  string | Create or delete token.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **status**  boolean | Status of the token.  **Choices:**   - `false` - `true` |
| **username**  string / required | Name of user who is the token assinged to. |

## [Examples](zabbix_token_module.md#id4)

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

- name: Create Zabbix token and generate token string
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_token:
    name: test token
    description: Admin test token
    username: Admin
    status: true
    expires_at: 1700000000
    generate_token: true
    state: present
```

## [Return Values](zabbix_token_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | The result of the operation  **Returned:** success  **Sample:** `"Successfully created token"` |
| **token**  string | Generated token string  **Returned:** *generate_token=true*  **Sample:** `"8ec0d52432c15c91fcafe9888500cf9a607f44091ab554dbee860f6b44fac895"` |

### Authors

- ONODERA Masaru(@masa-orca)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
- [Homepage](https://github.com/ansible-collections/community.zabbix)
- [Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
