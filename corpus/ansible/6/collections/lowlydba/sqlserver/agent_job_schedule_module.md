---
collection: ansible
version: "6"
title: "lowlydba.sqlserver.agent_job_schedule module – Configures a SQL Agent job schedule"
source_url: https://docs.ansible.com/projects/ansible/6/collections/lowlydba/sqlserver/agent_job_schedule_module.html
fetched_at: 2026-07-27T17:55:04+00:00
---
# lowlydba.sqlserver.agent_job_schedule module – Configures a SQL Agent job schedule

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
> see [Requirements](agent_job_schedule_module.md#ansible-collections-lowlydba-sqlserver-agent-job-schedule-module-requirements) for details.
>
> To use it in a playbook, specify: `lowlydba.sqlserver.agent_job_schedule`.

New in lowlydba.sqlserver 0.1.0

- [Synopsis](agent_job_schedule_module.md#synopsis)
- [Requirements](agent_job_schedule_module.md#requirements)
- [Parameters](agent_job_schedule_module.md#parameters)
- [Attributes](agent_job_schedule_module.md#attributes)
- [Examples](agent_job_schedule_module.md#examples)
- [Return Values](agent_job_schedule_module.md#return-values)

## [Synopsis](agent_job_schedule_module.md#id1)

- Configures settings for an agent schedule that can be applied to one or more agent jobs.

## [Requirements](agent_job_schedule_module.md#id2)

The below requirements are needed on the host that executes this module.

- [dbatools](https://www.powershellgallery.com/packages/dbatools/) PowerShell module

## [Parameters](agent_job_schedule_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **enabled**  boolean | Whether the schedule is enabled or disabled.  Choices:   - `false` - `true` |
| **end_date**  string | The date on which execution of a job can stop.  If *force=true* the end date will be `9999-12-31`.  Format is `YYYY-MM-DD`. |
| **end_time**  string | The time on any day to end execution of a job. Format `HHMMSS` (24 hour clock).  If (force=true) the start time will be `23:59:59`. |
| **force**  boolean | The force option will ignore some errors in the options and assume defaults.  It will also remove the any present schedules with the same name for the specific job.  Choices:   - `false` - `true` |
| **frequency_interval**  string | The days that a job is executed.  Allowed values for *frequency_type=Daily* - `EveryDay` or a number between `1` and `365` inclusive.  Allowed values for *frequency_type=Weekly* - `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`, `Weekdays`, `Weekend` or `EveryDay`.  Allowed values for *frequency_type=Monthly* - Numbers `1` through `31` for each day of the month.  If `Weekdays`, `Weekend` or `EveryDay` is used it overwrites any other value that has been passed before.  If *force=true* the default will be `1`. |
| **frequency_recurrence_factor**  integer | The number of weeks or months between the scheduled execution of a job.  Required if *frequency_type=Weekly*, *frequency_type=Monthly* or *frequency_type=MonthlyRelative*. |
| **frequency_relative_interval**  string | A job’s occurrence of *frequency_interval* in each month. If *frequency_interval=32* (`MonthlyRelative`).  Choices:   - `"Unused"` - `"First"` - `"Second"` - `"Third"` - `"Fourth"` - `"Last"` |
| **frequency_subday_interval**  integer | The number of subday type periods to occur between each execution of a job. |
| **frequency_subday_type**  string | Specifies the units for the subday *frequency_interval*.  Choices:   - `"Time"` - `"Seconds"` - `"Minutes"` - `"Hours"` |
| **frequency_type**  string | A value indicating when a job is to be executed.  If *force=true* the default will be `Once`.  Choices:   - `"Once"` - `"OneTime"` - `"Daily"` - `"Weekly"` - `"Monthly"` - `"MonthlyRelative"` - `"AgentStart"` - `"AutoStart"` - `"IdleComputer"` - `"OnIdle"` |
| **job**  string / required | The name of the job that has the schedule.  Schedules and jobs can also be associated via [lowlydba.sqlserver.agent_job](agent_job_module.md#ansible-collections-lowlydba-sqlserver-agent-job-module).  See <https://docs.dbatools.io/New-DbaAgentSchedule> for more detailed usage. |
| **schedule**  string / required | The name of the schedule. |
| **sql_instance**  string / required | The SQL Server instance to modify. |
| **sql_password**  string | Password for SQL Authentication. |
| **sql_username**  string | Username for SQL Authentication. |
| **start_date**  string | The date on which execution of a job can begin.  If *force=true*the start date will be the current day.  Format is `YYYY-MM-DD`. |
| **start_time**  string | The time on any day to begin execution of a job. Format `HHMMSS` (24 hour clock).  If *force=true* the start time will be `00:00:00`. |
| **state**  string | Whether or not the object should be `present` or `absent`.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Attributes](agent_job_schedule_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full | Can run in check_mode and return changed status prediction without modifying target. |
| **platform** | Platforms: all | Target OS/families that can be operated against. |

## [Examples](agent_job_schedule_module.md#id5)

```yaml+jinja
- name: Create a job schedule
  lowlydba.sqlserver.agent_job_schedule:
    sql_instance: sql-01.myco.io
    schedule: DailySchedule
    force: true
    enabled: true
    start_date: 2020-05-25  # May 25, 2020
    end_date: 2099-05-25    # May 25, 2099
    start_time: 010500      # 01:05:00 AM
    end_time: 140030        # 02:00:30 PM
    state: present

- name: Create a job with schedule
  lowlydba.sqlserver.agent_job:
    sql_instance: sql-01.myco.io
    job: MyJob
    force: true
    schedule: DailySchedule
```

## [Return Values](agent_job_schedule_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | Output from the `New-DbaAgentJobSchedule` or `Remove-DbaAgentJobSchedule` function.  Returned: success, but not in check_mode. |

### Authors

- John McCall (@lowlydba)

### Collection links

[Issue Tracker](https://github.com/LowlyDBA/lowlydba.sqlserver/issues)
[Repository (Sources)](https://github.com/LowlyDBA/lowlydba.sqlserver)
