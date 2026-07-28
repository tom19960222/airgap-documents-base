---
collection: ansible
version: "6"
title: "community.vmware.vmware_guest_tpm module – Add or remove vTPM device for specified VM."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_guest_tpm_module.html
fetched_at: 2026-07-27T17:22:07+00:00
---
# community.vmware.vmware_guest_tpm module – Add or remove vTPM device for specified VM.

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
> To use it in a playbook, specify: `community.vmware.vmware_guest_tpm`.

New in community.vmware 1.16.0

- [Synopsis](vmware_guest_tpm_module.md#synopsis)
- [Parameters](vmware_guest_tpm_module.md#parameters)
- [Notes](vmware_guest_tpm_module.md#notes)
- [Examples](vmware_guest_tpm_module.md#examples)
- [Return Values](vmware_guest_tpm_module.md#return-values)

## [Synopsis](vmware_guest_tpm_module.md#id1)

- This module is used for adding or removing Virtual Trusted Platform Module(vTPM) device for an existing Virtual Machine. You must create a key provider on vCenter before you can add a vTPM. The ESXi hosts running in your environment must be ESXi 6.7 or later (Windows guest OS), or 7.0 Update 2 (Linux guest OS).

## [Parameters](vmware_guest_tpm_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **datacenter**  string / required | The vCenter datacenter name used to get specified cluster or host.  This parameter is case sensitive. |
| **folder**  string | VM folder, absolute or relative path to find an existing VM.  This parameter is not required, only when multiple VMs are found with the same name.  The folder should include the datacenter name.  Examples:  folder: /datacenter1/vm  folder: datacenter1/vm  folder: /datacenter1/vm/folder1  folder: datacenter1/vm/folder1  folder: /folder1/datacenter1/vm  folder: folder1/datacenter1/vm  folder: /folder1/datacenter1/vm/folder2 |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **moid**  string | Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.  This is required if `name` or `uuid` is not supplied. |
| **name**  string | Name of the virtual machine.  This is required if parameter `uuid` or `moid` is not supplied. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | State of vTPM device.  If set to ‘absent’, vTPM device will be removed from VM.  If set to ‘present’, vTPM device will be added if not present.  Virtual machine should be turned off before add or remove vTPM device.  Virtual machine should not contain snapshots before add vTPM device.  Choices:   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **uuid**  string | UUID of the instance to manage if known, this is VMware’s unique identifier.  This is required if parameter `name` or `moid` is not supplied. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_guest_tpm_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_guest_tpm_module.md#id4)

```yaml+jinja
- name: Add vTPM to specified VM
  community.vmware.vmware_guest_tpm:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter }}"
    name: "Test_VM"
    state: present
  delegate_to: localhost

- name: Remove vTPM from specified VM
  community.vmware.vmware_guest_tpm:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter }}"
    name: "Test_VM"
    state: absent
  delegate_to: localhost
```

## [Return Values](vmware_guest_tpm_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **instance**  dictionary | metadata about the VM vTPM device  Returned: always  Sample: `"None"` |

### Authors

- Diane Wang (@Tomorrow9)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
