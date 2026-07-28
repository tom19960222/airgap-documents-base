---
collection: ansible
version: "8"
title: "Lowlydba.Sqlserver"
source_url: https://docs.ansible.com/projects/ansible/8/collections/lowlydba/sqlserver/index.html
fetched_at: 2026-07-28T01:02:44+00:00
---
# Lowlydba.Sqlserver

Collection version 2.2.2

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Ansible collection using PowerShell to configure and maintain SQL Server.

**Author:**

- John McCall (github.com/lowlydba)

**Supported ansible-core versions:**

- 2.12 or newer

- [Issue Tracker](https://github.com/LowlyDBA/lowlydba.sqlserver/issues)
- [Repository (Sources)](https://github.com/LowlyDBA/lowlydba.sqlserver)

## [Plugin Index](index.md#id2)

These are the plugins in the lowlydba.sqlserver collection:

### Modules

- [ag_listener module](ag_listener_module.md#ansible-collections-lowlydba-sqlserver-ag-listener-module) – Configures an availability group listener
- [ag_replica module](ag_replica_module.md#ansible-collections-lowlydba-sqlserver-ag-replica-module) – Configures an availability group replica
- [agent_job module](agent_job_module.md#ansible-collections-lowlydba-sqlserver-agent-job-module) – Configures a SQL Agent job
- [agent_job_category module](agent_job_category_module.md#ansible-collections-lowlydba-sqlserver-agent-job-category-module) – Configures a SQL Agent job category
- [agent_job_schedule module](agent_job_schedule_module.md#ansible-collections-lowlydba-sqlserver-agent-job-schedule-module) – Configures a SQL Agent job schedule
- [agent_job_step module](agent_job_step_module.md#ansible-collections-lowlydba-sqlserver-agent-job-step-module) – Configures a SQL Agent job step
- [availability_group module](availability_group_module.md#ansible-collections-lowlydba-sqlserver-availability-group-module) – Configures availability group(s)
- [backup module](backup_module.md#ansible-collections-lowlydba-sqlserver-backup-module) – Performs a backup operation
- [credential module](credential_module.md#ansible-collections-lowlydba-sqlserver-credential-module) – Configures a credential on a SQL server
- [database module](database_module.md#ansible-collections-lowlydba-sqlserver-database-module) – Creates and configures a database
- [dba_multitool module](dba_multitool_module.md#ansible-collections-lowlydba-sqlserver-dba-multitool-module) – Install/update the DBA Multitool suite by John McCall
- [first_responder_kit module](first_responder_kit_module.md#ansible-collections-lowlydba-sqlserver-first-responder-kit-module) – Install/update the First Responder Kit scripts
- [hadr module](hadr_module.md#ansible-collections-lowlydba-sqlserver-hadr-module) – Enable or disable HADR
- [install_script module](install_script_module.md#ansible-collections-lowlydba-sqlserver-install-script-module) – Runs migration scripts against a database
- [instance_info module](instance_info_module.md#ansible-collections-lowlydba-sqlserver-instance-info-module) – Returns basic information for a SQL Server instance
- [login module](login_module.md#ansible-collections-lowlydba-sqlserver-login-module) – Configures a login for the target SQL Server instance
- [maintenance_solution module](maintenance_solution_module.md#ansible-collections-lowlydba-sqlserver-maintenance-solution-module) – Install/update Maintenance Solution by Ola Hallengren
- [memory module](memory_module.md#ansible-collections-lowlydba-sqlserver-memory-module) – Sets the maximum memory for a SQL Server instance
- [nonquery module](nonquery_module.md#ansible-collections-lowlydba-sqlserver-nonquery-module) – Executes a generic nonquery
- [resource_governor module](resource_governor_module.md#ansible-collections-lowlydba-sqlserver-resource-governor-module) – Configures the resource governor on a SQL Server instance
- [restore module](restore_module.md#ansible-collections-lowlydba-sqlserver-restore-module) – Performs a restore operation
- [rg_resource_pool module](rg_resource_pool_module.md#ansible-collections-lowlydba-sqlserver-rg-resource-pool-module) – Configures a resource pool for use by the Resource Governor
- [rg_workload_group module](rg_workload_group_module.md#ansible-collections-lowlydba-sqlserver-rg-workload-group-module) – Configures a workload group for use by the Resource Governor
- [sa module](sa_module.md#ansible-collections-lowlydba-sqlserver-sa-module) – Configure the `sa` login for security best practices
- [sp_configure module](sp_configure_module.md#ansible-collections-lowlydba-sqlserver-sp-configure-module) – Make instance level system configuration changes via `sp_configure`
- [sp_whoisactive module](sp_whoisactive_module.md#ansible-collections-lowlydba-sqlserver-sp-whoisactive-module) – Install/update `sp_whoisactive` by Adam Mechanic
- [spn module](spn_module.md#ansible-collections-lowlydba-sqlserver-spn-module) – Configures SPNs for SQL Server
- [tcp_port module](tcp_port_module.md#ansible-collections-lowlydba-sqlserver-tcp-port-module) – Sets the TCP port for the instance
- [traceflag module](traceflag_module.md#ansible-collections-lowlydba-sqlserver-traceflag-module) – Enable or disable global trace flags on a SQL Server instance
- [user module](user_module.md#ansible-collections-lowlydba-sqlserver-user-module) – Configures a user within a database

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
