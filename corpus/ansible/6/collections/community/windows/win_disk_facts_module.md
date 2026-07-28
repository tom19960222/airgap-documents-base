---
collection: ansible
version: "6"
title: "community.windows.win_disk_facts module – Show the attached disks and disk information of the target host"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_disk_facts_module.html
fetched_at: 2026-07-27T17:23:15+00:00
---
# community.windows.win_disk_facts module – Show the attached disks and disk information of the target host

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/community/windows) (version 1.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
> You need further requirements to be able to use this module,
> see [Requirements](win_disk_facts_module.md#ansible-collections-community-windows-win-disk-facts-module-requirements) for details.
>
> To use it in a playbook, specify: `community.windows.win_disk_facts`.

- [Synopsis](win_disk_facts_module.md#synopsis)
- [Requirements](win_disk_facts_module.md#requirements)
- [Parameters](win_disk_facts_module.md#parameters)
- [Notes](win_disk_facts_module.md#notes)
- [Examples](win_disk_facts_module.md#examples)
- [Returned Facts](win_disk_facts_module.md#returned-facts)

## [Synopsis](win_disk_facts_module.md#id1)

- With the module you can retrieve and output detailed information about the attached disks of the target and its volumes and partitions if existent.

## [Requirements](win_disk_facts_module.md#id2)

The below requirements are needed on the host that executes this module.

- Windows 8.1 / Windows 2012 (NT 6.2)

## [Parameters](win_disk_facts_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **filter**  list / elements=string  added in community.windows 1.9.0 | Allows to filter returned facts by type of disk information.  If volumes are selected partitions will be returned as well.  Choices:   - `"physical_disk"` ← (default) - `"virtual_disk"` ← (default) - `"win32_disk_drive"` ← (default) - `"partitions"` ← (default) - `"volumes"` ← (default)   Default: `["physical_disk", "virtual_disk", "win32_disk_drive", "partitions", "volumes"]` |

## [Notes](win_disk_facts_module.md#id4)

> **Note:**
>
> - In order to understand all the returned properties and values please visit the following site and open the respective MSFT class <https://msdn.microsoft.com/en-us/library/windows/desktop/hh830612.aspx>

## [Examples](win_disk_facts_module.md#id5)

```yaml+jinja
- name: Get disk facts
  community.windows.win_disk_facts:

- name: Output first disk size
  debug:
    var: ansible_facts.disks[0].size

- name: Convert first system disk into various formats
  debug:
    msg: '{{ disksize_gib }} vs {{ disksize_gib_human }}'
  vars:
    # Get first system disk
    disk: '{{ ansible_facts.disks|selectattr("system_disk")|first }}'

    # Show disk size in Gibibytes
    disksize_gib_human: '{{ disk.size|filesizeformat(true) }}'   # returns "223.6 GiB" (human readable)
    disksize_gib: '{{ (disk.size/1024|pow(3))|round|int }} GiB'  # returns "224 GiB" (value in GiB)

    # Show disk size in Gigabytes
    disksize_gb_human: '{{ disk.size|filesizeformat }}'        # returns "240.1 GB" (human readable)
    disksize_gb: '{{ (disk.size/1000|pow(3))|round|int }} GB'  # returns "240 GB" (value in GB)

- name: Output second disk serial number
  debug:
    var: ansible_facts.disks[1].serial_number

- name: get disk physical_disk and partition facts on the target
  win_disk_facts:
    filter:
      - physical_disk
      - partitions
```

## [Returned Facts](win_disk_facts_module.md#id6)

Facts returned by this module are added/updated in the `hostvars` host facts and can be referenced by name just like any other host fact. They do not need to be registered in order to use them.

| Key | Description |
| --- | --- |
| **ansible_disks**  list / elements=string | Detailed information about one particular disk.  Returned: if disks were found |
| **bootable**  boolean | Information whether the particular disk is a bootable disk.  Returned: always  Sample: `false` |
| **bus_type**  string | Bus type of the particular disk.  Returned: always  Sample: `"SCSI"` |
| **clustered**  boolean | Information whether the particular disk is clustered (part of a failover cluster).  Returned: always  Sample: `false` |
| **firmware_version**  string | Firmware version of the particular disk.  Returned: always  Sample: `"0001"` |
| **friendly_name**  string | Friendly name of the particular disk.  Returned: always  Sample: `"Red Hat VirtIO SCSI Disk Device"` |
| **guid**  string | GUID of the particular disk on the target.  Returned: if existent  Sample: `"{efa5f928-57b9-47fc-ae3e-902e85fbe77f}"` |
| **location**  string | Location of the particular disk on the target.  Returned: always  Sample: `"PCIROOT(0)#PCI(0400)#SCSI(P00T00L00)"` |
| **manufacturer**  string | Manufacturer of the particular disk.  Returned: always  Sample: `"Red Hat"` |
| **model**  string | Model specification of the particular disk.  Returned: always  Sample: `"VirtIO"` |
| **number**  integer | Disk number of the particular disk.  Returned: always  Sample: `0` |
| **operational_status**  string | Operational status of the particular disk.  Returned: always  Sample: `"Online"` |
| **partition_count**  integer | Number of partitions on the particular disk.  Returned: always  Sample: `4` |
| **partition_style**  string | Partition style of the particular disk.  Returned: always  Sample: `"MBR"` |
| **partitions**  list / elements=string | Detailed information about one particular partition on the specified disk.  Returned: if existent |
| **access_paths**  string | Access paths of the particular partition.  Returned: if existent  Sample: `"\\\\?\\Volume{85bdc4a8-f8eb-11e6-80fa-806e6f6e6963}\\"` |
| **active**  boolean | Information whether the particular partition is an active partition or not.  Returned: if partition_style property of the particular disk has value “MBR”  Sample: `true` |
| **drive_letter**  string | Drive letter of the particular partition.  Returned: if existent  Sample: `"C"` |
| **gpt_type**  string | gpt type of the particular partition.  Returned: if partition_style property of the particular disk has value “GPT”  Sample: `"{e3c9e316-0b5c-4db8-817d-f92df00215ae}"` |
| **guid**  string | GUID of the particular partition.  Returned: if existent  Sample: `"{302e475c-6e64-4674-a8e2-2f1c7018bf97}"` |
| **hidden**  boolean | Information whether the particular partition is hidden or not.  Returned: always  Sample: `true` |
| **mbr_type**  integer | mbr type of the particular partition.  Returned: if partition_style property of the particular disk has value “MBR”  Sample: `7` |
| **no_default_driveletter**  boolean | Information whether the particular partition has a default drive letter or not.  Returned: if partition_style property of the particular disk has value “GPT”  Sample: `true` |
| **number**  integer | Number of the particular partition.  Returned: always  Sample: `1` |
| **offset**  integer | Offset of the particular partition.  Returned: always  Sample: `368050176` |
| **shadow_copy**  boolean | Information whether the particular partition is a shadow copy of another partition.  Returned: always  Sample: `false` |
| **size**  integer | Size in bytes of the particular partition.  Returned: always  Sample: `838860800` |
| **transition_state**  integer | Transition state of the particular partition.  Returned: always  Sample: `1` |
| **type**  string | Type of the particular partition.  Returned: always  Sample: `"IFS"` |
| **volumes**  list / elements=string | Detailed information about one particular volume on the specified partition.  Returned: if existent |
| **allocation_unit_size**  integer | Allocation unit size in bytes of the particular volume.  Returned: always  Sample: `4096` |
| **drive_type**  string | Drive type of the particular volume.  Returned: always  Sample: `"Fixed"` |
| **health_status**  string | Health status of the particular volume.  Returned: always  Sample: `"Healthy"` |
| **label**  string | File system label of the particular volume.  Returned: always  Sample: `"System Reserved"` |
| **object_id**  string | Object ID of the particular volume.  Returned: always  Sample: `"\\\\?\\Volume{85bdc4a9-f8eb-11e6-80fa-806e6f6e6963}\\"` |
| **path**  string | Path of the particular volume.  Returned: always  Sample: `"\\\\?\\Volume{85bdc4a9-f8eb-11e6-80fa-806e6f6e6963}\\"` |
| **size**  integer | Size in bytes of the particular volume.  Returned: always  Sample: `838856704` |
| **size_remaining**  integer | Remaining size in bytes of the particular volume.  Returned: always  Sample: `395620352` |
| **type**  string | File system type of the particular volume.  Returned: always  Sample: `"NTFS"` |
| **path**  string | Path of the particular disk on the target.  Returned: always  Sample: `"\\\\?\\scsi#disk&ven_red_hat&prod_virtio#4&23208fd0&1&000000#{<id>}"` |
| **physical_disk**  complex | Detailed information about physical disk properties of the particular disk.  Returned: if existent |
| **allocated_size**  integer | Allocated size in bytes of the particular physical disk.  Returned: always  Sample: `240057409536` |
| **bus_type**  string | Bus type of the particular physical disk.  Returned: always  Sample: `"SCSI"` |
| **can_pool**  boolean | Information whether the particular physical disk can be added to a storage pool.  Returned: always  Sample: `false` |
| **cannot_pool_reason**  string | Information why the particular physical disk can not be added to a storage pool.  Returned: if can_pool property has value false  Sample: `"Insufficient Capacity"` |
| **device_id**  string | Device ID of the particular physical disk.  Returned: always  Sample: `"0"` |
| **friendly_name**  string | Friendly name of the particular physical disk.  Returned: always  Sample: `"PhysicalDisk0"` |
| **health_status**  string | Health status of the particular physical disk.  Returned: always  Sample: `"Healthy"` |
| **indication_enabled**  boolean | Information whether indication is enabled for the particular physical disk.  Returned: always  Sample: `true` |
| **manufacturer**  string | Manufacturer of the particular physical disk.  Returned: always  Sample: `"SUSE"` |
| **media_type**  string | Media type of the particular physical disk.  Returned: always  Sample: `"UnSpecified"` |
| **model**  string | Model of the particular physical disk.  Returned: always  Sample: `"Xen Block"` |
| **object_id**  string | Object ID of the particular physical disk.  Returned: always  Sample: `"{1}\\\\\\\\HOST\\\\root/Microsoft/Windows/Storage/Providers_v2\\\\SPACES_PhysicalDisk.ObjectId=\\\"{<object_id>}:PD:{<pd>}\\\""` |
| **operational_status**  string | Operational status of the particular physical disk.  Returned: always  Sample: `"OK"` |
| **partial**  boolean | Information whether the particular physical disk is partial.  Returned: always  Sample: `false` |
| **physical_location**  string | Physical location of the particular physical disk.  Returned: always  Sample: `"Integrated : Adapter 3 : Port 0 : Target 0 : LUN 0"` |
| **serial_number**  string | Serial number of the particular physical disk.  Returned: always  Sample: `"b62beac80c3645e5877f"` |
| **size**  integer | Size in bytes of the particular physical disk.  Returned: always  Sample: `240057409536` |
| **spindle_speed**  integer | Spindle speed in rpm of the particular physical disk.  Returned: always  Sample: `4294967295` |
| **supported_usages**  complex | Supported usage types of the particular physical disk.  Returned: always |
| **Count**  integer | Count of supported usage types.  Returned: always  Sample: `5` |
| **value**  string | List of supported usage types.  Returned: always  Sample: `"Auto-Select, Hot Spare"` |
| **unique_id**  string | Unique ID of the particular physical disk.  Returned: always  Sample: `"3141463431303031"` |
| **usage_type**  string | Usage type of the particular physical disk.  Returned: always  Sample: `"Auto-Select"` |
| **read_only**  boolean | Read only status of the particular disk.  Returned: always  Sample: `true` |
| **sector_size**  integer | Sector size in bytes of the particular disk.  Returned: always  Sample: `4096` |
| **serial_number**  string | Serial number of the particular disk on the target.  Returned: always  Sample: `"b62beac80c3645e5877f"` |
| **size**  integer | Size in bytes of the particular disk.  Returned: always  Sample: `227727638528` |
| **system_disk**  boolean | Information whether the particular disk is a system disk.  Returned: always  Sample: `true` |
| **unique_id**  string | Unique ID of the particular disk on the target.  Returned: always  Sample: `"3141463431303031"` |
| **virtual_disk**  complex | Detailed information about virtual disk properties of the particular disk.  Returned: if existent |
| **access**  string | Access of the particular virtual disk.  Returned: always  Sample: `"Read/Write"` |
| **allocated_size**  integer | Allocated size in bytes of the particular virtual disk.  Returned: always  Sample: `240057409536` |
| **allocation_unit_size**  integer | Allocation unit size in bytes of the particular virtual disk.  Returned: always  Sample: `4096` |
| **available_copies**  integer | Number of the available copies of the particular virtual disk.  Returned: if existent  Sample: `1` |
| **columns**  integer | Number of the columns of the particular virtual disk.  Returned: always  Sample: `2` |
| **deduplication_enabled**  boolean | Information whether deduplication is enabled for the particular virtual disk.  Returned: always  Sample: `true` |
| **detached_reason**  string | Detached reason of the particular virtual disk.  Returned: always  Sample: `"None"` |
| **enclosure_aware**  boolean | Information whether the particular virtual disk is enclosure aware.  Returned: always  Sample: `false` |
| **fault_domain_awareness**  string | Fault domain awareness of the particular virtual disk.  Returned: always  Sample: `"PhysicalDisk"` |
| **footprint_on_pool**  integer | Footprint on pool in bytes of the particular virtual disk.  Returned: always  Sample: `240057409536` |
| **friendly_name**  string | Friendly name of the particular virtual disk.  Returned: always  Sample: `"Prod2 Virtual Disk"` |
| **groups**  integer | Number of the groups of the particular virtual disk.  Returned: always  Sample: `1` |
| **health_status**  string | Health status of the particular virtual disk.  Returned: always  Sample: `"Healthy"` |
| **inter_leave**  integer | Inter leave in bytes of the particular virtual disk.  Returned: always  Sample: `102400` |
| **logical_sector_size**  integer | Logical sector size in byte of the particular virtual disk.  Returned: always  Sample: `512` |
| **manual_attach**  boolean | Information whether the particular virtual disk is manual attached.  Returned: always  Sample: `true` |
| **media_type**  string | Media type of the particular virtual disk.  Returned: always  Sample: `"Unspecified"` |
| **name**  string | Name of the particular virtual disk.  Returned: always  Sample: `"vDisk1"` |
| **object_id**  string | Object ID of the particular virtual disk.  Returned: always  Sample: `"{1}\\\\\\\\HOST\\\\root/Microsoft/Windows/Storage/Providers_v2\\\\SPACES_VirtualDisk.ObjectId=\\\"{<object_id>}:VD:{<vd>}\\\""` |
| **operational_status**  string | Operational status of the particular virtual disk.  Returned: always  Sample: `"OK"` |
| **parity_layout**  integer | Parity layout of the particular virtual disk.  Returned: if existent  Sample: `1` |
| **physical_disk_redundancy**  integer | Type of the physical disk redundancy of the particular virtual disk.  Returned: always  Sample: `1` |
| **physical_sector_size**  integer | Physical sector size in bytes of the particular virtual disk.  Returned: always  Sample: `4096` |
| **provisioning_type**  string | Provisioning type of the particular virtual disk.  Returned: always  Sample: `"Thin"` |
| **read_cache_size**  integer | Read cache size in byte of the particular virtual disk.  Returned: always  Sample: `0` |
| **request_no_spof**  boolean | Information whether the particular virtual disk requests no single point of failure.  Returned: always  Sample: `true` |
| **resiliency_setting_name**  integer | Type of the physical disk redundancy of the particular virtual disk.  Returned: always  Sample: `1` |
| **size**  integer | Size in bytes of the particular virtual disk.  Returned: always  Sample: `240057409536` |
| **snapshot**  boolean | Information whether the particular virtual disk is a snapshot.  Returned: always  Sample: `false` |
| **tiered**  boolean | Information whether the particular virtual disk is tiered.  Returned: always  Sample: `true` |
| **unique_id**  string | Unique ID of the particular virtual disk.  Returned: always  Sample: `"260542E4C6B01D47A8FA7630FD90FFDE"` |
| **unique_id_format**  string | Unique ID format of the particular virtual disk.  Returned: always  Sample: `"Vendor Specific"` |
| **write_cache_size**  integer | Write cache size in byte of the particular virtual disk.  Returned: always  Sample: `100` |
| **win32_disk_drive**  complex | Representation of the Win32_DiskDrive class.  Returned: if existent |
| **availability**  integer | Availability and status of the device.  Returned: always |
| **bytes_per_sector**  integer | Number of bytes in each sector for the physical disk drive.  Returned: always  Sample: `512` |
| **capabilities**  list / elements=string | Array of capabilities of the media access device.  For example, the device may support random access (3), removable media (7), and automatic cleaning (9).  Returned: always  Sample: `[3, 4]` |
| **capability_descriptions**  list / elements=string | List of more detailed explanations for any of the access device features indicated in the Capabilities array.  Note, each entry of this array is related to the entry in the Capabilities array that is located at the same index.  Returned: always  Sample: `["Random Access", "Supports Writing"]` |
| **caption**  string | Short description of the object.  Returned: always  Sample: `"VMware Virtual disk SCSI Disk Device"` |
| **compression_method**  string | Algorithm or tool used by the device to support compression.  Returned: always  Sample: `"Compressed"` |
| **config_manager_error_code**  integer | Windows Configuration Manager error code.  Returned: always  Sample: `0` |
| **config_manager_user_config**  boolean | If True, the device is using a user-defined configuration.  Returned: always  Sample: `true` |
| **creation_class_name**  string | Name of the first concrete class to appear in the inheritance chain used in the creation of an instance.  When used with the other key properties of the class, the property allows all instances of this class  and its subclasses to be uniquely identified.  Returned: always  Sample: `"Win32_DiskDrive"` |
| **default_block_size**  integer | Default block size, in bytes, for this device.  Returned: always  Sample: `512` |
| **description**  string | Description of the object.  Returned: always  Sample: `"Disk drive"` |
| **device_id**  string | Unique identifier of the disk drive with other devices on the system.  Returned: always  Sample: `"\\\\.\\PHYSICALDRIVE0"` |
| **error_cleared**  boolean | If True, the error reported in LastErrorCode is now cleared.  Returned: always  Sample: `true` |
| **error_description**  string | More information about the error recorded in LastErrorCode,  and information on any corrective actions that may be taken.  Returned: always |
| **error_methodology**  string | Type of error detection and correction supported by this device.  Returned: always |
| **firmware_revision**  string | Revision for the disk drive firmware that is assigned by the manufacturer.  Returned: always  Sample: `"1.0"` |
| **index**  integer | Physical drive number of the given drive.  This property is filled by the STORAGE_DEVICE_NUMBER structure returned from the IOCTL_STORAGE_GET_DEVICE_NUMBER control code  A value of 0xffffffff indicates that the given drive does not map to a physical drive.  Returned: always  Sample: `0` |
| **install_date**  string | Date and time the object was installed. This property does not need a value to indicate that the object is installed.  Returned: always |
| **interface_type**  string | Interface type of physical disk drive.  Returned: always  Sample: `"SCSI"` |
| **last_error_code**  integer | Last error code reported by the logical device.  Returned: always |
| **manufacturer**  string | Name of the disk drive manufacturer.  Returned: always  Sample: `"Seagate"` |
| **max_block_size**  integer | Maximum block size, in bytes, for media accessed by this device.  Returned: always |
| **max_media_size**  integer | Maximum media size, in kilobytes, of media supported by this device.  Returned: always |
| **media_loaded**  boolean | If True, the media for a disk drive is loaded, which means that the device has a readable file system and is accessible.  For fixed disk drives, this property will always be TRUE.  Returned: always  Sample: `true` |
| **media_type**  string | Type of media used or accessed by this device.  Returned: always  Sample: `"Fixed hard disk media"` |
| **min_block_size**  integer | Minimum block size, in bytes, for media accessed by this device.  Returned: always |
| **model**  string | Manufacturer’s model number of the disk drive.  Returned: always  Sample: `"ST32171W"` |
| **name**  string | Label by which the object is known. When subclassed, the property can be overridden to be a key property.  Returned: always  Sample: `"\\\\\\\\.\\\\PHYSICALDRIVE0"` |
| **needs_cleaning**  boolean | If True, the media access device needs cleaning.  Whether manual or automatic cleaning is possible is indicated in the Capabilities property.  Returned: always |
| **number_of_media_supported**  integer | Maximum number of media which can be supported or inserted  (when the media access device supports multiple individual media).  Returned: always |
| **partitions**  integer | Number of partitions on this physical disk drive that are recognized by the operating system.  Returned: always  Sample: `3` |
| **pnp_device_id**  string | Windows Plug and Play device identifier of the logical device.  Returned: always  Sample: `"SCSI\\DISK&VEN_VMWARE&PROD_VIRTUAL_DISK\\5&1982005&0&000000"` |
| **power_management_capabilities**  list / elements=string | Array of the specific power-related capabilities of a logical device.  Returned: always |
| **power_management_supported**  boolean | If True, the device can be power-managed (can be put into suspend mode, and so on).  The property does not indicate that power management features are currently enabled,  only that the logical device is capable of power management.  Returned: always |
| **scsi_bus**  integer | SCSI bus number of the disk drive.  Returned: always  Sample: `0` |
| **scsi_logical_unit**  integer | SCSI logical unit number (LUN) of the disk drive.  Returned: always  Sample: `0` |
| **scsi_port**  integer | SCSI port number of the disk drive.  Returned: always  Sample: `0` |
| **scsi_target_id**  integer | SCSI identifier number of the disk drive.  Returned: always  Sample: `0` |
| **sectors_per_track**  integer | Number of sectors in each track for this physical disk drive.  Returned: always  Sample: `63` |
| **serial_number**  string | Number allocated by the manufacturer to identify the physical media.  Returned: always  Sample: `"6000c298f34101b38cb2b2508926b9de"` |
| **signature**  integer | Disk identification. This property can be used to identify a shared resource.  Returned: always |
| **size**  integer | Size of the disk drive. It is calculated by multiplying the total number of cylinders, tracks in each cylinder,  sectors in each track, and bytes in each sector.  Returned: always  Sample: `53686402560` |
| **status**  string | Current status of the object. Various operational and nonoperational statuses can be defined.  Operational statuses include: “OK”, “Degraded”, and “Pred Fail”  (an element, such as a SMART-enabled hard disk drive, may be functioning properly but predicting a failure in the near future).  Nonoperational statuses include: “Error”, “Starting”, “Stopping”, and “Service”.  “Service”, could apply during mirror-resilvering of a disk, reload of a user permissions list, or other administrative work.  Not all such work is online, yet the managed element is neither “OK” nor in one of the other states.  Returned: always  Sample: `"OK"` |
| **status_info**  integer | State of the logical device. If this property does not apply to the logical device, the value 5 (Not Applicable) should be used.  Returned: always |
| **system_creation_class_name**  string | Value of the scoping computer’s CreationClassName property.  Returned: always  Sample: `"Win32_ComputerSystem"` |
| **system_name**  string | Name of the scoping system.  Returned: always  Sample: `"WILMAR-TEST-123"` |
| **total_cylinders**  integer | Total number of cylinders on the physical disk drive.  Note: the value for this property is obtained through extended functions of BIOS interrupt 13h.  The value may be inaccurate if the drive uses a translation scheme to support high-capacity disk sizes.  Consult the manufacturer for accurate drive specifications.  Returned: always  Sample: `6527` |
| **total_heads**  integer | Total number of heads on the disk drive.  Note: the value for this property is obtained through extended functions of BIOS interrupt 13h.  The value may be inaccurate if the drive uses a translation scheme to support high-capacity disk sizes.  Consult the manufacturer for accurate drive specifications.  Returned: always  Sample: `255` |
| **total_sectors**  integer | Total number of sectors on the physical disk drive.  Note: the value for this property is obtained through extended functions of BIOS interrupt 13h.  The value may be inaccurate if the drive uses a translation scheme to support high-capacity disk sizes.  Consult the manufacturer for accurate drive specifications.  Returned: always  Sample: `104856255` |
| **total_tracks**  integer | Total number of tracks on the physical disk drive.  Note: the value for this property is obtained through extended functions of BIOS interrupt 13h.  The value may be inaccurate if the drive uses a translation scheme to support high-capacity disk sizes.  Consult the manufacturer for accurate drive specifications.  Returned: always  Sample: `1664385` |
| **tracks_per_cylinder**  integer | Number of tracks in each cylinder on the physical disk drive.  Note: the value for this property is obtained through extended functions of BIOS interrupt 13h.  The value may be inaccurate if the drive uses a translation scheme to support high-capacity disk sizes.  Consult the manufacturer for accurate drive specifications.  Returned: always  Sample: `255` |

### Authors

- Marc Tschapek (@marqelme)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
