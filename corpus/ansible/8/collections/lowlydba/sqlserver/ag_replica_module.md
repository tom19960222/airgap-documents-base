---
collection: ansible
version: "8"
title: "lowlydba.sqlserver.ag_replica module – Configures an availability group replica"
source_url: https://docs.ansible.com/projects/ansible/8/collections/lowlydba/sqlserver/ag_replica_module.html
fetched_at: 2026-07-28T02:40:22+00:00
---
# lowlydba.sqlserver.ag_replica module – Configures an availability group replica

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
> see [Requirements](ag_replica_module.md#ansible-collections-lowlydba-sqlserver-ag-replica-module-requirements) for details.
>
> To use it in a playbook, specify: `lowlydba.sqlserver.ag_replica`.

New in lowlydba.sqlserver 0.5.0

- [Synopsis](ag_replica_module.md#synopsis)
- [Requirements](ag_replica_module.md#requirements)
- [Parameters](ag_replica_module.md#parameters)
- [Attributes](ag_replica_module.md#attributes)
- [Examples](ag_replica_module.md#examples)
- [Return Values](ag_replica_module.md#return-values)

## [Synopsis](ag_replica_module.md#id1)

- Configures an availability group replica.

## [Requirements](ag_replica_module.md#id2)

The below requirements are needed on the host that executes this module.

- [dbatools](https://www.powershellgallery.com/packages/dbatools/) PowerShell module

## [Parameters](ag_replica_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ag_name**  string / required | Name of the Availability Group that will have the new replica joined to it. |
| **availability_mode**  string | Whether the replica should be Asynchronous or Synchronous.  **Choices:**   - `"AsynchronousCommit"` ← (default) - `"SynchronousCommit"` |
| **backup_priority**  integer | Sets the backup priority availability group replica.  **Default:** `50` |
| **cluster_type**  string | Cluster type of the Availability Group. Only supported in SQL Server 2017 and above.  **Choices:**   - `"Wsfc"` ← (default) - `"External"` - `"None"` |
| **configure_xe_session**  boolean | Configure the AlwaysOn_health extended events session to start automatically as the SSMS wizard would do.  **Choices:**   - `false` ← (default) - `true` |
| **connection_mode_in_primary_role**  string | Which connections can be made to the database when it is in the primary role.  **Choices:**   - `"AllowReadIntentConnectionsOnly"` - `"AllowAllConnections"` ← (default) |
| **connection_mode_in_secondary_role**  string | Which connections can be made to the database when it is in the secondary role.  **Choices:**   - `"AllowNoConnections"` ← (default) - `"AllowReadIntentConnectionsOnly"` - `"AllowAllConnections"` |
| **endpoint**  string | By default, this command will attempt to find a DatabaseMirror endpoint. If one does not exist, it will create it.  **Default:** `"hadr_endpoint"` |
| **endpoint_url**  string | By default, the property `Fqdn` of `Get-DbaEndpoint` is used as *endpoint_url*. Use *endpoint_url* if a different URL is required due to special network configurations. |
| **failover_mode**  string | Whether the replica have Automatic or Manual failover.  **Choices:**   - `"Automatic"` - `"Manual"` ← (default) |
| **read_only_routing_connection_url**  string | Sets the read only routing connection url for the availability replica. |
| **read_only_routing_list**  string | Sets the read only routing ordered list of replica server names to use when redirecting read-only connections through this availability replica. |
| **seeding_mode**  string | Default seeding mode for the replica. Should remain as the default otherwise manual setup may be required.  **Choices:**   - `"Automatic"` ← (default) - `"Manual"` |
| **session_timeout**  integer | How many seconds an availability replica waits for a ping response from a connected replica before considering the connection to have failed. |
| **sql_instance**  string / required | The SQL Server instance to modify. |
| **sql_instance_replica**  string / required | The SQL Server instance where of the replica to be configured. |
| **sql_password**  string | Password for SQL Authentication. |
| **sql_password_replica**  string | Password for SQL Authentication for the secondary replica. |
| **sql_username**  string | Username for SQL Authentication. |
| **sql_username_replica**  string | Username for SQL Authentication for the secondary replica. |
| **state**  string | Whether or not the object should be `present` or `absent`.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Attributes](ag_replica_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target. |
| **platform** | **Platforms:** **all** | Target OS/families that can be operated against. |

## [Examples](ag_replica_module.md#id5)

```yaml+jinja
- name: Create Availability Group
  lowlydba.sqlserver.availability_group:
    sql_instance: sql-01.myco.io
    ag_name: AG_MyDatabase

- name: Add a DR replica
  lowlydba.sqlserver.ag_replica:
    ag_name: 'AG_MyDatabase'
    sql_instance_primary: sql-01.myco.io
    sql_instance_replica: sql-02.myco.io
    failover_mode: 'Manual'
    availability_mode: 'Asynchronous'
    seeding_mode: 'Automatic'
    connection_mode_in_primary_role: 'AllowAllConnections'
    connection_mode_in_secondary_role: 'AllowNoConnections'
```

## [Return Values](ag_replica_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | Output from the `Add-DbaAgReplica` or `Set-DbaAgReplica` function.  **Returned:** success, but not in check_mode. |

### Authors

- John McCall (@lowlydba)

### Collection links

- [Issue Tracker](https://github.com/LowlyDBA/lowlydba.sqlserver/issues)
- [Repository (Sources)](https://github.com/LowlyDBA/lowlydba.sqlserver)
