---
collection: ansible
version: "6"
title: "purestorage.flasharray.purefa_alert module – Configure Pure Storage FlashArray alert email settings"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flasharray/purefa_alert_module.html
fetched_at: 2026-07-28T00:18:01+00:00
---
# purestorage.flasharray.purefa_alert module – Configure Pure Storage FlashArray alert email settings

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
> see [Requirements](purefa_alert_module.md#ansible-collections-purestorage-flasharray-purefa-alert-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_alert`.

New in purestorage.flasharray 1.0.0

- [Synopsis](purefa_alert_module.md#synopsis)
- [Requirements](purefa_alert_module.md#requirements)
- [Parameters](purefa_alert_module.md#parameters)
- [Notes](purefa_alert_module.md#notes)
- [Examples](purefa_alert_module.md#examples)

## [Synopsis](purefa_alert_module.md#id1)

- Configure alert email configuration for Pure Storage FlashArrays.

## [Requirements](purefa_alert_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_alert_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **address**  string / required | Email address (valid format required) |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **enabled**  boolean | Set specified email address to be enabled or disabled  Choices:   - `false` - `true` ← (default) |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **state**  string | Create or delete alert email  Choices:   - `"absent"` - `"present"` ← (default) |

## [Notes](purefa_alert_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_alert_module.md#id5)

```yaml+jinja
- name: Add new email recipient and enable, or enable existing email
  purestorage.flasharray.purefa_alert:
    address: "user@domain.com"
    enabled: true
    state: present
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
- name: Delete existing email recipient
  purestorage.flasharray.purefa_alert:
    state: absent
    address: "user@domain.com"
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
[Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
[Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
[Communication](index.md#communication-for-purestorage-flasharray)
