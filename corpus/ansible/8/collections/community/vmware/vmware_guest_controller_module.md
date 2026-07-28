---
collection: ansible
version: "8"
title: "community.vmware.vmware_guest_controller module – Manage disk or USB controllers related to virtual machine in given vCenter infrastructure"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_guest_controller_module.html
fetched_at: 2026-07-28T02:00:07+00:00
---
# community.vmware.vmware_guest_controller module – Manage disk or USB controllers related to virtual machine in given vCenter infrastructure

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
> To use it in a playbook, specify: `community.vmware.vmware_guest_controller`.

- [Synopsis](vmware_guest_controller_module.md#synopsis)
- [Parameters](vmware_guest_controller_module.md#parameters)
- [Notes](vmware_guest_controller_module.md#notes)
- [Examples](vmware_guest_controller_module.md#examples)
- [Return Values](vmware_guest_controller_module.md#return-values)

## [Synopsis](vmware_guest_controller_module.md#id1)

- This module can be used to add, remove disk controllers or USB controllers belonging to given virtual machine.
- All parameters and VMware object names are case sensitive.

## [Parameters](vmware_guest_controller_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **controllers**  list / elements=dictionary | A list of disk or USB controllers to add or remove.  Total 4 disk controllers with the same type are allowed per VM.  Total 2 USB controllers are allowed per VM, 1 USB 2.0 and 1 USB 3.0 or 3.1.  For specific guest OS, supported controller types please refer to VMware Compatibility Guide. |
| **bus_sharing**  string | Bus sharing type for SCSI controller.  **Choices:**   - `"noSharing"` ← (default) - `"physicalSharing"` - `"virtualSharing"` |
| **controller_number**  integer | Disk controller bus number. When `state` is set to `absent`, this parameter is required.  When `type` set to `usb2` or `usb3`, this parameter is not required.  **Choices:**   - `0` - `1` - `2` - `3` |
| **state**  string / required | Add new controller or remove specified existing controller.  If `state` is set to `absent`, the specified controller will be removed from virtual machine when there is no disk or device attaching to it.  If specified controller is removed or not exist, no action will be taken only warning message.  If `state` is set to `present`, new controller with specified type will be added.  If the number of controller with specified controller type reaches it’s maximum, no action will be taken only warning message.  **Choices:**   - `"present"` - `"absent"` |
| **type**  string / required | Type of disk or USB controller.  From vSphere 6.5 and virtual machine with hardware version 13, `nvme` controller starts to be supported.  **Choices:**   - `"buslogic"` - `"lsilogic"` - `"lsilogicsas"` - `"paravirtual"` - `"sata"` - `"nvme"` - `"usb2"` - `"usb3"` |
| **datacenter**  string | The datacenter name to which virtual machine belongs to.  **Default:** `"ha-datacenter"` |
| **folder**  string | Destination folder, absolute or relative path to find an existing guest.  This is a required parameter, only if multiple VMs are found with same name.  The folder should include the datacenter. ESX’s datacenter is ha-datacenter  Examples:  folder: /ha-datacenter/vm  folder: ha-datacenter/vm  folder: /datacenter1/vm  folder: datacenter1/vm  folder: /datacenter1/vm/folder1  folder: datacenter1/vm/folder1  folder: /folder1/datacenter1/vm  folder: folder1/datacenter1/vm  folder: /folder1/datacenter1/vm/folder2 |
| **gather_disk_controller_facts**  boolean | Whether to collect existing disk and USB controllers facts only.  When this parameter is set to `true`, `controllers` parameter will be ignored.  **Choices:**   - `false` ← (default) - `true` |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **moid**  string | Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.  This is required if `name` or `uuid` is not supplied. |
| **name**  string | Name of the virtual machine.  This is a required parameter, if parameter `uuid` or `moid` is not supplied. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **sleep_time**  integer | The sleep time in seconds after VM reconfigure task completes, used when not get the updated VM controller facts after VM reconfiguration.  This parameter is not required. Maximum value is 600.  **Default:** `10` |
| **use_instance_uuid**  boolean | Whether to use the VMware instance UUID rather than the BIOS UUID.  **Choices:**   - `false` ← (default) - `true` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **uuid**  string | UUID of the instance to gather facts if known, this is VMware’s unique identifier.  This is a required parameter, if parameter `name` or `moid` is not supplied. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_guest_controller_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_guest_controller_module.md#id4)

```yaml+jinja
- name: Add disk and USB 3.0 controllers for virtual machine located by name
  community.vmware.vmware_guest_controller:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    name: test_VM
    controllers:
      - state: present
        type: sata
      - state: present
        type: nvme
      - state: present
        type: usb3
  delegate_to: localhost
  register: disk_controller_facts

- name: Remove disk controllers and USB 2.0 from virtual machine located by moid
  community.vmware.vmware_guest_controller:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    moid: vm-33
    controllers:
      - state: absent
        controller_number: 1
        type: sata
      - state: absent
        controller_number: 0
        type: nvme
      - state: absent
        type: usb2
  delegate_to: localhost
  register: disk_controller_facts
```

## [Return Values](vmware_guest_controller_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **disk_controller_status**  dictionary | metadata about the virtual machine’s existing disk controllers or after adding or removing operation  **Returned:** always  **Sample:** `{"nvme": {"0": {"controller_busnumber": 0, "controller_controllerkey": 100, "controller_devicekey": 31000, "controller_disks_devicekey": [], "controller_label": "NVME controller 0", "controller_summary": "NVME controller 0", "controller_unitnumber": 30}}, "sata": {"0": {"controller_busnumber": 0, "controller_controllerkey": 100, "controller_devicekey": 15000, "controller_disks_devicekey": [16000, 16001], "controller_label": "SATA controller 0", "controller_summary": "AHCI", "controller_unitnumber": 24}}, "scsi": {"0": {"controller_bus_sharing": "noSharing", "controller_busnumber": 0, "controller_controllerkey": 100, "controller_devicekey": 1000, "controller_disks_devicekey": [2000], "controller_label": "SCSI controller 0", "controller_summary": "LSI Logic SAS", "controller_unitnumber": 3}, "1": {"controller_bus_sharing": "physicalSharing", "controller_busnumber": 1, "controller_controllerkey": 100, "controller_devicekey": 1001, "controller_disks_devicekey": [], "controller_label": "SCSI controller 1", "controller_summary": "VMware paravirtual SCSI", "controller_unitnumber": 4}}, "usb2": {"0": {"controller_busnumber": 0, "controller_controllerkey": 100, "controller_devicekey": 7000, "controller_disks_devicekey": [], "controller_label": "USB Controller", "controller_summary": "Auto connect Disabled", "controller_unitnumber": 22}}}` |

### Authors

- Diane Wang (@Tomorrow9)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
