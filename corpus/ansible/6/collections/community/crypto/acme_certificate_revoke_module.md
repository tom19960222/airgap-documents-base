---
collection: ansible
version: "6"
title: "community.crypto.acme_certificate_revoke module – Revoke certificates with the ACME protocol"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/crypto/acme_certificate_revoke_module.html
fetched_at: 2026-07-27T17:06:11+00:00
---
# community.crypto.acme_certificate_revoke module – Revoke certificates with the ACME protocol

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
> see [Requirements](acme_certificate_revoke_module.md#ansible-collections-community-crypto-acme-certificate-revoke-module-requirements) for details.
>
> To use it in a playbook, specify: `community.crypto.acme_certificate_revoke`.

- [Synopsis](acme_certificate_revoke_module.md#synopsis)
- [Requirements](acme_certificate_revoke_module.md#requirements)
- [Parameters](acme_certificate_revoke_module.md#parameters)
- [Attributes](acme_certificate_revoke_module.md#attributes)
- [Notes](acme_certificate_revoke_module.md#notes)
- [See Also](acme_certificate_revoke_module.md#see-also)
- [Examples](acme_certificate_revoke_module.md#examples)

## [Synopsis](acme_certificate_revoke_module.md#id1)

- Allows to revoke certificates issued by a CA supporting the [ACME protocol](https://tools.ietf.org/html/rfc8555), such as [Let’s Encrypt](https://letsencrypt.org/).

## [Requirements](acme_certificate_revoke_module.md#id2)

The below requirements are needed on the host that executes this module.

- either openssl or [cryptography](https://cryptography.io/) >= 1.5
- ipaddress

## [Parameters](acme_certificate_revoke_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account_key_content**  string | Content of the ACME account RSA or Elliptic Curve key.  Note that exactly one of `account_key_src`, `account_key_content`, `private_key_src` or `private_key_content` must be specified.  *Warning*: the content will be written into a temporary file, which will be deleted by Ansible when the module completes. Since this is an important private key — it can be used to change the account key, or to revoke your certificates without knowing their private keys —, this might not be acceptable.  In case `cryptography` is used, the content is not written into a temporary file. It can still happen that it is written to disk by Ansible in the process of moving the module with its argument to the node where it is executed. |
| **account_key_passphrase**  string  added in community.crypto 1.6.0 | Phassphrase to use to decode the account key.  **Note:** this is not supported by the `openssl` backend, only by the `cryptography` backend. |
| **account_key_src**  aliases: account_key  path | Path to a file containing the ACME account RSA or Elliptic Curve key.  RSA keys can be created with `openssl rsa ...`. Elliptic curve keys can be created with `openssl ecparam -genkey ...`. Any other tool creating private keys in PEM format can be used as well.  Mutually exclusive with `account_key_content`.  Required if `account_key_content` is not used. |
| **account_uri**  string | If specified, assumes that the account URI is as given. If the account key does not match this account, or an account with this URI does not exist, the module fails. |
| **acme_directory**  string / required | The ACME directory to use. This is the entry point URL to access the ACME CA server API.  For safety reasons the default is set to the Let’s Encrypt staging server (for the ACME v1 protocol). This will create technically correct, but untrusted certificates.  For Let’s Encrypt, all staging endpoints can be found here: <https://letsencrypt.org/docs/staging-environment/>. For Buypass, all endpoints can be found here: <https://community.buypass.com/t/63d4ay/buypass-go-ssl-endpoints>  For **Let’s Encrypt**, the production directory URL for ACME v2 is <https://acme-v02.api.letsencrypt.org/directory>.  For **Buypass**, the production directory URL for ACME v2 and v1 is <https://api.buypass.com/acme/directory>.  For **ZeroSSL**, the production directory URL for ACME v2 is <https://acme.zerossl.com/v2/DV90>.  For **Sectigo**, the production directory URL for ACME v2 is <https://acme-qa.secure.trust-provider.com/v2/DV>.  The notes for this module contain a list of ACME services this module has been tested against. |
| **acme_version**  integer / required | The ACME version of the endpoint.  Must be `1` for the classic Let’s Encrypt and Buypass ACME endpoints, or `2` for standardized ACME v2 endpoints.  The value `1` is deprecated since community.crypto 2.0.0 and will be removed from community.crypto 3.0.0.  Choices:   - `1` - `2` |
| **certificate**  path / required | Path to the certificate to revoke. |
| **private_key_content**  string | Content of the certificate’s private key.  Note that exactly one of `account_key_src`, `account_key_content`, `private_key_src` or `private_key_content` must be specified.  *Warning*: the content will be written into a temporary file, which will be deleted by Ansible when the module completes. Since this is an important private key — it can be used to change the account key, or to revoke your certificates without knowing their private keys —, this might not be acceptable.  In case `cryptography` is used, the content is not written into a temporary file. It can still happen that it is written to disk by Ansible in the process of moving the module with its argument to the node where it is executed. |
| **private_key_passphrase**  string  added in community.crypto 1.6.0 | Phassphrase to use to decode the certificate’s private key.  **Note:** this is not supported by the `openssl` backend, only by the `cryptography` backend. |
| **private_key_src**  path | Path to the certificate’s private key.  Note that exactly one of `account_key_src`, `account_key_content`, `private_key_src` or `private_key_content` must be specified. |
| **request_timeout**  integer  added in community.crypto 2.3.0 | The time Ansible should wait for a response from the ACME API.  This timeout is applied to all HTTP(S) requests (HEAD, GET, POST).  Default: `10` |
| **revoke_reason**  integer | One of the revocation reasonCodes defined in [Section 5.3.1 of RFC5280](https://tools.ietf.org/html/rfc5280#section-5.3.1).  Possible values are `0` (unspecified), `1` (keyCompromise), `2` (cACompromise), `3` (affiliationChanged), `4` (superseded), `5` (cessationOfOperation), `6` (certificateHold), `8` (removeFromCRL), `9` (privilegeWithdrawn), `10` (aACompromise). |
| **select_crypto_backend**  string | Determines which crypto backend to use.  The default choice is `auto`, which tries to use `cryptography` if available, and falls back to `openssl`.  If set to `openssl`, will try to use the `openssl` binary.  If set to `cryptography`, will try to use the [cryptography](https://cryptography.io/) library.  Choices:   - `"auto"` ← (default) - `"cryptography"` - `"openssl"` |
| **validate_certs**  boolean | Whether calls to the ACME directory will validate TLS certificates.  **Warning:** Should **only ever** be set to `false` for testing purposes, for example when testing against a local Pebble server.  Choices:   - `false` - `true` ← (default) |

## [Attributes](acme_certificate_revoke_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | Action groups: community.crypto.acme, acme | Use `group/acme` or `group/community.crypto.acme` in `module_defaults` to set defaults for this module. |
| **check_mode** | Support: none | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support: none | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](acme_certificate_revoke_module.md#id5)

> **Note:**
>
> - Exactly one of `account_key_src`, `account_key_content`, `private_key_src` or `private_key_content` must be specified.
> - Trying to revoke an already revoked certificate should result in an unchanged status, even if the revocation reason was different than the one specified here. Also, depending on the server, it can happen that some other error is returned if the certificate has already been revoked.
> - If a new enough version of the `cryptography` library is available (see Requirements for details), it will be used instead of the `openssl` binary. This can be explicitly disabled or enabled with the `select_crypto_backend` option. Note that using the `openssl` binary will be slower and less secure, as private key contents always have to be stored on disk (see `account_key_content`).
> - Although the defaults are chosen so that the module can be used with the [Let’s Encrypt](https://letsencrypt.org/) CA, the module can in principle be used with any CA providing an ACME endpoint, such as [Buypass Go SSL](https://www.buypass.com/ssl/products/acme).
> - So far, the ACME modules have only been tested by the developers against Let’s Encrypt (staging and production), Buypass (staging and production), ZeroSSL (production), and [Pebble testing server](https://github.com/letsencrypt/Pebble). We have got community feedback that they also work with Sectigo ACME Service for InCommon. If you experience problems with another ACME server, please [create an issue](https://github.com/ansible-collections/community.crypto/issues/new/choose) to help us supporting it. Feedback that an ACME server not mentioned does work is also appreciated.

## [See Also](acme_certificate_revoke_module.md#id6)

> **See also:**
>
> [The Let’s Encrypt documentation](https://letsencrypt.org/docs/)
> :   Documentation for the Let’s Encrypt Certification Authority. Provides useful information for example on rate limits.
>
> [Automatic Certificate Management Environment (ACME)](https://tools.ietf.org/html/rfc8555)
> :   The specification of the ACME protocol (RFC 8555).
>
> [community.crypto.acme_inspect](acme_inspect_module.md#ansible-collections-community-crypto-acme-inspect-module)
> :   Allows to debug problems.

## [Examples](acme_certificate_revoke_module.md#id7)

```yaml+jinja
- name: Revoke certificate with account key
  community.crypto.acme_certificate_revoke:
    account_key_src: /etc/pki/cert/private/account.key
    certificate: /etc/httpd/ssl/sample.com.crt

- name: Revoke certificate with certificate's private key
  community.crypto.acme_certificate_revoke:
    private_key_src: /etc/httpd/ssl/sample.com.key
    certificate: /etc/httpd/ssl/sample.com.crt
```

### Authors

- Felix Fontein (@felixfontein)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.crypto)
[Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-crypto)
