---
collection: ansible
version: "8"
title: "purestorage.fusion.fusion_az module – Create Availability Zones in Pure Storage Fusion"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/fusion/fusion_az_module.html
fetched_at: 2026-07-28T02:52:32+00:00
---
# purestorage.fusion.fusion_az module – Create Availability Zones in Pure Storage Fusion

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
> see [Requirements](fusion_az_module.md#ansible-collections-purestorage-fusion-fusion-az-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.fusion.fusion_az`.

New in purestorage.fusion 1.0.0

- [Synopsis](fusion_az_module.md#synopsis)
- [Requirements](fusion_az_module.md#requirements)
- [Parameters](fusion_az_module.md#parameters)
- [Notes](fusion_az_module.md#notes)
- [Examples](fusion_az_module.md#examples)

## [Synopsis](fusion_az_module.md#id1)

- Manage an Availability Zone in Pure Storage Fusion.

## [Requirements](fusion_az_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8
- purefusion

## [Parameters](fusion_az_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Access token for Fusion Service  Defaults to the set environment variable under FUSION_ACCESS_TOKEN |
| **display_name**  string | The human name of the Availability Zone.  If not provided, defaults to *name*. |
| **issuer_id**  aliases: app_id  string | Application ID from Pure1 Registration page  eg. pure1:apikey:dssf2331sd  Defaults to the set environment variable under FUSION_ISSUER_ID |
| **name**  string / required | The name of the Availability Zone. |
| **private_key_file**  aliases: key_file  string | Path to the private key file  Defaults to the set environment variable under FUSION_PRIVATE_KEY_FILE. |
| **private_key_password**  string | Password of the encrypted private key file |
| **region**  string / required | Region within which the AZ is created. |
| **state**  string | Define whether the Availability Zone should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](fusion_az_module.md#id4)

> **Note:**
>
> - Supports `check mode`.
> - This module requires the *purefusion* Python library
> - You must set `FUSION_ISSUER_ID` and `FUSION_PRIVATE_KEY_FILE` environment variables if *issuer_id* and *private_key_file* arguments are not passed to the module directly
> - If you want to use access token for authentication, you must use `FUSION_ACCESS_TOKEN` environment variable if *access_token* argument is not passed to the module directly

## [Examples](fusion_az_module.md#id5)

```yaml+jinja
- name: Create new AZ foo
  purestorage.fusion.fusion_az:
    name: foo
    display_name: "foo AZ"
    region: region1
    issuer_id: key_name
    private_key_file: "az-admin-private-key.pem"

- name: Delete AZ foo
  purestorage.fusion.fusion_az:
    name: foo
    state: absent
    region: region1
    issuer_id: key_name
    private_key_file: "az-admin-private-key.pem"
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/Fusion-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/Fusion-Collection)
