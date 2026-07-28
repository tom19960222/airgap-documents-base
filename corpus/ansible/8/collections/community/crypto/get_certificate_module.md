---
collection: ansible
version: "8"
title: "community.crypto.get_certificate module – Get a certificate from a host:port"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/crypto/get_certificate_module.html
fetched_at: 2026-07-28T01:42:27+00:00
---
# community.crypto.get_certificate module – Get a certificate from a host:port

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
> see [Requirements](get_certificate_module.md#ansible-collections-community-crypto-get-certificate-module-requirements) for details.
>
> To use it in a playbook, specify: `community.crypto.get_certificate`.

- [Synopsis](get_certificate_module.md#synopsis)
- [Requirements](get_certificate_module.md#requirements)
- [Parameters](get_certificate_module.md#parameters)
- [Attributes](get_certificate_module.md#attributes)
- [Notes](get_certificate_module.md#notes)
- [Examples](get_certificate_module.md#examples)
- [Return Values](get_certificate_module.md#return-values)

## [Synopsis](get_certificate_module.md#id1)

- Makes a secure connection and returns information about the presented certificate
- The module uses the cryptography Python library.
- Support SNI ([Server Name Indication](https://en.wikipedia.org/wiki/Server_Name_Indication)) only with python >= 2.7.

## [Requirements](get_certificate_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7 when using `proxy_host`
- cryptography >= 1.6

## [Parameters](get_certificate_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **asn1_base64**  boolean  *added in community.crypto 2.12.0* | Whether to encode the ASN.1 values in the `extensions` return value with Base64 or not.  The documentation claimed for a long time that the values are Base64 encoded, but they never were. For compatibility this option is set to `false`.  The default value `false` is **deprecated** and will change to `true` in community.crypto 3.0.0.  **Choices:**   - `false` - `true` |
| **ca_cert**  path | A PEM file containing one or more root certificates; if present, the cert will be validated against these root certs.  Note that this only validates the certificate is signed by the chain; not that the cert is valid for the host presenting it. |
| **ciphers**  list / elements=string  *added in community.crypto 2.11.0* | SSL/TLS Ciphers to use for the request.  When a list is provided, all ciphers are joined in order with `:`.  See the [OpenSSL Cipher List Format](https://www.openssl.org/docs/manmaster/man1/openssl-ciphers.html#CIPHER-LIST-FORMAT) for more details.  The available ciphers is dependent on the Python and OpenSSL/LibreSSL versions. |
| **host**  string / required | The host to get the cert for (IP is fine) |
| **port**  integer / required | The port to connect to |
| **proxy_host**  string | Proxy host used when get a certificate. |
| **proxy_port**  integer | Proxy port used when get a certificate.  **Default:** `8080` |
| **select_crypto_backend**  string | Determines which crypto backend to use.  The default choice is `auto`, which tries to use `cryptography` if available.  If set to `cryptography`, will try to use the [cryptography](https://cryptography.io/) library.  **Choices:**   - `"auto"` ← (default) - `"cryptography"` |
| **server_name**  string  *added in community.crypto 1.4.0* | Server name used for SNI ([Server Name Indication](https://en.wikipedia.org/wiki/Server_Name_Indication)) when hostname is an IP or is different from server name. |
| **starttls**  string  *added in community.crypto 1.9.0* | Requests a secure connection for protocols which require clients to initiate encryption.  Only available for `mysql` currently.  **Choices:**   - `"mysql"` |
| **timeout**  integer | The timeout in seconds  **Default:** `10` |

## [Attributes](get_certificate_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](get_certificate_module.md#id5)

> **Note:**
>
> - When using ca_cert on OS X it has been reported that in some conditions the validate will always succeed.

## [Examples](get_certificate_module.md#id6)

```yaml+jinja
- name: Get the cert from an RDP port
  community.crypto.get_certificate:
    host: "1.2.3.4"
    port: 3389
  delegate_to: localhost
  run_once: true
  register: cert

- name: Get a cert from an https port
  community.crypto.get_certificate:
    host: "www.google.com"
    port: 443
  delegate_to: localhost
  run_once: true
  register: cert

- name: How many days until cert expires
  ansible.builtin.debug:
    msg: "cert expires in: {{ expire_days }} days."
  vars:
    expire_days: "{{ (( cert.not_after | to_datetime('%Y%m%d%H%M%SZ')) - (ansible_date_time.iso8601 | to_datetime('%Y-%m-%dT%H:%M:%SZ')) ).days }}"
```

## [Return Values](get_certificate_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cert**  string | The certificate retrieved from the port  **Returned:** success |
| **expired**  boolean | Boolean indicating if the cert is expired  **Returned:** success |
| **extensions**  list / elements=dictionary | Extensions applied to the cert  **Returned:** success |
| **asn1_data**  string | The ASN.1 content of the extension.  If `asn1_base64=true` this will be Base64 encoded, otherwise the raw binary value will be returned.  Please note that the raw binary value might not survive JSON serialization to the Ansible controller, and also might cause failures when displaying it. See <https://github.com/ansible/ansible/issues/80258> for more information.  **Note** that depending on the `cryptography` version used, it is not possible to extract the ASN.1 content of the extension, but only to provide the re-encoded content of the extension in case it was parsed by `cryptography`. This should usually result in exactly the same value, except if the original extension value was malformed.  **Returned:** success |
| **critical**  boolean | Whether the extension is critical.  **Returned:** success |
| **name**  string | The extension’s name.  **Returned:** success |
| **issuer**  dictionary | Information about the issuer of the cert  **Returned:** success |
| **not_after**  string | Expiration date of the cert  **Returned:** success |
| **not_before**  string | Issue date of the cert  **Returned:** success |
| **serial_number**  string | The serial number of the cert  **Returned:** success |
| **signature_algorithm**  string | The algorithm used to sign the cert  **Returned:** success |
| **subject**  dictionary | Information about the subject of the cert (OU, CN, etc)  **Returned:** success |
| **version**  string | The version number of the certificate  **Returned:** success |

### Authors

- John Westcott IV (@john-westcott-iv)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.crypto)
- [Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-crypto)
