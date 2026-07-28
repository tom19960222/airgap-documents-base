---
collection: ansible
version: "6"
title: "community.general.mksysb module – Generates AIX mksysb rootvg backups"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/mksysb_module.html
fetched_at: 2026-07-27T17:10:58+00:00
---
# community.general.mksysb module – Generates AIX mksysb rootvg backups

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.mksysb`.

- [Synopsis](mksysb_module.md#synopsis)
- [Parameters](mksysb_module.md#parameters)
- [Examples](mksysb_module.md#examples)
- [Return Values](mksysb_module.md#return-values)

## [Synopsis](mksysb_module.md#id1)

- This module manages a basic AIX mksysb (image) of rootvg.

## [Parameters](mksysb_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **backup_crypt_files**  boolean | Backup encrypted files.  Choices:   - `false` - `true` ← (default) |
| **backup_dmapi_fs**  boolean | Back up DMAPI filesystem files.  Choices:   - `false` - `true` ← (default) |
| **create_map_files**  boolean | Creates a new MAP files.  Choices:   - `false` ← (default) - `true` |
| **exclude_files**  boolean | Excludes files using `/etc/rootvg.exclude`.  Choices:   - `false` ← (default) - `true` |
| **exclude_wpar_files**  boolean | Excludes WPAR files.  Choices:   - `false` ← (default) - `true` |
| **extended_attrs**  boolean | Backup extended attributes.  Choices:   - `false` - `true` ← (default) |
| **name**  string / required | Backup name |
| **new_image_data**  boolean | Creates a new file data.  Choices:   - `false` - `true` ← (default) |
| **software_packing**  boolean | Exclude files from packing option listed in `/etc/exclude_packing.rootvg`.  Choices:   - `false` ← (default) - `true` |
| **storage_path**  string / required | Storage path where the mksysb will stored. |
| **use_snapshot**  boolean | Creates backup using snapshots.  Choices:   - `false` ← (default) - `true` |

## [Examples](mksysb_module.md#id3)

```yaml+jinja
- name: Running a backup image mksysb
  community.general.mksysb:
    name: myserver
    storage_path: /repository/images
    exclude_files: true
    exclude_wpar_files: true
```

## [Return Values](mksysb_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Return changed for mksysb actions as true or false.  Returned: always |
| **msg**  string | Return message regarding the action.  Returned: always |

### Authors

- Kairo Araujo (@kairoaraujo)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
