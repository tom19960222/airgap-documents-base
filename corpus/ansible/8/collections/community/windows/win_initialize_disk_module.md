---
collection: ansible
version: "8"
title: "community.windows.win_initialize_disk module – Initializes disks on Windows Server"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_initialize_disk_module.html
fetched_at: 2026-07-28T02:02:03+00:00
---
# community.windows.win_initialize_disk module – Initializes disks on Windows Server

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
> To use it in a playbook, specify: `community.windows.win_initialize_disk`.

- [Synopsis](win_initialize_disk_module.md#synopsis)
- [Parameters](win_initialize_disk_module.md#parameters)
- [Notes](win_initialize_disk_module.md#notes)
- [See Also](win_initialize_disk_module.md#see-also)
- [Examples](win_initialize_disk_module.md#examples)

## [Synopsis](win_initialize_disk_module.md#id1)

- The [community.windows.win_initialize_disk](win_initialize_disk_module.md#ansible-collections-community-windows-win-initialize-disk-module) module initializes disks

## [Parameters](win_initialize_disk_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **disk_number**  integer | Used to specify the disk number of the disk to be initialized. |
| **force**  boolean | Specify if initializing should be forced for disks that are already initialized.  **Choices:**   - `false` ← (default) - `true` |
| **online**  boolean | If the disk is offline and/or readonly update the disk to be online and not readonly.  **Choices:**   - `false` - `true` ← (default) |
| **path**  string | Used to specify the path to the disk to be initialized. |
| **style**  string | The partition style to use for the disk. Valid options are mbr or gpt.  **Choices:**   - `"gpt"` ← (default) - `"mbr"` |
| **uniqueid**  string | Used to specify the uniqueid of the disk to be initialized. |

## [Notes](win_initialize_disk_module.md#id3)

> **Note:**
>
> - One of three parameters (*disk_number*, *uniqueid*, and *path*) are mandatory to identify the target disk, but more than one cannot be specified at the same time.
> - A minimum Operating System Version of Server 2012 or Windows 8 is required to use this module.
> - This module is idempotent if *force* is not specified.

## [See Also](win_initialize_disk_module.md#id4)

> **See also:**
>
> [community.windows.win_disk_facts](win_disk_facts_module.md#ansible-collections-community-windows-win-disk-facts-module)
> :   Show the attached disks and disk information of the target host.
>
> [community.windows.win_partition](win_partition_module.md#ansible-collections-community-windows-win-partition-module)
> :   Creates, changes and removes partitions on Windows Server.
>
> [community.windows.win_format](win_format_module.md#ansible-collections-community-windows-win-format-module)
> :   Formats an existing volume or a new volume on an existing partition on Windows.

## [Examples](win_initialize_disk_module.md#id5)

```yaml+jinja
- name: Initialize a disk
  community.windows.win_initialize_disk:
    disk_number: 1

- name: Initialize a disk with an MBR partition style
  community.windows.win_initialize_disk:
    disk_number: 1
    style: mbr

- name: Forcefully initiallize a disk
  community.windows.win_initialize_disk:
    disk_number: 2
    force: yes
```

### Authors

- Brant Evans (@branic)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
