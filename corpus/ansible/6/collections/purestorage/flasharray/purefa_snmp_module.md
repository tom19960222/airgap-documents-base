---
collection: ansible
version: "6"
title: "purestorage.flasharray.purefa_snmp module – Configure FlashArray SNMP Managers"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flasharray/purefa_snmp_module.html
fetched_at: 2026-07-28T00:18:29+00:00
---
# purestorage.flasharray.purefa_snmp module – Configure FlashArray SNMP Managers

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
> see [Requirements](purefa_snmp_module.md#ansible-collections-purestorage-flasharray-purefa-snmp-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_snmp`.

New in purestorage.flasharray 1.0.0

- [Synopsis](purefa_snmp_module.md#synopsis)
- [Requirements](purefa_snmp_module.md#requirements)
- [Parameters](purefa_snmp_module.md#parameters)
- [Notes](purefa_snmp_module.md#notes)
- [Examples](purefa_snmp_module.md#examples)

## [Synopsis](purefa_snmp_module.md#id1)

- Manage SNMP managers on a Pure Storage FlashArray.
- Changing of a named SNMP managers version is not supported.
- This module is not idempotent and will always modify an existing SNMP manager due to hidden parameters that cannot be compared to the play parameters.

## [Requirements](purefa_snmp_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_snmp_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **auth_passphrase**  string | SNMPv3 only. Passphrase of 8 - 32 characters. |
| **auth_protocol**  string | SNMP v3 only. Hash algorithm to use  Choices:   - `"MD5"` - `"SHA"` |
| **community**  string | SNMP v2c only. Manager community ID. Between 1 and 32 characters long. |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **host**  string | IPv4 or IPv6 address or FQDN to send trap messages to. |
| **name**  string / required | Name of SNMP Manager |
| **notification**  string | Action to perform on event.  Choices:   - `"inform"` - `"trap"` ← (default) |
| **privacy_passphrase**  string | SNMPv3 only. Passphrase to encrypt SNMP messages. Must be between 8 and 63 non-space ASCII characters. |
| **privacy_protocol**  string | SNMP v3 only. Encryption protocol to use  Choices:   - `"AES"` - `"DES"` |
| **state**  string | Create or delete SNMP manager  Choices:   - `"absent"` - `"present"` ← (default) |
| **user**  string | SNMP v3 only. User ID recognized by the specified SNMP manager. Must be between 1 and 32 characters. |
| **version**  string | Version of SNMP protocol to use for the manager.  Choices:   - `"v2c"` ← (default) - `"v3"` |

## [Notes](purefa_snmp_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_snmp_module.md#id5)

```yaml+jinja
- name: Delete exisitng SNMP manager
  purestorage.flasharray.purefa_snmp:
    name: manager1
    state: absent
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
- name: Create v2c SNMP manager
  puretorage.flasharray.urefa_snmp:
    name: manager1
    community: public
    host: 10.21.22.23
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
- name: Create v3 SNMP manager
  puretorage.flasharray.urefa_snmp:
    name: manager2
    version: v3
    auth_protocol: MD5
    auth_passphrase: password
    host: 10.21.22.23
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
- name: Update existing SNMP manager
  purestorage.flasharray.purefa_snmp:
    name: manager1
    community: private
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
