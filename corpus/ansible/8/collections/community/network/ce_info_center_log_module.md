---
collection: ansible
version: "8"
title: "community.network.ce_info_center_log module – Manages information center log configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_info_center_log_module.html
fetched_at: 2026-07-28T01:55:28+00:00
---
# community.network.ce_info_center_log module – Manages information center log configuration on HUAWEI CloudEngine switches.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.ce_info_center_log`.

- [Synopsis](ce_info_center_log_module.md#synopsis)
- [Parameters](ce_info_center_log_module.md#parameters)
- [Notes](ce_info_center_log_module.md#notes)
- [Examples](ce_info_center_log_module.md#examples)
- [Return Values](ce_info_center_log_module.md#return-values)

## [Synopsis](ce_info_center_log_module.md#id1)

- Setting the Timestamp Format of Logs. Configuring the Device to Output Logs to the Log Buffer.

Aliases: network.cloudengine.ce_info_center_log

## [Parameters](ce_info_center_log_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **channel_id**  string | Specifies a channel ID. The value is an integer ranging from 0 to 9. |
| **log_buff_enable**  string | Enables the Switch to send logs to the log buffer.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **log_buff_size**  string | Specifies the maximum number of logs in the log buffer. The value is an integer that ranges from 0 to 10240. If logbuffer-size is 0, logs are not displayed. |
| **log_enable**  string | Indicates whether log filtering is enabled.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **log_level**  string | Specifies a log severity.  **Choices:**   - `"emergencies"` - `"alert"` - `"critical"` - `"error"` - `"warning"` - `"notification"` - `"informational"` - `"debugging"` |
| **log_time_stamp**  string | Sets the timestamp format of logs.  **Choices:**   - `"date_boot"` - `"date_second"` - `"date_tenthsecond"` - `"date_millisecond"` - `"shortdate_second"` - `"shortdate_tenthsecond"` - `"shortdate_millisecond"` - `"formatdate_second"` - `"formatdate_tenthsecond"` - `"formatdate_millisecond"` |
| **module_name**  string | Specifies the name of a module. The value is a module name in registration logs. |
| **state**  string | Determines whether the config should be present or not on the device.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](ce_info_center_log_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_info_center_log_module.md#id4)

```yaml+jinja
- name: CloudEngine info center log test
  hosts: cloudengine
  connection: local
  gather_facts: false
  vars:
    cli:
      host: "{{ inventory_hostname }}"
      port: "{{ ansible_ssh_port }}"
      username: "{{ username }}"
      password: "{{ password }}"
      transport: cli

  tasks:

  - name: "Setting the timestamp format of logs"
    community.network.ce_info_center_log:
      log_time_stamp: date_tenthsecond
      provider: "{{ cli }}"

  - name: "Enabled to output information to the log buffer"
    community.network.ce_info_center_log:
      log_buff_enable: true
      provider: "{{ cli }}"

  - name: "Set the maximum number of logs in the log buffer"
    community.network.ce_info_center_log:
      log_buff_size: 100
      provider: "{{ cli }}"

  - name: "Set a rule for outputting logs to a channel"
    community.network.ce_info_center_log:
      module_name: aaa
      channel_id: 1
      log_enable: true
      log_level: critical
      provider: "{{ cli }}"
```

## [Return Values](ce_info_center_log_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of configuration after module execution  **Returned:** verbose mode  **Sample:** `{"log_time_stamp": "date_tenthsecond"}` |
| **existing**  dictionary | k/v pairs of existing configuration  **Returned:** verbose mode  **Sample:** `{"log_time_stamp": "date_second"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** verbose mode  **Sample:** `{"log_time_stamp": "date_tenthsecond", "state": "present"}` |
| **updates**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["info-center timestamp log date precision-time tenth-second"]` |

### Authors

- QijunPan (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
