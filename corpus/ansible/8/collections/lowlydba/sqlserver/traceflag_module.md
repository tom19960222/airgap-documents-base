---
collection: ansible
version: "8"
title: "lowlydba.sqlserver.traceflag module – Enable or disable global trace flags on a SQL Server instance"
source_url: https://docs.ansible.com/projects/ansible/8/collections/lowlydba/sqlserver/traceflag_module.html
fetched_at: 2026-07-28T02:40:43+00:00
---
# lowlydba.sqlserver.traceflag module – Enable or disable global trace flags on a SQL Server instance

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
> see [Requirements](traceflag_module.md#ansible-collections-lowlydba-sqlserver-traceflag-module-requirements) for details.
>
> To use it in a playbook, specify: `lowlydba.sqlserver.traceflag`.

New in lowlydba.sqlserver 0.1.0

- [Synopsis](traceflag_module.md#synopsis)
- [Requirements](traceflag_module.md#requirements)
- [Parameters](traceflag_module.md#parameters)
- [Attributes](traceflag_module.md#attributes)
- [Examples](traceflag_module.md#examples)
- [Return Values](traceflag_module.md#return-values)

## [Synopsis](traceflag_module.md#id1)

- Enable\Disable global trace flag on a SQL Instance. This trace flag takes affect immediately and does not require SQL Instance restart.
- This setting does not persist after restart.

## [Requirements](traceflag_module.md#id2)

The below requirements are needed on the host that executes this module.

- [dbatools](https://www.powershellgallery.com/packages/dbatools/) PowerShell module

## [Parameters](traceflag_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **enabled**  boolean / required | Flag to enable or disable the trace flag.  **Choices:**   - `false` - `true` |
| **sql_instance**  string / required | The SQL Server instance to modify. |
| **sql_password**  string | Password for SQL Authentication. |
| **sql_username**  string | Username for SQL Authentication. |
| **trace_flag**  integer / required | Trace Flag number. |

## [Attributes](traceflag_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target. |
| **platform** | **Platforms:** **all** | Target OS/families that can be operated against. |

## [Examples](traceflag_module.md#id5)

```yaml+jinja
- name: Eliminate successful backup information from SQL Error Log
  lowlydba.sqlserver.traceflag:
    sql_instance: sql-01.myco.io
    trace_flag: 3226
    enabled: true

- name: Disable trace flag
  lowlydba.sqlserver.traceflag:
    sql_instance: sql-01.myco.io
    trace_flag: 3226
    enabled: false
```

## [Return Values](traceflag_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | Output from the `Enable-DbaTraceFlag` or `Disable-DbaTraceFlag` function.  **Returned:** success, but not in check_mode. |

### Authors

- Sudhir Koduri (@kodurisudhir)

### Collection links

- [Issue Tracker](https://github.com/LowlyDBA/lowlydba.sqlserver/issues)
- [Repository (Sources)](https://github.com/LowlyDBA/lowlydba.sqlserver)
