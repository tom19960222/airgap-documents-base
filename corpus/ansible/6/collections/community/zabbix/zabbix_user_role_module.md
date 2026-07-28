---
collection: ansible
version: "6"
title: "community.zabbix.zabbix_user_role module – Adds or removes zabbix roles"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/zabbix/zabbix_user_role_module.html
fetched_at: 2026-07-27T17:24:24+00:00
---
# community.zabbix.zabbix_user_role module – Adds or removes zabbix roles

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
> see [Requirements](zabbix_user_role_module.md#ansible-collections-community-zabbix-zabbix-user-role-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_user_role`.

- [Synopsis](zabbix_user_role_module.md#synopsis)
- [Requirements](zabbix_user_role_module.md#requirements)
- [Parameters](zabbix_user_role_module.md#parameters)
- [Notes](zabbix_user_role_module.md#notes)
- [Examples](zabbix_user_role_module.md#examples)
- [Return Values](zabbix_user_role_module.md#return-values)

## [Synopsis](zabbix_user_role_module.md#id1)

- This module adds or removes zabbix roles

## [Requirements](zabbix_user_role_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](zabbix_user_role_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **login_password**  string | Zabbix user password.  If not set the environment variable `ZABBIX_PASSWORD` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **login_user**  string | Zabbix user name.  If not set the environment variable `ZABBIX_USERNAME` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **name**  string / required | Name of the role to be processed |
| **rules**  dictionary | Rules set as defined in <https://www.zabbix.com/documentation/current/en/manual/api/reference/role/object#role-rules>  Default: `{}` |
| **server_url**  aliases: url  string | URL of Zabbix server, with protocol (http or https). `url` is an alias for `server_url`.  If not set the environment variable `ZABBIX_SERVER` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **state**  string | State of the user_role.  On `present`, it will create if user_role does not exist or update the user_role if the associated data is different.  On `absent` will remove a user_role if it exists.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | The timeout of API request (seconds).  This option is deprecated with the move to httpapi connection and will be removed in the next release  Default: `10` |
| **type**  string | User type.  Choices:   - `"User"` ← (default) - `"Admin"` - `"Super Admin"` |
| **validate_certs**  boolean | If set to False, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If not set the environment variable `ZABBIX_VALIDATE_CERTS` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release  Choices:   - `false` - `true` ← (default) |

## [Notes](zabbix_user_role_module.md#id4)

> **Note:**
>
> - If you use *login_password=zabbix*, the word “zabbix” is replaced by “\*\*\*\*\*\*\*\*” in all module output, because *login_password* uses `no_log`. See [this FAQ](https://docs.ansible.com/ansible/latest/network/user_guide/faq.html#why-is-my-output-sometimes-replaced-with) for more information.

## [Examples](zabbix_user_role_module.md#id5)

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

# Create user role Operators with ui elements monitoring.hosts
# disabled and monitoring.maps enabled

- name: Create Zabbix user role
  community.zabbix.zabbix_user_role:
    state: present
    name: Operators
    type: User
    rules:
      ui.default_access: 0
      ui:
        - name: "monitoring.hosts"
          status: 0
        - name: "monitoring.maps"
          status: 1
```

## [Return Values](zabbix_user_role_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | The consequence of the action  Returned: always  Sample: `false` |
| **msg**  string | The result of the action  Returned: always  Sample: `"No action"` |

### Authors

- Martin van Es (@mrvanes)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
[Homepage](https://github.com/ansible-collections/community.zabbix)
[Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
