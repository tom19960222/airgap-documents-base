---
collection: ansible
version: "8"
title: "lowlydba.sqlserver.user module – Configures a user within a database"
source_url: https://docs.ansible.com/projects/ansible/8/collections/lowlydba/sqlserver/user_module.html
fetched_at: 2026-07-28T01:05:51+00:00
---
# lowlydba.sqlserver.user module – Configures a user within a database

> **Note:**
>
> This module is part of the [lowlydba.sqlserver collection](https://galaxy.ansible.com/ui/repo/published/lowlydba/sqlserver/) (version 2.2.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install lowlydba.sqlserver`.
> You need further requirements to be able to use this module,
> see [Requirements](user_module.md#ansible-collections-lowlydba-sqlserver-user-module-requirements) for details.
>
> To use it in a playbook, specify: `lowlydba.sqlserver.user`.

New in lowlydba.sqlserver 1.1.0

- [Synopsis](user_module.md#synopsis)
- [Requirements](user_module.md#requirements)
- [Parameters](user_module.md#parameters)
- [Attributes](user_module.md#attributes)
- [Examples](user_module.md#examples)
- [Return Values](user_module.md#return-values)

## [Synopsis](user_module.md#id1)

- Creates, modifies, or removes a user in a database.

## [Requirements](user_module.md#id2)

The below requirements are needed on the host that executes this module.

- [dbatools](https://www.powershellgallery.com/packages/dbatools/) PowerShell module

## [Parameters](user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **database**  string / required | Database for the user. |
| **default_schema**  string | The default database schema for the user.  **Default:** `"dbo"` |
| **external_provider**  boolean | Specifies that the user is for Azure AD Authentication. Only used when creating a new user, this cannot be modified for an existing user.  **Choices:**   - `false` - `true` |
| **login**  string / required | Name of the login that the user is mapped to. |
| **sql_instance**  string / required | The SQL Server instance to modify. |
| **sql_password**  string | Password for SQL Authentication. |
| **sql_username**  string | Username for SQL Authentication. |
| **state**  string | Whether or not the object should be `present` or `absent`.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **username**  string / required | Name of the user. |

## [Attributes](user_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target. |
| **platform** | **Platforms:** **all** | Target OS/families that can be operated against. |

## [Examples](user_module.md#id5)

```yaml+jinja
- name: Create a user
  lowlydba.sqlserver.user:
    sql_instance: sql-01.myco.io
    login: TheIntern
    username: TheIntern
    database: InternProject1

- name: Change user's schema
  lowlydba.sqlserver.login:
    sql_instance: sql-01.myco.io
    login: TheIntern
    username: TheIntern
    database: InternProject1
    default_schema: dev

- name: Remove a user
  lowlydba.sqlserver.login:
    sql_instance: sql-01.myco.io
    login: TheIntern
    username: TheIntern
    database: InternProject1
    state: absent
```

## [Return Values](user_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | Output from the `New-DbaDbUser`, `Get-DbaDbUser`, or `Remove-DbaDbUser` function.  **Returned:** success, but not in check_mode. |

### Authors

- John McCall (@lowlydba)

### Collection links

- [Issue Tracker](https://github.com/LowlyDBA/lowlydba.sqlserver/issues)
- [Repository (Sources)](https://github.com/LowlyDBA/lowlydba.sqlserver)
