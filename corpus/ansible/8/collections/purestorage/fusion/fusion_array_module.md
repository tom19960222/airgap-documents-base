---
collection: ansible
version: "8"
title: "purestorage.fusion.fusion_array module – Manage arrays in Pure Storage Fusion"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/fusion/fusion_array_module.html
fetched_at: 2026-07-28T02:52:31+00:00
---
# purestorage.fusion.fusion_array module – Manage arrays in Pure Storage Fusion

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
> see [Requirements](fusion_array_module.md#ansible-collections-purestorage-fusion-fusion-array-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.fusion.fusion_array`.

New in purestorage.fusion 1.0.0

- [Synopsis](fusion_array_module.md#synopsis)
- [Requirements](fusion_array_module.md#requirements)
- [Parameters](fusion_array_module.md#parameters)
- [Notes](fusion_array_module.md#notes)
- [Examples](fusion_array_module.md#examples)

## [Synopsis](fusion_array_module.md#id1)

- Create or delete an array in Pure Storage Fusion.

## [Requirements](fusion_array_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8
- purefusion

## [Parameters](fusion_array_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Access token for Fusion Service  Defaults to the set environment variable under FUSION_ACCESS_TOKEN |
| **apartment_id**  string | The Apartment ID of the Array. |
| **appliance_id**  string | Appliance ID of the array. |
| **availability_zone**  aliases: az  string / required | The availability zone the array is located in. |
| **display_name**  string | The human name of the array.  If not provided, defaults to *name*. |
| **hardware_type**  string | Hardware type to which the storage class applies.  **Choices:**   - `"flash-array-x"` - `"flash-array-c"` - `"flash-array-x-optane"` - `"flash-array-xl"` |
| **host_name**  string | Management IP address of the array, or FQDN. |
| **issuer_id**  aliases: app_id  string | Application ID from Pure1 Registration page  eg. pure1:apikey:dssf2331sd  Defaults to the set environment variable under FUSION_ISSUER_ID |
| **maintenance_mode**  boolean | Switch the array into maintenance mode or back. Array in maintenance mode can have placement groups migrated out but not in. Intended use cases are for example safe decommissioning or to prevent use of an array that has not yet been fully configured.  **Choices:**   - `false` - `true` |
| **name**  string / required | The name of the array. |
| **private_key_file**  aliases: key_file  string | Path to the private key file  Defaults to the set environment variable under FUSION_PRIVATE_KEY_FILE. |
| **private_key_password**  string | Password of the encrypted private key file |
| **region**  string / required | The region the AZ is in. |
| **state**  string | Define whether the array should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **unavailable_mode**  boolean | Switch the array into unavailable mode or back. Fusion tries to exclude unavailable arrays from virtually any operation it can. This is to prevent stalling operations in case of e.g. a networking failure. As of the moment arrays have to be marked unavailable manually.  **Choices:**   - `false` - `true` |

## [Notes](fusion_array_module.md#id4)

> **Note:**
>
> - Supports `check mode`.
> - This module requires the *purefusion* Python library
> - You must set `FUSION_ISSUER_ID` and `FUSION_PRIVATE_KEY_FILE` environment variables if *issuer_id* and *private_key_file* arguments are not passed to the module directly
> - If you want to use access token for authentication, you must use `FUSION_ACCESS_TOKEN` environment variable if *access_token* argument is not passed to the module directly

## [Examples](fusion_array_module.md#id5)

```yaml+jinja
- name: Create new array foo
  purestorage.fusion.fusion_array:
    name: foo
    az: zone_1
    region: region1
    hardware_type: flash-array-x
    host_name: foo_array
    display_name: "foo array"
    appliance_id: 1227571-198887878-35016350232000707
    issuer_id: key_name
    private_key_file: "az-admin-private-key.pem"
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/Fusion-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/Fusion-Collection)
