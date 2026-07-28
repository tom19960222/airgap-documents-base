---
collection: ansible
version: "8"
title: "lowlydba.sqlserver.sa module – Configure the sa login for security best practices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/lowlydba/sqlserver/sa_module.html
fetched_at: 2026-07-28T02:40:39+00:00
---
# lowlydba.sqlserver.sa module – Configure the `sa` login for security best practices

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
> see [Requirements](sa_module.md#ansible-collections-lowlydba-sqlserver-sa-module-requirements) for details.
>
> To use it in a playbook, specify: `lowlydba.sqlserver.sa`.

New in lowlydba.sqlserver 0.3.0

- [Synopsis](sa_module.md#synopsis)
- [Requirements](sa_module.md#requirements)
- [Parameters](sa_module.md#parameters)
- [Attributes](sa_module.md#attributes)
- [Examples](sa_module.md#examples)
- [Return Values](sa_module.md#return-values)

## [Synopsis](sa_module.md#id1)

- Rename, disable, and reset the password for the `sa` login on a SQL Server instance per best practices.

## [Requirements](sa_module.md#id2)

The below requirements are needed on the host that executes this module.

- [dbatools](https://www.powershellgallery.com/packages/dbatools/) PowerShell module

## [Parameters](sa_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **enabled**  boolean  *added in lowlydba.sqlserver 0.4.0* | Whether the login is enabled or disabled.  **Choices:**   - `false` - `true` ← (default) |
| **new_name**  string | The new name to rename the `sa` login to. |
| **password**  string | Password for the login. |
| **password_expiration_enabled**  boolean | Enforces password expiration policy. Requires *password_policy_enforced=true*.  **Choices:**   - `false` - `true` |
| **password_must_change**  boolean | Enforces user must change password at next login.  When specified, will enforce *password_expiration_enabled* and *password_policy_enforced* as they are required.  **Choices:**   - `false` - `true` |
| **password_policy_enforced**  boolean | Enforces password complexity policy.  **Choices:**   - `false` - `true` |
| **sql_instance**  string / required | The SQL Server instance to modify. |
| **sql_password**  string | Password for SQL Authentication. |
| **sql_username**  string | Username for SQL Authentication. |

## [Attributes](sa_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target. |
| **platform** | **Platforms:** **all** | Target OS/families that can be operated against. |

## [Examples](sa_module.md#id5)

```yaml+jinja
- name: Disable sa login
  lowlydba.sqlserver.sa:
    sql_instance: sql-01.myco.io
    enabled: false

- name: Rename sa login
  lowlydba.sqlserver.sa:
    sql_instance: sql-01.myco.io
    new_name: 'notthesayourelookingfor'
```

## [Return Values](sa_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | Output from the `Set-DbaLogin` function.  **Returned:** success, but not in check_mode. |

### Authors

- John McCall (@lowlydba)

### Collection links

- [Issue Tracker](https://github.com/LowlyDBA/lowlydba.sqlserver/issues)
- [Repository (Sources)](https://github.com/LowlyDBA/lowlydba.sqlserver)
