---
collection: ansible
version: "6"
title: "community.windows.win_disk_image module – Manage ISO/VHD/VHDX mounts on Windows hosts"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_disk_image_module.html
fetched_at: 2026-07-27T17:23:16+00:00
---
# community.windows.win_disk_image module – Manage ISO/VHD/VHDX mounts on Windows hosts

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
> To use it in a playbook, specify: `community.windows.win_disk_image`.

- [Synopsis](win_disk_image_module.md#synopsis)
- [Parameters](win_disk_image_module.md#parameters)
- [Examples](win_disk_image_module.md#examples)
- [Return Values](win_disk_image_module.md#return-values)

## [Synopsis](win_disk_image_module.md#id1)

- Manages mount behavior for a specified ISO, VHD, or VHDX image on a Windows host. When `state` is `present`, the image will be mounted under a system-assigned drive letter, which will be returned in the `mount_path` value of the module result.
- Requires Windows 8+ or Windows Server 2012+.

## [Parameters](win_disk_image_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **image_path**  string / required | Path to an ISO, VHD, or VHDX image on the target Windows host (the file cannot reside on a network share) |
| **state**  string | Whether the image should be present as a drive-letter mount or not.  Choices:   - `"absent"` - `"present"` ← (default) |

## [Examples](win_disk_image_module.md#id3)

```yaml+jinja
# Run installer from mounted ISO, then unmount
- name: Ensure an ISO is mounted
  community.windows.win_disk_image:
    image_path: C:\install.iso
    state: present
  register: disk_image_out

- name: Run installer from mounted ISO
  ansible.windows.win_package:
    path: '{{ disk_image_out.mount_paths[0] }}setup\setup.exe'
    product_id: 35a4e767-0161-46b0-979f-e61f282fee21
    state: present

- name: Unmount ISO
  community.windows.win_disk_image:
    image_path: C:\install.iso
    state: absent
```

## [Return Values](win_disk_image_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **mount_paths**  list / elements=string | A list of filesystem paths mounted from the target image.  Returned: when `state` is `present`  Sample: `["E:\\", "F:\\"]` |

### Authors

- Matt Davis (@nitzmahone)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
