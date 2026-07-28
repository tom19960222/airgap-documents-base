---
collection: ansible
version: "8"
title: "community.windows.win_scheduled_task_stat module – Get information about Windows Scheduled Tasks"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_scheduled_task_stat_module.html
fetched_at: 2026-07-28T02:02:26+00:00
---
# community.windows.win_scheduled_task_stat module – Get information about Windows Scheduled Tasks

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/ui/repo/published/community/windows/) (version 1.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_scheduled_task_stat`.

- [Synopsis](win_scheduled_task_stat_module.md#synopsis)
- [Parameters](win_scheduled_task_stat_module.md#parameters)
- [See Also](win_scheduled_task_stat_module.md#see-also)
- [Examples](win_scheduled_task_stat_module.md#examples)
- [Return Values](win_scheduled_task_stat_module.md#return-values)

## [Synopsis](win_scheduled_task_stat_module.md#id1)

- Will return whether the folder and task exists.
- Returns the names of tasks in the folder specified.
- Use [community.windows.win_scheduled_task](win_scheduled_task_module.md#ansible-collections-community-windows-win-scheduled-task-module) to configure a scheduled task.

## [Parameters](win_scheduled_task_stat_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  string | The name of the scheduled task to get information for.  If `name` is set and exists, will return information on the task itself. |
| **path**  string | The folder path where the task lives.  **Default:** `"\\"` |

## [See Also](win_scheduled_task_stat_module.md#id3)

> **See also:**
>
> [community.windows.win_scheduled_task](win_scheduled_task_module.md#ansible-collections-community-windows-win-scheduled-task-module)
> :   Manage scheduled tasks.

## [Examples](win_scheduled_task_stat_module.md#id4)

```yaml+jinja
- name: Get information about a folder
  community.windows.win_scheduled_task_stat:
    path: \folder name
  register: task_folder_stat

- name: Get information about a task in the root folder
  community.windows.win_scheduled_task_stat:
    name: task name
  register: task_stat

- name: Get information about a task in a custom folder
  community.windows.win_scheduled_task_stat:
    path: \folder name
    name: task name
  register: task_stat
```

## [Return Values](win_scheduled_task_stat_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **actions**  list / elements=string | A list of actions.  **Returned:** name is specified and task exists  **Sample:** `[{"Arguments": "/c echo hi", "Id": null, "Path": "cmd.exe", "Type": "TASK_ACTION_EXEC", "WorkingDirectory": null}]` |
| **folder_exists**  boolean | Whether the folder set at path exists.  **Returned:** always  **Sample:** `true` |
| **folder_task_count**  integer | The number of tasks that exist in the folder.  **Returned:** always  **Sample:** `2` |
| **folder_task_names**  list / elements=string | A list of tasks that exist in the folder.  **Returned:** always  **Sample:** `["Task 1", "Task 2"]` |
| **principal**  complex | Details on the principal configured to run the task.  **Returned:** name is specified and task exists |
| **display_name**  string | The name of the user/group that is displayed in the Task Scheduler UI.  **Sample:** `"Administrator"` |
| **group_id**  string | The group that will run the task.  **Sample:** `"BUILTIN\\Administrators"` |
| **id**  string | The ID for the principal.  **Sample:** `"Author"` |
| **logon_type**  string | The logon method that the task will run with.  **Sample:** `"TASK_LOGON_INTERACTIVE_TOKEN"` |
| **run_level**  string | The level of user rights used to run the task.  **Sample:** `"TASK_RUNLEVEL_LUA"` |
| **user_id**  string | The user that will run the task.  **Sample:** `"SERVER\\Administrator"` |
| **registration_info**  complex | Details on the task registration info.  **Returned:** name is specified and task exists |
| **author**  string | The author os the task.  **Sample:** `"SERVER\\Administrator"` |
| **date**  string | The date when the task was register.  **Sample:** `"2017-01-01T10:00:00"` |
| **description**  string | The description of the task.  **Sample:** `"task description"` |
| **documentation**  string | The documentation of the task.  **Sample:** `"task documentation"` |
| **security_descriptor**  string | The security descriptor of the task.  **Sample:** `"security descriptor"` |
| **source**  string | The source of the task.  **Sample:** `"source"` |
| **uri**  string | The URI/path of the task.  **Sample:** `"\\task\\task name"` |
| **version**  string | The version of the task.  **Sample:** `"1.0"` |
| **settings**  complex | Details on the task settings.  **Returned:** name is specified and task exists |
| **allow_demand_start**  boolean | Whether the task can be started by using either the Run command of the Context menu.  **Sample:** `true` |
| **allow_hard_terminate**  boolean | Whether the task can terminated by using TerminateProcess.  **Sample:** `true` |
| **compatibility**  integer | The compatibility level of the task  **Sample:** `2` |
| **delete_expired_task_after**  string | The amount of time the Task Scheduler will wait before deleting the task after it expires.  **Sample:** `"PT10M"` |
| **disallow_start_if_on_batteries**  boolean | Whether the task will not be started if the computer is running on battery power.  **Sample:** `false` |
| **disallow_start_on_remote_app_session**  boolean | Whether the task will not be started when in a remote app session.  **Sample:** `true` |
| **enabled**  boolean | Whether the task is enabled.  **Sample:** `true` |
| **execution_time_limit**  string | The amount of time allowed to complete the task.  **Sample:** `"PT72H"` |
| **hidden**  boolean | Whether the task is hidden in the UI.  **Sample:** `false` |
| **idle_settings**  dictionary | The idle settings of the task.  **Sample:** `{"idle_duration": "PT10M", "restart_on_idle": false, "stop_on_idle_end": true, "wait_timeout": "PT1H"}` |
| **maintenance_settings**  string | The maintenance settings of the task. |
| **mulitple_instances**  integer | Indicates the behaviour when starting a task that is already running.  **Sample:** `2` |
| **network_settings**  dictionary | The network settings of the task.  **Sample:** `{"id": null, "name": null}` |
| **priority**  integer | The priority level of the task.  **Sample:** `7` |
| **restart_count**  integer | The number of times that the task will attempt to restart on failures.  **Sample:** `0` |
| **restart_interval**  string | How long the Task Scheduler will attempt to restart the task.  **Sample:** `"PT15M"` |
| **run_only_id_idle**  boolean | Whether the task will run if the computer is in an idle state.  **Sample:** `true` |
| **run_only_if_network_available**  boolean | Whether the task will run only when a network is available.  **Sample:** `false` |
| **start_when_available**  boolean | Whether the task can start at any time after its scheduled time has passed.  **Sample:** `false` |
| **stop_if_going_on_batteries**  boolean | Whether the task will be stopped if the computer begins to run on battery power.  **Sample:** `true` |
| **use_unified_scheduling_engine**  boolean | Whether the task will use the unified scheduling engine.  **Sample:** `false` |
| **volatile**  boolean | Whether the task is volatile.  **Sample:** `false` |
| **wake_to_run**  boolean | Whether the task will wake the computer when it is time to run the task.  **Sample:** `false` |
| **state**  complex | Details on the state of the task  **Returned:** name is specified and task exists |
| **last_run_time**  string | The time the registered task was last run.  **Sample:** `"2017-09-20T20:50:00"` |
| **last_task_result**  integer | The results that were returned the last time the task was run.  **Sample:** `267009` |
| **next_run_time**  string | The time when the task is next scheduled to run.  **Sample:** `"2017-09-20T22:50:00"` |
| **number_of_missed_runs**  integer | The number of times a task has missed a scheduled run.  **Sample:** `1` |
| **status**  string | The status of the task, whether it is running, stopped, etc.  **Sample:** `"TASK_STATE_RUNNING"` |
| **task_exists**  boolean | Whether the task at the folder exists.  **Returned:** name is specified  **Sample:** `true` |
| **triggers**  list / elements=string | A list of triggers.  **Returned:** name is specified and task exists  **Sample:** `[{"delay": "PT15M", "enabled": true, "end_boundary": null, "execution_time_limit": null, "id": null, "repetition": {"duration": null, "interval": null, "stop_at_duration_end": false}, "start_boundary": null, "type": "TASK_TRIGGER_BOOT"}, {"days_of_month": "5,15,30", "enabled": true, "end_boundary": null, "execution_time_limit": null, "id": null, "months_of_year": "june,december", "random_delay": null, "repetition": {"duration": null, "interval": null, "stop_at_duration_end": false}, "run_on_last_day_of_month": true, "start_boundary": "2017-09-20T03:44:38", "type": "TASK_TRIGGER_MONTHLY"}]` |

### Authors

- Jordan Borean (@jborean93)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
