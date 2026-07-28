---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_maintenance module – Configure Pure Storage FlashArray Maintence Windows"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_maintenance_module.html
fetched_at: 2026-07-28T02:51:05+00:00
---
# purestorage.flasharray.purefa_maintenance module – Configure Pure Storage FlashArray Maintence Windows

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
> see [Requirements](purefa_maintenance_module.md#ansible-collections-purestorage-flasharray-purefa-maintenance-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_maintenance`.

New in purestorage.flasharray 1.7.0

- [Synopsis](purefa_maintenance_module.md#synopsis)
- [Requirements](purefa_maintenance_module.md#requirements)
- [Parameters](purefa_maintenance_module.md#parameters)
- [Notes](purefa_maintenance_module.md#notes)
- [Examples](purefa_maintenance_module.md#examples)

## [Synopsis](purefa_maintenance_module.md#id1)

- Configuration for Pure Storage FlashArray Maintenance Windows.

## [Requirements](purefa_maintenance_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_maintenance_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **state**  string | Create or delete maintennance window  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **timeout**  integer | Maintenance window period, specified in seconds.  Range allowed is 1 minute (60 seconds) to 24 hours (86400 seconds)  Default setting is 1 hour (3600 seconds)  **Default:** `3600` |

## [Notes](purefa_maintenance_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_maintenance_module.md#id5)

```yaml+jinja
- name: Delete exisitng maintenance window
  purestorage.flasharray.purefa_maintenance:
    state: absent
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Set maintnence window to default of 1 hour
  purestorage.flasharray.purefa_maintenance:
    state: present
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Update existing maintnence window
  purestorage.flasharray.purefa_maintenance:
    state: present
    timeout: 86400
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
