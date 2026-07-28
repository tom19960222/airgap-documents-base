---
collection: ansible
version: "8"
title: "purestorage.fusion.fusion_nig module – Manage Network Interface Groups in Pure Storage Fusion"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/fusion/fusion_nig_module.html
fetched_at: 2026-07-28T02:52:38+00:00
---
# purestorage.fusion.fusion_nig module – Manage Network Interface Groups in Pure Storage Fusion

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
> see [Requirements](fusion_nig_module.md#ansible-collections-purestorage-fusion-fusion-nig-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.fusion.fusion_nig`.

New in purestorage.fusion 1.0.0

- [Synopsis](fusion_nig_module.md#synopsis)
- [Requirements](fusion_nig_module.md#requirements)
- [Parameters](fusion_nig_module.md#parameters)
- [Notes](fusion_nig_module.md#notes)
- [Examples](fusion_nig_module.md#examples)

## [Synopsis](fusion_nig_module.md#id1)

- Create, delete and modify network interface groups in Pure Storage Fusion.
- Currently this only supports a single tenant subnet per tenant network

## [Requirements](fusion_nig_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8
- purefusion

## [Parameters](fusion_nig_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Access token for Fusion Service  Defaults to the set environment variable under FUSION_ACCESS_TOKEN |
| **availability_zone**  aliases: az  string / required | The name of the availability zone for the network interface group. |
| **display_name**  string | The human name of the network interface group.  If not provided, defaults to *name*. |
| **gateway**  string | Address of the subnet gateway. Currently must be a valid IPv4 address. |
| **group_type**  string | The type of network interface group.  **Choices:**   - `"eth"` ← (default) |
| **issuer_id**  aliases: app_id  string | Application ID from Pure1 Registration page  eg. pure1:apikey:dssf2331sd  Defaults to the set environment variable under FUSION_ISSUER_ID |
| **mtu**  integer | MTU setting for the subnet.  **Default:** `1500` |
| **name**  string / required | The name of the network interface group. |
| **prefix**  string | Network prefix in CIDR notation. Required to create a new network interface group. Currently only IPv4 addresses with subnet mask are supported. |
| **private_key_file**  aliases: key_file  string | Path to the private key file  Defaults to the set environment variable under FUSION_PRIVATE_KEY_FILE. |
| **private_key_password**  string | Password of the encrypted private key file |
| **region**  string / required | Region for the network interface group. |
| **state**  string | Define whether the network interface group should exist or not.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Notes](fusion_nig_module.md#id4)

> **Note:**
>
> - Supports `check mode`.
> - This module requires the *purefusion* Python library
> - You must set `FUSION_ISSUER_ID` and `FUSION_PRIVATE_KEY_FILE` environment variables if *issuer_id* and *private_key_file* arguments are not passed to the module directly
> - If you want to use access token for authentication, you must use `FUSION_ACCESS_TOKEN` environment variable if *access_token* argument is not passed to the module directly

## [Examples](fusion_nig_module.md#id5)

```yaml+jinja
- name: Create new network interface group foo in AZ bar
  purestorage.fusion.fusion_nig:
    name: foo
    availability_zone: bar
    region: region1
    mtu: 9000
    gateway: 10.21.200.1
    prefix: 10.21.200.0/24
    state: present
    issuer_id: key_name
    private_key_file: "az-admin-private-key.pem"

- name: Delete network interface group foo in AZ bar
  purestorage.fusion.fusion_nig:
    name: foo
    availability_zone: bar
    region: region1
    state: absent
    issuer_id: key_name
    private_key_file: "az-admin-private-key.pem"
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/Fusion-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/Fusion-Collection)
