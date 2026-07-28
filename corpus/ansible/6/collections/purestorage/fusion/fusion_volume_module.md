---
collection: ansible
version: "6"
title: "purestorage.fusion.fusion_volume module – Manage volumes in Pure Storage Fusion"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/fusion/fusion_volume_module.html
fetched_at: 2026-07-27T16:43:35+00:00
---
# purestorage.fusion.fusion_volume module – Manage volumes in Pure Storage Fusion

> **Note:**
>
> This module is part of the [purestorage.fusion collection](https://galaxy.ansible.com/purestorage/fusion) (version 1.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.fusion`.
> You need further requirements to be able to use this module,
> see [Requirements](fusion_volume_module.md#ansible-collections-purestorage-fusion-fusion-volume-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.fusion.fusion_volume`.

New in purestorage.fusion 1.0.0

- [Synopsis](fusion_volume_module.md#synopsis)
- [Requirements](fusion_volume_module.md#requirements)
- [Parameters](fusion_volume_module.md#parameters)
- [Notes](fusion_volume_module.md#notes)
- [Examples](fusion_volume_module.md#examples)

## [Synopsis](fusion_volume_module.md#id1)

- Create, update or delete a volume in Pure Storage Fusion.

## [Requirements](fusion_volume_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.5
- purefusion

## [Parameters](fusion_volume_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **app_id**  string | Application ID from Pure1 Registration page  eg. pure1:apikey:dssf2331sd  Defaults to the set environment variable under FUSION_APP_ID |
| **display_name**  string | The human name of the volume.  If not provided, defaults to *name*. |
| **eradicate**  boolean | Define whether to eradicate the volume on delete or leave in trash.  Choices:   - `false` ← (default) - `true` |
| **hosts**  list / elements=string | A list of host access policies to connect the volume to. |
| **key_file**  string | Path to the private key file  Defaults to the set environment variable under FUSION_PRIVATE_KEY_FILE. |
| **name**  string / required | The name of the volume. |
| **placement_group**  string | The name of the plcement group. |
| **protection_policy**  string | The name of the protection policy. |
| **rename**  string | New name for volume. |
| **size**  string | Volume size in M, G, T or P units. |
| **state**  string | Define whether the volume should exist or not.  Choices:   - `"absent"` - `"present"` ← (default) |
| **storage_class**  string | The name of the storage class. |
| **tenant**  string / required | The name of the tenant. |
| **tenant_space**  string / required | The name of the tenant space. |

## [Notes](fusion_volume_module.md#id4)

> **Note:**
>
> - Supports `check mode`.
> - This module requires the *purefusion* Python library
> - You must set `FUSION_APP_ID` and `FUSION_PRIVATE_KEY_FILE` environment variables if *app_id* and *key_file* arguments are not passed to the module directly

## [Examples](fusion_volume_module.md#id5)

```yaml+jinja
- name: Create new volume named foo in storage_class fred
  purestorage.fusion.fusion_volume:
    name: foo
    storage_class: fred
    size: 1T
    tenant: test
    tenant_space: space_1
    state: present
    app_id: key_name
    key_file: "az-admin-private-key.pem"

- name: Extend the size of an existing volume named foo
  purestorage.fusion.fusion_volume:
    name: foo
    size: 2T
    tenant: test
    tenant_space: space_1
    state: present
    app_id: key_name
    key_file: "az-admin-private-key.pem"

- name: Rename volume named foo to bar
  purestorage.fusion.fusion_volume:
    name: foo
    rename: bar
    tenant: test
    tenant_space: space_1
    state: absent
    app_id: key_name
    key_file: "az-admin-private-key.pem"

- name: Delete volume named foo
  purestorage.fusion.fusion_volume:
    name: foo
    tenant: test
    tenant_space: space_1
    state: absent
    app_id: key_name
    key_file: "az-admin-private-key.pem"
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/Fusion-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/Fusion-Collection)
