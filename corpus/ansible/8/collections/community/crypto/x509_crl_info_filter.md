---
collection: ansible
version: "8"
title: "community.crypto.x509_crl_info filter – Retrieve information from X.509 CRLs in PEM format"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/crypto/x509_crl_info_filter.html
fetched_at: 2026-07-28T01:42:48+00:00
---
# community.crypto.x509_crl_info filter – Retrieve information from X.509 CRLs in PEM format

> **Note:**
>
> This filter plugin is part of the [community.crypto collection](https://galaxy.ansible.com/ui/repo/published/community/crypto/) (version 2.16.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.crypto`.
> You need further requirements to be able to use this filter plugin,
> see [Requirements](x509_crl_info_filter.md#ansible-collections-community-crypto-x509-crl-info-filter-requirements) for details.
>
> To use it in a playbook, specify: `community.crypto.x509_crl_info`.

New in community.crypto 2.10.0

- [Synopsis](x509_crl_info_filter.md#synopsis)
- [Requirements](x509_crl_info_filter.md#requirements)
- [Input](x509_crl_info_filter.md#input)
- [Keyword parameters](x509_crl_info_filter.md#keyword-parameters)
- [See Also](x509_crl_info_filter.md#see-also)
- [Examples](x509_crl_info_filter.md#examples)
- [Return Value](x509_crl_info_filter.md#return-value)

## [Synopsis](x509_crl_info_filter.md#id1)

- Provided a X.509 crl in PEM format, retrieve information.
- This is a filter version of the [community.crypto.x509_crl_info](x509_crl_info_module.md#ansible-collections-community-crypto-x509-crl-info-module) module.

## [Requirements](x509_crl_info_filter.md#id2)

The below requirements are needed on the local controller node that executes this filter.

- If `name_encoding` is set to another value than `ignore`, the [idna Python library](https://pypi.org/project/idna/) needs to be installed.

## [Input](x509_crl_info_filter.md#id3)

This describes the input of the filter, the value before `| community.crypto.x509_crl_info`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | The content of the X.509 CRL in PEM format. |

## [Keyword parameters](x509_crl_info_filter.md#id4)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | community.crypto.x509_crl_info(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **list_revoked_certificates**  boolean  *added in community.crypto 1.7.0* | If set to `false`, the list of revoked certificates is not included in the result.  This is useful when retrieving information on large CRL files. Enumerating all revoked certificates can take some time, including serializing the result as JSON, sending it to the Ansible controller, and decoding it again.  **Choices:**   - `false` - `true` ← (default) |
| **name_encoding**  string | How to encode names (DNS names, URIs, email addresses) in return values.  `ignore` will use the encoding returned by the backend.  `idna` will convert all labels of domain names to IDNA encoding. IDNA2008 will be preferred, and IDNA2003 will be used if IDNA2008 encoding fails.  `unicode` will convert all labels of domain names to Unicode. IDNA2008 will be preferred, and IDNA2003 will be used if IDNA2008 decoding fails.  **Note** that `idna` and `unicode` require the [idna Python library](https://pypi.org/project/idna/) to be installed.  **Choices:**   - `"ignore"` ← (default) - `"idna"` - `"unicode"` |

## [See Also](x509_crl_info_filter.md#id5)

> **See also:**
>
> [community.crypto.x509_crl_info](x509_crl_info_module.md#ansible-collections-community-crypto-x509-crl-info-module)
> :   Retrieve information on Certificate Revocation Lists (CRLs).

## [Examples](x509_crl_info_filter.md#id6)

```yaml+jinja
- name: Show the Organization Name of the CRL's subject
  ansible.builtin.debug:
    msg: >-
      {{
        (
          lookup('ansible.builtin.file', '/path/to/cert.pem')
          | community.crypto.x509_crl_info
        ).issuer.organizationName
      }}
```

## [Return Value](x509_crl_info_filter.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  dictionary | Information on the CRL.  **Returned:** success |
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

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.crypto)
- [Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-crypto)
