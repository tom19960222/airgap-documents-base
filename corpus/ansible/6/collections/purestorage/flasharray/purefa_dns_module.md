---
collection: ansible
version: "6"
title: "purestorage.flasharray.purefa_dns module – Configure FlashArray DNS settings"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flasharray/purefa_dns_module.html
fetched_at: 2026-07-28T00:18:08+00:00
---
# purestorage.flasharray.purefa_dns module – Configure FlashArray DNS settings

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
> see [Requirements](purefa_dns_module.md#ansible-collections-purestorage-flasharray-purefa-dns-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_dns`.

New in purestorage.flasharray 1.0.0

- [Synopsis](purefa_dns_module.md#synopsis)
- [Requirements](purefa_dns_module.md#requirements)
- [Parameters](purefa_dns_module.md#parameters)
- [Notes](purefa_dns_module.md#notes)
- [Examples](purefa_dns_module.md#examples)

## [Synopsis](purefa_dns_module.md#id1)

- Set or erase configuration for the DNS settings.
- Nameservers provided will overwrite any existing nameservers.
- From Purity//FA 6.3.3 DNS setting for FA-File can be configured seperately to the management DNS settings

## [Requirements](purefa_dns_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_dns_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **domain**  string | Domain suffix to be appended when perofrming DNS lookups. |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **name**  string  added in purestorage.flasharray 1.14.0 | Name of the DNS configuration.  Default value only supported for management service  Default: `"management"` |
| **nameservers**  list / elements=string | List of up to 3 unique DNS server IP addresses. These can be IPv4 or IPv6 - No validation is done of the addresses is performed. |
| **service**  string  added in purestorage.flasharray 1.14.0 | Type of ser vice the DNS will work with  Choices:   - `"management"` ← (default) - `"file"` |
| **source**  string  added in purestorage.flasharray 1.14.0 | A virtual network interface (vif) |
| **state**  string | Set or delete directory service configuration  Choices:   - `"absent"` - `"present"` ← (default) |

## [Notes](purefa_dns_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_dns_module.md#id5)

```yaml+jinja
- name: Delete exisitng DNS settings
  purestorage.flasharray.purefa_dns:
    state: absent
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Set managemnt DNS settings
  purestorage.flasharray.purefa_dns:
    domain: purestorage.com
    nameservers:
      - 8.8.8.8
      - 8.8.4.4
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Set file DNS settings
  purestorage.flasharray.purefa_dns:
    domain: purestorage.com
    nameservers:
      - 8.8.8.8
      - 8.8.4.4
    name: ad_dns
    service: file
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
