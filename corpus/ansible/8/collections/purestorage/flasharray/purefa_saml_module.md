---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_saml module – Manage FlashArray SAML2 service and identity providers"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_saml_module.html
fetched_at: 2026-07-28T02:51:23+00:00
---
# purestorage.flasharray.purefa_saml module – Manage FlashArray SAML2 service and identity providers

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
> see [Requirements](purefa_saml_module.md#ansible-collections-purestorage-flasharray-purefa-saml-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_saml`.

New in purestorage.flasharray 1.12.0

- [Synopsis](purefa_saml_module.md#synopsis)
- [Requirements](purefa_saml_module.md#requirements)
- [Parameters](purefa_saml_module.md#parameters)
- [Notes](purefa_saml_module.md#notes)
- [Examples](purefa_saml_module.md#examples)

## [Synopsis](purefa_saml_module.md#id1)

- Enable or disable FlashArray SAML2 providers

## [Requirements](purefa_saml_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_saml_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **array_url**  string | The URL of the FlashArray |
| **decryption_credential**  string | The credential used by the service provider to decrypt encrypted SAML assertions from the identity provider |
| **enabled**  boolean | Defines the enabled state of the identity provider  **Choices:**   - `false` ← (default) - `true` |
| **encrypt_asserts**  boolean | If set to true, SAML assertions will be encrypted by the identity provider  **Choices:**   - `false` ← (default) - `true` |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **metadata_url**  string | The URL of the identity provider metadata |
| **name**  string / required | Name of the SAML2 identity provider (IdP) |
| **sign_request**  boolean | If set to true, SAML requests will be signed by the service provider.  **Choices:**   - `false` ← (default) - `true` |
| **signing_credential**  string | The credential used by the service provider to sign SAML requests |
| **state**  string | Define whether the API client should exist or not.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **url**  string | The URL of the identity provider |
| **x509_cert**  string | The X509 certificate that the service provider uses to verify the SAML response signature from the identity provider |

## [Notes](purefa_saml_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_saml_module.md#id5)

```yaml+jinja
- name: Create (disabled) SAML2 SSO with only metadata URL
  purestorage.flasharray.purefa_saml:
    name: myIDP
    array_url: "https://10.10.10.2"
    metadata_url: "https://myidp.acme.com/adfs/ls"
    x509_cert: "{{lookup('file', 'x509_cert_file') }}"
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Enable SAML2 SSO
  purestorage.flasharray.purefa_saml:
    name: myISO
    enabled: true
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Delete SAML2 SSO
  purestorage.flasharray.purefa_saml:
    state: absent
    name: myIDP
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
