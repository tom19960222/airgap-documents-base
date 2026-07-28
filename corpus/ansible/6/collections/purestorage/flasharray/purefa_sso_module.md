---
collection: ansible
version: "6"
title: "purestorage.flasharray.purefa_sso module – Configure Pure Storage FlashArray Single Sign-On"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flasharray/purefa_sso_module.html
fetched_at: 2026-07-28T00:18:29+00:00
---
# purestorage.flasharray.purefa_sso module – Configure Pure Storage FlashArray Single Sign-On

> **Note:**
>
> This module is part of the [purestorage.flasharray collection](https://galaxy.ansible.com/purestorage/flasharray) (version 1.15.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flasharray`.
> You need further requirements to be able to use this module,
> see [Requirements](purefa_sso_module.md#ansible-collections-purestorage-flasharray-purefa-sso-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_sso`.

New in purestorage.flasharray 1.9.0

- [DEPRECATED](purefa_sso_module.md#deprecated)
- [Synopsis](purefa_sso_module.md#synopsis)
- [Requirements](purefa_sso_module.md#requirements)
- [Parameters](purefa_sso_module.md#parameters)
- [Notes](purefa_sso_module.md#notes)
- [Examples](purefa_sso_module.md#examples)
- [Status](purefa_sso_module.md#status)

## [DEPRECATED](purefa_sso_module.md#id1)

Removed in:
:   version 2.0.0

Why:
:   Superceeded by [purestorage.flasharray.purefa_admin](purefa_admin_module.md#ansible-collections-purestorage-flasharray-purefa-admin-module)

Alternative:
:   Use [purestorage.flasharray.purefa_admin](purefa_admin_module.md#ansible-collections-purestorage-flasharray-purefa-admin-module) instead.

## [Synopsis](purefa_sso_module.md#id2)

- Enable or disable Single Sign-On (SSO) to give LDAP users the ability to navigate seamlessly from Pure1 Manage to the current array through a single login.

## [Requirements](purefa_sso_module.md#id3)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_sso_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **state**  string | Enable or disable the array Signle Sign-On from Pure1 Manage  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](purefa_sso_module.md#id5)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_sso_module.md#id6)

```yaml+jinja
- name: Enable SSO
  purestorage.flasharray.purefa_sso:
    state: present
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Disable SSO
  purestorage.flasharray.purefa_sso:
    state: absent
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
```

## [Status](purefa_sso_module.md#id7)

- This module will be removed in version 2.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](purefa_sso_module.md#deprecated).

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
[Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
[Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
[Communication](index.md#communication-for-purestorage-flasharray)
