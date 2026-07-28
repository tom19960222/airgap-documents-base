---
collection: ansible
version: "6"
title: "community.vmware.vmware_host_powerstate module – Manages power states of host systems in vCenter"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_host_powerstate_module.html
fetched_at: 2026-07-27T17:22:29+00:00
---
# community.vmware.vmware_host_powerstate module – Manages power states of host systems in vCenter

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
> To use it in a playbook, specify: `community.vmware.vmware_host_powerstate`.

- [Synopsis](vmware_host_powerstate_module.md#synopsis)
- [Parameters](vmware_host_powerstate_module.md#parameters)
- [Notes](vmware_host_powerstate_module.md#notes)
- [Examples](vmware_host_powerstate_module.md#examples)
- [Return Values](vmware_host_powerstate_module.md#return-values)

## [Synopsis](vmware_host_powerstate_module.md#id1)

- This module can be used to manage power states of host systems in given vCenter infrastructure.
- User can set power state to ‘power-down-to-standby’, ‘power-up-from-standby’, ‘shutdown-host’ and ‘reboot-host’.
- State ‘reboot-host’, ‘shutdown-host’ and ‘power-down-to-standby’ are not supported by all the host systems.

## [Parameters](vmware_host_powerstate_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster_name**  string | Name of the cluster from which all host systems will be used.  This is required parameter if `esxi_hostname` is not specified. |
| **esxi_hostname**  string | Name of the host system to work with.  This is required parameter if `cluster_name` is not specified. |
| **force**  boolean | This parameter specify if the host should be proceeding with user defined powerstate regardless of whether it is in maintenance mode.  If `state` set to `reboot-host` and `force` as `true`, then host system is rebooted regardless of whether it is in maintenance mode.  If `state` set to `shutdown-host` and `force` as `true`, then host system is shutdown regardless of whether it is in maintenance mode.  If `state` set to `power-down-to-standby` and `force` to `true`, then all powered off VMs will evacuated.  Not applicable if `state` set to `power-up-from-standby`.  Choices:   - `false` ← (default) - `true` |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | Set the state of the host system.  Choices:   - `"power-down-to-standby"` - `"power-up-from-standby"` - `"shutdown-host"` ← (default) - `"reboot-host"` |
| **timeout**  integer | This parameter defines timeout for `state` set to `power-down-to-standby` or `power-up-from-standby`.  Ignored if `state` set to `reboot-host` or `shutdown-host`.  This parameter is defined in seconds.  Default: `600` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_host_powerstate_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_host_powerstate_module.md#id4)

```yaml+jinja
- name: Set the state of a host system to reboot
  community.vmware.vmware_host_powerstate:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    state: reboot-host
  delegate_to: localhost
  register: reboot_host

- name: Set the state of a host system to power down to standby
  community.vmware.vmware_host_powerstate:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    state: power-down-to-standby
  delegate_to: localhost
  register: power_down

- name: Set the state of all host systems from cluster to reboot
  community.vmware.vmware_host_powerstate:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ cluster_name }}'
    state: reboot-host
  delegate_to: localhost
  register: reboot_host
```

## [Return Values](vmware_host_powerstate_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  dictionary | metadata about host system’s state  Returned: always  Sample: `{"esxi01": {"error": "", "msg": "power down 'esxi01' to standby"}}` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
