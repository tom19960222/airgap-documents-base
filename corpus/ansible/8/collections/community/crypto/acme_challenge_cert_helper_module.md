---
collection: ansible
version: "8"
title: "community.crypto.acme_challenge_cert_helper module – Prepare certificates required for ACME challenges such as tls-alpn-01"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/crypto/acme_challenge_cert_helper_module.html
fetched_at: 2026-07-28T01:42:22+00:00
---
# community.crypto.acme_challenge_cert_helper module – Prepare certificates required for ACME challenges such as `tls-alpn-01`

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
> see [Requirements](acme_challenge_cert_helper_module.md#ansible-collections-community-crypto-acme-challenge-cert-helper-module-requirements) for details.
>
> To use it in a playbook, specify: `community.crypto.acme_challenge_cert_helper`.

- [Synopsis](acme_challenge_cert_helper_module.md#synopsis)
- [Requirements](acme_challenge_cert_helper_module.md#requirements)
- [Parameters](acme_challenge_cert_helper_module.md#parameters)
- [Attributes](acme_challenge_cert_helper_module.md#attributes)
- [See Also](acme_challenge_cert_helper_module.md#see-also)
- [Examples](acme_challenge_cert_helper_module.md#examples)
- [Return Values](acme_challenge_cert_helper_module.md#return-values)

## [Synopsis](acme_challenge_cert_helper_module.md#id1)

- Prepares certificates for ACME challenges such as `tls-alpn-01`.
- The raw data is provided by the [community.crypto.acme_certificate](acme_certificate_module.md#ansible-collections-community-crypto-acme-certificate-module) module, and needs to be converted to a certificate to be used for challenge validation. This module provides a simple way to generate the required certificates.

## [Requirements](acme_challenge_cert_helper_module.md#id2)

The below requirements are needed on the host that executes this module.

- cryptography >= 1.3

## [Parameters](acme_challenge_cert_helper_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **challenge**  string / required | The challenge type.  **Choices:**   - `"tls-alpn-01"` |
| **challenge_data**  dictionary / required | The `challenge_data` entry provided by [community.crypto.acme_certificate](acme_certificate_module.md#ansible-collections-community-crypto-acme-certificate-module) for the challenge. |
| **private_key_content**  string | Content of the private key to use for this challenge certificate.  Mutually exclusive with `private_key_src`. |
| **private_key_passphrase**  string  *added in community.crypto 1.6.0* | Phassphrase to use to decode the private key. |
| **private_key_src**  path | Path to a file containing the private key file to use for this challenge certificate.  Mutually exclusive with `private_key_content`. |

## [Attributes](acme_challenge_cert_helper_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [See Also](acme_challenge_cert_helper_module.md#id5)

> **See also:**
>
> [Automatic Certificate Management Environment (ACME)](https://tools.ietf.org/html/rfc8555)
> :   The specification of the ACME protocol (RFC 8555).
>
> [ACME TLS ALPN Challenge Extension](https://www.rfc-editor.org/rfc/rfc8737.html)
> :   The specification of the `tls-alpn-01` challenge (RFC 8737).

## [Examples](acme_challenge_cert_helper_module.md#id6)

```yaml+jinja
- name: Create challenges for a given CRT for sample.com
  community.crypto.acme_certificate:
    account_key_src: /etc/pki/cert/private/account.key
    challenge: tls-alpn-01
    csr: /etc/pki/cert/csr/sample.com.csr
    dest: /etc/httpd/ssl/sample.com.crt
  register: sample_com_challenge

- name: Create certificates for challenges
  community.crypto.acme_challenge_cert_helper:
    challenge: tls-alpn-01
    challenge_data: "{{ item.value['tls-alpn-01'] }}"
    private_key_src: /etc/pki/cert/key/sample.com.key
  loop: "{{ sample_com_challenge.challenge_data | dictsort }}"
  register: sample_com_challenge_certs

- name: Install challenge certificates
  # We need to set up HTTPS such that for the domain,
  # regular_certificate is delivered for regular connections,
  # except if ALPN selects the "acme-tls/1"; then, the
  # challenge_certificate must be delivered.
  # This can for example be achieved with very new versions
  # of NGINX; search for ssl_preread and
  # ssl_preread_alpn_protocols for information on how to
  # route by ALPN protocol.
  ...:
    domain: "{{ item.domain }}"
    challenge_certificate: "{{ item.challenge_certificate }}"
    regular_certificate: "{{ item.regular_certificate }}"
    private_key: /etc/pki/cert/key/sample.com.key
  loop: "{{ sample_com_challenge_certs.results }}"

- name: Create certificate for a given CSR for sample.com
  community.crypto.acme_certificate:
    account_key_src: /etc/pki/cert/private/account.key
    challenge: tls-alpn-01
    csr: /etc/pki/cert/csr/sample.com.csr
    dest: /etc/httpd/ssl/sample.com.crt
    data: "{{ sample_com_challenge }}"
```

## [Return Values](acme_challenge_cert_helper_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **challenge_certificate**  string | The challenge certificate in PEM format.  **Returned:** always |
| **domain**  string | The domain the challenge is for. The certificate should be provided if this is specified in the request’s the `Host` header.  **Returned:** always |
| **identifier**  string | The identifier for the actual resource. Will be a domain name if `identifier_type=dns`, or an IP address if `identifier_type=ip`.  **Returned:** always |
| **identifier_type**  string | The identifier type for the actual resource identifier.  **Returned:** always  **Can only return:**   - `"dns"` - `"ip"` |
| **regular_certificate**  string | A self-signed certificate for the challenge domain.  If no existing certificate exists, can be used to set-up https in the first place if that is needed for providing the challenge.  **Returned:** always |

### Authors

- Felix Fontein (@felixfontein)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.crypto)
- [Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-crypto)
