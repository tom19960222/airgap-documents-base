---
collection: ansible
version: "8"
title: "community.crypto.crypto_info module – Retrieve cryptographic capabilities"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/crypto/crypto_info_module.html
fetched_at: 2026-07-28T01:42:25+00:00
---
# community.crypto.crypto_info module – Retrieve cryptographic capabilities

> **Note:**
>
> This module is part of the [community.crypto collection](https://galaxy.ansible.com/ui/repo/published/community/crypto/) (version 2.16.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.crypto`.
>
> To use it in a playbook, specify: `community.crypto.crypto_info`.

New in community.crypto 2.1.0

- [Synopsis](crypto_info_module.md#synopsis)
- [Attributes](crypto_info_module.md#attributes)
- [Examples](crypto_info_module.md#examples)
- [Return Values](crypto_info_module.md#return-values)

## [Synopsis](crypto_info_module.md#id1)

- Retrieve information on cryptographic capabilities.
- The current version retrieves information on the [Python cryptography library](https://cryptography.io/) available to Ansible modules, and on the OpenSSL binary `openssl` found in the path.

## [Attributes](crypto_info_module.md#id2)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](crypto_info_module.md#id3)

```yaml+jinja
- name: Retrieve information
  community.crypto.crypto_info:
    account_key_src: /etc/pki/cert/private/account.key
  register: crypto_information

- name: Show retrieved information
  ansible.builtin.debug:
    var: crypto_information
```

## [Return Values](crypto_info_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **openssl**  dictionary | Information on the installed OpenSSL binary.  **Returned:** when `openssl_present=true` |
| **path**  string | Path of the OpenSSL binary.  **Returned:** success  **Sample:** `"/usr/bin/openssl"` |
| **version**  string | The OpenSSL version.  **Returned:** success  **Sample:** `"1.1.1m"` |
| **version_output**  string | The complete output of `openssl version`.  **Returned:** success  **Sample:** `"OpenSSL 1.1.1m  14 Dec 2021\\n"` |
| **openssl_present**  boolean | Whether the OpenSSL binary `openssl` is installed and can be found in the PATH.  **Returned:** always  **Sample:** `true` |
| **python_cryptography_capabilities**  dictionary | Information on the installed [Python cryptography library](https://cryptography.io/).  **Returned:** when `python_cryptography_installed=true` |
| **curves**  list / elements=string | List of all supported elliptic curves.  Theoretically this should be non-empty for version 0.5 and higher, depending on the libssl version used.  **Returned:** success |
| **has_dsa**  boolean | Whether DSA keys are supported.  Theoretically this should be the case for version 0.5 and higher.  **Returned:** success |
| **has_dsa_sign**  boolean | Whether signing with DSA keys is supported.  Theoretically this should be the case for version 1.5 and higher.  **Returned:** success |
| **has_ec**  boolean | Whether elliptic curves are supported.  Theoretically this should be the case for version 0.5 and higher, depending on the libssl version used.  **Returned:** success |
| **has_ec_sign**  boolean | Whether signing with elliptic curves is supported.  Theoretically this should be the case for version 1.5 and higher, depending on the libssl version used.  **Returned:** success |
| **has_ed25519**  boolean | Whether Ed25519 keys are supported.  Theoretically this should be the case for version 2.6 and higher, depending on the libssl version used.  **Returned:** success |
| **has_ed25519_sign**  boolean | Whether signing with Ed25519 keys is supported.  Theoretically this should be the case for version 2.6 and higher, depending on the libssl version used.  **Returned:** success |
| **has_ed448**  boolean | Whether Ed448 keys are supported.  Theoretically this should be the case for version 2.6 and higher, depending on the libssl version used.  **Returned:** success |
| **has_ed448_sign**  boolean | Whether signing with Ed448 keys is supported.  Theoretically this should be the case for version 2.6 and higher, depending on the libssl version used.  **Returned:** success |
| **has_rsa**  boolean | Whether RSA keys are supported.  Theoretically this should be the case for version 0.5 and higher.  **Returned:** success |
| **has_rsa_sign**  boolean | Whether signing with RSA keys is supported.  Theoretically this should be the case for version 1.4 and higher.  **Returned:** success |
| **has_x25519**  boolean | Whether X25519 keys are supported.  Theoretically this should be the case for version 2.0 and higher, depending on the libssl version used.  **Returned:** success |
| **has_x25519_serialization**  boolean | Whether serialization of X25519 keys is supported.  Theoretically this should be the case for version 2.5 and higher, depending on the libssl version used.  **Returned:** success |
| **has_x448**  boolean | Whether X448 keys are supported.  Theoretically this should be the case for version 2.5 and higher, depending on the libssl version used.  **Returned:** success |
| **version**  string | The library version.  **Returned:** success |
| **python_cryptography_import_error**  string | Import error when trying to import the [Python cryptography library](https://cryptography.io/).  **Returned:** when `python_cryptography_installed=false` |
| **python_cryptography_installed**  boolean | Whether the [Python cryptography library](https://cryptography.io/) is installed.  **Returned:** always  **Sample:** `true` |

### Authors

- Felix Fontein (@felixfontein)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.crypto)
- [Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-crypto)
