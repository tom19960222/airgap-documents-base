---
collection: ansible
version: "6"
title: "purestorage.flasharray.purefa_apiclient module – Manage FlashArray API Clients"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flasharray/purefa_apiclient_module.html
fetched_at: 2026-07-28T00:18:02+00:00
---
# purestorage.flasharray.purefa_apiclient module – Manage FlashArray API Clients

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
> see [Requirements](purefa_apiclient_module.md#ansible-collections-purestorage-flasharray-purefa-apiclient-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_apiclient`.

New in purestorage.flasharray 1.5.0

- [Synopsis](purefa_apiclient_module.md#synopsis)
- [Requirements](purefa_apiclient_module.md#requirements)
- [Parameters](purefa_apiclient_module.md#parameters)
- [Notes](purefa_apiclient_module.md#notes)
- [Examples](purefa_apiclient_module.md#examples)

## [Synopsis](purefa_apiclient_module.md#id1)

- Enable or disable FlashArray API Clients

## [Requirements](purefa_apiclient_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_apiclient_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **enabled**  boolean | State of the API Client Key  Choices:   - `false` - `true` ← (default) |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **issuer**  string | The name of the identity provider that will be issuing ID Tokens for this API client  If not specified, defaults to the API client name, *name*. |
| **name**  string / required | Name of the API Client |
| **public_key**  string | The API clients PEM formatted (Base64 encoded) RSA public key.  Include the *—–BEGIN PUBLIC KEY—–* and *—–END PUBLIC KEY—–* lines |
| **role**  string | The maximum role allowed for ID Tokens issued by this API client  Choices:   - `"readonly"` - `"ops_admin"` - `"storage_admin"` - `"array_admin"` |
| **state**  string | Define whether the API client should exist or not.  Choices:   - `"absent"` - `"present"` ← (default) |
| **token_ttl**  integer | Time To Live length in seconds for the exchanged access token  Range is 1 second to 1 day (86400 seconds)  Default: `86400` |

## [Notes](purefa_apiclient_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_apiclient_module.md#id5)

```yaml+jinja
- name: Create API token ansible-token
  purestorage.flasharray.purefa_apiclient:
    name: ansible-token
    issuer: "Pure Storage"
    ttl: 3000
    role: array_admin
    public_key: "{{lookup('file', 'public_pem_file') }}"
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Disable API CLient
  purestorage.flasharray.purefa_apiclient:
    name: ansible-token
    enabled: false
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Enable API CLient
  purestorage.flasharray.purefa_apiclient:
    name: ansible-token
    enabled: true
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Delete API Client
  purestorage.flasharray.purefa_apiclient:
    state: absent
    name: ansible-token
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
