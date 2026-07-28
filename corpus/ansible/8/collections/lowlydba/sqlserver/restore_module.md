---
collection: ansible
version: "8"
title: "lowlydba.sqlserver.restore module – Performs a restore operation"
source_url: https://docs.ansible.com/projects/ansible/8/collections/lowlydba/sqlserver/restore_module.html
fetched_at: 2026-07-28T02:40:37+00:00
---
# lowlydba.sqlserver.restore module – Performs a restore operation

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
> see [Requirements](restore_module.md#ansible-collections-lowlydba-sqlserver-restore-module-requirements) for details.
>
> To use it in a playbook, specify: `lowlydba.sqlserver.restore`.

New in lowlydba.sqlserver 0.9.0

- [Synopsis](restore_module.md#synopsis)
- [Requirements](restore_module.md#requirements)
- [Parameters](restore_module.md#parameters)
- [Attributes](restore_module.md#attributes)
- [Examples](restore_module.md#examples)
- [Return Values](restore_module.md#return-values)

## [Synopsis](restore_module.md#id1)

- Performs a database restore operation.

## [Requirements](restore_module.md#id2)

The below requirements are needed on the host that executes this module.

- [dbatools](https://www.powershellgallery.com/packages/dbatools/) PowerShell module

## [Parameters](restore_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **azure_credential**  string | The name of the SQL Server credential to be used if restoring from an Azure hosted backup using Storage Access Keys. |
| **block_size**  string | Specifies block size to use.  **Choices:**   - `"0.5kb"` - `"1kb"` - `"2kb"` - `"4kb"` - `"8kb"` - `"16kb"` - `"32kb"` - `"64kb"` |
| **buffer_count**  integer | Number of I/O buffers to use.  **Default:** `0` |
| **database**  string | The database to process. |
| **destination_data_directory**  string | Path to restore the SQL Server backups to on the target instance.  If only this option is specified, then all database files (data and log) will be restored to this location |
| **destination_file_prefix**  string | This value will be prefixed to **all** restored files (log and data). |
| **destination_file_suffix**  string | This value will be suffixed to **all** restored files (log and data). |
| **destination_filestream_directory**  string | Path to restore FileStream data to.  This option can only be specified alongside *destination_data_directory*. |
| **destination_log_directory**  string | Path to restore the database log files to.  This option can only be specified alongside *destination_data_directory*. |
| **directory_recurse**  boolean | If specified the specified directory will be recursed into (overriding the default behaviour).  **Choices:**   - `false` ← (default) - `true` |
| **ignore_diff_backup**  boolean | Indicates to skip restoring any differential backups.  **Choices:**   - `false` ← (default) - `true` |
| **ignore_log_backup**  boolean | Indicates to skip restoring any log backups.  **Choices:**   - `false` ← (default) - `true` |
| **keep_cdc**  boolean | Indicates whether CDC information should be restored as part of the database.  **Choices:**   - `false` - `true` |
| **keep_replication**  boolean | Indicates whether replication configuration should be restored as part of the database restore operation.  **Choices:**   - `false` ← (default) - `true` |
| **maintenance_solution_backup**  boolean | Switch to indicate the backup files are in a folder structure as created by Ola Hallengreen’s maintenance scripts.  This allows for faster file parsing.  **Choices:**   - `false` ← (default) - `true` |
| **max_transfer_size**  integer | Sets the size of the unit of transfer. Values must be a multiple of 64kb.  **Default:** `0` |
| **no_recovery**  boolean | Indicates if the databases should be recovered after last restore.  **Choices:**   - `false` ← (default) - `true` |
| **no_xp_dir_recurse**  boolean | If specified, prevents the `XpDirTree` process from recursing (its default behaviour).  **Choices:**   - `false` ← (default) - `true` |
| **path**  string / required | Path to SQL Server backup files.  Paths passed in as strings will be scanned using the desired method, default is a recursive folder scan.  Accepts multiple paths separated by `,`. |
| **replace_db_name_in_file**  boolean | If switch set any occurrence of the original database’s name in a data or log file will be replace with the name specified in the *database_name* option.  **Choices:**   - `false` - `true` |
| **restore_time**  string | Specify a datetime string `HH:MM:SS MM/DD/YYYY` to which you want the database restored to.  Default is to the latest point available in the specified backups. |
| **restored_database_name_prefix**  string | A string which will be prefixed to the start of the restore Database’s name. |
| **reuse_source_folder_structure**  boolean | By default, databases will be migrated to the destination Sql Server’s default data and log directories.  You can override this by using `reuse_source_folder_structure`.  **Choices:**   - `false` - `true` |
| **sql_instance**  string / required | The SQL Server instance to modify. |
| **sql_password**  string | Password for SQL Authentication. |
| **sql_username**  string | Username for SQL Authentication. |
| **standby_directory**  string | If a directory is specified the database(s) will be restored into a standby state, with the standby file placed into this directory (which must exist, and be writable by the target Sql Server instance). |
| **stop_after_date**  string | By default the restore will stop at the first occurence of *stop_mark* found in the chain, passing a datetime string `HH:MM:SS MM/DD/YYYY` will cause it to stop the first *stop_mark* after that datetime. |
| **stop_before**  boolean | Switch to indicate the restore should stop before *stop_mark* occurs, default is to stop when mark is created.  **Choices:**   - `false` ← (default) - `true` |
| **stop_mark**  string | Marked point in the transaction log to stop the restore at. |
| **use_destination_default_directories**  boolean | Switch that tells the restore to use the default Data and Log locations on the target server.  If they don’t exist, the function will try to create them.  **Choices:**   - `false` - `true` |
| **verify_only**  boolean | Indicates the restore should be verified only.  **Choices:**   - `false` ← (default) - `true` |
| **with_replace**  boolean | Indicates if the restore is allowed to replace an existing database.  **Choices:**   - `false` ← (default) - `true` |
| **xp_dirtree**  boolean | Switch that indicated file scanning should be performed by the SQL Server instance using `xp_dirtree`.  This will scan recursively from the passed in path.  You must have sysadmin role membership on the instance for this to work.  **Choices:**   - `false` - `true` |

## [Attributes](restore_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target. |
| **platform** | **Platforms:** **all** | Target OS/families that can be operated against. |

## [Examples](restore_module.md#id5)

```yaml+jinja
- name: Restore a Database
  lowlydba.sqlserver.restore:
    sql_instance: sql-01.myco.io
    database: LowlyDB

- name: Restore a Database and allow future T-Log restores
  lowlydba.sqlserver.restore:
    sql_instance: sql-01.myco.io
    database: LowlyDB1
    no_recovery: true

- name: Verify backup files, no restore
  lowlydba.sqlserver.restore:
    sql_instance: sql-01.myco.io
    database: LowlyDB2
    verify_only: true
```

## [Return Values](restore_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | Modified output from the `Restore-DbaDatabase` function.  **Returned:** success, but not in check_mode. |

### Authors

- John McCall (@lowlydba)

### Collection links

- [Issue Tracker](https://github.com/LowlyDBA/lowlydba.sqlserver/issues)
- [Repository (Sources)](https://github.com/LowlyDBA/lowlydba.sqlserver)
