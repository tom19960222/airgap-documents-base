---
collection: ansible
version: "8"
title: "community.crypto.x509_crl_info module – Retrieve information on Certificate Revocation Lists (CRLs)"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/crypto/x509_crl_info_module.html
fetched_at: 2026-07-28T01:42:43+00:00
---
# community.crypto.x509_crl_info module – Retrieve information on Certificate Revocation Lists (CRLs)

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
> see [Requirements](x509_crl_info_module.md#ansible-collections-community-crypto-x509-crl-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.crypto.x509_crl_info`.

New in community.crypto 1.0.0

- [Synopsis](x509_crl_info_module.md#synopsis)
- [Requirements](x509_crl_info_module.md#requirements)
- [Parameters](x509_crl_info_module.md#parameters)
- [Attributes](x509_crl_info_module.md#attributes)
- [Notes](x509_crl_info_module.md#notes)
- [See Also](x509_crl_info_module.md#see-also)
- [Examples](x509_crl_info_module.md#examples)
- [Return Values](x509_crl_info_module.md#return-values)

## [Synopsis](x509_crl_info_module.md#id1)

- This module allows one to retrieve information on Certificate Revocation Lists (CRLs).

## [Requirements](x509_crl_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- If `name_encoding` is set to another value than `ignore`, the [idna Python library](https://pypi.org/project/idna/) needs to be installed.
- cryptography >= 1.2

## [Parameters](x509_crl_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **content**  string | Content of the X.509 CRL in PEM format, or Base64-encoded X.509 CRL.  Either `path` or `content` must be specified, but not both. |
| **list_revoked_certificates**  boolean  *added in community.crypto 1.7.0* | If set to `false`, the list of revoked certificates is not included in the result.  This is useful when retrieving information on large CRL files. Enumerating all revoked certificates can take some time, including serializing the result as JSON, sending it to the Ansible controller, and decoding it again.  **Choices:**   - `false` - `true` ← (default) |
| **name_encoding**  string | How to encode names (DNS names, URIs, email addresses) in return values.  `ignore` will use the encoding returned by the backend.  `idna` will convert all labels of domain names to IDNA encoding. IDNA2008 will be preferred, and IDNA2003 will be used if IDNA2008 encoding fails.  `unicode` will convert all labels of domain names to Unicode. IDNA2008 will be preferred, and IDNA2003 will be used if IDNA2008 decoding fails.  **Note** that `idna` and `unicode` require the [idna Python library](https://pypi.org/project/idna/) to be installed.  **Choices:**   - `"ignore"` ← (default) - `"idna"` - `"unicode"` |
| **path**  path | Remote absolute path where the generated CRL file should be created or is already located.  Either `path` or `content` must be specified, but not both. |

## [Attributes](x509_crl_info_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](x509_crl_info_module.md#id5)

> **Note:**
>
> - All timestamp values are provided in ASN.1 TIME format, in other words, following the `YYYYMMDDHHMMSSZ` pattern. They are all in UTC.

## [See Also](x509_crl_info_module.md#id6)

> **See also:**
>
> [community.crypto.x509_crl](x509_crl_module.md#ansible-collections-community-crypto-x509-crl-module)
> :   Generate Certificate Revocation Lists (CRLs).
>
> [community.crypto.x509_crl_info](x509_crl_info_filter.md#ansible-collections-community-crypto-x509-crl-info-filter) filter plugin
> :   A filter variant of this module.

## [Examples](x509_crl_info_module.md#id7)

```yaml+jinja
- name: Get information on CRL
  community.crypto.x509_crl_info:
    path: /etc/ssl/my-ca.crl
  register: result

- name: Print the information
  ansible.builtin.debug:
    msg: "{{ result }}"

- name: Get information on CRL without list of revoked certificates
  community.crypto.x509_crl_info:
    path: /etc/ssl/very-large.crl
    list_revoked_certificates: false
  register: result
```

## [Return Values](x509_crl_info_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **digest**  string | The signature algorithm used to sign the CRL.  **Returned:** success  **Sample:** `"sha256WithRSAEncryption"` |
| **format**  string | Whether the CRL is in PEM format (`pem`) or in DER format (`der`).  **Returned:** success  **Can only return:**   - `"pem"` - `"der"`   **Sample:** `"pem"` |
| **issuer**  dictionary | The CRL’s issuer.  Note that for repeated values, only the last one will be returned.  See `name_encoding` for how IDNs are handled.  **Returned:** success  **Sample:** `{"commonName": "ca.example.com", "organizationName": "Ansible"}` |
| **issuer_ordered**  list / elements=list | The CRL’s issuer as an ordered list of tuples.  **Returned:** success  **Sample:** `[["organizationName", "Ansible"], [{"commonName": "ca.example.com"}]]` |
| **last_update**  string | The point in time from which this CRL can be trusted as ASN.1 TIME.  **Returned:** success  **Sample:** `"20190413202428Z"` |
| **next_update**  string | The point in time from which a new CRL will be issued and the client has to check for it as ASN.1 TIME.  **Returned:** success  **Sample:** `"20190413202428Z"` |
| **revoked_certificates**  list / elements=dictionary | List of certificates to be revoked.  **Returned:** success if `list_revoked_certificates=true` |
| **invalidity_date**  string | The point in time it was known/suspected that the private key was compromised or that the certificate otherwise became invalid as ASN.1 TIME.  **Returned:** success  **Sample:** `"20190413202428Z"` |
| **invalidity_date_critical**  boolean | Whether the invalidity date extension is critical.  **Returned:** success  **Sample:** `false` |
| **issuer**  list / elements=string | The certificate’s issuer.  See `name_encoding` for how IDNs are handled.  **Returned:** success  **Sample:** `["DNS:ca.example.org"]` |
| **issuer_critical**  boolean | Whether the certificate issuer extension is critical.  **Returned:** success  **Sample:** `false` |
| **reason**  string | The value for the revocation reason extension.  **Returned:** success  **Can only return:**   - `"unspecified"` - `"key_compromise"` - `"ca_compromise"` - `"affiliation_changed"` - `"superseded"` - `"cessation_of_operation"` - `"certificate_hold"` - `"privilege_withdrawn"` - `"aa_compromise"` - `"remove_from_crl"`   **Sample:** `"key_compromise"` |
| **reason_critical**  boolean | Whether the revocation reason extension is critical.  **Returned:** success  **Sample:** `false` |
| **revocation_date**  string | The point in time the certificate was revoked as ASN.1 TIME.  **Returned:** success  **Sample:** `"20190413202428Z"` |
| **serial_number**  integer | Serial number of the certificate.  **Returned:** success  **Sample:** `1234` |

### Authors

- Felix Fontein (@felixfontein)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.crypto)
- [Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-crypto)
