---
collection: ansible
version: "8"
title: "lowlydba.sqlserver.backup module – Performs a backup operation"
source_url: https://docs.ansible.com/projects/ansible/8/collections/lowlydba/sqlserver/backup_module.html
fetched_at: 2026-07-28T02:40:28+00:00
---
# lowlydba.sqlserver.backup module – Performs a backup operation

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
> see [Requirements](backup_module.md#ansible-collections-lowlydba-sqlserver-backup-module-requirements) for details.
>
> To use it in a playbook, specify: `lowlydba.sqlserver.backup`.

New in lowlydba.sqlserver 0.8.0

- [Synopsis](backup_module.md#synopsis)
- [Requirements](backup_module.md#requirements)
- [Parameters](backup_module.md#parameters)
- [Attributes](backup_module.md#attributes)
- [Examples](backup_module.md#examples)
- [Return Values](backup_module.md#return-values)

## [Synopsis](backup_module.md#id1)

- Performs any type of database backup operation.

## [Requirements](backup_module.md#id2)

The below requirements are needed on the host that executes this module.

- [dbatools](https://www.powershellgallery.com/packages/dbatools/) PowerShell module

## [Parameters](backup_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **azure_base_url**  string | The URL to the base container of an Azure Storage account to write backups to. |
| **azure_credential**  string | The name of the credential on the SQL instance that can write to the *azure_base_url*, only needed if using Storage access keys If using SAS credentials, the command will look for a credential with a name matching the *azure_base_url*. |
| **block_size**  string | Specifies block size to use.  **Choices:**   - `"0.5kb"` - `"1kb"` - `"2kb"` - `"4kb"` - `"8kb"` - `"16kb"` - `"32kb"` - `"64kb"` |
| **buffer_count**  integer | Number of I/O buffers to use.  **Default:** `0` |
| **build_path**  boolean | By default this command will not attempt to create missing paths, this switch will change the behaviour so that it will.  **Choices:**   - `false` ← (default) - `true` |
| **checksum**  boolean | If set, the backup checksum will be calculated.  **Choices:**   - `false` ← (default) - `true` |
| **compress**  boolean | If set, use compression when creating the backup if it is supported by the version and edition.  **Choices:**   - `false` ← (default) - `true` |
| **copy_only**  boolean | The backup will be CopyOnly.  **Choices:**   - `false` ← (default) - `true` |
| **create_folder**  boolean | If set, database is backed up to its own subfolder within the path.  **Choices:**   - `false` ← (default) - `true` |
| **database**  string / required | The database to process. |
| **encryption_algorithm**  string | Specifies the Encryption Algorithm to used.  **Choices:**   - `"AES128"` - `"AES192"` - `"AES256"` - `"TRIPLEDES"` |
| **encryption_certificate**  string | The name of the certificate to be used to encrypt the backups. |
| **file_count**  integer | The number of striped files to create the backup with.  **Default:** `0` |
| **file_path**  string | The name of the file to backup to.  If no name is specified then the backup files will be named `DatabaseName_yyyyMMddHHmm` (i.e. `Database1_201714022131`) |
| **ignore_file_checks**  boolean | If set, stops the function from checking path validity.  **Choices:**   - `false` ← (default) - `true` |
| **increment_prefix**  boolean | If set, this will prefix backup files with an incrementing integer (ie; `1-`, `2-`).  Using this has been alleged to improved restore times on some Azure based SQL Database platforms.  **Choices:**   - `false` ← (default) - `true` |
| **initialize**  boolean | Initializes the media as part of the backup operation.  **Choices:**   - `false` ← (default) - `true` |
| **max_transfer_size**  integer | Sets the size of the unit of transfer. Values must be a multiple of 64kb.  **Default:** `0` |
| **no_recovery**  boolean | If set, performs a tail log backup.  **Choices:**   - `false` ← (default) - `true` |
| **path**  string | Path in which to place the backup files.  If not specified, the backups will be placed in the default backup location for SqlInstance. |
| **replace_in_name**  boolean | If set, the following list of strings will be replaced in the FilePath and Path strings. `instancename` - will be replaced with the instance Name `servername` - will be replaced with the server name `dbname` - will be replaced with the database name `timestamp` - will be replaced with the timestamp (either the default, or the format provided) `backuptype` - will be replaced with `Full`, `Log`, or `Differential` as appropriate  **Choices:**   - `false` ← (default) - `true` |
| **sql_instance**  string / required | The SQL Server instance to modify. |
| **sql_password**  string | Password for SQL Authentication. |
| **sql_username**  string | Username for SQL Authentication. |
| **timestamp_format**  string | By default the command timestamps backups using the format `yyyyMMddHHmm`. Using this option this can be overridden. |
| **type**  string | The type of backup to perform.  **Choices:**   - `"full"` - `"log"` - `"differential"` - `"diff"` - `"database"` ← (default) |
| **verify**  boolean | If set, the backup will be verified via `RESTORE VERIFYONLY`  **Choices:**   - `false` ← (default) - `true` |
| **with_format**  boolean | Formats the media as the first step of the backup operation.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](backup_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target. |
| **platform** | **Platforms:** **all** | Target OS/families that can be operated against. |

## [Examples](backup_module.md#id5)

```yaml+jinja
- name: Create striped full database backup in default dir
  lowlydba.sqlserver.backup:
    sql_instance: sql-01.myco.io
    database: LowlyDB
    type: full
    file_count: 8

- name: Create t-log backup
  lowlydba.sqlserver.backup:
    sql_instance: sql-01.myco.io
    database: LowlyDB
    type: log
```

## [Return Values](backup_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | Modified output from the `Backup-DbaDatabase` function.  **Returned:** success, but not in check_mode. |

### Authors

- John McCall (@lowlydba)

### Collection links

- [Issue Tracker](https://github.com/LowlyDBA/lowlydba.sqlserver/issues)
- [Repository (Sources)](https://github.com/LowlyDBA/lowlydba.sqlserver)
