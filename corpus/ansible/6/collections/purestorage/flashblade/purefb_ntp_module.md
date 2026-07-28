---
collection: ansible
version: "6"
title: "purestorage.flashblade.purefb_ntp module – Configure Pure Storage FlashBlade NTP settings"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flashblade/purefb_ntp_module.html
fetched_at: 2026-07-28T00:18:53+00:00
---
# purestorage.flashblade.purefb_ntp module – Configure Pure Storage FlashBlade NTP settings

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
> see [Requirements](purefb_ntp_module.md#ansible-collections-purestorage-flashblade-purefb-ntp-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_ntp`.

New in purestorage.flashblade 1.0.0

- [Synopsis](purefb_ntp_module.md#synopsis)
- [Requirements](purefb_ntp_module.md#requirements)
- [Parameters](purefb_ntp_module.md#parameters)
- [Notes](purefb_ntp_module.md#notes)
- [Examples](purefb_ntp_module.md#examples)

## [Synopsis](purefb_ntp_module.md#id1)

- Set or erase NTP configuration for Pure Storage FlashBlades.

## [Requirements](purefb_ntp_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_ntp_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **ntp_servers**  list / elements=string | A list of up to 4 alternate NTP servers. These may include IPv4, IPv6 or FQDNs. Invalid IP addresses will cause the module to fail. No validation is performed for FQDNs.  If more than 4 servers are provided, only the first 4 unique nameservers will be used.  if no servers are given a default of *0.pool.ntp.org* will be used. |
| **state**  string | Create or delete NTP servers configuration  Choices:   - `"absent"` - `"present"` ← (default) |

## [Notes](purefb_ntp_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_ntp_module.md#id5)

```yaml+jinja
- name: Delete exisitng NTP server entries
  purestorage.flashblade.purefb_ntp:
    state: absent
    fb_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Set array NTP servers
  purestorage.flashblade.purefb_ntp:
    state: present
    ntp_servers:
      - "0.pool.ntp.org"
      - "1.pool.ntp.org"
      - "2.pool.ntp.org"
      - "3.pool.ntp.org"
    fb_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
