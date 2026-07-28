---
collection: ansible
version: "6"
title: "purestorage.fusion.fusion_ss module – Manage storage services in Pure Storage Fusion"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/fusion/fusion_ss_module.html
fetched_at: 2026-07-28T00:19:15+00:00
---
# purestorage.fusion.fusion_ss module – Manage storage services in Pure Storage Fusion

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
> see [Requirements](fusion_ss_module.md#ansible-collections-purestorage-fusion-fusion-ss-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.fusion.fusion_ss`.

New in purestorage.fusion 1.0.0

- [Synopsis](fusion_ss_module.md#synopsis)
- [Requirements](fusion_ss_module.md#requirements)
- [Parameters](fusion_ss_module.md#parameters)
- [Notes](fusion_ss_module.md#notes)
- [Examples](fusion_ss_module.md#examples)

## [Synopsis](fusion_ss_module.md#id1)

- Manage a storage services in Pure Storage Fusion.

## [Requirements](fusion_ss_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.5
- purefusion

## [Parameters](fusion_ss_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **app_id**  string | Application ID from Pure1 Registration page  eg. pure1:apikey:dssf2331sd  Defaults to the set environment variable under FUSION_APP_ID |
| **display_name**  string | The human name of the storage service.  If not provided, defaults to *name*. |
| **hardware_types**  list / elements=string / required | Hardware types to which the storage service applies.  Choices:   - `"flash-array-x"` - `"flash-array-c"` - `"flash-array-x-optane"` - `"flash-array-xl"` |
| **key_file**  string | Path to the private key file  Defaults to the set environment variable under FUSION_PRIVATE_KEY_FILE. |
| **name**  string / required | The name of the storage service. |
| **state**  string | Define whether the storage service should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](fusion_ss_module.md#id4)

> **Note:**
>
> - Supports `check mode`.
> - This module requires the *purefusion* Python library
> - You must set `FUSION_APP_ID` and `FUSION_PRIVATE_KEY_FILE` environment variables if *app_id* and *key_file* arguments are not passed to the module directly

## [Examples](fusion_ss_module.md#id5)

```yaml+jinja
- name: Create new storage service foo
  purestorage.fusion.fusion_ss:
    name: foo
    hardware_type:
    - flash-array-x
    - flash-array-x-optane
    display_name: "test class"
    app_id: key_name
    key_file: "az-admin-private-key.pem"

- name: Update storage service
  purestorage.fusion.fusion_ss:
    name: foo
    display_name: "main class"
    hardware_types:
    - flash-array-c
    app_id: key_name
    key_file: "az-admin-private-key.pem"

- name: Delete storage service
  purestorage.fusion.fusion_ss:
    name: foo
    state: absent
    app_id: key_name
    key_file: "az-admin-private-key.pem"
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/Fusion-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/Fusion-Collection)
