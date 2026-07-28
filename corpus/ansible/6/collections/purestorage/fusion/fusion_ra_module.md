---
collection: ansible
version: "6"
title: "purestorage.fusion.fusion_ra module – Manage role assignments in Pure Storage Fusion"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/fusion/fusion_ra_module.html
fetched_at: 2026-07-28T00:19:13+00:00
---
# purestorage.fusion.fusion_ra module – Manage role assignments in Pure Storage Fusion

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
> see [Requirements](fusion_ra_module.md#ansible-collections-purestorage-fusion-fusion-ra-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.fusion.fusion_ra`.

New in purestorage.fusion 1.0.0

- [Synopsis](fusion_ra_module.md#synopsis)
- [Requirements](fusion_ra_module.md#requirements)
- [Parameters](fusion_ra_module.md#parameters)
- [Notes](fusion_ra_module.md#notes)
- [Examples](fusion_ra_module.md#examples)

## [Synopsis](fusion_ra_module.md#id1)

- Create or delete a storage class in Pure Storage Fusion.

## [Requirements](fusion_ra_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.5
- purefusion

## [Parameters](fusion_ra_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **app_id**  string | Application ID from Pure1 Registration page  eg. pure1:apikey:dssf2331sd  Defaults to the set environment variable under FUSION_APP_ID |
| **key_file**  string | Path to the private key file  Defaults to the set environment variable under FUSION_PRIVATE_KEY_FILE. |
| **name**  string / required | The name of the role to be assigned/unassigned. |
| **scope**  string | The level to which the role is assigned.  Choices:   - `"organization"` ← (default) - `"tenant"` - `"tenant_space"` |
| **state**  string | Define whether the role assingment should exist or not.  Choices:   - `"absent"` - `"present"` ← (default) |
| **tenant**  string | The name of the tenant the user has the role applied to.  Must be provided if *scope* is set to either `tenant` or `tenant_space`. |
| **tenant_space**  string | The name of the tenant_space the user has the role applied to.  Must be provided if *scope* is set to `tenant_space`. |
| **user**  string / required | The username to assign the role to.  Currently this only supports the Pure1 App ID.  This should be provide in the same format as *app_id*. |

## [Notes](fusion_ra_module.md#id4)

> **Note:**
>
> - Supports `check mode`.
> - This module requires the *purefusion* Python library
> - You must set `FUSION_APP_ID` and `FUSION_PRIVATE_KEY_FILE` environment variables if *app_id* and *key_file* arguments are not passed to the module directly

## [Examples](fusion_ra_module.md#id5)

```yaml+jinja
- name: Assign role foo to user in tenant bar
  purestorage.fusion.fusion_ra:
    name: foo
    user: key_name
    tenant: bar
    app_id: key_name
    key_file: "az-admin-private-key.pem"

- name: Delete role foo from user in tenant bar
  purestorage.fusion.fusion_ra:
    name: foo
    user: key_name
    tenant: bar
    state: absent
    app_id: key_name
    key_file: "az-admin-private-key.pem"
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/Fusion-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/Fusion-Collection)
