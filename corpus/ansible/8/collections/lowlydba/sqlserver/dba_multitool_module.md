---
collection: ansible
version: "8"
title: "lowlydba.sqlserver.dba_multitool module – Install/update the DBA Multitool suite by John McCall"
source_url: https://docs.ansible.com/projects/ansible/8/collections/lowlydba/sqlserver/dba_multitool_module.html
fetched_at: 2026-07-28T02:40:30+00:00
---
# lowlydba.sqlserver.dba_multitool module – Install/update the DBA Multitool suite by John McCall

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
> see [Requirements](dba_multitool_module.md#ansible-collections-lowlydba-sqlserver-dba-multitool-module-requirements) for details.
>
> To use it in a playbook, specify: `lowlydba.sqlserver.dba_multitool`.

New in lowlydba.sqlserver 0.7.0

- [Synopsis](dba_multitool_module.md#synopsis)
- [Requirements](dba_multitool_module.md#requirements)
- [Parameters](dba_multitool_module.md#parameters)
- [Attributes](dba_multitool_module.md#attributes)
- [Examples](dba_multitool_module.md#examples)
- [Return Values](dba_multitool_module.md#return-values)

## [Synopsis](dba_multitool_module.md#id1)

- A wrapper for `Install-DbaMultiTool` to fetch the latest version of the scripts, or install from a local cached version.

## [Requirements](dba_multitool_module.md#id2)

The below requirements are needed on the host that executes this module.

- [dbatools](https://www.powershellgallery.com/packages/dbatools/) PowerShell module

## [Parameters](dba_multitool_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **branch**  string | Specifies an alternate branch of the DBA MultiTool to install.  **Choices:**   - `"master"` - `"development"` |
| **database**  string / required | Name of the target database. |
| **force**  boolean | If this switch is enabled, the DBA MultiTool will be downloaded from the internet even if previously cached.  **Choices:**   - `false` ← (default) - `true` |
| **local_file**  string | Specifies the path to a local file to install DBA MultiTool from. This should be the zip file as distributed by the maintainers.  If this option is not specified, the latest version will be downloaded and installed from <https://github.com/LowlyDBA/dba-multitool/>. |
| **sql_instance**  string / required | The target SQL Server instance or instances. Server version must be SQL Server version 2005 or higher. |
| **sql_password**  string | Password for SQL Authentication. |
| **sql_username**  string | Username for SQL Authentication. |

## [Attributes](dba_multitool_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target. |
| **platform** | **Platforms:** **all** | Target OS/families that can be operated against. |

## [Examples](dba_multitool_module.md#id5)

```yaml+jinja
- name: Install DBA MultiTool
  lowlydba.sqlserver.dba_multitool:
    sql_instance: test-server.my.company.com
    database: dba_tools
```

## [Return Values](dba_multitool_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | Modified output from the `Install-DbaMultitool` function.  **Returned:** success, but not in check_mode. |

### Authors

- John McCall (@lowlydba)

### Collection links

- [Issue Tracker](https://github.com/LowlyDBA/lowlydba.sqlserver/issues)
- [Repository (Sources)](https://github.com/LowlyDBA/lowlydba.sqlserver)
