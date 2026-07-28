---
collection: ansible
version: "8"
title: "community.crypto.acme_inspect module – Send direct requests to an ACME server"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/crypto/acme_inspect_module.html
fetched_at: 2026-07-28T01:42:23+00:00
---
# community.crypto.acme_inspect module – Send direct requests to an ACME server

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
> see [Requirements](acme_inspect_module.md#ansible-collections-community-crypto-acme-inspect-module-requirements) for details.
>
> To use it in a playbook, specify: `community.crypto.acme_inspect`.

- [Synopsis](acme_inspect_module.md#synopsis)
- [Requirements](acme_inspect_module.md#requirements)
- [Parameters](acme_inspect_module.md#parameters)
- [Attributes](acme_inspect_module.md#attributes)
- [Notes](acme_inspect_module.md#notes)
- [See Also](acme_inspect_module.md#see-also)
- [Examples](acme_inspect_module.md#examples)
- [Return Values](acme_inspect_module.md#return-values)

## [Synopsis](acme_inspect_module.md#id1)

- Allows to send direct requests to an ACME server with the [ACME protocol](https://tools.ietf.org/html/rfc8555), which is supported by CAs such as [Let’s Encrypt](https://letsencrypt.org/).
- This module can be used to debug failed certificate request attempts, for example when [community.crypto.acme_certificate](acme_certificate_module.md#ansible-collections-community-crypto-acme-certificate-module) fails or encounters a problem which you wish to investigate.
- The module can also be used to directly access features of an ACME servers which are not yet supported by the Ansible ACME modules.

## [Requirements](acme_inspect_module.md#id2)

The below requirements are needed on the host that executes this module.

- either openssl or [cryptography](https://cryptography.io/) >= 1.5
- ipaddress

## [Parameters](acme_inspect_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account_key_content**  string | Content of the ACME account RSA or Elliptic Curve key.  Mutually exclusive with `account_key_src`.  Required if `account_key_src` is not used.  **Warning:** the content will be written into a temporary file, which will be deleted by Ansible when the module completes. Since this is an important private key — it can be used to change the account key, or to revoke your certificates without knowing their private keys —, this might not be acceptable.  In case `cryptography` is used, the content is not written into a temporary file. It can still happen that it is written to disk by Ansible in the process of moving the module with its argument to the node where it is executed. |
| **account_key_passphrase**  string  *added in community.crypto 1.6.0* | Phassphrase to use to decode the account key.  **Note:** this is not supported by the `openssl` backend, only by the `cryptography` backend. |
| **account_key_src**  aliases: account_key  path | Path to a file containing the ACME account RSA or Elliptic Curve key.  Private keys can be created with the [community.crypto.openssl_privatekey](openssl_privatekey_module.md#ansible-collections-community-crypto-openssl-privatekey-module) or [community.crypto.openssl_privatekey_pipe](openssl_privatekey_pipe_module.md#ansible-collections-community-crypto-openssl-privatekey-pipe-module) modules. If the requisite (cryptography) is not available, keys can also be created directly with the `openssl` command line tool: RSA keys can be created with `openssl genrsa ...`. Elliptic curve keys can be created with `openssl ecparam -genkey ...`. Any other tool creating private keys in PEM format can be used as well.  Mutually exclusive with `account_key_content`.  Required if `account_key_content` is not used. |
| **account_uri**  string | If specified, assumes that the account URI is as given. If the account key does not match this account, or an account with this URI does not exist, the module fails. |
| **acme_directory**  string / required | The ACME directory to use. This is the entry point URL to access the ACME CA server API.  For safety reasons the default is set to the Let’s Encrypt staging server (for the ACME v1 protocol). This will create technically correct, but untrusted certificates.  For Let’s Encrypt, all staging endpoints can be found here: <https://letsencrypt.org/docs/staging-environment/>. For Buypass, all endpoints can be found here: <https://community.buypass.com/t/63d4ay/buypass-go-ssl-endpoints>  For **Let’s Encrypt**, the production directory URL for ACME v2 is <https://acme-v02.api.letsencrypt.org/directory>.  For **Buypass**, the production directory URL for ACME v2 and v1 is <https://api.buypass.com/acme/directory>.  For **ZeroSSL**, the production directory URL for ACME v2 is <https://acme.zerossl.com/v2/DV90>.  For **Sectigo**, the production directory URL for ACME v2 is <https://acme-qa.secure.trust-provider.com/v2/DV>.  The notes for this module contain a list of ACME services this module has been tested against. |
| **acme_version**  integer / required | The ACME version of the endpoint.  Must be `1` for the classic Let’s Encrypt and Buypass ACME endpoints, or `2` for standardized ACME v2 endpoints.  The value `1` is deprecated since community.crypto 2.0.0 and will be removed from community.crypto 3.0.0.  **Choices:**   - `1` - `2` |
| **content**  string | An encoded JSON object which will be sent as the content if `method` is `post`.  Required when `method` is `post`, and not allowed otherwise. |
| **fail_on_acme_error**  boolean | If `method` is `post` or `get`, make the module fail in case an ACME error is returned.  **Choices:**   - `false` - `true` ← (default) |
| **method**  string | The method to use to access the given URL on the ACME server.  The value `post` executes an authenticated POST request. The content must be specified in the `content` option.  The value `get` executes an authenticated POST-as-GET request for ACME v2, and a regular GET request for ACME v1.  The value `directory-only` only retrieves the directory, without doing a request.  **Choices:**   - `"get"` ← (default) - `"post"` - `"directory-only"` |
| **request_timeout**  integer  *added in community.crypto 2.3.0* | The time Ansible should wait for a response from the ACME API.  This timeout is applied to all HTTP(S) requests (HEAD, GET, POST).  **Default:** `10` |
| **select_crypto_backend**  string | Determines which crypto backend to use.  The default choice is `auto`, which tries to use `cryptography` if available, and falls back to `openssl`.  If set to `openssl`, will try to use the `openssl` binary.  If set to `cryptography`, will try to use the [cryptography](https://cryptography.io/) library.  **Choices:**   - `"auto"` ← (default) - `"cryptography"` - `"openssl"` |
| **url**  string | The URL to send the request to.  Must be specified if `method` is not `directory-only`. |
| **validate_certs**  boolean | Whether calls to the ACME directory will validate TLS certificates.  **Warning:** Should **only ever** be set to `false` for testing purposes, for example when testing against a local Pebble server.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](acme_inspect_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | **Action groups:** **community.crypto.acme**, **acme** | Use `group/acme` or `group/community.crypto.acme` in `module_defaults` to set defaults for this module. |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](acme_inspect_module.md#id5)

> **Note:**
>
> - The `account_uri` option must be specified for properly authenticated ACME v2 requests (except a `new-account` request).
> - Using the `ansible` tool, [community.crypto.acme_inspect](acme_inspect_module.md#ansible-collections-community-crypto-acme-inspect-module) can be used to directly execute ACME requests without the need of writing a playbook. For example, the following command retrieves the ACME account with ID 1 from Let’s Encrypt (assuming `/path/to/key` is the correct private account key): `ansible localhost -m acme_inspect -a "account_key_src=/path/to/key acme_directory=https://acme-v02.api.letsencrypt.org/directory acme_version=2 account_uri=https://acme-v02.api.letsencrypt.org/acme/acct/1 method=get url=https://acme-v02.api.letsencrypt.org/acme/acct/1"`
> - If a new enough version of the `cryptography` library is available (see Requirements for details), it will be used instead of the `openssl` binary. This can be explicitly disabled or enabled with the `select_crypto_backend` option. Note that using the `openssl` binary will be slower and less secure, as private key contents always have to be stored on disk (see `account_key_content`).
> - Although the defaults are chosen so that the module can be used with the [Let’s Encrypt](https://letsencrypt.org/) CA, the module can in principle be used with any CA providing an ACME endpoint, such as [Buypass Go SSL](https://www.buypass.com/ssl/products/acme).
> - So far, the ACME modules have only been tested by the developers against Let’s Encrypt (staging and production), Buypass (staging and production), ZeroSSL (production), and [Pebble testing server](https://github.com/letsencrypt/Pebble). We have got community feedback that they also work with Sectigo ACME Service for InCommon. If you experience problems with another ACME server, please [create an issue](https://github.com/ansible-collections/community.crypto/issues/new/choose) to help us supporting it. Feedback that an ACME server not mentioned does work is also appreciated.

## [See Also](acme_inspect_module.md#id6)

> **See also:**
>
> [Automatic Certificate Management Environment (ACME)](https://tools.ietf.org/html/rfc8555)
> :   The specification of the ACME protocol (RFC 8555).
>
> [ACME TLS ALPN Challenge Extension](https://www.rfc-editor.org/rfc/rfc8737.html)
> :   The specification of the `tls-alpn-01` challenge (RFC 8737).

## [Examples](acme_inspect_module.md#id7)

```yaml+jinja
- name: Get directory
  community.crypto.acme_inspect:
    acme_directory: https://acme-staging-v02.api.letsencrypt.org/directory
    acme_version: 2
    method: directory-only
  register: directory

- name: Create an account
  community.crypto.acme_inspect:
    acme_directory: https://acme-staging-v02.api.letsencrypt.org/directory
    acme_version: 2
    account_key_src: /etc/pki/cert/private/account.key
    url: "{{ directory.newAccount}}"
    method: post
    content: '{"termsOfServiceAgreed":true}'
  register: account_creation
  # account_creation.headers.location contains the account URI
  # if creation was successful

- name: Get account information
  community.crypto.acme_inspect:
    acme_directory: https://acme-staging-v02.api.letsencrypt.org/directory
    acme_version: 2
    account_key_src: /etc/pki/cert/private/account.key
    account_uri: "{{ account_creation.headers.location }}"
    url: "{{ account_creation.headers.location }}"
    method: get

- name: Update account contacts
  community.crypto.acme_inspect:
    acme_directory: https://acme-staging-v02.api.letsencrypt.org/directory
    acme_version: 2
    account_key_src: /etc/pki/cert/private/account.key
    account_uri: "{{ account_creation.headers.location }}"
    url: "{{ account_creation.headers.location }}"
    method: post
    content: '{{ account_info | to_json }}'
  vars:
    account_info:
      # For valid values, see
      # https://tools.ietf.org/html/rfc8555#section-7.3
      contact:
      - mailto:me@example.com

- name: Create certificate order
  community.crypto.acme_certificate:
    acme_directory: https://acme-staging-v02.api.letsencrypt.org/directory
    acme_version: 2
    account_key_src: /etc/pki/cert/private/account.key
    account_uri: "{{ account_creation.headers.location }}"
    csr: /etc/pki/cert/csr/sample.com.csr
    fullchain_dest: /etc/httpd/ssl/sample.com-fullchain.crt
    challenge: http-01
  register: certificate_request

# Assume something went wrong. certificate_request.order_uri contains
# the order URI.

- name: Get order information
  community.crypto.acme_inspect:
    acme_directory: https://acme-staging-v02.api.letsencrypt.org/directory
    acme_version: 2
    account_key_src: /etc/pki/cert/private/account.key
    account_uri: "{{ account_creation.headers.location }}"
    url: "{{ certificate_request.order_uri }}"
    method: get
  register: order

- name: Get first authz for order
  community.crypto.acme_inspect:
    acme_directory: https://acme-staging-v02.api.letsencrypt.org/directory
    acme_version: 2
    account_key_src: /etc/pki/cert/private/account.key
    account_uri: "{{ account_creation.headers.location }}"
    url: "{{ order.output_json.authorizations[0] }}"
    method: get
  register: authz

- name: Get HTTP-01 challenge for authz
  community.crypto.acme_inspect:
    acme_directory: https://acme-staging-v02.api.letsencrypt.org/directory
    acme_version: 2
    account_key_src: /etc/pki/cert/private/account.key
    account_uri: "{{ account_creation.headers.location }}"
    url: "{{ authz.output_json.challenges | selectattr('type', 'equalto', 'http-01') }}"
    method: get
  register: http01challenge

- name: Activate HTTP-01 challenge manually
  community.crypto.acme_inspect:
    acme_directory: https://acme-staging-v02.api.letsencrypt.org/directory
    acme_version: 2
    account_key_src: /etc/pki/cert/private/account.key
    account_uri: "{{ account_creation.headers.location }}"
    url: "{{ http01challenge.url }}"
    method: post
    content: '{}'
```

## [Return Values](acme_inspect_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **directory**  dictionary | The ACME directory’s content  **Returned:** always  **Sample:** `{"a85k3x9f91A4": "https://community.letsencrypt.org/t/adding-random-entries-to-the-directory/33417", "keyChange": "https://acme-v02.api.letsencrypt.org/acme/key-change", "meta": {"caaIdentities": ["letsencrypt.org"], "termsOfService": "https://letsencrypt.org/documents/LE-SA-v1.2-November-15-2017.pdf", "website": "https://letsencrypt.org"}, "newAccount": "https://acme-v02.api.letsencrypt.org/acme/new-acct", "newNonce": "https://acme-v02.api.letsencrypt.org/acme/new-nonce", "newOrder": "https://acme-v02.api.letsencrypt.org/acme/new-order", "revokeCert": "https://acme-v02.api.letsencrypt.org/acme/revoke-cert"}` |
| **headers**  dictionary | The request’s HTTP headers (with lowercase keys)  **Returned:** always  **Sample:** `{"boulder-requester": "12345", "cache-control": "max-age=0, no-cache, no-store", "connection": "close", "content-length": "904", "content-type": "application/json", "cookies": {}, "cookies_string": "", "date": "Wed, 07 Nov 2018 12:34:56 GMT", "expires": "Wed, 07 Nov 2018 12:44:56 GMT", "link": "<https://letsencrypt.org/documents/LE-SA-v1.2-November-15-2017.pdf>;rel=\"terms-of-service\"", "msg": "OK (904 bytes)", "pragma": "no-cache", "replay-nonce": "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGH", "server": "nginx", "status": 200, "strict-transport-security": "max-age=604800", "url": "https://acme-v02.api.letsencrypt.org/acme/acct/46161", "x-frame-options": "DENY"}` |
| **output_json**  dictionary | The output parsed as JSON  **Returned:** if output can be parsed as JSON  **Sample:** `[{"id": 12345}, {"key": [{"kty": "RSA"}, "..."]}]` |
| **output_text**  string | The raw text output  **Returned:** always  **Sample:** `"{\n  \"id\": 12345,\n  \"key\": {\n    \"kty\": \"RSA\",\n ..."` |

### Authors

- Felix Fontein (@felixfontein)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.crypto)
- [Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-crypto)
