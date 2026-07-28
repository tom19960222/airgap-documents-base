---
collection: ansible
version: "6"
title: "community.vmware.vmware_guest_tools_upgrade module – Module to upgrade VMTools"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_guest_tools_upgrade_module.html
fetched_at: 2026-07-27T17:22:06+00:00
---
# community.vmware.vmware_guest_tools_upgrade module – Module to upgrade VMTools

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
> To use it in a playbook, specify: `community.vmware.vmware_guest_tools_upgrade`.

- [Synopsis](vmware_guest_tools_upgrade_module.md#synopsis)
- [Parameters](vmware_guest_tools_upgrade_module.md#parameters)
- [Notes](vmware_guest_tools_upgrade_module.md#notes)
- [Examples](vmware_guest_tools_upgrade_module.md#examples)

## [Synopsis](vmware_guest_tools_upgrade_module.md#id1)

- This module upgrades the VMware Tools on Windows and Linux guests and reboots them.

## [Parameters](vmware_guest_tools_upgrade_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **datacenter**  string / required | Destination datacenter where the virtual machine exists. |
| **folder**  string | Destination folder, absolute or relative path to find an existing guest.  This is required, if `name` is supplied.  The folder should include the datacenter. ESX’s datacenter is ha-datacenter  Examples:  folder: /ha-datacenter/vm  folder: ha-datacenter/vm  folder: /datacenter1/vm  folder: datacenter1/vm  folder: /datacenter1/vm/folder1  folder: datacenter1/vm/folder1  folder: /folder1/datacenter1/vm  folder: folder1/datacenter1/vm  folder: /folder1/datacenter1/vm/folder2 |
| **force_upgrade**  boolean | This flag overrides the guest operating system detection and forcibly upgrade VMware tools or open-vm-tools.  This is useful when VMware tools is too old and unable to detect the ‘guestFamily’ value.  Using this flag may sometime give unexpected results since module will override the default  behaviour of ‘guestFamily’ detection.  Choices:   - `false` ← (default) - `true` |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **moid**  string | Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.  This is required if `name` or `uuid` is not supplied. |
| **name**  string | Name of the virtual machine to work with.  This is required if `uuid` or `moid` is not supplied. |
| **name_match**  string | If multiple virtual machines matching the name, use the first or last found.  Choices:   - `"first"` ← (default) - `"last"` |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **uuid**  string | UUID of the instance to manage if known, this is VMware’s unique identifier.  This is required if `name` or `moid` is not supplied. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_guest_tools_upgrade_module.md#id3)

> **Note:**
>
> - In order to upgrade VMTools, please power on virtual machine before hand - either ‘manually’ or using module [community.vmware.vmware_guest_powerstate](vmware_guest_powerstate_module.md#ansible-collections-community-vmware-vmware-guest-powerstate-module).
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_guest_tools_upgrade_module.md#id4)

```yaml+jinja
- name: Get VM UUID
  vmware_guest_facts:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter }}"
    folder: "/{{datacenter}}/vm"
    name: "{{ vm_name }}"
  delegate_to: localhost
  register: vm_facts

- name: Upgrade VMware Tools using uuid
  community.vmware.vmware_guest_tools_upgrade:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    uuid: "{{ vm_facts.instance.hw_product_uuid }}"
  delegate_to: localhost

- name: Upgrade VMware Tools using MoID
  community.vmware.vmware_guest_tools_upgrade:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    moid: vm-42
  delegate_to: localhost
```

### Authors

- Mike Klebolt (@MikeKlebolt)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
