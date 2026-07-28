---
collection: ansible
version: "6"
title: "community.crypto.x509_certificate_info module – Provide information of OpenSSL X.509 certificates"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/crypto/x509_certificate_info_module.html
fetched_at: 2026-07-27T17:06:30+00:00
---
# community.crypto.x509_certificate_info module – Provide information of OpenSSL X.509 certificates

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
> see [Requirements](x509_certificate_info_module.md#ansible-collections-community-crypto-x509-certificate-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.crypto.x509_certificate_info`.

- [Synopsis](x509_certificate_info_module.md#synopsis)
- [Requirements](x509_certificate_info_module.md#requirements)
- [Parameters](x509_certificate_info_module.md#parameters)
- [Attributes](x509_certificate_info_module.md#attributes)
- [Notes](x509_certificate_info_module.md#notes)
- [See Also](x509_certificate_info_module.md#see-also)
- [Examples](x509_certificate_info_module.md#examples)
- [Return Values](x509_certificate_info_module.md#return-values)

## [Synopsis](x509_certificate_info_module.md#id1)

- This module allows one to query information on OpenSSL certificates.
- It uses the cryptography python library to interact with OpenSSL.
- Note that this module was called `openssl_certificate_info` when included directly in Ansible up to version 2.9. When moved to the collection `community.crypto`, it was renamed to [community.crypto.x509_certificate_info](x509_certificate_info_module.md#ansible-collections-community-crypto-x509-certificate-info-module). From Ansible 2.10 on, it can still be used by the old short name (or by `ansible.builtin.openssl_certificate_info`), which redirects to `community.crypto.x509_certificate_info`. When using FQCNs or when using the [collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html#using-collections-in-a-playbook) keyword, the new name [community.crypto.x509_certificate_info](x509_certificate_info_module.md#ansible-collections-community-crypto-x509-certificate-info-module) should be used to avoid a deprecation warning.

## [Requirements](x509_certificate_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- If *name_encoding* is set to another value than `ignore`, the [idna Python library](https://pypi.org/project/idna/) needs to be installed.
- cryptography >= 1.6

## [Parameters](x509_certificate_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **content**  string  added in community.crypto 1.0.0 | Content of the X.509 certificate in PEM format.  Either *path* or *content* must be specified, but not both. |
| **name_encoding**  string | How to encode names (DNS names, URIs, email addresses) in return values.  `ignore` will use the encoding returned by the backend.  `idna` will convert all labels of domain names to IDNA encoding. IDNA2008 will be preferred, and IDNA2003 will be used if IDNA2008 encoding fails.  `unicode` will convert all labels of domain names to Unicode. IDNA2008 will be preferred, and IDNA2003 will be used if IDNA2008 decoding fails.  **Note** that `idna` and `unicode` require the [idna Python library](https://pypi.org/project/idna/) to be installed.  Choices:   - `"ignore"` ← (default) - `"idna"` - `"unicode"` |
| **path**  path | Remote absolute path where the certificate file is loaded from.  Either *path* or *content* must be specified, but not both. |
| **select_crypto_backend**  string | Determines which crypto backend to use.  The default choice is `auto`, which tries to use `cryptography` if available.  If set to `cryptography`, will try to use the [cryptography](https://cryptography.io/) library.  Choices:   - `"auto"` ← (default) - `"cryptography"` |
| **valid_at**  dictionary | A dict of names mapping to time specifications. Every time specified here will be checked whether the certificate is valid at this point. See the `valid_at` return value for informations on the result.  Time can be specified either as relative time or as absolute timestamp.  Time will always be interpreted as UTC.  Valid format is `[+-]timespec | ASN.1 TIME` where timespec can be an integer + `[w | d | h | m | s]` (for example `+32w1d2h`), and ASN.1 TIME (in other words, pattern `YYYYMMDDHHMMSSZ`). Note that all timestamps will be treated as being in UTC. |

## [Attributes](x509_certificate_info_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support:  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](x509_certificate_info_module.md#id5)

> **Note:**
>
> - All timestamp values are provided in ASN.1 TIME format, in other words, following the `YYYYMMDDHHMMSSZ` pattern. They are all in UTC.

## [See Also](x509_certificate_info_module.md#id6)

> **See also:**
>
> [community.crypto.x509_certificate](x509_certificate_module.md#ansible-collections-community-crypto-x509-certificate-module)
> :   Generate and/or check OpenSSL certificates.
>
> [community.crypto.x509_certificate_pipe](x509_certificate_pipe_module.md#ansible-collections-community-crypto-x509-certificate-pipe-module)
> :   Generate and/or check OpenSSL certificates.

## [Examples](x509_certificate_info_module.md#id7)

```yaml+jinja
- name: Generate a Self Signed OpenSSL certificate
  community.crypto.x509_certificate:
    path: /etc/ssl/crt/ansible.com.crt
    privatekey_path: /etc/ssl/private/ansible.com.pem
    csr_path: /etc/ssl/csr/ansible.com.csr
    provider: selfsigned

# Get information on the certificate

- name: Get information on generated certificate
  community.crypto.x509_certificate_info:
    path: /etc/ssl/crt/ansible.com.crt
  register: result

- name: Dump information
  ansible.builtin.debug:
    var: result

# Check whether the certificate is valid or not valid at certain times, fail
# if this is not the case. The first task (x509_certificate_info) collects
# the information, and the second task (assert) validates the result and
# makes the playbook fail in case something is not as expected.

- name: Test whether that certificate is valid tomorrow and/or in three weeks
  community.crypto.x509_certificate_info:
    path: /etc/ssl/crt/ansible.com.crt
    valid_at:
      point_1: "+1d"
      point_2: "+3w"
  register: result

- name: Validate that certificate is valid tomorrow, but not in three weeks
  assert:
    that:
      - result.valid_at.point_1      # valid in one day
      - not result.valid_at.point_2  # not valid in three weeks
```

## [Return Values](x509_certificate_info_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **authority_cert_issuer**  list / elements=string | The certificate’s authority cert issuer as a list of general names.  Is `none` if the `AuthorityKeyIdentifier` extension is not present.  See *name_encoding* for how IDNs are handled.  Returned: success  Sample: `["DNS:www.ansible.com", "IP:1.2.3.4"]` |
| **authority_cert_serial_number**  integer | The certificate’s authority cert serial number.  Is `none` if the `AuthorityKeyIdentifier` extension is not present.  Returned: success  Sample: `12345` |
| **authority_key_identifier**  string | The certificate’s authority key identifier.  The identifier is returned in hexadecimal, with `:` used to separate bytes.  Is `none` if the `AuthorityKeyIdentifier` extension is not present.  Returned: success  Sample: `"00:11:22:33:44:55:66:77:88:99:aa:bb:cc:dd:ee:ff:00:11:22:33"` |
| **basic_constraints**  list / elements=string | Entries in the `basic_constraints` extension, or `none` if extension is not present.  Returned: success  Sample: `["CA:TRUE", "pathlen:1"]` |
| **basic_constraints_critical**  boolean | Whether the `basic_constraints` extension is critical.  Returned: success |
| **expired**  boolean | Whether the certificate is expired (in other words, `notAfter` is in the past).  Returned: success |
| **extended_key_usage**  list / elements=string | Entries in the `extended_key_usage` extension, or `none` if extension is not present.  Returned: success  Sample: `["Biometric Info", "DVCS", "Time Stamping"]` |
| **extended_key_usage_critical**  boolean | Whether the `extended_key_usage` extension is critical.  Returned: success |
| **extensions_by_oid**  dictionary | Returns a dictionary for every extension OID.  Returned: success  Sample: `{"1.3.6.1.5.5.7.1.24": {"critical": false, "value": "MAMCAQU="}}` |
| **critical**  boolean | Whether the extension is critical.  Returned: success |
| **value**  string | The Base64 encoded value (in DER format) of the extension.  **Note** that depending on the `cryptography` version used, it is not possible to extract the ASN.1 content of the extension, but only to provide the re-encoded content of the extension in case it was parsed by `cryptography`. This should usually result in exactly the same value, except if the original extension value was malformed.  Returned: success  Sample: `"MAMCAQU="` |
| **fingerprints**  dictionary  added in community.crypto 1.2.0 | Fingerprints of the DER-encoded form of the whole certificate.  For every hash algorithm available, the fingerprint is computed.  Returned: success  Sample: `"{'sha256': 'd4:b3:aa:6d:c8:04:ce:4e:ba:f6:29:4d:92:a3:94:b0:c2:ff:bd:bf:33:63:11:43:34:0f:51:b0:95:09:2f:63', 'sha512': 'f7:07:4a:f0:b0:f0:e6:8b:95:5f:f9:e6:61:0a:32:68:f1..."` |
| **issuer**  dictionary | The certificate’s issuer.  Note that for repeated values, only the last one will be returned.  Returned: success  Sample: `{"commonName": "ca.example.com", "organizationName": "Ansible"}` |
| **issuer_ordered**  list / elements=list | The certificate’s issuer as an ordered list of tuples.  Returned: success  Sample: `[["organizationName", "Ansible"], [{"commonName": "ca.example.com"}]]` |
| **issuer_uri**  string  added in community.crypto 2.9.0 | The Issuer URI, if included in the certificate. Will be `none` if no issuer URI is included.  Returned: success |
| **key_usage**  string | Entries in the `key_usage` extension, or `none` if extension is not present.  Returned: success  Sample: `"['Key Agreement', 'Data Encipherment']"` |
| **key_usage_critical**  boolean | Whether the `key_usage` extension is critical.  Returned: success |
| **not_after**  string | `notAfter` date as ASN.1 TIME.  Returned: success  Sample: `"20190413202428Z"` |
| **not_before**  string | `notBefore` date as ASN.1 TIME.  Returned: success  Sample: `"20190331202428Z"` |
| **ocsp_must_staple**  boolean | `true` if the OCSP Must Staple extension is present, `none` otherwise.  Returned: success |
| **ocsp_must_staple_critical**  boolean | Whether the `ocsp_must_staple` extension is critical.  Returned: success |
| **ocsp_uri**  string | The OCSP responder URI, if included in the certificate. Will be `none` if no OCSP responder URI is included.  Returned: success |
| **public_key**  string | Certificate’s public key in PEM format.  Returned: success  Sample: `"-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8A..."` |
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
| **public_key_fingerprints**  dictionary | Fingerprints of certificate’s public key.  For every hash algorithm available, the fingerprint is computed.  Returned: success  Sample: `"{'sha256': 'd4:b3:aa:6d:c8:04:ce:4e:ba:f6:29:4d:92:a3:94:b0:c2:ff:bd:bf:33:63:11:43:34:0f:51:b0:95:09:2f:63', 'sha512': 'f7:07:4a:f0:b0:f0:e6:8b:95:5f:f9:e6:61:0a:32:68:f1..."` |
| **public_key_type**  string  added in community.crypto 1.7.0 | The certificate’s public key’s type.  One of `RSA`, `DSA`, `ECC`, `Ed25519`, `X25519`, `Ed448`, or `X448`.  Will start with `unknown` if the key type cannot be determined.  Returned: success  Sample: `"RSA"` |
| **serial_number**  integer | The certificate’s serial number.  Returned: success  Sample: `1234` |
| **signature_algorithm**  string | The signature algorithm used to sign the certificate.  Returned: success  Sample: `"sha256WithRSAEncryption"` |
| **subject**  dictionary | The certificate’s subject as a dictionary.  Note that for repeated values, only the last one will be returned.  Returned: success  Sample: `{"commonName": "www.example.com", "emailAddress": "test@example.com"}` |
| **subject_alt_name**  list / elements=string | Entries in the `subject_alt_name` extension, or `none` if extension is not present.  See *name_encoding* for how IDNs are handled.  Returned: success  Sample: `["DNS:www.ansible.com", "IP:1.2.3.4"]` |
| **subject_alt_name_critical**  boolean | Whether the `subject_alt_name` extension is critical.  Returned: success |
| **subject_key_identifier**  string | The certificate’s subject key identifier.  The identifier is returned in hexadecimal, with `:` used to separate bytes.  Is `none` if the `SubjectKeyIdentifier` extension is not present.  Returned: success  Sample: `"00:11:22:33:44:55:66:77:88:99:aa:bb:cc:dd:ee:ff:00:11:22:33"` |
| **subject_ordered**  list / elements=list | The certificate’s subject as an ordered list of tuples.  Returned: success  Sample: `[["commonName", "www.example.com"], [{"emailAddress": "test@example.com"}]]` |
| **valid_at**  dictionary | For every time stamp provided in the *valid_at* option, a boolean whether the certificate is valid at that point in time or not.  Returned: success |
| **version**  integer | The certificate version.  Returned: success  Sample: `3` |

### Authors

- Felix Fontein (@felixfontein)
- Yanis Guenane (@Spredzy)
- Markus Teufelberger (@MarkusTeufelberger)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.crypto)
[Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-crypto)
