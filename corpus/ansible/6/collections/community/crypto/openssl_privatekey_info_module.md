---
collection: ansible
version: "6"
title: "community.crypto.openssl_privatekey_info module – Provide information for OpenSSL private keys"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/crypto/openssl_privatekey_info_module.html
fetched_at: 2026-07-27T17:06:25+00:00
---
# community.crypto.openssl_privatekey_info module – Provide information for OpenSSL private keys

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
> see [Requirements](openssl_privatekey_info_module.md#ansible-collections-community-crypto-openssl-privatekey-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.crypto.openssl_privatekey_info`.

- [Synopsis](openssl_privatekey_info_module.md#synopsis)
- [Requirements](openssl_privatekey_info_module.md#requirements)
- [Parameters](openssl_privatekey_info_module.md#parameters)
- [Attributes](openssl_privatekey_info_module.md#attributes)
- [See Also](openssl_privatekey_info_module.md#see-also)
- [Examples](openssl_privatekey_info_module.md#examples)
- [Return Values](openssl_privatekey_info_module.md#return-values)

## [Synopsis](openssl_privatekey_info_module.md#id1)

- This module allows one to query information on OpenSSL private keys.
- In case the key consistency checks fail, the module will fail as this indicates a faked private key. In this case, all return variables are still returned. Note that key consistency checks are not available all key types; if none is available, `none` is returned for `key_is_consistent`.
- It uses the cryptography python library to interact with OpenSSL.

## [Requirements](openssl_privatekey_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- cryptography >= 1.2.3

## [Parameters](openssl_privatekey_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **check_consistency**  boolean  added in community.crypto 2.0.0 | Whether to check consistency of the private key.  In community.crypto < 2.0.0, consistency was always checked.  Since community.crypto 2.0.0, the consistency check has been disabled by default to avoid private key material to be transported around and computed with, and only do so when requested explicitly. This can potentially prevent [side-channel attacks](https://en.wikipedia.org/wiki/Side-channel_attack).  Choices:   - `false` ← (default) - `true` |
| **content**  string  added in community.crypto 1.0.0 | Content of the private key file.  Either *path* or *content* must be specified, but not both. |
| **passphrase**  string | The passphrase for the private key. |
| **path**  path | Remote absolute path where the private key file is loaded from. |
| **return_private_key_data**  boolean | Whether to return private key data.  Only set this to `true` when you want private information about this key to leave the remote machine.  **WARNING:** you have to make sure that private key data is not accidentally logged!  Choices:   - `false` ← (default) - `true` |
| **select_crypto_backend**  string | Determines which crypto backend to use.  The default choice is `auto`, which tries to use `cryptography` if available.  If set to `cryptography`, will try to use the [cryptography](https://cryptography.io/) library.  Choices:   - `"auto"` ← (default) - `"cryptography"` |

## [Attributes](openssl_privatekey_info_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support:  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [See Also](openssl_privatekey_info_module.md#id5)

> **See also:**
>
> [community.crypto.openssl_privatekey](openssl_privatekey_module.md#ansible-collections-community-crypto-openssl-privatekey-module)
> :   Generate OpenSSL private keys.
>
> [community.crypto.openssl_privatekey_pipe](openssl_privatekey_pipe_module.md#ansible-collections-community-crypto-openssl-privatekey-pipe-module)
> :   Generate OpenSSL private keys without disk access.

## [Examples](openssl_privatekey_info_module.md#id6)

```yaml+jinja
- name: Generate an OpenSSL private key with the default values (4096 bits, RSA)
  community.crypto.openssl_privatekey:
    path: /etc/ssl/private/ansible.com.pem

- name: Get information on generated key
  community.crypto.openssl_privatekey_info:
    path: /etc/ssl/private/ansible.com.pem
  register: result

- name: Dump information
  ansible.builtin.debug:
    var: result
```

## [Return Values](openssl_privatekey_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **can_load_key**  boolean | Whether the module was able to load the private key from disk.  Returned: always |
| **can_parse_key**  boolean | Whether the module was able to parse the private key.  Returned: always |
| **key_is_consistent**  boolean | Whether the key is consistent. Can also return `none` next to `true` and `false`, to indicate that consistency could not be checked.  In case the check returns `false`, the module will fail.  Returned: when *check_consistency=true* |
| **private_data**  dictionary | Private key data. Depends on key type.  Returned: success and when *return_private_key_data* is set to `true` |
| **public_data**  dictionary | Public key data. Depends on key type.  Returned: success |
| **curve**  string | The curve’s name for ECC.  Returned: When `type=ECC` |
| **exponent**  integer | The RSA key’s public exponent.  Returned: When `type=RSA` |
| **exponent_size**  integer | The maximum number of bits of a private key. This is basically the bit size of the subgroup used.  Returned: When `type=ECC` |
| **g**  integer | The `g` value for DSA.  This is the element spanning the subgroup of the multiplicative group of the prime field used.  Returned: When `type=DSA` |
| **modulus**  integer | The RSA key’s modulus.  Returned: When `type=RSA` |
| **p**  integer | The `p` value for DSA.  This is the prime modulus upon which arithmetic takes place.  Returned: When `type=DSA` |
| **q**  integer | The `q` value for DSA.  This is a prime that divides `p - 1`, and at the same time the order of the subgroup of the multiplicative group of the prime field used.  Returned: When `type=DSA` |
| **size**  integer | Bit size of modulus (RSA) or prime number (DSA).  Returned: When `type=RSA` or `type=DSA` |
| **x**  integer | The `x` coordinate for the public point on the elliptic curve.  Returned: When `type=ECC` |
| **y**  integer | For `type=ECC`, this is the `y` coordinate for the public point on the elliptic curve.  For `type=DSA`, this is the publicly known group element whose discrete logarithm w.r.t. `g` is the private key.  Returned: When `type=DSA` or `type=ECC` |
| **public_key**  string | Private key’s public key in PEM format.  Returned: success  Sample: `"-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8A..."` |
| **public_key_fingerprints**  dictionary | Fingerprints of private key’s public key.  For every hash algorithm available, the fingerprint is computed.  Returned: success  Sample: `"{'sha256': 'd4:b3:aa:6d:c8:04:ce:4e:ba:f6:29:4d:92:a3:94:b0:c2:ff:bd:bf:33:63:11:43:34:0f:51:b0:95:09:2f:63', 'sha512': 'f7:07:4a:f0:b0:f0:e6:8b:95:5f:f9:e6:61:0a:32:68:f1..."` |
| **type**  string | The key’s type.  One of `RSA`, `DSA`, `ECC`, `Ed25519`, `X25519`, `Ed448`, or `X448`.  Will start with `unknown` if the key type cannot be determined.  Returned: success  Sample: `"RSA"` |

### Authors

- Felix Fontein (@felixfontein)
- Yanis Guenane (@Spredzy)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.crypto)
[Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-crypto)
