---
collection: ansible
version: "8"
title: "community.general.emc_vnx_sg_member module – Manage storage group member on EMC VNX"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/emc_vnx_sg_member_module.html
fetched_at: 2026-07-28T01:45:30+00:00
---
# community.general.emc_vnx_sg_member module – Manage storage group member on EMC VNX

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](emc_vnx_sg_member_module.md#ansible-collections-community-general-emc-vnx-sg-member-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.emc_vnx_sg_member`.

- [Synopsis](emc_vnx_sg_member_module.md#synopsis)
- [Requirements](emc_vnx_sg_member_module.md#requirements)
- [Parameters](emc_vnx_sg_member_module.md#parameters)
- [Attributes](emc_vnx_sg_member_module.md#attributes)
- [Notes](emc_vnx_sg_member_module.md#notes)
- [Examples](emc_vnx_sg_member_module.md#examples)
- [Return Values](emc_vnx_sg_member_module.md#return-values)

## [Synopsis](emc_vnx_sg_member_module.md#id1)

- This module manages the members of an existing storage group.

Aliases: storage.emc.emc_vnx_sg_member

## [Requirements](emc_vnx_sg_member_module.md#id2)

The below requirements are needed on the host that executes this module.

- An EMC VNX Storage device.
- Ansible 2.7.
- storops (0.5.10 or greater). Install using ‘pip install storops’.

## [Parameters](emc_vnx_sg_member_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **lunid**  integer / required | Lun id to be added. |
| **name**  string / required | Name of the Storage group to manage. |
| **sp_address**  string / required | Address of the SP of target/secondary storage. |
| **sp_password**  string | password for accessing SP.  **Default:** `"sysadmin"` |
| **sp_user**  string | Username for accessing SP.  **Default:** `"sysadmin"` |
| **state**  string | Indicates the desired lunid state.  `present` ensures specified lunid is present in the Storage Group.  `absent` ensures specified lunid is absent from Storage Group.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Attributes](emc_vnx_sg_member_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](emc_vnx_sg_member_module.md#id5)

> **Note:**
>
> - The modules prefixed with emc_vnx are built to support the EMC VNX storage platform.

## [Examples](emc_vnx_sg_member_module.md#id6)

```yaml+jinja
- name: Add lun to storage group
  community.general.emc_vnx_sg_member:
    name: sg01
    sp_address: sp1a.fqdn
    sp_user: sysadmin
    sp_password: sysadmin
    lunid: 100
    state: present

- name: Remove lun from storage group
  community.general.emc_vnx_sg_member:
    name: sg01
    sp_address: sp1a.fqdn
    sp_user: sysadmin
    sp_password: sysadmin
    lunid: 100
    state: absent
```

## [Return Values](emc_vnx_sg_member_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hluid**  integer | LUNID that hosts attached to the storage group will see.  **Returned:** success |

### Authors

- Luca ‘remix_tj’ Lorenzetto (@remixtj)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
