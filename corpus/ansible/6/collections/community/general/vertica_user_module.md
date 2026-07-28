---
collection: ansible
version: "6"
title: "community.general.vertica_user module – Adds or removes Vertica database users and assigns roles"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/vertica_user_module.html
fetched_at: 2026-07-27T17:13:54+00:00
---
# community.general.vertica_user module – Adds or removes Vertica database users and assigns roles

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](vertica_user_module.md#ansible-collections-community-general-vertica-user-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.vertica_user`.

- [Synopsis](vertica_user_module.md#synopsis)
- [Requirements](vertica_user_module.md#requirements)
- [Parameters](vertica_user_module.md#parameters)
- [Notes](vertica_user_module.md#notes)
- [Examples](vertica_user_module.md#examples)

## [Synopsis](vertica_user_module.md#id1)

- Adds or removes Vertica database user and, optionally, assigns roles.
- A user will not be removed until all the dependencies have been dropped.
- In such a situation, if the module tries to remove the user it will fail and only remove roles granted to the user.

## [Requirements](vertica_user_module.md#id2)

The below requirements are needed on the host that executes this module.

- unixODBC
- pyodbc

## [Parameters](vertica_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cluster**  string | Name of the Vertica cluster.  Default: `"localhost"` |
| **db**  string | Name of the Vertica database. |
| **expired**  boolean | Sets the user’s password expiration.  Choices:   - `false` - `true` |
| **ldap**  boolean | Set to true if users are authenticated via LDAP.  The user will be created with password expired and set to *$ldap$*.  Choices:   - `false` - `true` |
| **login_password**  string | The password used to authenticate with. |
| **login_user**  string | The username used to authenticate with.  Default: `"dbadmin"` |
| **password**  string | The user’s password encrypted by the MD5 algorithm.  The password must be generated with the format `"md5" + md5[password + username]`, resulting in a total of 35 characters. An easy way to do this is by querying the Vertica database with select ‘md5’||md5(’<user_password><user_name>’). |
| **port**  string | Vertica cluster port to connect to.  Default: `"5433"` |
| **profile**  string | Sets the user’s profile. |
| **resource_pool**  string | Sets the user’s resource pool. |
| **roles**  aliases: role  string | Comma separated list of roles to assign to the user. |
| **state**  string | Whether to create `present`, drop `absent` or lock `locked` a user.  Choices:   - `"present"` ← (default) - `"absent"` - `"locked"` |
| **user**  aliases: name  string / required | Name of the user to add or remove. |

## [Notes](vertica_user_module.md#id4)

> **Note:**
>
> - The default authentication assumes that you are either logging in as or sudo’ing to the `dbadmin` account on the host.
> - This module uses `pyodbc`, a Python ODBC database adapter. You must ensure that `unixODBC` and `pyodbc` is installed on the host and properly configured.
> - Configuring `unixODBC` for Vertica requires `Driver = /opt/vertica/lib64/libverticaodbc.so` to be added to the `Vertica` section of either `/etc/odbcinst.ini` or `$HOME/.odbcinst.ini` and both `ErrorMessagesPath = /opt/vertica/lib64` and `DriverManagerEncoding = UTF-16` to be added to the `Driver` section of either `/etc/vertica.ini` or `$HOME/.vertica.ini`.

## [Examples](vertica_user_module.md#id5)

```yaml+jinja
- name: Creating a new vertica user with password
  community.general.vertica_user: name=user_name password=md5<encrypted_password> db=db_name state=present

- name: Creating a new vertica user authenticated via ldap with roles assigned
  community.general.vertica_user:
    name=user_name
    ldap=true
    db=db_name
    roles=schema_name_ro
    state=present
```

### Authors

- Dariusz Owczarek (@dareko)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
