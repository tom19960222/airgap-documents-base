---
collection: ansible
version: "6"
title: "community.vmware.vmware_host_auto_start module – Manage the auto power ON or OFF for vm on ESXi host"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_host_auto_start_module.html
fetched_at: 2026-07-27T17:22:12+00:00
---
# community.vmware.vmware_host_auto_start module – Manage the auto power ON or OFF for vm on ESXi host

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
> To use it in a playbook, specify: `community.vmware.vmware_host_auto_start`.

- [Synopsis](vmware_host_auto_start_module.md#synopsis)
- [Parameters](vmware_host_auto_start_module.md#parameters)
- [Notes](vmware_host_auto_start_module.md#notes)
- [Examples](vmware_host_auto_start_module.md#examples)
- [Return Values](vmware_host_auto_start_module.md#return-values)

## [Synopsis](vmware_host_auto_start_module.md#id1)

- In this module, can set up automatic startup and shutdown of virtual machines according to host startup or shutdown.

## [Parameters](vmware_host_auto_start_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **esxi_hostname**  string / required | ESXi hostname where the VM to set auto power on or off exists. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **moid**  string | Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.  This is required if `name` or `uuid` is not supplied. |
| **name**  string | VM name to set auto power on or off.  This is not necessary if change only system default VM settings for autoStart config. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **power_info**  dictionary | Startup or shutdown settings of virtual machine.  This setting will override the system defaults.  Default: `{"start_action": "none", "start_delay": -1, "start_order": -1, "stop_action": "systemDefault", "stop_delay": -1, "wait_for_heartbeat": "systemDefault"}` |
| **start_action**  string | Whether to start the virtual machine when the host startup.  Choices:   - `"none"` ← (default) - `"powerOn"` |
| **start_delay**  integer | Auto start delay in seconds of virtual machine.  Default: `-1` |
| **start_order**  integer | The autostart priority of virtual machine.  Virtual machines with a lower number are powered on first.  On host shutdown, the virtual machines are shut down in reverse order, meaning those with a higher number are powered off first.  Default: `-1` |
| **stop_action**  string | Stop action executed on the virtual machine when the system stops of virtual machine.  Choices:   - `"none"` - `"systemDefault"` ← (default) - `"powerOff"` - `"suspend"` |
| **stop_delay**  integer | Auto stop delay in seconds of virtual machine.  Default: `-1` |
| **wait_for_heartbeat**  string | Continue power on processing when VMware Tools started.  Choices:   - `"no"` - `"yes"` - `"systemDefault"` ← (default) |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **system_defaults**  dictionary | System defaults for auto-start or auto-stop config for virtual machine. |
| **enabled**  boolean | Enable automatically start or stop of virtual machines.  Choices:   - `false` ← (default) - `true` |
| **start_delay**  integer | Default auto start delay in seconds.  Default: `120` |
| **stop_action**  string | Default stop action executed on the virtual machine when the system stops.  Choices:   - `"none"` - `"guestShutdown"` - `"powerOff"` ← (default) - `"suspend"` |
| **stop_delay**  integer | Default auto stop delay in seconds.  Default: `120` |
| **wait_for_heartbeat**  boolean | Continue power on processing when VMware Tools started.  If this parameter is enabled to powers on the next virtual machine without waiting for the delay to pass.  However, the virtual machine must have VMware Tools installed.  Choices:   - `false` ← (default) - `true` |
| **use_instance_uuid**  boolean | Whether to use the VMware instance UUID rather than the BIOS UUID.  Choices:   - `false` ← (default) - `true` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **uuid**  string | VM uuid to set auto power on or off, this is VMware’s unique identifier.  This is required if `name` is not supplied.  This is not necessary if change only system default VM settings for autoStart config. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_host_auto_start_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_host_auto_start_module.md#id4)

```yaml+jinja
---
- name: Update for system defaults config.
  community.vmware.vmware_host_auto_start:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    esxi_hostname: "{{ esxi_hostname }}"
    system_defaults:
      enabled: true
      start_delay: 100
      stop_action: guestShutdown

- name: Update for powerInfo config of virtual machine.
  community.vmware.vmware_host_auto_start:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    esxi_hostname: "{{ esxi_hostname }}"
    name: "{{ vm_name }}"
    power_info:
      start_action: powerOn
      start_delay: 10
      start_order: 1
      stop_action: powerOff
      wait_for_heartbeat: true
```

## [Return Values](vmware_host_auto_start_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **power_info_config**  dictionary | Parameter return when virtual machine power info config is changed.  Returned: changed  Sample: `{"start_action": "powerOn", "start_delay": -1, "start_order": -1, "stop_action": "systemDefault", "stop_delay": -1, "wait_for_heartbeat": "systemDefault"}` |
| **system_defaults_config**  dictionary | Parameter return when system defaults config is changed.  Returned: changed  Sample: `{"enabled": true, "start_delay": 120, "stop_action": "powerOff", "stop_delay": 120, "wait_for_heartbeat": false}` |

### Authors

- sky-joker (@sky-joker)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
