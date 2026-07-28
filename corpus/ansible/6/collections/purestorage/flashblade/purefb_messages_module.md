---
collection: ansible
version: "6"
title: "purestorage.flashblade.purefb_messages module – List FlashBlade Alert Messages"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flashblade/purefb_messages_module.html
fetched_at: 2026-07-28T00:18:52+00:00
---
# purestorage.flashblade.purefb_messages module – List FlashBlade Alert Messages

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
> see [Requirements](purefb_messages_module.md#ansible-collections-purestorage-flashblade-purefb-messages-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_messages`.

New in purestorage.flashblade 1.10.0

- [Synopsis](purefb_messages_module.md#synopsis)
- [Requirements](purefb_messages_module.md#requirements)
- [Parameters](purefb_messages_module.md#parameters)
- [Notes](purefb_messages_module.md#notes)
- [Examples](purefb_messages_module.md#examples)

## [Synopsis](purefb_messages_module.md#id1)

- List Alert messages based on filters provided

## [Requirements](purefb_messages_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_messages_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **flagged**  boolean | Show alerts that have been acknowledged or not  Choices:   - `false` ← (default) - `true` |
| **history**  string | Historical time period to show alerts for, from present time  Allowed time period are hour(h), day(d), week(w) and year(y)  Default: `"1w"` |
| **severity**  list / elements=string | severity of the alerts to show  Choices:   - `"all"` ← (default) - `"critical"` - `"warning"` - `"info"`   Default: `["all"]` |
| **state**  string | State of alerts to show  Choices:   - `"all"` - `"open"` ← (default) - `"closed"` |

## [Notes](purefb_messages_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_messages_module.md#id5)

```yaml+jinja
- name: Show critical alerts from past 4 weeks that haven't been acknowledged
  purefb_messages:
    history: 4w
    flagged : False
    severity:
    - critical
    fb_url: 10.10.10.2
    api_token: T-68618f31-0c9e-4e57-aa44-5306a2cf10e3
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
