---
collection: ansible
version: "6"
title: "purestorage.flasharray.purefa_kmip module – Manage FlashArray KMIP server objects"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flasharray/purefa_kmip_module.html
fetched_at: 2026-07-28T00:18:16+00:00
---
# purestorage.flasharray.purefa_kmip module – Manage FlashArray KMIP server objects

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
> see [Requirements](purefa_kmip_module.md#ansible-collections-purestorage-flasharray-purefa-kmip-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_kmip`.

New in purestorage.flasharray 1.10.0

- [Synopsis](purefa_kmip_module.md#synopsis)
- [Requirements](purefa_kmip_module.md#requirements)
- [Parameters](purefa_kmip_module.md#parameters)
- [Notes](purefa_kmip_module.md#notes)
- [Examples](purefa_kmip_module.md#examples)

## [Synopsis](purefa_kmip_module.md#id1)

- Manage FlashArray KMIP Server objects

## [Requirements](purefa_kmip_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_kmip_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **ca_certificate**  string | The text of the CA certificate for the KMIP server.  Includes the “—–BEGIN CERTIFICATE—–” and “—–END CERTIFICATE—–” lines  Does not exceed 3000 characters in length |
| **certificate**  string | Name of existing certifcate used to verify FlashArray authenticity to the KMIP server.  Use the *purestorage.flasharray.purefa_certs* module to create certificates. |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **name**  string / required | Name of the KMIP server object |
| **state**  string | Action for the module to perform  Choices:   - `"absent"` - `"present"` ← (default) |
| **uris**  list / elements=string | A list of URIs for the configured KMIP servers. |

## [Notes](purefa_kmip_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_kmip_module.md#id5)

```yaml+jinja
- name: Create KMIP obejct
  purestorage.flasharray.purefa_kmip:
    name: foo
    certificate: bar
    ca_certificate: "{{lookup('file', 'example.crt') }}"
    uris:
    - 1.1.1.1:8888
    - 2.3.3.3:9999
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Delete KMIP object
  purestorage.flasharray.purefa_kmip:
    name: foo
    state: absent
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Update KMIP object
  purestorage.flasharray.purefa_kmip:
    name: foo
    ca_certificate: "{{lookup('file', 'example2.crt') }}"
    uris:
    - 3.3.3.3:8888
    - 4.4.4.4:9999
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
