---
collection: ansible
version: "6"
title: "community.vmware.vmware_vcenter_settings_info module – Gather info vCenter settings"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_vcenter_settings_info_module.html
fetched_at: 2026-07-27T17:22:51+00:00
---
# community.vmware.vmware_vcenter_settings_info module – Gather info vCenter settings

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
> To use it in a playbook, specify: `community.vmware.vmware_vcenter_settings_info`.

- [Synopsis](vmware_vcenter_settings_info_module.md#synopsis)
- [Parameters](vmware_vcenter_settings_info_module.md#parameters)
- [Notes](vmware_vcenter_settings_info_module.md#notes)
- [Examples](vmware_vcenter_settings_info_module.md#examples)
- [Return Values](vmware_vcenter_settings_info_module.md#return-values)

## [Synopsis](vmware_vcenter_settings_info_module.md#id1)

- This module can be used to gather information about vCenter settings.

## [Parameters](vmware_vcenter_settings_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **properties**  list / elements=string | Specify the properties to retrieve.  Example:  properties: [  “config.workflow.port”  ]  Only valid when `schema` is `vsphere`. |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **schema**  string | Specify the output schema desired.  The ‘summary’ output schema is the legacy output from the module.  The ‘vsphere’ output schema is the vSphere API class definition which requires pyvmomi>6.7.1.  Choices:   - `"summary"` ← (default) - `"vsphere"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_vcenter_settings_info_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_vcenter_settings_info_module.md#id4)

```yaml+jinja
- name: "Gather info about vCenter settings"
  community.vmware.vmware_vcenter_settings_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
  register: vcenter_settings_info

- name: "Gather some info from vCenter using the vSphere API output schema"
  community.vmware.vmware_vcenter_settings_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    schema: vsphere
    properties:
      - config.workflow.port
  register: vcenter_settings_info_vsphere_api
```

## [Return Values](vmware_vcenter_settings_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vcenter_config_info**  dictionary | dict of vCenter settings  Returned: success  Sample: `{"db_event_cleanup_previous": true, "db_event_retention_previous": 30, "db_max_connections_previous": 50, "db_task_cleanup_previous": true, "db_task_retention_previous": 30, "directory_query_limit_previous": true, "directory_query_limit_size_previous": 5000, "directory_timeout_previous": 60, "directory_validation_period_previous": 1440, "directory_validation_previous": true, "logging_options_previous": "info", "mail_sender_previous": "", "mail_server_previous": "", "runtime_managed_address_previous": "", "runtime_server_name_previous": "vcenter.local", "runtime_unique_id_previous": 48, "snmp_1_community_previous": "public", "snmp_1_enabled_previous": true, "snmp_1_url_previous": "localhost", "snmp_2_community_previous": "", "snmp_2_enabled_previous": false, "snmp_2_url_previous": "", "snmp_3_community_previous": "", "snmp_3_enabled_previous": false, "snmp_3_url_previous": "", "snmp_4_community_previous": "", "snmp_4_enabled_previous": false, "snmp_4_url_previous": "", "snmp_receiver_1_port_previous": 162, "snmp_receiver_2_port_previous": 162, "snmp_receiver_3_port_previous": 162, "snmp_receiver_4_port_previous": 162, "timeout_long_operations_previous": 120, "timeout_normal_operations_previous": 30}` |

### Authors

- sky-joker (@sky-joker)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
