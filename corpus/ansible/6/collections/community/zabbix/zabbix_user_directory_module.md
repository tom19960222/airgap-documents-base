---
collection: ansible
version: "6"
title: "community.zabbix.zabbix_user_directory module – Create/update/delete Zabbix user directories"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/zabbix/zabbix_user_directory_module.html
fetched_at: 2026-07-27T17:24:23+00:00
---
# community.zabbix.zabbix_user_directory module – Create/update/delete Zabbix user directories

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
> see [Requirements](zabbix_user_directory_module.md#ansible-collections-community-zabbix-zabbix-user-directory-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_user_directory`.

- [Synopsis](zabbix_user_directory_module.md#synopsis)
- [Requirements](zabbix_user_directory_module.md#requirements)
- [Parameters](zabbix_user_directory_module.md#parameters)
- [Notes](zabbix_user_directory_module.md#notes)
- [Examples](zabbix_user_directory_module.md#examples)

## [Synopsis](zabbix_user_directory_module.md#id1)

- This module allows you to create, modify and delete Zabbix user directories.

## [Requirements](zabbix_user_directory_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.9

## [Parameters](zabbix_user_directory_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **base_dn**  string | LDAP base distinguished name string. |
| **bind_dn**  string | LDAP bind distinguished name string. Can be empty for anonymous binding.  Default: `""` |
| **bind_password**  string | LDAP bind password. Can be empty for anonymous binding.  Available only for *present* `state`. |
| **description**  string | User directory description.  Default: `""` |
| **host**  string | LDAP server host name, IP or URI. URI should contain schema, host and port (optional). |
| **login_password**  string | Zabbix user password.  If not set the environment variable `ZABBIX_PASSWORD` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **login_user**  string | Zabbix user name.  If not set the environment variable `ZABBIX_USERNAME` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **name**  string / required | Unique name of the user directory. |
| **port**  integer | LDAP server port. |
| **search_attribute**  string | LDAP attribute name to identify user by username in Zabbix database. |
| **search_filter**  string | LDAP custom filter string when authenticating user in LDAP.  Default: `"(%{attr}=%{user})"` |
| **server_url**  aliases: url  string | URL of Zabbix server, with protocol (http or https). `url` is an alias for `server_url`.  If not set the environment variable `ZABBIX_SERVER` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **start_tls**  integer | LDAP startTLS option. It cannot be used with ldaps:// protocol hosts.  Choices:   - `0` ← (default) - `1` |
| **state**  string | State of the user directory.  On `present`, it will create if user directory does not exist or update it if the associated data is different.  On `absent` will remove the user directory if it exists.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | The timeout of API request (seconds).  This option is deprecated with the move to httpapi connection and will be removed in the next release  Default: `10` |
| **validate_certs**  boolean | If set to False, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If not set the environment variable `ZABBIX_VALIDATE_CERTS` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release  Choices:   - `false` - `true` ← (default) |

## [Notes](zabbix_user_directory_module.md#id4)

> **Note:**
>
> - If you use *login_password=zabbix*, the word “zabbix” is replaced by “\*\*\*\*\*\*\*\*” in all module output, because *login_password* uses `no_log`. See [this FAQ](https://docs.ansible.com/ansible/latest/network/user_guide/faq.html#why-is-my-output-sometimes-replaced-with) for more information.

## [Examples](zabbix_user_directory_module.md#id5)

```yaml+jinja
---
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

- name: Create new user directory or update existing info
  community.zabbix.zabbix_user_directory:
    server_url: http://monitor.example.com
    login_user: username
    login_password: password
    state: present
    name: TestUserDirectory
    host: 'test.com'
    port: 389
    base_dn: 'ou=Users,dc=example,dc=org'
    search_attribute: 'uid'
    bind_dn: 'cn=ldap_search,dc=example,dc=org'
    description: 'Test user directory'
    search_filter: '(%{attr}=test_user)'
    start_tls: 0
```

### Authors

- Evgeny Yurchenko (@BGmot)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
[Homepage](https://github.com/ansible-collections/community.zabbix)
[Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
