---
collection: ansible
version: "8"
title: "ansible.windows.win_service module – Manage and query Windows services"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/windows/win_service_module.html
fetched_at: 2026-07-28T01:10:47+00:00
---
# ansible.windows.win_service module – Manage and query Windows services

> **Note:**
>
> This module is part of the [ansible.windows collection](https://galaxy.ansible.com/ui/repo/published/ansible/windows/) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.windows`.
>
> To use it in a playbook, specify: `ansible.windows.win_service`.

- [Synopsis](win_service_module.md#synopsis)
- [Parameters](win_service_module.md#parameters)
- [Notes](win_service_module.md#notes)
- [See Also](win_service_module.md#see-also)
- [Examples](win_service_module.md#examples)
- [Return Values](win_service_module.md#return-values)

## [Synopsis](win_service_module.md#id1)

- Manage and query Windows services.
- For non-Windows targets, use the [ansible.builtin.service](../builtin/service_module.md#ansible-collections-ansible-builtin-service-module) module instead.

## [Parameters](win_service_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **dependencies**  list / elements=string | A list of service dependencies to set for this particular service.  This should be a list of service names and not the display name of the service.  This works by `dependency_action` to either add/remove or set the services in this list. |
| **dependency_action**  string | Used in conjunction with `dependency` to either add the dependencies to the existing service dependencies.  Remove the dependencies to the existing dependencies.  Set the dependencies to only the values in the list replacing the existing dependencies.  **Choices:**   - `"add"` - `"remove"` - `"set"` ← (default) |
| **description**  string | The description to set for the service. |
| **desktop_interact**  boolean | Whether to allow the service user to interact with the desktop.  This can only be set to `true` when using the `LocalSystem` username.  This can only be set to `true` when the *service_type* is `win32_own_process` or `win32_share_process`.  **Choices:**   - `false` ← (default) - `true` |
| **display_name**  string | The display name to set for the service. |
| **error_control**  string | The severity of the error and action token if the service fails to start.  A new service defaults to `normal`.  `critical` will log the error and restart the system with the last-known good configuration. If the startup fails on reboot then the system will fail to operate.  `ignore` ignores the error.  `normal` logs the error in the event log but continues.  `severe` is like `critical` but a failure on the last-known good configuration reboot startup will be ignored.  **Choices:**   - `"critical"` - `"ignore"` - `"normal"` - `"severe"` |
| **failure_actions**  list / elements=dictionary | A list of failure actions the service controller should take on each failure of a service.  The service manager will run the actions from first to last defined until the service starts. If *failure_reset_period_sec* has been exceeded then the failure actions will restart from the beginning.  If all actions have been performed the the service manager will repeat the last service defined.  The existing actions will be replaced with the list defined in the task if there is a mismatch with any of them.  Set to an empty list to delete all failure actions on a service otherwise an omitted or null value preserves the existing actions on the service. |
| **delay_ms**  aliases: delay  any | The time to wait, in milliseconds, before performing the specified action.  **Default:** `0` |
| **type**  string / required | The action to be performed.  `none` will perform no action, when used this should only be set as the last action.  `reboot` will reboot the host, when used this should only be set as the last action as the reboot will reset the action list back to the beginning.  `restart` will restart the service.  `run_command` will run the command specified by *failure_command*.  **Choices:**   - `"none"` - `"reboot"` - `"restart"` - `"run_command"` |
| **failure_actions_on_non_crash_failure**  boolean | Controls whether failure actions will be performed on non crash failures or not.  **Choices:**   - `false` - `true` |
| **failure_command**  string | The command to run for a `run_command` failure action.  Set to an empty string to remove the command. |
| **failure_reboot_msg**  string | The message to be broadcast to users logged on the host for a `reboot` failure action.  Set to an empty string to remove the message. |
| **failure_reset_period_sec**  aliases: failure_reset_period  any | The time in seconds after which the failure action list resets back to the start of the list if there are no failures.  To set this value, *failure_actions* must have at least 1 action present.  Specify `'0xFFFFFFFF'` to set an infinite reset period. |
| **force_dependent_services**  boolean | If `true`, stopping or restarting a service with dependent services will force the dependent services to stop or restart also.  If `false`, stopping or restarting a service with dependent services may fail.  **Choices:**   - `false` ← (default) - `true` |
| **load_order_group**  string | The name of the load ordering group of which this service is a member.  Specify an empty string to remove the existing load order group of a service. |
| **name**  string / required | Name of the service.  If only the name parameter is specified, the module will report on whether the service exists or not without making any changes. |
| **password**  string | The password to set the service to start as.  This and the `username` argument should be supplied together when using a local or domain account.  If omitted then the password will continue to use the existing value password set.  If specifying `LocalSystem`, `NetworkService`, `LocalService`, the `NT SERVICE`, or a gMSA this field can be omitted as those accounts have no password. |
| **path**  string | The path to the executable to set for the service. |
| **pre_shutdown_timeout_ms**  aliases: pre_shutdown_timeout  any | The time in which the service manager waits after sending a preshutdown notification to the service until it proceeds to continue with the other shutdown actions. |
| **required_privileges**  list / elements=string | A list of privileges the service must have when starting up.  When set the service will only have the privileges specified on its access token.  The *username* of the service must already have the privileges assigned.  The existing privileges will be replace with the list defined in the task if there is a mismatch with any of them.  Set to an empty list to remove all required privileges, otherwise an omitted or null value will keep the existing privileges.  See [privilege text constants](https://docs.microsoft.com/en-us/windows/win32/secauthz/privilege-constants) for a list of privilege constants that can be used. |
| **service_type**  string | The type of service.  The default type of a new service is `win32_own_process`.  *desktop_interact* can only be set if the service type is `win32_own_process` or `win32_share_process`.  **Choices:**   - `"user_own_process"` - `"user_share_process"` - `"win32_own_process"` - `"win32_share_process"` |
| **sid_info**  string | Used to define the behaviour of the service’s access token groups.  `none` will not add any groups to the token.  `restricted` will add the `NT SERVICE\<service name>` SID to the access token’s groups and restricted groups.  `unrestricted` will add the `NT SERVICE\<service name>` SID to the access token’s groups.  **Choices:**   - `"none"` - `"restricted"` - `"unrestricted"` |
| **start_mode**  string | Set the startup type for the service.  A newly created service will default to `auto`.  **Choices:**   - `"auto"` - `"delayed"` - `"disabled"` - `"manual"` |
| **state**  string | The desired state of the service.  `started`/`stopped`/`absent`/`paused` are idempotent actions that will not run commands unless necessary.  `restarted` will always bounce the service.  Only services that support the paused state can be paused, you can check the return value `can_pause_and_continue`.  You can only pause a service that is already started.  A newly created service will default to `stopped`.  **Choices:**   - `"absent"` - `"paused"` - `"started"` - `"stopped"` - `"restarted"` |
| **update_password**  string | When set to `always` and *password* is set, the module will always report a change and set the password.  Set to `on_create` to only set the password if the module needs to create the service.  If *username* was specified and the service changed to that username then *password* will also be changed if specified.  The current default is `on_create` but this behaviour may change in the future, it is best to be explicit here.  **Choices:**   - `"always"` - `"on_create"` |
| **username**  string | The username to set the service to start as.  Can also be set to `LocalSystem` or `SYSTEM` to use the SYSTEM account.  A newly created service will default to `LocalSystem`.  If using a custom user account, it must have the `SeServiceLogonRight` granted to be able to start up. You can use the [ansible.windows.win_user_right](win_user_right_module.md#ansible-collections-ansible-windows-win-user-right-module) module to grant this user right for you.  Set to `NT SERVICE\service name` to run as the NT SERVICE account for that service.  This can also be a gMSA in the form `DOMAIN\gMSA$`. |

## [Notes](win_service_module.md#id3)

> **Note:**
>
> - This module historically returning information about the service in its return values. These should be avoided in favour of the [ansible.windows.win_service_info](win_service_info_module.md#ansible-collections-ansible-windows-win-service-info-module) module.
> - Most of the options in this module are non-driver services that you can view in SCManager. While you can edit driver services, not all functionality may be available.
> - The user running the module must have the following access rights on the service to be able to use it with this module - `SERVICE_CHANGE_CONFIG`, `SERVICE_ENUMERATE_DEPENDENTS`, `SERVICE_QUERY_CONFIG`, `SERVICE_QUERY_STATUS`.
> - Changing the state or removing the service will also require futher rights depending on what needs to be done.

## [See Also](win_service_module.md#id4)

> **See also:**
>
> [ansible.builtin.service](../builtin/service_module.md#ansible-collections-ansible-builtin-service-module)
> :   Manage services.
>
> [community.windows.win_nssm](../../community/windows/win_nssm_module.md#ansible-collections-community-windows-win-nssm-module)
> :   Install a service using NSSM.
>
> [ansible.windows.win_service_info](win_service_info_module.md#ansible-collections-ansible-windows-win-service-info-module)
> :   Gather information about Windows services.
>
> [ansible.windows.win_user_right](win_user_right_module.md#ansible-collections-ansible-windows-win-user-right-module)
> :   Manage Windows User Rights.

## [Examples](win_service_module.md#id5)

```yaml+jinja
- name: Restart a service
  ansible.windows.win_service:
    name: spooler
    state: restarted

- name: Set service startup mode to auto and ensure it is started
  ansible.windows.win_service:
    name: spooler
    start_mode: auto
    state: started

- name: Pause a service
  ansible.windows.win_service:
    name: Netlogon
    state: paused

- name: Ensure that WinRM is started when the system has settled
  ansible.windows.win_service:
    name: WinRM
    start_mode: delayed

# A new service will also default to the following values:
# - username: LocalSystem
# - state: stopped
# - start_mode: auto
- name: Create a new service
  ansible.windows.win_service:
    name: service name
    path: C:\temp\test.exe

- name: Create a new service with extra details
  ansible.windows.win_service:
    name: service name
    path: C:\temp\test.exe
    display_name: Service Name
    description: A test service description

- name: Remove a service
  ansible.windows.win_service:
    name: service name
    state: absent

# This is required to be set for non-service accounts that need to run as a service
- name: Grant domain account the SeServiceLogonRight user right
  ansible.windows.win_user_right:
    name: SeServiceLogonRight
    users:
    - DOMAIN\User
    action: add

- name: Set the log on user to a domain account
  ansible.windows.win_service:
    name: service name
    state: restarted
    username: DOMAIN\User
    password: Password

- name: Set the log on user to a local account
  ansible.windows.win_service:
    name: service name
    state: restarted
    username: .\Administrator
    password: Password

- name: Set the log on user to Local System
  ansible.windows.win_service:
    name: service name
    state: restarted
    username: SYSTEM

- name: Set the log on user to Local System and allow it to interact with the desktop
  ansible.windows.win_service:
    name: service name
    state: restarted
    username: SYSTEM
    desktop_interact: true

- name: Set the log on user to Network Service
  ansible.windows.win_service:
    name: service name
    state: restarted
    username: NT AUTHORITY\NetworkService

- name: Set the log on user to Local Service
  ansible.windows.win_service:
    name: service name
    state: restarted
    username: NT AUTHORITY\LocalService

- name: Set the log on user as the services' virtual account
  ansible.windows.win_service:
    name: service name
    username: NT SERVICE\service name

- name: Set the log on user as a gMSA
  ansible.windows.win_service:
    name: service name
    username: DOMAIN\gMSA$  # The end $ is important and should be set for all gMSA

- name: Set dependencies to ones only in the list
  ansible.windows.win_service:
    name: service name
    dependencies: [ service1, service2 ]

- name: Add dependencies to existing dependencies
  ansible.windows.win_service:
    name: service name
    dependencies: [ service1, service2 ]
    dependency_action: add

- name: Remove dependencies from existing dependencies
  ansible.windows.win_service:
    name: service name
    dependencies:
    - service1
    - service2
    dependency_action: remove

- name: Set required privileges for a service
  ansible.windows.win_service:
    name: service name
    username: NT SERVICE\LocalService
    required_privileges:
    - SeBackupPrivilege
    - SeRestorePrivilege

- name: Remove all required privileges for a service
  ansible.windows.win_service:
    name: service name
    username: NT SERVICE\LocalService
    required_privileges: []

- name: Set failure actions for a service with no reset period
  ansible.windows.win_service:
    name: service name
    failure_actions:
    - type: restart
    - type: run_command
      delay_ms: 1000
    - type: restart
      delay_ms: 5000
    - type: reboot
    failure_command: C:\Windows\System32\cmd.exe /c mkdir C:\temp
    failure_reboot_msg: Restarting host because service name has failed
    failure_reset_period_sec: '0xFFFFFFFF'

- name: Set only 1 failure action without a repeat of the last action
  ansible.windows.win_service:
    name: service name
    failure_actions:
    - type: restart
      delay_ms: 5000
    - type: none

- name: Remove failure action information
  ansible.windows.win_service:
    name: service name
    failure_actions: []
    failure_command: ''  # removes the existing command
    failure_reboot_msg: ''  # removes the existing reboot msg
```

## [Return Values](win_service_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **can_pause_and_continue**  boolean | Whether the service can be paused and unpaused.  **Returned:** success and service exists  **Sample:** `true` |
| **depended_by**  list / elements=string | A list of services that depend on this service.  **Returned:** success and service exists  **Sample:** `["False"]` |
| **dependencies**  list / elements=string | A list of services that is depended by this service.  **Returned:** success and service exists  **Sample:** `["False"]` |
| **description**  string | The description of the service.  **Returned:** success and service exists  **Sample:** `"Manages communication between system components."` |
| **desktop_interact**  boolean | Whether the current user is allowed to interact with the desktop.  **Returned:** success and service exists  **Sample:** `false` |
| **display_name**  string | The display name of the installed service.  **Returned:** success and service exists  **Sample:** `"CoreMessaging"` |
| **exists**  boolean | Whether the service exists or not.  **Returned:** success  **Sample:** `true` |
| **name**  string | The service name or id of the service.  **Returned:** success and service exists  **Sample:** `"CoreMessagingRegistrar"` |
| **path**  string | The path to the service executable.  **Returned:** success and service exists  **Sample:** `"C:\\Windows\\system32\\svchost.exe -k LocalServiceNoNetwork"` |
| **start_mode**  string | The startup type of the service.  **Returned:** success and service exists  **Sample:** `"manual"` |
| **state**  string | The current running status of the service.  **Returned:** success and service exists  **Sample:** `"stopped"` |
| **username**  string | The username that runs the service.  **Returned:** success and service exists  **Sample:** `"LocalSystem"` |

### Authors

- Chris Hoffman (@chrishoffman)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
- [Communication](index.md#communication-for-ansible-windows)
