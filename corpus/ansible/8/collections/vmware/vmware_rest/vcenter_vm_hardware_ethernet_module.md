---
collection: ansible
version: "8"
title: "vmware.vmware_rest.vcenter_vm_hardware_ethernet module – Adds a virtual Ethernet adapter to the virtual machine."
source_url: https://docs.ansible.com/projects/ansible/8/collections/vmware/vmware_rest/vcenter_vm_hardware_ethernet_module.html
fetched_at: 2026-07-28T02:58:18+00:00
---
# vmware.vmware_rest.vcenter_vm_hardware_ethernet module – Adds a virtual Ethernet adapter to the virtual machine.

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
> see [Requirements](vcenter_vm_hardware_ethernet_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-hardware-ethernet-module-requirements) for details.
>
> To use it in a playbook, specify: `vmware.vmware_rest.vcenter_vm_hardware_ethernet`.

New in vmware.vmware_rest 0.1.0

- [Synopsis](vcenter_vm_hardware_ethernet_module.md#synopsis)
- [Requirements](vcenter_vm_hardware_ethernet_module.md#requirements)
- [Parameters](vcenter_vm_hardware_ethernet_module.md#parameters)
- [Notes](vcenter_vm_hardware_ethernet_module.md#notes)
- [Examples](vcenter_vm_hardware_ethernet_module.md#examples)
- [Return Values](vcenter_vm_hardware_ethernet_module.md#return-values)

## [Synopsis](vcenter_vm_hardware_ethernet_module.md#id1)

- Adds a virtual Ethernet adapter to the virtual machine.

## [Requirements](vcenter_vm_hardware_ethernet_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp

## [Parameters](vcenter_vm_hardware_ethernet_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allow_guest_control**  boolean | Flag indicating whether the guest can connect and disconnect the device.  **Choices:**   - `false` - `true` |
| **backing**  dictionary | Physical resource backing for the virtual Ethernet adapter. Required with *state=[‘present’]*  Valid attributes are:  - `type` (str): The `backing_type` defines the valid backing types for a virtual Ethernet adapter. ([‘present’])  This key is required with [‘present’].    - Accepted values:      - DISTRIBUTED_PORTGROUP     - HOST_DEVICE     - OPAQUE_NETWORK     - STANDARD_PORTGROUP - `network` (str): Identifier of the network that backs the virtual Ethernet adapter. ([‘present’]) - `distributed_port` (str): Key of the distributed virtual port that backs the virtual Ethernet adapter. Depending on the type of the Portgroup, the port may be specified using this field. If the portgroup type is early-binding (also known as static), a port is assigned when the Ethernet adapter is configured to use the port. The port may be either automatically or specifically assigned based on the value of this field. If the portgroup type is ephemeral, the port is created and assigned to a virtual machine when it is powered on and the Ethernet adapter is connected. This field cannot be specified as no free ports exist before use. ([‘present’]) |
| **label**  string | The name of the item |
| **mac_address**  string | MAC address. This field may be modified at any time, and changes will be applied the next time the virtual machine is powered on. |
| **mac_type**  string | The `mac_address_type` defines the valid MAC address origins for a virtual Ethernet adapter.  **Choices:**   - `"ASSIGNED"` - `"GENERATED"` - `"MANUAL"` |
| **nic**  string | Virtual Ethernet adapter identifier. Required with *state=[‘absent’, ‘connect’, ‘disconnect’, ‘present’]* |
| **pci_slot_number**  integer | Address of the virtual Ethernet adapter on the PCI bus. If the PCI address is invalid, the server will change when it the VM is started or as the device is hot added. |
| **session_timeout**  float  *added in vmware.vmware_rest 2.1.0* | Timeout settings for client session.  The maximal number of seconds for the whole operation including connection establishment, request sending and response.  The default value is 300s. |
| **start_connected**  boolean | Flag indicating whether the virtual device should be connected whenever the virtual machine is powered on.  **Choices:**   - `false` - `true` |
| **state**  string | **Choices:**   - `"absent"` - `"connect"` - `"disconnect"` - `"present"` ← (default) |
| **type**  string | The `emulation_type` defines the valid emulation types for a virtual Ethernet adapter.  **Choices:**   - `"E1000"` - `"E1000E"` - `"PCNET32"` - `"VMXNET"` - `"VMXNET2"` - `"VMXNET3"` |
| **upt_compatibility_enabled**  boolean | Flag indicating whether Universal Pass-Through (UPT) compatibility should be enabled on this virtual Ethernet adapter. This field may be modified at any time, and changes will be applied the next time the virtual machine is powered on.  **Choices:**   - `false` - `true` |
| **vcenter_hostname**  string / required | The hostname or IP address of the vSphere vCenter  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **vcenter_password**  string / required | The vSphere vCenter password  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **vcenter_rest_log_file**  string | You can use this optional parameter to set the location of a log file.  This file will be used to record the HTTP REST interaction.  The file will be stored on the host that run the module.  If the value is not specified in the task, the value of  environment variable `VMWARE_REST_LOG_FILE` will be used instead. |
| **vcenter_username**  string / required | The vSphere vCenter username  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **vcenter_validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |
| **vm**  string / required | Virtual machine identifier. This parameter is mandatory. |
| **wake_on_lan_enabled**  boolean | Flag indicating whether wake-on-LAN shoud be enabled on this virtual Ethernet adapter. This field may be modified at any time, and changes will be applied the next time the virtual machine is powered on.  **Choices:**   - `false` - `true` |

## [Notes](vcenter_vm_hardware_ethernet_module.md#id4)

> **Note:**
>
> - Tested on vSphere 7.0.2

## [Examples](vcenter_vm_hardware_ethernet_module.md#id5)

```yaml+jinja
- name: Get the dvswitch called my-portgroup
  vmware.vmware_rest.vcenter_network_info:
    filter_types: DISTRIBUTED_PORTGROUP
    filter_names: my portrgoup
  register: my_portgroup

- name: Look up the VM called test_vm1 in the inventory
  register: search_result
  vmware.vmware_rest.vcenter_vm_info:
    filter_names:
    - test_vm1

- name: Collect information about a specific VM
  vmware.vmware_rest.vcenter_vm_info:
    vm: '{{ search_result.value[0].vm }}'
  register: test_vm1_info

- name: Attach a VM to a dvswitch
  vmware.vmware_rest.vcenter_vm_hardware_ethernet:
    vm: '{{ test_vm1_info.id }}'
    pci_slot_number: 4
    backing:
      type: DISTRIBUTED_PORTGROUP
      network: '{{ my_portgroup.value[0].network }}'
    start_connected: false
  register: vm_hardware_ethernet_1

- name: Turn the NIC's start_connected flag on
  vmware.vmware_rest.vcenter_vm_hardware_ethernet:
    nic: '{{ vm_hardware_ethernet_1.id }}'
    start_connected: true
    vm: '{{ test_vm1_info.id }}'

- name: Attach the VM to a standard portgroup
  vmware.vmware_rest.vcenter_vm_hardware_ethernet:
    vm: '{{ test_vm1_info.id }}'
    pci_slot_number: 4
    backing:
      type: STANDARD_PORTGROUP
      network: "{{ lookup('vmware.vmware_rest.network_moid', '/my_dc/network/VM Network') }}"
  register: _result

- name: Attach the VM to a standard portgroup (again)
  vmware.vmware_rest.vcenter_vm_hardware_ethernet:
    vm: '{{ test_vm1_info.id }}'
    pci_slot_number: 4
    backing:
      type: STANDARD_PORTGROUP
      network: "{{ lookup('vmware.vmware_rest.network_moid', '/my_dc/network/VM Network') }}"
  register: _result

- name: Collect a list of the NIC for a given VM
  vmware.vmware_rest.vcenter_vm_hardware_ethernet_info:
    vm: '{{ test_vm1_info.id }}'
  register: vm_nic

- name: Attach the VM to a standard portgroup (again) using the nic ID
  vmware.vmware_rest.vcenter_vm_hardware_ethernet:
    vm: '{{ test_vm1_info.id }}'
    nic: '{{ vm_nic.value[0].nic }}'
    backing:
      type: STANDARD_PORTGROUP
      network: "{{ lookup('vmware.vmware_rest.network_moid', '/my_dc/network/VM Network') }}"
  register: _result

- name: Attach to another standard portgroup
  vmware.vmware_rest.vcenter_vm_hardware_ethernet:
    vm: '{{ test_vm1_info.id }}'
    nic: '{{ vm_nic.value[0].nic }}'
    backing:
      type: STANDARD_PORTGROUP
      network: "{{ lookup('vmware.vmware_rest.network_moid', '/my_dc/network/second_vswitch') }}"
  register: _result
```

## [Return Values](vcenter_vm_hardware_ethernet_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | moid of the resource  **Returned:** On success  **Sample:** `"4000"` |
| **value**  dictionary | Attach a VM to a dvswitch  **Returned:** On success  **Sample:** `{"allow_guest_control": 0, "backing": {"connection_cookie": 632732945, "distributed_port": "2", "distributed_switch_uuid": "50 31 d3 c4 2d 09 4f e3-0f d6 7f 30 3d fe d4 a0", "network": "dvportgroup-1022", "type": "DISTRIBUTED_PORTGROUP"}, "label": "Network adapter 1", "mac_address": "00:50:56:b1:33:76", "mac_type": "ASSIGNED", "pci_slot_number": 4, "start_connected": 0, "state": "NOT_CONNECTED", "type": "VMXNET3", "upt_compatibility_enabled": 0, "wake_on_lan_enabled": 0}` |

### Authors

- Ansible Cloud Team (@ansible-collections)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vmware.vmware_rest/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/vmware.vmware_rest)
- [Repository (Sources)](https://github.com/ansible-collections/vmware.vmware_rest.git)
