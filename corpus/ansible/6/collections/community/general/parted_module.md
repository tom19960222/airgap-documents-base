---
collection: ansible
version: "6"
title: "community.general.parted module – Configure block device partitions"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/parted_module.html
fetched_at: 2026-07-27T17:11:49+00:00
---
# community.general.parted module – Configure block device partitions

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](parted_module.md#ansible-collections-community-general-parted-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.parted`.

- [Synopsis](parted_module.md#synopsis)
- [Requirements](parted_module.md#requirements)
- [Parameters](parted_module.md#parameters)
- [Notes](parted_module.md#notes)
- [Examples](parted_module.md#examples)
- [Return Values](parted_module.md#return-values)

## [Synopsis](parted_module.md#id1)

- This module allows configuring block device partition using the `parted` command line tool. For a full description of the fields and the options check the GNU parted manual.

## [Requirements](parted_module.md#id2)

The below requirements are needed on the host that executes this module.

- This module requires parted version 1.8.3 and above
- align option (except ‘undefined’) requires parted 2.1 and above
- If the version of parted is below 3.1, it requires a Linux version running the sysfs file system `/sys/`.

## [Parameters](parted_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **align**  string | Set alignment for newly created partitions. Use ‘undefined’ for parted default aligment.  Choices:   - `"cylinder"` - `"minimal"` - `"none"` - `"optimal"` ← (default) - `"undefined"` |
| **device**  string / required | The block device (disk) where to operate. |
| **flags**  list / elements=string | A list of the flags that has to be set on the partition. |
| **fs_type**  string  added in community.general 0.2.0 | If specified and the partition does not exist, will set filesystem type to given partition.  Parameter optional, but see notes below about negative `part_start` values. |
| **label**  string | Disk label type to use.  If `device` already contains different label, it will be changed to `label` and any previous partitions will be lost.  Choices:   - `"aix"` - `"amiga"` - `"bsd"` - `"dvh"` - `"gpt"` - `"loop"` - `"mac"` - `"msdos"` ← (default) - `"pc98"` - `"sun"` |
| **name**  string | Sets the name for the partition number (GPT, Mac, MIPS and PC98 only). |
| **number**  integer | The number of the partition to work with or the number of the partition that will be created.  Required when performing any action on the disk, except fetching information. |
| **part_end**  string | Where the partition will end as offset from the beginning of the disk, that is, the “distance” from the start of the disk. Negative numbers specify distance from the end of the disk.  The distance can be specified with all the units supported by parted (except compat) and it is case sensitive, e.g. `10GiB`, `15%`.  Default: `"100%"` |
| **part_start**  string | Where the partition will start as offset from the beginning of the disk, that is, the “distance” from the start of the disk. Negative numbers specify distance from the end of the disk.  The distance can be specified with all the units supported by parted (except compat) and it is case sensitive, e.g. `10GiB`, `15%`.  Using negative values may require setting of `fs_type` (see notes).  Default: `"0%"` |
| **part_type**  string | May be specified only with ‘msdos’ or ‘dvh’ partition tables.  A `name` must be specified for a ‘gpt’ partition table.  Neither `part_type` nor `name` may be used with a ‘sun’ partition table.  Choices:   - `"extended"` - `"logical"` - `"primary"` ← (default) |
| **resize**  boolean  added in community.general 1.3.0 | Call `resizepart` on existing partitions to match the size specified by *part_end*.  Choices:   - `false` ← (default) - `true` |
| **state**  string | Whether to create or delete a partition.  If set to `info` the module will only return the device information.  Choices:   - `"absent"` - `"present"` - `"info"` ← (default) |
| **unit**  string | Selects the current default unit that Parted will use to display locations and capacities on the disk and to interpret those given by the user if they are not suffixed by an unit.  When fetching information about a disk, it is always recommended to specify a unit.  Choices:   - `"s"` - `"B"` - `"KB"` - `"KiB"` ← (default) - `"MB"` - `"MiB"` - `"GB"` - `"GiB"` - `"TB"` - `"TiB"` - `"%"` - `"cyl"` - `"chs"` - `"compact"` |

## [Notes](parted_module.md#id4)

> **Note:**
>
> - When fetching information about a new disk and when the version of parted installed on the system is before version 3.1, the module queries the kernel through `/sys/` to obtain disk information. In this case the units CHS and CYL are not supported.
> - Negative `part_start` start values were rejected if `fs_type` was not given. This bug was fixed in parted 3.2.153. If you want to use negative `part_start`, specify `fs_type` as well or make sure your system contains newer parted.

## [Examples](parted_module.md#id5)

```yaml+jinja
- name: Create a new ext4 primary partition
  community.general.parted:
    device: /dev/sdb
    number: 1
    state: present
    fs_type: ext4

- name: Remove partition number 1
  community.general.parted:
    device: /dev/sdb
    number: 1
    state: absent

- name: Create a new primary partition with a size of 1GiB
  community.general.parted:
    device: /dev/sdb
    number: 1
    state: present
    part_end: 1GiB

- name: Create a new primary partition for LVM
  community.general.parted:
    device: /dev/sdb
    number: 2
    flags: [ lvm ]
    state: present
    part_start: 1GiB

- name: Create a new primary partition with a size of 1GiB at disk's end
  community.general.parted:
    device: /dev/sdb
    number: 3
    state: present
    fs_type: ext3
    part_start: -1GiB

# Example on how to read info and reuse it in subsequent task
- name: Read device information (always use unit when probing)
  community.general.parted: device=/dev/sdb unit=MiB
  register: sdb_info

- name: Remove all partitions from disk
  community.general.parted:
    device: /dev/sdb
    number: '{{ item.num }}'
    state: absent
  loop: '{{ sdb_info.partitions }}'

- name: Extend an existing partition to fill all available space
  community.general.parted:
    device: /dev/sdb
    number: "{{ sdb_info.partitions | length }}"
    part_end: "100%"
    resize: true
    state: present
```

## [Return Values](parted_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **partition_info**  complex | Current partition information  Returned: success  Sample: `{"disk": {"dev": "/dev/sdb", "logical_block": 512, "model": "VMware Virtual disk", "physical_block": 512, "size": 5.0, "table": "msdos", "unit": "gib"}, "partitions": [{"begin": 0.0, "end": 1.0, "flags": ["boot", "lvm"], "fstype": "", "name": "", "num": 1, "size": 1.0}, {"begin": 1.0, "end": 5.0, "flags": [], "fstype": "", "name": "", "num": 2, "size": 4.0}], "script": "unit KiB print "}` |
| **disk**  dictionary | Generic device information.  Returned: success |
| **partitions**  list / elements=string | List of device partitions.  Returned: success |
| **script**  string | parted script executed by module  Returned: success |

### Authors

- Fabrizio Colonna (@ColOfAbRiX)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
