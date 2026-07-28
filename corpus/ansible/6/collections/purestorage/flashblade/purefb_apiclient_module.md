---
collection: ansible
version: "6"
title: "purestorage.flashblade.purefb_apiclient module – Manage FlashBlade API Clients"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flashblade/purefb_apiclient_module.html
fetched_at: 2026-07-28T00:18:39+00:00
---
# purestorage.flashblade.purefb_apiclient module – Manage FlashBlade API Clients

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
> see [Requirements](purefb_apiclient_module.md#ansible-collections-purestorage-flashblade-purefb-apiclient-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_apiclient`.

New in purestorage.flashblade 1.6.0

- [Synopsis](purefb_apiclient_module.md#synopsis)
- [Requirements](purefb_apiclient_module.md#requirements)
- [Parameters](purefb_apiclient_module.md#parameters)
- [Notes](purefb_apiclient_module.md#notes)
- [Examples](purefb_apiclient_module.md#examples)

## [Synopsis](purefb_apiclient_module.md#id1)

- Enable or disable FlashBlade API Clients

## [Requirements](purefb_apiclient_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_apiclient_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **enabled**  boolean | State of the API Client Key  Choices:   - `false` - `true` ← (default) |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **issuer**  string | The name of the identity provider that will be issuing ID Tokens for this API client  If not specified, defaults to the API client name, *name*. |
| **name**  string / required | Name of the API Client |
| **public_key**  string | The API clients PEM formatted (Base64 encoded) RSA public key.  Include the *—–BEGIN PUBLIC KEY—–* and *—–END PUBLIC KEY—–* lines |
| **role**  string | The maximum role allowed for ID Tokens issued by this API client  Choices:   - `"readonly"` - `"ops_admin"` - `"storage_admin"` - `"array_admin"` |
| **state**  string | Define whether the API client should exist or not.  Choices:   - `"absent"` - `"present"` ← (default) |
| **token_ttl**  integer | Time To Live length in seconds for the exchanged access token  Range is 1 second to 1 day (86400 seconds)  Default: `86400` |

## [Notes](purefb_apiclient_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_apiclient_module.md#id5)

```yaml+jinja
- name: Create API token ansible-token
  purestorage.flashblade.purefb_apiclient:
    name: ansible_token
    issuer: "Pure_Storage"
    token_ttl: 3000
    role: array_admin
    public_key: "{{lookup('file', 'public_pem_file') }}"
    fb_url: 10.10.10.2
    api_token: T-68618f31-0c9e-4e57-aa44-5306a2cf10e3

- name: Disable API CLient
  purestorage.flashblade.purefb_apiclient:
    name: ansible_token
    enabled: false
    fb_url: 10.10.10.2
    api_token: T-68618f31-0c9e-4e57-aa44-5306a2cf10e3

- name: Enable API CLient
  purestorage.flashblade.purefb_apiclient:
    name: ansible_token
    enabled: true
    fb_url: 10.10.10.2
    api_token: T-68618f31-0c9e-4e57-aa44-5306a2cf10e3

- name: Delete API Client
  purestorage.flashblade.purefb_apiclient:
    state: absent
    name: ansible_token
    fb_url: 10.10.10.2
    api_token: T-68618f31-0c9e-4e57-aa44-5306a2cf10e3
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
