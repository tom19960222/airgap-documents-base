---
collection: ansible
version: "8"
title: "purestorage.fusion.fusion_hw module – Create hardware types in Pure Storage Fusion"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/fusion/fusion_hw_module.html
fetched_at: 2026-07-28T02:52:34+00:00
---
# purestorage.fusion.fusion_hw module – Create hardware types in Pure Storage Fusion

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
> see [Requirements](fusion_hw_module.md#ansible-collections-purestorage-fusion-fusion-hw-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.fusion.fusion_hw`.

New in purestorage.fusion 1.0.0

- [DEPRECATED](fusion_hw_module.md#deprecated)
- [Synopsis](fusion_hw_module.md#synopsis)
- [Requirements](fusion_hw_module.md#requirements)
- [Parameters](fusion_hw_module.md#parameters)
- [Notes](fusion_hw_module.md#notes)
- [Examples](fusion_hw_module.md#examples)
- [Status](fusion_hw_module.md#status)

## [DEPRECATED](fusion_hw_module.md#id1)

Removed in:
:   major release after 2023-08-09

Why:
:   Hardware type cannot be modified in Pure Storage Fusion

Alternative:
:   there’s no alternative as this functionality has never worked before

## [Synopsis](fusion_hw_module.md#id2)

- Create a hardware type in Pure Storage Fusion.

## [Requirements](fusion_hw_module.md#id3)

The below requirements are needed on the host that executes this module.

- python >= 3.8
- purefusion

## [Parameters](fusion_hw_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Access token for Fusion Service  Defaults to the set environment variable under FUSION_ACCESS_TOKEN |
| **array_type**  string | The array type for the hardware type.  **Choices:**   - `"FA//X"` - `"FA//C"` |
| **display_name**  string | The human name of the hardware type.  If not provided, defaults to *name*. |
| **issuer_id**  aliases: app_id  string | Application ID from Pure1 Registration page  eg. pure1:apikey:dssf2331sd  Defaults to the set environment variable under FUSION_ISSUER_ID |
| **media_type**  string | Volume size limit in M, G, T or P units. |
| **name**  string | The name of the hardware type. |
| **private_key_file**  aliases: key_file  string | Path to the private key file  Defaults to the set environment variable under FUSION_PRIVATE_KEY_FILE. |
| **private_key_password**  string | Password of the encrypted private key file |
| **state**  string | Define whether the hardware type should exist or not.  Currently there is no mechanism to delete a hardware type.  **Choices:**   - `"present"` ← (default) |

## [Notes](fusion_hw_module.md#id5)

> **Note:**
>
> - Supports `check mode`.
> - This module requires the *purefusion* Python library
> - You must set `FUSION_ISSUER_ID` and `FUSION_PRIVATE_KEY_FILE` environment variables if *issuer_id* and *private_key_file* arguments are not passed to the module directly
> - If you want to use access token for authentication, you must use `FUSION_ACCESS_TOKEN` environment variable if *access_token* argument is not passed to the module directly

## [Examples](fusion_hw_module.md#id6)

```yaml+jinja

```

## [Status](fusion_hw_module.md#id7)

- This module will be removed in a major release after 2023-08-09.
  *[deprecated]*
- For more information see [DEPRECATED](fusion_hw_module.md#deprecated).

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/Fusion-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/Fusion-Collection)
