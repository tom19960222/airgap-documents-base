---
collection: ansible
version: "6"
title: "community.crypto.openssl_csr_pipe module – Generate OpenSSL Certificate Signing Request (CSR)"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/crypto/openssl_csr_pipe_module.html
fetched_at: 2026-07-27T17:06:21+00:00
---
# community.crypto.openssl_csr_pipe module – Generate OpenSSL Certificate Signing Request (CSR)

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
> see [Requirements](openssl_csr_pipe_module.md#ansible-collections-community-crypto-openssl-csr-pipe-module-requirements) for details.
>
> To use it in a playbook, specify: `community.crypto.openssl_csr_pipe`.

New in community.crypto 1.3.0

- [Synopsis](openssl_csr_pipe_module.md#synopsis)
- [Requirements](openssl_csr_pipe_module.md#requirements)
- [Parameters](openssl_csr_pipe_module.md#parameters)
- [Attributes](openssl_csr_pipe_module.md#attributes)
- [Notes](openssl_csr_pipe_module.md#notes)
- [See Also](openssl_csr_pipe_module.md#see-also)
- [Examples](openssl_csr_pipe_module.md#examples)
- [Return Values](openssl_csr_pipe_module.md#return-values)

## [Synopsis](openssl_csr_pipe_module.md#id1)

- Please note that the module regenerates an existing CSR if it does not match the module’s options, or if it seems to be corrupt.
- This module allows one to (re)generate OpenSSL certificate signing requests.
- This module supports the subjectAltName, keyUsage, extendedKeyUsage, basicConstraints and OCSP Must Staple extensions.

## [Requirements](openssl_csr_pipe_module.md#id2)

The below requirements are needed on the host that executes this module.

- cryptography >= 1.3

## [Parameters](openssl_csr_pipe_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **authority_cert_issuer**  list / elements=string | Names that will be present in the authority cert issuer field of the certificate signing request.  Values must be prefixed by their options. (i.e., `email`, `URI`, `DNS`, `RID`, `IP`, `dirName`, `otherName` and the ones specific to your CA)  Example: `DNS:ca.example.org`  If specified, *authority_cert_serial_number* must also be specified.  Please note that commercial CAs ignore this value, respectively use a value of their own choice. Specifying this option is mostly useful for self-signed certificates or for own CAs.  Note that this is only supported if the `cryptography` backend is used!  The `AuthorityKeyIdentifier` extension will only be added if at least one of *authority_key_identifier*, *authority_cert_issuer* and *authority_cert_serial_number* is specified. |
| **authority_cert_serial_number**  integer | The authority cert serial number.  If specified, *authority_cert_issuer* must also be specified.  Note that this is only supported if the `cryptography` backend is used!  Please note that commercial CAs ignore this value, respectively use a value of their own choice. Specifying this option is mostly useful for self-signed certificates or for own CAs.  The `AuthorityKeyIdentifier` extension will only be added if at least one of *authority_key_identifier*, *authority_cert_issuer* and *authority_cert_serial_number* is specified. |
| **authority_key_identifier**  string | The authority key identifier as a hex string, where two bytes are separated by colons.  Example: `00:11:22:33:44:55:66:77:88:99:aa:bb:cc:dd:ee:ff:00:11:22:33`  Please note that commercial CAs ignore this value, respectively use a value of their own choice. Specifying this option is mostly useful for self-signed certificates or for own CAs.  Note that this is only supported if the `cryptography` backend is used!  The `AuthorityKeyIdentifier` extension will only be added if at least one of *authority_key_identifier*, *authority_cert_issuer* and *authority_cert_serial_number* is specified. |
| **basic_constraints**  aliases: basicConstraints  list / elements=string | Indicates basic constraints, such as if the certificate is a CA. |
| **basic_constraints_critical**  aliases: basicConstraints_critical  boolean | Should the basicConstraints extension be considered as critical.  Choices:   - `false` ← (default) - `true` |
| **common_name**  aliases: CN, commonName  string | The commonName field of the certificate signing request subject. |
| **content**  string | The existing CSR. |
| **country_name**  aliases: C, countryName  string | The countryName field of the certificate signing request subject. |
| **create_subject_key_identifier**  boolean | Create the Subject Key Identifier from the public key.  Please note that commercial CAs can ignore the value, respectively use a value of their own choice instead. Specifying this option is mostly useful for self-signed certificates or for own CAs.  Note that this is only supported if the `cryptography` backend is used!  Choices:   - `false` ← (default) - `true` |
| **crl_distribution_points**  list / elements=dictionary  added in community.crypto 1.4.0 | Allows to specify one or multiple CRL distribution points.  Only supported by the `cryptography` backend. |
| **crl_issuer**  list / elements=string | Information about the issuer of the CRL. |
| **full_name**  list / elements=string | Describes how the CRL can be retrieved.  Mutually exclusive with *relative_name*.  Example: `URI:https://ca.example.com/revocations.crl`. |
| **reasons**  list / elements=string | List of reasons that this distribution point can be used for when performing revocation checks.  Choices:   - `"key_compromise"` - `"ca_compromise"` - `"affiliation_changed"` - `"superseded"` - `"cessation_of_operation"` - `"certificate_hold"` - `"privilege_withdrawn"` - `"aa_compromise"` |
| **relative_name**  list / elements=string | Describes how the CRL can be retrieved relative to the CRL issuer.  Mutually exclusive with *full_name*.  Example: `/CN=example.com`.  Can only be used when cryptography >= 1.6 is installed. |
| **digest**  string | The digest used when signing the certificate signing request with the private key.  Default: `"sha256"` |
| **email_address**  aliases: E, emailAddress  string | The emailAddress field of the certificate signing request subject. |
| **extended_key_usage**  aliases: extKeyUsage, extendedKeyUsage  list / elements=string | Additional restrictions (for example client authentication, server authentication) on the allowed purposes for which the public key may be used. |
| **extended_key_usage_critical**  aliases: extKeyUsage_critical, extendedKeyUsage_critical  boolean | Should the extkeyUsage extension be considered as critical.  Choices:   - `false` ← (default) - `true` |
| **key_usage**  aliases: keyUsage  list / elements=string | This defines the purpose (for example encipherment, signature, certificate signing) of the key contained in the certificate. |
| **key_usage_critical**  aliases: keyUsage_critical  boolean | Should the keyUsage extension be considered as critical.  Choices:   - `false` ← (default) - `true` |
| **locality_name**  aliases: L, localityName  string | The localityName field of the certificate signing request subject. |
| **name_constraints_critical**  boolean | Should the Name Constraints extension be considered as critical.  Choices:   - `false` ← (default) - `true` |
| **name_constraints_excluded**  list / elements=string | For CA certificates, this specifies a list of identifiers which describe subtrees of names that this CA is **not** allowed to issue certificates for.  Values must be prefixed by their options. (i.e., `email`, `URI`, `DNS`, `RID`, `IP`, `dirName`, `otherName` and the ones specific to your CA). |
| **name_constraints_permitted**  list / elements=string | For CA certificates, this specifies a list of identifiers which describe subtrees of names that this CA is allowed to issue certificates for.  Values must be prefixed by their options. (i.e., `email`, `URI`, `DNS`, `RID`, `IP`, `dirName`, `otherName` and the ones specific to your CA). |
| **ocsp_must_staple**  aliases: ocspMustStaple  boolean | Indicates that the certificate should contain the OCSP Must Staple extension (<https://tools.ietf.org/html/rfc7633>).  Choices:   - `false` ← (default) - `true` |
| **ocsp_must_staple_critical**  aliases: ocspMustStaple_critical  boolean | Should the OCSP Must Staple extension be considered as critical.  Note that according to the RFC, this extension should not be marked as critical, as old clients not knowing about OCSP Must Staple are required to reject such certificates (see <https://tools.ietf.org/html/rfc7633#section-4>).  Choices:   - `false` ← (default) - `true` |
| **organization_name**  aliases: O, organizationName  string | The organizationName field of the certificate signing request subject. |
| **organizational_unit_name**  aliases: OU, organizationalUnitName  string | The organizationalUnitName field of the certificate signing request subject. |
| **privatekey_content**  string | The content of the private key to use when signing the certificate signing request.  Either *privatekey_path* or *privatekey_content* must be specified if *state* is `present`, but not both. |
| **privatekey_passphrase**  string | The passphrase for the private key.  This is required if the private key is password protected. |
| **privatekey_path**  path | The path to the private key to use when signing the certificate signing request.  Either *privatekey_path* or *privatekey_content* must be specified if *state* is `present`, but not both. |
| **select_crypto_backend**  string | Determines which crypto backend to use.  The default choice is `auto`, which tries to use `cryptography` if available.  If set to `cryptography`, will try to use the [cryptography](https://cryptography.io/) library.  Choices:   - `"auto"` ← (default) - `"cryptography"` |
| **state_or_province_name**  aliases: ST, stateOrProvinceName  string | The stateOrProvinceName field of the certificate signing request subject. |
| **subject**  dictionary | Key/value pairs that will be present in the subject name field of the certificate signing request.  If you need to specify more than one value with the same key, use a list as value.  If the order of the components is important, use *subject_ordered*.  Mutually exclusive with *subject_ordered*. |
| **subject_alt_name**  aliases: subjectAltName  list / elements=string | Subject Alternative Name (SAN) extension to attach to the certificate signing request.  Values must be prefixed by their options. (These are `email`, `URI`, `DNS`, `RID`, `IP`, `dirName`, `otherName`, and the ones specific to your CA).  Note that if no SAN is specified, but a common name, the common name will be added as a SAN except if `useCommonNameForSAN` is set to *false*.  More at <https://tools.ietf.org/html/rfc5280#section-4.2.1.6>. |
| **subject_alt_name_critical**  aliases: subjectAltName_critical  boolean | Should the subjectAltName extension be considered as critical.  Choices:   - `false` ← (default) - `true` |
| **subject_key_identifier**  string | The subject key identifier as a hex string, where two bytes are separated by colons.  Example: `00:11:22:33:44:55:66:77:88:99:aa:bb:cc:dd:ee:ff:00:11:22:33`  Please note that commercial CAs ignore this value, respectively use a value of their own choice. Specifying this option is mostly useful for self-signed certificates or for own CAs.  Note that this option can only be used if *create_subject_key_identifier* is `false`.  Note that this is only supported if the `cryptography` backend is used! |
| **subject_ordered**  list / elements=dictionary  added in community.crypto 2.0.0 | A list of dictionaries, where every dictionary must contain one key/value pair. This key/value pair will be present in the subject name field of the certificate signing request.  If you want to specify more than one value with the same key in a row, you can use a list as value.  Mutually exclusive with *subject*, and any other subject field option, such as *country_name*, *state_or_province_name*, *locality_name*, *organization_name*, *organizational_unit_name*, *common_name*, or *email_address*. |
| **use_common_name_for_san**  aliases: useCommonNameForSAN  boolean | If set to `true`, the module will fill the common name in for `subject_alt_name` with `DNS:` prefix if no SAN is specified.  Choices:   - `false` - `true` ← (default) |
| **version**  integer | The version of the certificate signing request.  The only allowed value according to [RFC 2986](https://tools.ietf.org/html/rfc2986#section-4.1) is 1.  This option no longer accepts unsupported values since community.crypto 2.0.0.  Choices:   - `1` ← (default) |

## [Attributes](openssl_csr_pipe_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support: full | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](openssl_csr_pipe_module.md#id5)

> **Note:**
>
> - If the certificate signing request already exists it will be checked whether subjectAltName, keyUsage, extendedKeyUsage and basicConstraints only contain the requested values, whether OCSP Must Staple is as requested, and if the request was signed by the given private key.

## [See Also](openssl_csr_pipe_module.md#id6)

> **See also:**
>
> [community.crypto.openssl_csr](openssl_csr_module.md#ansible-collections-community-crypto-openssl-csr-module)
> :   Generate OpenSSL Certificate Signing Request (CSR).
>
> [community.crypto.x509_certificate](x509_certificate_module.md#ansible-collections-community-crypto-x509-certificate-module)
> :   Generate and/or check OpenSSL certificates.
>
> [community.crypto.x509_certificate_pipe](x509_certificate_pipe_module.md#ansible-collections-community-crypto-x509-certificate-pipe-module)
> :   Generate and/or check OpenSSL certificates.
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
>
> [community.crypto.openssl_csr_info](openssl_csr_info_module.md#ansible-collections-community-crypto-openssl-csr-info-module)
> :   Provide information of OpenSSL Certificate Signing Requests (CSR).

## [Examples](openssl_csr_pipe_module.md#id7)

```yaml+jinja
- name: Generate an OpenSSL Certificate Signing Request
  community.crypto.openssl_csr_pipe:
    privatekey_path: /etc/ssl/private/ansible.com.pem
    common_name: www.ansible.com
  register: result
- debug:
    var: result.csr

- name: Generate an OpenSSL Certificate Signing Request with an inline CSR
  community.crypto.openssl_csr:
    content: "{{ lookup('file', '/etc/ssl/csr/www.ansible.com.csr') }}"
    privatekey_content: "{{ private_key_content }}"
    common_name: www.ansible.com
  register: result
- name: Store CSR
  ansible.builtin.copy:
    dest: /etc/ssl/csr/www.ansible.com.csr
    content: "{{ result.csr }}"
  when: result is changed
```

## [Return Values](openssl_csr_pipe_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **basicConstraints**  list / elements=string | Indicates if the certificate belongs to a CA  Returned: changed or success  Sample: `["CA:TRUE", "pathLenConstraint:0"]` |
| **csr**  string | The (current or generated) CSR’s content.  Returned: changed or success |
| **extendedKeyUsage**  list / elements=string | Additional restriction on the public key purposes  Returned: changed or success  Sample: `["clientAuth"]` |
| **keyUsage**  list / elements=string | Purpose for which the public key may be used  Returned: changed or success  Sample: `["digitalSignature", "keyAgreement"]` |
| **name_constraints_excluded**  list / elements=string | List of excluded subtrees the CA cannot sign certificates for.  Returned: changed or success  Sample: `["email:.com"]` |
| **name_constraints_permitted**  list / elements=string | List of permitted subtrees to sign certificates for.  Returned: changed or success  Sample: `["email:.somedomain.com"]` |
| **ocsp_must_staple**  boolean | Indicates whether the certificate has the OCSP Must Staple feature enabled  Returned: changed or success  Sample: `false` |
| **privatekey**  string | Path to the TLS/SSL private key the CSR was generated for  Will be `none` if the private key has been provided in *privatekey_content*.  Returned: changed or success  Sample: `"/etc/ssl/private/ansible.com.pem"` |
| **subject**  list / elements=list | A list of the subject tuples attached to the CSR  Returned: changed or success  Sample: `[["CN", "www.ansible.com"], ["O", "Ansible"]]` |
| **subjectAltName**  list / elements=string | The alternative names this CSR is valid for  Returned: changed or success  Sample: `["DNS:www.ansible.com", "DNS:m.ansible.com"]` |

### Authors

- Yanis Guenane (@Spredzy)
- Felix Fontein (@felixfontein)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.crypto)
[Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-crypto)
