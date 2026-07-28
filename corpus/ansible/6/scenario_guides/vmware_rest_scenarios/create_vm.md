---
collection: ansible
version: "6"
title: "How to create a Virtual Machine"
source_url: https://docs.ansible.com/projects/ansible/6/scenario_guides/vmware_rest_scenarios/create_vm.html
fetched_at: 2026-07-27T16:43:18+00:00
---
# How to create a Virtual Machine

- [Introduction](create_vm.md#introduction)
- [Scenario requirements](create_vm.md#scenario-requirements)
- [How to create a virtual machine](create_vm.md#id1)

  - [Result](create_vm.md#result)

## [Introduction](create_vm.md#id2)

This section shows you how to use Ansible to create a virtual machine.

## [Scenario requirements](create_vm.md#id3)

You’ve already followed [How to collect information about your environment](collect_information.md#vmware-rest-collect-info) and you’ve got the following variables defined:

- `my_cluster_info`
- `my_datastore`
- `my_virtual_machine_folder`
- `my_cluster_info`

## [How to create a virtual machine](create_vm.md#id4)

In this example, we will use the `vcenter_vm` module to create a new guest.

```YAML+Jinja
- name: Create a VM
  vmware.vmware_rest.vcenter_vm:
    placement:
      cluster: "{{ my_cluster_info.id }}"
      datastore: "{{ my_datastore.datastore }}"
      folder: "{{ my_virtual_machine_folder.folder }}"
      resource_pool: "{{ my_cluster_info.value.resource_pool }}"
    name: test_vm1
    guest_OS: DEBIAN_8_64
    hardware_version: VMX_11
    memory:
      hot_add_enabled: true
      size_MiB: 1024
  register: _result
```

### [Result](create_vm.md#id5)

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
    "changed": true
}
```

> **Note:**
>
> `vcenter_vm` accepts more parameters, however you may prefer to start with a simple VM and use the `vcenter_vm_hardware` modules to tune it up afterwards. It’s easier this way to identify a potential problematical step.
