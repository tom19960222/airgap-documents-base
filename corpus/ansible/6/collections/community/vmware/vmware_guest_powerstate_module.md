---
collection: ansible
version: "6"
title: "community.vmware.vmware_guest_powerstate module – Manages power states of virtual machines in vCenter"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_guest_powerstate_module.html
fetched_at: 2026-07-27T17:22:00+00:00
---
# community.vmware.vmware_guest_powerstate module – Manages power states of virtual machines in vCenter

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
> To use it in a playbook, specify: `community.vmware.vmware_guest_powerstate`.

- [Synopsis](vmware_guest_powerstate_module.md#synopsis)
- [Parameters](vmware_guest_powerstate_module.md#parameters)
- [Notes](vmware_guest_powerstate_module.md#notes)
- [Examples](vmware_guest_powerstate_module.md#examples)

## [Synopsis](vmware_guest_powerstate_module.md#id1)

- Power on / Power off / Restart a virtual machine.

## [Parameters](vmware_guest_powerstate_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **answer**  list / elements=dictionary  added in community.vmware 1.11.0 | A list of questions to answer, should one or more arise while waiting for the task to complete.  Some common uses are to allow a cdrom to be changed even if locked, or to answer the question as to whether a VM was copied or moved.  The *answer* can be used if *state* is `powered-on`. |
| **question**  string / required | The message id, for example `msg.uuid.altered`. |
| **response**  string / required | The choice key, for example `button.uuid.copiedTheVM`. |
| **datacenter**  string  added in community.vmware 1.13.0 | The *datacenter* where the VM you’d like to operate the power.  This parameter is case sensitive.  Default: `"ha-datacenter"` |
| **folder**  string | Destination folder, absolute or relative path to find an existing guest.  The folder should include the datacenter. ESX’s datacenter is ha-datacenter  Examples:  folder: /ha-datacenter/vm  folder: ha-datacenter/vm  folder: /datacenter1/vm  folder: datacenter1/vm  folder: /datacenter1/vm/folder1  folder: datacenter1/vm/folder1  folder: /folder1/datacenter1/vm  folder: folder1/datacenter1/vm  folder: /folder1/datacenter1/vm/folder2 |
| **force**  boolean | Ignore warnings and complete the actions.  This parameter is useful while forcing virtual machine state.  Choices:   - `false` ← (default) - `true` |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **moid**  string | Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.  This is required if `name` or `uuid` is not supplied. |
| **name**  string | Name of the virtual machine to work with.  Virtual machine names in vCenter are not necessarily unique, which may be problematic, see `name_match`. |
| **name_match**  string | If multiple virtual machines matching the name, use the first or last found.  Choices:   - `"first"` ← (default) - `"last"` |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **schedule_task_description**  string | Description of schedule task.  Valid only if `scheduled_at` is specified. |
| **schedule_task_enabled**  boolean | Flag to indicate whether the scheduled task is enabled or disabled.  Choices:   - `false` - `true` ← (default) |
| **schedule_task_name**  string | Name of schedule task.  Valid only if `scheduled_at` is specified. |
| **scheduled_at**  string | Date and time in string format at which specified task needs to be performed.  The required format for date and time - ‘dd/mm/yyyy hh:mm’.  Scheduling task requires vCenter server. A standalone ESXi server does not support this option. |
| **state**  string | Set the state of the virtual machine.  Choices:   - `"powered-off"` - `"powered-on"` - `"reboot-guest"` - `"restarted"` - `"shutdown-guest"` - `"suspended"` - `"present"` ← (default) |
| **state_change_timeout**  integer | If the `state` is set to `shutdown-guest`, by default the module will return immediately after sending the shutdown signal.  If this argument is set to a positive integer, the module will instead wait for the VM to reach the poweredoff state.  The value sets a timeout in seconds for the module to wait for the state change.  Default: `0` |
| **use_instance_uuid**  boolean | Whether to use the VMware instance UUID rather than the BIOS UUID.  Choices:   - `false` ← (default) - `true` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **uuid**  string | UUID of the instance to manage if known, this is VMware’s unique identifier.  This is required if `name` or `moid` is not supplied. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_guest_powerstate_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_guest_powerstate_module.md#id4)

```yaml+jinja
- name: Set the state of a virtual machine to poweroff
  community.vmware.vmware_guest_powerstate:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    folder: "/{{ datacenter_name }}/vm/my_folder"
    name: "{{ guest_name }}"
    state: powered-off
  delegate_to: localhost
  register: deploy

- name: Set the state of a virtual machine to poweron using MoID
  community.vmware.vmware_guest_powerstate:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    folder: "/{{ datacenter_name }}/vm/my_folder"
    moid: vm-42
    state: powered-on
  delegate_to: localhost
  register: deploy

- name: Set the state of a virtual machine to poweroff at given scheduled time
  community.vmware.vmware_guest_powerstate:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    folder: "/{{ datacenter_name }}/vm/my_folder"
    name: "{{ guest_name }}"
    state: powered-off
    scheduled_at: "09/01/2018 10:18"
    schedule_task_name: "task_00001"
    schedule_task_description: "Sample task to poweroff VM"
    schedule_task_enabled: True
  delegate_to: localhost
  register: deploy_at_schedule_datetime

- name: Wait for the virtual machine to shutdown
  community.vmware.vmware_guest_powerstate:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    name: "{{ guest_name }}"
    state: shutdown-guest
    state_change_timeout: 200
  delegate_to: localhost
  register: deploy

- name: Automatically answer if a question locked a virtual machine
  block:
    - name: Power on a virtual machine without the answer param
      community.vmware.vmware_guest_powerstate:
        hostname: "{{ esxi_hostname }}"
        username: "{{ esxi_username }}"
        password: "{{ esxi_password }}"
        validate_certs: false
        folder: "{{ f1 }}"
        name: "{{ vm_name }}"
        state: powered-on
  rescue:
    - name: Power on a virtual machine with the answer param
      community.vmware.vmware_guest_powerstate:
        hostname: "{{ esxi_hostname }}"
        username: "{{ esxi_username }}"
        password: "{{ esxi_password }}"
        validate_certs: false
        folder: "{{ f1 }}"
        name: "{{ vm_name }}"
        answer:
          - question: "msg.uuid.altered"
            response: "button.uuid.copiedTheVM"
        state: powered-on
```

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
