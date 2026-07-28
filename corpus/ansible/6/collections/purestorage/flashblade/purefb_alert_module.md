---
collection: ansible
version: "6"
title: "purestorage.flashblade.purefb_alert module – Configure Pure Storage FlashBlade alert email settings"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flashblade/purefb_alert_module.html
fetched_at: 2026-07-28T00:18:38+00:00
---
# purestorage.flashblade.purefb_alert module – Configure Pure Storage FlashBlade alert email settings

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
> see [Requirements](purefb_alert_module.md#ansible-collections-purestorage-flashblade-purefb-alert-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_alert`.

New in purestorage.flashblade 1.0.0

- [Synopsis](purefb_alert_module.md#synopsis)
- [Requirements](purefb_alert_module.md#requirements)
- [Parameters](purefb_alert_module.md#parameters)
- [Notes](purefb_alert_module.md#notes)
- [Examples](purefb_alert_module.md#examples)

## [Synopsis](purefb_alert_module.md#id1)

- Configure alert email configuration for Pure Storage FlashArrays.
- Add or delete an individual syslog server to the existing list of serves.

## [Requirements](purefb_alert_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_alert_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **address**  string / required | Email address (valid format required) |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **enabled**  boolean | Set specified email address to be enabled or disabled  Choices:   - `false` - `true` ← (default) |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **severity**  string | The minimum severity that an alert must have in order for emails to be sent to the array’s alert watchers  Choices:   - `"info"` ← (default) - `"warning"` - `"critical"` |
| **state**  string | Create or delete alert email  Choices:   - `"absent"` - `"present"` ← (default) |

## [Notes](purefb_alert_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_alert_module.md#id5)

```yaml+jinja
- name: Add new email recipient and enable, or enable existing email
  purestorage.flashblade.purefb_alert:
    address: "user@domain.com"
    enabled: true
    state: present
    fb_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
- name: Delete existing email recipient
  purestorage.flashblade.purefb_alert:
    state: absent
    address: "user@domain.com"
    fb_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
