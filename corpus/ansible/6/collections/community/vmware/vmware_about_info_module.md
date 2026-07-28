---
collection: ansible
version: "6"
title: "community.vmware.vmware_about_info module – Provides information about VMware server to which user is connecting to"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_about_info_module.html
fetched_at: 2026-07-27T17:21:20+00:00
---
# community.vmware.vmware_about_info module – Provides information about VMware server to which user is connecting to

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
> To use it in a playbook, specify: `community.vmware.vmware_about_info`.

- [Synopsis](vmware_about_info_module.md#synopsis)
- [Parameters](vmware_about_info_module.md#parameters)
- [Notes](vmware_about_info_module.md#notes)
- [Examples](vmware_about_info_module.md#examples)
- [Return Values](vmware_about_info_module.md#return-values)

## [Synopsis](vmware_about_info_module.md#id1)

- This module can be used to gather information about VMware server to which user is trying to connect.

## [Parameters](vmware_about_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_about_info_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_about_info_module.md#id4)

```yaml+jinja
- name: Provide information about vCenter
  community.vmware.vmware_about_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
  delegate_to: localhost
  register: vcenter_about_info

- name: Provide information about a standalone ESXi server
  community.vmware.vmware_about_info:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
  delegate_to: localhost
  register: esxi_about_info
```

## [Return Values](vmware_about_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **about_info**  string | dict about VMware server  Returned: success  Sample: `"{'api_type': 'VirtualCenter', 'api_version': '6.5', 'build': '5973321', 'instance_uuid': 'dbed6e0c-bd88-4ef6-b594-21283e1c677f', 'license_product_name': 'VMware VirtualCenter Server', 'license_product_version': '6.0', 'locale_build': '000', 'locale_version': 'INTL', 'os_type': 'darwin-amd64', 'product_full_name': 'VMware vCenter Server 6.5.0 build-5973321', 'product_line_id': 'vpx', 'product_name': 'VMware vCenter Server (govmomi simulator)', 'vendor': 'VMware, Inc.', 'version': '6.5.0'}"` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
