---
collection: ansible
version: "8"
title: "community.vmware.vmware_guest_snapshot_info module – Gather info about virtual machine’s snapshots in vCenter"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_guest_snapshot_info_module.html
fetched_at: 2026-07-28T02:00:22+00:00
---
# community.vmware.vmware_guest_snapshot_info module – Gather info about virtual machine’s snapshots in vCenter

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
> To use it in a playbook, specify: `community.vmware.vmware_guest_snapshot_info`.

- [Synopsis](vmware_guest_snapshot_info_module.md#synopsis)
- [Parameters](vmware_guest_snapshot_info_module.md#parameters)
- [Notes](vmware_guest_snapshot_info_module.md#notes)
- [Examples](vmware_guest_snapshot_info_module.md#examples)
- [Return Values](vmware_guest_snapshot_info_module.md#return-values)

## [Synopsis](vmware_guest_snapshot_info_module.md#id1)

- This module can be used to gather information about virtual machine’s snapshots.

## [Parameters](vmware_guest_snapshot_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **datacenter**  string / required | Name of the datacenter. |
| **folder**  string | Destination folder, absolute or relative path to find an existing guest.  This is required parameter, if `name` is supplied.  The folder should include the datacenter. ESX’s datacenter is ha-datacenter  Examples:  folder: /ha-datacenter/vm  folder: ha-datacenter/vm  folder: /datacenter1/vm  folder: datacenter1/vm  folder: /datacenter1/vm/folder1  folder: datacenter1/vm/folder1  folder: /folder1/datacenter1/vm  folder: folder1/datacenter1/vm  folder: /folder1/datacenter1/vm/folder2 |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **moid**  string | Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.  This is required if `name` or `uuid` is not supplied. |
| **name**  string | Name of the VM to work with.  This is required if `uuid` or `moid` is not supplied. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **use_instance_uuid**  boolean | Whether to use the VMware instance UUID rather than the BIOS UUID.  **Choices:**   - `false` ← (default) - `true` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **uuid**  string | UUID of the instance to manage if known, this is VMware’s BIOS UUID by default.  This is required if `name` or `moid` parameter is not supplied.  The `folder` is ignored, if `uuid` is provided. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_guest_snapshot_info_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_guest_snapshot_info_module.md#id4)

```yaml+jinja
- name: Gather snapshot information about the virtual machine in the given vCenter
  community.vmware.vmware_guest_snapshot_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    folder: "/{{ datacenter_name }}/vm/"
    name: "{{ guest_name }}"
  delegate_to: localhost
  register: snapshot_info

- name: Gather snapshot information about the virtual machine using MoID
  community.vmware.vmware_guest_snapshot_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    moid: vm-42
  delegate_to: localhost
  register: snapshot_info
```

## [Return Values](vmware_guest_snapshot_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **guest_snapshots**  dictionary | metadata about the snapshot information  **Returned:** always  **Sample:** `{"current_snapshot": {"creation_time": "2018-02-10T14:48:31.999459+00:00", "description": "", "id": 28, "name": "snap_0003", "quiesced": false, "state": "poweredOff"}, "snapshots": [{"creation_time": "2018-02-10T14:48:31.999459+00:00", "description": "", "id": 28, "name": "snap_0003", "quiesced": false, "state": "poweredOff"}]}` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
