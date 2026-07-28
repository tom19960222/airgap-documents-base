---
collection: ansible
version: "6"
title: "community.general.iso_create module – Generate ISO file with specified files or folders"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/iso_create_module.html
fetched_at: 2026-07-27T17:10:07+00:00
---
# community.general.iso_create module – Generate ISO file with specified files or folders

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
> see [Requirements](iso_create_module.md#ansible-collections-community-general-iso-create-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.iso_create`.

New in community.general 0.2.0

- [Synopsis](iso_create_module.md#synopsis)
- [Requirements](iso_create_module.md#requirements)
- [Parameters](iso_create_module.md#parameters)
- [Examples](iso_create_module.md#examples)
- [Return Values](iso_create_module.md#return-values)

## [Synopsis](iso_create_module.md#id1)

- This module is used to generate ISO file with specified path of files.

## [Requirements](iso_create_module.md#id2)

The below requirements are needed on the host that executes this module.

- pycdlib
- python >= 2.7

## [Parameters](iso_create_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dest_iso**  path / required | The absolute path with file name of the new generated ISO file on local machine.  Will create intermediate folders when they does not exist. |
| **interchange_level**  integer | The ISO9660 interchange level to use, it dictates the rules on the names of files.  Levels and valid values `1`, `2`, `3`, `4` are supported.  The default value is level `1`, which is the most conservative, level `3` is recommended.  ISO9660 file names at interchange level `1` cannot have more than 8 characters or 3 characters in the extension.  Choices:   - `1` ← (default) - `2` - `3` - `4` |
| **joliet**  integer | Support levels and valid values are `1`, `2`, or `3`.  Level `3` is by far the most common.  If not specified, then no Joliet support is added.  Choices:   - `1` - `2` - `3` |
| **rock_ridge**  string | Whether to make this ISO have the Rock Ridge extensions or not.  Valid values are `1.09`, `1.10` or `1.12`, means adding the specified Rock Ridge version to the ISO.  If unsure, set `1.09` to ensure maximum compatibility.  If not specified, then not add Rock Ridge extension to the ISO.  Choices:   - `"1.09"` - `"1.10"` - `"1.12"` |
| **src_files**  list / elements=path / required | This is a list of absolute paths of source files or folders which will be contained in the new generated ISO file.  Will fail if specified file or folder in `src_files` does not exist on local machine.  Note: With all ISO9660 levels from 1 to 3, all file names are restricted to uppercase letters, numbers and underscores (_). File names are limited to 31 characters, directory nesting is limited to 8 levels, and path names are limited to 255 characters. |
| **udf**  boolean | Whether to add UDF support to this ISO.  If set to `True`, then version 2.60 of the UDF spec is used.  If not specified or set to `False`, then no UDF support is added.  Choices:   - `false` ← (default) - `true` |
| **vol_ident**  string | The volume identification string to use on the new generated ISO image. |

## [Examples](iso_create_module.md#id4)

```yaml+jinja
- name: Create an ISO file
  community.general.iso_create:
    src_files:
      - /root/testfile.yml
      - /root/testfolder
    dest_iso: /tmp/test.iso
    interchange_level: 3

- name: Create an ISO file with Rock Ridge extension
  community.general.iso_create:
    src_files:
      - /root/testfile.yml
      - /root/testfolder
    dest_iso: /tmp/test.iso
    rock_ridge: 1.09

- name: Create an ISO file with Joliet support
  community.general.iso_create:
    src_files:
      - ./windows_config/Autounattend.xml
    dest_iso: ./test.iso
    interchange_level: 3
    joliet: 3
    vol_ident: WIN_AUTOINSTALL
```

## [Return Values](iso_create_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **created_iso**  string | Created iso file path.  Returned: on success  Sample: `"/path/to/test.iso"` |
| **interchange_level**  integer | Configured interchange level.  Returned: on success  Sample: `3` |
| **joliet**  integer | Configured Joliet support level.  Returned: on success  Sample: `3` |
| **rock_ridge**  string | Configured Rock Ridge version.  Returned: on success  Sample: `"1.09"` |
| **source_file**  list / elements=path | Configured source files or directories list.  Returned: on success  Sample: `["/path/to/file.txt", "/path/to/folder"]` |
| **udf**  boolean | Configured UDF support.  Returned: on success  Sample: `false` |
| **vol_ident**  string | Configured volume identification string.  Returned: on success  Sample: `"OEMDRV"` |

### Authors

- Diane Wang (@Tomorrow9)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
