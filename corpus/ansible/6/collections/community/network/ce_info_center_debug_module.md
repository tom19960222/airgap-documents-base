---
collection: ansible
version: "6"
title: "community.network.ce_info_center_debug module – Manages information center debug configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_info_center_debug_module.html
fetched_at: 2026-07-27T17:17:27+00:00
---
# community.network.ce_info_center_debug module – Manages information center debug configuration on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_info_center_debug`.

- [Synopsis](ce_info_center_debug_module.md#synopsis)
- [Parameters](ce_info_center_debug_module.md#parameters)
- [Notes](ce_info_center_debug_module.md#notes)
- [Examples](ce_info_center_debug_module.md#examples)
- [Return Values](ce_info_center_debug_module.md#return-values)

## [Synopsis](ce_info_center_debug_module.md#id1)

- Manages information center debug configurations on HUAWEI CloudEngine switches.

## [Parameters](ce_info_center_debug_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **channel_id**  string | Number of a channel. The value is an integer ranging from 0 to 9. The default value is 0. |
| **debug_enable**  string | Whether a device is enabled to output debugging information.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **debug_level**  string | Debug level permitted to output.  Choices:   - `"emergencies"` - `"alert"` - `"critical"` - `"error"` - `"warning"` - `"notification"` - `"informational"` - `"debugging"` |
| **debug_time_stamp**  string | Timestamp type of debugging information.  Choices:   - `"date_boot"` - `"date_second"` - `"date_tenthsecond"` - `"date_millisecond"` - `"shortdate_second"` - `"shortdate_tenthsecond"` - `"shortdate_millisecond"` - `"formatdate_second"` - `"formatdate_tenthsecond"` - `"formatdate_millisecond"` |
| **module_name**  string | Module name of the rule. The value is a string of 1 to 31 case-insensitive characters. The default value is default. Please use lower-case letter, such as [aaa, acl, arp, bfd]. |
| **state**  string | Specify desired state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](ce_info_center_debug_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_info_center_debug_module.md#id4)

```yaml+jinja
- name: CloudEngine info center debug test
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

  - name: "Config debug time stamp"
    community.network.ce_info_center_debug:
      state: present
      debug_time_stamp: date_boot
      provider: "{{ cli }}"

  - name: "Undo debug time stamp"
    community.network.ce_info_center_debug:
      state: absent
      debug_time_stamp: date_boot
      provider: "{{ cli }}"

  - name: "Config debug module log level"
    community.network.ce_info_center_debug:
      state: present
      module_name: aaa
      channel_id: 1
      debug_enable: true
      debug_level: error
      provider: "{{ cli }}"

  - name: "Undo debug module log level"
    community.network.ce_info_center_debug:
      state: absent
      module_name: aaa
      channel_id: 1
      debug_enable: true
      debug_level: error
      provider: "{{ cli }}"
```

## [Return Values](ce_info_center_debug_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of aaa params after module execution  Returned: always  Sample: `{"debugTimeStamp": "DATE_BOOT"}` |
| **existing**  dictionary | k/v pairs of existing aaa server  Returned: always  Sample: `{"debugTimeStamp": "DATE_MILLISECOND"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: always  Sample: `{"debug_time_stamp": "date_boot", "state": "present"}` |
| **updates**  list / elements=string | command sent to the device  Returned: always  Sample: `["info-center timestamp debugging boot"]` |

### Authors

- wangdezhuang (@QijunPan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
