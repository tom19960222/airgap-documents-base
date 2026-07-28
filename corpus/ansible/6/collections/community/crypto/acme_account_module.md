---
collection: ansible
version: "6"
title: "community.crypto.acme_account module – Create, modify or delete ACME accounts"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/crypto/acme_account_module.html
fetched_at: 2026-07-27T17:06:09+00:00
---
# community.crypto.acme_account module – Create, modify or delete ACME accounts

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
> see [Requirements](acme_account_module.md#ansible-collections-community-crypto-acme-account-module-requirements) for details.
>
> To use it in a playbook, specify: `community.crypto.acme_account`.

- [Synopsis](acme_account_module.md#synopsis)
- [Requirements](acme_account_module.md#requirements)
- [Parameters](acme_account_module.md#parameters)
- [Attributes](acme_account_module.md#attributes)
- [Notes](acme_account_module.md#notes)
- [See Also](acme_account_module.md#see-also)
- [Examples](acme_account_module.md#examples)
- [Return Values](acme_account_module.md#return-values)

## [Synopsis](acme_account_module.md#id1)

- Allows to create, modify or delete accounts with a CA supporting the [ACME protocol](https://tools.ietf.org/html/rfc8555), such as [Let’s Encrypt](https://letsencrypt.org/).
- This module only works with the ACME v2 protocol.

## [Requirements](acme_account_module.md#id2)

The below requirements are needed on the host that executes this module.

- either openssl or [cryptography](https://cryptography.io/) >= 1.5
- ipaddress

## [Parameters](acme_account_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account_key_content**  string | Content of the ACME account RSA or Elliptic Curve key.  Mutually exclusive with `account_key_src`.  Required if `account_key_src` is not used.  **Warning:** the content will be written into a temporary file, which will be deleted by Ansible when the module completes. Since this is an important private key — it can be used to change the account key, or to revoke your certificates without knowing their private keys —, this might not be acceptable.  In case `cryptography` is used, the content is not written into a temporary file. It can still happen that it is written to disk by Ansible in the process of moving the module with its argument to the node where it is executed. |
| **account_key_passphrase**  string  added in community.crypto 1.6.0 | Phassphrase to use to decode the account key.  **Note:** this is not supported by the `openssl` backend, only by the `cryptography` backend. |
| **account_key_src**  aliases: account_key  path | Path to a file containing the ACME account RSA or Elliptic Curve key.  Private keys can be created with the [community.crypto.openssl_privatekey](openssl_privatekey_module.md#ansible-collections-community-crypto-openssl-privatekey-module) or [community.crypto.openssl_privatekey_pipe](openssl_privatekey_pipe_module.md#ansible-collections-community-crypto-openssl-privatekey-pipe-module) modules. If the requisite (cryptography) is not available, keys can also be created directly with the `openssl` command line tool: RSA keys can be created with `openssl genrsa ...`. Elliptic curve keys can be created with `openssl ecparam -genkey ...`. Any other tool creating private keys in PEM format can be used as well.  Mutually exclusive with `account_key_content`.  Required if `account_key_content` is not used. |
| **account_uri**  string | If specified, assumes that the account URI is as given. If the account key does not match this account, or an account with this URI does not exist, the module fails. |
| **acme_directory**  string / required | The ACME directory to use. This is the entry point URL to access the ACME CA server API.  For safety reasons the default is set to the Let’s Encrypt staging server (for the ACME v1 protocol). This will create technically correct, but untrusted certificates.  For Let’s Encrypt, all staging endpoints can be found here: <https://letsencrypt.org/docs/staging-environment/>. For Buypass, all endpoints can be found here: <https://community.buypass.com/t/63d4ay/buypass-go-ssl-endpoints>  For **Let’s Encrypt**, the production directory URL for ACME v2 is <https://acme-v02.api.letsencrypt.org/directory>.  For **Buypass**, the production directory URL for ACME v2 and v1 is <https://api.buypass.com/acme/directory>.  For **ZeroSSL**, the production directory URL for ACME v2 is <https://acme.zerossl.com/v2/DV90>.  For **Sectigo**, the production directory URL for ACME v2 is <https://acme-qa.secure.trust-provider.com/v2/DV>.  The notes for this module contain a list of ACME services this module has been tested against. |
| **acme_version**  integer / required | The ACME version of the endpoint.  Must be `1` for the classic Let’s Encrypt and Buypass ACME endpoints, or `2` for standardized ACME v2 endpoints.  The value `1` is deprecated since community.crypto 2.0.0 and will be removed from community.crypto 3.0.0.  Choices:   - `1` - `2` |
| **allow_creation**  boolean | Whether account creation is allowed (when state is `present`).  Choices:   - `false` - `true` ← (default) |
| **contact**  list / elements=string | A list of contact URLs.  Email addresses must be prefixed with `mailto:`.  See <https://tools.ietf.org/html/rfc8555#section-7.3> for what is allowed.  Must be specified when state is `present`. Will be ignored if state is `absent` or `changed_key`.  Default: `[]` |
| **external_account_binding**  dictionary  added in community.crypto 1.1.0 | Allows to provide external account binding data during account creation.  This is used by CAs like Sectigo to bind a new ACME account to an existing CA-specific account, to be able to properly identify a customer.  Only used when creating a new account. Can not be specified for ACME v1. |
| **alg**  string / required | The MAC algorithm provided by the CA.  If not specified by the CA, this is probably `HS256`.  Choices:   - `"HS256"` - `"HS384"` - `"HS512"` |
| **key**  string / required | Base64 URL encoded value of the MAC key provided by the CA.  Padding (`=` symbols at the end) can be omitted. |
| **kid**  string / required | The key identifier provided by the CA. |
| **new_account_key_content**  string | Content of the ACME account RSA or Elliptic Curve key to change to.  Same restrictions apply as to `account_key_content`.  Mutually exclusive with `new_account_key_src`.  Required if `new_account_key_src` is not used and state is `changed_key`. |
| **new_account_key_passphrase**  string  added in community.crypto 1.6.0 | Phassphrase to use to decode the new account key.  **Note:** this is not supported by the `openssl` backend, only by the `cryptography` backend. |
| **new_account_key_src**  path | Path to a file containing the ACME account RSA or Elliptic Curve key to change to.  Same restrictions apply as to `account_key_src`.  Mutually exclusive with `new_account_key_content`.  Required if `new_account_key_content` is not used and state is `changed_key`. |
| **request_timeout**  integer  added in community.crypto 2.3.0 | The time Ansible should wait for a response from the ACME API.  This timeout is applied to all HTTP(S) requests (HEAD, GET, POST).  Default: `10` |
| **select_crypto_backend**  string | Determines which crypto backend to use.  The default choice is `auto`, which tries to use `cryptography` if available, and falls back to `openssl`.  If set to `openssl`, will try to use the `openssl` binary.  If set to `cryptography`, will try to use the [cryptography](https://cryptography.io/) library.  Choices:   - `"auto"` ← (default) - `"cryptography"` - `"openssl"` |
| **state**  string / required | The state of the account, to be identified by its account key.  If the state is `absent`, the account will either not exist or be deactivated.  If the state is `changed_key`, the account must exist. The account key will be changed; no other information will be touched.  Choices:   - `"present"` - `"absent"` - `"changed_key"` |
| **terms_agreed**  boolean | Boolean indicating whether you agree to the terms of service document.  ACME servers can require this to be true.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether calls to the ACME directory will validate TLS certificates.  **Warning:** Should **only ever** be set to `false` for testing purposes, for example when testing against a local Pebble server.  Choices:   - `false` - `true` ← (default) |

## [Attributes](acme_account_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | Action groups: community.crypto.acme, acme | Use `group/acme` or `group/community.crypto.acme` in `module_defaults` to set defaults for this module. |
| **check_mode** | Support: full | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support: full | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](acme_account_module.md#id5)

> **Note:**
>
> - The [community.crypto.acme_certificate](acme_certificate_module.md#ansible-collections-community-crypto-acme-certificate-module) module also allows to do basic account management. When using both modules, it is recommended to disable account management for [community.crypto.acme_certificate](acme_certificate_module.md#ansible-collections-community-crypto-acme-certificate-module). For that, use the `modify_account` option of [community.crypto.acme_certificate](acme_certificate_module.md#ansible-collections-community-crypto-acme-certificate-module).
> - If a new enough version of the `cryptography` library is available (see Requirements for details), it will be used instead of the `openssl` binary. This can be explicitly disabled or enabled with the `select_crypto_backend` option. Note that using the `openssl` binary will be slower and less secure, as private key contents always have to be stored on disk (see `account_key_content`).
> - Although the defaults are chosen so that the module can be used with the [Let’s Encrypt](https://letsencrypt.org/) CA, the module can in principle be used with any CA providing an ACME endpoint, such as [Buypass Go SSL](https://www.buypass.com/ssl/products/acme).
> - So far, the ACME modules have only been tested by the developers against Let’s Encrypt (staging and production), Buypass (staging and production), ZeroSSL (production), and [Pebble testing server](https://github.com/letsencrypt/Pebble). We have got community feedback that they also work with Sectigo ACME Service for InCommon. If you experience problems with another ACME server, please [create an issue](https://github.com/ansible-collections/community.crypto/issues/new/choose) to help us supporting it. Feedback that an ACME server not mentioned does work is also appreciated.

## [See Also](acme_account_module.md#id6)

> **See also:**
>
> [Automatic Certificate Management Environment (ACME)](https://tools.ietf.org/html/rfc8555)
> :   The specification of the ACME protocol (RFC 8555).
>
> [community.crypto.acme_account_info](acme_account_info_module.md#ansible-collections-community-crypto-acme-account-info-module)
> :   Retrieves facts about an ACME account.
>
> [community.crypto.openssl_privatekey](openssl_privatekey_module.md#ansible-collections-community-crypto-openssl-privatekey-module)
> :   Can be used to create a private account key.
>
> [community.crypto.openssl_privatekey_pipe](openssl_privatekey_pipe_module.md#ansible-collections-community-crypto-openssl-privatekey-pipe-module)
> :   Can be used to create a private account key without writing it to disk.
>
> [community.crypto.acme_inspect](acme_inspect_module.md#ansible-collections-community-crypto-acme-inspect-module)
> :   Allows to debug problems.

## [Examples](acme_account_module.md#id7)

```yaml+jinja
- name: Make sure account exists and has given contacts. We agree to TOS.
  community.crypto.acme_account:
    account_key_src: /etc/pki/cert/private/account.key
    state: present
    terms_agreed: true
    contact:
    - mailto:me@example.com
    - mailto:myself@example.org

- name: Make sure account has given email address. Do not create account if it does not exist
  community.crypto.acme_account:
    account_key_src: /etc/pki/cert/private/account.key
    state: present
    allow_creation: false
    contact:
    - mailto:me@example.com

- name: Change account's key to the one stored in the variable new_account_key
  community.crypto.acme_account:
    account_key_src: /etc/pki/cert/private/account.key
    new_account_key_content: '{{ new_account_key }}'
    state: changed_key

- name: Delete account (we have to use the new key)
  community.crypto.acme_account:
    account_key_content: '{{ new_account_key }}'
    state: absent
```

## [Return Values](acme_account_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **account_uri**  string | ACME account URI, or None if account does not exist.  Returned: always |

### Authors

- Felix Fontein (@felixfontein)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.crypto)
[Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-crypto)
