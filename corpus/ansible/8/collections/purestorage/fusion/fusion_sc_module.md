---
collection: ansible
version: "8"
title: "purestorage.fusion.fusion_sc module – Manage storage classes in Pure Storage Fusion"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/fusion/fusion_sc_module.html
fetched_at: 2026-07-28T02:52:43+00:00
---
# purestorage.fusion.fusion_sc module – Manage storage classes in Pure Storage Fusion

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
> see [Requirements](fusion_sc_module.md#ansible-collections-purestorage-fusion-fusion-sc-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.fusion.fusion_sc`.

New in purestorage.fusion 1.0.0

- [Synopsis](fusion_sc_module.md#synopsis)
- [Requirements](fusion_sc_module.md#requirements)
- [Parameters](fusion_sc_module.md#parameters)
- [Notes](fusion_sc_module.md#notes)
- [Examples](fusion_sc_module.md#examples)

## [Synopsis](fusion_sc_module.md#id1)

- Manage a storage class in Pure Storage Fusion.

## [Requirements](fusion_sc_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8
- purefusion

## [Parameters](fusion_sc_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Access token for Fusion Service  Defaults to the set environment variable under FUSION_ACCESS_TOKEN |
| **bw_limit**  string | The bandwidth limit in M or G units. M will set MB/s. G will set GB/s.  Must be between 1MB/s and 512GB/s.  If not provided at creation, this will default to 512GB/s. |
| **display_name**  string | The human name of the storage class.  If not provided, defaults to *name*. |
| **iops_limit**  string | The IOPs limit - use value or K or M. K will mean 1000. M will mean 1000000.  Must be between 100 and 100000000.  If not provided at creation, this will default to 100000000. |
| **issuer_id**  aliases: app_id  string | Application ID from Pure1 Registration page  eg. pure1:apikey:dssf2331sd  Defaults to the set environment variable under FUSION_ISSUER_ID |
| **name**  string / required | The name of the storage class. |
| **private_key_file**  aliases: key_file  string | Path to the private key file  Defaults to the set environment variable under FUSION_PRIVATE_KEY_FILE. |
| **private_key_password**  string | Password of the encrypted private key file |
| **size_limit**  string | Volume size limit in M, G, T or P units.  Must be between 1MB and 4PB.  If not provided at creation, this will default to 4PB. |
| **state**  string | Define whether the storage class should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **storage_service**  string / required | Storage service to which the storage class belongs. |

## [Notes](fusion_sc_module.md#id4)

> **Note:**
>
> - Supports `check_mode`.
> - It is not currently possible to update bw_limit or iops_limit after a storage class has been created.
> - This module requires the *purefusion* Python library
> - You must set `FUSION_ISSUER_ID` and `FUSION_PRIVATE_KEY_FILE` environment variables if *issuer_id* and *private_key_file* arguments are not passed to the module directly
> - If you want to use access token for authentication, you must use `FUSION_ACCESS_TOKEN` environment variable if *access_token* argument is not passed to the module directly

## [Examples](fusion_sc_module.md#id5)

```yaml+jinja
- name: Create new storage class foo
  purestorage.fusion.fusion_sc:
    name: foo
    size_limit: 100G
    iops_limit: 100000
    bw_limit: 25M
    storage_service: service1
    display_name: "test class"
    issuer_id: key_name
    private_key_file: "az-admin-private-key.pem"

- name: Update storage class (only display_name change is supported)
  purestorage.fusion.fusion_sc:
    name: foo
    display_name: "main class"
    storage_service: service1
    issuer_id: key_name
    private_key_file: "az-admin-private-key.pem"

- name: Delete storage class
  purestorage.fusion.fusion_sc:
    name: foo
    storage_service: service1
    state: absent
    issuer_id: key_name
    private_key_file: "az-admin-private-key.pem"
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/Fusion-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/Fusion-Collection)
