---
collection: ansible
version: "6"
title: "community.vmware.vmware_maintenancemode module – Place a host into maintenance mode"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_maintenancemode_module.html
fetched_at: 2026-07-27T17:22:40+00:00
---
# community.vmware.vmware_maintenancemode module – Place a host into maintenance mode

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
> To use it in a playbook, specify: `community.vmware.vmware_maintenancemode`.

- [Synopsis](vmware_maintenancemode_module.md#synopsis)
- [Parameters](vmware_maintenancemode_module.md#parameters)
- [Notes](vmware_maintenancemode_module.md#notes)
- [Examples](vmware_maintenancemode_module.md#examples)
- [Return Values](vmware_maintenancemode_module.md#return-values)

## [Synopsis](vmware_maintenancemode_module.md#id1)

- This module can be used for placing a ESXi host into maintenance mode.
- Support for VSAN compliant maintenance mode when selected.

## [Parameters](vmware_maintenancemode_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **esxi_hostname**  string / required | Name of the host as defined in vCenter. |
| **evacuate**  boolean | If set to `True`, evacuate all powered off VMs.  Choices:   - `false` ← (default) - `true` |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | Enter or exit maintenance mode.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | Specify a timeout for the operation.  Default: `0` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |
| **vsan**  aliases: vsan_mode  string | Specify which VSAN compliant mode to enter.  Choices:   - `"ensureObjectAccessibility"` - `"evacuateAllData"` - `"noAction"` |

## [Notes](vmware_maintenancemode_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_maintenancemode_module.md#id4)

```yaml+jinja
- name: Enter VSAN-Compliant Maintenance Mode
  community.vmware.vmware_maintenancemode:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi_hostname }}"
    vsan: ensureObjectAccessibility
    evacuate: true
    timeout: 3600
    state: present
  delegate_to: localhost
```

## [Return Values](vmware_maintenancemode_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hostname**  string | Name of host in vCenter  Returned: always  Sample: `"esxi.local.domain"` |
| **hostsystem**  string | Name of vim reference  Returned: always  Sample: `"'vim.HostSystem:host-236'"` |
| **status**  string | Action taken  Returned: always  Sample: `"ENTER"` |

### Authors

- Jay Jahns (@jjahns)
- Abhijeet Kasurde (@Akasurde)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
