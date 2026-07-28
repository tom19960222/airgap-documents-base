---
collection: ansible
version: "6"
title: "ansible.windows.win_service_info module – Gather information about Windows services"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/windows/win_service_info_module.html
fetched_at: 2026-07-27T16:45:02+00:00
---
# ansible.windows.win_service_info module – Gather information about Windows services

> **Note:**
>
> This module is part of the [ansible.windows collection](https://galaxy.ansible.com/ansible/windows) (version 1.12.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.windows`.
>
> To use it in a playbook, specify: `ansible.windows.win_service_info`.

- [Synopsis](win_service_info_module.md#synopsis)
- [Parameters](win_service_info_module.md#parameters)
- [See Also](win_service_info_module.md#see-also)
- [Examples](win_service_info_module.md#examples)
- [Return Values](win_service_info_module.md#return-values)

## [Synopsis](win_service_info_module.md#id1)

- Gather information about all or a specific installed Windows service(s).

## [Parameters](win_service_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  string | If specified, this is used to match the `name` or `display_name` of the Windows service to get the info for.  Can be a wildcard to match multiple services but the wildcard will only be matched on the `name` of the service and not `display_name`.  If omitted then all services will returned. |

## [See Also](win_service_info_module.md#id3)

> **See also:**
>
> [ansible.windows.win_service](win_service_module.md#ansible-collections-ansible-windows-win-service-module)
> :   Manage and query Windows services.

## [Examples](win_service_info_module.md#id4)

```yaml+jinja
- name: Get info for all installed services
  ansible.windows.win_service_info:
  register: service_info

- name: Get info for a single service
  ansible.windows.win_service_info:
    name: WinRM
  register: service_info

- name: Get info for a service using its display name
  ansible.windows.win_service_info:
    name: Windows Remote Management (WS-Management)

- name: Find all services that start with 'win'
  ansible.windows.win_service_info:
    name: win*
```

## [Return Values](win_service_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **exists**  boolean | Whether any services were found based on the criteria specified.  Returned: always  Sample: `true` |
| **services**  list / elements=dictionary | A list of service(s) that were found based on the criteria.  Will be an empty list if no services were found.  Returned: always |
| **checkpoint**  integer | A check-point value that the service increments periodically to report its progress.  Returned: success  Sample: `0` |
| **controls_accepted**  list / elements=string | A list of controls that the service can accept.  Common controls are `stop`, `pause_continue`, `shutdown`.  Returned: success  Sample: `["stop", "shutdown"]` |
| **dependencies**  list / elements=string | A list of services by their `name` that this service is dependent on.  Returned: success  Sample: `["HTTP", "RPCSS"]` |
| **dependency_of**  list / elements=string | A list of services by their `name` that depend on this service.  Returned: success  Sample: `["upnphost", "WMPNetworkSvc"]` |
| **description**  string | The description of the service.  Returned: success  Sample: `"Example description of the Windows service."` |
| **desktop_interact**  boolean | Whether the service can interact with the desktop, only valid for services running as `SYSTEM`.  Returned: success  Sample: `false` |
| **display_name**  string | The display name to be used by SCM to identify the service.  Returned: success  Sample: `"Windows Remote Management (WS-Management)"` |
| **error_control**  string | The action to take if a service fails to start.  Common values are `critical`, `ignore`, `normal`, `severe`.  Returned: success  Sample: `"normal"` |
| **failure_action_on_non_crash_failure**  boolean | Controls when failure actions are fired based on how the service was stopped.  Returned: success  Sample: `false` |
| **failure_actions**  list / elements=dictionary | A list of failure actions to run in the event of a failure.  Returned: success |
| **delay_ms**  integer | The time to wait, in milliseconds, before performing the specified action.  Returned: success  Sample: `120000` |
| **type**  string | The action that will be performed.  Common values are `none`, `reboot`, `restart`, `run_command`.  Returned: success  Sample: `"run_command"` |
| **failure_command**  string | The command line that will be run when a `run_command` failure action is fired.  Returned: success  Sample: `"runme.exe"` |
| **failure_reboot_msg**  string | The message to be broadcast to server users before rebooting when a `reboot` failure action is fired.  Returned: success  Sample: `"Service failed, rebooting host."` |
| **failure_reset_period_sec**  integer | The time, in seconds, after which to reset the failure count to zero.  Returned: success  Sample: `86400` |
| **launch_protection**  string | The protection type of the service.  Common values are `none`, `windows`, `windows_light`, or `antimalware_light`.  Returned: success  Sample: `"none"` |
| **load_order_group**  string | The name of the load ordering group to which the service belongs.  Will be an empty string if it does not belong to any group.  Returned: success  Sample: `"My group"` |
| **name**  string | The name of the service.  Returned: success  Sample: `"WinRM"` |
| **path**  string | The path to the service binary and any arguments used when starting the service.  The binary part can be quoted to ensure any spaces in path are not treated as arguments.  Returned: success  Sample: `"C:\\Windows\\System32\\svchost.exe -k netsvcs -p"` |
| **pre_shutdown_timeout_ms**  integer | The preshutdown timeout out value in milliseconds.  Returned: success  Sample: `10000` |
| **preferred_node**  integer | The node number for the preferred node.  This will be `null` if the Windows host has no NUMA configuration.  Returned: success  Sample: `0` |
| **process_id**  integer | The process identifier of the running service.  Returned: success  Sample: `5135` |
| **required_privileges**  list / elements=string | A list of privileges that the service requires and will run with  Returned: success  Sample: `["SeBackupPrivilege", "SeRestorePrivilege"]` |
| **service_exit_code**  integer | A service-specific error code that is set while the service is starting or stopping.  Returned: success  Sample: `0` |
| **service_flags**  list / elements=string | Shows more information about the behaviour of a running service.  Currently the only flag that can be set is `runs_in_system_process`.  Returned: success  Sample: `["runs_in_system_process"]` |
| **service_type**  string | The type of service.  Common types are `win32_own_process`, `win32_share_process`, `user_own_process`, `user_share_process`, `kernel_driver`.  Returned: success  Sample: `"win32_own_process"` |
| **sid_info**  string | The behavior of how the service’s access token is generated and how to add the service SID to the token.  Common values are `none`, `restricted`, or `unrestricted`.  Returned: success  Sample: `"none"` |
| **start_mode**  string | When the service is set to start.  Common values are `auto`, `manual`, `disabled`, `delayed`.  Returned: success  Sample: `"auto"` |
| **state**  string | The current running state of the service.  Common values are `stopped`, `start_pending`, `stop_pending`, `started`, `continue_pending`, `pause_pending`, `paused`.  Returned: success  Sample: `"started"` |
| **triggers**  list / elements=dictionary | A list of triggers defined for the service.  Returned: success |
| **action**  string | The action to perform once triggered, can be `start_service` or `stop_service`.  Returned: success  Sample: `"start_service"` |
| **data_items**  list / elements=dictionary | A list of trigger data items that contain trigger specific data.  A trigger can contain 0 or multiple data items.  Returned: success |
| **data**  complex | The trigger data item value.  Can be a string, list of string, int, or base64 string of binary data.  Returned: success  Sample: `"named pipe"` |
| **type**  string | The type of `data` for the trigger.  Common values are `string`, `binary`, `level`, `keyword_any`, or `keyword_all`.  Returned: success  Sample: `"string"` |
| **sub_type**  string | The trigger event sub type that is specific to each `type`.  Common values are `named_pipe_event`, `domain_join`, `domain_leave`, `firewall_port_open`, and others.  Returned: success |
| **sub_type_guid**  string | The guid which represents the trigger sub type.  Returned: success  Sample: `"1ce20aba-9851-4421-9430-1ddeb766e809"` |
| **type**  string | The trigger event type.  Common values are `custom`, `rpc_interface_event`, `domain_join`, `group_policy`, and others.  Returned: success  Sample: `"domain_join"` |
| **username**  string | The username used to run the service.  Can be null for user services and certain driver services.  Returned: success  Sample: `"NT AUTHORITY\\SYSTEM"` |
| **wait_hint_ms**  integer | The estimated time in milliseconds required for a pending start, stop, pause,or continue operations.  Returned: success  Sample: `0` |
| **win32_exitcode**  integer | The error code returned from the service binary once it has stopped.  When set to `1066` then a service specific error is returned on `service_exit_code`.  Returned: success  Sample: `0` |

### Authors

- Jordan Borean (@jborean93)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
[Communication](index.md#communication-for-ansible-windows)
