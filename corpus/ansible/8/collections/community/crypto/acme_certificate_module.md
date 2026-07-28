---
collection: ansible
version: "8"
title: "community.crypto.acme_certificate module – Create SSL/TLS certificates with the ACME protocol"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/crypto/acme_certificate_module.html
fetched_at: 2026-07-28T01:42:21+00:00
---
# community.crypto.acme_certificate module – Create SSL/TLS certificates with the ACME protocol

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
> see [Requirements](acme_certificate_module.md#ansible-collections-community-crypto-acme-certificate-module-requirements) for details.
>
> To use it in a playbook, specify: `community.crypto.acme_certificate`.

- [Synopsis](acme_certificate_module.md#synopsis)
- [Requirements](acme_certificate_module.md#requirements)
- [Parameters](acme_certificate_module.md#parameters)
- [Attributes](acme_certificate_module.md#attributes)
- [Notes](acme_certificate_module.md#notes)
- [See Also](acme_certificate_module.md#see-also)
- [Examples](acme_certificate_module.md#examples)
- [Return Values](acme_certificate_module.md#return-values)

## [Synopsis](acme_certificate_module.md#id1)

- Create and renew SSL/TLS certificates with a CA supporting the [ACME protocol](https://tools.ietf.org/html/rfc8555), such as [Let’s Encrypt](https://letsencrypt.org/) or [Buypass](https://www.buypass.com/). The current implementation supports the `http-01`, `dns-01` and `tls-alpn-01` challenges.
- To use this module, it has to be executed twice. Either as two different tasks in the same run or during two runs. Note that the output of the first run needs to be recorded and passed to the second run as the module argument `data`.
- Between these two tasks you have to fulfill the required steps for the chosen challenge by whatever means necessary. For `http-01` that means creating the necessary challenge file on the destination webserver. For `dns-01` the necessary dns record has to be created. For `tls-alpn-01` the necessary certificate has to be created and served. It is *not* the responsibility of this module to perform these steps.
- For details on how to fulfill these challenges, you might have to read through [the main ACME specification](https://tools.ietf.org/html/rfc8555#section-8) and the [TLS-ALPN-01 specification](https://www.rfc-editor.org/rfc/rfc8737.html#section-3). Also, consider the examples provided for this module.
- The module includes experimental support for IP identifiers according to the [RFC 8738](https://www.rfc-editor.org/rfc/rfc8738.html).

## [Requirements](acme_certificate_module.md#id2)

The below requirements are needed on the host that executes this module.

- either openssl or [cryptography](https://cryptography.io/) >= 1.5
- ipaddress

## [Parameters](acme_certificate_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account_email**  string | The email address associated with this account.  It will be used for certificate expiration warnings.  Note that when `modify_account` is not set to `false` and you also used the [community.crypto.acme_account](acme_account_module.md#ansible-collections-community-crypto-acme-account-module) module to specify more than one contact for your account, this module will update your account and restrict it to the (at most one) contact email address specified here. |
| **account_key_content**  string | Content of the ACME account RSA or Elliptic Curve key.  Mutually exclusive with `account_key_src`.  Required if `account_key_src` is not used.  **Warning:** the content will be written into a temporary file, which will be deleted by Ansible when the module completes. Since this is an important private key — it can be used to change the account key, or to revoke your certificates without knowing their private keys —, this might not be acceptable.  In case `cryptography` is used, the content is not written into a temporary file. It can still happen that it is written to disk by Ansible in the process of moving the module with its argument to the node where it is executed. |
| **account_key_passphrase**  string  *added in community.crypto 1.6.0* | Phassphrase to use to decode the account key.  **Note:** this is not supported by the `openssl` backend, only by the `cryptography` backend. |
| **account_key_src**  aliases: account_key  path | Path to a file containing the ACME account RSA or Elliptic Curve key.  Private keys can be created with the [community.crypto.openssl_privatekey](openssl_privatekey_module.md#ansible-collections-community-crypto-openssl-privatekey-module) or [community.crypto.openssl_privatekey_pipe](openssl_privatekey_pipe_module.md#ansible-collections-community-crypto-openssl-privatekey-pipe-module) modules. If the requisite (cryptography) is not available, keys can also be created directly with the `openssl` command line tool: RSA keys can be created with `openssl genrsa ...`. Elliptic curve keys can be created with `openssl ecparam -genkey ...`. Any other tool creating private keys in PEM format can be used as well.  Mutually exclusive with `account_key_content`.  Required if `account_key_content` is not used. |
| **account_uri**  string | If specified, assumes that the account URI is as given. If the account key does not match this account, or an account with this URI does not exist, the module fails. |
| **acme_directory**  string / required | The ACME directory to use. This is the entry point URL to access the ACME CA server API.  For safety reasons the default is set to the Let’s Encrypt staging server (for the ACME v1 protocol). This will create technically correct, but untrusted certificates.  For Let’s Encrypt, all staging endpoints can be found here: <https://letsencrypt.org/docs/staging-environment/>. For Buypass, all endpoints can be found here: <https://community.buypass.com/t/63d4ay/buypass-go-ssl-endpoints>  For **Let’s Encrypt**, the production directory URL for ACME v2 is <https://acme-v02.api.letsencrypt.org/directory>.  For **Buypass**, the production directory URL for ACME v2 and v1 is <https://api.buypass.com/acme/directory>.  For **ZeroSSL**, the production directory URL for ACME v2 is <https://acme.zerossl.com/v2/DV90>.  For **Sectigo**, the production directory URL for ACME v2 is <https://acme-qa.secure.trust-provider.com/v2/DV>.  The notes for this module contain a list of ACME services this module has been tested against. |
| **acme_version**  integer / required | The ACME version of the endpoint.  Must be `1` for the classic Let’s Encrypt and Buypass ACME endpoints, or `2` for standardized ACME v2 endpoints.  The value `1` is deprecated since community.crypto 2.0.0 and will be removed from community.crypto 3.0.0.  **Choices:**   - `1` - `2` |
| **agreement**  string | URI to a terms of service document you agree to when using the ACME v1 service at `acme_directory`.  Default is latest gathered from `acme_directory` URL.  This option will only be used when `acme_version` is 1. |
| **chain_dest**  aliases: chain  path | If specified, the intermediate certificate will be written to this file. |
| **challenge**  string | The challenge to be performed.  If set to `no challenge`, no challenge will be used. This is necessary for some private CAs which use External Account Binding and other means of validating certificate assurance. For example, an account could be allowed to issue certificates for `foo.example.com` without any further validation for a certain period of time.  **Choices:**   - `"http-01"` ← (default) - `"dns-01"` - `"tls-alpn-01"` - `"no challenge"` |
| **csr**  aliases: src  path | File containing the CSR for the new certificate.  Can be created with [community.crypto.openssl_csr](openssl_csr_module.md#ansible-collections-community-crypto-openssl-csr-module) or `openssl req ...`.  The CSR may contain multiple Subject Alternate Names, but each one will lead to an individual challenge that must be fulfilled for the CSR to be signed.  *Note*: the private key used to create the CSR *must not* be the account key. This is a bad idea from a security point of view, and the CA should not accept the CSR. The ACME server should return an error in this case.  Precisely one of `csr` or `csr_content` must be specified. |
| **csr_content**  string  *added in community.crypto 1.2.0* | Content of the CSR for the new certificate.  Can be created with [community.crypto.openssl_csr_pipe](openssl_csr_pipe_module.md#ansible-collections-community-crypto-openssl-csr-pipe-module) or `openssl req ...`.  The CSR may contain multiple Subject Alternate Names, but each one will lead to an individual challenge that must be fulfilled for the CSR to be signed.  *Note*: the private key used to create the CSR *must not* be the account key. This is a bad idea from a security point of view, and the CA should not accept the CSR. The ACME server should return an error in this case.  Precisely one of `csr` or `csr_content` must be specified. |
| **data**  dictionary | The data to validate ongoing challenges. This must be specified for the second run of the module only.  The value that must be used here will be provided by a previous use of this module. See the examples for more details.  Note that for ACME v2, only the `order_uri` entry of `data` will be used. For ACME v1, `data` must be non-empty to indicate the second stage is active; all needed data will be taken from the CSR.  *Note*: the `data` option was marked as `no_log` up to Ansible 2.5. From Ansible 2.6 on, it is no longer marked this way as it causes error messages to be come unusable, and `data` does not contain any information which can be used without having access to the account key or which are not public anyway. |
| **deactivate_authzs**  boolean | Deactivate authentication objects (authz) after issuing a certificate, or when issuing the certificate failed.  Authentication objects are bound to an account key and remain valid for a certain amount of time, and can be used to issue certificates without having to re-authenticate the domain. This can be a security concern.  **Choices:**   - `false` ← (default) - `true` |
| **dest**  aliases: cert  path | The destination file for the certificate.  Required if `fullchain_dest` is not specified. |
| **force**  boolean | Enforces the execution of the challenge and validation, even if an existing certificate is still valid for more than `remaining_days`.  This is especially helpful when having an updated CSR, for example with additional domains for which a new certificate is desired.  **Choices:**   - `false` ← (default) - `true` |
| **fullchain_dest**  aliases: fullchain  path | The destination file for the full chain (that is, a certificate followed by chain of intermediate certificates).  Required if `dest` is not specified. |
| **modify_account**  boolean | Boolean indicating whether the module should create the account if necessary, and update its contact data.  Set to `false` if you want to use the [community.crypto.acme_account](acme_account_module.md#ansible-collections-community-crypto-acme-account-module) module to manage your account instead, and to avoid accidental creation of a new account using an old key if you changed the account key with [community.crypto.acme_account](acme_account_module.md#ansible-collections-community-crypto-acme-account-module).  If set to `false`, `terms_agreed` and `account_email` are ignored.  **Choices:**   - `false` - `true` ← (default) |
| **remaining_days**  integer | The number of days the certificate must have left being valid. If `cert_days` < `remaining_days`, then it will be renewed. If the certificate is not renewed, module return values will not include `challenge_data`.  To make sure that the certificate is renewed in any case, you can use the `force` option.  **Default:** `10` |
| **request_timeout**  integer  *added in community.crypto 2.3.0* | The time Ansible should wait for a response from the ACME API.  This timeout is applied to all HTTP(S) requests (HEAD, GET, POST).  **Default:** `10` |
| **retrieve_all_alternates**  boolean | When set to `true`, will retrieve all alternate trust chains offered by the ACME CA. These will not be written to disk, but will be returned together with the main chain as `all_chains`. See the documentation for the `all_chains` return value for details.  **Choices:**   - `false` ← (default) - `true` |
| **select_chain**  list / elements=dictionary  *added in community.crypto 1.0.0* | Allows to specify criteria by which an (alternate) trust chain can be selected.  The list of criteria will be processed one by one until a chain is found matching a criterium. If such a chain is found, it will be used by the module instead of the default chain.  If a criterium matches multiple chains, the first one matching will be returned. The order is determined by the ordering of the `Link` headers returned by the ACME server and might not be deterministic.  Every criterium can consist of multiple different conditions, like `select_chain[].issuer` and `select_chain[].subject`. For the criterium to match a chain, all conditions must apply to the same certificate in the chain.  This option can only be used with the `cryptography` backend. |
| **authority_key_identifier**  string | Checks for the AuthorityKeyIdentifier extension. This is an identifier based on the private key of the issuer of the intermediate certificate.  The identifier must be of the form `C4:A7:B1:A4:7B:2C:71:FA:DB:E1:4B:90:75:FF:C4:15:60:85:89:10`. |
| **issuer**  dictionary | Allows to specify parts of the issuer of a certificate in the chain must have to be selected.  If `select_chain[].issuer` is empty, any certificate will match.  An example value would be `{"commonName": "My Preferred CA Root"}`. |
| **subject**  dictionary | Allows to specify parts of the subject of a certificate in the chain must have to be selected.  If `select_chain[].subject` is empty, any certificate will match.  An example value would be `{"CN": "My Preferred CA Intermediate"}` |
| **subject_key_identifier**  string | Checks for the SubjectKeyIdentifier extension. This is an identifier based on the private key of the intermediate certificate.  The identifier must be of the form `A8:4A:6A:63:04:7D:DD:BA:E6:D1:39:B7:A6:45:65:EF:F3:A8:EC:A1`. |
| **test_certificates**  string | Determines which certificates in the chain will be tested.  `all` tests all certificates in the chain (excluding the leaf, which is identical in all chains).  `first` only tests the first certificate in the chain, that is the one which signed the leaf.  `last` only tests the last certificate in the chain, that is the one furthest away from the leaf. Its issuer is the root certificate of this chain.  **Choices:**   - `"first"` - `"last"` - `"all"` ← (default) |
| **select_crypto_backend**  string | Determines which crypto backend to use.  The default choice is `auto`, which tries to use `cryptography` if available, and falls back to `openssl`.  If set to `openssl`, will try to use the `openssl` binary.  If set to `cryptography`, will try to use the [cryptography](https://cryptography.io/) library.  **Choices:**   - `"auto"` ← (default) - `"cryptography"` - `"openssl"` |
| **terms_agreed**  boolean | Boolean indicating whether you agree to the terms of service document.  ACME servers can require this to be true.  This option will only be used when `acme_version` is not 1.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether calls to the ACME directory will validate TLS certificates.  **Warning:** Should **only ever** be set to `false` for testing purposes, for example when testing against a local Pebble server.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](acme_certificate_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | **Action groups:** **community.crypto.acme**, **acme** | Use `group/acme` or `group/community.crypto.acme` in `module_defaults` to set defaults for this module. |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |
| **safe_file_operations** | **Support:** **full** | Uses Ansible’s strict file operation functions to ensure proper permissions and avoid data corruption. |

## [Notes](acme_certificate_module.md#id5)

> **Note:**
>
> - At least one of `dest` and `fullchain_dest` must be specified.
> - This module includes basic account management functionality. If you want to have more control over your ACME account, use the [community.crypto.acme_account](acme_account_module.md#ansible-collections-community-crypto-acme-account-module) module and disable account management for this module using the `modify_account` option.
> - This module was called `letsencrypt` before Ansible 2.6. The usage did not change.
> - If a new enough version of the `cryptography` library is available (see Requirements for details), it will be used instead of the `openssl` binary. This can be explicitly disabled or enabled with the `select_crypto_backend` option. Note that using the `openssl` binary will be slower and less secure, as private key contents always have to be stored on disk (see `account_key_content`).
> - Although the defaults are chosen so that the module can be used with the [Let’s Encrypt](https://letsencrypt.org/) CA, the module can in principle be used with any CA providing an ACME endpoint, such as [Buypass Go SSL](https://www.buypass.com/ssl/products/acme).
> - So far, the ACME modules have only been tested by the developers against Let’s Encrypt (staging and production), Buypass (staging and production), ZeroSSL (production), and [Pebble testing server](https://github.com/letsencrypt/Pebble). We have got community feedback that they also work with Sectigo ACME Service for InCommon. If you experience problems with another ACME server, please [create an issue](https://github.com/ansible-collections/community.crypto/issues/new/choose) to help us supporting it. Feedback that an ACME server not mentioned does work is also appreciated.

## [See Also](acme_certificate_module.md#id6)

> **See also:**
>
> [The Let’s Encrypt documentation](https://letsencrypt.org/docs/)
> :   Documentation for the Let’s Encrypt Certification Authority. Provides useful information for example on rate limits.
>
> [Buypass Go SSL](https://www.buypass.com/ssl/products/acme)
> :   Documentation for the Buypass Certification Authority. Provides useful information for example on rate limits.
>
> [Automatic Certificate Management Environment (ACME)](https://tools.ietf.org/html/rfc8555)
> :   The specification of the ACME protocol (RFC 8555).
>
> [ACME TLS ALPN Challenge Extension](https://www.rfc-editor.org/rfc/rfc8737.html-05)
> :   The specification of the `tls-alpn-01` challenge (RFC 8737).
>
> [community.crypto.acme_challenge_cert_helper](acme_challenge_cert_helper_module.md#ansible-collections-community-crypto-acme-challenge-cert-helper-module)
> :   Helps preparing `tls-alpn-01` challenges.
>
> [community.crypto.openssl_privatekey](openssl_privatekey_module.md#ansible-collections-community-crypto-openssl-privatekey-module)
> :   Can be used to create private keys (both for certificates and accounts).
>
> [community.crypto.openssl_privatekey_pipe](openssl_privatekey_pipe_module.md#ansible-collections-community-crypto-openssl-privatekey-pipe-module)
> :   Can be used to create private keys without writing it to disk (both for certificates and accounts).
>
> [community.crypto.openssl_csr](openssl_csr_module.md#ansible-collections-community-crypto-openssl-csr-module)
> :   Can be used to create a Certificate Signing Request (CSR).
>
> [community.crypto.openssl_csr_pipe](openssl_csr_pipe_module.md#ansible-collections-community-crypto-openssl-csr-pipe-module)
> :   Can be used to create a Certificate Signing Request (CSR) without writing it to disk.
>
> [community.crypto.certificate_complete_chain](certificate_complete_chain_module.md#ansible-collections-community-crypto-certificate-complete-chain-module)
> :   Allows to find the root certificate for the returned fullchain.
>
> [community.crypto.acme_certificate_revoke](acme_certificate_revoke_module.md#ansible-collections-community-crypto-acme-certificate-revoke-module)
> :   Allows to revoke certificates.
>
> [community.crypto.acme_account](acme_account_module.md#ansible-collections-community-crypto-acme-account-module)
> :   Allows to create, modify or delete an ACME account.
>
> [community.crypto.acme_inspect](acme_inspect_module.md#ansible-collections-community-crypto-acme-inspect-module)
> :   Allows to debug problems.

## [Examples](acme_certificate_module.md#id7)

```yaml+jinja
### Example with HTTP challenge ###

- name: Create a challenge for sample.com using a account key from a variable.
  community.crypto.acme_certificate:
    account_key_content: "{{ account_private_key }}"
    csr: /etc/pki/cert/csr/sample.com.csr
    dest: /etc/httpd/ssl/sample.com.crt
  register: sample_com_challenge

# Alternative first step:
- name: Create a challenge for sample.com using a account key from Hashi Vault.
  community.crypto.acme_certificate:
    account_key_content: >-
      {{ lookup('community.hashi_vault.hashi_vault', 'secret=secret/account_private_key:value') }}
    csr: /etc/pki/cert/csr/sample.com.csr
    fullchain_dest: /etc/httpd/ssl/sample.com-fullchain.crt
  register: sample_com_challenge

# Alternative first step:
- name: Create a challenge for sample.com using a account key file.
  community.crypto.acme_certificate:
    account_key_src: /etc/pki/cert/private/account.key
    csr_content: "{{ lookup('file', '/etc/pki/cert/csr/sample.com.csr') }}"
    dest: /etc/httpd/ssl/sample.com.crt
    fullchain_dest: /etc/httpd/ssl/sample.com-fullchain.crt
  register: sample_com_challenge

# perform the necessary steps to fulfill the challenge
# for example:
#
# - name: Copy http-01 challenge for sample.com
#   ansible.builtin.copy:
#     dest: /var/www/html/{{ sample_com_challenge['challenge_data']['sample.com']['http-01']['resource'] }}
#     content: "{{ sample_com_challenge['challenge_data']['sample.com']['http-01']['resource_value'] }}"
#   when: sample_com_challenge is changed and 'sample.com' in sample_com_challenge['challenge_data']
#
# Alternative way:
#
# - name: Copy http-01 challenges
#   ansible.builtin.copy:
#     dest: /var/www/{{ item.key }}/{{ item.value['http-01']['resource'] }}
#     content: "{{ item.value['http-01']['resource_value'] }}"
#   loop: "{{ sample_com_challenge.challenge_data | dict2items }}"
#   when: sample_com_challenge is changed

- name: Let the challenge be validated and retrieve the cert and intermediate certificate
  community.crypto.acme_certificate:
    account_key_src: /etc/pki/cert/private/account.key
    csr: /etc/pki/cert/csr/sample.com.csr
    dest: /etc/httpd/ssl/sample.com.crt
    fullchain_dest: /etc/httpd/ssl/sample.com-fullchain.crt
    chain_dest: /etc/httpd/ssl/sample.com-intermediate.crt
    data: "{{ sample_com_challenge }}"

### Example with DNS challenge against production ACME server ###

- name: Create a challenge for sample.com using a account key file.
  community.crypto.acme_certificate:
    account_key_src: /etc/pki/cert/private/account.key
    account_email: myself@sample.com
    src: /etc/pki/cert/csr/sample.com.csr
    cert: /etc/httpd/ssl/sample.com.crt
    challenge: dns-01
    acme_directory: https://acme-v01.api.letsencrypt.org/directory
    # Renew if the certificate is at least 30 days old
    remaining_days: 60
  register: sample_com_challenge

# perform the necessary steps to fulfill the challenge
# for example:
#
# - name: Create DNS record for sample.com dns-01 challenge
#   community.aws.route53:
#     zone: sample.com
#     record: "{{ sample_com_challenge.challenge_data['sample.com']['dns-01'].record }}"
#     type: TXT
#     ttl: 60
#     state: present
#     wait: true
#     # Note: route53 requires TXT entries to be enclosed in quotes
#     value: "{{ sample_com_challenge.challenge_data['sample.com']['dns-01'].resource_value | regex_replace('^(.*)$', '\"\\1\"') }}"
#   when: sample_com_challenge is changed and 'sample.com' in sample_com_challenge.challenge_data
#
# Alternative way:
#
# - name: Create DNS records for dns-01 challenges
#   community.aws.route53:
#     zone: sample.com
#     record: "{{ item.key }}"
#     type: TXT
#     ttl: 60
#     state: present
#     wait: true
#     # Note: item.value is a list of TXT entries, and route53
#     # requires every entry to be enclosed in quotes
#     value: "{{ item.value | map('regex_replace', '^(.*)$', '\"\\1\"' ) | list }}"
#   loop: "{{ sample_com_challenge.challenge_data_dns | dict2items }}"
#   when: sample_com_challenge is changed

- name: Let the challenge be validated and retrieve the cert and intermediate certificate
  community.crypto.acme_certificate:
    account_key_src: /etc/pki/cert/private/account.key
    account_email: myself@sample.com
    src: /etc/pki/cert/csr/sample.com.csr
    cert: /etc/httpd/ssl/sample.com.crt
    fullchain: /etc/httpd/ssl/sample.com-fullchain.crt
    chain: /etc/httpd/ssl/sample.com-intermediate.crt
    challenge: dns-01
    acme_directory: https://acme-v01.api.letsencrypt.org/directory
    remaining_days: 60
    data: "{{ sample_com_challenge }}"
  when: sample_com_challenge is changed

# Alternative second step:
- name: Let the challenge be validated and retrieve the cert and intermediate certificate
  community.crypto.acme_certificate:
    account_key_src: /etc/pki/cert/private/account.key
    account_email: myself@sample.com
    src: /etc/pki/cert/csr/sample.com.csr
    cert: /etc/httpd/ssl/sample.com.crt
    fullchain: /etc/httpd/ssl/sample.com-fullchain.crt
    chain: /etc/httpd/ssl/sample.com-intermediate.crt
    challenge: tls-alpn-01
    remaining_days: 60
    data: "{{ sample_com_challenge }}"
    # We use Let's Encrypt's ACME v2 endpoint
    acme_directory: https://acme-v02.api.letsencrypt.org/directory
    acme_version: 2
    # The following makes sure that if a chain with /CN=DST Root CA X3 in its issuer is provided
    # as an alternative, it will be selected. These are the roots cross-signed by IdenTrust.
    # As long as Let's Encrypt provides alternate chains with the cross-signed root(s) when
    # switching to their own ISRG Root X1 root, this will use the chain ending with a cross-signed
    # root. This chain is more compatible with older TLS clients.
    select_chain:
      - test_certificates: last
        issuer:
          CN: DST Root CA X3
          O: Digital Signature Trust Co.
  when: sample_com_challenge is changed
```

## [Return Values](acme_certificate_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **account_uri**  string | ACME account URI.  **Returned:** changed |
| **all_chains**  list / elements=dictionary | When `retrieve_all_alternates` is set to `true`, the module will query the ACME server for alternate chains. This return value will contain a list of all chains returned, the first entry being the main chain returned by the server.  See [Section 7.4.2 of RFC8555](https://tools.ietf.org/html/rfc8555#section-7.4.2) for details.  **Returned:** when certificate was retrieved and `retrieve_all_alternates` is set to `true` |
| **cert**  string | The leaf certificate itself, in PEM format.  **Returned:** always |
| **chain**  string | The certificate chain, excluding the root, as concatenated PEM certificates.  **Returned:** always |
| **full_chain**  string | The certificate chain, excluding the root, but including the leaf certificate, as concatenated PEM certificates.  **Returned:** always |
| **authorizations**  dictionary | ACME authorization data.  Maps an identifier to ACME authorization objects. See <https://tools.ietf.org/html/rfc8555#section-7.1.4>.  **Returned:** changed  **Sample:** `{"example.com": {"challenges": [{"status": "valid", "token": "A5b1C3d2E9f8G7h6", "type": "http-01", "url": "https://example.org/acme/challenge/12345", "validated": "2022-08-01T01:01:02.34Z"}], "expires": "2022-08-04T01:02:03.45Z", "identifier": {"type": "dns", "value": "example.com"}, "status": "valid", "wildcard": false}}` |
| **cert_days**  integer | The number of days the certificate remains valid.  **Returned:** success |
| **challenge_data**  list / elements=dictionary | Per identifier / challenge type challenge data.  Since Ansible 2.8.5, only challenges which are not yet valid are returned.  **Returned:** changed |
| **record**  string | The full DNS record’s name for the challenge.  **Returned:** changed and challenge is `dns-01`  **Sample:** `"_acme-challenge.example.com"` |
| **resource**  string | The challenge resource that must be created for validation.  **Returned:** changed  **Sample:** `".well-known/acme-challenge/evaGxfADs6pSRb2LAv9IZf17Dt3juxGJ-PCt92wr-oA"` |
| **resource_original**  string | The original challenge resource including type identifier for `tls-alpn-01` challenges.  **Returned:** changed and `challenge` is `tls-alpn-01`  **Sample:** `"DNS:example.com"` |
| **resource_value**  string | The value the resource has to produce for the validation.  For `http-01` and `dns-01` challenges, the value can be used as-is.  For `tls-alpn-01` challenges, note that this return value contains a Base64 encoded version of the correct binary blob which has to be put into the acmeValidation x509 extension; see <https://www.rfc-editor.org/rfc/rfc8737.html#section-3> for details. To do this, you might need the [ansible.builtin.b64decode](../../ansible/builtin/b64decode_filter.md#ansible-collections-ansible-builtin-b64decode-filter) Jinja filter to extract the binary blob from this return value.  **Returned:** changed  **Sample:** `"IlirfxKKXA...17Dt3juxGJ-PCt92wr-oA"` |
| **challenge_data_dns**  dictionary | List of TXT values per DNS record, in case challenge is `dns-01`.  Since Ansible 2.8.5, only challenges which are not yet valid are returned.  **Returned:** changed |
| **finalization_uri**  string | ACME finalization URI.  **Returned:** changed |
| **order_uri**  string | ACME order URI.  **Returned:** changed |

### Authors

- Michael Gruener (@mgruener)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.crypto)
- [Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-crypto)
