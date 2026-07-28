---
collection: ansible
version: "8"
title: "community.crypto.openssl_publickey_info module – Provide information for OpenSSL public keys"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/crypto/openssl_publickey_info_module.html
fetched_at: 2026-07-28T01:42:38+00:00
---
# community.crypto.openssl_publickey_info module – Provide information for OpenSSL public keys

> **Note:**
>
> This module is part of the [community.crypto collection](https://galaxy.ansible.com/ui/repo/published/community/crypto/) (version 2.16.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.crypto`.
> You need further requirements to be able to use this module,
> see [Requirements](openssl_publickey_info_module.md#ansible-collections-community-crypto-openssl-publickey-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.crypto.openssl_publickey_info`.

New in community.crypto 1.7.0

- [Synopsis](openssl_publickey_info_module.md#synopsis)
- [Requirements](openssl_publickey_info_module.md#requirements)
- [Parameters](openssl_publickey_info_module.md#parameters)
- [Attributes](openssl_publickey_info_module.md#attributes)
- [See Also](openssl_publickey_info_module.md#see-also)
- [Examples](openssl_publickey_info_module.md#examples)
- [Return Values](openssl_publickey_info_module.md#return-values)

## [Synopsis](openssl_publickey_info_module.md#id1)

- This module allows one to query information on OpenSSL public keys.
- It uses the cryptography python library to interact with OpenSSL.

## [Requirements](openssl_publickey_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- cryptography >= 1.2.3

## [Parameters](openssl_publickey_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **content**  string | Content of the public key file.  Either `path` or `content` must be specified, but not both. |
| **path**  path | Remote absolute path where the public key file is loaded from. |
| **select_crypto_backend**  string | Determines which crypto backend to use.  The default choice is `auto`, which tries to use `cryptography` if available.  If set to `cryptography`, will try to use the [cryptography](https://cryptography.io/) library.  **Choices:**   - `"auto"` ← (default) - `"cryptography"` |

## [Attributes](openssl_publickey_info_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [See Also](openssl_publickey_info_module.md#id5)

> **See also:**
>
> [community.crypto.openssl_publickey](openssl_publickey_module.md#ansible-collections-community-crypto-openssl-publickey-module)
> :   Generate an OpenSSL public key from its private key.
>
> [community.crypto.openssl_privatekey_info](openssl_privatekey_info_module.md#ansible-collections-community-crypto-openssl-privatekey-info-module)
> :   Provide information for OpenSSL private keys.
>
> [community.crypto.openssl_publickey_info](openssl_publickey_info_filter.md#ansible-collections-community-crypto-openssl-publickey-info-filter) filter plugin
> :   A filter variant of this module.

## [Examples](openssl_publickey_info_module.md#id6)

```yaml+jinja
- name: Generate an OpenSSL private key with the default values (4096 bits, RSA)
  community.crypto.openssl_privatekey:
    path: /etc/ssl/private/ansible.com.pem

- name: Create public key from private key
  community.crypto.openssl_publickey:
    privatekey_path: /etc/ssl/private/ansible.com.pem
    path: /etc/ssl/ansible.com.pub

- name: Get information on public key
  community.crypto.openssl_publickey_info:
    path: /etc/ssl/ansible.com.pub
  register: result

- name: Dump information
  ansible.builtin.debug:
    var: result
```

## [Return Values](openssl_publickey_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **fingerprints**  dictionary | Fingerprints of public key.  For every hash algorithm available, the fingerprint is computed.  **Returned:** success  **Sample:** `"{'sha256': 'd4:b3:aa:6d:c8:04:ce:4e:ba:f6:29:4d:92:a3:94:b0:c2:ff:bd:bf:33:63:11:43:34:0f:51:b0:95:09:2f:63', 'sha512': 'f7:07:4a:f0:b0:f0:e6:8b:95:5f:f9:e6:61:0a:32:68:f1..."` |
| **public_data**  dictionary | Public key data. Depends on key type.  **Returned:** success |
| **curve**  string | The curve’s name for ECC.  **Returned:** When `type=ECC` |
| **exponent**  integer | The RSA key’s public exponent.  **Returned:** When `type=RSA` |
| **exponent_size**  integer | The maximum number of bits of a private key. This is basically the bit size of the subgroup used.  **Returned:** When `type=ECC` |
| **g**  integer | The `g` value for DSA.  This is the element spanning the subgroup of the multiplicative group of the prime field used.  **Returned:** When `type=DSA` |
| **modulus**  integer | The RSA key’s modulus.  **Returned:** When `type=RSA` |
| **p**  integer | The `p` value for DSA.  This is the prime modulus upon which arithmetic takes place.  **Returned:** When `type=DSA` |
| **q**  integer | The `q` value for DSA.  This is a prime that divides `p - 1`, and at the same time the order of the subgroup of the multiplicative group of the prime field used.  **Returned:** When `type=DSA` |
| **size**  integer | Bit size of modulus (RSA) or prime number (DSA).  **Returned:** When `type=RSA` or `type=DSA` |
| **x**  integer | The `x` coordinate for the public point on the elliptic curve.  **Returned:** When `type=ECC` |
| **y**  integer | For `type=ECC`, this is the `y` coordinate for the public point on the elliptic curve.  For `type=DSA`, this is the publicly known group element whose discrete logarithm w.r.t. `g` is the private key.  **Returned:** When `type=DSA` or `type=ECC` |
| **type**  string | The key’s type.  One of `RSA`, `DSA`, `ECC`, `Ed25519`, `X25519`, `Ed448`, or `X448`.  Will start with `unknown` if the key type cannot be determined.  **Returned:** success  **Sample:** `"RSA"` |

### Authors

- Felix Fontein (@felixfontein)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.crypto)
- [Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-crypto)
