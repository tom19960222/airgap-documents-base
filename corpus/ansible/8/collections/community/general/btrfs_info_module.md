---
collection: ansible
version: "8"
title: "community.general.btrfs_info module – Query btrfs filesystem info"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/btrfs_info_module.html
fetched_at: 2026-07-28T01:44:52+00:00
---
# community.general.btrfs_info module – Query btrfs filesystem info

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.btrfs_info`.

New in community.general 6.6.0

- [Synopsis](btrfs_info_module.md#synopsis)
- [Attributes](btrfs_info_module.md#attributes)
- [Examples](btrfs_info_module.md#examples)
- [Return Values](btrfs_info_module.md#return-values)

## [Synopsis](btrfs_info_module.md#id1)

- Query status of available btrfs filesystems, including uuid, label, subvolumes and mountpoints.

## [Attributes](btrfs_info_module.md#id2)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](btrfs_info_module.md#id3)

```yaml+jinja
- name: Query information about mounted btrfs filesystems
  community.general.btrfs_info:
  register: my_btrfs_info
```

## [Return Values](btrfs_info_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **filesystems**  list / elements=dictionary | Summaries of the current state for all btrfs filesystems found on the target host.  **Returned:** success |
| **default_subvolume**  integer | The id of the filesystem’s default subvolume.  **Returned:** success  **Sample:** `5` |
| **devices**  list / elements=string | A list of devices assigned to the filesystem.  **Returned:** success  **Sample:** `["/dev/sda1", "/dev/sdb1"]` |
| **label**  string | An optional label assigned to the filesystem.  **Returned:** success  **Sample:** `"Tank"` |
| **subvolumes**  list / elements=dictionary | A list of dicts containing metadata for all of the filesystem’s subvolumes.  **Returned:** success |
| **id**  integer | An identifier assigned to the subvolume, unique within the containing filesystem.  **Returned:** success  **Sample:** `256` |
| **mountpoints**  list / elements=string | Paths where the subvolume is mounted on the targeted host.  **Returned:** success  **Sample:** `["/home"]` |
| **parent**  integer | The identifier of this subvolume’s parent.  **Returned:** success  **Sample:** `5` |
| **path**  string | The full path of the subvolume relative to the btrfs fileystem’s root.  **Returned:** success  **Sample:** `"/@home"` |
| **uuid**  string | A unique identifier assigned to the filesystem.  **Returned:** success  **Sample:** `"96c9c605-1454-49b8-a63a-15e2584c208e"` |

### Authors

- Gregory Furlong (@gnfzdz)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
