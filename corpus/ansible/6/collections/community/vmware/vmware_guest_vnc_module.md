---
collection: ansible
version: "6"
title: "community.vmware.vmware_guest_vnc module – Manages VNC remote display on virtual machines in vCenter"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_guest_vnc_module.html
fetched_at: 2026-07-27T17:22:09+00:00
---
# community.vmware.vmware_guest_vnc module – Manages VNC remote display on virtual machines in vCenter

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
> To use it in a playbook, specify: `community.vmware.vmware_guest_vnc`.

- [DEPRECATED](vmware_guest_vnc_module.md#deprecated)
- [Synopsis](vmware_guest_vnc_module.md#synopsis)
- [Parameters](vmware_guest_vnc_module.md#parameters)
- [Notes](vmware_guest_vnc_module.md#notes)
- [Examples](vmware_guest_vnc_module.md#examples)
- [Return Values](vmware_guest_vnc_module.md#return-values)
- [Status](vmware_guest_vnc_module.md#status)

## [DEPRECATED](vmware_guest_vnc_module.md#id1)

Removed in:
:   major release after 2022-10-15

Why:
:   VNC has been removed in 7.0 and 2022-10-15 is the End of General Support date for 6.5 / 6.7.

Alternative:
:   Users should use the VM Console via the vSphere Client, the ESXi Host Client, or the VMware Remote Console to connect to virtual machines.

## [Synopsis](vmware_guest_vnc_module.md#id2)

- This module can be used to enable and disable VNC remote display on virtual machine.

## [Parameters](vmware_guest_vnc_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **datacenter**  string | Destination datacenter for the deploy operation.  This parameter is case sensitive.  Default: `"ha-datacenter"` |
| **folder**  string | Destination folder, absolute or relative path to find an existing guest.  The folder should include the datacenter. ESX’s datacenter is ha-datacenter |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **moid**  string | Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.  This is required if `name` or `uuid` is not supplied. |
| **name**  string | Name of the virtual machine to work with.  Virtual machine names in vCenter are not necessarily unique, which may be problematic, see `name_match`. |
| **name_match**  string | If multiple virtual machines matching the name, use the first or last found.  Choices:   - `"first"` ← (default) - `"last"` |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | Set the state of VNC on virtual machine.  Choices:   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **uuid**  string | UUID of the instance to manage if known, this is VMware’s unique identifier.  This is required, if `name` or `moid` is not supplied. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |
| **vnc_ip**  string | Sets an IP for VNC on virtual machine.  This is required only when *state* is set to present and will be ignored if *state* is absent.  Default: `"0.0.0.0"` |
| **vnc_password**  string | Sets a password for VNC on virtual machine.  This is required only when *state* is set to present and will be ignored if *state* is absent.  Default: `""` |
| **vnc_port**  integer | The port that VNC listens on. Usually a number between 5900 and 7000 depending on your config.  This is required only when *state* is set to present and will be ignored if *state* is absent.  Default: `0` |

## [Notes](vmware_guest_vnc_module.md#id4)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_guest_vnc_module.md#id5)

```yaml+jinja
- name: Enable VNC remote display on the VM
  community.vmware.vmware_guest_vnc:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    folder: /mydatacenter/vm
    name: testvm1
    vnc_port: 5990
    vnc_password: vNc5ecr3t
    datacenter: "{{ datacenter_name }}"
    state: present
  delegate_to: localhost
  register: vnc_result

- name: Disable VNC remote display on the VM
  community.vmware.vmware_guest_vnc:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    uuid: 32074771-7d6b-699a-66a8-2d9cf8236fff
    state: absent
  delegate_to: localhost
  register: vnc_result

- name: Disable VNC remote display on the VM using MoID
  community.vmware.vmware_guest_vnc:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    moid: vm-42
    state: absent
  delegate_to: localhost
  register: vnc_result
```

## [Return Values](vmware_guest_vnc_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | If anything changed on VM’s extraConfig.  Returned: always |
| **failed**  boolean | If changes failed.  Returned: always |
| **instance**  dictionary | Dictionary describing the VM, including VNC info.  Returned: On success in both *state* |

## [Status](vmware_guest_vnc_module.md#id7)

- This module will be removed in a major release after 2022-10-15.
  *[deprecated]*
- For more information see [DEPRECATED](vmware_guest_vnc_module.md#deprecated).

### Authors

- Armin Ranjbar Daemi (@rmin)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
