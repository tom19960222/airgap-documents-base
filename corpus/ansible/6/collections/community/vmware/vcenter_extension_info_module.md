---
collection: ansible
version: "6"
title: "community.vmware.vcenter_extension_info module – Gather info vCenter extensions"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vcenter_extension_info_module.html
fetched_at: 2026-07-27T17:21:17+00:00
---
# community.vmware.vcenter_extension_info module – Gather info vCenter extensions

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
> To use it in a playbook, specify: `community.vmware.vcenter_extension_info`.

- [Synopsis](vcenter_extension_info_module.md#synopsis)
- [Parameters](vcenter_extension_info_module.md#parameters)
- [Notes](vcenter_extension_info_module.md#notes)
- [Examples](vcenter_extension_info_module.md#examples)
- [Return Values](vcenter_extension_info_module.md#return-values)

## [Synopsis](vcenter_extension_info_module.md#id1)

- This module can be used to gather information about vCenter extension.

## [Parameters](vcenter_extension_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vcenter_extension_info_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vcenter_extension_info_module.md#id4)

```yaml+jinja
- name: Gather info about vCenter Extensions
  community.vmware.vcenter_extension_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
  register: ext_info
  delegate_to: localhost
```

## [Return Values](vcenter_extension_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **extension_info**  list / elements=string | List of extensions  Returned: success  Sample: `[{"extension_company": "VMware, Inc.", "extension_key": "com.vmware.vim.ls", "extension_label": "License Services", "extension_last_heartbeat_time": "2018-09-03T09:36:18.003768+00:00", "extension_subject_name": "", "extension_summary": "Provides various license services", "extension_type": "", "extension_version": "5.0"}, {"extension_company": "VMware Inc.", "extension_key": "com.vmware.vim.sms", "extension_label": "VMware vCenter Storage Monitoring Service", "extension_last_heartbeat_time": "2018-09-03T09:36:18.005730+00:00", "extension_subject_name": "", "extension_summary": "Storage Monitoring and Reporting", "extension_type": "", "extension_version": "5.5"}]` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
