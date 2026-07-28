---
collection: ansible
version: "8"
title: "vmware.vmware_rest.vcenter_vm_hardware_boot_device module – Sets the virtual devices that will be used to boot the virtual machine"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vmware/vmware_rest/vcenter_vm_hardware_boot_device_module.html
fetched_at: 2026-07-28T02:58:10+00:00
---
# vmware.vmware_rest.vcenter_vm_hardware_boot_device module – Sets the virtual devices that will be used to boot the virtual machine

> **Note:**
>
> This module is part of the [vmware.vmware_rest collection](https://galaxy.ansible.com/ui/repo/published/vmware/vmware_rest/) (version 2.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vmware.vmware_rest`.
> You need further requirements to be able to use this module,
> see [Requirements](vcenter_vm_hardware_boot_device_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-hardware-boot-device-module-requirements) for details.
>
> To use it in a playbook, specify: `vmware.vmware_rest.vcenter_vm_hardware_boot_device`.

New in vmware.vmware_rest 0.1.0

- [Synopsis](vcenter_vm_hardware_boot_device_module.md#synopsis)
- [Requirements](vcenter_vm_hardware_boot_device_module.md#requirements)
- [Parameters](vcenter_vm_hardware_boot_device_module.md#parameters)
- [Notes](vcenter_vm_hardware_boot_device_module.md#notes)
- [Examples](vcenter_vm_hardware_boot_device_module.md#examples)
- [Return Values](vcenter_vm_hardware_boot_device_module.md#return-values)

## [Synopsis](vcenter_vm_hardware_boot_device_module.md#id1)

- Sets the virtual devices that will be used to boot the virtual machine. The virtual machine will check the devices in order, attempting to boot from each, until the virtual machine boots successfully. If the [{@term](mailto:{%40term) list} is empty, the virtual machine will use a default boot sequence. There should be no more than one instance of [{@link](mailto:{%40link) Entry} for a given device type except [{@link](mailto:{%40link) Device.Type#ETHERNET} in the [{@term](mailto:{%40term) list}.

## [Requirements](vcenter_vm_hardware_boot_device_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp

## [Parameters](vcenter_vm_hardware_boot_device_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **devices**  list / elements=dictionary / required | Ordered list of boot devices. This parameter is mandatory.  Valid attributes are:  - `type` (str): The `type` defines the valid device types that may be used as bootable devices. ([‘set’])  This key is required with [‘set’].    - Accepted values:      - CDROM     - DISK     - ETHERNET     - FLOPPY - `nic` (str): Virtual Ethernet device. Ethernet device to use as boot device for this entry. ([‘set’]) - `disks` (list): Virtual disk device. List of virtual disks in boot order. ([‘set’]) |
| **session_timeout**  float  *added in vmware.vmware_rest 2.1.0* | Timeout settings for client session.  The maximal number of seconds for the whole operation including connection establishment, request sending and response.  The default value is 300s. |
| **state**  string | **Choices:**   - `"set"` ← (default) |
| **vcenter_hostname**  string / required | The hostname or IP address of the vSphere vCenter  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **vcenter_password**  string / required | The vSphere vCenter password  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **vcenter_rest_log_file**  string | You can use this optional parameter to set the location of a log file.  This file will be used to record the HTTP REST interaction.  The file will be stored on the host that run the module.  If the value is not specified in the task, the value of  environment variable `VMWARE_REST_LOG_FILE` will be used instead. |
| **vcenter_username**  string / required | The vSphere vCenter username  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **vcenter_validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |
| **vm**  string / required | Virtual machine identifier. This parameter is mandatory. |

## [Notes](vcenter_vm_hardware_boot_device_module.md#id4)

> **Note:**
>
> - Tested on vSphere 7.0.2

## [Examples](vcenter_vm_hardware_boot_device_module.md#id5)

```yaml+jinja
- name: Look up the VM called test_vm1 in the inventory
  register: search_result
  vmware.vmware_rest.vcenter_vm_info:
    filter_names:
    - test_vm1

- name: Collect information about a specific VM
  vmware.vmware_rest.vcenter_vm_info:
    vm: '{{ search_result.value[0].vm }}'
  register: test_vm1_info

- name: Set a boot device
  vmware.vmware_rest.vcenter_vm_hardware_boot_device:
    vm: '{{ test_vm1_info.id }}'
    devices:
    - type: CDROM
  register: _result
```

## [Return Values](vcenter_vm_hardware_boot_device_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **value**  dictionary | Set a boot device  **Returned:** On success  **Sample:** `{}` |

### Authors

- Ansible Cloud Team (@ansible-collections)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vmware.vmware_rest/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/vmware.vmware_rest)
- [Repository (Sources)](https://github.com/ansible-collections/vmware.vmware_rest.git)
