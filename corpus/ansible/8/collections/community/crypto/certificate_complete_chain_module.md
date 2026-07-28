---
collection: ansible
version: "8"
title: "community.crypto.certificate_complete_chain module – Complete certificate chain given a set of untrusted and root certificates"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/crypto/certificate_complete_chain_module.html
fetched_at: 2026-07-28T01:42:24+00:00
---
# community.crypto.certificate_complete_chain module – Complete certificate chain given a set of untrusted and root certificates

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
> see [Requirements](certificate_complete_chain_module.md#ansible-collections-community-crypto-certificate-complete-chain-module-requirements) for details.
>
> To use it in a playbook, specify: `community.crypto.certificate_complete_chain`.

- [Synopsis](certificate_complete_chain_module.md#synopsis)
- [Requirements](certificate_complete_chain_module.md#requirements)
- [Parameters](certificate_complete_chain_module.md#parameters)
- [Attributes](certificate_complete_chain_module.md#attributes)
- [Examples](certificate_complete_chain_module.md#examples)
- [Return Values](certificate_complete_chain_module.md#return-values)

## [Synopsis](certificate_complete_chain_module.md#id1)

- This module completes a given chain of certificates in PEM format by finding intermediate certificates from a given set of certificates, until it finds a root certificate in another given set of certificates.
- This can for example be used to find the root certificate for a certificate chain returned by [community.crypto.acme_certificate](acme_certificate_module.md#ansible-collections-community-crypto-acme-certificate-module).
- Note that this module does *not* check for validity of the chains. It only checks that issuer and subject match, and that the signature is correct. It ignores validity dates and key usage completely. If you need to verify that a generated chain is valid, please use `openssl verify ...`.

## [Requirements](certificate_complete_chain_module.md#id2)

The below requirements are needed on the host that executes this module.

- cryptography >= 1.5

## [Parameters](certificate_complete_chain_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **input_chain**  string / required | A concatenated set of certificates in PEM format forming a chain.  The module will try to complete this chain. |
| **intermediate_certificates**  list / elements=path | A list of filenames or directories.  A filename is assumed to point to a file containing one or more certificates in PEM format. All certificates in this file will be added to the set of root certificates.  If a directory name is given, all files in the directory and its subdirectories will be scanned and tried to be parsed as concatenated certificates in PEM format.  Symbolic links will be followed.  **Default:** `[]` |
| **root_certificates**  list / elements=path / required | A list of filenames or directories.  A filename is assumed to point to a file containing one or more certificates in PEM format. All certificates in this file will be added to the set of root certificates.  If a directory name is given, all files in the directory and its subdirectories will be scanned and tried to be parsed as concatenated certificates in PEM format.  Symbolic links will be followed. |

## [Attributes](certificate_complete_chain_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](certificate_complete_chain_module.md#id5)

```yaml+jinja
# Given a leaf certificate for www.ansible.com and one or more intermediate
# certificates, finds the associated root certificate.
- name: Find root certificate
  community.crypto.certificate_complete_chain:
    input_chain: "{{ lookup('ansible.builtin.file', '/etc/ssl/csr/www.ansible.com-fullchain.pem') }}"
    root_certificates:
    - /etc/ca-certificates/
  register: www_ansible_com
- name: Write root certificate to disk
  ansible.builtin.copy:
    dest: /etc/ssl/csr/www.ansible.com-root.pem
    content: "{{ www_ansible_com.root }}"

# Given a leaf certificate for www.ansible.com, and a list of intermediate
# certificates, finds the associated root certificate.
- name: Find root certificate
  community.crypto.certificate_complete_chain:
    input_chain: "{{ lookup('ansible.builtin.file', '/etc/ssl/csr/www.ansible.com.pem') }}"
    intermediate_certificates:
    - /etc/ssl/csr/www.ansible.com-chain.pem
    root_certificates:
    - /etc/ca-certificates/
  register: www_ansible_com
- name: Write complete chain to disk
  ansible.builtin.copy:
    dest: /etc/ssl/csr/www.ansible.com-completechain.pem
    content: "{{ ''.join(www_ansible_com.complete_chain) }}"
- name: Write root chain (intermediates and root) to disk
  ansible.builtin.copy:
    dest: /etc/ssl/csr/www.ansible.com-rootchain.pem
    content: "{{ ''.join(www_ansible_com.chain) }}"
```

## [Return Values](certificate_complete_chain_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **chain**  list / elements=string | The chain added to the given input chain. Includes the root certificate.  Returned as a list of PEM certificates.  **Returned:** success |
| **complete_chain**  list / elements=string | The completed chain, including leaf, all intermediates, and root.  Returned as a list of PEM certificates.  **Returned:** success |
| **root**  string | The root certificate in PEM format.  **Returned:** success |

### Authors

- Felix Fontein (@felixfontein)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.crypto)
- [Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-crypto)
