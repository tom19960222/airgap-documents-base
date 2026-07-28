---
collection: ansible
version: "6"
title: "community.general.vexata_volume module – Manage volumes on Vexata VX100 storage arrays"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/vexata_volume_module.html
fetched_at: 2026-07-27T17:13:56+00:00
---
# community.general.vexata_volume module – Manage volumes on Vexata VX100 storage arrays

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
> see [Requirements](vexata_volume_module.md#ansible-collections-community-general-vexata-volume-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.vexata_volume`.

- [Synopsis](vexata_volume_module.md#synopsis)
- [Requirements](vexata_volume_module.md#requirements)
- [Parameters](vexata_volume_module.md#parameters)
- [Examples](vexata_volume_module.md#examples)

## [Synopsis](vexata_volume_module.md#id1)

- Create, deletes or extend volumes on a Vexata VX100 array.

## [Requirements](vexata_volume_module.md#id2)

The below requirements are needed on the host that executes this module.

- Vexata VX100 storage array with VXOS >= v3.5.0 on storage array
- vexatapi >= 0.0.1
- python >= 2.7
- VEXATA_USER and VEXATA_PASSWORD environment variables must be set if user and password arguments are not passed to the module directly.

## [Parameters](vexata_volume_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **array**  string / required | Vexata VX100 array hostname or IPv4 Address. |
| **name**  string / required | Volume name. |
| **password**  string | Vexata API user password. |
| **size**  string | Volume size in M, G, T units. M=2^20, G=2^30, T=2^40 bytes. |
| **state**  string | Creates/Modifies volume when present or removes when absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **user**  string | Vexata API user with administrative privileges. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` ← (default) - `true` |

## [Examples](vexata_volume_module.md#id4)

```yaml+jinja
- name: Create new 2 TiB volume named foo
  community.general.vexata_volume:
    name: foo
    size: 2T
    state: present
    array: vx100_ultra.test.com
    user: admin
    password: secret

- name: Expand volume named foo to 4 TiB
  community.general.vexata_volume:
    name: foo
    size: 4T
    state: present
    array: vx100_ultra.test.com
    user: admin
    password: secret

- name: Delete volume named foo
  community.general.vexata_volume:
    name: foo
    state: absent
    array: vx100_ultra.test.com
    user: admin
    password: secret
```

### Authors

- Sandeep Kasargod (@vexata)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
