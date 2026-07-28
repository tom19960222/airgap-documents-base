---
collection: ansible
version: "6"
title: "purestorage.fusion.fusion_pg module – Manage placement groups in Pure Storage Fusion"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/fusion/fusion_pg_module.html
fetched_at: 2026-07-28T00:19:12+00:00
---
# purestorage.fusion.fusion_pg module – Manage placement groups in Pure Storage Fusion

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
> see [Requirements](fusion_pg_module.md#ansible-collections-purestorage-fusion-fusion-pg-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.fusion.fusion_pg`.

New in purestorage.fusion 1.0.0

- [Synopsis](fusion_pg_module.md#synopsis)
- [Requirements](fusion_pg_module.md#requirements)
- [Parameters](fusion_pg_module.md#parameters)
- [Notes](fusion_pg_module.md#notes)
- [Examples](fusion_pg_module.md#examples)

## [Synopsis](fusion_pg_module.md#id1)

- Create, update or delete a placement groups in Pure Storage Fusion.

## [Requirements](fusion_pg_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.5
- purefusion

## [Parameters](fusion_pg_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **app_id**  string | Application ID from Pure1 Registration page  eg. pure1:apikey:dssf2331sd  Defaults to the set environment variable under FUSION_APP_ID |
| **availability_zone**  aliases: az  string | The name of the availability zone to create the placement group in. |
| **display_name**  string | The human name of the placement group.  If not provided, defaults to *name*. |
| **key_file**  string | Path to the private key file  Defaults to the set environment variable under FUSION_PRIVATE_KEY_FILE. |
| **name**  string / required | The name of the placement group. |
| **placement_engine**  string | For workload placement recommendations from Pure1 Meta, use `pure1meta`.  Please note that this might increase volume creation time.  Choices:   - `"heuristics"` ← (default) - `"pure1meta"` |
| **state**  string | Define whether the placement group should exist or not.  Choices:   - `"absent"` - `"present"` ← (default) |
| **tenant**  string / required | The name of the tenant. |
| **tenant_space**  string / required | The name of the tenant space. |

## [Notes](fusion_pg_module.md#id4)

> **Note:**
>
> - Supports `check mode`.
> - This module requires the *purefusion* Python library
> - You must set `FUSION_APP_ID` and `FUSION_PRIVATE_KEY_FILE` environment variables if *app_id* and *key_file* arguments are not passed to the module directly

## [Examples](fusion_pg_module.md#id5)

```yaml+jinja
- name: Create new placement group named foo
  purestorage.fusion.fusion_pg:
    name: foo
    tenant: test
    tenant_space: space_1
    availability_zone: az1
    placement_engine: pure1meta
    state: present
    app_id: key_name
    key_file: "az-admin-private-key.pem"

- name: Delete placement group foo
  purestorage.fusion.fusion_pg:
    name: foo
    tenant: test
    tenant_space: space_1
    state: absent
    app_id: key_name
    key_file: "az-admin-private-key.pem"
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/Fusion-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/Fusion-Collection)
