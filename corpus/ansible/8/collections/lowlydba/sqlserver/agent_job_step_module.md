---
collection: ansible
version: "8"
title: "lowlydba.sqlserver.agent_job_step module – Configures a SQL Agent job step"
source_url: https://docs.ansible.com/projects/ansible/8/collections/lowlydba/sqlserver/agent_job_step_module.html
fetched_at: 2026-07-28T02:40:26+00:00
---
# lowlydba.sqlserver.agent_job_step module – Configures a SQL Agent job step

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
> see [Requirements](agent_job_step_module.md#ansible-collections-lowlydba-sqlserver-agent-job-step-module-requirements) for details.
>
> To use it in a playbook, specify: `lowlydba.sqlserver.agent_job_step`.

New in lowlydba.sqlserver 0.1.0

- [Synopsis](agent_job_step_module.md#synopsis)
- [Requirements](agent_job_step_module.md#requirements)
- [Parameters](agent_job_step_module.md#parameters)
- [Attributes](agent_job_step_module.md#attributes)
- [Examples](agent_job_step_module.md#examples)
- [Return Values](agent_job_step_module.md#return-values)

## [Synopsis](agent_job_step_module.md#id1)

- Configures a step for an agent job.

## [Requirements](agent_job_step_module.md#id2)

The below requirements are needed on the host that executes this module.

- [dbatools](https://www.powershellgallery.com/packages/dbatools/) PowerShell module

## [Parameters](agent_job_step_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **command**  string | The commands to be executed by SQLServerAgent service through subsystem. |
| **database**  string | The name of the database in which to execute a Transact-SQL step.  **Default:** `"master"` |
| **job**  string / required | The name of the job to which to add the step. |
| **on_fail_action**  string | The action to perform if the step fails.  **Choices:**   - `"QuitWithSuccess"` - `"QuitWithFailure"` ← (default) - `"GoToNextStep"` - `"GoToStep"` |
| **on_fail_step_id**  integer | The ID of the step in this job to execute if the step fails and *on_fail_action=GoToStep*.  **Default:** `0` |
| **on_success_action**  string | The action to perform if the step succeeds.  **Choices:**   - `"QuitWithSuccess"` ← (default) - `"QuitWithFailure"` - `"GoToNextStep"` - `"GoToStep"` |
| **on_success_step_id**  integer | The ID of the step in this job to execute if the step succeeds and *on_success_action=GoToStep*.  **Default:** `0` |
| **retry_attempts**  integer | The number of retry attempts to use if this step fails. The default is `0`.  **Default:** `0` |
| **retry_interval**  integer | The amount of time in minutes between retry attempts.  **Default:** `0` |
| **sql_instance**  string / required | The SQL Server instance to modify. |
| **sql_password**  string | Password for SQL Authentication. |
| **sql_username**  string | Username for SQL Authentication. |
| **state**  string | Whether or not the object should be `present` or `absent`.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **step_id**  integer | The sequence identification number for the job step. Step identification numbers start at `1` and increment without gaps.  Required if *state=present*. |
| **step_name**  string | The name of the step. Required if *state=present*. |
| **subsystem**  string | The subsystem used by the SQL Server Agent service to execute command.  **Choices:**   - `"CmdExec"` - `"Distribution"` - `"LogReader"` - `"Merge"` - `"PowerShell"` - `"QueueReader"` - `"Snapshot"` - `"Ssis"` - `"TransactSql"` ← (default) |

## [Attributes](agent_job_step_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target. |
| **platform** | **Platforms:** **all** | Target OS/families that can be operated against. |

## [Examples](agent_job_step_module.md#id5)

```yaml+jinja
- name: Create a job
  lowlydba.sqlserver.agent_job:
    sql_instance: sql-01.myco.io
    job: MyJob
    force: true

- name: Create a job step
  lowlydba.sqlserver.agent_job_step:
    sql_instance: sql-01.myco.io
    job: MyJob
    step_name: Step1
    step_id: 1
    command: "TRUNCATE TABLE dbo.TestData;"
```

## [Return Values](agent_job_step_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | Output from the `New-DbaAgentJobStep`, `Set-DbaAgentJobStep`, or `Remove-DbaAgentJobStep` function.  **Returned:** success, but not in check_mode. |

### Authors

- John McCall (@lowlydba)

### Collection links

- [Issue Tracker](https://github.com/LowlyDBA/lowlydba.sqlserver/issues)
- [Repository (Sources)](https://github.com/LowlyDBA/lowlydba.sqlserver)
