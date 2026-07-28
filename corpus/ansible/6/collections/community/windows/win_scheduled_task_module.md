---
collection: ansible
version: "6"
title: "community.windows.win_scheduled_task module – Manage scheduled tasks"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_scheduled_task_module.html
fetched_at: 2026-07-27T17:23:55+00:00
---
# community.windows.win_scheduled_task module – Manage scheduled tasks

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/community/windows) (version 1.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_scheduled_task`.

- [Synopsis](win_scheduled_task_module.md#synopsis)
- [Parameters](win_scheduled_task_module.md#parameters)
- [Notes](win_scheduled_task_module.md#notes)
- [See Also](win_scheduled_task_module.md#see-also)
- [Examples](win_scheduled_task_module.md#examples)

## [Synopsis](win_scheduled_task_module.md#id1)

- Creates/modifies or removes Windows scheduled tasks.

## [Parameters](win_scheduled_task_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **actions**  list / elements=dictionary | A list of action to configure for the task.  See suboptions for details on how to construct each list entry.  When creating a task there MUST be at least one action but when deleting a task this can be a null or an empty list.  The ordering of this list is important, the module will ensure the order is kept when modifying the task.  This module only supports the `ExecAction` type but can still delete the older legacy types. |
| **arguments**  string | An argument string to supply for the executable. |
| **path**  string / required | The path to the executable for the ExecAction. |
| **working_directory**  string | The working directory to run the executable from. |
| **allow_demand_start**  boolean | Whether the task can be started by using either the Run command or the Context menu.  Choices:   - `false` - `true` |
| **allow_hard_terminate**  boolean | Whether the task can be terminated by using TerminateProcess.  Choices:   - `false` - `true` |
| **author**  string | The author of the task. |
| **compatibility**  integer | The integer value with indicates which version of Task Scheduler a task is compatible with.  `0` means the task is compatible with the AT command.  `1` means the task is compatible with Task Scheduler 1.0(Windows Vista, Windows Server 2008 and older).  `2` means the task is compatible with Task Scheduler 2.0(Windows Vista, Windows Server 2008).  `3` means the task is compatible with Task Scheduler 2.0(Windows 7, Windows Server 2008 R2).  `4` means the task is compatible with Task Scheduler 2.0(Windows 10, Windows Server 2016, Windows Server 2019).  Choices:   - `0` - `1` - `2` - `3` - `4` |
| **date**  string | The date when the task was registered. |
| **delete_expired_task_after**  string | The amount of time that the Task Scheduler will wait before deleting the task after it expires.  A task expires after the end_boundary has been exceeded for all triggers associated with the task.  This is in the ISO 8601 Duration format `P[n]Y[n]M[n]DT[n]H[n]M[n]S`. |
| **description**  string | The description of the task. |
| **disallow_start_if_on_batteries**  boolean | Whether the task will not be started if the computer is running on battery power.  Choices:   - `false` - `true` |
| **display_name**  string | The name of the user/group that is displayed in the Task Scheduler UI. |
| **enabled**  boolean | Whether the task is enabled, the task can only run when `yes`.  Choices:   - `false` - `true` |
| **execution_time_limit**  string | The amount of time allowed to complete the task.  When set to `PT0S`, the time limit is infinite.  When omitted, the default time limit is 72 hours.  This is in the ISO 8601 Duration format `P[n]Y[n]M[n]DT[n]H[n]M[n]S`. |
| **group**  string | The group that will run the task.  `group` and `username` are exclusive to each other and cannot be set at the same time.  `logon_type` can either be not set or equal `group`. |
| **hidden**  boolean | Whether the task will be hidden in the UI.  Choices:   - `false` - `true` |
| **logon_type**  string | The logon method that the task will run with.  `password` means the password will be stored and the task has access to network resources.  `s4u` means the existing token will be used to run the task and no password will be stored with the task. Means no network or encrypted files access.  `interactive_token` means the user must already be logged on interactively and will run in an existing interactive session.  `group` means that the task will run as a group.  `service_account` means that a service account like System, Local Service or Network Service will run the task.  Choices:   - `"none"` - `"password"` - `"s4u"` - `"interactive_token"` - `"group"` - `"service_account"` - `"token_or_password"` |
| **multiple_instances**  integer | An integer that indicates the behaviour when starting a task that is already running.  `0` will start a new instance in parallel with existing instances of that task.  `1` will wait until other instances of that task to finish running before starting itself.  `2` will not start a new instance if another is running.  `3` will stop other instances of the task and start the new one.  Choices:   - `0` - `1` - `2` - `3` |
| **name**  string / required | The name of the scheduled task without the path. |
| **password**  string | The password for the user account to run the scheduled task as.  This is required when running a task without the user being logged in, excluding the builtin service accounts and Group Managed Service Accounts (gMSA).  If set, will always result in a change unless `update_password` is set to `no` and no other changes are required for the service. |
| **path**  string | Task folder in which this task will be stored.  Will create the folder when `state=present` and the folder does not already exist.  Will remove the folder when `state=absent` and there are no tasks left in the folder.  Default: `"\\"` |
| **priority**  integer | The priority level (0-10) of the task.  When creating a new task the default is `7`.  See <https://msdn.microsoft.com/en-us/library/windows/desktop/aa383512.aspx> for details on the priority levels. |
| **restart_count**  integer | The number of times that the Task Scheduler will attempt to restart the task. |
| **restart_interval**  string | How long the Task Scheduler will attempt to restart the task.  If this is set then `restart_count` must also be set.  The maximum allowed time is 31 days.  The minimum allowed time is 1 minute.  This is in the ISO 8601 Duration format `P[n]Y[n]M[n]DT[n]H[n]M[n]S`. |
| **run_level**  aliases: runlevel  string | The level of user rights used to run the task.  If not specified the task will be created with limited rights.  Choices:   - `"limited"` - `"highest"` |
| **run_only_if_idle**  boolean | Whether the task will run the task only if the computer is in an idle state.  Choices:   - `false` - `true` |
| **run_only_if_network_available**  boolean | Whether the task will run only when a network is available.  Choices:   - `false` - `true` |
| **source**  string | The source of the task. |
| **start_when_available**  boolean | Whether the task can start at any time after its scheduled time has passed.  Choices:   - `false` - `true` |
| **state**  string | When `state=present` will ensure the task exists.  When `state=absent` will ensure the task does not exist.  Choices:   - `"absent"` - `"present"` ← (default) |
| **stop_if_going_on_batteries**  boolean | Whether the task will be stopped if the computer begins to run on battery power.  Choices:   - `false` - `true` |
| **triggers**  list / elements=dictionary | A list of triggers to configure for the task.  See suboptions for details on how to construct each list entry.  The ordering of this list is important, the module will ensure the order is kept when modifying the task.  There are multiple types of triggers, see <https://msdn.microsoft.com/en-us/library/windows/desktop/aa383868.aspx> for a list of trigger types and their options.  The suboption options listed below are not required for all trigger types, read the description for more details. |
| **days_of_month**  string | The days of the month from 1 to 31 for the triggers.  If you wish to set the trigger for the last day of any month use `run_on_last_day_of_month`.  Can be a list or comma separated string of day numbers.  Required when `type=monthly`. |
| **days_of_week**  string | The days of the week for the trigger.  Can be a list or comma separated string of full day names e.g. monday instead of mon.  Required when `type` is `weekly`.  Optional when `type=monthlydow`. |
| **delay**  string | The time to delay the task from running once the trigger has been fired.  Optional when `type` is `boot`, `event`, `logon`, `registration`, `session_state_change`.  Is in the ISO 8601 Duration format `P[n]Y[n]M[n]DT[n]H[n]M[n]S`. |
| **enabled**  boolean | Whether to set the trigger to enabled or disabled  Used in all trigger types.  Choices:   - `false` - `true` |
| **end_boundary**  string | The end time for when the trigger is deactivated.  This is in ISO 8601 DateTime format `YYYY-MM-DDThh:mm:ss`. |
| **execution_time_limit**  string | The maximum amount of time that the task is allowed to run for.  Optional for all the trigger types.  Is in the ISO 8601 Duration format `P[n]Y[n]M[n]DT[n]H[n]M[n]S`. |
| **months_of_year**  string | The months of the year for the trigger.  Can be a list or comma separated string of full month names e.g. march instead of mar.  Optional when `type` is `monthlydow`, `monthly`. |
| **random_delay**  string | The delay time that is randomly added to the start time of the trigger.  Optional when `type` is `daily`, `monthlydow`, `monthly`, `time`, `weekly`.  Is in the ISO 8601 Duration format `P[n]Y[n]M[n]DT[n]H[n]M[n]S`. |
| **repetition**  string | Allows you to define the repetition action of the trigger that defines how often the task is run and how long the repetition pattern is repeated after the task is started.  It takes in the following keys, `duration`, `interval`, `stop_at_duration_end` |
| **duration**  string | Defines how long the pattern is repeated.  The value is in the ISO 8601 Duration format `P[n]Y[n]M[n]DT[n]H[n]M[n]S`.  By default this is not set which means it will repeat indefinitely. |
| **interval**  string | The amount of time between each restart of the task.  The value is written in the ISO 8601 Duration format `P[n]Y[n]M[n]DT[n]H[n]M[n]S`. |
| **stop_at_duration_end**  boolean | Whether a running instance of the task is stopped at the end of the repetition pattern.  Choices:   - `false` - `true` |
| **run_on_last_day_of_month**  boolean | Boolean value that sets whether the task runs on the last day of the month.  Optional when `type` is `monthly`.  Choices:   - `false` - `true` |
| **run_on_last_week_of_month**  boolean | Boolean value that sets whether the task runs on the last week of the month.  Optional when `type` is `monthlydow`.  Choices:   - `false` - `true` |
| **start_boundary**  string | The start time for the task, even if the trigger meets the other start criteria, it won’t start until this time is met.  If you wish to run a task at 9am on a day you still need to specify the date on which the trigger is activated, you can set any date even ones in the past.  Required when `type` is `daily`, `monthlydow`, `monthly`, `time`, `weekly`.  Optional for the rest of the trigger types.  This is in ISO 8601 DateTime format `YYYY-MM-DDThh:mm:ss`. |
| **state_change**  string  added in community.windows 1.6.0 | Allows you to define the kind of Terminal Server session change that triggers a task.  Optional when `type=session_state_change`  Choices:   - `"console_connect"` - `"console_disconnect"` - `"remote_connect"` - `"remote_disconnect"` - `"session_lock"` - `"session_unlock"` |
| **subscription**  string | Only used and is required for `type=event`.  The XML query string that identifies the event that fires the trigger. |
| **type**  string / required | The trigger type, this value controls what below options are required.  Choices:   - `"boot"` - `"daily"` - `"event"` - `"idle"` - `"logon"` - `"monthlydow"` - `"monthly"` - `"registration"` - `"time"` - `"weekly"` - `"session_state_change"` |
| **user_id**  string | The username that the trigger will target.  Optional when `type` is `logon`, `session_state_change`.  Can be the username or SID of a user.  When `type=logon` and you want the trigger to fire when a user in a group logs on, leave this as null and set `group` to the group you wish to trigger. |
| **weeks_interval**  integer | The interval of weeks to run on, e.g. `1` means every week while `2` means every other week.  Optional when `type=weekly`. |
| **weeks_of_month**  string | The weeks of the month for the trigger.  Can be a list or comma separated string of the numbers 1 to 4 representing the first to 4th week of the month.  Optional when `type=monthlydow`. |
| **update_password**  boolean | Whether to update the password even when not other changes have occurred.  When `yes` will always result in a change when executing the module.  Choices:   - `false` - `true` ← (default) |
| **username**  aliases: user  string | The user to run the scheduled task as.  Will default to the current user under an interactive token if not specified during creation.  The user account specified must have the `SeBatchLogonRight` logon right which can be added with [ansible.windows.win_user_right](../../ansible/windows/win_user_right_module.md#ansible-collections-ansible-windows-win-user-right-module). |
| **version**  string | The version number of the task. |
| **wake_to_run**  boolean | Whether the task will wake the computer when it is time to run the task.  Choices:   - `false` - `true` |

## [Notes](win_scheduled_task_module.md#id3)

> **Note:**
>
> - The option names and structure for actions and triggers of a service follow the `RegisteredTask` naming standard and requirements, it would be useful to read up on this guide if coming across any issues <https://msdn.microsoft.com/en-us/library/windows/desktop/aa382542.aspx>.
> - A Group Managed Service Account (gMSA) can be used by setting `logon_type` to `password` and omitting the password parameter. For more information on gMSAs, see <https://techcommunity.microsoft.com/t5/Core-Infrastructure-and-Security/Windows-Server-2012-Group-Managed-Service-Accounts/ba-p/255910>

## [See Also](win_scheduled_task_module.md#id4)

> **See also:**
>
> [community.windows.win_scheduled_task_stat](win_scheduled_task_stat_module.md#ansible-collections-community-windows-win-scheduled-task-stat-module)
> :   Get information about Windows Scheduled Tasks.
>
> [ansible.windows.win_user_right](../../ansible/windows/win_user_right_module.md#ansible-collections-ansible-windows-win-user-right-module)
> :   Manage Windows User Rights.

## [Examples](win_scheduled_task_module.md#id5)

```yaml+jinja
- name: Create a task to open 2 command prompts as SYSTEM
  community.windows.win_scheduled_task:
    name: TaskName
    description: open command prompt
    actions:
    - path: cmd.exe
      arguments: /c hostname
    - path: cmd.exe
      arguments: /c whoami
    triggers:
    - type: daily
      start_boundary: '2017-10-09T09:00:00'
    username: SYSTEM
    state: present
    enabled: yes

- name: Create task to run a PS script as NETWORK service on boot
  community.windows.win_scheduled_task:
    name: TaskName2
    description: Run a PowerShell script
    actions:
    - path: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
      arguments: -ExecutionPolicy Unrestricted -NonInteractive -File C:\TestDir\Test.ps1
    triggers:
    - type: boot
    username: NETWORK SERVICE
    run_level: highest
    state: present

- name: Update Local Security Policy to allow users to run scheduled tasks
  ansible.windows.win_user_right:
    name: SeBatchLogonRight
    users:
    - LocalUser
    - DOMAIN\NetworkUser
    action: add

- name: Change above task to run under a domain user account, storing the passwords
  community.windows.win_scheduled_task:
    name: TaskName2
    username: DOMAIN\User
    password: Password
    logon_type: password

- name: Change the above task again, choosing not to store the password
  community.windows.win_scheduled_task:
    name: TaskName2
    username: DOMAIN\User
    logon_type: s4u

- name: Change above task to use a gMSA, where the password is managed automatically
  community.windows.win_scheduled_task:
    name: TaskName2
    username: DOMAIN\gMsaSvcAcct$
    logon_type: password

- name: Create task with multiple triggers
  community.windows.win_scheduled_task:
    name: TriggerTask
    path: \Custom
    actions:
    - path: cmd.exe
    triggers:
    - type: daily
    - type: monthlydow
    username: SYSTEM

- name: Set logon type to password but don't force update the password
  community.windows.win_scheduled_task:
    name: TriggerTask
    path: \Custom
    actions:
    - path: cmd.exe
    username: Administrator
    password: password
    update_password: no

- name: Disable a task that already exists
  community.windows.win_scheduled_task:
    name: TaskToDisable
    enabled: no

- name: Create a task that will be repeated every minute for five minutes
  community.windows.win_scheduled_task:
    name: RepeatedTask
    description: open command prompt
    actions:
    - path: cmd.exe
      arguments: /c hostname
    triggers:
    - type: registration
      repetition:
        interval: PT1M
        duration: PT5M
        stop_at_duration_end: yes

- name: Create task to run a PS script in Windows 10 compatibility on boot with a delay of 1min
  community.windows.win_scheduled_task:
    name: TriggerTask
    path: \Custom
    actions:
    - path: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
      arguments: -ExecutionPolicy Unrestricted -NonInteractive -File C:\TestDir\Test.ps1
    triggers:
    - type: boot
      delay: PT1M
    username: SYSTEM
    compatibility: 4
```

### Authors

- Peter Mounce (@petemounce)
- Jordan Borean (@jborean93)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
