---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_ad module – Manage FlashArray Active Directory Account"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_ad_module.html
fetched_at: 2026-07-28T02:50:34+00:00
---
# purestorage.flasharray.purefa_ad module – Manage FlashArray Active Directory Account

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
> see [Requirements](purefa_ad_module.md#ansible-collections-purestorage-flasharray-purefa-ad-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_ad`.

New in purestorage.flasharray 1.9.0

- [Synopsis](purefa_ad_module.md#synopsis)
- [Requirements](purefa_ad_module.md#requirements)
- [Parameters](purefa_ad_module.md#parameters)
- [Notes](purefa_ad_module.md#notes)
- [Examples](purefa_ad_module.md#examples)

## [Synopsis](purefa_ad_module.md#id1)

- Add or delete FlashArray Active Directory Account
- FlashArray allows the creation of one AD computer account, or joining of an existing AD computer account.

## [Requirements](purefa_ad_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_ad_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **computer**  string | The common name of the computer account to be created in the Active Directory domain.  If not specified, defaults to the name of the Active Directory configuration. |
| **directory_servers**  list / elements=string | A list of directory servers that will be used for lookups related to user authorization  Accepted server formats are IP address and DNS name  All specified servers must be registered to the domain appropriately in the array configured DNS and are only communicated with over the secure LDAP (LDAPS) protocol. If not specified, servers are resolved for the domain in DNS  The specified list can have a maximum length of 1, or 3 for Purity 6.1.6 or higher. If more are provided only the first allowed count used. |
| **domain**  string | The Active Directory domain to join |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **join_existing**  boolean  *added in purestorage.flasharray 1.14.0* | If specified as *true*, the domain is searched for a pre-existing computer account to join to, and no new account will be created within the domain. The `username` specified when joining a pre-existing account must have permissions to ‘read all properties from’ and ‘reset the password of’ the pre-existing account. `join_ou` will be read from the pre-existing account and cannot be specified when joining to an existing account  **Choices:**   - `false` ← (default) - `true` |
| **join_ou**  string  *added in purestorage.flasharray 1.10.0* | Distinguished name of organization unit in which the computer account should be created when joining the domain. e.g. OU=Arrays,OU=Storage.  The **DC=…** components can be omitted.  If left empty, defaults to **CN=Computers**.  Requires Purity//FA 6.1.8 or higher |
| **kerberos_servers**  list / elements=string | A list of key distribution servers to use for Kerberos protocol  Accepted server formats are IP address and DNS name  All specified servers must be registered to the domain appropriately in the array configured DNS and are only communicated with over the secure LDAP (LDAPS) protocol. If not specified, servers are resolved for the domain in DNS.  The specified list can have a maximum length of 1, or 3 for Purity 6.1.6 or higher. If more are provided only the first allowed count used. |
| **local_only**  boolean | Do a local-only delete of an active directory account  **Choices:**   - `false` ← (default) - `true` |
| **name**  string / required | Name of the AD account |
| **password**  string | Password string for *username* |
| **state**  string | Define whether the AD sccount is deleted or not  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **tls**  string  *added in purestorage.flasharray 1.14.0* | TLS mode for communication with domain controllers.  **Choices:**   - `"required"` ← (default) - `"optional"` |
| **username**  string | A user capable of creating a computer account within the domain |

## [Notes](purefa_ad_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_ad_module.md#id5)

```yaml+jinja
- name: Create new AD account
  purestorage.flasharray.purefa_ad:
    name: ad_account
    computer: FLASHARRAY
    domain: acme.com
    join_ou: "OU=Acme,OU=Dev"
    username: Administrator
    password: Password
    kerberos_servers:
    - kdc.acme.com
    directory_servers:
    - ldap.acme.com
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Delete AD account locally
  purestorage.flasharray.purefa_ad:
    name: ad_account
    local_only: true
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Fully delete AD account. Note that correct AD permissions are required
  purestorage.flasharray.purefa_ad:
    name: ad_account
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
- [Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
- [Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
- [Communication](index.md#communication-for-purestorage-flasharray)
