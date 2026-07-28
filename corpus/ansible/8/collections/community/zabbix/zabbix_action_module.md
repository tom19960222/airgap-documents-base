---
collection: ansible
version: "8"
title: "community.zabbix.zabbix_action module – Create/Delete/Update Zabbix actions"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/zabbix/zabbix_action_module.html
fetched_at: 2026-07-28T02:02:38+00:00
---
# community.zabbix.zabbix_action module – Create/Delete/Update Zabbix actions

> **Note:**
>
> This module is part of the [community.zabbix collection](https://galaxy.ansible.com/ui/repo/published/community/zabbix/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.zabbix`.
> You need further requirements to be able to use this module,
> see [Requirements](zabbix_action_module.md#ansible-collections-community-zabbix-zabbix-action-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_action`.

- [Synopsis](zabbix_action_module.md#synopsis)
- [Requirements](zabbix_action_module.md#requirements)
- [Parameters](zabbix_action_module.md#parameters)
- [Examples](zabbix_action_module.md#examples)
- [Return Values](zabbix_action_module.md#return-values)

## [Synopsis](zabbix_action_module.md#id1)

- This module allows you to create, modify and delete Zabbix actions.

## [Requirements](zabbix_action_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.9

## [Parameters](zabbix_action_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **acknowledge_operations**  aliases: update_operations  list / elements=dictionary | List of acknowledge operations.  Action acknowledge operations are known as update operations since Zabbix 4.0.  `Suboptions` are the same as for *operations*.  **Default:** `[]` |
| **command**  string | Command to run. |
| **command_type**  string | Type of operation command.  **Choices:**   - `"custom_script"` - `"ipmi"` - `"ssh"` - `"telnet"` - `"global_script"` |
| **execute_on**  string | Target on which the custom script operation command will be executed.  **Choices:**   - `"agent"` - `"server"` - `"proxy"` |
| **media_type**  string | Media type that will be used to send the message.  Can be used with *type=send_message* or *type=notify_all_involved* inside *acknowledge_operations*.  Set to `all` for all media types  **Default:** `"all"` |
| **op_message**  string | Operation message text.  If *op_message* and *subject* not defined then “default message” from media type will be used |
| **password**  string | Password used for authentication.  Required when *ssh_auth_type=password* or *command_type=telnet*.  Can be used when *type=remote_command*. |
| **port**  integer | Port number used for authentication.  Can be used when *command_type in [ssh, telnet]* and *type=remote_command*. |
| **run_on_groups**  list / elements=string | Host groups to run remote commands on.  Required when *type=remote_command* and *run_on_hosts* is not set. |
| **run_on_hosts**  list / elements=string | Hosts to run remote commands on.  Required when *type=remote_command* and *run_on_groups* is not set.  If set to 0 the command will be run on the current host. |
| **script_name**  string | The name of script used for global script commands.  Required when *command_type=global_script*.  Can be used when *type=remote_command*. |
| **send_to_groups**  list / elements=string | User groups to send messages to. |
| **send_to_users**  list / elements=string | Users (usernames or aliases) to send messages to. |
| **ssh_auth_type**  string | Authentication method used for SSH commands.  Required when *type=remote_command* and *command_type=ssh*.  **Choices:**   - `"password"` - `"public_key"` |
| **ssh_privatekey_file**  string | Name of the private key file used for SSH commands with public key authentication.  Required when *ssh_auth_type=public_key*.  Can be used when *type=remote_command*. |
| **ssh_publickey_file**  string | Name of the public key file used for SSH commands with public key authentication.  Required when *ssh_auth_type=public_key*.  Can be used when *type=remote_command*. |
| **subject**  string | Operation message subject.  If *op_message* and *subject* not defined then “default message” from media type will be used |
| **type**  string / required | Type of operation.  **Choices:**   - `"send_message"` - `"remote_command"` - `"notify_all_involved"` |
| **username**  string | User name used for authentication.  Required when *ssh_auth_type in [public_key, password]* or *command_type=telnet*.  Can be used when *type=remote_command*. |
| **conditions**  list / elements=dictionary | List of conditions to use for filtering results.  For more information about suboptions of this option please check out Zabbix API documentation <https://www.zabbix.com/documentation/5.0/manual/api/reference/action/object#action_filter_condition>  **Default:** `[]` |
| **formulaid**  string | Arbitrary unique ID that is used to reference the condition from a custom expression.  Can only contain upper-case letters.  Required for custom expression filters and ignored otherwise. |
| **operator**  string / required | Condition operator.  When *type* is set to `time_period`, the choices are `in`, `not in`.  **Choices:**   - `"equals"` - `"="` - `"does not equal"` - `"<>"` - `"contains"` - `"like"` - `"does not contain"` - `"not like"` - `"in"` - `"is greater than or equals"` - `">="` - `"is less than or equals"` - `"<="` - `"not in"` - `"matches"` - `"does not match"` - `"Yes"` - `"No"` |
| **type**  string / required | Type (label) of the condition.  Possible values when *event_source=trigger*:  - `host_group` - `host` - `trigger` - `trigger_name` - `trigger_severity` - `time_period` - `host_template` - `maintenance_status` known in Zabbix 4.0 and above as ‘Problem is suppressed’ - `event_tag` - `event_tag_value`  Possible values when *event_source=discovery*:  - `host_IP` - `discovered_service_type` - `discovered_service_port` - `discovery_status` - `uptime_or_downtime_duration` - `received_value` - `discovery_rule` - `discovery_check` - `proxy` - `discovery_object`  Possible values when *event_source=auto_registration*:  - `proxy` - `host_name` - `host_metadata`  Possible values when *event_source=internal*:  - `host_group` - `host` - `host_template` - `event_type` |
| **value**  string | Value to compare with.  When *type=discovery_status*, the choices are:  - `up` - `down` - `discovered` - `lost`  When *type=discovery_object*, the choices are:  - `host` - `service`  When *type=event_type*, the choices are:  - `item in not supported state` - `item in normal state` - `LLD rule in not supported state` - `LLD rule in normal state` - `trigger in unknown state` - `trigger in normal state`  When *type=trigger_severity*, the choices are (case-insensitive):  - `not classified` - `information` - `warning` - `average` - `high` - `disaster`  Irrespective of user-visible names being changed in Zabbix. Defaults to `not classified` if omitted.  Besides the above options, this is usually either the name of the object or a string to compare with. |
| **value2**  string | Secondary value to compare with.  Required for trigger actions when condition *type=event_tag_value*. |
| **esc_period**  string | Default operation step duration. Must be greater than 60 seconds.  Accepts seconds, time unit with suffix and user macro since => Zabbix 3.4  Required when `state=present`. |
| **eval_type**  string | Filter condition evaluation method.  Defaults to `andor` if conditions are less then 2 or if *formula* is not specified.  Defaults to `custom_expression` when formula is specified.  **Choices:**   - `"andor"` - `"and"` - `"or"` - `"custom_expression"` |
| **event_source**  string | Type of events that the action will handle.  Required when `state=present`.  **Choices:**   - `"trigger"` - `"discovery"` - `"auto_registration"` - `"internal"` |
| **formula**  string | User-defined expression to be used for evaluating conditions with a custom expression.  The expression must contain IDs that reference each condition by its formulaid.  The IDs used in the expression must exactly match the ones defined in the *conditions*. No condition can remain unused or omitted.  Required when *eval_type=custom_expression*.  Use sequential IDs that start at “A”. If non-sequential IDs are used, Zabbix re-indexes them. This makes each module run notice the difference in IDs and update the action. |
| **http_login_password**  string | Basic Auth password |
| **http_login_user**  string | Basic Auth login |
| **name**  string / required | Name of the action |
| **notify_if_canceled**  boolean | Weather to notify when escalation is canceled.  Can be used when *event_source=trigger*.  **Choices:**   - `false` - `true` ← (default) |
| **operations**  list / elements=dictionary | List of action operations  **Default:** `[]` |
| **command**  string | Command to run.  Required when *type=remote_command* and *command_type!=global_script*. |
| **command_type**  string | Type of operation command.  Required when *type=remote_command*.  **Choices:**   - `"custom_script"` - `"ipmi"` - `"ssh"` - `"telnet"` - `"global_script"` |
| **esc_period**  string | Duration of an escalation step in seconds.  Must be greater than 60 seconds.  Accepts seconds, time unit with suffix and user macro.  If set to 0 or 0s, the default action escalation period will be used.  **Default:** `"0s"` |
| **esc_step_from**  integer | Step to start escalation from.  **Default:** `1` |
| **esc_step_to**  integer | Step to end escalation at.  Specify 0 for infinitely.  **Default:** `1` |
| **execute_on**  string | Target on which the custom script operation command will be executed.  Required when *type=remote_command* and *command_type=custom_script*.  **Choices:**   - `"agent"` - `"server"` - `"proxy"` |
| **host_groups**  list / elements=string | List of host groups host should be added to.  Required when *type=add_to_host_group* or *type=remove_from_host_group*. |
| **inventory**  string | Host inventory mode.  Required when *type=set_host_inventory_mode*.  **Choices:**   - `"manual"` - `"automatic"` |
| **media_type**  string | Media type that will be used to send the message.  Can be used with *type=send_message* or *type=notify_all_involved* inside *acknowledge_operations*.  Set to `all` for all media types  **Default:** `"all"` |
| **op_message**  string | Operation message text.  If *op_message* and *subject* not defined then “default message” from media type will be used |
| **operation_condition**  string | The action operation condition object defines a condition that must be met to perform the current operation.  **Choices:**   - `"acknowledged"` - `"not_acknowledged"` |
| **password**  string | Password used for authentication.  Required when *ssh_auth_type=password* or *command_type=telnet*.  Can be used when *type=remote_command*. |
| **port**  integer | Port number used for authentication.  Can be used when *command_type in [ssh, telnet]* and *type=remote_command*. |
| **run_on_groups**  list / elements=string | Host groups to run remote commands on.  Required when *type=remote_command* and *run_on_hosts* is not set. |
| **run_on_hosts**  list / elements=string | Hosts to run remote commands on.  Required when *type=remote_command* and *run_on_groups* is not set.  If set to 0 the command will be run on the current host. |
| **script_name**  string | The name of script used for global script commands.  Required when *command_type=global_script*.  Can be used when *type=remote_command*. |
| **send_to_groups**  list / elements=string | User groups to send messages to. |
| **send_to_users**  list / elements=string | Users (usernames or aliases) to send messages to. |
| **ssh_auth_type**  string | Authentication method used for SSH commands.  Required when *type=remote_command* and *command_type=ssh*.  **Choices:**   - `"password"` - `"public_key"` |
| **ssh_privatekey_file**  string | Name of the private key file used for SSH commands with public key authentication.  Required when *ssh_auth_type=public_key*.  Can be used when *type=remote_command*. |
| **ssh_publickey_file**  string | Name of the public key file used for SSH commands with public key authentication.  Required when *ssh_auth_type=public_key*.  Can be used when *type=remote_command*. |
| **subject**  string | Operation message subject.  If *op_message* and *subject* not defined then “default message” from media type will be used |
| **templates**  list / elements=string | List of templates host should be linked to.  Required when *type=link_to_template* or *type=unlink_from_template*. |
| **type**  string / required | Type of operation.  Valid choices when setting type for *recovery_operations* and *acknowledge_operations*:  - `send_message` - `remote_command` - `notify_all_involved`  Choice `notify_all_involved` only supported in *recovery_operations* and *acknowledge_operations*.  **Choices:**   - `"send_message"` - `"remote_command"` - `"add_host"` - `"remove_host"` - `"add_to_host_group"` - `"remove_from_host_group"` - `"link_to_template"` - `"unlink_from_template"` - `"enable_host"` - `"disable_host"` - `"set_host_inventory_mode"` - `"notify_all_involved"` |
| **username**  string | User name used for authentication.  Required when *ssh_auth_type in [public_key, password]* or *command_type=telnet*.  Can be used when *type=remote_command*. |
| **pause_in_maintenance**  boolean | Whether to pause escalation during maintenance periods or not.  Can be used when *event_source=trigger*.  **Choices:**   - `false` - `true` ← (default) |
| **pause_symptoms**  boolean | Whether to pause escalation if event is a symptom event.  *supported* if `event_source` is set to `trigger`  Works only with >= Zabbix 6.4  **Choices:**   - `false` - `true` ← (default) |
| **recovery_operations**  list / elements=dictionary | List of recovery operations.  `Suboptions` are the same as for *operations*.  **Default:** `[]` |
| **command**  string | Command to run. |
| **command_type**  string | Type of operation command.  **Choices:**   - `"custom_script"` - `"ipmi"` - `"ssh"` - `"telnet"` - `"global_script"` |
| **execute_on**  string | Target on which the custom script operation command will be executed.  **Choices:**   - `"agent"` - `"server"` - `"proxy"` |
| **media_type**  string | Media type that will be used to send the message.  Can be used with *type=send_message* or *type=notify_all_involved* inside *acknowledge_operations*.  Set to `all` for all media types  **Default:** `"all"` |
| **op_message**  string | Operation message text.  If *op_message* and *subject* not defined then “default message” from media type will be used |
| **password**  string | Password used for authentication.  Required when *ssh_auth_type=password* or *command_type=telnet*.  Can be used when *type=remote_command*. |
| **port**  integer | Port number used for authentication.  Can be used when *command_type in [ssh, telnet]* and *type=remote_command*. |
| **run_on_groups**  list / elements=string | Host groups to run remote commands on.  Required when *type=remote_command* and *run_on_hosts* is not set. |
| **run_on_hosts**  list / elements=string | Hosts to run remote commands on.  Required when *type=remote_command* and *run_on_groups* is not set.  If set to 0 the command will be run on the current host. |
| **script_name**  string | The name of script used for global script commands.  Required when *command_type=global_script*.  Can be used when *type=remote_command*. |
| **send_to_groups**  list / elements=string | User groups to send messages to. |
| **send_to_users**  list / elements=string | Users (usernames or aliases) to send messages to. |
| **ssh_auth_type**  string | Authentication method used for SSH commands.  Required when *type=remote_command* and *command_type=ssh*.  **Choices:**   - `"password"` - `"public_key"` |
| **ssh_privatekey_file**  string | Name of the private key file used for SSH commands with public key authentication.  Required when *ssh_auth_type=public_key*.  Can be used when *type=remote_command*. |
| **ssh_publickey_file**  string | Name of the public key file used for SSH commands with public key authentication.  Required when *ssh_auth_type=public_key*.  Can be used when *type=remote_command*. |
| **subject**  string | Operation message subject.  If *op_message* and *subject* not defined then “default message” from media type will be used |
| **type**  string / required | Type of operation.  **Choices:**   - `"send_message"` - `"remote_command"` - `"notify_all_involved"` |
| **username**  string | User name used for authentication.  Required when *ssh_auth_type in [public_key, password]* or *command_type=telnet*.  Can be used when *type=remote_command*. |
| **state**  string | State of the action.  On `present`, it will create an action if it does not exist or update the action if the associated data is different.  On `absent`, it will remove the action if it exists.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **status**  string | Status of the action.  **Choices:**   - `"enabled"` ← (default) - `"disabled"` |

## [Examples](zabbix_action_module.md#id4)

```yaml+jinja
# If you want to use Username and Password to be authenticated by Zabbix Server
- name: Set credentials to access Zabbix Server API
  ansible.builtin.set_fact:
    ansible_user: Admin
    ansible_httpapi_pass: zabbix

# If you want to use API token to be authenticated by Zabbix Server
# https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/administration/general#api-tokens
- name: Set API token
  ansible.builtin.set_fact:
    ansible_zabbix_auth_key: 8ec0d52432c15c91fcafe9888500cf9a607f44091ab554dbee860f6b44fac895

# Trigger action with only one condition
- name: Deploy trigger action
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_action:
    name: "Send alerts to Admin"
    event_source: "trigger"
    state: present
    status: enabled
    esc_period: 60
    conditions:
      - type: "trigger_severity"
        operator: ">="
        value: "Information"
    operations:
      - type: send_message
        subject: "Something bad is happening"
        op_message: "Come on, guys do something"
        media_type: "Email"
        send_to_users:
          - "Admin"

# Trigger action with multiple conditions and operations
- name: Deploy trigger action
  # set task level  variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_action:
    name: "Send alerts to Admin"
    event_source: "trigger"
    state: present
    status: enabled
    esc_period: 1m
    conditions:
      - type: "trigger_name"
        operator: "like"
        value: "Zabbix agent is unreachable"
        formulaid: A
      - type: "trigger_severity"
        operator: ">="
        value: "disaster"
        formulaid: B
    formula: A or B
    operations:
      - type: send_message
        media_type: "Email"
        send_to_users:
          - "Admin"
      - type: remote_command
        command: "systemctl restart zabbix-agent"
        command_type: custom_script
        execute_on: server
        run_on_hosts:
          - 0

# Trigger action with recovery and acknowledge operations
- name: Deploy trigger action
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_action:
    name: "Send alerts to Admin"
    event_source: "trigger"
    state: present
    status: enabled
    esc_period: 1h
    conditions:
      - type: "trigger_severity"
        operator: ">="
        value: "Information"
    operations:
      - type: send_message
        subject: "Something bad is happening"
        op_message: "Come on, guys do something"
        media_type: "Email"
        send_to_users:
          - "Admin"
    recovery_operations:
      - type: send_message
        subject: "Host is down"
        op_message: "Come on, guys do something"
        media_type: "Email"
        send_to_users:
          - "Admin"
    acknowledge_operations:
      - type: send_message
        media_type: "Email"
        send_to_users:
          - "Admin"
```

## [Return Values](zabbix_action_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | The result of the operation  **Returned:** success  **Sample:** `"Action Deleted: Register webservers, ID: 0001"` |

### Authors

- Ruben Tsirunyan (@rubentsirunyan)
- Ruben Harutyunov (@K-DOT)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
- [Homepage](https://github.com/ansible-collections/community.zabbix)
- [Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
