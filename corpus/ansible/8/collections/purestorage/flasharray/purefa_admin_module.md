---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_admin module – Configure Pure Storage FlashArray Global Admin settings"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_admin_module.html
fetched_at: 2026-07-28T02:50:35+00:00
---
# purestorage.flasharray.purefa_admin module – Configure Pure Storage FlashArray Global Admin settings

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
> see [Requirements](purefa_admin_module.md#ansible-collections-purestorage-flasharray-purefa-admin-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_admin`.

New in purestorage.flasharray 1.12.0

- [Synopsis](purefa_admin_module.md#synopsis)
- [Requirements](purefa_admin_module.md#requirements)
- [Parameters](purefa_admin_module.md#parameters)
- [Notes](purefa_admin_module.md#notes)
- [Examples](purefa_admin_module.md#examples)

## [Synopsis](purefa_admin_module.md#id1)

- Set global admin settings for the FlashArray

## [Requirements](purefa_admin_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_admin_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **lockout**  integer | Account lockout duration, in seconds, after max_login exceeded  Range between 1 second and 90 days (7776000 seconds) |
| **max_login**  integer | Maximum number of failed logins before account is locked |
| **min_password**  integer | Minimum user password length  **Default:** `1` |
| **sso**  boolean | Enable or disable the array Signle Sign-On from Pure1 Manage  **Choices:**   - `false` ← (default) - `true` |

## [Notes](purefa_admin_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_admin_module.md#id5)

```yaml+jinja
- name: Set global login parameters
  purestorage.flasharray.purefa_admin:
    sso: false
    max_login: 5
    min_password: 10
    lockout: 300
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
