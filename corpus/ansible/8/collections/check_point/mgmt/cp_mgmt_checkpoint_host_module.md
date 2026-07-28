---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_checkpoint_host module – Manages checkpoint-host objects on Checkpoint over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_checkpoint_host_module.html
fetched_at: 2026-07-28T01:15:56+00:00
---
# check_point.mgmt.cp_mgmt_checkpoint_host module – Manages checkpoint-host objects on Checkpoint over Web Services API

> **Note:**
>
> This module is part of the [check_point.mgmt collection](https://galaxy.ansible.com/ui/repo/published/check_point/mgmt/) (version 5.1.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install check_point.mgmt`.
>
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_checkpoint_host`.

New in check_point.mgmt 5.0.0

- [Synopsis](cp_mgmt_checkpoint_host_module.md#synopsis)
- [Parameters](cp_mgmt_checkpoint_host_module.md#parameters)
- [Examples](cp_mgmt_checkpoint_host_module.md#examples)
- [Return Values](cp_mgmt_checkpoint_host_module.md#return-values)

## [Synopsis](cp_mgmt_checkpoint_host_module.md#id1)

- Manages checkpoint-host objects on Checkpoint devices including creating, updating and removing objects.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_checkpoint_host_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  **Choices:**   - `false` - `true` |
| **check_point_host_version**  string | Check Point host platform version. |
| **color**  string | Color of the object. Should be one of existing colors.  **Choices:**   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **groups**  list / elements=string | Collection of group identifiers. |
| **hardware**  string | Hardware name. |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **interfaces**  list / elements=dictionary | Check Point host interfaces. |
| **color**  string | Color of the object. Should be one of existing colors.  **Choices:**   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **mask_length**  integer | IPv4 or IPv6 network mask length. If both masks are required use mask-length4 and mask-length6 fields explicitly. Instead of IPv4 mask length it is possible to specify IPv4 mask itself in subnet-mask field. |
| **mask_length4**  integer | IPv4 network mask length. |
| **mask_length6**  integer | IPv6 network mask length. |
| **name**  string | Interface name. |
| **subnet**  string | IPv4 or IPv6 network address. If both addresses are required use subnet4 and subnet6 fields explicitly. |
| **subnet4**  string | IPv4 network address. |
| **subnet6**  string | IPv6 network address. |
| **subnet_mask**  string | IPv4 network mask. |
| **ip_address**  string | IPv4 or IPv6 address. If both addresses are required use ipv4-address and ipv6-address fields explicitly. |
| **ipv4_address**  string | IPv4 address. |
| **ipv6_address**  string | IPv6 address. |
| **logs_settings**  dictionary | Logs settings. |
| **accept_syslog_messages**  boolean | Enable accept syslog messages.  **Choices:**   - `false` - `true` |
| **alert_when_free_disk_space_below**  boolean | Enable alert when free disk space is below threshold.  **Choices:**   - `false` - `true` |
| **alert_when_free_disk_space_below_threshold**  integer | Alert when free disk space below threshold. |
| **alert_when_free_disk_space_below_type**  string | Alert when free disk space below type.  **Choices:**   - `"none"` - `"log"` - `"popup alert"` - `"mail alert"` - `"snmp trap alert"` - `"user defined alert no.1"` - `"user defined alert no.2"` - `"user defined alert no.3"` |
| **before_delete_keep_logs_from_the_last_days**  boolean | Enable before delete keep logs from the last days.  **Choices:**   - `false` - `true` |
| **before_delete_keep_logs_from_the_last_days_threshold**  integer | Before delete keep logs from the last days threshold. |
| **before_delete_run_script**  boolean | Enable Before delete run script.  **Choices:**   - `false` - `true` |
| **before_delete_run_script_command**  string | Before delete run script command. |
| **delete_index_files_older_than_days**  boolean | Enable delete index files older than days.  **Choices:**   - `false` - `true` |
| **delete_index_files_older_than_days_threshold**  integer | Delete index files older than days threshold. |
| **delete_when_free_disk_space_below**  boolean | Enable delete when free disk space below.  **Choices:**   - `false` - `true` |
| **delete_when_free_disk_space_below_threshold**  integer | Delete when free disk space below threshold. |
| **detect_new_citrix_ica_application_names**  boolean | Enable detect new Citrix ICA application names.  **Choices:**   - `false` - `true` |
| **distribute_logs_between_all_active_servers**  boolean | Distribute logs between all active servers.  **Choices:**   - `false` - `true` |
| **enable_log_indexing**  boolean | Enable log indexing.  **Choices:**   - `false` - `true` |
| **forward_logs_to_log_server**  boolean | Enable forward logs to log server.  **Choices:**   - `false` - `true` |
| **forward_logs_to_log_server_name**  string | Forward logs to log server name. |
| **forward_logs_to_log_server_schedule_name**  string | Forward logs to log server schedule name. |
| **free_disk_space_metrics**  string | Free disk space metrics.  **Choices:**   - `"mbytes"` - `"percent"` |
| **rotate_log_by_file_size**  boolean | Enable rotate log by file size.  **Choices:**   - `false` - `true` |
| **rotate_log_file_size_threshold**  integer | Log file size threshold. |
| **rotate_log_on_schedule**  boolean | Enable rotate log on schedule.  **Choices:**   - `false` - `true` |
| **rotate_log_schedule_name**  string | Rotate log schedule name. |
| **smart_event_intro_correletion_unit**  boolean | Enable SmartEvent intro correlation unit.  **Choices:**   - `false` - `true` |
| **stop_logging_when_free_disk_space_below**  boolean | Enable stop logging when free disk space below.  **Choices:**   - `false` - `true` |
| **stop_logging_when_free_disk_space_below_threshold**  integer | Stop logging when free disk space below threshold. |
| **turn_on_qos_logging**  boolean | Enable turn on QoS Logging.  **Choices:**   - `false` - `true` |
| **update_account_log_every**  integer | Update account log in every amount of seconds. |
| **management_blades**  dictionary | Management blades. |
| **compliance**  boolean | Compliance blade. Can be set when ‘network-policy-management’ was selected to be True.  **Choices:**   - `false` - `true` |
| **endpoint_policy**  boolean | Enable Endpoint Policy. </br>To complete Endpoint Security Management configuration, perform Install Database on your Endpoint Management Server. </br>Field is not supported on Multi Domain Server environment.  **Choices:**   - `false` - `true` |
| **logging_and_status**  boolean | Enable Logging & Status.  **Choices:**   - `false` - `true` |
| **network_policy_management**  boolean | Enable Network Policy Management.  **Choices:**   - `false` - `true` |
| **smart_event_correlation**  boolean | Enable SmartEvent Correlation Unit.  **Choices:**   - `false` - `true` |
| **smart_event_server**  boolean | Enable SmartEvent server. </br>When activating SmartEvent server, blades ‘logging-and-status’ and ‘smart-event-correlation’ should be set to True. </br>To complete SmartEvent configuration, perform Install Database or Install Policy on your Security Management servers and Log servers. </br>Activating SmartEvent Server is not recommended in Management High Availability environment. For more information refer to sk25164.  **Choices:**   - `false` - `true` |
| **user_directory**  boolean | Enable User Directory. Can be set when ‘network-policy-management’ was selected to be True.  **Choices:**   - `false` - `true` |
| **name**  string / required | Object name. |
| **nat_settings**  dictionary | NAT settings. |
| **auto_rule**  boolean | Whether to add automatic address translation rules.  **Choices:**   - `false` - `true` |
| **hide_behind**  string | Hide behind method. This parameter is forbidden in case “method” parameter is “static”.  **Choices:**   - `"gateway"` - `"ip-address"` |
| **install_on**  string | Which gateway should apply the NAT translation. |
| **ip_address**  string | IPv4 or IPv6 address. If both addresses are required use ipv4-address and ipv6-address fields explicitly. This parameter is not required in case “method” parameter is “hide” and “hide-behind” parameter is “gateway”. |
| **ipv4_address**  string | IPv4 address. |
| **ipv6_address**  string | IPv6 address. |
| **method**  string | NAT translation method.  **Choices:**   - `"hide"` - `"static"` |
| **one_time_password**  string | Secure internal connection one time password. |
| **os**  string | Operating system name. |
| **save_logs_locally**  boolean | Enable save logs locally.  **Choices:**   - `false` - `true` |
| **send_alerts_to_server**  list / elements=string | Collection of Server(s) to send alerts to identified by the name or UID. |
| **send_logs_to_backup_server**  list / elements=string | Collection of Backup server(s) to send logs to identified by the name or UID. |
| **send_logs_to_server**  list / elements=string | Collection of Server(s) to send logs to identified by the name or UID. |
| **state**  string | State of the access rule (present or absent). Defaults to present.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=string | Collection of tag identifiers. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_checkpoint_host_module.md#id3)

```yaml+jinja
- name: add-checkpoint-host
  cp_mgmt_checkpoint_host:
    ipv4_address: 5.5.5.5
    management_blades:
      logging_and_status: true
      network_policy_management: true
    name: secondarylogserver
    state: present

- name: set-checkpoint-host
  cp_mgmt_checkpoint_host:
    hardware: Smart-1
    management_blades:
      compliance: true
      network_policy_management: true
      user_directory: true
    name: secondarylogserver
    os: Linux
    state: present

- name: delete-checkpoint-host
  cp_mgmt_checkpoint_host:
    name: secondarylogserver
    state: absent
```

## [Return Values](cp_mgmt_checkpoint_host_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_checkpoint_host**  dictionary | The checkpoint object created or updated.  **Returned:** always, except when deleting the object. |

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
