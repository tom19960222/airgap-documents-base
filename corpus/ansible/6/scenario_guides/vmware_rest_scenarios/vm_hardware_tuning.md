---
collection: ansible
version: "6"
title: "How to modify a virtual machine"
source_url: https://docs.ansible.com/projects/ansible/6/scenario_guides/vmware_rest_scenarios/vm_hardware_tuning.html
fetched_at: 2026-07-27T16:43:19+00:00
---
# How to modify a virtual machine

- [Introduction](vm_hardware_tuning.md#introduction)
- [Scenario requirements](vm_hardware_tuning.md#scenario-requirements)
- [How to add a CDROM drive to a virtual machine](vm_hardware_tuning.md#how-to-add-a-cdrom-drive-to-a-virtual-machine)

  - [Add a new SATA adapter](vm_hardware_tuning.md#add-a-new-sata-adapter)
  - [Result](vm_hardware_tuning.md#result)
  - [Add a CDROM drive](vm_hardware_tuning.md#add-a-cdrom-drive)
  - [Result](vm_hardware_tuning.md#id1)
- [How to attach a VM to a network](vm_hardware_tuning.md#how-to-attach-a-vm-to-a-network)

  - [Attach a new NIC](vm_hardware_tuning.md#attach-a-new-nic)
  - [Result](vm_hardware_tuning.md#id2)
  - [Adjust the configuration of the NIC](vm_hardware_tuning.md#adjust-the-configuration-of-the-nic)
  - [Result](vm_hardware_tuning.md#id3)
- [Increase the memory of the VM](vm_hardware_tuning.md#increase-the-memory-of-the-vm)

  - [Result](vm_hardware_tuning.md#id4)
- [Upgrade the hardware version of the VM](vm_hardware_tuning.md#upgrade-the-hardware-version-of-the-vm)

  - [Result](vm_hardware_tuning.md#id5)
- [Adjust the number of CPUs of the VM](vm_hardware_tuning.md#adjust-the-number-of-cpus-of-the-vm)

  - [Result](vm_hardware_tuning.md#id6)
- [Remove a SATA controller](vm_hardware_tuning.md#remove-a-sata-controller)

  - [Result](vm_hardware_tuning.md#id7)
- [Attach a floppy drive](vm_hardware_tuning.md#attach-a-floppy-drive)

  - [Result](vm_hardware_tuning.md#id8)
- [Attach a new disk](vm_hardware_tuning.md#attach-a-new-disk)

  - [Result](vm_hardware_tuning.md#id9)

## [Introduction](vm_hardware_tuning.md#id10)

This section shows you how to use Ansible to modify an existing virtual machine.

## [Scenario requirements](vm_hardware_tuning.md#id11)

You’ve already followed [How to create a Virtual Machine](create_vm.md#vmware-rest-create-vm) and created a VM.

## [How to add a CDROM drive to a virtual machine](vm_hardware_tuning.md#id12)

In this example, we use the `vcenter_vm_hardware_*` modules to add a new CDROM to an existing VM.

### [Add a new SATA adapter](vm_hardware_tuning.md#id13)

First we create a new SATA adapter. We specify the `pci_slot_number`. This way if we run the task again it won’t do anything if there is already an adapter there.

```YAML+Jinja
- name: Create a SATA adapter at PCI slot 34
  vmware.vmware_rest.vcenter_vm_hardware_adapter_sata:
    vm: '{{ test_vm1_info.id }}'
    pci_slot_number: 34
  register: _sata_adapter_result_1
```

### [Result](vm_hardware_tuning.md#id14)

```YAML+Jinja
{
    "value": {
        "bus": 0,
        "pci_slot_number": 34,
        "label": "SATA controller 0",
        "type": "AHCI"
    },
    "id": "15000",
    "changed": true
}
```

### [Add a CDROM drive](vm_hardware_tuning.md#id15)

Now we can create the CDROM drive:

```YAML+Jinja
- name: Attach an ISO image to a guest VM
  vmware.vmware_rest.vcenter_vm_hardware_cdrom:
    vm: '{{ test_vm1_info.id }}'
    type: SATA
    sata:
      bus: 0
      unit: 2
    start_connected: true
    backing:
      iso_file: '[ro_datastore] fedora.iso'
      type: ISO_FILE
  register: _result
```

### [Result](vm_hardware_tuning.md#id16)

```YAML+Jinja
{
    "value": {
        "start_connected": true,
        "backing": {
            "iso_file": "[ro_datastore] fedora.iso",
            "type": "ISO_FILE"
        },
        "allow_guest_control": false,
        "label": "CD/DVD drive 1",
        "state": "NOT_CONNECTED",
        "type": "SATA",
        "sata": {
            "bus": 0,
            "unit": 2
        }
    },
    "id": "16002",
    "changed": true
}
```

## [How to attach a VM to a network](vm_hardware_tuning.md#id17)

### [Attach a new NIC](vm_hardware_tuning.md#id18)

Here we attach the VM to the network (through the portgroup). We specify a `pci_slot_number` for the same reason.

The second task adjusts the NIC configuration.

```YAML+Jinja
- name: Attach a VM to a dvswitch
  vmware.vmware_rest.vcenter_vm_hardware_ethernet:
    vm: '{{ test_vm1_info.id }}'
    pci_slot_number: 4
    backing:
      type: DISTRIBUTED_PORTGROUP
      network: "{{ my_portgroup_info.dvs_portgroup_info.dvswitch1[0].key }}"
    start_connected: false
  register: vm_hardware_ethernet_1
```

### [Result](vm_hardware_tuning.md#id19)

```YAML+Jinja
{
    "value": {
        "start_connected": false,
        "pci_slot_number": 4,
        "backing": {
            "connection_cookie": 2145337177,
            "distributed_switch_uuid": "50 33 88 3a 8c 6e f9 02-7a fd c2 c0 2c cf f2 ac",
            "distributed_port": "2",
            "type": "DISTRIBUTED_PORTGROUP",
            "network": "dvportgroup-1649"
        },
        "mac_address": "00:50:56:b3:49:5c",
        "mac_type": "ASSIGNED",
        "allow_guest_control": false,
        "wake_on_lan_enabled": false,
        "label": "Network adapter 1",
        "state": "NOT_CONNECTED",
        "type": "VMXNET3",
        "upt_compatibility_enabled": false
    },
    "id": "4000",
    "changed": true
}
```

### [Adjust the configuration of the NIC](vm_hardware_tuning.md#id20)

```YAML+Jinja
- name: Turn the NIC's start_connected flag on
  vmware.vmware_rest.vcenter_vm_hardware_ethernet:
    nic: '{{ vm_hardware_ethernet_1.id }}'
    start_connected: true
    vm: '{{ test_vm1_info.id }}'
```

### [Result](vm_hardware_tuning.md#id21)

```YAML+Jinja
{
    "id": "4000",
    "changed": true
}
```

## [Increase the memory of the VM](vm_hardware_tuning.md#id22)

We can also adjust the amount of memory that we dedicate to our VM.

```YAML+Jinja
- name: Increase the memory of a VM
  vmware.vmware_rest.vcenter_vm_hardware_memory:
    vm: '{{ test_vm1_info.id }}'
    size_MiB: 1080
  register: _result
```

### [Result](vm_hardware_tuning.md#id23)

```YAML+Jinja
{
    "id": null,
    "changed": true
}
```

## [Upgrade the hardware version of the VM](vm_hardware_tuning.md#id24)

Here we use the `vcenter_vm_hardware` module to upgrade the version of the hardware:

```YAML+Jinja
- name: Upgrade the VM hardware version
  vmware.vmware_rest.vcenter_vm_hardware:
    upgrade_policy: AFTER_CLEAN_SHUTDOWN
    upgrade_version: VMX_13
    vm: '{{ test_vm1_info.id }}'
  register: _result
```

### [Result](vm_hardware_tuning.md#id25)

```YAML+Jinja
{
    "id": null,
    "changed": true
}
```

## [Adjust the number of CPUs of the VM](vm_hardware_tuning.md#id26)

You can use `vcenter_vm_hardware_cpu` for that:

```YAML+Jinja
- name: Dedicate one core to the VM
  vmware.vmware_rest.vcenter_vm_hardware_cpu:
    vm: '{{ test_vm1_info.id }}'
    count: 1
  register: _result
```

### [Result](vm_hardware_tuning.md#id27)

```YAML+Jinja
{
    "value": {
        "hot_remove_enabled": false,
        "count": 1,
        "hot_add_enabled": false,
        "cores_per_socket": 1
    },
    "id": null,
    "changed": false
}
```

## [Remove a SATA controller](vm_hardware_tuning.md#id28)

In this example, we remove the SATA controller of the PCI slot 34.

```YAML+Jinja
{
    "changed": true
}
```

### [Result](vm_hardware_tuning.md#id29)

```YAML+Jinja
{
    "changed": true
}
```

## [Attach a floppy drive](vm_hardware_tuning.md#id30)

Here we attach a floppy drive to a VM.

```YAML+Jinja
- name: Add a floppy disk drive
  vmware.vmware_rest.vcenter_vm_hardware_floppy:
    vm: '{{ test_vm1_info.id }}'
    allow_guest_control: true
  register: my_floppy_drive
```

### [Result](vm_hardware_tuning.md#id31)

```YAML+Jinja
{
    "value": {
        "start_connected": false,
        "backing": {
            "auto_detect": true,
            "type": "HOST_DEVICE",
            "host_device": ""
        },
        "allow_guest_control": true,
        "label": "Floppy drive 1",
        "state": "NOT_CONNECTED"
    },
    "id": "8000",
    "changed": true
}
```

## [Attach a new disk](vm_hardware_tuning.md#id32)

Here we attach a tiny disk to the VM. The `capacity` is in bytes.

```YAML+Jinja
- name: Create a new disk
  vmware.vmware_rest.vcenter_vm_hardware_disk:
    vm: '{{ test_vm1_info.id }}'
    type: SATA
    new_vmdk:
      capacity: 320000
  register: my_new_disk
```

### [Result](vm_hardware_tuning.md#id33)

```YAML+Jinja
{
    "value": {
        "backing": {
            "vmdk_file": "[local] test_vm1_8/test_vm1_1.vmdk",
            "type": "VMDK_FILE"
        },
        "label": "Hard disk 2",
        "type": "SATA",
        "sata": {
            "bus": 0,
            "unit": 0
        },
        "capacity": 320000
    },
    "id": "16000",
    "changed": true
}
```
