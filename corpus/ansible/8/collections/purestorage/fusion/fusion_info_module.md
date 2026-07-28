---
collection: ansible
version: "8"
title: "purestorage.fusion.fusion_info module – Collect information from Pure Fusion"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/fusion/fusion_info_module.html
fetched_at: 2026-07-28T02:52:35+00:00
---
# purestorage.fusion.fusion_info module – Collect information from Pure Fusion

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
> see [Requirements](fusion_info_module.md#ansible-collections-purestorage-fusion-fusion-info-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.fusion.fusion_info`.

New in purestorage.fusion 1.0.0

- [Synopsis](fusion_info_module.md#synopsis)
- [Requirements](fusion_info_module.md#requirements)
- [Parameters](fusion_info_module.md#parameters)
- [Notes](fusion_info_module.md#notes)
- [Examples](fusion_info_module.md#examples)
- [Return Values](fusion_info_module.md#return-values)

## [Synopsis](fusion_info_module.md#id1)

- Collect information from a Pure Fusion environment.
- By default, the module will collect basic information including counts for arrays, availability_zones, volumes, snapshots . Fleet capacity and data reduction rates are also provided.
- Additional information can be collected based on the configured set of arguments.

## [Requirements](fusion_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8
- purefusion

## [Parameters](fusion_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Access token for Fusion Service  Defaults to the set environment variable under FUSION_ACCESS_TOKEN |
| **gather_subset**  list / elements=string | When supplied, this argument will define the information to be collected. Possible values for this include all, minimum, roles, users, arrays, hardware_types, volumes, host_access_policies, storage_classes, protection_policies, placement_groups, network_interfaces, availability_zones, network_interface_groups, storage_endpoints, snapshots, regions, storage_services, tenants, tenant_spaces, network_interface_groups and api_clients.  **Default:** `["minimum"]` |
| **issuer_id**  aliases: app_id  string | Application ID from Pure1 Registration page  eg. pure1:apikey:dssf2331sd  Defaults to the set environment variable under FUSION_ISSUER_ID |
| **private_key_file**  aliases: key_file  string | Path to the private key file  Defaults to the set environment variable under FUSION_PRIVATE_KEY_FILE. |
| **private_key_password**  string | Password of the encrypted private key file |

## [Notes](fusion_info_module.md#id4)

> **Note:**
>
> - Supports `check mode`.
> - This module requires the *purefusion* Python library
> - You must set `FUSION_ISSUER_ID` and `FUSION_PRIVATE_KEY_FILE` environment variables if *issuer_id* and *private_key_file* arguments are not passed to the module directly
> - If you want to use access token for authentication, you must use `FUSION_ACCESS_TOKEN` environment variable if *access_token* argument is not passed to the module directly

## [Examples](fusion_info_module.md#id5)

```yaml+jinja
- name: Collect default set of information
  purestorage.fusion.fusion_info:
    issuer_id: key_name
    private_key_file: "az-admin-private-key.pem"
    register: fusion_info

- name: Show default information
  ansible.builtin.debug:
    msg: "{{ fusion_info['fusion_info']['default'] }}"

- name: Collect all information
  purestorage.fusion.fusion_info:
    gather_subset:
      - all
    issuer_id: key_name
    private_key_file: "az-admin-private-key.pem"

- name: Show all information
  ansible.builtin.debug:
    msg: "{{ fusion_info['fusion_info'] }}"
```

## [Return Values](fusion_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **fusion_info**  dictionary | Returns the information collected from Fusion  **Returned:** always |

### Authors

- Pure Storage ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/Fusion-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/Fusion-Collection)
