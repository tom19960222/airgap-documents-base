---
collection: ansible
version: "8"
title: "community.vmware.vmware_guest_disk module – Manage disks related to virtual machine in given vCenter infrastructure"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_guest_disk_module.html
fetched_at: 2026-07-28T02:00:11+00:00
---
# community.vmware.vmware_guest_disk module – Manage disks related to virtual machine in given vCenter infrastructure

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
> To use it in a playbook, specify: `community.vmware.vmware_guest_disk`.

- [Synopsis](vmware_guest_disk_module.md#synopsis)
- [Parameters](vmware_guest_disk_module.md#parameters)
- [Notes](vmware_guest_disk_module.md#notes)
- [Examples](vmware_guest_disk_module.md#examples)
- [Return Values](vmware_guest_disk_module.md#return-values)

## [Synopsis](vmware_guest_disk_module.md#id1)

- This module can be used to add, remove and update disks belonging to given virtual machine.
- All parameters and VMware object names are case sensitive.
- This module is destructive in nature, please read documentation carefully before proceeding.
- Be careful while removing disk specified as this may lead to data loss.

## [Parameters](vmware_guest_disk_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **datacenter**  string / required | The datacenter name to which virtual machine belongs to. |
| **disk**  list / elements=dictionary | A list of disks to add or remove.  The virtual disk related information is provided using this list.  All values and parameters are case sensitive.  **Default:** `[]` |
| **autoselect_datastore**  boolean | Select the less used datastore. Specify only if `datastore` is not specified.  Not applicable when disk `type` is set to `vpmemdisk`.  **Choices:**   - `false` - `true` |
| **bus_sharing**  string | Only functions with Paravirtual SCSI Controller.  Allows for the sharing of the scsi bus between two virtual machines.  **Choices:**   - `"noSharing"` ← (default) - `"physicalSharing"` - `"virtualSharing"` |
| **cluster_disk**  boolean | This value allows for the sharing of an RDM between two machines.  The primary machine holding the RDM uses the default `false`.  The secondary machine holding the RDM uses `true`.  **Choices:**   - `false` ← (default) - `true` |
| **compatibility_mode**  string | Compatibility mode for raw devices. Required when disk type `type` is set to `rdm`.  **Choices:**   - `"physicalMode"` - `"virtualMode"` |
| **controller_number**  integer | This parameter is used with `controller_type` for specifying controller bus number.  For `ide` controller type, valid value is 0 or 1.  **Choices:**   - `0` - `1` - `2` - `3` |
| **controller_type**  string | This parameter is added for managing disks attaching other types of controllers, e.g., SATA or NVMe.  If either `controller_type` or `scsi_type` is not specified, then use `paravirtual` type.  **Choices:**   - `"buslogic"` - `"lsilogic"` - `"lsilogicsas"` - `"paravirtual"` - `"sata"` - `"nvme"` - `"ide"` |
| **datastore**  string | Name of datastore or datastore cluster to be used for the disk.  Not applicable when disk `type` is set to `vpmemdisk`. |
| **destroy**  boolean | If `state` is `absent`, make sure the disk file is deleted from the datastore. Added in version 2.10.  **Choices:**   - `false` - `true` ← (default) |
| **disk_mode**  string | Type of disk mode. If not specified then use `persistent` mode for new disk.  If set to ‘persistent’ mode, changes are immediately and permanently written to the virtual disk.  If set to ‘independent_persistent’ mode, same as persistent, but not affected by snapshots.  If set to ‘independent_nonpersistent’ mode, changes to virtual disk are made to a redo log and discarded at power off, but not affected by snapshots.  Not applicable when disk `type` is set to `vpmemdisk`.  **Choices:**   - `"persistent"` - `"independent_persistent"` - `"independent_nonpersistent"` |
| **filename**  string | Existing disk image to be used. Filename must already exist on the datastore.  Specify filename string in `[datastore_name] path/to/file.vmdk` format. Added in version 2.10.  Not applicable when disk `type` is set to `vpmemdisk`. |
| **iolimit**  dictionary | Section specifies the shares and limit for storage I/O resource.  Not applicable when disk `type` is set to `vpmemdisk`. |
| **limit**  integer | Section specifies values for limit where the utilization of a virtual machine will not exceed, even if there are available resources. |
| **shares**  dictionary | Specifies different types of shares user can add for the given disk. |
| **level**  string | Specifies different level for the shares section.  **Choices:**   - `"low"` - `"normal"` - `"high"` - `"custom"` |
| **level_value**  integer | Custom value when `level` is set as `custom`. |
| **rdm_path**  string | Path of LUN for Raw Device Mapping required for disk type `rdm`.  Only valid if `type` is set to `rdm`. |
| **scsi_controller**  integer | SCSI controller number. Only 4 SCSI controllers are allowed per VM.  Care should be taken while specifying ‘scsi_controller’ is 0 and ‘unit_number’ as 0 as this disk may contain OS.  **Choices:**   - `0` - `1` - `2` - `3` |
| **scsi_type**  string | Type of SCSI controller. This value is required only for the first occurrence of SCSI Controller.  This value is ignored, if SCSI Controller is already present or `state` is `absent`.  **Choices:**   - `"buslogic"` - `"lsilogic"` - `"lsilogicsas"` - `"paravirtual"` |
| **shares**  dictionary | Section for iolimit section tells about what are all different types of shares user can add for disk.  Not applicable when disk `type` is set to `vpmemdisk`. |
| **level**  string | Tells about different level for the shares section.  **Choices:**   - `"low"` - `"normal"` - `"high"` - `"custom"` |
| **level_value**  integer | Custom value when `level` is set as `custom`. |
| **sharing**  boolean | The sharing mode of the virtual disk.  Setting sharing means that multiple virtual machines can write to the virtual disk.  Sharing can only be set if `type` is set to `eagerzeroedthick` or `rdm`.  **Choices:**   - `false` ← (default) - `true` |
| **size**  string | Disk storage size.  If size specified then unit must be specified. There is no space allowed in between size number and unit.  Only first occurrence in disk element will be considered, even if there are multiple size\* parameters available. |
| **size_gb**  integer | Disk storage size in gb. |
| **size_kb**  integer | Disk storage size in kb. |
| **size_mb**  integer | Disk storage size in mb. |
| **size_tb**  integer | Disk storage size in tb. |
| **state**  string | State of disk.  If set to ‘absent’, disk will be removed permanently from virtual machine configuration and from VMware storage.  If set to ‘present’, disk will be added if not present at given Controller and Unit Number.  or disk exists with different size, disk size is increased, reducing disk size is not allowed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **type**  string | The type of disk, if not specified then use `thick` type for new disk, no eagerzero.  The disk type `rdm` is added in version 1.13.0.  The disk type `vpmemdisk` is added in version 2.7.0.  **Choices:**   - `"thin"` - `"eagerzeroedthick"` - `"thick"` - `"rdm"` - `"vpmemdisk"` |
| **unit_number**  integer / required | Disk Unit Number.  Valid value range from 0 to 15, except 7 for SCSI Controller.  Valid value range from 0 to 64, except 7 for Paravirtual SCSI Controller on Virtual Hardware version 14 or higher.  Valid value range from 0 to 29 for SATA controller.  Valid value range from 0 to 14 for NVME controller.  Valid value range from 0 to 1 for IDE controller. |
| **folder**  string | Destination folder, absolute or relative path to find an existing guest.  This is a required parameter, only if multiple VMs are found with same name.  The folder should include the datacenter. ESX’s datacenter is ha-datacenter  Examples:  folder: /ha-datacenter/vm  folder: ha-datacenter/vm  folder: /datacenter1/vm  folder: datacenter1/vm  folder: /datacenter1/vm/folder1  folder: datacenter1/vm/folder1  folder: /folder1/datacenter1/vm  folder: folder1/datacenter1/vm  folder: /folder1/datacenter1/vm/folder2 |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **moid**  string | Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.  This is required if `name` or `uuid` is not supplied. |
| **name**  string | Name of the virtual machine.  This is a required parameter, if parameter `uuid` or `moid` is not supplied. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **use_instance_uuid**  boolean | Whether to use the VMware instance UUID rather than the BIOS UUID.  **Choices:**   - `false` ← (default) - `true` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **uuid**  string | UUID of the instance to gather facts if known, this is VMware’s unique identifier.  This is a required parameter, if parameter `name` or `moid` is not supplied. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_guest_disk_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_guest_disk_module.md#id4)

```yaml+jinja
- name: Add disks to virtual machine using UUID
  community.vmware.vmware_guest_disk:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    uuid: 421e4592-c069-924d-ce20-7e7533fab926
    disk:
      - size_mb: 10
        type: thin
        datastore: datacluster0
        state: present
        scsi_controller: 1
        unit_number: 1
        scsi_type: 'paravirtual'
        disk_mode: 'persistent'
      - size_gb: 10
        type: eagerzeroedthick
        state: present
        autoselect_datastore: true
        scsi_controller: 2
        scsi_type: 'buslogic'
        unit_number: 12
        disk_mode: 'independent_persistent'
      - size: 10Gb
        type: eagerzeroedthick
        state: present
        autoselect_datastore: true
        scsi_controller: 2
        scsi_type: 'buslogic'
        unit_number: 1
        disk_mode: 'independent_nonpersistent'
      - filename: "[datastore1] path/to/existing/disk.vmdk"
  delegate_to: localhost
  register: disk_facts

- name: Add disks with specified shares to the virtual machine
  community.vmware.vmware_guest_disk:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    disk:
      - size_gb: 1
        type: thin
        datastore: datacluster0
        state: present
        scsi_controller: 1
        unit_number: 1
        disk_mode: 'independent_persistent'
        shares:
          level: custom
          level_value: 1300
  delegate_to: localhost
  register: test_custom_shares

- name: Add physical raw device mapping to virtual machine using name
  community.vmware.vmware_guest_disk:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    validate_certs: false
    name: "Test_VM"
    disk:
      - type: rdm
        state: present
        scsi_controller: 1
        unit_number: 5
        rdm_path: /vmfs/devices/disks/naa.060000003b1234efb453
        compatibility_mode: 'physicalMode'

- name: Add virtual raw device mapping to virtual machine using name and virtual mode
  community.vmware.vmware_guest_disk:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    validate_certs: false
    name: "Test_VM"
    disk:
      - type: rdm
        state: present
        scsi_controller: 1
        unit_number: 5
        rdm_path: /vmfs/devices/disks/naa.060000003b1234efb453
        compatibility_mode: 'virtualMode'
        disk_mode: 'persistent'

- name: Add raw device mapping to virtual machine with Physical bus sharing
  community.vmware.vmware_guest_disk:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    validate_certs: false
    name: "Test_VM"
    disk:
      - type: rdm
        state: present
        scsi_controller: 1
        unit_number: 5
        rdm_path: /vmfs/devices/disks/naa.060000003b1234efb453
        compatibility_mode: 'virtualMode'
        disk_mode: 'persistent'
        bus_sharing: physicalSharing

- name: Add raw device mapping to virtual machine with Physical bus sharing and clustered disk
  community.vmware.vmware_guest_disk:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    validate_certs: false
    name: "Test_VM"
    disk:
      - type: rdm
        state: present
        scsi_controller: 1
        unit_number: 5
        compatibility_mode: 'virtualMode'
        disk_mode: 'persistent'
        bus_sharing: physicalSharing
        filename: "[datastore1] path/to/rdm/disk-marker.vmdk"

- name: create new disk with custom IO limits and shares in IO Limits
  community.vmware.vmware_guest_disk:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    disk:
      - size_gb: 1
        type: thin
        datastore: datacluster0
        state: present
        scsi_controller: 1
        unit_number: 1
        disk_mode: 'independent_persistent'
        iolimit:
            limit: 1506
            shares:
              level: custom
              level_value: 1305
  delegate_to: localhost
  register: test_custom_IoLimit_shares

- name: Remove disks from virtual machine using name
  community.vmware.vmware_guest_disk:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    name: VM_225
    disk:
      - state: absent
        scsi_controller: 1
        unit_number: 1
  delegate_to: localhost
  register: disk_facts

- name: Remove disk from virtual machine using moid
  community.vmware.vmware_guest_disk:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    moid: vm-42
    disk:
      - state: absent
        scsi_controller: 1
        unit_number: 1
  delegate_to: localhost
  register: disk_facts

- name: Remove disk from virtual machine but keep the VMDK file on the datastore
  community.vmware.vmware_guest_disk:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    name: VM_225
    disk:
      - state: absent
        scsi_controller: 1
        unit_number: 2
        destroy: false
  delegate_to: localhost
  register: disk_facts

- name: Add disks to virtual machine using UUID to SATA and NVMe controller
  community.vmware.vmware_guest_disk:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    validate_certs: false
    uuid: 421e4592-c069-924d-ce20-7e7533fab926
    disk:
      - size_mb: 256
        type: thin
        datastore: datacluster0
        state: present
        controller_type: sata
        controller_number: 1
        unit_number: 1
        disk_mode: 'persistent'
      - size_gb: 1
        state: present
        autoselect_datastore: true
        controller_type: nvme
        controller_number: 2
        unit_number: 3
        disk_mode: 'independent_persistent'
  delegate_to: localhost
  register: disk_facts

- name: Add a new vPMem disk to virtual machine to SATA controller
  community.vmware.vmware_guest_disk:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    validate_certs: false
    name: VM_226
    disk:
      - type: vpmemdisk
        size_gb: 1
        state: present
        controller_type: sata
        controller_number: 1
        unit_number: 2
  delegate_to: localhost
  register: disk_facts
```

## [Return Values](vmware_guest_disk_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **disk_changes**  dictionary | result of each task, key is the 0-based index with the same sequence in which the tasks were defined  **Returned:** always  **Sample:** `{"0": "Disk deleted.", "1": "Disk created."}` |
| **disk_data**  dictionary | metadata about the virtual machine’s disks after managing them  **Returned:** always  **Sample:** `{"0": {"backing_datastore": "datastore2", "backing_disk_mode": "persistent", "backing_eagerlyscrub": false, "backing_filename": "[datastore2] VM_225/VM_225.vmdk", "backing_thinprovisioned": false, "backing_uuid": "421e4592-c069-924d-ce20-7e7533fab926", "backing_writethrough": false, "capacity_in_bytes": 10485760, "capacity_in_kb": 10240, "controller_key": 1000, "key": 2000, "label": "Hard disk 1", "summary": "10,240 KB", "unit_number": 0}}` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
