---
collection: ansible
version: "8"
title: "lowlydba.sqlserver.sp_configure module – Make instance level system configuration changes via sp_configure"
source_url: https://docs.ansible.com/projects/ansible/8/collections/lowlydba/sqlserver/sp_configure_module.html
fetched_at: 2026-07-28T02:40:40+00:00
---
# lowlydba.sqlserver.sp_configure module – Make instance level system configuration changes via `sp_configure`

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
> see [Requirements](sp_configure_module.md#ansible-collections-lowlydba-sqlserver-sp-configure-module-requirements) for details.
>
> To use it in a playbook, specify: `lowlydba.sqlserver.sp_configure`.

New in lowlydba.sqlserver 0.1.0

- [Synopsis](sp_configure_module.md#synopsis)
- [Requirements](sp_configure_module.md#requirements)
- [Parameters](sp_configure_module.md#parameters)
- [Attributes](sp_configure_module.md#attributes)
- [Examples](sp_configure_module.md#examples)
- [Return Values](sp_configure_module.md#return-values)

## [Synopsis](sp_configure_module.md#id1)

- Read instance level system configuration for a given configuration and update to a new value as provided.

## [Requirements](sp_configure_module.md#id2)

The below requirements are needed on the host that executes this module.

- [dbatools](https://www.powershellgallery.com/packages/dbatools/) PowerShell module

## [Parameters](sp_configure_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **name**  string / required | Name of the configuration that will be changed. |
| **sql_instance**  string / required | The SQL Server instance to modify. |
| **sql_password**  string | Password for SQL Authentication. |
| **sql_username**  string | Username for SQL Authentication. |
| **value**  integer / required | New value the configuration will be set to. |

## [Attributes](sp_configure_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target. |
| **platform** | **Platforms:** **all** | Target OS/families that can be operated against. |

## [Examples](sp_configure_module.md#id5)

```yaml+jinja
- name: Enable remote DAC connection
  lowlydba.sqlserver.sp_configure:
    sql_instance: sql-01.myco.io
    name: RemoteDacConnectionsEnabled
    value: 1
```

## [Return Values](sp_configure_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | Output from the `Set-DbaSpConfigure` function.  RestartRequired returned if the setting requires a service restart to take effect.  **Returned:** success, but not in check_mode. |

### Authors

- Sudhir Koduri (@kodurisudhir)

### Collection links

- [Issue Tracker](https://github.com/LowlyDBA/lowlydba.sqlserver/issues)
- [Repository (Sources)](https://github.com/LowlyDBA/lowlydba.sqlserver)
