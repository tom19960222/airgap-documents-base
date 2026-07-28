---
collection: ansible
version: "6"
title: "vmware.vmware_rest.vcenter_vm_hardware_adapter_scsi module – Adds a virtual SCSI adapter to the virtual machine."
source_url: https://docs.ansible.com/projects/ansible/6/collections/vmware/vmware_rest/vcenter_vm_hardware_adapter_scsi_module.html
fetched_at: 2026-07-28T00:22:23+00:00
---
# vmware.vmware_rest.vcenter_vm_hardware_adapter_scsi module – Adds a virtual SCSI adapter to the virtual machine.

> **Note:**
>
> This module is part of the [vmware.vmware_rest collection](https://galaxy.ansible.com/vmware/vmware_rest) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vmware.vmware_rest`.
> You need further requirements to be able to use this module,
> see [Requirements](vcenter_vm_hardware_adapter_scsi_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-hardware-adapter-scsi-module-requirements) for details.
>
> To use it in a playbook, specify: `vmware.vmware_rest.vcenter_vm_hardware_adapter_scsi`.

New in vmware.vmware_rest 0.1.0

- [Synopsis](vcenter_vm_hardware_adapter_scsi_module.md#synopsis)
- [Requirements](vcenter_vm_hardware_adapter_scsi_module.md#requirements)
- [Parameters](vcenter_vm_hardware_adapter_scsi_module.md#parameters)
- [Notes](vcenter_vm_hardware_adapter_scsi_module.md#notes)
- [Examples](vcenter_vm_hardware_adapter_scsi_module.md#examples)
- [Return Values](vcenter_vm_hardware_adapter_scsi_module.md#return-values)

## [Synopsis](vcenter_vm_hardware_adapter_scsi_module.md#id1)

- Adds a virtual SCSI adapter to the virtual machine.

## [Requirements](vcenter_vm_hardware_adapter_scsi_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp

## [Parameters](vcenter_vm_hardware_adapter_scsi_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **adapter**  string | Virtual SCSI adapter identifier. Required with *state=[‘absent’, ‘present’]* |
| **bus**  integer | SCSI bus number. |
| **label**  string | The name of the item |
| **pci_slot_number**  integer | Address of the SCSI adapter on the PCI bus. If the PCI address is invalid, the server will change it when the VM is started or as the device is hot added. |
| **session_timeout**  float  added in vmware.vmware_rest 2.1.0 | Timeout settings for client session.  The maximal number of seconds for the whole operation including connection establishment, request sending and response.  The default value is 300s. |
| **sharing**  string | The `sharing` defines the valid bus sharing modes for a virtual SCSI adapter.  Choices:   - `"NONE"` - `"PHYSICAL"` - `"VIRTUAL"` |
| **state**  string | Choices:   - `"absent"` - `"present"` ← (default) |
| **type**  string | The `type` defines the valid emulation types for a virtual SCSI adapter.  Choices:   - `"BUSLOGIC"` - `"LSILOGIC"` - `"LSILOGICSAS"` - `"PVSCSI"` |
| **vcenter_hostname**  string / required | The hostname or IP address of the vSphere vCenter  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **vcenter_password**  string / required | The vSphere vCenter password  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **vcenter_rest_log_file**  string | You can use this optional parameter to set the location of a log file.  This file will be used to record the HTTP REST interaction.  The file will be stored on the host that run the module.  If the value is not specified in the task, the value of  environment variable `VMWARE_REST_LOG_FILE` will be used instead. |
| **vcenter_username**  string / required | The vSphere vCenter username  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **vcenter_validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |
| **vm**  string / required | Virtual machine identifier. This parameter is mandatory. |

## [Notes](vcenter_vm_hardware_adapter_scsi_module.md#id4)

> **Note:**
>
> - Tested on vSphere 7.0.2

## [Examples](vcenter_vm_hardware_adapter_scsi_module.md#id5)

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

- name: Create a SCSI adapter at PCI slot 35
  vmware.vmware_rest.vcenter_vm_hardware_adapter_scsi:
    vm: '{{ test_vm1_info.id }}'
    pci_slot_number: 35

- name: Drop the SCSI controller
  vmware.vmware_rest.vcenter_vm_hardware_adapter_scsi:
    vm: '{{ test_vm1_info.id }}'
    pci_slot_number: 35
    state: absent
```

## [Return Values](vcenter_vm_hardware_adapter_scsi_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | moid of the resource  Returned: On success  Sample: `"1000"` |
| **value**  dictionary | Create a SCSI adapter at PCI slot 35  Returned: On success  Sample: `{"label": "SCSI controller 0", "pci_slot_number": 35, "scsi": {"bus": 0, "unit": 7}, "sharing": "NONE", "type": "PVSCSI"}` |

### Authors

- Ansible Cloud Team (@ansible-collections)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/vmware.vmware_rest/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/vmware.vmware_rest)
[Repository (Sources)](https://github.com/ansible-collections/vmware.vmware_rest.git)
