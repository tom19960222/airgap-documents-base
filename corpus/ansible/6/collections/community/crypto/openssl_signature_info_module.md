---
collection: ansible
version: "6"
title: "community.crypto.openssl_signature_info module – Verify signatures with openssl"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/crypto/openssl_signature_info_module.html
fetched_at: 2026-07-27T17:06:28+00:00
---
# community.crypto.openssl_signature_info module – Verify signatures with openssl

> **Note:**
>
> This module is part of the [community.crypto collection](https://galaxy.ansible.com/community/crypto) (version 2.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.crypto`.
> You need further requirements to be able to use this module,
> see [Requirements](openssl_signature_info_module.md#ansible-collections-community-crypto-openssl-signature-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.crypto.openssl_signature_info`.

New in community.crypto 1.1.0

- [Synopsis](openssl_signature_info_module.md#synopsis)
- [Requirements](openssl_signature_info_module.md#requirements)
- [Parameters](openssl_signature_info_module.md#parameters)
- [Attributes](openssl_signature_info_module.md#attributes)
- [Notes](openssl_signature_info_module.md#notes)
- [See Also](openssl_signature_info_module.md#see-also)
- [Examples](openssl_signature_info_module.md#examples)
- [Return Values](openssl_signature_info_module.md#return-values)

## [Synopsis](openssl_signature_info_module.md#id1)

- This module allows one to verify a signature for a file by a certificate.
- The module uses the cryptography Python library.

## [Requirements](openssl_signature_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- cryptography >= 1.4 (some key types require newer versions)

## [Parameters](openssl_signature_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **certificate_content**  string | The content of the certificate used to verify the signature.  Either *certificate_path* or *certificate_content* must be specified, but not both. |
| **certificate_path**  path | The path to the certificate used to verify the signature.  Either *certificate_path* or *certificate_content* must be specified, but not both. |
| **path**  path / required | The signed file to verify.  This file will only be read and not modified. |
| **select_crypto_backend**  string | Determines which crypto backend to use.  The default choice is `auto`, which tries to use `cryptography` if available.  If set to `cryptography`, will try to use the [cryptography](https://cryptography.io/) library.  Choices:   - `"auto"` ← (default) - `"cryptography"` |
| **signature**  string / required | Base64 encoded signature. |

## [Attributes](openssl_signature_info_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support:  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](openssl_signature_info_module.md#id5)

> **Note:**
>
> - When using the `cryptography` backend, the following key types require at least the following `cryptography` version:
>   RSA keys: `cryptography` >= 1.4
>   DSA and ECDSA keys: `cryptography` >= 1.5
>   ed448 and ed25519 keys: `cryptography` >= 2.6

## [See Also](openssl_signature_info_module.md#id6)

> **See also:**
>
> [community.crypto.openssl_signature](openssl_signature_module.md#ansible-collections-community-crypto-openssl-signature-module)
> :   Sign data with openssl.
>
> [community.crypto.x509_certificate](x509_certificate_module.md#ansible-collections-community-crypto-x509-certificate-module)
> :   Generate and/or check OpenSSL certificates.

## [Examples](openssl_signature_info_module.md#id7)

```yaml+jinja
- name: Sign example file
  community.crypto.openssl_signature:
    privatekey_path: private.key
    path: /tmp/example_file
  register: sig

- name: Verify signature of example file
  community.crypto.openssl_signature_info:
    certificate_path: cert.pem
    path: /tmp/example_file
    signature: "{{ sig.signature }}"
  register: verify

- name: Make sure the signature is valid
  assert:
    that:
      - verify.valid
```

## [Return Values](openssl_signature_info_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **valid**  boolean | `true` means the signature was valid for the given file, `false` means it was not.  Returned: success |

### Authors

- Patrick Pichler (@aveexy)
- Markus Teufelberger (@MarkusTeufelberger)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.crypto)
[Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-crypto)
