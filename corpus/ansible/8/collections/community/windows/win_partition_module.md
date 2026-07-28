---
collection: ansible
version: "8"
title: "community.windows.win_partition module – Creates, changes and removes partitions on Windows Server"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_partition_module.html
fetched_at: 2026-07-28T02:02:09+00:00
---
# community.windows.win_partition module – Creates, changes and removes partitions on Windows Server

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/ui/repo/published/community/windows/) (version 1.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_partition`.

- [Synopsis](win_partition_module.md#synopsis)
- [Parameters](win_partition_module.md#parameters)
- [Notes](win_partition_module.md#notes)
- [Examples](win_partition_module.md#examples)

## [Synopsis](win_partition_module.md#id1)

- The [community.windows.win_partition](win_partition_module.md#ansible-collections-community-windows-win-partition-module) module can create, modify or delete a partition on a disk

## [Parameters](win_partition_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **active**  boolean | Specifies if the partition is active and can be used to start the system. This property is only valid when the disk’s partition style is MBR.  **Choices:**   - `false` - `true` |
| **disk_number**  integer | Disk number is mandatory for creating new partitions.  A combination of *disk_number* and *partition_number* can be used to specify the partition instead of *drive_letter* if required. |
| **drive_letter**  string | Used for accessing partitions if *disk_number* and *partition_number* are not provided.  Use `auto` for automatically assigning a drive letter, or a letter A-Z for manually assigning a drive letter to a new partition. If not specified, no drive letter is assigned when creating a new partition. |
| **gpt_type**  string | Specify the partition’s GPT type if the disk’s partition style is GPT.  This only applies to new partitions.  This does not relate to the partitions file system formatting.  **Choices:**   - `"system_partition"` - `"microsoft_reserved"` - `"basic_data"` - `"microsoft_recovery"` |
| **hidden**  boolean | Hides the target partition, making it undetectable by the mount manager.  **Choices:**   - `false` - `true` |
| **mbr_type**  string | Specify the partition’s MBR type if the disk’s partition style is MBR.  This only applies to new partitions.  This does not relate to the partitions file system formatting.  **Choices:**   - `"fat12"` - `"fat16"` - `"extended"` - `"huge"` - `"ifs"` - `"fat32"` |
| **offline**  boolean | Sets the partition offline.  Adding a mount point (such as a drive letter) will cause the partition to go online again.  **Choices:**   - `false` - `true` |
| **partition_number**  integer | Used in conjunction with *disk_number* to uniquely identify a partition. |
| **partition_size**  string | Specify size of the partition in B, KB, KiB, MB, MiB, GB, GiB, TB or TiB. Use -1 to specify maximum supported size.  Partition size is mandatory for creating a new partition but not for updating or deleting a partition.  The decimal SI prefixes kilo, mega, giga, tera, etc., are powers of 10^3 = 1000. The binary prefixes kibi, mebi, gibi, tebi, etc. respectively refer to the corresponding power of 2^10 = 1024. Thus, a gigabyte (GB) is 1000000000 (1000^3) bytes while 1 gibibyte (GiB) is 1073741824 (1024^3) bytes. |
| **read_only**  boolean | Make the partition read only, restricting changes from being made to the partition.  **Choices:**   - `false` - `true` |
| **state**  string | Used to specify the state of the partition. Use `absent` to specify if a partition should be removed and `present` to specify if the partition should be created or updated.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Notes](win_partition_module.md#id3)

> **Note:**
>
> - A minimum Operating System Version of 6.2 is required to use this module. To check if your OS is compatible, see <https://docs.microsoft.com/en-us/windows/desktop/sysinfo/operating-system-version>.
> - This module cannot be used for removing the drive letter associated with a partition, initializing a disk or, file system formatting.
> - Idempotence works only if you’re specifying a drive letter or other unique attributes such as a combination of disk number and partition number.
> - For more information, see <https://msdn.microsoft.com/en-us/library/windows/desktop/hh830524.aspx>.

## [Examples](win_partition_module.md#id4)

```yaml+jinja
- name: Create a partition with drive letter D and size 5 GiB
  community.windows.win_partition:
    drive_letter: D
    partition_size: 5 GiB
    disk_number: 1

- name: Resize previously created partition to it's maximum size and change it's drive letter to E
  community.windows.win_partition:
    drive_letter: E
    partition_size: -1
    partition_number: 1
    disk_number: 1

- name: Delete partition
  community.windows.win_partition:
    disk_number: 1
    partition_number: 1
    state: absent
```

### Authors

- Varun Chopra (@chopraaa)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
