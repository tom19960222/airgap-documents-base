---
collection: ansible
version: "6"
title: "community.crypto.openssl_privatekey module – Generate OpenSSL private keys"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/crypto/openssl_privatekey_module.html
fetched_at: 2026-07-27T17:06:23+00:00
---
# community.crypto.openssl_privatekey module – Generate OpenSSL private keys

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
> see [Requirements](openssl_privatekey_module.md#ansible-collections-community-crypto-openssl-privatekey-module-requirements) for details.
>
> To use it in a playbook, specify: `community.crypto.openssl_privatekey`.

- [Synopsis](openssl_privatekey_module.md#synopsis)
- [Requirements](openssl_privatekey_module.md#requirements)
- [Parameters](openssl_privatekey_module.md#parameters)
- [Attributes](openssl_privatekey_module.md#attributes)
- [See Also](openssl_privatekey_module.md#see-also)
- [Examples](openssl_privatekey_module.md#examples)
- [Return Values](openssl_privatekey_module.md#return-values)

## [Synopsis](openssl_privatekey_module.md#id1)

- Keys are generated in PEM format.
- One can generate [RSA](https://en.wikipedia.org/wiki/RSA_%28cryptosystem%29), [DSA](https://en.wikipedia.org/wiki/Digital_Signature_Algorithm), [ECC](https://en.wikipedia.org/wiki/Elliptic-curve_cryptography) or [EdDSA](https://en.wikipedia.org/wiki/EdDSA) private keys.
- Please note that the module regenerates private keys if they do not match the module’s options. In particular, if you provide another passphrase (or specify none), change the keysize, etc., the private key will be regenerated. If you are concerned that this could **overwrite your private key**, consider using the *backup* option.
- The default mode for the private key file will be `0600` if *mode* is not explicitly set.
- This module allows one to (re)generate OpenSSL private keys.

## [Requirements](openssl_privatekey_module.md#id2)

The below requirements are needed on the host that executes this module.

- cryptography >= 1.2.3 (older versions might work as well)

## [Parameters](openssl_privatekey_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **attributes**  aliases: attr  string | The attributes the resulting filesystem object should have.  To get supported flags look at the man page for *chattr* on the target system.  This string should contain the attributes in the same order as the one displayed by *lsattr*.  The `=` operator is assumed as default, otherwise `+` or `-` operators need to be included in the string. |
| **backup**  boolean | Create a backup file including a timestamp so you can get the original private key back if you overwrote it with a new one by accident.  Choices:   - `false` ← (default) - `true` |
| **cipher**  string | The cipher to encrypt the private key. Must be `auto`. |
| **curve**  string | Note that not all curves are supported by all versions of `cryptography`.  For maximal interoperability, `secp384r1` or `secp256r1` should be used.  We use the curve names as defined in the [IANA registry for TLS](https://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml#tls-parameters-8).  Please note that all curves except `secp224r1`, `secp256k1`, `secp256r1`, `secp384r1` and `secp521r1` are discouraged for new private keys.  Choices:   - `"secp224r1"` - `"secp256k1"` - `"secp256r1"` - `"secp384r1"` - `"secp521r1"` - `"secp192r1"` - `"brainpoolP256r1"` - `"brainpoolP384r1"` - `"brainpoolP512r1"` - `"sect163k1"` - `"sect163r2"` - `"sect233k1"` - `"sect233r1"` - `"sect283k1"` - `"sect283r1"` - `"sect409k1"` - `"sect409r1"` - `"sect571k1"` - `"sect571r1"` |
| **force**  boolean | Should the key be regenerated even if it already exists.  Choices:   - `false` ← (default) - `true` |
| **format**  string  added in community.crypto 1.0.0 | Determines which format the private key is written in. By default, PKCS1 (traditional OpenSSL format) is used for all keys which support it. Please note that not every key can be exported in any format.  The value `auto` selects a format based on the key format. The value `auto_ignore` does the same, but for existing private key files, it will not force a regenerate when its format is not the automatically selected one for generation.  Note that if the format for an existing private key mismatches, the key is **regenerated** by default. To change this behavior, use the *format_mismatch* option.  Choices:   - `"pkcs1"` - `"pkcs8"` - `"raw"` - `"auto"` - `"auto_ignore"` ← (default) |
| **format_mismatch**  string  added in community.crypto 1.0.0 | Determines behavior of the module if the format of a private key does not match the expected format, but all other parameters are as expected.  If set to `regenerate` (default), generates a new private key.  If set to `convert`, the key will be converted to the new format instead.  Only supported by the `cryptography` backend.  Choices:   - `"regenerate"` ← (default) - `"convert"` |
| **group**  string | Name of the group that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current group of the current user unless you are root, in which case it can preserve the previous ownership. |
| **mode**  any | The permissions the resulting filesystem object should have.  For those used to */usr/bin/chmod* remember that modes are actually octal numbers. You must either add a leading zero so that Ansible’s YAML parser knows it is an octal number (like `0644` or `01777`) or quote it (like `'644'` or `'1777'`) so Ansible receives a string and can do its own conversion from string into number.  Giving Ansible a number without following one of these rules will end up with a decimal number which will have unexpected results.  As of Ansible 1.8, the mode may be specified as a symbolic mode (for example, `u+rwx` or `u=rw,g=r,o=r`).  If `mode` is not specified and the destination filesystem object **does not** exist, the default `umask` on the system will be used when setting the mode for the newly created filesystem object.  If `mode` is not specified and the destination filesystem object **does** exist, the mode of the existing filesystem object will be used.  Specifying `mode` is the best way to ensure filesystem objects are created with the correct permissions. See CVE-2020-1736 for further details. |
| **owner**  string | Name of the user that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current user unless you are root, in which case it can preserve the previous ownership. |
| **passphrase**  string | The passphrase for the private key. |
| **path**  path / required | Name of the file in which the generated TLS/SSL private key will be written. It will have `0600` mode if *mode* is not explicitly set. |
| **regenerate**  string  added in community.crypto 1.0.0 | Allows to configure in which situations the module is allowed to regenerate private keys. The module will always generate a new key if the destination file does not exist.  By default, the key will be regenerated when it does not match the module’s options, except when the key cannot be read or the passphrase does not match. Please note that this **changed** for Ansible 2.10. For Ansible 2.9, the behavior was as if `full_idempotence` is specified.  If set to `never`, the module will fail if the key cannot be read or the passphrase is not matching, and will never regenerate an existing key.  If set to `fail`, the module will fail if the key does not correspond to the module’s options.  If set to `partial_idempotence`, the key will be regenerated if it does not conform to the module’s options. The key is **not** regenerated if it cannot be read (broken file), the key is protected by an unknown passphrase, or when they key is not protected by a passphrase, but a passphrase is specified.  If set to `full_idempotence`, the key will be regenerated if it does not conform to the module’s options. This is also the case if the key cannot be read (broken file), the key is protected by an unknown passphrase, or when they key is not protected by a passphrase, but a passphrase is specified. Make sure you have a **backup** when using this option!  If set to `always`, the module will always regenerate the key. This is equivalent to setting *force* to `true`.  Note that if *format_mismatch* is set to `convert` and everything matches except the format, the key will always be converted, except if *regenerate* is set to `always`.  Choices:   - `"never"` - `"fail"` - `"partial_idempotence"` - `"full_idempotence"` ← (default) - `"always"` |
| **return_content**  boolean  added in community.crypto 1.0.0 | If set to `true`, will return the (current or generated) private key’s content as *privatekey*.  Note that especially if the private key is not encrypted, you have to make sure that the returned value is treated appropriately and not accidentally written to logs etc.! Use with care!  Use Ansible’s *no_log* task option to avoid the output being shown. See also <https://docs.ansible.com/ansible/latest/reference_appendices/faq.html#how-do-i-keep-secret-data-in-my-playbook>.  Choices:   - `false` ← (default) - `true` |
| **select_crypto_backend**  string | Determines which crypto backend to use.  The default choice is `auto`, which tries to use `cryptography` if available.  If set to `cryptography`, will try to use the [cryptography](https://cryptography.io/) library.  Choices:   - `"auto"` ← (default) - `"cryptography"` |
| **selevel**  string | The level part of the SELinux filesystem object context.  This is the MLS/MCS attribute, sometimes known as the `range`.  When set to `_default`, it will use the `level` portion of the policy if available. |
| **serole**  string | The role part of the SELinux filesystem object context.  When set to `_default`, it will use the `role` portion of the policy if available. |
| **setype**  string | The type part of the SELinux filesystem object context.  When set to `_default`, it will use the `type` portion of the policy if available. |
| **seuser**  string | The user part of the SELinux filesystem object context.  By default it uses the `system` policy, where applicable.  When set to `_default`, it will use the `user` portion of the policy if available. |
| **size**  integer | Size (in bits) of the TLS/SSL key to generate.  Default: `4096` |
| **state**  string | Whether the private key should exist or not, taking action if the state is different from what is stated.  Choices:   - `"absent"` - `"present"` ← (default) |
| **type**  string | The algorithm used to generate the TLS/SSL private key.  Note that `ECC`, `X25519`, `X448`, `Ed25519` and `Ed448` require the `cryptography` backend. `X25519` needs cryptography 2.5 or newer, while `X448`, `Ed25519` and `Ed448` require cryptography 2.6 or newer. For `ECC`, the minimal cryptography version required depends on the *curve* option.  Choices:   - `"DSA"` - `"ECC"` - `"Ed25519"` - `"Ed448"` - `"RSA"` ← (default) - `"X25519"` - `"X448"` |
| **unsafe_writes**  boolean | Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target filesystem object.  By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target filesystem objects, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted filesystem objects, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.  This option allows Ansible to fall back to unsafe methods of updating filesystem objects when atomic operations fail (however, it doesn’t force Ansible to perform unsafe writes).  IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.  Choices:   - `false` ← (default) - `true` |

## [Attributes](openssl_privatekey_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support: full | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |
| **safe_file_operations** | Support: full | Uses Ansible’s strict file operation functions to ensure proper permissions and avoid data corruption. |

## [See Also](openssl_privatekey_module.md#id5)

> **See also:**
>
> [community.crypto.openssl_privatekey_pipe](openssl_privatekey_pipe_module.md#ansible-collections-community-crypto-openssl-privatekey-pipe-module)
> :   Generate OpenSSL private keys without disk access.
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

## [Examples](openssl_privatekey_module.md#id6)

```yaml+jinja
- name: Generate an OpenSSL private key with the default values (4096 bits, RSA)
  community.crypto.openssl_privatekey:
    path: /etc/ssl/private/ansible.com.pem

- name: Generate an OpenSSL private key with the default values (4096 bits, RSA) and a passphrase
  community.crypto.openssl_privatekey:
    path: /etc/ssl/private/ansible.com.pem
    passphrase: ansible
    cipher: auto

- name: Generate an OpenSSL private key with a different size (2048 bits)
  community.crypto.openssl_privatekey:
    path: /etc/ssl/private/ansible.com.pem
    size: 2048

- name: Force regenerate an OpenSSL private key if it already exists
  community.crypto.openssl_privatekey:
    path: /etc/ssl/private/ansible.com.pem
    force: true

- name: Generate an OpenSSL private key with a different algorithm (DSA)
  community.crypto.openssl_privatekey:
    path: /etc/ssl/private/ansible.com.pem
    type: DSA
```

## [Return Values](openssl_privatekey_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_file**  string | Name of backup file created.  Returned: changed and if *backup* is `true`  Sample: `"/path/to/privatekey.pem.2019-03-09@11:22~"` |
| **curve**  string | Elliptic curve used to generate the TLS/SSL private key.  Returned: changed or success, and *type* is `ECC`  Sample: `"secp256r1"` |
| **filename**  string | Path to the generated TLS/SSL private key file.  Returned: changed or success  Sample: `"/etc/ssl/private/ansible.com.pem"` |
| **fingerprint**  dictionary | The fingerprint of the public key. Fingerprint will be generated for each `hashlib.algorithms` available.  Returned: changed or success  Sample: `{"md5": "84:75:71:72:8d:04:b5:6c:4d:37:6d:66:83:f5:4c:29", "sha1": "51:cc:7c:68:5d:eb:41:43:88:7e:1a:ae:c7:f8:24:72:ee:71:f6:10", "sha224": "b1:19:a6:6c:14:ac:33:1d:ed:18:50:d3:06:5c:b2:32:91:f1:f1:52:8c:cb:d5:75:e9:f5:9b:46", "sha256": "41:ab:c7:cb:d5:5f:30:60:46:99:ac:d4:00:70:cf:a1:76:4f:24:5d:10:24:57:5d:51:6e:09:97:df:2f:de:c7", "sha384": "85:39:50:4e:de:d9:19:33:40:70:ae:10:ab:59:24:19:51:c3:a2:e4:0b:1c:b1:6e:dd:b3:0c:d9:9e:6a:46:af:da:18:f8:ef:ae:2e:c0:9a:75:2c:9b:b3:0f:3a:5f:3d", "sha512": "fd:ed:5e:39:48:5f:9f:fe:7f:25:06:3f:79:08:cd:ee:a5:e7:b3:3d:13:82:87:1f:84:e1:f5:c7:28:77:53:94:86:56:38:69:f0:d9:35:22:01:1e:a6:60:...:0f:9b"}` |
| **privatekey**  string  added in community.crypto 1.0.0 | The (current or generated) private key’s content.  Will be Base64-encoded if the key is in raw format.  Returned: if *state* is `present` and *return_content* is `true` |
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
