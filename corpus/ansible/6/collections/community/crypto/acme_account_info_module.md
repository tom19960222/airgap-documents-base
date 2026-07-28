---
collection: ansible
version: "6"
title: "community.crypto.acme_account_info module – Retrieves information on ACME accounts"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/crypto/acme_account_info_module.html
fetched_at: 2026-07-27T17:06:10+00:00
---
# community.crypto.acme_account_info module – Retrieves information on ACME accounts

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
> see [Requirements](acme_account_info_module.md#ansible-collections-community-crypto-acme-account-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.crypto.acme_account_info`.

- [Synopsis](acme_account_info_module.md#synopsis)
- [Requirements](acme_account_info_module.md#requirements)
- [Parameters](acme_account_info_module.md#parameters)
- [Attributes](acme_account_info_module.md#attributes)
- [Notes](acme_account_info_module.md#notes)
- [See Also](acme_account_info_module.md#see-also)
- [Examples](acme_account_info_module.md#examples)
- [Return Values](acme_account_info_module.md#return-values)

## [Synopsis](acme_account_info_module.md#id1)

- Allows to retrieve information on accounts a CA supporting the [ACME protocol](https://tools.ietf.org/html/rfc8555), such as [Let’s Encrypt](https://letsencrypt.org/).
- This module only works with the ACME v2 protocol.

## [Requirements](acme_account_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- either openssl or [cryptography](https://cryptography.io/) >= 1.5
- ipaddress

## [Parameters](acme_account_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account_key_content**  string | Content of the ACME account RSA or Elliptic Curve key.  Mutually exclusive with `account_key_src`.  Required if `account_key_src` is not used.  **Warning:** the content will be written into a temporary file, which will be deleted by Ansible when the module completes. Since this is an important private key — it can be used to change the account key, or to revoke your certificates without knowing their private keys —, this might not be acceptable.  In case `cryptography` is used, the content is not written into a temporary file. It can still happen that it is written to disk by Ansible in the process of moving the module with its argument to the node where it is executed. |
| **account_key_passphrase**  string  added in community.crypto 1.6.0 | Phassphrase to use to decode the account key.  **Note:** this is not supported by the `openssl` backend, only by the `cryptography` backend. |
| **account_key_src**  aliases: account_key  path | Path to a file containing the ACME account RSA or Elliptic Curve key.  Private keys can be created with the [community.crypto.openssl_privatekey](openssl_privatekey_module.md#ansible-collections-community-crypto-openssl-privatekey-module) or [community.crypto.openssl_privatekey_pipe](openssl_privatekey_pipe_module.md#ansible-collections-community-crypto-openssl-privatekey-pipe-module) modules. If the requisite (cryptography) is not available, keys can also be created directly with the `openssl` command line tool: RSA keys can be created with `openssl genrsa ...`. Elliptic curve keys can be created with `openssl ecparam -genkey ...`. Any other tool creating private keys in PEM format can be used as well.  Mutually exclusive with `account_key_content`.  Required if `account_key_content` is not used. |
| **account_uri**  string | If specified, assumes that the account URI is as given. If the account key does not match this account, or an account with this URI does not exist, the module fails. |
| **acme_directory**  string / required | The ACME directory to use. This is the entry point URL to access the ACME CA server API.  For safety reasons the default is set to the Let’s Encrypt staging server (for the ACME v1 protocol). This will create technically correct, but untrusted certificates.  For Let’s Encrypt, all staging endpoints can be found here: <https://letsencrypt.org/docs/staging-environment/>. For Buypass, all endpoints can be found here: <https://community.buypass.com/t/63d4ay/buypass-go-ssl-endpoints>  For **Let’s Encrypt**, the production directory URL for ACME v2 is <https://acme-v02.api.letsencrypt.org/directory>.  For **Buypass**, the production directory URL for ACME v2 and v1 is <https://api.buypass.com/acme/directory>.  For **ZeroSSL**, the production directory URL for ACME v2 is <https://acme.zerossl.com/v2/DV90>.  For **Sectigo**, the production directory URL for ACME v2 is <https://acme-qa.secure.trust-provider.com/v2/DV>.  The notes for this module contain a list of ACME services this module has been tested against. |
| **acme_version**  integer / required | The ACME version of the endpoint.  Must be `1` for the classic Let’s Encrypt and Buypass ACME endpoints, or `2` for standardized ACME v2 endpoints.  The value `1` is deprecated since community.crypto 2.0.0 and will be removed from community.crypto 3.0.0.  Choices:   - `1` - `2` |
| **request_timeout**  integer  added in community.crypto 2.3.0 | The time Ansible should wait for a response from the ACME API.  This timeout is applied to all HTTP(S) requests (HEAD, GET, POST).  Default: `10` |
| **retrieve_orders**  string | Whether to retrieve the list of order URLs or order objects, if provided by the ACME server.  A value of `ignore` will not fetch the list of orders.  If the value is not `ignore` and the ACME server supports orders, the `order_uris` return value is always populated. The `orders` return value is only returned if this option is set to `object_list`.  Currently, Let’s Encrypt does not return orders, so the `orders` result will always be empty.  Choices:   - `"ignore"` ← (default) - `"url_list"` - `"object_list"` |
| **select_crypto_backend**  string | Determines which crypto backend to use.  The default choice is `auto`, which tries to use `cryptography` if available, and falls back to `openssl`.  If set to `openssl`, will try to use the `openssl` binary.  If set to `cryptography`, will try to use the [cryptography](https://cryptography.io/) library.  Choices:   - `"auto"` ← (default) - `"cryptography"` - `"openssl"` |
| **validate_certs**  boolean | Whether calls to the ACME directory will validate TLS certificates.  **Warning:** Should **only ever** be set to `false` for testing purposes, for example when testing against a local Pebble server.  Choices:   - `false` - `true` ← (default) |

## [Attributes](acme_account_info_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | Action groups: community.crypto.acme, acme | Use `group/acme` or `group/community.crypto.acme` in `module_defaults` to set defaults for this module. |
| **check_mode** | Support: full  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support:  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](acme_account_info_module.md#id5)

> **Note:**
>
> - The [community.crypto.acme_account](acme_account_module.md#ansible-collections-community-crypto-acme-account-module) module allows to modify, create and delete ACME accounts.
> - This module was called `acme_account_facts` before Ansible 2.8. The usage did not change.
> - If a new enough version of the `cryptography` library is available (see Requirements for details), it will be used instead of the `openssl` binary. This can be explicitly disabled or enabled with the `select_crypto_backend` option. Note that using the `openssl` binary will be slower and less secure, as private key contents always have to be stored on disk (see `account_key_content`).
> - Although the defaults are chosen so that the module can be used with the [Let’s Encrypt](https://letsencrypt.org/) CA, the module can in principle be used with any CA providing an ACME endpoint, such as [Buypass Go SSL](https://www.buypass.com/ssl/products/acme).
> - So far, the ACME modules have only been tested by the developers against Let’s Encrypt (staging and production), Buypass (staging and production), ZeroSSL (production), and [Pebble testing server](https://github.com/letsencrypt/Pebble). We have got community feedback that they also work with Sectigo ACME Service for InCommon. If you experience problems with another ACME server, please [create an issue](https://github.com/ansible-collections/community.crypto/issues/new/choose) to help us supporting it. Feedback that an ACME server not mentioned does work is also appreciated.

## [See Also](acme_account_info_module.md#id6)

> **See also:**
>
> [community.crypto.acme_account](acme_account_module.md#ansible-collections-community-crypto-acme-account-module)
> :   Allows to create, modify or delete an ACME account.

## [Examples](acme_account_info_module.md#id7)

```yaml+jinja
- name: Check whether an account with the given account key exists
  community.crypto.acme_account_info:
    account_key_src: /etc/pki/cert/private/account.key
  register: account_data
- name: Verify that account exists
  assert:
    that:
      - account_data.exists
- name: Print account URI
  ansible.builtin.debug:
    var: account_data.account_uri
- name: Print account contacts
  ansible.builtin.debug:
    var: account_data.account.contact

- name: Check whether the account exists and is accessible with the given account key
  acme_account_info:
    account_key_content: "{{ acme_account_key }}"
    account_uri: "{{ acme_account_uri }}"
  register: account_data
- name: Verify that account exists
  assert:
    that:
      - account_data.exists
- name: Print account contacts
  ansible.builtin.debug:
    var: account_data.account.contact
```

## [Return Values](acme_account_info_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **account**  dictionary | The account information, as retrieved from the ACME server.  Returned: if account exists |
| **contact**  list / elements=string | the challenge resource that must be created for validation  Returned: always  Sample: `["mailto:me@example.com", "tel:00123456789"]` |
| **orders**  string | A URL where a list of orders can be retrieved for this account.  Use the *retrieve_orders* option to query this URL and retrieve the complete list of orders.  Returned: always  Sample: `"https://example.ca/account/1/orders"` |
| **public_account_key**  string | the public account key as a [JSON Web Key](https://tools.ietf.org/html/rfc7517).  Returned: always  Sample: `"{\"kty\":\"EC\",\"crv\":\"P-256\",\"x\":\"MKBCTNIcKUSDii11ySs3526iDZ8AiTo7Tu6KPAqv7D4\",\"y\":\"4Etl6SRW2YiLUrN5vfvVHuhp7x8PxltmWWlbbM4IFyM\"}"` |
| **status**  string | the account’s status  Returned: always  Can only return:   - `"valid"` - `"deactivated"` - `"revoked"`   Sample: `"valid"` |
| **account_uri**  string | ACME account URI, or None if account does not exist.  Returned: always |
| **exists**  boolean | Whether the account exists.  Returned: always |
| **order_uris**  list / elements=string  added in community.crypto 1.5.0 | The list of orders.  If *retrieve_orders* is `url_list`, this will be a list of URLs.  If *retrieve_orders* is `object_list`, this will be a list of objects.  Returned: if account exists, *retrieve_orders* is not `ignore`, and server supports order listing |
| **orders**  list / elements=dictionary | The list of orders.  Returned: if account exists, *retrieve_orders* is `object_list`, and server supports order listing |
| **authorizations**  list / elements=string | A list of URLs for authorizations for this order.  Returned: success |
| **certificate**  string | The URL for retrieving the certificate.  Returned: when certificate was issued |
| **error**  dictionary | In case an error occurred during processing, this contains information about the error.  The field is structured as a problem document (RFC7807).  Returned: when an error occurred |
| **expires**  string | When the order expires.  Timestamp should be formatted as described in RFC3339.  Only required to be included in result when *status* is `pending` or `valid`.  Returned: when server gives expiry date |
| **finalize**  string | A URL used for finalizing an ACME order.  Returned: success |
| **identifiers**  list / elements=dictionary | List of identifiers this order is for.  Returned: success |
| **type**  string | Type of identifier. `dns` or `ip`.  Returned: success |
| **value**  string | Name of identifier. Hostname or IP address.  Returned: success |
| **wildcard**  boolean | Whether *value* is actually a wildcard. The wildcard prefix `*.` is not included in *value* if this is `true`.  Returned: required to be included if the identifier is wildcarded |
| **notAfter**  string | The requested value of the `notAfter` field in the certificate.  Date should be formatted as described in RFC3339.  Server is not required to return this.  Returned: when server returns this |
| **notBefore**  string | The requested value of the `notBefore` field in the certificate.  Date should be formatted as described in RFC3339.  Server is not required to return this.  Returned: when server returns this |
| **status**  string | The order’s status.  Returned: success  Can only return:   - `"pending"` - `"ready"` - `"processing"` - `"valid"` - `"invalid"` |

### Authors

- Felix Fontein (@felixfontein)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.crypto)
[Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-crypto)
