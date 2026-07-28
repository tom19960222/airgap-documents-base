---
collection: ansible
version: "8"
title: "purestorage.fusion.fusion_volume module – Manage volumes in Pure Storage Fusion"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/fusion/fusion_volume_module.html
fetched_at: 2026-07-28T01:05:57+00:00
---
# purestorage.fusion.fusion_volume module – Manage volumes in Pure Storage Fusion

> **Note:**
>
> This module is part of the [purestorage.fusion collection](https://galaxy.ansible.com/ui/repo/published/purestorage/fusion/) (version 1.6.0).
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

- python >= 3.8
- purefusion

## [Parameters](fusion_volume_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Access token for Fusion Service  Defaults to the set environment variable under FUSION_ACCESS_TOKEN |
| **display_name**  string | The human name of the volume.  If not provided, defaults to *name*. |
| **eradicate**  boolean | Wipes the volume instead of a soft delete if true. Must be used with `state: absent`.  **Choices:**   - `false` ← (default) - `true` |
| **host_access_policies**  list / elements=string | A list of host access policies to connect the volume to. To clear, assign empty list: host_access_policies: [] |
| **issuer_id**  aliases: app_id  string | Application ID from Pure1 Registration page  eg. pure1:apikey:dssf2331sd  Defaults to the set environment variable under FUSION_ISSUER_ID |
| **name**  string / required | The name of the volume. |
| **placement_group**  string | The name of the placement group. |
| **private_key_file**  aliases: key_file  string | Path to the private key file  Defaults to the set environment variable under FUSION_PRIVATE_KEY_FILE. |
| **private_key_password**  string | Password of the encrypted private key file |
| **protection_policy**  string | The name of the protection policy. |
| **rename**  string | New name for volume. |
| **size**  string | Volume size in M, G, T or P units. |
| **source_snapshot**  string | The source snapshot name. It must live within the same tenant space. Cannot be used together with `source_volume`. |
| **source_volume**  string | The source volume name. It must live within the same tenant space. Cannot be used together with `source_snapshot` or `source_volume_snapshot`. |
| **source_volume_snapshot**  string | The source volume snapshot name. It must live within the same tenant space. Cannot be used together with `source_volume`. |
| **state**  string | Define whether the volume should exist or not.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **storage_class**  string | The name of the storage class. |
| **tenant**  string / required | The name of the tenant. |
| **tenant_space**  string / required | The name of the tenant space. |

## [Notes](fusion_volume_module.md#id4)

> **Note:**
>
> - Supports `check mode`.
> - This module requires the *purefusion* Python library
> - You must set `FUSION_ISSUER_ID` and `FUSION_PRIVATE_KEY_FILE` environment variables if *issuer_id* and *private_key_file* arguments are not passed to the module directly
> - If you want to use access token for authentication, you must use `FUSION_ACCESS_TOKEN` environment variable if *access_token* argument is not passed to the module directly

## [Examples](fusion_volume_module.md#id5)

```yaml+jinja
- name: Create new volume named foo in storage_class fred
  purestorage.fusion.fusion_volume:
    name: foo
    storage_class: fred
    placement_group: pg
    size: 1T
    tenant: test
    tenant_space: space_1
    state: present
    issuer_id: key_name
    private_key_file: "az-admin-private-key.pem"

- name: Create new volume based on a volume from the same tenant space
  purestorage.fusion.fusion_volume:
    name: foo
    storage_class: fred
    placement_group: pg
    tenant: test
    tenant_space: space_1
    state: present
    source_volume: "original_volume_name"
    issuer_id: key_name
    private_key_file: "az-admin-private-key.pem"

- name: Create new volume based on a volume snapshot from the same tenant space
  purestorage.fusion.fusion_volume:
    name: foo
    storage_class: fred
    placement_group: pg
    tenant: test
    tenant_space: space_1
    state: present
    source_snapshot: "snap"
    source_volume_snapshot: "vol_snap"
    issuer_id: key_name
    private_key_file: "az-admin-private-key.pem"

- name: Extend the size of an existing volume named foo
  purestorage.fusion.fusion_volume:
    name: foo
    size: 2T
    tenant: test
    tenant_space: space_1
    state: present
    issuer_id: key_name
    private_key_file: "az-admin-private-key.pem"

- name: Delete volume named foo
  purestorage.fusion.fusion_volume:
    name: foo
    tenant: test
    tenant_space: space_1
    state: absent
    issuer_id: key_name
    private_key_file: "az-admin-private-key.pem"
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/Fusion-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/Fusion-Collection)
