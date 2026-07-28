---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_dsrole module – Configure FlashArray Directory Service Roles"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_dsrole_module.html
fetched_at: 2026-07-28T02:50:51+00:00
---
# purestorage.flasharray.purefa_dsrole module – Configure FlashArray Directory Service Roles

> **Note:**
>
> This module is part of the [purestorage.flasharray collection](https://galaxy.ansible.com/ui/repo/published/purestorage/flasharray/) (version 1.24.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flasharray`.
> You need further requirements to be able to use this module,
> see [Requirements](purefa_dsrole_module.md#ansible-collections-purestorage-flasharray-purefa-dsrole-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_dsrole`.

New in purestorage.flasharray 1.0.0

- [Synopsis](purefa_dsrole_module.md#synopsis)
- [Requirements](purefa_dsrole_module.md#requirements)
- [Parameters](purefa_dsrole_module.md#parameters)
- [Notes](purefa_dsrole_module.md#notes)
- [Examples](purefa_dsrole_module.md#examples)

## [Synopsis](purefa_dsrole_module.md#id1)

- Set or erase directory services role configurations.
- Only available for FlashArray running Purity 5.2.0 or higher

## [Requirements](purefa_dsrole_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_dsrole_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **group**  string | Sets the common Name (CN) of the configured directory service group containing users for the FlashBlade. This name should be just the Common Name of the group without the CN= specifier.  Common Names should not exceed 64 characters in length. |
| **group_base**  string | Specifies where the configured group is located in the directory tree. This field consists of Organizational Units (OUs) that combine with the base DN attribute and the configured group CNs to complete the full Distinguished Name of the groups. The group base should specify OU= for each OU and multiple OUs should be separated by commas. The order of OUs is important and should get larger in scope from left to right.  Each OU should not exceed 64 characters in length. |
| **role**  string / required | The directory service role to work on  **Choices:**   - `"array_admin"` - `"ops_admin"` - `"readonly"` - `"storage_admin"` |
| **state**  string | Create or delete directory service role  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Notes](purefa_dsrole_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_dsrole_module.md#id5)

```yaml+jinja
- name: Delete exisitng array_admin directory service role
  purestorage.flasharray.purefa_dsrole:
    role: array_admin
    state: absent
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create array_admin directory service role
  purestorage.flasharray.purefa_dsrole:
    role: array_admin
    group_base: "OU=PureGroups,OU=SANManagers"
    group: pureadmins
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Update ops_admin directory service role
  purestorage.flasharray.purefa_dsrole:
    role: ops_admin
    group_base: "OU=PureGroups"
    group: opsgroup
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
- [Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
- [Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
- [Communication](index.md#communication-for-purestorage-flasharray)
