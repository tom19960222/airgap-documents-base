---
collection: ansible
version: "8"
title: "Community.Crypto"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/crypto/index.html
fetched_at: 2026-07-28T01:02:08+00:00
---
# Community.Crypto

Collection version 2.16.1

- [Description](index.md#description)
- [Communication](index.md#communication)
- [Scenario Guides](index.md#scenario-guides)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

**Author:**

- Ansible (github.com/ansible)

**Supported ansible-core versions:**

- 2.9.10 or newer

- [Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.crypto)
- [Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)

## [Communication](index.md#id2)

- Matrix room `#users:ansible.im`: [General usage and support questions](https://matrix.to/#/#users:ansible.im).
- IRC channel `#ansible` (Libera network):
  [General usage and support questions](https://web.libera.chat/?channel=#ansible).
- Mailing list: [Ansible Project List](https://groups.google.com/g/ansible-project).
  ([Subscribe](mailto:ansible-project+subscribe%40googlegroups.com?subject=subscribe))

## [Scenario Guides](index.md#id3)

- [How to create self-signed certificates](docsite/guide_selfsigned.md)
- [How to create a small CA](docsite/guide_ownca.md)

## [Plugin Index](index.md#id4)

These are the plugins in the community.crypto collection:

### Modules

- [acme_account module](acme_account_module.md#ansible-collections-community-crypto-acme-account-module) – Create, modify or delete ACME accounts
- [acme_account_info module](acme_account_info_module.md#ansible-collections-community-crypto-acme-account-info-module) – Retrieves information on ACME accounts
- [acme_certificate module](acme_certificate_module.md#ansible-collections-community-crypto-acme-certificate-module) – Create SSL/TLS certificates with the ACME protocol
- [acme_certificate_revoke module](acme_certificate_revoke_module.md#ansible-collections-community-crypto-acme-certificate-revoke-module) – Revoke certificates with the ACME protocol
- [acme_challenge_cert_helper module](acme_challenge_cert_helper_module.md#ansible-collections-community-crypto-acme-challenge-cert-helper-module) – Prepare certificates required for ACME challenges such as `tls-alpn-01`
- [acme_inspect module](acme_inspect_module.md#ansible-collections-community-crypto-acme-inspect-module) – Send direct requests to an ACME server
- [certificate_complete_chain module](certificate_complete_chain_module.md#ansible-collections-community-crypto-certificate-complete-chain-module) – Complete certificate chain given a set of untrusted and root certificates
- [crypto_info module](crypto_info_module.md#ansible-collections-community-crypto-crypto-info-module) – Retrieve cryptographic capabilities
- [ecs_certificate module](ecs_certificate_module.md#ansible-collections-community-crypto-ecs-certificate-module) – Request SSL/TLS certificates with the Entrust Certificate Services (ECS) API
- [ecs_domain module](ecs_domain_module.md#ansible-collections-community-crypto-ecs-domain-module) – Request validation of a domain with the Entrust Certificate Services (ECS) API
- [get_certificate module](get_certificate_module.md#ansible-collections-community-crypto-get-certificate-module) – Get a certificate from a host:port
- [luks_device module](luks_device_module.md#ansible-collections-community-crypto-luks-device-module) – Manage encrypted (LUKS) devices
- [openssh_cert module](openssh_cert_module.md#ansible-collections-community-crypto-openssh-cert-module) – Generate OpenSSH host or user certificates.
- [openssh_keypair module](openssh_keypair_module.md#ansible-collections-community-crypto-openssh-keypair-module) – Generate OpenSSH private and public keys
- [openssl_csr module](openssl_csr_module.md#ansible-collections-community-crypto-openssl-csr-module) – Generate OpenSSL Certificate Signing Request (CSR)
- [openssl_csr_info module](openssl_csr_info_module.md#ansible-collections-community-crypto-openssl-csr-info-module) – Provide information of OpenSSL Certificate Signing Requests (CSR)
- [openssl_csr_pipe module](openssl_csr_pipe_module.md#ansible-collections-community-crypto-openssl-csr-pipe-module) – Generate OpenSSL Certificate Signing Request (CSR)
- [openssl_dhparam module](openssl_dhparam_module.md#ansible-collections-community-crypto-openssl-dhparam-module) – Generate OpenSSL Diffie-Hellman Parameters
- [openssl_pkcs12 module](openssl_pkcs12_module.md#ansible-collections-community-crypto-openssl-pkcs12-module) – Generate OpenSSL PKCS#12 archive
- [openssl_privatekey module](openssl_privatekey_module.md#ansible-collections-community-crypto-openssl-privatekey-module) – Generate OpenSSL private keys
- [openssl_privatekey_convert module](openssl_privatekey_convert_module.md#ansible-collections-community-crypto-openssl-privatekey-convert-module) – Convert OpenSSL private keys
- [openssl_privatekey_info module](openssl_privatekey_info_module.md#ansible-collections-community-crypto-openssl-privatekey-info-module) – Provide information for OpenSSL private keys
- [openssl_privatekey_pipe module](openssl_privatekey_pipe_module.md#ansible-collections-community-crypto-openssl-privatekey-pipe-module) – Generate OpenSSL private keys without disk access
- [openssl_publickey module](openssl_publickey_module.md#ansible-collections-community-crypto-openssl-publickey-module) – Generate an OpenSSL public key from its private key.
- [openssl_publickey_info module](openssl_publickey_info_module.md#ansible-collections-community-crypto-openssl-publickey-info-module) – Provide information for OpenSSL public keys
- [openssl_signature module](openssl_signature_module.md#ansible-collections-community-crypto-openssl-signature-module) – Sign data with openssl
- [openssl_signature_info module](openssl_signature_info_module.md#ansible-collections-community-crypto-openssl-signature-info-module) – Verify signatures with openssl
- [x509_certificate module](x509_certificate_module.md#ansible-collections-community-crypto-x509-certificate-module) – Generate and/or check OpenSSL certificates
- [x509_certificate_info module](x509_certificate_info_module.md#ansible-collections-community-crypto-x509-certificate-info-module) – Provide information of OpenSSL X.509 certificates
- [x509_certificate_pipe module](x509_certificate_pipe_module.md#ansible-collections-community-crypto-x509-certificate-pipe-module) – Generate and/or check OpenSSL certificates
- [x509_crl module](x509_crl_module.md#ansible-collections-community-crypto-x509-crl-module) – Generate Certificate Revocation Lists (CRLs)
- [x509_crl_info module](x509_crl_info_module.md#ansible-collections-community-crypto-x509-crl-info-module) – Retrieve information on Certificate Revocation Lists (CRLs)

### Filter Plugins

- [gpg_fingerprint filter](gpg_fingerprint_filter.md#ansible-collections-community-crypto-gpg-fingerprint-filter) – Retrieve a GPG fingerprint from a GPG public or private key
- [openssl_csr_info filter](openssl_csr_info_filter.md#ansible-collections-community-crypto-openssl-csr-info-filter) – Retrieve information from OpenSSL Certificate Signing Requests (CSR)
- [openssl_privatekey_info filter](openssl_privatekey_info_filter.md#ansible-collections-community-crypto-openssl-privatekey-info-filter) – Retrieve information from OpenSSL private keys
- [openssl_publickey_info filter](openssl_publickey_info_filter.md#ansible-collections-community-crypto-openssl-publickey-info-filter) – Retrieve information from OpenSSL public keys in PEM format
- [split_pem filter](split_pem_filter.md#ansible-collections-community-crypto-split-pem-filter) – Split PEM file contents into multiple objects
- [x509_certificate_info filter](x509_certificate_info_filter.md#ansible-collections-community-crypto-x509-certificate-info-filter) – Retrieve information from X.509 certificates in PEM format
- [x509_crl_info filter](x509_crl_info_filter.md#ansible-collections-community-crypto-x509-crl-info-filter) – Retrieve information from X.509 CRLs in PEM format

### Lookup Plugins

- [gpg_fingerprint lookup](gpg_fingerprint_lookup.md#ansible-collections-community-crypto-gpg-fingerprint-lookup) – Retrieve a GPG fingerprint from a GPG public or private key file

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
