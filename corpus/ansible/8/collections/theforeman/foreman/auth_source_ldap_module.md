---
collection: ansible
version: "8"
title: "theforeman.foreman.auth_source_ldap module – Manage LDAP Authentication Sources"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/auth_source_ldap_module.html
fetched_at: 2026-07-28T02:55:34+00:00
---
# theforeman.foreman.auth_source_ldap module – Manage LDAP Authentication Sources

> **Note:**
>
> This module is part of the [theforeman.foreman collection](https://galaxy.ansible.com/ui/repo/published/theforeman/foreman/) (version 3.15.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install theforeman.foreman`.
> You need further requirements to be able to use this module,
> see [Requirements](auth_source_ldap_module.md#ansible-collections-theforeman-foreman-auth-source-ldap-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.auth_source_ldap`.

New in theforeman.foreman 1.0.0

- [Synopsis](auth_source_ldap_module.md#synopsis)
- [Requirements](auth_source_ldap_module.md#requirements)
- [Parameters](auth_source_ldap_module.md#parameters)
- [Attributes](auth_source_ldap_module.md#attributes)
- [Examples](auth_source_ldap_module.md#examples)
- [Return Values](auth_source_ldap_module.md#return-values)

## [Synopsis](auth_source_ldap_module.md#id1)

- Create, update, and delete LDAP authentication sources

Aliases: foreman_auth_source_ldap

## [Requirements](auth_source_ldap_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](auth_source_ldap_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account**  string | Account name to use when accessing the LDAP server. |
| **account_password**  string | Account password to use when accessing the LDAP server.  Required when using *onthefly_register*.  When this parameter is set, the module will not be idempotent. |
| **attr_firstname**  string | Attribute containing first name.  Required when using *onthefly_register*. |
| **attr_lastname**  string | Attribute containing last name.  Required when using *onthefly_register*. |
| **attr_login**  string | Attribute containing login ID.  Required when using *onthefly_register*. |
| **attr_mail**  string | Attribute containing email address.  Required when using *onthefly_register*. |
| **attr_photo**  string | Attribute containing user photo |
| **base_dn**  string | The base DN to use when searching. |
| **groups_base**  string | Base DN where groups reside. |
| **host**  string / required | The hostname of the LDAP server |
| **ldap_filter**  string | Filter to apply to LDAP searches |
| **locations**  list / elements=string | List of locations the entity should be assigned to |
| **name**  string / required | The name of the LDAP authentication source |
| **onthefly_register**  boolean | Whether or not to register users on the fly.  **Choices:**   - `false` - `true` |
| **organizations**  list / elements=string | List of organizations the entity should be assigned to |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **port**  integer | The port number of the LDAP server  **Default:** `389` |
| **server_type**  string | Type of the LDAP server  **Choices:**   - `"free_ipa"` - `"active_directory"` - `"posix"` |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tls**  boolean | Whether or not to use TLS when contacting the LDAP server.  **Choices:**   - `false` - `true` |
| **use_netgroups**  boolean | Whether to use NIS netgroups instead of posix groups, not valid for *server_type=active_directory*  **Choices:**   - `false` - `true` |
| **usergroup_sync**  boolean | Whether or not to sync external user groups on login  **Choices:**   - `false` - `true` |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](auth_source_ldap_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Examples](auth_source_ldap_module.md#id5)

```yaml+jinja
- name: Simple FreeIPA authentication source
  theforeman.foreman.auth_source_ldap:
    name: "Example LDAP"
    host: "ldap.example.org"
    server_url: "https://foreman.example.com"
    locations:
      - "Uppsala"
    organizations:
      - "Sweden"
    username: "admin"
    password: "changeme"
    state: present

- name: FreeIPA with automatic registration
  theforeman.foreman.auth_source_ldap:
    name: "Example LDAP"
    host: "ldap.example.org"
    onthefly_register: true
    account: uid=ansible,cn=sysaccounts,cn=etc,dc=example,dc=com
    account_password: secret
    base_dn: dc=example,dc=com
    groups_base: cn=groups,cn=accounts, dc=example,dc=com
    server_type: free_ipa
    attr_login: uid
    attr_firstname: givenName
    attr_lastname: sn
    attr_mail: mail
    attr_photo: jpegPhoto
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: present

- name: Active Directory with automatic registration
  theforeman.foreman.auth_source_ldap:
    name: "Example AD"
    host: "ad.example.org"
    onthefly_register: true
    account: EXAMPLE\ansible
    account_password: secret
    base_dn: cn=Users,dc=example,dc=com
    groups_base: cn=Users,dc=example,dc=com
    server_type: active_directory
    attr_login: sAMAccountName
    attr_firstname: givenName
    attr_lastname: sn
    attr_mail: mail
    ldap_filter: (memberOf=CN=Domain Users,CN=Users,DC=example,DC=com)
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: present
```

## [Return Values](auth_source_ldap_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  **Returned:** success |
| **auth_source_ldaps**  list / elements=dictionary | List of auth sources for LDAP.  **Returned:** success |

### Authors

- Christoffer Reijer (@ephracis) Basalt AB

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
