---
collection: ansible
version: "8"
title: "purestorage.fusion.fusion_tn module – Manage tenant networks in Pure Storage Fusion"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/fusion/fusion_tn_module.html
fetched_at: 2026-07-28T02:52:48+00:00
---
# purestorage.fusion.fusion_tn module – Manage tenant networks in Pure Storage Fusion

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
> see [Requirements](fusion_tn_module.md#ansible-collections-purestorage-fusion-fusion-tn-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.fusion.fusion_tn`.

New in purestorage.fusion 1.0.0

- [DEPRECATED](fusion_tn_module.md#deprecated)
- [Synopsis](fusion_tn_module.md#synopsis)
- [Requirements](fusion_tn_module.md#requirements)
- [Parameters](fusion_tn_module.md#parameters)
- [Notes](fusion_tn_module.md#notes)
- [Examples](fusion_tn_module.md#examples)
- [Status](fusion_tn_module.md#status)

## [DEPRECATED](fusion_tn_module.md#id1)

Removed in:
:   major release after 2023-07-26

Why:
:   Tenant Networks were removed as a concept in Pure Storage Fusion

Alternative:
:   most of the functionality can be replicated using [purestorage.fusion.fusion_se](fusion_se_module.md#ansible-collections-purestorage-fusion-fusion-se-module) and [purestorage.fusion.fusion_nig](fusion_nig_module.md#ansible-collections-purestorage-fusion-fusion-nig-module)

## [Synopsis](fusion_tn_module.md#id2)

- Create or delete tenant networks in Pure Storage Fusion.

## [Requirements](fusion_tn_module.md#id3)

The below requirements are needed on the host that executes this module.

- python >= 3.8
- purefusion

## [Parameters](fusion_tn_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Access token for Fusion Service  Defaults to the set environment variable under FUSION_ACCESS_TOKEN |
| **addresses**  list / elements=string | List of IP addresses to be used in the subnet of the tenant network.  IP addresses must include a CIDR notation.  IPv4 and IPv6 are fully supported. |
| **availability_zone**  aliases: az  string | The name of the availability zone for the tenant network. |
| **display_name**  string | The human name of the tenant network.  If not provided, defaults to *name*. |
| **gateway**  string | Address of the subnet gateway.  Currently this must be provided. |
| **issuer_id**  aliases: app_id  string | Application ID from Pure1 Registration page  eg. pure1:apikey:dssf2331sd  Defaults to the set environment variable under FUSION_ISSUER_ID |
| **mtu**  integer | MTU setting for the subnet.  **Default:** `1500` |
| **name**  string | The name of the tenant network. |
| **prefix**  string | Network prefix in CIDR format.  This will be deprecated soon. |
| **private_key_file**  aliases: key_file  string | Path to the private key file  Defaults to the set environment variable under FUSION_PRIVATE_KEY_FILE. |
| **private_key_password**  string | Password of the encrypted private key file |
| **provider_subnets**  list / elements=string | List of provider subnets to assign to the tenant networks subnet. |
| **region**  string | The name of the region the availability zone is in |
| **state**  string | Define whether the tenant network should exist or not.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Notes](fusion_tn_module.md#id5)

> **Note:**
>
> - Supports `check_mode`.
> - Currently this only supports a single tenant subnet per tenant network.
> - This module requires the *purefusion* Python library
> - You must set `FUSION_ISSUER_ID` and `FUSION_PRIVATE_KEY_FILE` environment variables if *issuer_id* and *private_key_file* arguments are not passed to the module directly
> - If you want to use access token for authentication, you must use `FUSION_ACCESS_TOKEN` environment variable if *access_token* argument is not passed to the module directly

## [Examples](fusion_tn_module.md#id6)

```yaml+jinja

```

## [Status](fusion_tn_module.md#id7)

- This module will be removed in a major release after 2023-07-26.
  *[deprecated]*
- For more information see [DEPRECATED](fusion_tn_module.md#deprecated).

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/Fusion-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/Fusion-Collection)
