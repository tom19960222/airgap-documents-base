---
collection: ansible
version: "6"
title: "community.crypto.x509_certificate_pipe module – Generate and/or check OpenSSL certificates"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/crypto/x509_certificate_pipe_module.html
fetched_at: 2026-07-27T17:06:30+00:00
---
# community.crypto.x509_certificate_pipe module – Generate and/or check OpenSSL certificates

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
> see [Requirements](x509_certificate_pipe_module.md#ansible-collections-community-crypto-x509-certificate-pipe-module-requirements) for details.
>
> To use it in a playbook, specify: `community.crypto.x509_certificate_pipe`.

New in community.crypto 1.3.0

- [Synopsis](x509_certificate_pipe_module.md#synopsis)
- [Requirements](x509_certificate_pipe_module.md#requirements)
- [Parameters](x509_certificate_pipe_module.md#parameters)
- [Attributes](x509_certificate_pipe_module.md#attributes)
- [Notes](x509_certificate_pipe_module.md#notes)
- [See Also](x509_certificate_pipe_module.md#see-also)
- [Examples](x509_certificate_pipe_module.md#examples)
- [Return Values](x509_certificate_pipe_module.md#return-values)

## [Synopsis](x509_certificate_pipe_module.md#id1)

- It implements a notion of provider (ie. `selfsigned`, `ownca`, `entrust`) for your certificate.
- It uses the cryptography python library to interact with OpenSSL.
- Please note that the module regenerates an existing certificate if it does not match the module’s options, or if it seems to be corrupt. If you are concerned that this could overwrite your existing certificate, consider using the *backup* option.
- The `ownca` provider is intended for generating an OpenSSL certificate signed with your own CA (Certificate Authority) certificate (self-signed certificate).
- This module allows one to (re)generate OpenSSL certificates.

## [Requirements](x509_certificate_pipe_module.md#id2)

The below requirements are needed on the host that executes this module.

- cryptography >= 1.6 (if using `selfsigned` or `ownca` provider)

## [Parameters](x509_certificate_pipe_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **content**  string | The existing certificate. |
| **csr_content**  string | Content of the Certificate Signing Request (CSR) used to generate this certificate.  This is mutually exclusive with *csr_path*. |
| **csr_path**  path | Path to the Certificate Signing Request (CSR) used to generate this certificate.  This is mutually exclusive with *csr_content*. |
| **entrust_api_client_cert_key_path**  path | The path to the private key of the client certificate used to authenticate to the Entrust Certificate Services (ECS) API.  This is only used by the `entrust` provider.  This is required if the provider is `entrust`. |
| **entrust_api_client_cert_path**  path | The path to the client certificate used to authenticate to the Entrust Certificate Services (ECS) API.  This is only used by the `entrust` provider.  This is required if the provider is `entrust`. |
| **entrust_api_key**  string | The key (password) for authentication to the Entrust Certificate Services (ECS) API.  This is only used by the `entrust` provider.  This is required if the provider is `entrust`. |
| **entrust_api_specification_path**  path | The path to the specification file defining the Entrust Certificate Services (ECS) API configuration.  You can use this to keep a local copy of the specification to avoid downloading it every time the module is used.  This is only used by the `entrust` provider.  Default: `"https://cloud.entrust.net/EntrustCloud/documentation/cms-api-2.1.0.yaml"` |
| **entrust_api_user**  string | The username for authentication to the Entrust Certificate Services (ECS) API.  This is only used by the `entrust` provider.  This is required if the provider is `entrust`. |
| **entrust_cert_type**  string | Specify the type of certificate requested.  This is only used by the `entrust` provider.  Choices:   - `"STANDARD_SSL"` ← (default) - `"ADVANTAGE_SSL"` - `"UC_SSL"` - `"EV_SSL"` - `"WILDCARD_SSL"` - `"PRIVATE_SSL"` - `"PD_SSL"` - `"CDS_ENT_LITE"` - `"CDS_ENT_PRO"` - `"SMIME_ENT"` |
| **entrust_not_after**  string | The point in time at which the certificate stops being valid.  Time can be specified either as relative time or as an absolute timestamp.  A valid absolute time format is `ASN.1 TIME` such as `2019-06-18`.  A valid relative time format is `[+-]timespec` where timespec can be an integer + `[w | d | h | m | s]`, such as `+365d` or `+32w1d2h`).  Time will always be interpreted as UTC.  Note that only the date (day, month, year) is supported for specifying the expiry date of the issued certificate.  The full date-time is adjusted to EST (GMT -5:00) before issuance, which may result in a certificate with an expiration date one day earlier than expected if a relative time is used.  The minimum certificate lifetime is 90 days, and maximum is three years.  If this value is not specified, the certificate will stop being valid 365 days the date of issue.  This is only used by the `entrust` provider.  Please note that this value is **not** covered by the *ignore_timestamps* option.  Default: `"+365d"` |
| **entrust_requester_email**  string | The email of the requester of the certificate (for tracking purposes).  This is only used by the `entrust` provider.  This is required if the provider is `entrust`. |
| **entrust_requester_name**  string | The name of the requester of the certificate (for tracking purposes).  This is only used by the `entrust` provider.  This is required if the provider is `entrust`. |
| **entrust_requester_phone**  string | The phone number of the requester of the certificate (for tracking purposes).  This is only used by the `entrust` provider.  This is required if the provider is `entrust`. |
| **force**  boolean | Generate the certificate, even if it already exists.  Choices:   - `false` ← (default) - `true` |
| **ignore_timestamps**  boolean  added in community.crypto 2.0.0 | Whether the “not before” and “not after” timestamps should be ignored for idempotency checks.  It is better to keep the default value `true` when using relative timestamps (like `+0s` for now).  Choices:   - `false` - `true` ← (default) |
| **ownca_content**  string | Content of the CA (Certificate Authority) certificate.  This is only used by the `ownca` provider.  This is mutually exclusive with *ownca_path*. |
| **ownca_create_authority_key_identifier**  boolean | Create a Authority Key Identifier from the CA’s certificate. If the CSR provided a authority key identifier, it is ignored.  The Authority Key Identifier is generated from the CA certificate’s Subject Key Identifier, if available. If it is not available, the CA certificate’s public key will be used.  This is only used by the `ownca` provider.  Note that this is only supported if the `cryptography` backend is used!  Choices:   - `false` - `true` ← (default) |
| **ownca_create_subject_key_identifier**  string | Whether to create the Subject Key Identifier (SKI) from the public key.  A value of `create_if_not_provided` (default) only creates a SKI when the CSR does not provide one.  A value of `always_create` always creates a SKI. If the CSR provides one, that one is ignored.  A value of `never_create` never creates a SKI. If the CSR provides one, that one is used.  This is only used by the `ownca` provider.  Note that this is only supported if the `cryptography` backend is used!  Choices:   - `"create_if_not_provided"` ← (default) - `"always_create"` - `"never_create"` |
| **ownca_digest**  string | The digest algorithm to be used for the `ownca` certificate.  This is only used by the `ownca` provider.  Default: `"sha256"` |
| **ownca_not_after**  string | The point in time at which the certificate stops being valid.  Time can be specified either as relative time or as absolute timestamp.  Time will always be interpreted as UTC.  Valid format is `[+-]timespec | ASN.1 TIME` where timespec can be an integer + `[w | d | h | m | s]` (for example `+32w1d2h`).  If this value is not specified, the certificate will stop being valid 10 years from now.  Note that this value is **not used to determine whether an existing certificate should be regenerated**. This can be changed by setting the *ignore_timestamps* option to `false`. Please note that you should avoid relative timestamps when setting *ignore_timestamps=false*.  This is only used by the `ownca` provider.  On macOS 10.15 and onwards, TLS server certificates must have a validity period of 825 days or fewer. Please see <https://support.apple.com/en-us/HT210176> for more details.  Default: `"+3650d"` |
| **ownca_not_before**  string | The point in time the certificate is valid from.  Time can be specified either as relative time or as absolute timestamp.  Time will always be interpreted as UTC.  Valid format is `[+-]timespec | ASN.1 TIME` where timespec can be an integer + `[w | d | h | m | s]` (for example `+32w1d2h`).  If this value is not specified, the certificate will start being valid from now.  Note that this value is **not used to determine whether an existing certificate should be regenerated**. This can be changed by setting the *ignore_timestamps* option to `false`. Please note that you should avoid relative timestamps when setting *ignore_timestamps=false*.  This is only used by the `ownca` provider.  Default: `"+0s"` |
| **ownca_path**  path | Remote absolute path of the CA (Certificate Authority) certificate.  This is only used by the `ownca` provider.  This is mutually exclusive with *ownca_content*. |
| **ownca_privatekey_content**  string | Content of the CA (Certificate Authority) private key to use when signing the certificate.  This is only used by the `ownca` provider.  This is mutually exclusive with *ownca_privatekey_path*. |
| **ownca_privatekey_passphrase**  string | The passphrase for the *ownca_privatekey_path* resp. *ownca_privatekey_content*.  This is only used by the `ownca` provider. |
| **ownca_privatekey_path**  path | Path to the CA (Certificate Authority) private key to use when signing the certificate.  This is only used by the `ownca` provider.  This is mutually exclusive with *ownca_privatekey_content*. |
| **ownca_version**  integer | The version of the `ownca` certificate.  Nowadays it should almost always be `3`.  This is only used by the `ownca` provider.  Default: `3` |
| **privatekey_content**  string | Path to the private key to use when signing the certificate.  This is mutually exclusive with *privatekey_path*. |
| **privatekey_passphrase**  string | The passphrase for the *privatekey_path* resp. *privatekey_content*.  This is required if the private key is password protected. |
| **privatekey_path**  path | Path to the private key to use when signing the certificate.  This is mutually exclusive with *privatekey_content*. |
| **provider**  string / required | Name of the provider to use to generate/retrieve the OpenSSL certificate.  The `entrust` provider requires credentials for the [Entrust Certificate Services](https://www.entrustdatacard.com/products/categories/ssl-certificates) (ECS) API.  Choices:   - `"entrust"` - `"ownca"` - `"selfsigned"` |
| **select_crypto_backend**  string | Determines which crypto backend to use.  The default choice is `auto`, which tries to use `cryptography` if available.  If set to `cryptography`, will try to use the [cryptography](https://cryptography.io/) library.  Choices:   - `"auto"` ← (default) - `"cryptography"` |
| **selfsigned_create_subject_key_identifier**  string | Whether to create the Subject Key Identifier (SKI) from the public key.  A value of `create_if_not_provided` (default) only creates a SKI when the CSR does not provide one.  A value of `always_create` always creates a SKI. If the CSR provides one, that one is ignored.  A value of `never_create` never creates a SKI. If the CSR provides one, that one is used.  This is only used by the `selfsigned` provider.  Note that this is only supported if the `cryptography` backend is used!  Choices:   - `"create_if_not_provided"` ← (default) - `"always_create"` - `"never_create"` |
| **selfsigned_digest**  string | Digest algorithm to be used when self-signing the certificate.  This is only used by the `selfsigned` provider.  Default: `"sha256"` |
| **selfsigned_not_after**  aliases: selfsigned_notAfter  string | The point in time at which the certificate stops being valid.  Time can be specified either as relative time or as absolute timestamp.  Time will always be interpreted as UTC.  Valid format is `[+-]timespec | ASN.1 TIME` where timespec can be an integer + `[w | d | h | m | s]` (for example `+32w1d2h`).  If this value is not specified, the certificate will stop being valid 10 years from now.  Note that this value is **not used to determine whether an existing certificate should be regenerated**. This can be changed by setting the *ignore_timestamps* option to `false`. Please note that you should avoid relative timestamps when setting *ignore_timestamps=false*.  This is only used by the `selfsigned` provider.  On macOS 10.15 and onwards, TLS server certificates must have a validity period of 825 days or fewer. Please see <https://support.apple.com/en-us/HT210176> for more details.  Default: `"+3650d"` |
| **selfsigned_not_before**  aliases: selfsigned_notBefore  string | The point in time the certificate is valid from.  Time can be specified either as relative time or as absolute timestamp.  Time will always be interpreted as UTC.  Valid format is `[+-]timespec | ASN.1 TIME` where timespec can be an integer + `[w | d | h | m | s]` (for example `+32w1d2h`).  If this value is not specified, the certificate will start being valid from now.  Note that this value is **not used to determine whether an existing certificate should be regenerated**. This can be changed by setting the *ignore_timestamps* option to `false`. Please note that you should avoid relative timestamps when setting *ignore_timestamps=false*.  This is only used by the `selfsigned` provider.  Default: `"+0s"` |
| **selfsigned_version**  integer | Version of the `selfsigned` certificate.  Nowadays it should almost always be `3`.  This is only used by the `selfsigned` provider.  Default: `3` |

## [Attributes](x509_certificate_pipe_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support: full | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](x509_certificate_pipe_module.md#id5)

> **Note:**
>
> - All ASN.1 TIME values should be specified following the YYYYMMDDHHMMSSZ pattern.
> - Date specified should be UTC. Minutes and seconds are mandatory.
> - For security reason, when you use `ownca` provider, you should NOT run [community.crypto.x509_certificate](x509_certificate_module.md#ansible-collections-community-crypto-x509-certificate-module) on a target machine, but on a dedicated CA machine. It is recommended not to store the CA private key on the target machine. Once signed, the certificate can be moved to the target machine.
> - For the `selfsigned` provider, *csr_path* and *csr_content* are optional. If not provided, a certificate without any information (Subject, Subject Alternative Names, Key Usage, etc.) is created.

## [See Also](x509_certificate_pipe_module.md#id6)

> **See also:**
>
> [community.crypto.x509_certificate](x509_certificate_module.md#ansible-collections-community-crypto-x509-certificate-module)
> :   Generate and/or check OpenSSL certificates.
>
> [community.crypto.openssl_csr](openssl_csr_module.md#ansible-collections-community-crypto-openssl-csr-module)
> :   Generate OpenSSL Certificate Signing Request (CSR).
>
> [community.crypto.openssl_csr_pipe](openssl_csr_pipe_module.md#ansible-collections-community-crypto-openssl-csr-pipe-module)
> :   Generate OpenSSL Certificate Signing Request (CSR).
>
> [community.crypto.openssl_dhparam](openssl_dhparam_module.md#ansible-collections-community-crypto-openssl-dhparam-module)
> :   Generate OpenSSL Diffie-Hellman Parameters.
>
> [community.crypto.openssl_pkcs12](openssl_pkcs12_module.md#ansible-collections-community-crypto-openssl-pkcs12-module)
> :   Generate OpenSSL PKCS#12 archive.
>
> [community.crypto.openssl_privatekey](openssl_privatekey_module.md#ansible-collections-community-crypto-openssl-privatekey-module)
> :   Generate OpenSSL private keys.
>
> [community.crypto.openssl_privatekey_pipe](openssl_privatekey_pipe_module.md#ansible-collections-community-crypto-openssl-privatekey-pipe-module)
> :   Generate OpenSSL private keys without disk access.
>
> [community.crypto.openssl_publickey](openssl_publickey_module.md#ansible-collections-community-crypto-openssl-publickey-module)
> :   Generate an OpenSSL public key from its private key.

## [Examples](x509_certificate_pipe_module.md#id7)

```yaml+jinja
- name: Generate a Self Signed OpenSSL certificate
  community.crypto.x509_certificate_pipe:
    provider: selfsigned
    privatekey_path: /etc/ssl/private/ansible.com.pem
    csr_path: /etc/ssl/csr/ansible.com.csr
  register: result
- name: Print the certificate
  ansible.builtin.debug:
    var: result.certificate

# In the following example, both CSR and certificate file are stored on the
# machine where ansible-playbook is executed, while the OwnCA data (certificate,
# private key) are stored on the remote machine.

- name: (1/2) Generate an OpenSSL Certificate with the CSR provided inline
  community.crypto.x509_certificate_pipe:
    provider: ownca
    content: "{{ lookup('file', '/etc/ssl/csr/www.ansible.com.crt') }}"
    csr_content: "{{ lookup('file', '/etc/ssl/csr/www.ansible.com.csr') }}"
    ownca_cert: /path/to/ca_cert.crt
    ownca_privatekey: /path/to/ca_cert.key
    ownca_privatekey_passphrase: hunter2
  register: result

- name: (2/2) Store certificate
  ansible.builtin.copy:
    dest: /etc/ssl/csr/www.ansible.com.crt
    content: "{{ result.certificate }}"
  delegate_to: localhost
  when: result is changed

# In the following example, the certificate from another machine is signed by
# our OwnCA whose private key and certificate are only available on this
# machine (where ansible-playbook is executed), without having to write
# the certificate file to disk on localhost. The CSR could have been
# provided by community.crypto.openssl_csr_pipe earlier, or also have been
# read from the remote machine.

- name: (1/3) Read certificate's contents from remote machine
  ansible.builtin.slurp:
    src: /etc/ssl/csr/www.ansible.com.crt
  register: certificate_content

- name: (2/3) Generate an OpenSSL Certificate with the CSR provided inline
  community.crypto.x509_certificate_pipe:
    provider: ownca
    content: "{{ certificate_content.content | b64decode }}"
    csr_content: "{{ the_csr }}"
    ownca_cert: /path/to/ca_cert.crt
    ownca_privatekey: /path/to/ca_cert.key
    ownca_privatekey_passphrase: hunter2
  delegate_to: localhost
  register: result

- name: (3/3) Store certificate
  ansible.builtin.copy:
    dest: /etc/ssl/csr/www.ansible.com.crt
    content: "{{ result.certificate }}"
  when: result is changed
```

## [Return Values](x509_certificate_pipe_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **certificate**  string | The (current or generated) certificate’s content.  Returned: changed or success |

### Authors

- Yanis Guenane (@Spredzy)
- Markus Teufelberger (@MarkusTeufelberger)
- Felix Fontein (@felixfontein)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.crypto)
[Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-crypto)
