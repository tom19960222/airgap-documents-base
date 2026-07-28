---
collection: ansible
version: "6"
title: "Retrieve information from a specific VM"
source_url: https://docs.ansible.com/projects/ansible/6/scenario_guides/vmware_rest_scenarios/vm_info.html
fetched_at: 2026-07-27T16:43:18+00:00
---
# Retrieve information from a specific VM

- [Introduction](vm_info.md#introduction)
- [Scenario requirements](vm_info.md#scenario-requirements)
- [How to collect virtual machine information](vm_info.md#how-to-collect-virtual-machine-information)

  - [List the VM](vm_info.md#list-the-vm)
  - [Result](vm_info.md#result)
  - [Collect the details about a specific VM](vm_info.md#collect-the-details-about-a-specific-vm)
  - [Result](vm_info.md#id1)
  - [Get the hardware version of a specific VM](vm_info.md#get-the-hardware-version-of-a-specific-vm)
  - [Result](vm_info.md#id2)
  - [List the SCSI adapter(s) of a specific VM](vm_info.md#list-the-scsi-adapter-s-of-a-specific-vm)
  - [Result](vm_info.md#id3)
  - [List the CDROM drive(s) of a specific VM](vm_info.md#list-the-cdrom-drive-s-of-a-specific-vm)
  - [Result](vm_info.md#id4)
  - [Get the memory information of the VM](vm_info.md#get-the-memory-information-of-the-vm)
  - [Result](vm_info.md#id5)

    - [Get the storage policy of the VM](vm_info.md#get-the-storage-policy-of-the-vm)
  - [Result](vm_info.md#id6)

    - [Get the disk information of the VM](vm_info.md#get-the-disk-information-of-the-vm)
  - [Result](vm_info.md#id7)

## [Introduction](vm_info.md#id8)

This section shows you how to use Ansible to retrieve information about a specific virtual machine.

## [Scenario requirements](vm_info.md#id9)

You’ve already followed [How to create a Virtual Machine](create_vm.md#vmware-rest-create-vm) and you’ve got create a new VM called `test_vm1`.

## [How to collect virtual machine information](vm_info.md#id10)

### [List the VM](vm_info.md#id11)

In this example, we use the `vcenter_vm_info` module to collect information about our new VM.

In this example, we start by asking for a list of VMs. We use a filter to limit the results to just the VM called `test_vm1`. So we are in a list context, with one single entry in the `value` key.

```YAML+Jinja
- name: Look up the VM called test_vm1 in the inventory
  register: search_result
  vmware.vmware_rest.vcenter_vm_info:
    filter_names:
    - test_vm1
```

### [Result](vm_info.md#id12)

As expected, we get a list. And thanks to our filter, we just get one entry.

```YAML+Jinja
{
    "value": [
        {
            "memory_size_MiB": 1024,
            "vm": "vm-1650",
            "name": "test_vm1",
            "power_state": "POWERED_OFF",
            "cpu_count": 1
        }
    ],
    "changed": false
}
```

### [Collect the details about a specific VM](vm_info.md#id13)

For the next steps, we pass the ID of the VM through the `vm` parameter. This allow us to collect more details about this specific VM.

```YAML+Jinja
- name: Collect information about a specific VM
  vmware.vmware_rest.vcenter_vm_info:
    vm: '{{ search_result.value[0].vm }}'
  register: test_vm1_info
```

### [Result](vm_info.md#id14)

The result is a structure with all the details about our VM. You will note this is actually the same information that we get when we created the VM.

```YAML+Jinja
{
    "value": {
        "instant_clone_frozen": false,
        "cdroms": [],
        "memory": {
            "size_MiB": 1024,
            "hot_add_enabled": true
        },
        "disks": [
            {
                "value": {
                    "scsi": {
                        "bus": 0,
                        "unit": 0
                    },
                    "backing": {
                        "vmdk_file": "[local] test_vm1_8/test_vm1.vmdk",
                        "type": "VMDK_FILE"
                    },
                    "label": "Hard disk 1",
                    "type": "SCSI",
                    "capacity": 17179869184
                },
                "key": "2000"
            }
        ],
        "parallel_ports": [],
        "sata_adapters": [],
        "cpu": {
            "hot_remove_enabled": false,
            "count": 1,
            "hot_add_enabled": false,
            "cores_per_socket": 1
        },
        "scsi_adapters": [
            {
                "value": {
                    "scsi": {
                        "bus": 0,
                        "unit": 7
                    },
                    "label": "SCSI controller 0",
                    "sharing": "NONE",
                    "type": "PVSCSI"
                },
                "key": "1000"
            }
        ],
        "power_state": "POWERED_OFF",
        "floppies": [],
        "identity": {
            "name": "test_vm1",
            "instance_uuid": "5033c296-6954-64df-faca-d001de53763d",
            "bios_uuid": "42330d17-e603-d925-fa4b-18827dbc1409"
        },
        "nvme_adapters": [],
        "name": "test_vm1",
        "nics": [],
        "boot": {
            "delay": 0,
            "retry_delay": 10000,
            "enter_setup_mode": false,
            "type": "BIOS",
            "retry": false
        },
        "serial_ports": [],
        "boot_devices": [],
        "guest_OS": "DEBIAN_8_64",
        "hardware": {
            "upgrade_policy": "NEVER",
            "upgrade_status": "NONE",
            "version": "VMX_11"
        }
    },
    "id": "vm-1650",
    "changed": false
}
```

### [Get the hardware version of a specific VM](vm_info.md#id15)

We can also use all the `vcenter_vm_*_info` modules to retrieve a smaller amount
of information. Here we use `vcenter_vm_hardware_info` to know the hardware version of
the VM.

```YAML+Jinja
- name: Collect the hardware information
  vmware.vmware_rest.vcenter_vm_hardware_info:
    vm: '{{ search_result.value[0].vm }}'
  register: my_vm1_hardware_info
```

### [Result](vm_info.md#id16)

```YAML+Jinja
{
    "value": {
        "upgrade_policy": "NEVER",
        "upgrade_status": "NONE",
        "version": "VMX_11"
    },
    "changed": false
}
```

### [List the SCSI adapter(s) of a specific VM](vm_info.md#id17)

Here for instance, we list the SCSI adapter(s) of the VM:

```YAML+Jinja
- name: List the SCSI adapter of a given VM
  vmware.vmware_rest.vcenter_vm_hardware_adapter_scsi_info:
    vm: '{{ test_vm1_info.id }}'
  register: _result
```

You can do the same for the SATA controllers with `vcenter_vm_adapter_sata_info`.

### [Result](vm_info.md#id18)

```YAML+Jinja
{
    "value": [
        {
            "scsi": {
                "bus": 0,
                "unit": 7
            },
            "label": "SCSI controller 0",
            "type": "PVSCSI",
            "sharing": "NONE"
        }
    ],
    "changed": false
}
```

### [List the CDROM drive(s) of a specific VM](vm_info.md#id19)

And we list its CDROM drives.

```YAML+Jinja
- name: List the cdrom devices on the guest
  vmware.vmware_rest.vcenter_vm_hardware_cdrom_info:
    vm: '{{ test_vm1_info.id }}'
  register: _result
```

### [Result](vm_info.md#id20)

```YAML+Jinja
{
    "value": [],
    "changed": false
}
```

### [Get the memory information of the VM](vm_info.md#id21)

Here we collect the memory information of the VM:

```YAML+Jinja
- name: Retrieve the memory information from the VM
  vmware.vmware_rest.vcenter_vm_hardware_memory_info:
    vm: '{{ test_vm1_info.id }}'
  register: _result
```

### [Result](vm_info.md#id22)

```YAML+Jinja
{
    "value": {
        "size_MiB": 1024,
        "hot_add_enabled": true
    },
    "changed": false
}
```

#### [Get the storage policy of the VM](vm_info.md#id23)

We use the `vcenter_vm_storage_policy_info` module for that:

```YAML+Jinja
- name: Get VM storage policy
  vmware.vmware_rest.vcenter_vm_storage_policy_info:
    vm: '{{ test_vm1_info.id }}'
  register: _result
```

### [Result](vm_info.md#id24)

```YAML+Jinja
{
    "value": {
        "disks": []
    },
    "changed": false
}
```

#### [Get the disk information of the VM](vm_info.md#id25)

We use the `vcenter_vm_hardware_disk_info` for this operation:

```YAML+Jinja
- name: Retrieve the disk information from the VM
  vmware.vmware_rest.vcenter_vm_hardware_disk_info:
    vm: '{{ test_vm1_info.id }}'
  register: _result
```

### [Result](vm_info.md#id26)

```YAML+Jinja
{
    "value": [
        {
            "scsi": {
                "bus": 0,
                "unit": 0
            },
            "backing": {
                "vmdk_file": "[local] test_vm1_8/test_vm1.vmdk",
                "type": "VMDK_FILE"
            },
            "label": "Hard disk 1",
            "type": "SCSI",
            "capacity": 17179869184
        }
    ],
    "changed": false
}
```
