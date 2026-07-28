---
collection: ansible
version: "8"
title: "community.crypto.x509_certificate module – Generate and/or check OpenSSL certificates"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/crypto/x509_certificate_module.html
fetched_at: 2026-07-28T01:42:40+00:00
---
# community.crypto.x509_certificate module – Generate and/or check OpenSSL certificates

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
> see [Requirements](x509_certificate_module.md#ansible-collections-community-crypto-x509-certificate-module-requirements) for details.
>
> To use it in a playbook, specify: `community.crypto.x509_certificate`.

- [Synopsis](x509_certificate_module.md#synopsis)
- [Requirements](x509_certificate_module.md#requirements)
- [Parameters](x509_certificate_module.md#parameters)
- [Attributes](x509_certificate_module.md#attributes)
- [Notes](x509_certificate_module.md#notes)
- [See Also](x509_certificate_module.md#see-also)
- [Examples](x509_certificate_module.md#examples)
- [Return Values](x509_certificate_module.md#return-values)

## [Synopsis](x509_certificate_module.md#id1)

- It implements a notion of provider (one of `selfsigned`, `ownca`, `acme`, and `entrust`) for your certificate.
- It uses the cryptography python library to interact with OpenSSL.
- Note that this module was called `openssl_certificate` when included directly in Ansible up to version 2.9. When moved to the collection `community.crypto`, it was renamed to [community.crypto.x509_certificate](x509_certificate_module.md#ansible-collections-community-crypto-x509-certificate-module). From Ansible 2.10 on, it can still be used by the old short name (or by `ansible.builtin.openssl_certificate`), which redirects to [community.crypto.x509_certificate](x509_certificate_module.md#ansible-collections-community-crypto-x509-certificate-module). When using FQCNs or when using the [collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html#using-collections-in-a-playbook) keyword, the new name [community.crypto.x509_certificate](x509_certificate_module.md#ansible-collections-community-crypto-x509-certificate-module) should be used to avoid a deprecation warning.
- Please note that the module regenerates existing certificate if it does not match the module’s options, or if it seems to be corrupt. If you are concerned that this could overwrite your existing certificate, consider using the `backup` option.
- The `ownca` provider is intended for generating an OpenSSL certificate signed with your own CA (Certificate Authority) certificate (self-signed certificate).
- This module allows one to (re)generate OpenSSL certificates.

## [Requirements](x509_certificate_module.md#id2)

The below requirements are needed on the host that executes this module.

- acme-tiny >= 4.0.0 (if using the `acme` provider)
- cryptography >= 1.6 (if using `selfsigned` or `ownca` provider)

## [Parameters](x509_certificate_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **acme_accountkey_path**  path | The path to the accountkey for the `acme` provider.  This is only used by the `acme` provider. |
| **acme_chain**  boolean | Include the intermediate certificate to the generated certificate  This is only used by the `acme` provider.  Note that this is only available for older versions of `acme-tiny`. New versions include the chain automatically, and setting `acme_chain` to `true` results in an error.  **Choices:**   - `false` ← (default) - `true` |
| **acme_challenge_path**  path | The path to the ACME challenge directory that is served on <http://%3CHOST%3E:80/.well-known/acme-challenge/>  This is only used by the `acme` provider. |
| **acme_directory**  string  *added in community.crypto 1.0.0* | The ACME directory to use. You can use any directory that supports the ACME protocol, such as Buypass or Let’s Encrypt.  Let’s Encrypt recommends using their staging server while developing jobs. <https://letsencrypt.org/docs/staging-environment/>.  **Default:** `"https://acme-v02.api.letsencrypt.org/directory"` |
| **attributes**  aliases: attr  string | The attributes the resulting filesystem object should have.  To get supported flags look at the man page for *chattr* on the target system.  This string should contain the attributes in the same order as the one displayed by *lsattr*.  The `=` operator is assumed as default, otherwise `+` or `-` operators need to be included in the string. |
| **backup**  boolean | Create a backup file including a timestamp so you can get the original certificate back if you overwrote it with a new one by accident.  **Choices:**   - `false` ← (default) - `true` |
| **csr_content**  string  *added in community.crypto 1.0.0* | Content of the Certificate Signing Request (CSR) used to generate this certificate.  This is mutually exclusive with `csr_path`. |
| **csr_path**  path | Path to the Certificate Signing Request (CSR) used to generate this certificate.  This is mutually exclusive with `csr_content`. |
| **entrust_api_client_cert_key_path**  path | The path to the private key of the client certificate used to authenticate to the Entrust Certificate Services (ECS) API.  This is only used by the `entrust` provider.  This is required if the provider is `entrust`. |
| **entrust_api_client_cert_path**  path | The path to the client certificate used to authenticate to the Entrust Certificate Services (ECS) API.  This is only used by the `entrust` provider.  This is required if the provider is `entrust`. |
| **entrust_api_key**  string | The key (password) for authentication to the Entrust Certificate Services (ECS) API.  This is only used by the `entrust` provider.  This is required if the provider is `entrust`. |
| **entrust_api_specification_path**  path | The path to the specification file defining the Entrust Certificate Services (ECS) API configuration.  You can use this to keep a local copy of the specification to avoid downloading it every time the module is used.  This is only used by the `entrust` provider.  **Default:** `"https://cloud.entrust.net/EntrustCloud/documentation/cms-api-2.1.0.yaml"` |
| **entrust_api_user**  string | The username for authentication to the Entrust Certificate Services (ECS) API.  This is only used by the `entrust` provider.  This is required if the provider is `entrust`. |
| **entrust_cert_type**  string | Specify the type of certificate requested.  This is only used by the `entrust` provider.  **Choices:**   - `"STANDARD_SSL"` ← (default) - `"ADVANTAGE_SSL"` - `"UC_SSL"` - `"EV_SSL"` - `"WILDCARD_SSL"` - `"PRIVATE_SSL"` - `"PD_SSL"` - `"CDS_ENT_LITE"` - `"CDS_ENT_PRO"` - `"SMIME_ENT"` |
| **entrust_not_after**  string | The point in time at which the certificate stops being valid.  Time can be specified either as relative time or as an absolute timestamp.  A valid absolute time format is `ASN.1 TIME` such as `2019-06-18`.  A valid relative time format is `[+-]timespec` where timespec can be an integer + `[w | d | h | m | s]`, such as `+365d` or `+32w1d2h`).  Time will always be interpreted as UTC.  Note that only the date (day, month, year) is supported for specifying the expiry date of the issued certificate.  The full date-time is adjusted to EST (GMT -5:00) before issuance, which may result in a certificate with an expiration date one day earlier than expected if a relative time is used.  The minimum certificate lifetime is 90 days, and maximum is three years.  If this value is not specified, the certificate will stop being valid 365 days the date of issue.  This is only used by the `entrust` provider.  Please note that this value is **not** covered by the `ignore_timestamps` option.  **Default:** `"+365d"` |
| **entrust_requester_email**  string | The email of the requester of the certificate (for tracking purposes).  This is only used by the `entrust` provider.  This is required if the provider is `entrust`. |
| **entrust_requester_name**  string | The name of the requester of the certificate (for tracking purposes).  This is only used by the `entrust` provider.  This is required if the provider is `entrust`. |
| **entrust_requester_phone**  string | The phone number of the requester of the certificate (for tracking purposes).  This is only used by the `entrust` provider.  This is required if the provider is `entrust`. |
| **force**  boolean | Generate the certificate, even if it already exists.  **Choices:**   - `false` ← (default) - `true` |
| **group**  string | Name of the group that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current group of the current user unless you are root, in which case it can preserve the previous ownership. |
| **ignore_timestamps**  boolean  *added in community.crypto 2.0.0* | Whether the “not before” and “not after” timestamps should be ignored for idempotency checks.  It is better to keep the default value `true` when using relative timestamps (like `+0s` for now).  **Choices:**   - `false` - `true` ← (default) |
| **mode**  any | The permissions the resulting filesystem object should have.  For those used to */usr/bin/chmod* remember that modes are actually octal numbers. You must give Ansible enough information to parse them correctly. For consistent results, quote octal numbers (for example, `'644'` or `'1777'`) so Ansible receives a string and can do its own conversion from string into number. Adding a leading zero (for example, `0755`) works sometimes, but can fail in loops and some other circumstances.  Giving Ansible a number without following either of these rules will end up with a decimal number which will have unexpected results.  As of Ansible 1.8, the mode may be specified as a symbolic mode (for example, `u+rwx` or `u=rw,g=r,o=r`).  If `mode` is not specified and the destination filesystem object **does not** exist, the default `umask` on the system will be used when setting the mode for the newly created filesystem object.  If `mode` is not specified and the destination filesystem object **does** exist, the mode of the existing filesystem object will be used.  Specifying `mode` is the best way to ensure filesystem objects are created with the correct permissions. See CVE-2020-1736 for further details. |
| **ownca_content**  string  *added in community.crypto 1.0.0* | Content of the CA (Certificate Authority) certificate.  This is only used by the `ownca` provider.  This is mutually exclusive with `ownca_path`. |
| **ownca_create_authority_key_identifier**  boolean | Create a Authority Key Identifier from the CA’s certificate. If the CSR provided a authority key identifier, it is ignored.  The Authority Key Identifier is generated from the CA certificate’s Subject Key Identifier, if available. If it is not available, the CA certificate’s public key will be used.  This is only used by the `ownca` provider.  Note that this is only supported if the `cryptography` backend is used!  **Choices:**   - `false` - `true` ← (default) |
| **ownca_create_subject_key_identifier**  string | Whether to create the Subject Key Identifier (SKI) from the public key.  A value of `create_if_not_provided` (default) only creates a SKI when the CSR does not provide one.  A value of `always_create` always creates a SKI. If the CSR provides one, that one is ignored.  A value of `never_create` never creates a SKI. If the CSR provides one, that one is used.  This is only used by the `ownca` provider.  Note that this is only supported if the `cryptography` backend is used!  **Choices:**   - `"create_if_not_provided"` ← (default) - `"always_create"` - `"never_create"` |
| **ownca_digest**  string | The digest algorithm to be used for the `ownca` certificate.  This is only used by the `ownca` provider.  **Default:** `"sha256"` |
| **ownca_not_after**  string | The point in time at which the certificate stops being valid.  Time can be specified either as relative time or as absolute timestamp.  Time will always be interpreted as UTC.  Valid format is `[+-]timespec | ASN.1 TIME` where timespec can be an integer + `[w | d | h | m | s]` (for example `+32w1d2h`).  If this value is not specified, the certificate will stop being valid 10 years from now.  Note that this value is **not used to determine whether an existing certificate should be regenerated**. This can be changed by setting the `ignore_timestamps` option to `false`. Please note that you should avoid relative timestamps when setting `ignore_timestamps=false`.  This is only used by the `ownca` provider.  On macOS 10.15 and onwards, TLS server certificates must have a validity period of 825 days or fewer. Please see <https://support.apple.com/en-us/HT210176> for more details.  **Default:** `"+3650d"` |
| **ownca_not_before**  string | The point in time the certificate is valid from.  Time can be specified either as relative time or as absolute timestamp.  Time will always be interpreted as UTC.  Valid format is `[+-]timespec | ASN.1 TIME` where timespec can be an integer + `[w | d | h | m | s]` (for example `+32w1d2h`).  If this value is not specified, the certificate will start being valid from now.  Note that this value is **not used to determine whether an existing certificate should be regenerated**. This can be changed by setting the `ignore_timestamps` option to `false`. Please note that you should avoid relative timestamps when setting `ignore_timestamps=false`.  This is only used by the `ownca` provider.  **Default:** `"+0s"` |
| **ownca_path**  path | Remote absolute path of the CA (Certificate Authority) certificate.  This is only used by the `ownca` provider.  This is mutually exclusive with `ownca_content`. |
| **ownca_privatekey_content**  string  *added in community.crypto 1.0.0* | Content of the CA (Certificate Authority) private key to use when signing the certificate.  This is only used by the `ownca` provider.  This is mutually exclusive with `ownca_privatekey_path`. |
| **ownca_privatekey_passphrase**  string | The passphrase for the `ownca_privatekey_path` resp. `ownca_privatekey_content`.  This is only used by the `ownca` provider. |
| **ownca_privatekey_path**  path | Path to the CA (Certificate Authority) private key to use when signing the certificate.  This is only used by the `ownca` provider.  This is mutually exclusive with `ownca_privatekey_content`. |
| **ownca_version**  integer | The version of the `ownca` certificate.  Nowadays it should almost always be `3`.  This is only used by the `ownca` provider.  **Default:** `3` |
| **owner**  string | Name of the user that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current user unless you are root, in which case it can preserve the previous ownership.  Specifying a numeric username will be assumed to be a user ID and not a username. Avoid numeric usernames to avoid this confusion. |
| **path**  path / required | Remote absolute path where the generated certificate file should be created or is already located. |
| **privatekey_content**  string  *added in community.crypto 1.0.0* | Content of the private key to use when signing the certificate.  This is mutually exclusive with `privatekey_path`. |
| **privatekey_passphrase**  string | The passphrase for the `privatekey_path` resp. `privatekey_content`.  This is required if the private key is password protected. |
| **privatekey_path**  path | Path to the private key to use when signing the certificate.  This is mutually exclusive with `privatekey_content`. |
| **provider**  string | Name of the provider to use to generate/retrieve the OpenSSL certificate. Please see the examples on how to emulate it with [community.crypto.x509_certificate_info](x509_certificate_info_module.md#ansible-collections-community-crypto-x509-certificate-info-module), [community.crypto.openssl_csr_info](openssl_csr_info_module.md#ansible-collections-community-crypto-openssl-csr-info-module), [community.crypto.openssl_privatekey_info](openssl_privatekey_info_module.md#ansible-collections-community-crypto-openssl-privatekey-info-module) and [ansible.builtin.assert](../../ansible/builtin/assert_module.md#ansible-collections-ansible-builtin-assert-module).  The `entrust` provider was added for Ansible 2.9 and requires credentials for the [Entrust Certificate Services](https://www.entrustdatacard.com/products/categories/ssl-certificates) (ECS) API.  Required if `state` is `present`.  **Choices:**   - `"acme"` - `"entrust"` - `"ownca"` - `"selfsigned"` |
| **return_content**  boolean  *added in community.crypto 1.0.0* | If set to `true`, will return the (current or generated) certificate’s content as `certificate`.  **Choices:**   - `false` ← (default) - `true` |
| **select_crypto_backend**  string | Determines which crypto backend to use.  The default choice is `auto`, which tries to use `cryptography` if available.  If set to `cryptography`, will try to use the [cryptography](https://cryptography.io/) library.  **Choices:**   - `"auto"` ← (default) - `"cryptography"` |
| **selevel**  string | The level part of the SELinux filesystem object context.  This is the MLS/MCS attribute, sometimes known as the `range`.  When set to `_default`, it will use the `level` portion of the policy if available. |
| **selfsigned_create_subject_key_identifier**  string | Whether to create the Subject Key Identifier (SKI) from the public key.  A value of `create_if_not_provided` (default) only creates a SKI when the CSR does not provide one.  A value of `always_create` always creates a SKI. If the CSR provides one, that one is ignored.  A value of `never_create` never creates a SKI. If the CSR provides one, that one is used.  This is only used by the `selfsigned` provider.  Note that this is only supported if the `cryptography` backend is used!  **Choices:**   - `"create_if_not_provided"` ← (default) - `"always_create"` - `"never_create"` |
| **selfsigned_digest**  string | Digest algorithm to be used when self-signing the certificate.  This is only used by the `selfsigned` provider.  **Default:** `"sha256"` |
| **selfsigned_not_after**  aliases: selfsigned_notAfter  string | The point in time at which the certificate stops being valid.  Time can be specified either as relative time or as absolute timestamp.  Time will always be interpreted as UTC.  Valid format is `[+-]timespec | ASN.1 TIME` where timespec can be an integer + `[w | d | h | m | s]` (for example `+32w1d2h`).  If this value is not specified, the certificate will stop being valid 10 years from now.  Note that this value is **not used to determine whether an existing certificate should be regenerated**. This can be changed by setting the `ignore_timestamps` option to `false`. Please note that you should avoid relative timestamps when setting `ignore_timestamps=false`.  This is only used by the `selfsigned` provider.  On macOS 10.15 and onwards, TLS server certificates must have a validity period of 825 days or fewer. Please see <https://support.apple.com/en-us/HT210176> for more details.  **Default:** `"+3650d"` |
| **selfsigned_not_before**  aliases: selfsigned_notBefore  string | The point in time the certificate is valid from.  Time can be specified either as relative time or as absolute timestamp.  Time will always be interpreted as UTC.  Valid format is `[+-]timespec | ASN.1 TIME` where timespec can be an integer + `[w | d | h | m | s]` (for example `+32w1d2h`).  If this value is not specified, the certificate will start being valid from now.  Note that this value is **not used to determine whether an existing certificate should be regenerated**. This can be changed by setting the `ignore_timestamps` option to `false`. Please note that you should avoid relative timestamps when setting `ignore_timestamps=false`.  This is only used by the `selfsigned` provider.  **Default:** `"+0s"` |
| **selfsigned_version**  integer | Version of the `selfsigned` certificate.  Nowadays it should almost always be `3`.  This is only used by the `selfsigned` provider.  **Default:** `3` |
| **serole**  string | The role part of the SELinux filesystem object context.  When set to `_default`, it will use the `role` portion of the policy if available. |
| **setype**  string | The type part of the SELinux filesystem object context.  When set to `_default`, it will use the `type` portion of the policy if available. |
| **seuser**  string | The user part of the SELinux filesystem object context.  By default it uses the `system` policy, where applicable.  When set to `_default`, it will use the `user` portion of the policy if available. |
| **state**  string | Whether the certificate should exist or not, taking action if the state is different from what is stated.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **unsafe_writes**  boolean | Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target filesystem object.  By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target filesystem objects, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted filesystem objects, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.  This option allows Ansible to fall back to unsafe methods of updating filesystem objects when atomic operations fail (however, it doesn’t force Ansible to perform unsafe writes).  IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](x509_certificate_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |
| **safe_file_operations** | **Support:** **full** | Uses Ansible’s strict file operation functions to ensure proper permissions and avoid data corruption. |

## [Notes](x509_certificate_module.md#id5)

> **Note:**
>
> - All ASN.1 TIME values should be specified following the YYYYMMDDHHMMSSZ pattern.
> - Date specified should be UTC. Minutes and seconds are mandatory.
> - For security reason, when you use `ownca` provider, you should NOT run [community.crypto.x509_certificate](x509_certificate_module.md#ansible-collections-community-crypto-x509-certificate-module) on a target machine, but on a dedicated CA machine. It is recommended not to store the CA private key on the target machine. Once signed, the certificate can be moved to the target machine.
> - For the `selfsigned` provider, `csr_path` and `csr_content` are optional. If not provided, a certificate without any information (Subject, Subject Alternative Names, Key Usage, etc.) is created.

## [See Also](x509_certificate_module.md#id6)

> **See also:**
>
> [community.crypto.x509_certificate_pipe](x509_certificate_pipe_module.md#ansible-collections-community-crypto-x509-certificate-pipe-module)
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

## [Examples](x509_certificate_module.md#id7)

```yaml+jinja
- name: Generate a Self Signed OpenSSL certificate
  community.crypto.x509_certificate:
    path: /etc/ssl/crt/ansible.com.crt
    privatekey_path: /etc/ssl/private/ansible.com.pem
    csr_path: /etc/ssl/csr/ansible.com.csr
    provider: selfsigned

- name: Generate an OpenSSL certificate signed with your own CA certificate
  community.crypto.x509_certificate:
    path: /etc/ssl/crt/ansible.com.crt
    csr_path: /etc/ssl/csr/ansible.com.csr
    ownca_path: /etc/ssl/crt/ansible_CA.crt
    ownca_privatekey_path: /etc/ssl/private/ansible_CA.pem
    provider: ownca

- name: Generate a Let's Encrypt Certificate
  community.crypto.x509_certificate:
    path: /etc/ssl/crt/ansible.com.crt
    csr_path: /etc/ssl/csr/ansible.com.csr
    provider: acme
    acme_accountkey_path: /etc/ssl/private/ansible.com.pem
    acme_challenge_path: /etc/ssl/challenges/ansible.com/

- name: Force (re-)generate a new Let's Encrypt Certificate
  community.crypto.x509_certificate:
    path: /etc/ssl/crt/ansible.com.crt
    csr_path: /etc/ssl/csr/ansible.com.csr
    provider: acme
    acme_accountkey_path: /etc/ssl/private/ansible.com.pem
    acme_challenge_path: /etc/ssl/challenges/ansible.com/
    force: true

- name: Generate an Entrust certificate via the Entrust Certificate Services (ECS) API
  community.crypto.x509_certificate:
    path: /etc/ssl/crt/ansible.com.crt
    csr_path: /etc/ssl/csr/ansible.com.csr
    provider: entrust
    entrust_requester_name: Jo Doe
    entrust_requester_email: jdoe@ansible.com
    entrust_requester_phone: 555-555-5555
    entrust_cert_type: STANDARD_SSL
    entrust_api_user: apiusername
    entrust_api_key: a^lv*32!cd9LnT
    entrust_api_client_cert_path: /etc/ssl/entrust/ecs-client.crt
    entrust_api_client_cert_key_path: /etc/ssl/entrust/ecs-key.crt
    entrust_api_specification_path: /etc/ssl/entrust/api-docs/cms-api-2.1.0.yaml

# The following example shows how to emulate the behavior of the removed
# "assertonly" provider with the x509_certificate_info, openssl_csr_info,
# openssl_privatekey_info and assert modules:

- name: Get certificate information
  community.crypto.x509_certificate_info:
    path: /etc/ssl/crt/ansible.com.crt
    # for valid_at, invalid_at and valid_in
    valid_at:
      one_day_ten_hours: "+1d10h"
      fixed_timestamp: 20200331202428Z
      ten_seconds: "+10"
  register: result

- name: Get CSR information
  community.crypto.openssl_csr_info:
    # Verifies that the CSR signature is valid; module will fail if not
    path: /etc/ssl/csr/ansible.com.csr
  register: result_csr

- name: Get private key information
  community.crypto.openssl_privatekey_info:
    path: /etc/ssl/csr/ansible.com.key
  register: result_privatekey

- name: Check conditions on certificate, CSR, and private key
  ansible.builtin.assert:
    that:
      # When private key was specified for assertonly, this was checked:
      - result.public_key == result_privatekey.public_key
      # When CSR was specified for assertonly, this was checked:
      - result.public_key == result_csr.public_key
      - result.subject_ordered == result_csr.subject_ordered
      - result.extensions_by_oid == result_csr.extensions_by_oid
      # signature_algorithms check
      - "result.signature_algorithm == 'sha256WithRSAEncryption' or result.signature_algorithm == 'sha512WithRSAEncryption'"
      # subject and subject_strict
      - "result.subject.commonName == 'ansible.com'"
      - "result.subject | length == 1"  # the number must be the number of entries you check for
      # issuer and issuer_strict
      - "result.issuer.commonName == 'ansible.com'"
      - "result.issuer | length == 1"  # the number must be the number of entries you check for
      # has_expired
      - not result.expired
      # version
      - result.version == 3
      # key_usage and key_usage_strict
      - "'Data Encipherment' in result.key_usage"
      - "result.key_usage | length == 1"  # the number must be the number of entries you check for
      # extended_key_usage and extended_key_usage_strict
      - "'DVCS' in result.extended_key_usage"
      - "result.extended_key_usage | length == 1"  # the number must be the number of entries you check for
      # subject_alt_name and subject_alt_name_strict
      - "'dns:ansible.com' in result.subject_alt_name"
      - "result.subject_alt_name | length == 1"  # the number must be the number of entries you check for
      # not_before and not_after
      - "result.not_before == '20190331202428Z'"
      - "result.not_after == '20190413202428Z'"
      # valid_at, invalid_at and valid_in
      - "result.valid_at.one_day_ten_hours"  # for valid_at
      - "not result.valid_at.fixed_timestamp"  # for invalid_at
      - "result.valid_at.ten_seconds"  # for valid_in
```

## [Return Values](x509_certificate_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_file**  string | Name of backup file created.  **Returned:** changed and if `backup` is `true`  **Sample:** `"/path/to/www.ansible.com.crt.2019-03-09@11:22~"` |
| **certificate**  string  *added in community.crypto 1.0.0* | The (current or generated) certificate’s content.  **Returned:** if `state` is `present` and `return_content` is `true` |
| **filename**  string | Path to the generated certificate.  **Returned:** changed or success  **Sample:** `"/etc/ssl/crt/www.ansible.com.crt"` |

### Authors

- Yanis Guenane (@Spredzy)
- Markus Teufelberger (@MarkusTeufelberger)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.crypto)
- [Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-crypto)
