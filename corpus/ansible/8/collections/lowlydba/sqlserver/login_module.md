---
collection: ansible
version: "8"
title: "lowlydba.sqlserver.login module – Configures a login for the target SQL Server instance"
source_url: https://docs.ansible.com/projects/ansible/8/collections/lowlydba/sqlserver/login_module.html
fetched_at: 2026-07-28T02:40:33+00:00
---
# lowlydba.sqlserver.login module – Configures a login for the target SQL Server instance

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
> see [Requirements](login_module.md#ansible-collections-lowlydba-sqlserver-login-module-requirements) for details.
>
> To use it in a playbook, specify: `lowlydba.sqlserver.login`.

New in lowlydba.sqlserver 0.1.0

- [Synopsis](login_module.md#synopsis)
- [Requirements](login_module.md#requirements)
- [Parameters](login_module.md#parameters)
- [Attributes](login_module.md#attributes)
- [Notes](login_module.md#notes)
- [Examples](login_module.md#examples)
- [Return Values](login_module.md#return-values)

## [Synopsis](login_module.md#id1)

- Creates, modifies, or removes a Windows or SQL Authentication login on a SQL Server instance.

## [Requirements](login_module.md#id2)

The below requirements are needed on the host that executes this module.

- [dbatools](https://www.powershellgallery.com/packages/dbatools/) PowerShell module

## [Parameters](login_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **default_database**  string | Default database for the login. |
| **enabled**  boolean  *added in lowlydba.sqlserver 0.4.0* | Whether the login is enabled or disabled.  **Choices:**   - `false` - `true` ← (default) |
| **language**  string | Default language for the login. Only used when creating a new login, not when modifying an existing one. |
| **login**  string / required | Name of the login to configure. |
| **password**  string | Password for the login, if SQL Authentication login. |
| **password_expiration_enabled**  boolean | Enforces password expiration policy. Requires *password_policy_enforced=true*.  **Choices:**   - `false` - `true` |
| **password_must_change**  boolean | Enforces user must change password at next login.  When specified will enforce *password_expiration_enabled* and *password_policy_enforced* as they are required.  **Choices:**   - `false` - `true` |
| **password_policy_enforced**  boolean | Enforces password complexity policy.  **Choices:**   - `false` - `true` |
| **sid**  string  *added in lowlydba.sqlserver 2.1.0* | Provide an explicit Sid that should be used when creating the account. |
| **sql_instance**  string / required | The SQL Server instance to modify. |
| **sql_password**  string | Password for SQL Authentication. |
| **sql_username**  string | Username for SQL Authentication. |
| **state**  string | Whether or not the object should be `present` or `absent`.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Attributes](login_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target. |
| **platform** | **Platforms:** **all** | Target OS/families that can be operated against. |

## [Notes](login_module.md#id5)

> **Note:**
>
> - Module will always return changed if a password is supplied.

## [Examples](login_module.md#id6)

```yaml+jinja
- name: Create a login
  lowlydba.sqlserver.login:
    sql_instance: sql-01.myco.io
    login: TheIntern
    password: ReallyComplexStuff12345!

- name: Disable a login
  lowlydba.sqlserver.login:
    sql_instance: sql-01.myco.io
    login: TheIntern
    enabled: false
```

## [Return Values](login_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | Output from the `New-DbaLogin`, `Set-DbaLogin`, or `Remove-DbaLogin` function.  **Returned:** success, but not in check_mode. |

### Authors

- John McCall (@lowlydba)

### Collection links

- [Issue Tracker](https://github.com/LowlyDBA/lowlydba.sqlserver/issues)
- [Repository (Sources)](https://github.com/LowlyDBA/lowlydba.sqlserver)
