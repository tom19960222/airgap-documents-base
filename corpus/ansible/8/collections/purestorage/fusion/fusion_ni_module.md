---
collection: ansible
version: "8"
title: "purestorage.fusion.fusion_ni module – Manage network interfaces in Pure Storage Fusion"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/fusion/fusion_ni_module.html
fetched_at: 2026-07-28T02:52:37+00:00
---
# purestorage.fusion.fusion_ni module – Manage network interfaces in Pure Storage Fusion

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
> see [Requirements](fusion_ni_module.md#ansible-collections-purestorage-fusion-fusion-ni-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.fusion.fusion_ni`.

New in purestorage.fusion 1.0.0

- [Synopsis](fusion_ni_module.md#synopsis)
- [Requirements](fusion_ni_module.md#requirements)
- [Parameters](fusion_ni_module.md#parameters)
- [Notes](fusion_ni_module.md#notes)
- [Examples](fusion_ni_module.md#examples)

## [Synopsis](fusion_ni_module.md#id1)

- Update parameters of network interfaces in Pure Storage Fusion.

## [Requirements](fusion_ni_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8
- purefusion

## [Parameters](fusion_ni_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Access token for Fusion Service  Defaults to the set environment variable under FUSION_ACCESS_TOKEN |
| **array**  string / required | The name of the array the network interface belongs to. |
| **availability_zone**  aliases: az  string / required | The name of the availability zone for the network interface. |
| **display_name**  string | The human name of the network interface.  If not provided, defaults to *name*. |
| **enabled**  boolean | True if network interface is in use.  **Choices:**   - `false` - `true` |
| **eth**  string | The IP address associated with the network interface.  IP address must include a CIDR notation.  Only IPv4 is supported at the moment.  Required together with `network_interface_group` parameter. |
| **issuer_id**  aliases: app_id  string | Application ID from Pure1 Registration page  eg. pure1:apikey:dssf2331sd  Defaults to the set environment variable under FUSION_ISSUER_ID |
| **name**  string / required | The name of the network interface. |
| **network_interface_group**  string | The name of the network interface group this network interface belongs to. |
| **private_key_file**  aliases: key_file  string | Path to the private key file  Defaults to the set environment variable under FUSION_PRIVATE_KEY_FILE. |
| **private_key_password**  string | Password of the encrypted private key file |
| **region**  string / required | The name of the region the availability zone is in. |

## [Notes](fusion_ni_module.md#id4)

> **Note:**
>
> - Supports `check_mode`.
> - This module requires the *purefusion* Python library
> - You must set `FUSION_ISSUER_ID` and `FUSION_PRIVATE_KEY_FILE` environment variables if *issuer_id* and *private_key_file* arguments are not passed to the module directly
> - If you want to use access token for authentication, you must use `FUSION_ACCESS_TOKEN` environment variable if *access_token* argument is not passed to the module directly

## [Examples](fusion_ni_module.md#id5)

```yaml+jinja
- name: Patch network interface
  purestorage.fusion.fusion_ni:
    name: foo
    region: us-west
    availability_zone: bar
    array: array0
    eth: 10.21.200.124/24
    enabled: true
    network_interface_group: subnet-0
    issuer_id: key_name
    private_key_file: "az-admin-private-key.pem"
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/Fusion-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/Fusion-Collection)
