---
collection: ansible
version: "6"
title: "purestorage.flasharray.purefa_ntp module – Configure Pure Storage FlashArray NTP settings"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flasharray/purefa_ntp_module.html
fetched_at: 2026-07-28T00:18:19+00:00
---
# purestorage.flasharray.purefa_ntp module – Configure Pure Storage FlashArray NTP settings

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
> see [Requirements](purefa_ntp_module.md#ansible-collections-purestorage-flasharray-purefa-ntp-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_ntp`.

New in purestorage.flasharray 1.0.0

- [Synopsis](purefa_ntp_module.md#synopsis)
- [Requirements](purefa_ntp_module.md#requirements)
- [Parameters](purefa_ntp_module.md#parameters)
- [Notes](purefa_ntp_module.md#notes)
- [Examples](purefa_ntp_module.md#examples)

## [Synopsis](purefa_ntp_module.md#id1)

- Set or erase NTP configuration for Pure Storage FlashArrays.

## [Requirements](purefa_ntp_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_ntp_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **ntp_servers**  list / elements=string | A list of up to 4 alternate NTP servers. These may include IPv4, IPv6 or FQDNs. Invalid IP addresses will cause the module to fail. No validation is performed for FQDNs.  If more than 4 servers are provided, only the first 4 unique nameservers will be used.  if no servers are given a default of *0.pool.ntp.org* will be used. |
| **state**  string | Create or delete NTP servers configuration  Choices:   - `"absent"` - `"present"` ← (default) |

## [Notes](purefa_ntp_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_ntp_module.md#id5)

```yaml+jinja
- name: Delete exisitng NTP server entries
  purestorage.flasharray.purefa_ntp:
    state: absent
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Set array NTP servers
  purestorage.flasharray.purefa_ntp:
    state: present
    ntp_servers:
      - "0.pool.ntp.org"
      - "1.pool.ntp.org"
      - "2.pool.ntp.org"
      - "3.pool.ntp.org"
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
