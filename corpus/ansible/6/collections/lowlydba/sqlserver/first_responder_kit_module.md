---
collection: ansible
version: "6"
title: "lowlydba.sqlserver.first_responder_kit module – Install/update the First Responder Kit scripts"
source_url: https://docs.ansible.com/projects/ansible/6/collections/lowlydba/sqlserver/first_responder_kit_module.html
fetched_at: 2026-07-27T17:55:08+00:00
---
# lowlydba.sqlserver.first_responder_kit module – Install/update the First Responder Kit scripts

> **Note:**
>
> This module is part of the [lowlydba.sqlserver collection](https://galaxy.ansible.com/lowlydba/sqlserver) (version 1.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install lowlydba.sqlserver`.
> You need further requirements to be able to use this module,
> see [Requirements](first_responder_kit_module.md#ansible-collections-lowlydba-sqlserver-first-responder-kit-module-requirements) for details.
>
> To use it in a playbook, specify: `lowlydba.sqlserver.first_responder_kit`.

New in lowlydba.sqlserver 0.10.0

- [Synopsis](first_responder_kit_module.md#synopsis)
- [Requirements](first_responder_kit_module.md#requirements)
- [Parameters](first_responder_kit_module.md#parameters)
- [Attributes](first_responder_kit_module.md#attributes)
- [Examples](first_responder_kit_module.md#examples)
- [Return Values](first_responder_kit_module.md#return-values)

## [Synopsis](first_responder_kit_module.md#id1)

- A wrapper for `Install-DbaFirstResponderKit` to fetch the latest version of the scripts, or install from a local cached version.

## [Requirements](first_responder_kit_module.md#id2)

The below requirements are needed on the host that executes this module.

- [dbatools](https://www.powershellgallery.com/packages/dbatools/) PowerShell module

## [Parameters](first_responder_kit_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **branch**  string | Specifies an alternate branch of the First Responder Kit to install.  Choices:   - `"main"` - `"dev"` |
| **database**  string / required | Name of the target database. |
| **force**  boolean | If this switch is enabled, the FRK will be downloaded from the internet even if previously cached.  Choices:   - `false` ← (default) - `true` |
| **local_file**  string | Specifies the path to a local file to install FRK from. This should be the zip file as distributed by the maintainers.  If this option is not specified, the latest version will be downloaded and installed Github. |
| **only_script**  string | Specifies the name(s) of the script(s) to run for installation. Wildcards are permitted.  This way only part of the First Responder Kit can be installed.  Choices:   - `"Install-All-Scripts.sql"` ← (default) - `"Install-Core-Blitz-No-Query-Store.sql"` - `"Install-Core-Blitz-With-Query-Store.sql"` - `"sp_Blitz.sql"` - `"sp_BlitzFirst.sql"` - `"sp_BlitzIndex.sql"` - `"sp_BlitzCache.sql"` - `"sp_BlitzWho.sql"` - `"sp_BlitzQueryStore.sql"` - `"sp_BlitzAnalysis.sql"` - `"sp_BlitzBackups.sql"` - `"sp_BlitzInMemoryOLTP.sql"` - `"sp_BlitzLock.sql"` - `"sp_AllNightLog.sql"` - `"sp_AllNightLog_Setup.sql"` - `"sp_DatabaseRestore.sql"` - `"sp_ineachdb.sql"` - `"SqlServerVersions.sql"` - `"Uninstall.sql"` |
| **sql_instance**  string / required | The SQL Server instance to modify. |
| **sql_password**  string | Password for SQL Authentication. |
| **sql_username**  string | Username for SQL Authentication. |

## [Attributes](first_responder_kit_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full | Can run in check_mode and return changed status prediction without modifying target. |
| **platform** | Platforms: all | Target OS/families that can be operated against. |

## [Examples](first_responder_kit_module.md#id5)

```yaml+jinja
- name: Install FRK
  lowlydba.sqlserver.first_responder_kit:
    sql_instance: test-server.my.company.com
    database: dba_tools
```

## [Return Values](first_responder_kit_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | Modified output from the `Install-DbaFirstResponderKit` function.  Returned: success, but not in check_mode. |

### Authors

- John McCall (@lowlydba)

### Collection links

[Issue Tracker](https://github.com/LowlyDBA/lowlydba.sqlserver/issues)
[Repository (Sources)](https://github.com/LowlyDBA/lowlydba.sqlserver)
