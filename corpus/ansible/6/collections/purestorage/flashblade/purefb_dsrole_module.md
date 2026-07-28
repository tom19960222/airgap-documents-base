---
collection: ansible
version: "6"
title: "purestorage.flashblade.purefb_dsrole module – Configure FlashBlade  Management Directory Service Roles"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flashblade/purefb_dsrole_module.html
fetched_at: 2026-07-28T00:18:45+00:00
---
# purestorage.flashblade.purefb_dsrole module – Configure FlashBlade Management Directory Service Roles

> **Note:**
>
> This module is part of the [purestorage.flashblade collection](https://galaxy.ansible.com/purestorage/flashblade) (version 1.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flashblade`.
> You need further requirements to be able to use this module,
> see [Requirements](purefb_dsrole_module.md#ansible-collections-purestorage-flashblade-purefb-dsrole-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_dsrole`.

New in purestorage.flashblade 1.0.0

- [Synopsis](purefb_dsrole_module.md#synopsis)
- [Requirements](purefb_dsrole_module.md#requirements)
- [Parameters](purefb_dsrole_module.md#parameters)
- [Notes](purefb_dsrole_module.md#notes)
- [Examples](purefb_dsrole_module.md#examples)

## [Synopsis](purefb_dsrole_module.md#id1)

- Set or erase directory services role configurations.

## [Requirements](purefb_dsrole_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_dsrole_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **group**  string | Sets the common Name (CN) of the configured directory service group containing users for the FlashBlade. This name should be just the Common Name of the group without the CN= specifier.  Common Names should not exceed 64 characters in length. |
| **group_base**  string | Specifies where the configured group is located in the directory tree. This field consists of Organizational Units (OUs) that combine with the base DN attribute and the configured group CNs to complete the full Distinguished Name of the groups. The group base should specify OU= for each OU and multiple OUs should be separated by commas. The order of OUs is important and should get larger in scope from left to right.  Each OU should not exceed 64 characters in length. |
| **role**  string / required | The directory service role to work on  Choices:   - `"array_admin"` - `"ops_admin"` - `"readonly"` - `"storage_admin"` |
| **state**  string | Create or delete directory service role  Choices:   - `"absent"` - `"present"` ← (default) |

## [Notes](purefb_dsrole_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_dsrole_module.md#id5)

```yaml+jinja
- name: Delete existing array_admin directory service role
  purestorage.flashblade.purefb_dsrole:
    role: array_admin
    state: absent
    fb_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create array_admin directory service role
  purestorage.flashblade.purefb_dsrole:
    role: array_admin
    group_base: "OU=PureGroups,OU=SANManagers"
    group: pureadmins
    fb_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Update ops_admin directory service role
  purestorage.flashblade.purefb_dsrole:
    role: ops_admin
    group_base: "OU=PureGroups"
    group: opsgroup
    fb_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
