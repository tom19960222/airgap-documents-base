---
collection: ansible
version: "8"
title: "purestorage.flashblade.purefb_syslog module – Configure Pure Storage FlashBlade syslog settings"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flashblade/purefb_syslog_module.html
fetched_at: 2026-07-28T02:52:22+00:00
---
# purestorage.flashblade.purefb_syslog module – Configure Pure Storage FlashBlade syslog settings

> **Note:**
>
> This module is part of the [purestorage.flashblade collection](https://galaxy.ansible.com/ui/repo/published/purestorage/flashblade/) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flashblade`.
> You need further requirements to be able to use this module,
> see [Requirements](purefb_syslog_module.md#ansible-collections-purestorage-flashblade-purefb-syslog-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_syslog`.

New in purestorage.flashblade 1.4.0

- [Synopsis](purefb_syslog_module.md#synopsis)
- [Requirements](purefb_syslog_module.md#requirements)
- [Parameters](purefb_syslog_module.md#parameters)
- [Notes](purefb_syslog_module.md#notes)
- [Examples](purefb_syslog_module.md#examples)

## [Synopsis](purefb_syslog_module.md#id1)

- Configure syslog configuration for Pure Storage FlashBlades.
- Add or delete an individual syslog server to the existing list of serves.

## [Requirements](purefb_syslog_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_syslog_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **address**  string | Syslog server address. This field supports IPv4 or FQDN. An invalid IP addresses will cause the module to fail. No validation is performed for FQDNs. |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **name**  string / required | Unique identifier for the syslog server address |
| **port**  string | Port at which the server is listening. If no port is specified the system will use 514 |
| **protocol**  string | Protocol which server uses  **Choices:**   - `"tcp"` - `"tls"` - `"udp"` |
| **state**  string | Create or delete syslog servers configuration  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Notes](purefb_syslog_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_syslog_module.md#id5)

```yaml+jinja
- name: Delete exisitng syslog server entries
  purestorage.flashblade.purefb_syslog:
    name: syslog1
    state: absent
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Set array syslog servers
  purestorage.flashblade.purefb_syslog:
    state: present
    name: syslog1
    address: syslog1.com
    protocol: udp
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
