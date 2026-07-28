---
collection: ansible
version: "8"
title: "vmware.vmware_rest.vcenter_vm_hardware_disk module – Adds a virtual disk to the virtual machine"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vmware/vmware_rest/vcenter_vm_hardware_disk_module.html
fetched_at: 2026-07-28T02:58:16+00:00
---
# vmware.vmware_rest.vcenter_vm_hardware_disk module – Adds a virtual disk to the virtual machine

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
> see [Requirements](vcenter_vm_hardware_disk_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-hardware-disk-module-requirements) for details.
>
> To use it in a playbook, specify: `vmware.vmware_rest.vcenter_vm_hardware_disk`.

New in vmware.vmware_rest 0.1.0

- [Synopsis](vcenter_vm_hardware_disk_module.md#synopsis)
- [Requirements](vcenter_vm_hardware_disk_module.md#requirements)
- [Parameters](vcenter_vm_hardware_disk_module.md#parameters)
- [Notes](vcenter_vm_hardware_disk_module.md#notes)
- [Examples](vcenter_vm_hardware_disk_module.md#examples)
- [Return Values](vcenter_vm_hardware_disk_module.md#return-values)

## [Synopsis](vcenter_vm_hardware_disk_module.md#id1)

- Adds a virtual disk to the virtual machine. While adding the virtual disk, a new VMDK file may be created or an existing VMDK file may be used to back the virtual disk.

## [Requirements](vcenter_vm_hardware_disk_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp

## [Parameters](vcenter_vm_hardware_disk_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **backing**  dictionary | Existing physical resource backing for the virtual disk. Exactly one of `#backing` or `#new_vmdk` must be specified. Required with *state=[‘present’]*  Valid attributes are:  - `type` (str): The `backing_type` defines the valid backing types for a virtual disk. ([‘present’])  This key is required with [‘present’].    - Accepted values:      - VMDK_FILE - `vmdk_file` (str): Path of the VMDK file backing the virtual disk. ([‘present’]) |
| **disk**  string | Virtual disk identifier. Required with *state=[‘absent’, ‘present’]* |
| **ide**  dictionary | Address for attaching the device to a virtual IDE adapter.  Valid attributes are:  - `primary` (bool): Flag specifying whether the device should be attached to the primary or secondary IDE adapter of the virtual machine. ([‘present’]) - `master` (bool): Flag specifying whether the device should be the master or slave device on the IDE adapter. ([‘present’]) |
| **label**  string | The name of the item |
| **new_vmdk**  dictionary | Specification for creating a new VMDK backing for the virtual disk. Exactly one of `#backing` or `#new_vmdk` must be specified.  Valid attributes are:  - `name` (str): Base name of the VMDK file. The name should not include the ‘.vmdk’ file extension. ([‘present’]) - `capacity` (int): Capacity of the virtual disk backing in bytes. ([‘present’]) - `storage_policy` (dict): The `storage_policy_spec` [{@term](mailto:{%40term) structure} contains information about the storage policy that is to be associated the with VMDK file. ([‘present’])    - Accepted keys:      - policy (string): Identifier of the storage policy which should be associated with the VMDK file. |
| **sata**  dictionary | Address for attaching the device to a virtual SATA adapter. Required with *state=[‘present’]*  Valid attributes are:  - `bus` (int): Bus number of the adapter to which the device should be attached. ([‘present’])  This key is required with [‘present’]. - `unit` (int): Unit number of the device. ([‘present’]) |
| **scsi**  dictionary | Address for attaching the device to a virtual SCSI adapter. Required with *state=[‘present’]*  Valid attributes are:  - `bus` (int): Bus number of the adapter to which the device should be attached. ([‘present’])  This key is required with [‘present’]. - `unit` (int): Unit number of the device. ([‘present’]) |
| **session_timeout**  float  *added in vmware.vmware_rest 2.1.0* | Timeout settings for client session.  The maximal number of seconds for the whole operation including connection establishment, request sending and response.  The default value is 300s. |
| **state**  string | **Choices:**   - `"absent"` - `"present"` ← (default) |
| **type**  string | The `host_bus_adapter_type` defines the valid types of host bus adapters that may be used for attaching a virtual storage device to a virtual machine.  **Choices:**   - `"IDE"` - `"SATA"` - `"SCSI"` |
| **vcenter_hostname**  string / required | The hostname or IP address of the vSphere vCenter  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **vcenter_password**  string / required | The vSphere vCenter password  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **vcenter_rest_log_file**  string | You can use this optional parameter to set the location of a log file.  This file will be used to record the HTTP REST interaction.  The file will be stored on the host that run the module.  If the value is not specified in the task, the value of  environment variable `VMWARE_REST_LOG_FILE` will be used instead. |
| **vcenter_username**  string / required | The vSphere vCenter username  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **vcenter_validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |
| **vm**  string / required | Virtual machine identifier. This parameter is mandatory. |

## [Notes](vcenter_vm_hardware_disk_module.md#id4)

> **Note:**
>
> - Tested on vSphere 7.0.2

## [Examples](vcenter_vm_hardware_disk_module.md#id5)

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

- name: Create a new disk
  vmware.vmware_rest.vcenter_vm_hardware_disk:
    vm: '{{ test_vm1_info.id }}'
    type: SATA
    new_vmdk:
      capacity: 320000
  register: my_new_disk

- name: Delete the disk
  vmware.vmware_rest.vcenter_vm_hardware_disk:
    vm: '{{ test_vm1_info.id }}'
    disk: '{{ my_new_disk.id }}'
    state: absent
  register: _result
```

## [Return Values](vcenter_vm_hardware_disk_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | moid of the resource  **Returned:** On success  **Sample:** `"16000"` |
| **value**  dictionary | Create a new disk  **Returned:** On success  **Sample:** `{"backing": {"type": "VMDK_FILE", "vmdk_file": "[local] test_vm1/test_vm1_1.vmdk"}, "capacity": 320000, "label": "Hard disk 2", "sata": {"bus": 0, "unit": 0}, "type": "SATA"}` |

### Authors

- Ansible Cloud Team (@ansible-collections)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vmware.vmware_rest/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/vmware.vmware_rest)
- [Repository (Sources)](https://github.com/ansible-collections/vmware.vmware_rest.git)
