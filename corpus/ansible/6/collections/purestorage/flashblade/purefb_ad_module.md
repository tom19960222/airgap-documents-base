---
collection: ansible
version: "6"
title: "purestorage.flashblade.purefb_ad module – Manage FlashBlade Active Directory Account"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flashblade/purefb_ad_module.html
fetched_at: 2026-07-28T00:18:37+00:00
---
# purestorage.flashblade.purefb_ad module – Manage FlashBlade Active Directory Account

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
> see [Requirements](purefb_ad_module.md#ansible-collections-purestorage-flashblade-purefb-ad-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_ad`.

New in purestorage.flashblade 1.6.0

- [Synopsis](purefb_ad_module.md#synopsis)
- [Requirements](purefb_ad_module.md#requirements)
- [Parameters](purefb_ad_module.md#parameters)
- [Notes](purefb_ad_module.md#notes)
- [Examples](purefb_ad_module.md#examples)

## [Synopsis](purefb_ad_module.md#id1)

- Add or delete FlashBlade Active Directory Account
- FlashBlade allows the creation of one AD computer account, or joining of an existing AD computer account.

## [Requirements](purefb_ad_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_ad_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **computer**  string | The common name of the computer account to be created in the Active Directory domain.  If not specified, defaults to the name of the Active Directory configuration. |
| **directory_servers**  list / elements=string | A list of directory servers that will be used for lookups related to user authorization  Accepted server formats are IP address and DNS name  All specified servers must be registered to the domain appropriately in the array configured DNS and will only be communicated with over the secure LDAP (LDAPS) protocol. If not specified, servers are resolved for the domain in DNS  The specified list can have a maximum length of 5. If more are provided only the first 5 are used. |
| **domain**  string | The Active Directory domain to join |
| **encryption**  list / elements=string | The encryption types that will be supported for use by clients for Kerberos authentication  Choices:   - `"aes256-sha1"` ← (default) - `"aes128-sha1"` - `"arcfour-hmac"`   Default: `["aes256-sha1"]` |
| **existing**  boolean | Does the account *name* already exist in the AD environment  Choices:   - `false` ← (default) - `true` |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **join_ou**  string | Location where the Computer account will be created. e.g. OU=Arrays,OU=Storage.  If left empty, defaults to **CN=Computers**. |
| **kerberos_servers**  list / elements=string | A list of key distribution servers to use for Kerberos protocol  Accepted server formats are IP address and DNS name  All specified servers must be registered to the domain appropriately in the array configured DNS. If not specified, servers are resolved for the domain in DNS.  The specified list can have a maximum length of 5. If more are provided only the first 5 are used. |
| **local_only**  boolean | Do a local-only delete of an active directory account  Choices:   - `false` ← (default) - `true` |
| **name**  string / required | Name of the AD account |
| **password**  string | Password string for *username* |
| **service**  list / elements=string | Service protocol for Active Directory principals  Refer to FlashBlade User Guide for more details  Choices:   - `"nfs"` ← (default) - `"cifs"` - `"HOST"`   Default: `["nfs"]` |
| **service_principals**  list / elements=string | A list of either FQDNs or SPNs for registering services with the domain.  If not specified **Computer Name.Domain** is used |
| **state**  string | Define whether the AD sccount is deleted or not  Choices:   - `"absent"` - `"present"` ← (default) |
| **username**  string | A user capable of creating a computer account within the domain |

## [Notes](purefb_ad_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_ad_module.md#id5)

```yaml+jinja
- name: Create new AD account
  purestorage.flashblade.purefb_ad:
    name: ad_account
    computer: FLASHBLADE
    domain: acme.com
    username: Administrator
    password: Password
    join_ou: "CN=FakeOU"
    encryption:
    - aes128-cts-hmac-sha1-96
    - aes256-cts-hmac-sha1-96
    kerberos_servers:
    - kdc.acme.com
    directory_servers:
    - ldap.acme.com
    service_principals:
    - vip1.flashblade.acme.com
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Connect to existing AD account
  purestorage.flashblade.purefb_ad:
    name: ad_account
    computer: FLASHBLADE
    domain: acme.com
    username: Administrator
    password: Password
    existing: True
    kerberos_servers:
    - kdc.acme.com
    directory_servers:
    - ldap.acme.com
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Update existing AD account
  purestorage.flashblade.purefb_ad:
    name: ad_account
    encryption:
    - aes256-cts-hmac-sha1-96
    kerberos_servers:
    - kdc.acme.com
    directory_servers:
    - ldap.acme.com
    service_principals:
    - vip1.flashblade.acme.com
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Delete local AD account
  purestorage.flashblade.purefb_ad:
    name: ad_account
    local_only: True
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Fully delete AD account
  purestorage.flashblade.purefb_ad:
    name: ad_account
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
