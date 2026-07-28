---
collection: ansible
version: "6"
title: "community.general.iso_customize module – Add/remove/change files in ISO file"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/iso_customize_module.html
fetched_at: 2026-07-27T17:10:07+00:00
---
# community.general.iso_customize module – Add/remove/change files in ISO file

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
> see [Requirements](iso_customize_module.md#ansible-collections-community-general-iso-customize-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.iso_customize`.

New in community.general 5.8.0

- [Synopsis](iso_customize_module.md#synopsis)
- [Requirements](iso_customize_module.md#requirements)
- [Parameters](iso_customize_module.md#parameters)
- [Notes](iso_customize_module.md#notes)
- [Examples](iso_customize_module.md#examples)
- [Return Values](iso_customize_module.md#return-values)

## [Synopsis](iso_customize_module.md#id1)

- This module is used to add/remove/change files in ISO file.
- The file inside ISO will be overwritten if it exists by option *add_files*.

## [Requirements](iso_customize_module.md#id2)

The below requirements are needed on the host that executes this module.

- pycdlib
- python >= 2.7

## [Parameters](iso_customize_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **add_files**  list / elements=dictionary | Allows to add and replace files in the ISO file.  Will create intermediate folders inside the ISO file when they do not exist.  Default: `[]` |
| **dest_file**  string / required | The absolute path of the file inside the ISO file. |
| **src_file**  path / required | The path with file name on the machine the module is executed on. |
| **delete_files**  list / elements=string | Absolute paths for files inside the ISO file that should be removed.  Default: `[]` |
| **dest_iso**  path / required | The path of the customized ISO file. |
| **src_iso**  path / required | This is the path of source ISO file. |

## [Notes](iso_customize_module.md#id4)

> **Note:**
>
> - The `pycdlib` library states it supports Python 2.7 and 3.4 only.
> - The function *add_file* in pycdlib will overwrite the existing file in ISO with type ISO9660 / Rock Ridge 1.12 / Joliet / UDF. But it will not overwrite the existing file in ISO with Rock Ridge 1.09 / 1.10. So we take workaround “delete the existing file and then add file for ISO with Rock Ridge”.

## [Examples](iso_customize_module.md#id5)

```yaml+jinja
- name: "Customize ISO file"
  community.general.iso_customize:
    src_iso: "/path/to/ubuntu-22.04-desktop-amd64.iso"
    dest_iso: "/path/to/ubuntu-22.04-desktop-amd64-customized.iso"
    delete_files:
      - "/boot.catalog"
    add_files:
      - src_file: "/path/to/grub.cfg"
        dest_file: "/boot/grub/grub.cfg"
      - src_file: "/path/to/ubuntu.seed"
        dest_file: "/preseed/ubuntu.seed"
  register: customize_iso_result
```

## [Return Values](iso_customize_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dest_iso**  string | Path of the customized ISO file.  Returned: on success  Sample: `"/path/to/customized.iso"` |
| **src_iso**  string | Path of source ISO file.  Returned: on success  Sample: `"/path/to/file.iso"` |

### Authors

- Yuhua Zou (@ZouYuhua)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
