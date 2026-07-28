---
collection: ansible
version: "8"
title: "How to create self-signed certificates"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/crypto/docsite/guide_selfsigned.html
fetched_at: 2026-07-28T01:42:18+00:00
---
# How to create self-signed certificates

The [community.crypto collection](https://galaxy.ansible.com/ui/repo/published/community/crypto/) offers multiple modules that create private keys, certificate signing requests, and certificates. This guide shows how to create self-signed certificates.

For creating any kind of certificate, you always have to start with a private key. You can use the [community.crypto.openssl_privatekey module](../openssl_privatekey_module.md#ansible-collections-community-crypto-openssl-privatekey-module) to create a private key. If you only specify `path`, the default parameters will be used. This will result in a 4096 bit RSA private key:

```yaml+jinja
- name: Create private key (RSA, 4096 bits)
  community.crypto.openssl_privatekey:
    path: /path/to/certificate.key
```

You can specify `type` to select another key type, `size` to select a different key size (only available for RSA and DSA keys), or `passphrase` if you want to store the key password-protected:

```yaml+jinja
- name: Create private key (X25519) with password protection
  community.crypto.openssl_privatekey:
    path: /path/to/certificate.key
    type: X25519
    passphrase: changeme
```

To create a very simple self-signed certificate with no specific information, you can proceed directly with the [community.crypto.x509_certificate module](../x509_certificate_module.md#ansible-collections-community-crypto-x509-certificate-module):

```yaml+jinja
- name: Create simple self-signed certificate
  community.crypto.x509_certificate:
    path: /path/to/certificate.pem
    privatekey_path: /path/to/certificate.key
    provider: selfsigned
```

(If you used `passphrase` for the private key, you have to provide `privatekey_passphrase`.)

You can use `selfsigned_not_after` to define when the certificate expires (default: in roughly 10 years), and `selfsigned_not_before` to define from when the certificate is valid (default: now).

To define further properties of the certificate, like the subject, Subject Alternative Names (SANs), key usages, name constraints, etc., you need to first create a Certificate Signing Request (CSR) and provide it to the [community.crypto.x509_certificate module](../x509_certificate_module.md#ansible-collections-community-crypto-x509-certificate-module). If you do not need the CSR file, you can use the [community.crypto.openssl_csr_pipe module](../openssl_csr_pipe_module.md#ansible-collections-community-crypto-openssl-csr-pipe-module) as in the example below. (To store it to disk, use the [community.crypto.openssl_csr module](../openssl_csr_module.md#ansible-collections-community-crypto-openssl-csr-module) instead.)

```yaml+jinja
- name: Create certificate signing request (CSR) for self-signed certificate
  community.crypto.openssl_csr_pipe:
    privatekey_path: /path/to/certificate.key
    common_name: ansible.com
    organization_name: Ansible, Inc.
    subject_alt_name:
      - "DNS:ansible.com"
      - "DNS:www.ansible.com"
      - "DNS:docs.ansible.com"
  register: csr

- name: Create self-signed certificate from CSR
  community.crypto.x509_certificate:
    path: /path/to/certificate.pem
    csr_content: "{{ csr.csr }}"
    privatekey_path: /path/to/certificate.key
    provider: selfsigned
```
