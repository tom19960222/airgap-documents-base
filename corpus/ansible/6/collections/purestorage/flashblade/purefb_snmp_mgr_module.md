---
collection: ansible
version: "6"
title: "purestorage.flashblade.purefb_snmp_mgr module – Configure FlashBlade SNMP Managers"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flashblade/purefb_snmp_mgr_module.html
fetched_at: 2026-07-28T00:19:01+00:00
---
# purestorage.flashblade.purefb_snmp_mgr module – Configure FlashBlade SNMP Managers

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
> see [Requirements](purefb_snmp_mgr_module.md#ansible-collections-purestorage-flashblade-purefb-snmp-mgr-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_snmp_mgr`.

New in purestorage.flashblade 1.0.0

- [Synopsis](purefb_snmp_mgr_module.md#synopsis)
- [Requirements](purefb_snmp_mgr_module.md#requirements)
- [Parameters](purefb_snmp_mgr_module.md#parameters)
- [Notes](purefb_snmp_mgr_module.md#notes)
- [Examples](purefb_snmp_mgr_module.md#examples)

## [Synopsis](purefb_snmp_mgr_module.md#id1)

- Manage SNMP managers on a Pure Storage FlashBlade.
- This module is not idempotent and will always modify an existing SNMP manager due to hidden parameters that cannot be compared to the play parameters.

## [Requirements](purefb_snmp_mgr_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_snmp_mgr_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **auth_passphrase**  string | SNMPv3 only. Passphrase of 8 - 32 characters. |
| **auth_protocol**  string | SNMP v3 only. Hash algorithm to use  Choices:   - `"MD5"` - `"SHA"` |
| **community**  string | SNMP v2c only. Manager community ID. Between 1 and 32 characters long. |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **host**  string | IPv4 or IPv6 address or FQDN to send trap messages to. |
| **name**  string / required | Name of SNMP Manager |
| **notification**  string | Action to perform on event.  Choices:   - `"inform"` - `"trap"` ← (default) |
| **privacy_passphrase**  string | SNMPv3 only. Passphrase to encrypt SNMP messages. Must be between 8 and 63 non-space ASCII characters. |
| **privacy_protocol**  string | SNMP v3 only. Encryption protocol to use  Choices:   - `"AES"` - `"DES"` |
| **state**  string | Create or delete SNMP manager  Choices:   - `"absent"` - `"present"` ← (default) |
| **user**  string | SNMP v3 only. User ID recognized by the specified SNMP manager. Must be between 1 and 32 characters. |
| **version**  string | Version of SNMP protocol to use for the manager.  Choices:   - `"v2c"` - `"v3"` |

## [Notes](purefb_snmp_mgr_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_snmp_mgr_module.md#id5)

```yaml+jinja
- name: Delete exisitng SNMP manager
  purestorage.flashblade.purefb_snmp_mgr:
    name: manager1
    state: absent
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
- name: Create v2c SNMP manager
  purestorage.flashblade.purefb_snmp_mgr:
    name: manager1
    community: public
    host: 10.21.22.23
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
- name: Create v3 SNMP manager
  purestorage.flashblade.purefb_snmp_mgr:
    name: manager2
    version: v3
    auth_protocol: MD5
    auth_passphrase: password
    host: 10.21.22.23
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
- name: Update existing SNMP manager
  purestorage.flashblade.purefb_snmp_mgr:
    name: manager1
    community: private
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
