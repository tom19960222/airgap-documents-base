---
collection: ansible
version: "6"
title: "community.general.iso_extract module – Extract files from an ISO image"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/iso_extract_module.html
fetched_at: 2026-07-27T17:10:08+00:00
---
# community.general.iso_extract module – Extract files from an ISO image

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
> see [Requirements](iso_extract_module.md#ansible-collections-community-general-iso-extract-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.iso_extract`.

- [Synopsis](iso_extract_module.md#synopsis)
- [Requirements](iso_extract_module.md#requirements)
- [Parameters](iso_extract_module.md#parameters)
- [Notes](iso_extract_module.md#notes)
- [Examples](iso_extract_module.md#examples)

## [Synopsis](iso_extract_module.md#id1)

- This module has two possible ways of operation.
- If 7zip is installed on the system, this module extracts files from an ISO into a temporary directory and copies files to a given destination, if needed.
- If the user has mount-capabilities (CAP_SYS_ADMIN on Linux) this module mounts the ISO image to a temporary location, and copies files to a given destination, if needed.

## [Requirements](iso_extract_module.md#id2)

The below requirements are needed on the host that executes this module.

- Either 7z (from `7zip` or `p7zip` package)
- Or mount capabilities (root-access, or CAP_SYS_ADMIN capability on Linux)

## [Parameters](iso_extract_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dest**  path / required | The destination directory to extract files to. |
| **executable**  path | The path to the `7z` executable to use for extracting files from the ISO.  If not provided, it will assume the value `7z`. |
| **files**  list / elements=string / required | A list of files to extract from the image.  Extracting directories does not work. |
| **force**  boolean | If `true`, which will replace the remote file when contents are different than the source.  If `false`, the file will only be extracted and copied if the destination does not already exist.  Choices:   - `false` - `true` ← (default) |
| **image**  aliases: path, src  path / required | The ISO image to extract files from. |

## [Notes](iso_extract_module.md#id4)

> **Note:**
>
> - Only the file checksum (content) is taken into account when extracting files from the ISO image. If *force=false*, only checks the presence of the file.
> - In Ansible 2.3 this module was using `mount` and `umount` commands only, requiring root access. This is no longer needed with the introduction of 7zip for extraction.

## [Examples](iso_extract_module.md#id5)

```yaml+jinja
- name: Extract kernel and ramdisk from a LiveCD
  community.general.iso_extract:
    image: /tmp/rear-test.iso
    dest: /tmp/virt-rear/
    files:
    - isolinux/kernel
    - isolinux/initrd.cgz
```

### Authors

- Jeroen Hoekx (@jhoekx)
- Matt Robinson (@ribbons)
- Dag Wieers (@dagwieers)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
