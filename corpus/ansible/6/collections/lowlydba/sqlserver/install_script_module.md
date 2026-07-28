---
collection: ansible
version: "6"
title: "lowlydba.sqlserver.install_script module – Runs migration scripts against a database"
source_url: https://docs.ansible.com/projects/ansible/6/collections/lowlydba/sqlserver/install_script_module.html
fetched_at: 2026-07-27T17:55:09+00:00
---
# lowlydba.sqlserver.install_script module – Runs migration scripts against a database

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
> see [Requirements](install_script_module.md#ansible-collections-lowlydba-sqlserver-install-script-module-requirements) for details.
>
> To use it in a playbook, specify: `lowlydba.sqlserver.install_script`.

New in lowlydba.sqlserver 0.11.0

- [Synopsis](install_script_module.md#synopsis)
- [Requirements](install_script_module.md#requirements)
- [Parameters](install_script_module.md#parameters)
- [Attributes](install_script_module.md#attributes)
- [Examples](install_script_module.md#examples)
- [Return Values](install_script_module.md#return-values)

## [Synopsis](install_script_module.md#id1)

- Uses the module `DBOps` to run `Dbo-InstallScript` against a target SQL Server database.

## [Requirements](install_script_module.md#id2)

The below requirements are needed on the host that executes this module.

- [dbatools](https://www.powershellgallery.com/packages/dbatools/) PowerShell module
- [dbops](https://github.com/dataplat/dbops) PowerShell module

## [Parameters](install_script_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **connection_timeout**  integer | Database server connection timeout in seconds. Only affects connection attempts. Does not affect execution timeout.  Default: `30` |
| **create_database**  boolean | Will create an empty database if missing.  Choices:   - `false` ← (default) - `true` |
| **database**  string / required | Name of the target database. |
| **deployment_method**  string | `SingleTransaction` - wrap all the deployment scripts into a single transaction and rollback whole deployment on error.  `TransactionPerScript` - wrap each script into a separate transaction; rollback single script deployment in case of error.  `NoTransaction` - deploy as is.  Choices:   - `"NoTransaction"` ← (default) - `"SingleTransaction"` - `"TransactionPerScript"` |
| **execution_timeout**  integer | Script execution timeout. The script will be aborted if the execution takes more than specified number of seconds.  Default: `0` |
| **match**  string | Runs a regex verification against provided file names using the provided string. |
| **no_log_version**  boolean | If set, the deployment will not be tracked in the database. That will also mean that all the scripts and all the builds from the package are going to be deployed regardless of any previous deployment history.  Choices:   - `false` ← (default) - `true` |
| **no_recurse**  boolean | Only process the first level of the target path.  Choices:   - `false` ← (default) - `true` |
| **output_file**  string | Log output into specified file. |
| **path**  string / required | Directory where targeted sql scripts are stored. |
| **schema_version_table**  string | A table that will hold the history of script execution. This table is used to choose what scripts are going to be run during the deployment, preventing the scripts from being execured twice. |
| **sql_instance**  string / required | The SQL Server instance to modify. |
| **sql_password**  string | Password for SQL Authentication. |
| **sql_username**  string | Username for SQL Authentication. |

## [Attributes](install_script_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full | Can run in check_mode and return changed status prediction without modifying target. |
| **platform** | Platforms: all | Target OS/families that can be operated against. |

## [Examples](install_script_module.md#id5)

```yaml+jinja
- name: Migrate a database
  lowlydba.sqlserver.install_script:
    sql_instance: test-server.my.company.com
    database: AdventureWorks
    path: migrations
```

## [Return Values](install_script_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | Modified output from the `Install-DboScript` function.  Returned: success, but not in check_mode. |

### Authors

- John McCall (@lowlydba)

### Collection links

[Issue Tracker](https://github.com/LowlyDBA/lowlydba.sqlserver/issues)
[Repository (Sources)](https://github.com/LowlyDBA/lowlydba.sqlserver)
