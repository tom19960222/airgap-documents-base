---
collection: ansible
version: "6"
title: "community.windows.win_format module – Formats an existing volume or a new volume on an existing partition on Windows"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_format_module.html
fetched_at: 2026-07-27T17:23:27+00:00
---
# community.windows.win_format module – Formats an existing volume or a new volume on an existing partition on Windows

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/community/windows) (version 1.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_format`.

- [Synopsis](win_format_module.md#synopsis)
- [Parameters](win_format_module.md#parameters)
- [Notes](win_format_module.md#notes)
- [See Also](win_format_module.md#see-also)
- [Examples](win_format_module.md#examples)

## [Synopsis](win_format_module.md#id1)

- The [community.windows.win_format](win_format_module.md#ansible-collections-community-windows-win-format-module) module formats an existing volume or a new volume on an existing partition on Windows

## [Parameters](win_format_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **allocation_unit_size**  integer | Specifies the cluster size to use when formatting the volume.  If no cluster size is specified when you format a partition, defaults are selected based on the size of the partition.  This value must be a multiple of the physical sector size of the disk. |
| **compress**  boolean | Enable compression on the resulting NTFS volume.  NTFS compression is not supported where *allocation_unit_size* is more than 4096.  Choices:   - `false` - `true` |
| **drive_letter**  string | Used to specify the drive letter of the volume to be formatted. |
| **file_system**  string | Used to specify the file system to be used when formatting the target volume.  Choices:   - `"ntfs"` - `"refs"` - `"exfat"` - `"fat32"` - `"fat"` |
| **force**  boolean | Specify if formatting should be forced for volumes that are not created from new partitions or if the source and target file system are different.  Choices:   - `false` ← (default) - `true` |
| **full**  boolean | A full format writes to every sector of the disk, takes much longer to perform than the default (quick) format, and is not recommended on storage that is thinly provisioned.  Specify `true` for full format.  Choices:   - `false` ← (default) - `true` |
| **integrity_streams**  boolean | Enable integrity streams on the resulting ReFS volume.  Choices:   - `false` - `true` |
| **label**  string | Used to specify the label of the volume to be formatted. |
| **large_frs**  boolean | Specifies that large File Record System (FRS) should be used.  Choices:   - `false` - `true` |
| **new_label**  string | Used to specify the new file system label of the formatted volume. |
| **path**  string | Used to specify the path to the volume to be formatted. |

## [Notes](win_format_module.md#id3)

> **Note:**
>
> - Microsoft Windows Server 2012 or Microsoft Windows 8 or newer is required to use this module. To check if your system is compatible, see <https://docs.microsoft.com/en-us/windows/desktop/sysinfo/operating-system-version>.
> - One of three parameters (*drive_letter*, *path* and *label*) are mandatory to identify the target volume but more than one cannot be specified at the same time.
> - This module is idempotent if *force* is not specified and file system labels remain preserved.
> - For more information, see <https://docs.microsoft.com/en-us/previous-versions/windows/desktop/stormgmt/format-msft-volume>

## [See Also](win_format_module.md#id4)

> **See also:**
>
> [community.windows.win_disk_facts](win_disk_facts_module.md#ansible-collections-community-windows-win-disk-facts-module)
> :   Show the attached disks and disk information of the target host.
>
> [community.windows.win_partition](win_partition_module.md#ansible-collections-community-windows-win-partition-module)
> :   Creates, changes and removes partitions on Windows Server.

## [Examples](win_format_module.md#id5)

```yaml+jinja
- name: Create a partition with drive letter D and size 5 GiB
  community.windows.win_partition:
    drive_letter: D
    partition_size: 5 GiB
    disk_number: 1

- name: Full format the newly created partition as NTFS and label it
  community.windows.win_format:
    drive_letter: D
    file_system: NTFS
    new_label: Formatted
    full: True
```

### Authors

- Varun Chopra (@chopraaa)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
