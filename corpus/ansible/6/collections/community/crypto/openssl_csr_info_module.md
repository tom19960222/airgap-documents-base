---
collection: ansible
version: "6"
title: "community.crypto.openssl_csr_info module – Provide information of OpenSSL Certificate Signing Requests (CSR)"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/crypto/openssl_csr_info_module.html
fetched_at: 2026-07-27T17:06:21+00:00
---
# community.crypto.openssl_csr_info module – Provide information of OpenSSL Certificate Signing Requests (CSR)

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
> see [Requirements](openssl_csr_info_module.md#ansible-collections-community-crypto-openssl-csr-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.crypto.openssl_csr_info`.

- [Synopsis](openssl_csr_info_module.md#synopsis)
- [Requirements](openssl_csr_info_module.md#requirements)
- [Parameters](openssl_csr_info_module.md#parameters)
- [Attributes](openssl_csr_info_module.md#attributes)
- [See Also](openssl_csr_info_module.md#see-also)
- [Examples](openssl_csr_info_module.md#examples)
- [Return Values](openssl_csr_info_module.md#return-values)

## [Synopsis](openssl_csr_info_module.md#id1)

- This module allows one to query information on OpenSSL Certificate Signing Requests (CSR).
- In case the CSR signature cannot be validated, the module will fail. In this case, all return variables are still returned.
- It uses the cryptography python library to interact with OpenSSL.

## [Requirements](openssl_csr_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- If *name_encoding* is set to another value than `ignore`, the [idna Python library](https://pypi.org/project/idna/) needs to be installed.
- cryptography >= 1.3

## [Parameters](openssl_csr_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **content**  string  added in community.crypto 1.0.0 | Content of the CSR file.  Either *path* or *content* must be specified, but not both. |
| **name_encoding**  string | How to encode names (DNS names, URIs, email addresses) in return values.  `ignore` will use the encoding returned by the backend.  `idna` will convert all labels of domain names to IDNA encoding. IDNA2008 will be preferred, and IDNA2003 will be used if IDNA2008 encoding fails.  `unicode` will convert all labels of domain names to Unicode. IDNA2008 will be preferred, and IDNA2003 will be used if IDNA2008 decoding fails.  **Note** that `idna` and `unicode` require the [idna Python library](https://pypi.org/project/idna/) to be installed.  Choices:   - `"ignore"` ← (default) - `"idna"` - `"unicode"` |
| **path**  path | Remote absolute path where the CSR file is loaded from.  Either *path* or *content* must be specified, but not both. |
| **select_crypto_backend**  string | Determines which crypto backend to use.  The default choice is `auto`, which tries to use `cryptography` if available.  If set to `cryptography`, will try to use the [cryptography](https://cryptography.io/) library.  Choices:   - `"auto"` ← (default) - `"cryptography"` |

## [Attributes](openssl_csr_info_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support:  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [See Also](openssl_csr_info_module.md#id5)

> **See also:**
>
> [community.crypto.openssl_csr](openssl_csr_module.md#ansible-collections-community-crypto-openssl-csr-module)
> :   Generate OpenSSL Certificate Signing Request (CSR).
>
> [community.crypto.openssl_csr_pipe](openssl_csr_pipe_module.md#ansible-collections-community-crypto-openssl-csr-pipe-module)
> :   Generate OpenSSL Certificate Signing Request (CSR).

## [Examples](openssl_csr_info_module.md#id6)

```yaml+jinja
- name: Generate an OpenSSL Certificate Signing Request
  community.crypto.openssl_csr:
    path: /etc/ssl/csr/www.ansible.com.csr
    privatekey_path: /etc/ssl/private/ansible.com.pem
    common_name: www.ansible.com

- name: Get information on the CSR
  community.crypto.openssl_csr_info:
    path: /etc/ssl/csr/www.ansible.com.csr
  register: result

- name: Dump information
  debug:
    var: result
```

## [Return Values](openssl_csr_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **authority_cert_issuer**  list / elements=string | The CSR’s authority cert issuer as a list of general names.  Is `none` if the `AuthorityKeyIdentifier` extension is not present.  See *name_encoding* for how IDNs are handled.  Returned: success  Sample: `["DNS:www.ansible.com", "IP:1.2.3.4"]` |
| **authority_cert_serial_number**  integer | The CSR’s authority cert serial number.  Is `none` if the `AuthorityKeyIdentifier` extension is not present.  Returned: success  Sample: `12345` |
| **authority_key_identifier**  string | The CSR’s authority key identifier.  The identifier is returned in hexadecimal, with `:` used to separate bytes.  Is `none` if the `AuthorityKeyIdentifier` extension is not present.  Returned: success  Sample: `"00:11:22:33:44:55:66:77:88:99:aa:bb:cc:dd:ee:ff:00:11:22:33"` |
| **basic_constraints**  list / elements=string | Entries in the `basic_constraints` extension, or `none` if extension is not present.  Returned: success  Sample: `["CA:TRUE", "pathlen:1"]` |
| **basic_constraints_critical**  boolean | Whether the `basic_constraints` extension is critical.  Returned: success |
| **extended_key_usage**  list / elements=string | Entries in the `extended_key_usage` extension, or `none` if extension is not present.  Returned: success  Sample: `["Biometric Info", "DVCS", "Time Stamping"]` |
| **extended_key_usage_critical**  boolean | Whether the `extended_key_usage` extension is critical.  Returned: success |
| **extensions_by_oid**  dictionary | Returns a dictionary for every extension OID  Returned: success  Sample: `{"1.3.6.1.5.5.7.1.24": {"critical": false, "value": "MAMCAQU="}}` |
| **critical**  boolean | Whether the extension is critical.  Returned: success |
| **value**  string | The Base64 encoded value (in DER format) of the extension.  **Note** that depending on the `cryptography` version used, it is not possible to extract the ASN.1 content of the extension, but only to provide the re-encoded content of the extension in case it was parsed by `cryptography`. This should usually result in exactly the same value, except if the original extension value was malformed.  Returned: success  Sample: `"MAMCAQU="` |
| **key_usage**  string | Entries in the `key_usage` extension, or `none` if extension is not present.  Returned: success  Sample: `"['Key Agreement', 'Data Encipherment']"` |
| **key_usage_critical**  boolean | Whether the `key_usage` extension is critical.  Returned: success |
| **name_constraints_critical**  boolean  added in community.crypto 1.1.0 | Whether the `name_constraints` extension is critical.  Is `none` if extension is not present.  Returned: success |
| **name_constraints_excluded**  list / elements=string  added in community.crypto 1.1.0 | List of excluded subtrees the CA cannot sign certificates for.  Is `none` if extension is not present.  See *name_encoding* for how IDNs are handled.  Returned: success  Sample: `["email:.com"]` |
| **name_constraints_permitted**  list / elements=string  added in community.crypto 1.1.0 | List of permitted subtrees to sign certificates for.  Returned: success  Sample: `["email:.somedomain.com"]` |
| **ocsp_must_staple**  boolean | `true` if the OCSP Must Staple extension is present, `none` otherwise.  Returned: success |
| **ocsp_must_staple_critical**  boolean | Whether the `ocsp_must_staple` extension is critical.  Returned: success |
| **public_key**  string | CSR’s public key in PEM format  Returned: success  Sample: `"-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8A..."` |
| **public_key_data**  dictionary  added in community.crypto 1.7.0 | Public key data. Depends on the public key’s type.  Returned: success |
| **curve**  string | The curve’s name for ECC.  Returned: When `public_key_type=ECC` |
| **exponent**  integer | The RSA key’s public exponent.  Returned: When `public_key_type=RSA` |
| **exponent_size**  integer | The maximum number of bits of a private key. This is basically the bit size of the subgroup used.  Returned: When `public_key_type=ECC` |
| **g**  integer | The `g` value for DSA.  This is the element spanning the subgroup of the multiplicative group of the prime field used.  Returned: When `public_key_type=DSA` |
| **modulus**  integer | The RSA key’s modulus.  Returned: When `public_key_type=RSA` |
| **p**  integer | The `p` value for DSA.  This is the prime modulus upon which arithmetic takes place.  Returned: When `public_key_type=DSA` |
| **q**  integer | The `q` value for DSA.  This is a prime that divides `p - 1`, and at the same time the order of the subgroup of the multiplicative group of the prime field used.  Returned: When `public_key_type=DSA` |
| **size**  integer | Bit size of modulus (RSA) or prime number (DSA).  Returned: When `public_key_type=RSA` or `public_key_type=DSA` |
| **x**  integer | The `x` coordinate for the public point on the elliptic curve.  Returned: When `public_key_type=ECC` |
| **y**  integer | For `public_key_type=ECC`, this is the `y` coordinate for the public point on the elliptic curve.  For `public_key_type=DSA`, this is the publicly known group element whose discrete logarithm w.r.t. `g` is the private key.  Returned: When `public_key_type=DSA` or `public_key_type=ECC` |
| **public_key_fingerprints**  dictionary | Fingerprints of CSR’s public key.  For every hash algorithm available, the fingerprint is computed.  Returned: success  Sample: `"{'sha256': 'd4:b3:aa:6d:c8:04:ce:4e:ba:f6:29:4d:92:a3:94:b0:c2:ff:bd:bf:33:63:11:43:34:0f:51:b0:95:09:2f:63', 'sha512': 'f7:07:4a:f0:b0:f0:e6:8b:95:5f:f9:e6:61:0a:32:68:f1..."` |
| **public_key_type**  string  added in community.crypto 1.7.0 | The CSR’s public key’s type.  One of `RSA`, `DSA`, `ECC`, `Ed25519`, `X25519`, `Ed448`, or `X448`.  Will start with `unknown` if the key type cannot be determined.  Returned: success  Sample: `"RSA"` |
| **signature_valid**  boolean | Whether the CSR’s signature is valid.  In case the check returns `false`, the module will fail.  Returned: success |
| **subject**  dictionary | The CSR’s subject as a dictionary.  Note that for repeated values, only the last one will be returned.  Returned: success  Sample: `{"commonName": "www.example.com", "emailAddress": "test@example.com"}` |
| **subject_alt_name**  list / elements=string | Entries in the `subject_alt_name` extension, or `none` if extension is not present.  See *name_encoding* for how IDNs are handled.  Returned: success  Sample: `["DNS:www.ansible.com", "IP:1.2.3.4"]` |
| **subject_alt_name_critical**  boolean | Whether the `subject_alt_name` extension is critical.  Returned: success |
| **subject_key_identifier**  string | The CSR’s subject key identifier.  The identifier is returned in hexadecimal, with `:` used to separate bytes.  Is `none` if the `SubjectKeyIdentifier` extension is not present.  Returned: success  Sample: `"00:11:22:33:44:55:66:77:88:99:aa:bb:cc:dd:ee:ff:00:11:22:33"` |
| **subject_ordered**  list / elements=list | The CSR’s subject as an ordered list of tuples.  Returned: success  Sample: `[["commonName", "www.example.com"], [{"emailAddress": "test@example.com"}]]` |

### Authors

- Felix Fontein (@felixfontein)
- Yanis Guenane (@Spredzy)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.crypto)
[Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-crypto)
