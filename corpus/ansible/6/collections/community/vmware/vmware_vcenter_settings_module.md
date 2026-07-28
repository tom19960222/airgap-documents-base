---
collection: ansible
version: "6"
title: "community.vmware.vmware_vcenter_settings module – Configures general settings on a vCenter server"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_vcenter_settings_module.html
fetched_at: 2026-07-27T17:22:51+00:00
---
# community.vmware.vmware_vcenter_settings module – Configures general settings on a vCenter server

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/community/vmware) (version 2.10.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
>
> To use it in a playbook, specify: `community.vmware.vmware_vcenter_settings`.

- [Synopsis](vmware_vcenter_settings_module.md#synopsis)
- [Parameters](vmware_vcenter_settings_module.md#parameters)
- [Notes](vmware_vcenter_settings_module.md#notes)
- [Examples](vmware_vcenter_settings_module.md#examples)
- [Return Values](vmware_vcenter_settings_module.md#return-values)

## [Synopsis](vmware_vcenter_settings_module.md#id1)

- This module can be used to configure the vCenter server general settings (except the statistics).
- The statistics can be configured with the module `vmware_vcenter_statistics`.

## [Parameters](vmware_vcenter_settings_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **advanced_settings**  dictionary  added in community.vmware 1.11.0 | A dictionary of advanced settings.  Default: `{}` |
| **database**  dictionary | The database settings for vCenter server.  Default: `{"event_cleanup": true, "event_retention": 30, "max_connections": 50, "task_cleanup": true, "task_retention": 30}` |
| **event_cleanup**  boolean | Event cleanup.  Choices:   - `false` - `true` ← (default) |
| **event_retention**  integer | Event retention in days.  Default: `30` |
| **max_connections**  integer | Maximum connections.  Default: `50` |
| **task_cleanup**  boolean | Task cleanup.  Choices:   - `false` - `true` ← (default) |
| **task_retention**  integer | Task retention in days.  Default: `30` |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **logging_options**  string | The level of detail that vCenter server usesfor log files.  Choices:   - `"none"` - `"error"` - `"warning"` - `"info"` ← (default) - `"verbose"` - `"trivia"` |
| **mail**  dictionary | The settings vCenter server uses to send email alerts.  Default: `{"sender": "", "server": ""}` |
| **sender**  string | Mail sender address. |
| **server**  string | Mail server. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **runtime_settings**  dictionary | The unique runtime settings for vCenter server. |
| **managed_address**  string | vCenter server managed address. |
| **unique_id**  integer | vCenter server unique ID. |
| **vcenter_server_name**  string | vCenter server name. Default is FQDN. |
| **snmp_receivers**  dictionary | SNMP trap destinations for vCenter server alerts.  Default: `{"snmp_receiver_1_community": "public", "snmp_receiver_1_enabled": true, "snmp_receiver_1_port": 162, "snmp_receiver_1_url": "localhost", "snmp_receiver_2_community": "", "snmp_receiver_2_enabled": false, "snmp_receiver_2_port": 162, "snmp_receiver_2_url": "", "snmp_receiver_3_community": "", "snmp_receiver_3_enabled": false, "snmp_receiver_3_port": 162, "snmp_receiver_3_url": "", "snmp_receiver_4_community": "", "snmp_receiver_4_enabled": false, "snmp_receiver_4_port": 162, "snmp_receiver_4_url": ""}` |
| **snmp_receiver_1_community**  string | Community string.  Default: `"public"` |
| **snmp_receiver_1_enabled**  boolean | Enable receiver.  Choices:   - `false` - `true` ← (default) |
| **snmp_receiver_1_port**  integer | Receiver port.  Default: `162` |
| **snmp_receiver_1_url**  string | Primary Receiver ULR.  Default: `"localhost"` |
| **snmp_receiver_2_community**  string | Community string.  Default: `""` |
| **snmp_receiver_2_enabled**  boolean | Enable receiver.  Choices:   - `false` ← (default) - `true` |
| **snmp_receiver_2_port**  integer | Receiver port.  Default: `162` |
| **snmp_receiver_2_url**  string | Receiver 2 ULR.  Default: `""` |
| **snmp_receiver_3_community**  string | Community string.  Default: `""` |
| **snmp_receiver_3_enabled**  boolean | Enable receiver.  Choices:   - `false` ← (default) - `true` |
| **snmp_receiver_3_port**  integer | Receiver port.  Default: `162` |
| **snmp_receiver_3_url**  string | Receiver 3 ULR.  Default: `""` |
| **snmp_receiver_4_community**  string | Community string.  Default: `""` |
| **snmp_receiver_4_enabled**  boolean | Enable receiver.  Choices:   - `false` ← (default) - `true` |
| **snmp_receiver_4_port**  integer | Receiver port.  Default: `162` |
| **snmp_receiver_4_url**  string | Receiver 4 ULR.  Default: `""` |
| **timeout_settings**  dictionary | The vCenter server connection timeout for normal and long operations.  Default: `{"long_operations": 120, "normal_operations": 30}` |
| **long_operations**  integer | Long operation timeout.  Default: `120` |
| **normal_operations**  integer | Normal operation timeout.  Default: `30` |
| **user_directory**  dictionary | The user directory settings for the vCenter server installation.  Default: `{"query_limit": true, "query_limit_size": 5000, "timeout": 60, "validation": true, "validation_period": 1440}` |
| **query_limit**  boolean | Query limit.  Choices:   - `false` - `true` ← (default) |
| **query_limit_size**  integer | Query limit size.  Default: `5000` |
| **timeout**  integer | User directory timeout.  Default: `60` |
| **validation**  boolean | Mail Validation.  Choices:   - `false` - `true` ← (default) |
| **validation_period**  integer | Validation period.  Default: `1440` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_vcenter_settings_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_vcenter_settings_module.md#id4)

```yaml+jinja
- name: Configure vCenter general settings
  community.vmware.vmware_vcenter_settings:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    database:
      max_connections: 50
      task_cleanup: true
      task_retention: 30
      event_cleanup: true
      event_retention: 30
    runtime_settings:
      unique_id: 1
      managed_address: "{{ lookup('dig', inventory_hostname) }}"
      vcenter_server_name: "{{ inventory_hostname }}"
    user_directory:
      timeout: 60
      query_limit: true
      query_limit_size: 5000
      validation: true
      validation_period: 1440
    mail:
      server: mail.example.com
      sender: vcenter@{{ inventory_hostname }}
    snmp_receivers:
      snmp_receiver_1_url: localhost
      snmp_receiver_1_enabled: true
      snmp_receiver_1_port: 162
      snmp_receiver_1_community: public
    timeout_settings:
      normal_operations: 30
      long_operations: 120
    logging_options: info
  delegate_to: localhost

- name: Enable Retreat Mode for cluster with MOID domain-c8 (https://kb.vmware.com/kb/80472)
  community.vmware.vmware_vcenter_settings:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    advanced_settings:
      'config.vcls.clusters.domain-c8.enabled': 'false'
  delegate_to: localhost
```

## [Return Values](vmware_vcenter_settings_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **results**  dictionary | metadata about vCenter settings  supported diff mode from version 1.8.0  Returned: always  Sample: `{"changed": false, "db_event_cleanup": true, "db_event_retention": 30, "db_max_connections": 50, "db_task_cleanup": true, "db_task_retention": 30, "diff": {"after": {"db_event_cleanup": true, "db_event_retention": 30, "db_max_connections": 50, "db_task_cleanup": true, "db_task_retention": 30, "directory_query_limit": true, "directory_query_limit_size": 5000, "directory_timeout": 60, "directory_validation": true, "directory_validation_period": 1440, "logging_options": "info", "mail_sender": "vcenter@vcenter01.example.com", "mail_server": "mail.example.com", "runtime_managed_address": "192.168.1.10", "runtime_server_name": "vcenter01.example.com", "runtime_unique_id": 1, "snmp_receiver_1_community": "public", "snmp_receiver_1_enabled": true, "snmp_receiver_1_port": 162, "snmp_receiver_1_url": "localhost", "snmp_receiver_2_community": "", "snmp_receiver_2_enabled": false, "snmp_receiver_2_port": 162, "snmp_receiver_2_url": "", "snmp_receiver_3_community": "", "snmp_receiver_3_enabled": false, "snmp_receiver_3_port": 162, "snmp_receiver_3_url": "", "snmp_receiver_4_community": "", "snmp_receiver_4_enabled": false, "snmp_receiver_4_port": 162, "snmp_receiver_4_url": "", "timeout_long_operations": 120, "timeout_normal_operations": 30}, "before": {"db_event_cleanup": true, "db_event_retention": 30, "db_max_connections": 50, "db_task_cleanup": true, "db_task_retention": 30, "directory_query_limit": true, "directory_query_limit_size": 5000, "directory_timeout": 60, "directory_validation": true, "directory_validation_period": 1440, "logging_options": "info", "mail_sender": "vcenter@vcenter01.example.com", "mail_server": "mail.example.com", "runtime_managed_address": "192.168.1.10", "runtime_server_name": "vcenter01.example.com", "runtime_unique_id": 1, "snmp_receiver_1_community": "public", "snmp_receiver_1_enabled": true, "snmp_receiver_1_port": 162, "snmp_receiver_1_url": "localhost", "snmp_receiver_2_community": "", "snmp_receiver_2_enabled": false, "snmp_receiver_2_port": 162, "snmp_receiver_2_url": "", "snmp_receiver_3_community": "", "snmp_receiver_3_enabled": false, "snmp_receiver_3_port": 162, "snmp_receiver_3_url": "", "snmp_receiver_4_community": "", "snmp_receiver_4_enabled": false, "snmp_receiver_4_port": 162, "snmp_receiver_4_url": "", "timeout_long_operations": 120, "timeout_normal_operations": 30}}, "directory_query_limit": true, "directory_query_limit_size": 5000, "directory_timeout": 60, "directory_validation": true, "directory_validation_period": 1440, "logging_options": "info", "mail_sender": "vcenter@vcenter01.example.com", "mail_server": "mail.example.com", "msg": "vCenter settings already configured properly", "runtime_managed_address": "192.168.1.10", "runtime_server_name": "vcenter01.example.com", "runtime_unique_id": 1, "timeout_long_operations": 120, "timeout_normal_operations": 30}` |

### Authors

- Christian Kotte (@ckotte)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
