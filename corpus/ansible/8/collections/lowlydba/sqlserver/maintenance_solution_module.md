---
collection: ansible
version: "8"
title: "lowlydba.sqlserver.maintenance_solution module – Install/update Maintenance Solution by Ola Hallengren"
source_url: https://docs.ansible.com/projects/ansible/8/collections/lowlydba/sqlserver/maintenance_solution_module.html
fetched_at: 2026-07-28T02:40:34+00:00
---
# lowlydba.sqlserver.maintenance_solution module – Install/update Maintenance Solution by Ola Hallengren

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
> see [Requirements](maintenance_solution_module.md#ansible-collections-lowlydba-sqlserver-maintenance-solution-module-requirements) for details.
>
> To use it in a playbook, specify: `lowlydba.sqlserver.maintenance_solution`.

New in lowlydba.sqlserver 0.1.0

- [Synopsis](maintenance_solution_module.md#synopsis)
- [Requirements](maintenance_solution_module.md#requirements)
- [Parameters](maintenance_solution_module.md#parameters)
- [Attributes](maintenance_solution_module.md#attributes)
- [Examples](maintenance_solution_module.md#examples)
- [Return Values](maintenance_solution_module.md#return-values)

## [Synopsis](maintenance_solution_module.md#id1)

- A wrapper for `Install-DbaMaintenanceSolution` to fetch the latest version of the Ola Hallengren’s Maintenance Solution, or install from a local cached version.

## [Requirements](maintenance_solution_module.md#id2)

The below requirements are needed on the host that executes this module.

- [dbatools](https://www.powershellgallery.com/packages/dbatools/) PowerShell module

## [Parameters](maintenance_solution_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **backup_location**  string | Location of the backup root directory. If this is not supplied, the default backup directory will be used. |
| **cleanup_time**  integer | Time in hours, after which backup files are deleted.  **Default:** `0` |
| **database**  string / required | Name of the target database. |
| **force**  boolean | If this switch is enabled, the Maintenance Solution will be downloaded from the internet even if previously cached.  **Choices:**   - `false` ← (default) - `true` |
| **install_jobs**  boolean | If this switch is enabled, the corresponding SQL Agent Jobs will be created.  **Choices:**   - `false` ← (default) - `true` |
| **install_parallel**  boolean | If this switch is enabled, the `Queue` and `QueueDatabase` tables are created, for use when `@DatabasesInParallel = 'Y'` are set in the jobs.  **Choices:**   - `false` ← (default) - `true` |
| **local_file**  string | Specifies the path to a local file to install Ola’s solution from. This should be the zip file as distributed by the maintainers.  If this option is not specified, the latest version will be downloaded and installed from the [Maintenance Solution Github](https://github.com/olahallengren/sql-server-maintenance-solution). |
| **log_to_table**  boolean | If this switch is enabled, the Maintenance Solution will be configured to log commands to a table.  **Choices:**   - `false` ← (default) - `true` |
| **output_file_dir**  string | Specify the output file directory where the Maintenance Solution will write to. |
| **replace_existing**  boolean | If this switch is enabled, objects already present in the target database will be dropped and recreated.  **Choices:**   - `false` - `true` |
| **solution**  string | Specifies which portion of the Maintenance Solution to install.  **Choices:**   - `"All"` ← (default) - `"Backup"` - `"IntegrityCheck"` - `"IndexOptimize"` |
| **sql_instance**  string / required | The SQL Server instance to modify. |
| **sql_password**  string | Password for SQL Authentication. |
| **sql_username**  string | Username for SQL Authentication. |

## [Attributes](maintenance_solution_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target. |
| **platform** | **Platforms:** **all** | Target OS/families that can be operated against. |

## [Examples](maintenance_solution_module.md#id5)

```yaml+jinja
- name: Install/Update Maintenance Solution
  lowlydba.sqlserver.multitool:
    sql_instance: sql-01.myco.io
    database: main
    replace_existing: true
```

## [Return Values](maintenance_solution_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | Output from the `Install-MaintenanceSolution` function.  **Returned:** success, but not in check_mode. |

### Authors

- John McCall (@lowlydba)

### Collection links

- [Issue Tracker](https://github.com/LowlyDBA/lowlydba.sqlserver/issues)
- [Repository (Sources)](https://github.com/LowlyDBA/lowlydba.sqlserver)
