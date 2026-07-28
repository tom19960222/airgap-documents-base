---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_messages module – List FlashArray Alert Messages"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_messages_module.html
fetched_at: 2026-07-28T02:51:06+00:00
---
# purestorage.flasharray.purefa_messages module – List FlashArray Alert Messages

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
> see [Requirements](purefa_messages_module.md#ansible-collections-purestorage-flasharray-purefa-messages-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_messages`.

New in purestorage.flasharray 1.14.0

- [Synopsis](purefa_messages_module.md#synopsis)
- [Requirements](purefa_messages_module.md#requirements)
- [Parameters](purefa_messages_module.md#parameters)
- [Notes](purefa_messages_module.md#notes)
- [Examples](purefa_messages_module.md#examples)

## [Synopsis](purefa_messages_module.md#id1)

- List Alert messages based on filters provided

## [Requirements](purefa_messages_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_messages_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **flagged**  boolean | Show alerts that have been acknowledged or not  **Choices:**   - `false` ← (default) - `true` |
| **history**  string | Historical time period to show alerts for, from present time  Allowed time period are hour(h), day(d), week(w) and year(y)  **Default:** `"1w"` |
| **severity**  string | severity of the alerts to show  **Choices:**   - `"critical"` - `"warning"` - `"info"` ← (default) |
| **state**  string | State of alerts to show  **Choices:**   - `"open"` ← (default) - `"closed"` |

## [Notes](purefa_messages_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_messages_module.md#id5)

```yaml+jinja
- name: Show critical alerts from past 4 weeks that haven't been acknowledged
  purefa_messages:
    history: 4w
    flagged : false
    severity: critical
    fa_url: 10.10.10.2
    api_token: 89a9356f-c203-d263-8a89-c229486a13ba
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
- [Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
- [Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
- [Communication](index.md#communication-for-purestorage-flasharray)
