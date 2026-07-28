---
collection: ansible
version: "8"
title: "community.general.btrfs_subvolume module – Manage btrfs subvolumes"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/btrfs_subvolume_module.html
fetched_at: 2026-07-28T01:44:53+00:00
---
# community.general.btrfs_subvolume module – Manage btrfs subvolumes

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
> To use it in a playbook, specify: `community.general.btrfs_subvolume`.

New in community.general 6.6.0

- [Synopsis](btrfs_subvolume_module.md#synopsis)
- [Parameters](btrfs_subvolume_module.md#parameters)
- [Attributes](btrfs_subvolume_module.md#attributes)
- [Notes](btrfs_subvolume_module.md#notes)
- [Examples](btrfs_subvolume_module.md#examples)
- [Return Values](btrfs_subvolume_module.md#return-values)

## [Synopsis](btrfs_subvolume_module.md#id1)

- Creates, updates and deletes btrfs subvolumes and snapshots.

## [Parameters](btrfs_subvolume_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **automount**  boolean | Allow the module to temporarily mount the targeted btrfs filesystem in order to validate the current state and make any required changes.  **Choices:**   - `false` ← (default) - `true` |
| **default**  boolean | Make the subvolume specified by `name` the filesystem’s default subvolume.  **Choices:**   - `false` ← (default) - `true` |
| **filesystem_device**  path | A block device contained within the btrfs filesystem to be targeted.  Useful when multiple btrfs filesystems are present to specify which filesystem should be targeted. |
| **filesystem_label**  string | A descriptive label assigned to the btrfs filesystem to be targeted.  Useful when multiple btrfs filesystems are present to specify which filesystem should be targeted. |
| **filesystem_uuid**  string | A unique identifier assigned to the btrfs filesystem to be targeted.  Useful when multiple btrfs filesystems are present to specify which filesystem should be targeted. |
| **name**  string / required | Name of the subvolume/snapshot to be targeted. |
| **recursive**  boolean | When true, indicates that parent/child subvolumes should be created/removedas necessary to complete the operation (for `state=present` and `state=absent` respectively).  **Choices:**   - `false` ← (default) - `true` |
| **snapshot_conflict**  string | Policy defining behavior when a subvolume already exists at the path of the requested snapshot.  `skip` - Create a snapshot only if a subvolume does not yet exist at the target location, otherwise indicate that no change is required. Warning, this option does not yet verify that the target subvolume was generated from a snapshot of the requested source.  `clobber` - If a subvolume already exists at the requested location, delete it first. This option is not idempotent and will result in a new snapshot being generated on every execution.  `error` - If a subvolume already exists at the requested location, return an error. This option is not idempotent and will result in an error on replay of the module.  **Choices:**   - `"skip"` ← (default) - `"clobber"` - `"error"` |
| **snapshot_source**  string | Identifies the source subvolume for the created snapshot.  Infers that the created subvolume is a snapshot. |
| **state**  string | Indicates the current state of the targeted subvolume.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Attributes](btrfs_subvolume_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **partial**  In some scenarios it may erroneously report intermediate subvolumes being created. After mounting, if a directory like file is found where the subvolume would have been created, the operation is skipped. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](btrfs_subvolume_module.md#id4)

> **Note:**
>
> - If any or all of the options `filesystem_device`, `filesystem_label` or `filesystem_uuid` parameters are provided, there is expected to be a matching btrfs filesystem. If none are provided and only a single btrfs filesystem exists or only a single btrfs filesystem is mounted, that filesystem will be used; otherwise, the module will take no action and return an error.

## [Examples](btrfs_subvolume_module.md#id5)

```yaml+jinja
- name: Create a @home subvolume under the root subvolume
  community.general.btrfs_subvolume:
    name: /@home
    device: /dev/vda2

- name: Remove the @home subvolume if it exists
  community.general.btrfs_subvolume:
    name: /@home
    state: absent
    device: /dev/vda2

- name: Create a snapshot of the root subvolume named @
  community.general.btrfs_subvolume:
    name: /@
    snapshot_source: /
    device: /dev/vda2

- name: Create a snapshot of the root subvolume and make it the new default subvolume
  community.general.btrfs_subvolume:
    name: /@
    snapshot_source: /
    default: Yes
    device: /dev/vda2

- name: Create a snapshot of the /@ subvolume and recursively creating intermediate subvolumes as required
  community.general.btrfs_subvolume:
    name: /@snapshots/@2022_06_09
    snapshot_source: /@
    recursive: True
    device: /dev/vda2

- name: Remove the /@ subvolume and recursively delete child subvolumes as required
  community.general.btrfs_subvolume:
    name: /@snapshots/@2022_06_09
    snapshot_source: /@
    recursive: True
    device: /dev/vda2
```

## [Return Values](btrfs_subvolume_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **filesystem**  dictionary | A summary of the final state of the targeted btrfs filesystem.  **Returned:** success |
| **default_subvolume**  integer | The ID of the filesystem’s default subvolume.  **Returned:** success and if filesystem is mounted  **Sample:** `5` |
| **devices**  list / elements=string | A list of devices assigned to the filesystem.  **Returned:** success  **Sample:** `["/dev/sda1", "/dev/sdb1"]` |
| **label**  string | An optional label assigned to the filesystem.  **Returned:** success  **Sample:** `"Tank"` |
| **subvolumes**  list / elements=dictionary | A list of dicts containing metadata for all of the filesystem’s subvolumes.  **Returned:** success and if filesystem is mounted |
| **id**  integer | An identifier assigned to the subvolume, unique within the containing filesystem.  **Returned:** success  **Sample:** `256` |
| **mountpoints**  list / elements=string | Paths where the subvolume is mounted on the targeted host.  **Returned:** success  **Sample:** `["/home"]` |
| **parent**  integer | The identifier of this subvolume’s parent.  **Returned:** success  **Sample:** `5` |
| **path**  string | The full path of the subvolume relative to the btrfs fileystem’s root.  **Returned:** success  **Sample:** `"/@home"` |
| **uuid**  string | A unique identifier assigned to the filesystem.  **Returned:** success  **Sample:** `"96c9c605-1454-49b8-a63a-15e2584c208e"` |
| **modifications**  list / elements=string | A list where each element describes a change made to the target btrfs filesystem.  **Returned:** Success |
| **target_subvolume_id**  integer | The ID of the subvolume specified with the `name` parameter, either pre-existing or created as part of module execution.  **Returned:** Success and subvolume exists after module execution  **Sample:** `257` |

### Authors

- Gregory Furlong (@gnfzdz)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
