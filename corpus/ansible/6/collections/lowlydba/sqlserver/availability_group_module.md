---
collection: ansible
version: "6"
title: "lowlydba.sqlserver.availability_group module – Configures availability group(s)"
source_url: https://docs.ansible.com/projects/ansible/6/collections/lowlydba/sqlserver/availability_group_module.html
fetched_at: 2026-07-27T17:55:05+00:00
---
# lowlydba.sqlserver.availability_group module – Configures availability group(s)

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
> see [Requirements](availability_group_module.md#ansible-collections-lowlydba-sqlserver-availability-group-module-requirements) for details.
>
> To use it in a playbook, specify: `lowlydba.sqlserver.availability_group`.

New in lowlydba.sqlserver 0.4.0

- [Synopsis](availability_group_module.md#synopsis)
- [Requirements](availability_group_module.md#requirements)
- [Parameters](availability_group_module.md#parameters)
- [Attributes](availability_group_module.md#attributes)
- [Examples](availability_group_module.md#examples)
- [Return Values](availability_group_module.md#return-values)

## [Synopsis](availability_group_module.md#id1)

- Configures SQL Server Availability Group(s) with up to one replica.

## [Requirements](availability_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- [dbatools](https://www.powershellgallery.com/packages/dbatools/) PowerShell module

## [Parameters](availability_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ag_name**  string / required | Name of the Availability Group. |
| **all_ags**  boolean | Apply changes to all availability groups on the instance. Only used for configuring existing availability groups.  Choices:   - `false` - `true` |
| **allow_null_backup**  boolean | Allow taking a full backup to `NULL` if one does not exist and *seeding_mode=Automatic*.  Choices:   - `false` - `true` |
| **automated_backup_preference**  string | How to handle backup requests by default.  Choices:   - `"None"` - `"Primary"` - `"Secondary"` ← (default) - `"SecondaryOnly"` |
| **availability_mode**  string | Whether the replica should be Asynchronous or Synchronous.  Only used in creating a new availability group.  Choices:   - `"AsynchronousCommit"` - `"SynchronousCommit"` ← (default) |
| **basic_availability_group**  boolean | Indicates whether the availability group is Basic Availability Group.  Choices:   - `false` - `true` |
| **cluster_type**  string | Cluster type of the Availability Group. Only supported in SQL Server 2017 and above.  Choices:   - `"Wsfc"` ← (default) - `"External"` - `"None"` |
| **database**  aliases: database_name  string | Name of the database to create the Availability Group for. |
| **database_health_trigger**  boolean | Indicates whether the availability group triggers the database health.  Choices:   - `false` - `true` |
| **dtc_support_enabled**  boolean | Enables Dtc support.  Choices:   - `false` - `true` |
| **failover_mode**  string | Whether the replica have Automatic or Manual failover.  Choices:   - `"Automatic"` ← (default) - `"Manual"` |
| **failure_condition_level**  string | Specifies the different conditions that can trigger an automatic failover in Availability Group.  Choices:   - `"OnAnyQualifiedFailureCondition"` - `"OnCriticalServerErrors"` - `"OnModerateServerErrors"` - `"OnServerDown"` - `"OnServerUnresponsive"` |
| **force**  boolean | Drop and recreate the database on remote servers using fresh backup.  Choices:   - `false` - `true` |
| **healthcheck_timeout**  integer | This setting used to specify the length of time, in milliseconds, that the SQL Server resource DLL should wait for information returned by the `sp_server_diagnostics` stored procedure before reporting the Always On Failover Cluster Instance (FCI) as unresponsive.  Changes that are made to the timeout settings are effective immediately and do not require a restart of the SQL Server resource. |
| **is_distributed_ag**  boolean | Indicates whether the availability group is distributed.  Choices:   - `false` - `true` |
| **seeding_mode**  string | Default seeding mode for the replica. Should remain as the default otherwise manual setup may be required.  Choices:   - `"Automatic"` - `"Manual"` ← (default) |
| **shared_path**  string | The network share where the backups will be backed up and restored from. |
| **sql_instance**  string / required | The SQL Server instance to modify. |
| **sql_instance_secondary**  string | The secondary SQL Server instance for the new Availability Group. |
| **sql_password**  string | Password for SQL Authentication. |
| **sql_password_secondary**  string | Password for SQL Authentication for the secondary replica. |
| **sql_username**  string | Username for SQL Authentication. |
| **sql_username_secondary**  string | Username for SQL Authentication for the secondary replica. |
| **state**  string | Whether or not the object should be `present` or `absent`.  Choices:   - `"present"` ← (default) - `"absent"` |
| **use_last_backup**  boolean | Use the last full and log backup of database. A log backup must be the last backup.  Choices:   - `false` - `true` |

## [Attributes](availability_group_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full | Can run in check_mode and return changed status prediction without modifying target. |
| **platform** | Platforms: all | Target OS/families that can be operated against. |

## [Examples](availability_group_module.md#id5)

```yaml+jinja
- name: Create Availability Group
  lowlydba.sqlserver.availability_group:
    sql_instance: sql-01.myco.io
    ag_name: AG_MyDatabase
```

## [Return Values](availability_group_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | Output from the `New-DbaAvailabilityGroup` or `Set-DbaAvailabilityGroup` function.  Returned: success, but not in check_mode. |

### Authors

- John McCall (@lowlydba)

### Collection links

[Issue Tracker](https://github.com/LowlyDBA/lowlydba.sqlserver/issues)
[Repository (Sources)](https://github.com/LowlyDBA/lowlydba.sqlserver)
