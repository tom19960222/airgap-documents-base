---
collection: ansible
version: "8"
title: "lowlydba.sqlserver.agent_job module – Configures a SQL Agent job"
source_url: https://docs.ansible.com/projects/ansible/8/collections/lowlydba/sqlserver/agent_job_module.html
fetched_at: 2026-07-28T02:40:23+00:00
---
# lowlydba.sqlserver.agent_job module – Configures a SQL Agent job

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
> see [Requirements](agent_job_module.md#ansible-collections-lowlydba-sqlserver-agent-job-module-requirements) for details.
>
> To use it in a playbook, specify: `lowlydba.sqlserver.agent_job`.

New in lowlydba.sqlserver 0.1.0

- [Synopsis](agent_job_module.md#synopsis)
- [Requirements](agent_job_module.md#requirements)
- [Parameters](agent_job_module.md#parameters)
- [Attributes](agent_job_module.md#attributes)
- [Notes](agent_job_module.md#notes)
- [Examples](agent_job_module.md#examples)
- [Return Values](agent_job_module.md#return-values)

## [Synopsis](agent_job_module.md#id1)

- Configure a SQL Agent job, including which schedules and category it belongs to.

## [Requirements](agent_job_module.md#id2)

The below requirements are needed on the host that executes this module.

- [dbatools](https://www.powershellgallery.com/packages/dbatools/) PowerShell module

## [Parameters](agent_job_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **category**  string | Category for the target SQL Agent job. Must already exist. |
| **description**  string | Description for the SQL Agent job. |
| **enabled**  boolean  *added in lowlydba.sqlserver 0.4.0* | Whether the SQL Agent job should be enabled or disabled.  **Choices:**   - `false` - `true` ← (default) |
| **force**  boolean | If *force=true*, any job categories will be created if they don’t exist already.  **Choices:**   - `false` ← (default) - `true` |
| **job**  string / required | The name of the target SQL Agent job. |
| **owner_login**  string | The owning login for the database. Will default to the current user if the database is being created and none supplied. |
| **schedule**  string | The name of the schedule the job should be associated with. Only one schedule per job is supported. |
| **sql_instance**  string / required | The SQL Server instance to modify. |
| **sql_password**  string | Password for SQL Authentication. |
| **sql_username**  string | Username for SQL Authentication. |
| **start_step_id**  integer | What step number the job should begin with when run. |
| **state**  string | Whether or not the object should be `present` or `absent`.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Attributes](agent_job_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target. |
| **platform** | **Platforms:** **all** | Target OS/families that can be operated against. |

## [Notes](agent_job_module.md#id5)

> **Note:**
>
> - On slower hardware, stale job component data may be returned (i.e., a previous or default job category). Configuring each component (schedule, step, category, etc.) individually is recommended for this reason.

## [Examples](agent_job_module.md#id6)

```yaml+jinja
- name: Create a job
  lowlydba.sqlserver.agent_job:
    sql_instance: sql-01.myco.io
    job: MyJob
    force: true
```

## [Return Values](agent_job_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | Output from the `New-DbaAgentJob`, `Set-DbaAgentJob`, or `Remove-DbaAgentJob` function.  **Returned:** success, but not in check_mode. |

### Authors

- John McCall (@lowlydba)

### Collection links

- [Issue Tracker](https://github.com/LowlyDBA/lowlydba.sqlserver/issues)
- [Repository (Sources)](https://github.com/LowlyDBA/lowlydba.sqlserver)
