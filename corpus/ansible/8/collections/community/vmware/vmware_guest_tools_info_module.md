---
collection: ansible
version: "8"
title: "community.vmware.vmware_guest_tools_info module – Gather info about VMware tools installed in VM"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_guest_tools_info_module.html
fetched_at: 2026-07-28T02:00:24+00:00
---
# community.vmware.vmware_guest_tools_info module – Gather info about VMware tools installed in VM

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/ui/repo/published/community/vmware/) (version 3.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
>
> To use it in a playbook, specify: `community.vmware.vmware_guest_tools_info`.

- [Synopsis](vmware_guest_tools_info_module.md#synopsis)
- [Parameters](vmware_guest_tools_info_module.md#parameters)
- [Notes](vmware_guest_tools_info_module.md#notes)
- [Examples](vmware_guest_tools_info_module.md#examples)
- [Return Values](vmware_guest_tools_info_module.md#return-values)

## [Synopsis](vmware_guest_tools_info_module.md#id1)

- Gather information about the VMware tools installed in virtual machine.

## [Parameters](vmware_guest_tools_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **datacenter**  string | The datacenter name to which virtual machine belongs to. |
| **folder**  string | Destination folder, absolute or relative path to find an existing guest.  This is required if name is supplied.  The folder should include the datacenter. ESXi server’s datacenter is ha-datacenter.  Examples:  folder: /ha-datacenter/vm  folder: ha-datacenter/vm  folder: /datacenter1/vm  folder: datacenter1/vm  folder: /datacenter1/vm/folder1  folder: datacenter1/vm/folder1  folder: /folder1/datacenter1/vm  folder: folder1/datacenter1/vm  folder: /folder1/datacenter1/vm/folder2 |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **moid**  string | Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.  This is required if `name` or `uuid` is not supplied. |
| **name**  string | Name of the VM to get VMware tools info.  This is required if `uuid` or `moid` is not supplied. |
| **name_match**  string | If multiple VMs matching the name, use the first or last found.  **Choices:**   - `"first"` ← (default) - `"last"` |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **use_instance_uuid**  boolean | Whether to use the VMware instance UUID rather than the BIOS UUID.  **Choices:**   - `false` ← (default) - `true` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **uuid**  string | UUID of the instance to manage if known, this is VMware’s unique identifier.  This is required if `name` or `moid` is not supplied. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_guest_tools_info_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_guest_tools_info_module.md#id4)

```yaml+jinja
- name: Gather VMware tools info installed in VM specified by uuid
  community.vmware.vmware_guest_tools_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    uuid: 421e4592-c069-924d-ce20-7e7533fab926
  delegate_to: localhost
  register: vmtools_info

- name: Gather VMware tools info installed in VM specified by name
  community.vmware.vmware_guest_tools_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    name: "{{ vm_name }}"
  delegate_to: localhost
  register: vmtools_info
```

## [Return Values](vmware_guest_tools_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vmtools_info**  dictionary | metadata about the VMware tools installed in virtual machine  **Returned:** always  **Sample:** `{"vm_guest_fullname": "Microsoft Windows 10 (64-bit)", "vm_guest_hostname": "test", "vm_guest_id": "windows9_64Guest", "vm_hw_version": "vmx-14", "vm_ipaddress": "10.10.10.10", "vm_moid": null, "vm_name": "test_vm", "vm_tools_install_status": "toolsOk", "vm_tools_install_type": "guestToolsTypeMSI", "vm_tools_last_install_count": 0, "vm_tools_running_status": "guestToolsRunning", "vm_tools_upgrade_policy": "manual", "vm_tools_version": 10341, "vm_tools_version_status": "guestToolsCurrent", "vm_use_instance_uuid": false, "vm_uuid": null}` |

### Authors

- Diane Wang (@Tomorrow9)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
