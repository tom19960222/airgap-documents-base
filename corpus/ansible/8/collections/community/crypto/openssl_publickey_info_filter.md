---
collection: ansible
version: "8"
title: "community.crypto.openssl_publickey_info filter – Retrieve information from OpenSSL public keys in PEM format"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/crypto/openssl_publickey_info_filter.html
fetched_at: 2026-07-28T01:42:46+00:00
---
# community.crypto.openssl_publickey_info filter – Retrieve information from OpenSSL public keys in PEM format

> **Note:**
>
> This filter plugin is part of the [community.crypto collection](https://galaxy.ansible.com/ui/repo/published/community/crypto/) (version 2.16.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.crypto`.
>
> To use it in a playbook, specify: `community.crypto.openssl_publickey_info`.

New in community.crypto 2.10.0

- [Synopsis](openssl_publickey_info_filter.md#synopsis)
- [Input](openssl_publickey_info_filter.md#input)
- [See Also](openssl_publickey_info_filter.md#see-also)
- [Examples](openssl_publickey_info_filter.md#examples)
- [Return Value](openssl_publickey_info_filter.md#return-value)

## [Synopsis](openssl_publickey_info_filter.md#id1)

- Provided a public key in OpenSSL PEM format, retrieve information.
- This is a filter version of the [community.crypto.openssl_publickey_info](openssl_publickey_info_module.md#ansible-collections-community-crypto-openssl-publickey-info-module) module.

## [Input](openssl_publickey_info_filter.md#id2)

This describes the input of the filter, the value before `| community.crypto.openssl_publickey_info`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | The content of the OpenSSL PEM public key. |

## [See Also](openssl_publickey_info_filter.md#id3)

> **See also:**
>
> [community.crypto.openssl_publickey_info](openssl_publickey_info_module.md#ansible-collections-community-crypto-openssl-publickey-info-module)
> :   Provide information for OpenSSL public keys.

## [Examples](openssl_publickey_info_filter.md#id4)

```yaml+jinja
- name: Show the type of a public key
  ansible.builtin.debug:
    msg: >-
      {{
        (
          lookup('ansible.builtin.file', '/path/to/public-key.pem')
          | community.crypto.openssl_publickey_info
        ).type
      }}
```

## [Return Value](openssl_publickey_info_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  dictionary | Information on the public key.  **Returned:** success |
| **fingerprints**  dictionary | Fingerprints of public key.  For every hash algorithm available, the fingerprint is computed.  **Returned:** success  **Sample:** `"{'sha256': 'd4:b3:aa:6d:c8:04:ce:4e:ba:f6:29:4d:92:a3:94:b0:c2:ff:bd:bf:33:63:11:43:34:0f:51:b0:95:09:2f:63', 'sha512': 'f7:07:4a:f0:b0:f0:e6:8b:95:5f:f9:e6:61:0a:32:68:f1..."` |
| **public_data**  dictionary | Public key data. Depends on key type.  **Returned:** success |
| **curve**  string | The curve’s name for ECC.  **Returned:** When `_value.type=ECC` |
| **exponent**  integer | The RSA key’s public exponent.  **Returned:** When `_value.type=RSA` |
| **exponent_size**  integer | The maximum number of bits of a private key. This is basically the bit size of the subgroup used.  **Returned:** When `_value.type=ECC` |
| **g**  integer | The `g` value for DSA.  This is the element spanning the subgroup of the multiplicative group of the prime field used.  **Returned:** When `_value.type=DSA` |
| **modulus**  integer | The RSA key’s modulus.  **Returned:** When `_value.type=RSA` |
| **p**  integer | The `p` value for DSA.  This is the prime modulus upon which arithmetic takes place.  **Returned:** When `_value.type=DSA` |
| **q**  integer | The `q` value for DSA.  This is a prime that divides `p - 1`, and at the same time the order of the subgroup of the multiplicative group of the prime field used.  **Returned:** When `_value.type=DSA` |
| **size**  integer | Bit size of modulus (RSA) or prime number (DSA).  **Returned:** When `_value.type=RSA` or `_value.type=DSA` |
| **x**  integer | The `x` coordinate for the public point on the elliptic curve.  **Returned:** When `_value.type=ECC` |
| **y**  integer | For `_value.type=ECC`, this is the `y` coordinate for the public point on the elliptic curve.  For `_value.type=DSA`, this is the publicly known group element whose discrete logarithm with respect to `g` is the private key.  **Returned:** When `_value.type=DSA` or `_value.type=ECC` |
| **type**  string | The key’s type.  One of `RSA`, `DSA`, `ECC`, `Ed25519`, `X25519`, `Ed448`, or `X448`.  Will start with `unknown` if the key type cannot be determined.  **Returned:** success  **Sample:** `"RSA"` |

### Authors

- Felix Fontein (@felixfontein)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.crypto)
- [Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-crypto)
