---
collection: ansible
version: "6"
title: "community.windows.win_data_deduplication module – Module to enable Data Deduplication on a volume."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_data_deduplication_module.html
fetched_at: 2026-07-27T17:23:13+00:00
---
# community.windows.win_data_deduplication module – Module to enable Data Deduplication on a volume.

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
> To use it in a playbook, specify: `community.windows.win_data_deduplication`.

- [Synopsis](win_data_deduplication_module.md#synopsis)
- [Parameters](win_data_deduplication_module.md#parameters)
- [Examples](win_data_deduplication_module.md#examples)

## [Synopsis](win_data_deduplication_module.md#id1)

- This module can be used to enable Data Deduplication on a Windows volume.
- The module will install the FS-Data-Deduplication feature (a reboot will be necessary).

## [Parameters](win_data_deduplication_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **drive_letter**  string / required | Windows drive letter on which to enable data deduplication. |
| **settings**  dictionary | Dictionary of settings to pass to the Set-DedupVolume powershell command. |
| **minimum_file_age_days**  integer | Minimum file age you want to target for deduplication.  Default: `2` |
| **minimum_file_size**  integer | Minimum file size you want to target for deduplication.  It will default to 32768 if not defined or if the value is less than 32768.  Default: `32768` |
| **no_compress**  boolean | Wether you want to enabled filesystem compression or not.  Choices:   - `false` ← (default) - `true` |
| **optimize_in_use_files**  boolean | Indicates that the server attempts to optimize currently open files.  Choices:   - `false` ← (default) - `true` |
| **verify**  boolean | Indicates whether the deduplication engine performs a byte-for-byte verification for each duplicate chunk that optimization creates, rather than relying on a cryptographically strong hash.  This option is not recommend.  Setting this parameter to True can degrade optimization performance.  Choices:   - `false` ← (default) - `true` |
| **state**  string | Wether to enable or disable data deduplication on the selected volume.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Examples](win_data_deduplication_module.md#id3)

```yaml+jinja
- name: Enable Data Deduplication on D
  community.windows.win_data_deduplication:
    drive_letter: 'D'
    state: present

- name: Enable Data Deduplication on D
  community.windows.win_data_deduplication:
    drive_letter: 'D'
    state: present
    settings:
      no_compress: true
      minimum_file_age_days: 1
      minimum_file_size: 0
```

### Authors

- rnsc (@rnsc)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
