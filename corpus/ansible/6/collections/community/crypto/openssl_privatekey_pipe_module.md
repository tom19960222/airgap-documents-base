---
collection: ansible
version: "6"
title: "community.crypto.openssl_privatekey_pipe module – Generate OpenSSL private keys without disk access"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/crypto/openssl_privatekey_pipe_module.html
fetched_at: 2026-07-27T17:06:26+00:00
---
# community.crypto.openssl_privatekey_pipe module – Generate OpenSSL private keys without disk access

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
> see [Requirements](openssl_privatekey_pipe_module.md#ansible-collections-community-crypto-openssl-privatekey-pipe-module-requirements) for details.
>
> To use it in a playbook, specify: `community.crypto.openssl_privatekey_pipe`.

New in community.crypto 1.3.0

- [Synopsis](openssl_privatekey_pipe_module.md#synopsis)
- [Requirements](openssl_privatekey_pipe_module.md#requirements)
- [Parameters](openssl_privatekey_pipe_module.md#parameters)
- [Attributes](openssl_privatekey_pipe_module.md#attributes)
- [See Also](openssl_privatekey_pipe_module.md#see-also)
- [Examples](openssl_privatekey_pipe_module.md#examples)
- [Return Values](openssl_privatekey_pipe_module.md#return-values)

## [Synopsis](openssl_privatekey_pipe_module.md#id1)

- Keys are generated in PEM format.
- Make sure to not write the result of this module into logs or to the console, as it contains private key data! Use the *no_log* task option to be sure.
- Note that this module is implemented as an [action plugin](https://docs.ansible.com/ansible/latest/plugins/action.html) and will always be executed on the controller.
- One can generate [RSA](https://en.wikipedia.org/wiki/RSA_%28cryptosystem%29), [DSA](https://en.wikipedia.org/wiki/Digital_Signature_Algorithm), [ECC](https://en.wikipedia.org/wiki/Elliptic-curve_cryptography) or [EdDSA](https://en.wikipedia.org/wiki/EdDSA) private keys.
- Please note that the module regenerates private keys if they do not match the module’s options. In particular, if you provide another passphrase (or specify none), change the keysize, etc., the private key will be regenerated. If you are concerned that this could **overwrite your private key**, consider using the *backup* option.
- This allows to read and write keys to vaults without having to write intermediate versions to disk.
- This module allows one to (re)generate OpenSSL private keys without disk access.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](openssl_privatekey_pipe_module.md#id2)

The below requirements are needed on the host that executes this module.

- cryptography >= 1.2.3 (older versions might work as well)

## [Parameters](openssl_privatekey_pipe_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cipher**  string | The cipher to encrypt the private key. Must be `auto`. |
| **content**  string | The current private key data.  Needed for idempotency. If not provided, the module will always return a change, and all idempotence-related options are ignored. |
| **content_base64**  boolean | Set to `true` if the content is base64 encoded.  Choices:   - `false` ← (default) - `true` |
| **curve**  string | Note that not all curves are supported by all versions of `cryptography`.  For maximal interoperability, `secp384r1` or `secp256r1` should be used.  We use the curve names as defined in the [IANA registry for TLS](https://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml#tls-parameters-8).  Please note that all curves except `secp224r1`, `secp256k1`, `secp256r1`, `secp384r1` and `secp521r1` are discouraged for new private keys.  Choices:   - `"secp224r1"` - `"secp256k1"` - `"secp256r1"` - `"secp384r1"` - `"secp521r1"` - `"secp192r1"` - `"brainpoolP256r1"` - `"brainpoolP384r1"` - `"brainpoolP512r1"` - `"sect163k1"` - `"sect163r2"` - `"sect233k1"` - `"sect233r1"` - `"sect283k1"` - `"sect283r1"` - `"sect409k1"` - `"sect409r1"` - `"sect571k1"` - `"sect571r1"` |
| **format**  string | Determines which format the private key is written in. By default, PKCS1 (traditional OpenSSL format) is used for all keys which support it. Please note that not every key can be exported in any format.  The value `auto` selects a format based on the key format. The value `auto_ignore` does the same, but for existing private key files, it will not force a regenerate when its format is not the automatically selected one for generation.  Note that if the format for an existing private key mismatches, the key is **regenerated** by default. To change this behavior, use the *format_mismatch* option.  Choices:   - `"pkcs1"` - `"pkcs8"` - `"raw"` - `"auto"` - `"auto_ignore"` ← (default) |
| **format_mismatch**  string | Determines behavior of the module if the format of a private key does not match the expected format, but all other parameters are as expected.  If set to `regenerate` (default), generates a new private key.  If set to `convert`, the key will be converted to the new format instead.  Only supported by the `cryptography` backend.  Choices:   - `"regenerate"` ← (default) - `"convert"` |
| **passphrase**  string | The passphrase for the private key. |
| **regenerate**  string | Allows to configure in which situations the module is allowed to regenerate private keys. The module will always generate a new key if the destination file does not exist.  By default, the key will be regenerated when it does not match the module’s options, except when the key cannot be read or the passphrase does not match. Please note that this **changed** for Ansible 2.10. For Ansible 2.9, the behavior was as if `full_idempotence` is specified.  If set to `never`, the module will fail if the key cannot be read or the passphrase is not matching, and will never regenerate an existing key.  If set to `fail`, the module will fail if the key does not correspond to the module’s options.  If set to `partial_idempotence`, the key will be regenerated if it does not conform to the module’s options. The key is **not** regenerated if it cannot be read (broken file), the key is protected by an unknown passphrase, or when they key is not protected by a passphrase, but a passphrase is specified.  If set to `full_idempotence`, the key will be regenerated if it does not conform to the module’s options. This is also the case if the key cannot be read (broken file), the key is protected by an unknown passphrase, or when they key is not protected by a passphrase, but a passphrase is specified. Make sure you have a **backup** when using this option!  If set to `always`, the module will always regenerate the key. This is equivalent to setting *force* to `true`.  Note that if *format_mismatch* is set to `convert` and everything matches except the format, the key will always be converted, except if *regenerate* is set to `always`.  Choices:   - `"never"` - `"fail"` - `"partial_idempotence"` - `"full_idempotence"` ← (default) - `"always"` |
| **return_current_key**  boolean | Set to `true` to return the current private key when the module did not generate a new one.  Note that in case of check mode, when this option is not set to `true`, the module always returns the current key (if it was provided) and Ansible will replace it by `VALUE_SPECIFIED_IN_NO_LOG_PARAMETER`.  Choices:   - `false` ← (default) - `true` |
| **select_crypto_backend**  string | Determines which crypto backend to use.  The default choice is `auto`, which tries to use `cryptography` if available.  If set to `cryptography`, will try to use the [cryptography](https://cryptography.io/) library.  Choices:   - `"auto"` ← (default) - `"cryptography"` |
| **size**  integer | Size (in bits) of the TLS/SSL key to generate.  Default: `4096` |
| **type**  string | The algorithm used to generate the TLS/SSL private key.  Note that `ECC`, `X25519`, `X448`, `Ed25519` and `Ed448` require the `cryptography` backend. `X25519` needs cryptography 2.5 or newer, while `X448`, `Ed25519` and `Ed448` require cryptography 2.6 or newer. For `ECC`, the minimal cryptography version required depends on the *curve* option.  Choices:   - `"DSA"` - `"ECC"` - `"Ed25519"` - `"Ed448"` - `"RSA"` ← (default) - `"X25519"` - `"X448"` |

## [Attributes](openssl_privatekey_pipe_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **action** | Support: full | Indicates this has a corresponding action plugin so some parts of the options can be executed on the controller. |
| **async** | Support: none  This action runs completely on the controller. | Supports being used with the `async` keyword. |
| **check_mode** | Support: full | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support: full | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [See Also](openssl_privatekey_pipe_module.md#id5)

> **See also:**
>
> [community.crypto.openssl_privatekey](openssl_privatekey_module.md#ansible-collections-community-crypto-openssl-privatekey-module)
> :   Generate OpenSSL private keys.
>
> [community.crypto.openssl_privatekey_info](openssl_privatekey_info_module.md#ansible-collections-community-crypto-openssl-privatekey-info-module)
> :   Provide information for OpenSSL private keys.
>
> [community.crypto.x509_certificate](x509_certificate_module.md#ansible-collections-community-crypto-x509-certificate-module)
> :   Generate and/or check OpenSSL certificates.
>
> [community.crypto.x509_certificate_pipe](x509_certificate_pipe_module.md#ansible-collections-community-crypto-x509-certificate-pipe-module)
> :   Generate and/or check OpenSSL certificates.
>
> [community.crypto.openssl_csr](openssl_csr_module.md#ansible-collections-community-crypto-openssl-csr-module)
> :   Generate OpenSSL Certificate Signing Request (CSR).
>
> [community.crypto.openssl_csr_pipe](openssl_csr_pipe_module.md#ansible-collections-community-crypto-openssl-csr-pipe-module)
> :   Generate OpenSSL Certificate Signing Request (CSR).
>
> [community.crypto.openssl_dhparam](openssl_dhparam_module.md#ansible-collections-community-crypto-openssl-dhparam-module)
> :   Generate OpenSSL Diffie-Hellman Parameters.
>
> [community.crypto.openssl_pkcs12](openssl_pkcs12_module.md#ansible-collections-community-crypto-openssl-pkcs12-module)
> :   Generate OpenSSL PKCS#12 archive.
>
> [community.crypto.openssl_publickey](openssl_publickey_module.md#ansible-collections-community-crypto-openssl-publickey-module)
> :   Generate an OpenSSL public key from its private key.

## [Examples](openssl_privatekey_pipe_module.md#id6)

```yaml+jinja
- name: Generate an OpenSSL private key with the default values (4096 bits, RSA)
  community.crypto.openssl_privatekey_pipe:
    path: /etc/ssl/private/ansible.com.pem
  register: output
  no_log: true  # make sure that private key data is not accidentally revealed in logs!
- name: Show generated key
  debug:
    msg: "{{ output.privatekey }}"
  # DO NOT OUTPUT KEY MATERIAL TO CONSOLE OR LOGS IN PRODUCTION!

- block:
    - name: Update sops-encrypted key with the community.sops collection
      community.crypto.openssl_privatekey_pipe:
        content: "{{ lookup('community.sops.sops', 'private_key.pem.sops') }}"
        size: 2048
      register: output
      no_log: true  # make sure that private key data is not accidentally revealed in logs!

    - name: Update encrypted key when openssl_privatekey_pipe reported a change
      community.sops.sops_encrypt:
        path: private_key.pem.sops
        content_text: "{{ output.privatekey }}"
      when: output is changed
  always:
    - name: Make sure that output (which contains the private key) is overwritten
      set_fact:
        output: ''
```

## [Return Values](openssl_privatekey_pipe_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **curve**  string | Elliptic curve used to generate the TLS/SSL private key.  Returned: changed or success, and *type* is `ECC`  Sample: `"secp256r1"` |
| **fingerprint**  dictionary | The fingerprint of the public key. Fingerprint will be generated for each `hashlib.algorithms` available.  Returned: changed or success  Sample: `{"md5": "84:75:71:72:8d:04:b5:6c:4d:37:6d:66:83:f5:4c:29", "sha1": "51:cc:7c:68:5d:eb:41:43:88:7e:1a:ae:c7:f8:24:72:ee:71:f6:10", "sha224": "b1:19:a6:6c:14:ac:33:1d:ed:18:50:d3:06:5c:b2:32:91:f1:f1:52:8c:cb:d5:75:e9:f5:9b:46", "sha256": "41:ab:c7:cb:d5:5f:30:60:46:99:ac:d4:00:70:cf:a1:76:4f:24:5d:10:24:57:5d:51:6e:09:97:df:2f:de:c7", "sha384": "85:39:50:4e:de:d9:19:33:40:70:ae:10:ab:59:24:19:51:c3:a2:e4:0b:1c:b1:6e:dd:b3:0c:d9:9e:6a:46:af:da:18:f8:ef:ae:2e:c0:9a:75:2c:9b:b3:0f:3a:5f:3d", "sha512": "fd:ed:5e:39:48:5f:9f:fe:7f:25:06:3f:79:08:cd:ee:a5:e7:b3:3d:13:82:87:1f:84:e1:f5:c7:28:77:53:94:86:56:38:69:f0:d9:35:22:01:1e:a6:60:...:0f:9b"}` |
| **privatekey**  string | The generated private key’s content.  Please note that if the result is not changed, the current private key will only be returned if the *return_current_key* option is set to `true`.  Will be Base64-encoded if the key is in raw format.  Returned: changed, or *return_current_key* is `true` |
| **size**  integer | Size (in bits) of the TLS/SSL private key.  Returned: changed or success  Sample: `4096` |
| **type**  string | Algorithm used to generate the TLS/SSL private key.  Returned: changed or success  Sample: `"RSA"` |

### Authors

- Yanis Guenane (@Spredzy)
- Felix Fontein (@felixfontein)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.crypto)
[Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-crypto)
