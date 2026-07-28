---
collection: ansible
version: "6"
title: "community.network.ce_info_center_trap module – Manages information center trap configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_info_center_trap_module.html
fetched_at: 2026-07-27T17:17:29+00:00
---
# community.network.ce_info_center_trap module – Manages information center trap configuration on HUAWEI CloudEngine switches.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.ce_info_center_trap`.

- [Synopsis](ce_info_center_trap_module.md#synopsis)
- [Parameters](ce_info_center_trap_module.md#parameters)
- [Notes](ce_info_center_trap_module.md#notes)
- [Examples](ce_info_center_trap_module.md#examples)
- [Return Values](ce_info_center_trap_module.md#return-values)

## [Synopsis](ce_info_center_trap_module.md#id1)

- Manages information center trap configurations on HUAWEI CloudEngine switches.

## [Parameters](ce_info_center_trap_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **channel_id**  string | Number of a channel. The value is an integer ranging from 0 to 9. The default value is 0. |
| **module_name**  string | Module name of the rule. The value is a string of 1 to 31 case-insensitive characters. The default value is default. Please use lower-case letter, such as [aaa, acl, arp, bfd]. |
| **state**  string | Specify desired state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **trap_buff_enable**  string | Whether a trap buffer is enabled to output information.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **trap_buff_size**  string | Size of a trap buffer. The value is an integer ranging from 0 to 1024. The default value is 256. |
| **trap_enable**  string | Whether a device is enabled to output alarms.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **trap_level**  string | Trap level permitted to output.  Choices:   - `"emergencies"` - `"alert"` - `"critical"` - `"error"` - `"warning"` - `"notification"` - `"informational"` - `"debugging"` |
| **trap_time_stamp**  string | Timestamp format of alarm information.  Choices:   - `"date_boot"` - `"date_second"` - `"date_tenthsecond"` - `"date_millisecond"` - `"shortdate_second"` - `"shortdate_tenthsecond"` - `"shortdate_millisecond"` - `"formatdate_second"` - `"formatdate_tenthsecond"` - `"formatdate_millisecond"` |

## [Notes](ce_info_center_trap_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_info_center_trap_module.md#id4)

```yaml+jinja
- name: CloudEngine info center trap test
  hosts: cloudengine
  connection: local
  gather_facts: no
  vars:
    cli:
      host: "{{ inventory_hostname }}"
      port: "{{ ansible_ssh_port }}"
      username: "{{ username }}"
      password: "{{ password }}"
      transport: cli

  tasks:

  - name: "Config trap buffer"
    community.network.ce_info_center_trap:
      state: present
      trap_buff_enable: true
      trap_buff_size: 768
      provider: "{{ cli }}"

  - name: "Undo trap buffer"
    community.network.ce_info_center_trap:
      state: absent
      trap_buff_enable: true
      trap_buff_size: 768
      provider: "{{ cli }}"

  - name: "Config trap module log level"
    community.network.ce_info_center_trap:
      state: present
      module_name: aaa
      channel_id: 1
      trap_enable: true
      trap_level: error
      provider: "{{ cli }}"

  - name: "Undo trap module log level"
    community.network.ce_info_center_trap:
      state: absent
      module_name: aaa
      channel_id: 1
      trap_enable: true
      trap_level: error
      provider: "{{ cli }}"
```

## [Return Values](ce_info_center_trap_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of aaa params after module execution  Returned: always  Sample: `{"icTrapBuffEn": "true", "trapBuffSize": "768"}` |
| **existing**  dictionary | k/v pairs of existing aaa server  Returned: always  Sample: `{"icTrapBuffEn": "false", "trapBuffSize": "256"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: always  Sample: `{"state": "present", "trap_buff_enable": "true", "trap_buff_size": "768"}` |
| **updates**  list / elements=string | command sent to the device  Returned: always  Sample: `["info-center trapbuffer", "info-center trapbuffer size 768"]` |

### Authors

- wangdezhuang (@QijunPan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
