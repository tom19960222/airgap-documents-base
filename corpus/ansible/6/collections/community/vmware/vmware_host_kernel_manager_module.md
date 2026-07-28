---
collection: ansible
version: "6"
title: "community.vmware.vmware_host_kernel_manager module – Manage kernel module options on ESXi hosts"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_host_kernel_manager_module.html
fetched_at: 2026-07-27T17:22:23+00:00
---
# community.vmware.vmware_host_kernel_manager module – Manage kernel module options on ESXi hosts

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
> To use it in a playbook, specify: `community.vmware.vmware_host_kernel_manager`.

- [Synopsis](vmware_host_kernel_manager_module.md#synopsis)
- [Parameters](vmware_host_kernel_manager_module.md#parameters)
- [Notes](vmware_host_kernel_manager_module.md#notes)
- [Examples](vmware_host_kernel_manager_module.md#examples)
- [Return Values](vmware_host_kernel_manager_module.md#return-values)

## [Synopsis](vmware_host_kernel_manager_module.md#id1)

- This module can be used to manage kernel module options on ESXi hosts.
- All connected ESXi hosts in scope will be configured when specified.
- If a host is not connected at time of configuration, it will be marked as such in the output.
- Kernel module options may require a reboot to take effect which is not covered here.
- You can use [ansible.builtin.reboot](../../ansible/builtin/reboot_module.md#ansible-collections-ansible-builtin-reboot-module) or [community.vmware.vmware_host_powerstate](vmware_host_powerstate_module.md#ansible-collections-community-vmware-vmware-host-powerstate-module) module to reboot all ESXi host systems.

## [Parameters](vmware_host_kernel_manager_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster_name**  string | Name of the VMware cluster to work on.  All ESXi hosts in this cluster will be configured.  This parameter is required if `esxi_hostname` is not specified. |
| **esxi_hostname**  string | Name of the ESXi host to work on.  This parameter is required if `cluster_name` is not specified. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **kernel_module_name**  string / required | Name of the kernel module to be configured. |
| **kernel_module_option**  string / required | Specified configurations will be applied to the given module.  These values are specified in key=value pairs and separated by a space when there are multiple options. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_host_kernel_manager_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_host_kernel_manager_module.md#id4)

```yaml+jinja
- name: Configure IPv6 to be off via tcpip4 kernel module
  community.vmware.vmware_host_kernel_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    kernel_module_name: "tcpip4"
    kernel_module_option: "ipv6=0"

- name: Using cluster_name, configure vmw_psp_rr options
  community.vmware.vmware_host_kernel_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ virtual_cluster_name }}'
    kernel_module_name: "vmw_psp_rr"
    kernel_module_option: "maxPathsPerDevice=2"
```

## [Return Values](vmware_host_kernel_manager_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **host_kernel_status**  dictionary | dict with information on what was changed, by ESXi host in scope.  Returned: success  Sample: `{"results": {"myhost01.example.com": {"changed": true, "configured_options": "ipv6=0", "msg": "Options have been changed on the kernel module", "original_options": "ipv6=1"}}}` |

### Authors

- Aaron Longchamps (@alongchamps)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
