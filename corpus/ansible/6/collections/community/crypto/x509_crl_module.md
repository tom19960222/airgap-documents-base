---
collection: ansible
version: "6"
title: "community.crypto.x509_crl module – Generate Certificate Revocation Lists (CRLs)"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/crypto/x509_crl_module.html
fetched_at: 2026-07-27T17:06:31+00:00
---
# community.crypto.x509_crl module – Generate Certificate Revocation Lists (CRLs)

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
> see [Requirements](x509_crl_module.md#ansible-collections-community-crypto-x509-crl-module-requirements) for details.
>
> To use it in a playbook, specify: `community.crypto.x509_crl`.

New in community.crypto 1.0.0

- [Synopsis](x509_crl_module.md#synopsis)
- [Requirements](x509_crl_module.md#requirements)
- [Parameters](x509_crl_module.md#parameters)
- [Attributes](x509_crl_module.md#attributes)
- [Notes](x509_crl_module.md#notes)
- [Examples](x509_crl_module.md#examples)
- [Return Values](x509_crl_module.md#return-values)

## [Synopsis](x509_crl_module.md#id1)

- This module allows one to (re)generate or update Certificate Revocation Lists (CRLs).
- Certificates on the revocation list can be either specified by serial number and (optionally) their issuer, or as a path to a certificate file in PEM format.

## [Requirements](x509_crl_module.md#id2)

The below requirements are needed on the host that executes this module.

- If *name_encoding* is set to another value than `ignore`, the [idna Python library](https://pypi.org/project/idna/) needs to be installed.
- cryptography >= 1.2

## [Parameters](x509_crl_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **attributes**  aliases: attr  string | The attributes the resulting filesystem object should have.  To get supported flags look at the man page for *chattr* on the target system.  This string should contain the attributes in the same order as the one displayed by *lsattr*.  The `=` operator is assumed as default, otherwise `+` or `-` operators need to be included in the string. |
| **backup**  boolean | Create a backup file including a timestamp so you can get the original CRL back if you overwrote it with a new one by accident.  Choices:   - `false` ← (default) - `true` |
| **digest**  string | Digest algorithm to be used when signing the CRL.  Default: `"sha256"` |
| **force**  boolean | Should the CRL be forced to be regenerated.  Choices:   - `false` ← (default) - `true` |
| **format**  string | Whether the CRL file should be in PEM or DER format.  If an existing CRL file does match everything but *format*, it will be converted to the correct format instead of regenerated.  Choices:   - `"pem"` ← (default) - `"der"` |
| **group**  string | Name of the group that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current group of the current user unless you are root, in which case it can preserve the previous ownership. |
| **ignore_timestamps**  boolean | Whether the timestamps *last_update*, *next_update* and *revocation_date* (in *revoked_certificates*) should be ignored for idempotency checks. The timestamp *invalidity_date* in *revoked_certificates* will never be ignored.  Use this in combination with relative timestamps for these values to get idempotency.  Choices:   - `false` ← (default) - `true` |
| **issuer**  dictionary | Key/value pairs that will be present in the issuer name field of the CRL.  If you need to specify more than one value with the same key, use a list as value.  If the order of the components is important, use *issuer_ordered*.  One of *issuer* and *issuer_ordered* is required if *state* is `present`.  Mutually exclusive with *issuer_ordered*. |
| **issuer_ordered**  list / elements=dictionary  added in community.crypto 2.0.0 | A list of dictionaries, where every dictionary must contain one key/value pair. This key/value pair will be present in the issuer name field of the CRL.  If you want to specify more than one value with the same key in a row, you can use a list as value.  One of *issuer* and *issuer_ordered* is required if *state* is `present`.  Mutually exclusive with *issuer*. |
| **last_update**  string | The point in time from which this CRL can be trusted.  Time can be specified either as relative time or as absolute timestamp.  Time will always be interpreted as UTC.  Valid format is `[+-]timespec | ASN.1 TIME` where timespec can be an integer + `[w | d | h | m | s]` (for example `+32w1d2h`).  Note that if using relative time this module is NOT idempotent, except when *ignore_timestamps* is set to `true`.  Default: `"+0s"` |
| **mode**  string | Defines how to process entries of existing CRLs.  If set to `generate`, makes sure that the CRL has the exact set of revoked certificates as specified in *revoked_certificates*.  If set to `update`, makes sure that the CRL contains the revoked certificates from *revoked_certificates*, but can also contain other revoked certificates. If the CRL file already exists, all entries from the existing CRL will also be included in the new CRL. When using `update`, you might be interested in setting *ignore_timestamps* to `true`.  Choices:   - `"generate"` ← (default) - `"update"` |
| **name_encoding**  string | How to encode names (DNS names, URIs, email addresses) in return values.  `ignore` will use the encoding returned by the backend.  `idna` will convert all labels of domain names to IDNA encoding. IDNA2008 will be preferred, and IDNA2003 will be used if IDNA2008 encoding fails.  `unicode` will convert all labels of domain names to Unicode. IDNA2008 will be preferred, and IDNA2003 will be used if IDNA2008 decoding fails.  **Note** that `idna` and `unicode` require the [idna Python library](https://pypi.org/project/idna/) to be installed.  Choices:   - `"ignore"` ← (default) - `"idna"` - `"unicode"` |
| **next_update**  string | The absolute latest point in time by which this *issuer* is expected to have issued another CRL. Many clients will treat a CRL as expired once *next_update* occurs.  Time can be specified either as relative time or as absolute timestamp.  Time will always be interpreted as UTC.  Valid format is `[+-]timespec | ASN.1 TIME` where timespec can be an integer + `[w | d | h | m | s]` (for example `+32w1d2h`).  Note that if using relative time this module is NOT idempotent, except when *ignore_timestamps* is set to `true`.  Required if *state* is `present`. |
| **owner**  string | Name of the user that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current user unless you are root, in which case it can preserve the previous ownership. |
| **path**  path / required | Remote absolute path where the generated CRL file should be created or is already located. |
| **privatekey_content**  string | The content of the CA’s private key to use when signing the CRL.  Either *privatekey_path* or *privatekey_content* must be specified if *state* is `present`, but not both. |
| **privatekey_passphrase**  string | The passphrase for the *privatekey_path*.  This is required if the private key is password protected. |
| **privatekey_path**  path | Path to the CA’s private key to use when signing the CRL.  Either *privatekey_path* or *privatekey_content* must be specified if *state* is `present`, but not both. |
| **return_content**  boolean | If set to `true`, will return the (current or generated) CRL’s content as *crl*.  Choices:   - `false` ← (default) - `true` |
| **revoked_certificates**  list / elements=dictionary | List of certificates to be revoked.  Required if *state* is `present`. |
| **content**  string | Content of a certificate in PEM format.  The serial number and issuer will be extracted from the certificate.  Mutually exclusive with *path* and *serial_number*. One of these three options must be specified. |
| **invalidity_date**  string | The point in time it was known/suspected that the private key was compromised or that the certificate otherwise became invalid.  Time can be specified either as relative time or as absolute timestamp.  Time will always be interpreted as UTC.  Valid format is `[+-]timespec | ASN.1 TIME` where timespec can be an integer + `[w | d | h | m | s]` (for example `+32w1d2h`).  Note that if using relative time this module is NOT idempotent. This will NOT change when *ignore_timestamps* is set to `true`. |
| **invalidity_date_critical**  boolean | Whether the invalidity date extension should be critical.  Choices:   - `false` ← (default) - `true` |
| **issuer**  list / elements=string | The certificate’s issuer.  Example: `DNS:ca.example.org` |
| **issuer_critical**  boolean | Whether the certificate issuer extension should be critical.  Choices:   - `false` ← (default) - `true` |
| **path**  path | Path to a certificate in PEM format.  The serial number and issuer will be extracted from the certificate.  Mutually exclusive with *content* and *serial_number*. One of these three options must be specified. |
| **reason**  string | The value for the revocation reason extension.  Choices:   - `"unspecified"` - `"key_compromise"` - `"ca_compromise"` - `"affiliation_changed"` - `"superseded"` - `"cessation_of_operation"` - `"certificate_hold"` - `"privilege_withdrawn"` - `"aa_compromise"` - `"remove_from_crl"` |
| **reason_critical**  boolean | Whether the revocation reason extension should be critical.  Choices:   - `false` ← (default) - `true` |
| **revocation_date**  string | The point in time the certificate was revoked.  Time can be specified either as relative time or as absolute timestamp.  Time will always be interpreted as UTC.  Valid format is `[+-]timespec | ASN.1 TIME` where timespec can be an integer + `[w | d | h | m | s]` (for example `+32w1d2h`).  Note that if using relative time this module is NOT idempotent, except when *ignore_timestamps* is set to `true`.  Default: `"+0s"` |
| **serial_number**  integer | Serial number of the certificate.  Mutually exclusive with *path* and *content*. One of these three options must be specified. |
| **selevel**  string | The level part of the SELinux filesystem object context.  This is the MLS/MCS attribute, sometimes known as the `range`.  When set to `_default`, it will use the `level` portion of the policy if available. |
| **serole**  string | The role part of the SELinux filesystem object context.  When set to `_default`, it will use the `role` portion of the policy if available. |
| **setype**  string | The type part of the SELinux filesystem object context.  When set to `_default`, it will use the `type` portion of the policy if available. |
| **seuser**  string | The user part of the SELinux filesystem object context.  By default it uses the `system` policy, where applicable.  When set to `_default`, it will use the `user` portion of the policy if available. |
| **state**  string | Whether the CRL file should exist or not, taking action if the state is different from what is stated.  Choices:   - `"absent"` - `"present"` ← (default) |
| **unsafe_writes**  boolean | Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target filesystem object.  By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target filesystem objects, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted filesystem objects, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.  This option allows Ansible to fall back to unsafe methods of updating filesystem objects when atomic operations fail (however, it doesn’t force Ansible to perform unsafe writes).  IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.  Choices:   - `false` ← (default) - `true` |

## [Attributes](x509_crl_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support: full | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |
| **safe_file_operations** | Support: full | Uses Ansible’s strict file operation functions to ensure proper permissions and avoid data corruption. |

## [Notes](x509_crl_module.md#id5)

> **Note:**
>
> - All ASN.1 TIME values should be specified following the YYYYMMDDHHMMSSZ pattern.
> - Date specified should be UTC. Minutes and seconds are mandatory.

## [Examples](x509_crl_module.md#id6)

```yaml+jinja
- name: Generate a CRL
  community.crypto.x509_crl:
    path: /etc/ssl/my-ca.crl
    privatekey_path: /etc/ssl/private/my-ca.pem
    issuer:
      CN: My CA
    last_update: "+0s"
    next_update: "+7d"
    revoked_certificates:
      - serial_number: 1234
        revocation_date: 20190331202428Z
        issuer:
          CN: My CA
      - serial_number: 2345
        revocation_date: 20191013152910Z
        reason: affiliation_changed
        invalidity_date: 20191001000000Z
      - path: /etc/ssl/crt/revoked-cert.pem
        revocation_date: 20191010010203Z
```

## [Return Values](x509_crl_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_file**  string | Name of backup file created.  Returned: changed and if *backup* is `true`  Sample: `"/path/to/my-ca.crl.2019-03-09@11:22~"` |
| **crl**  string | The (current or generated) CRL’s content.  Will be the CRL itself if *format* is `pem`, and Base64 of the CRL if *format* is `der`.  Returned: if *state* is `present` and *return_content* is `true` |
| **digest**  string | The signature algorithm used to sign the CRL.  Returned: success  Sample: `"sha256WithRSAEncryption"` |
| **filename**  string | Path to the generated CRL.  Returned: changed or success  Sample: `"/path/to/my-ca.crl"` |
| **format**  string | Whether the CRL is in PEM format (`pem`) or in DER format (`der`).  Returned: success  Sample: `"pem"` |
| **issuer**  dictionary | The CRL’s issuer.  Note that for repeated values, only the last one will be returned.  See *name_encoding* for how IDNs are handled.  Returned: success  Sample: `{"commonName": "ca.example.com", "organizationName": "Ansible"}` |
| **issuer_ordered**  list / elements=list | The CRL’s issuer as an ordered list of tuples.  Returned: success  Sample: `[["organizationName", "Ansible"], [{"commonName": "ca.example.com"}]]` |
| **last_update**  string | The point in time from which this CRL can be trusted as ASN.1 TIME.  Returned: success  Sample: `"20190413202428Z"` |
| **next_update**  string | The point in time from which a new CRL will be issued and the client has to check for it as ASN.1 TIME.  Returned: success  Sample: `"20190413202428Z"` |
| **privatekey**  string | Path to the private CA key.  Returned: changed or success  Sample: `"/path/to/my-ca.pem"` |
| **revoked_certificates**  list / elements=dictionary | List of certificates to be revoked.  Returned: success |
| **invalidity_date**  string | The point in time it was known/suspected that the private key was compromised or that the certificate otherwise became invalid as ASN.1 TIME.  Returned: success  Sample: `"20190413202428Z"` |
| **invalidity_date_critical**  boolean | Whether the invalidity date extension is critical.  Returned: success  Sample: `false` |
| **issuer**  list / elements=string | The certificate’s issuer.  See *name_encoding* for how IDNs are handled.  Returned: success  Sample: `["DNS:ca.example.org"]` |
| **issuer_critical**  boolean | Whether the certificate issuer extension is critical.  Returned: success  Sample: `false` |
| **reason**  string | The value for the revocation reason extension.  One of `unspecified`, `key_compromise`, `ca_compromise`, `affiliation_changed`, `superseded`, `cessation_of_operation`, `certificate_hold`, `privilege_withdrawn`, `aa_compromise`, and `remove_from_crl`.  Returned: success  Sample: `"key_compromise"` |
| **reason_critical**  boolean | Whether the revocation reason extension is critical.  Returned: success  Sample: `false` |
| **revocation_date**  string | The point in time the certificate was revoked as ASN.1 TIME.  Returned: success  Sample: `"20190413202428Z"` |
| **serial_number**  integer | Serial number of the certificate.  Returned: success  Sample: `1234` |

### Authors

- Felix Fontein (@felixfontein)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.crypto)
[Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-crypto)
