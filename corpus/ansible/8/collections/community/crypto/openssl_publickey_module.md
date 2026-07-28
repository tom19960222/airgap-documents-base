---
collection: ansible
version: "8"
title: "community.crypto.openssl_publickey module – Generate an OpenSSL public key from its private key."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/crypto/openssl_publickey_module.html
fetched_at: 2026-07-28T01:42:36+00:00
---
# community.crypto.openssl_publickey module – Generate an OpenSSL public key from its private key.

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
> see [Requirements](openssl_publickey_module.md#ansible-collections-community-crypto-openssl-publickey-module-requirements) for details.
>
> To use it in a playbook, specify: `community.crypto.openssl_publickey`.

- [Synopsis](openssl_publickey_module.md#synopsis)
- [Requirements](openssl_publickey_module.md#requirements)
- [Parameters](openssl_publickey_module.md#parameters)
- [Attributes](openssl_publickey_module.md#attributes)
- [See Also](openssl_publickey_module.md#see-also)
- [Examples](openssl_publickey_module.md#examples)
- [Return Values](openssl_publickey_module.md#return-values)

## [Synopsis](openssl_publickey_module.md#id1)

- This module allows one to (re)generate public keys from their private keys.
- Public keys are generated in PEM or OpenSSH format. Private keys must be OpenSSL PEM keys. **OpenSSH private keys are not supported**, use the [community.crypto.openssh_keypair](openssh_keypair_module.md#ansible-collections-community-crypto-openssh-keypair-module) module to manage these.
- The module uses the cryptography Python library.

## [Requirements](openssl_publickey_module.md#id2)

The below requirements are needed on the host that executes this module.

- cryptography >= 1.2.3 (older versions might work as well)
- Needs cryptography >= 1.4 if `format` is `OpenSSH`

## [Parameters](openssl_publickey_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **attributes**  aliases: attr  string | The attributes the resulting filesystem object should have.  To get supported flags look at the man page for *chattr* on the target system.  This string should contain the attributes in the same order as the one displayed by *lsattr*.  The `=` operator is assumed as default, otherwise `+` or `-` operators need to be included in the string. |
| **backup**  boolean | Create a backup file including a timestamp so you can get the original public key back if you overwrote it with a different one by accident.  **Choices:**   - `false` ← (default) - `true` |
| **force**  boolean | Should the key be regenerated even it it already exists.  **Choices:**   - `false` ← (default) - `true` |
| **format**  string | The format of the public key.  **Choices:**   - `"OpenSSH"` - `"PEM"` ← (default) |
| **group**  string | Name of the group that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current group of the current user unless you are root, in which case it can preserve the previous ownership. |
| **mode**  any | The permissions the resulting filesystem object should have.  For those used to */usr/bin/chmod* remember that modes are actually octal numbers. You must give Ansible enough information to parse them correctly. For consistent results, quote octal numbers (for example, `'644'` or `'1777'`) so Ansible receives a string and can do its own conversion from string into number. Adding a leading zero (for example, `0755`) works sometimes, but can fail in loops and some other circumstances.  Giving Ansible a number without following either of these rules will end up with a decimal number which will have unexpected results.  As of Ansible 1.8, the mode may be specified as a symbolic mode (for example, `u+rwx` or `u=rw,g=r,o=r`).  If `mode` is not specified and the destination filesystem object **does not** exist, the default `umask` on the system will be used when setting the mode for the newly created filesystem object.  If `mode` is not specified and the destination filesystem object **does** exist, the mode of the existing filesystem object will be used.  Specifying `mode` is the best way to ensure filesystem objects are created with the correct permissions. See CVE-2020-1736 for further details. |
| **owner**  string | Name of the user that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current user unless you are root, in which case it can preserve the previous ownership.  Specifying a numeric username will be assumed to be a user ID and not a username. Avoid numeric usernames to avoid this confusion. |
| **path**  path / required | Name of the file in which the generated TLS/SSL public key will be written. |
| **privatekey_content**  string  *added in community.crypto 1.0.0* | The content of the TLS/SSL private key from which to generate the public key.  Either `privatekey_path` or `privatekey_content` must be specified, but not both. If `state` is `present`, one of them is required. |
| **privatekey_passphrase**  string | The passphrase for the private key. |
| **privatekey_path**  path | Path to the TLS/SSL private key from which to generate the public key.  Either `privatekey_path` or `privatekey_content` must be specified, but not both. If `state` is `present`, one of them is required. |
| **return_content**  boolean  *added in community.crypto 1.0.0* | If set to `true`, will return the (current or generated) public key’s content as `publickey`.  **Choices:**   - `false` ← (default) - `true` |
| **select_crypto_backend**  string | Determines which crypto backend to use.  The default choice is `auto`, which tries to use `cryptography` if available.  If set to `cryptography`, will try to use the [cryptography](https://cryptography.io/) library.  **Choices:**   - `"auto"` ← (default) - `"cryptography"` |
| **selevel**  string | The level part of the SELinux filesystem object context.  This is the MLS/MCS attribute, sometimes known as the `range`.  When set to `_default`, it will use the `level` portion of the policy if available. |
| **serole**  string | The role part of the SELinux filesystem object context.  When set to `_default`, it will use the `role` portion of the policy if available. |
| **setype**  string | The type part of the SELinux filesystem object context.  When set to `_default`, it will use the `type` portion of the policy if available. |
| **seuser**  string | The user part of the SELinux filesystem object context.  By default it uses the `system` policy, where applicable.  When set to `_default`, it will use the `user` portion of the policy if available. |
| **state**  string | Whether the public key should exist or not, taking action if the state is different from what is stated.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **unsafe_writes**  boolean | Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target filesystem object.  By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target filesystem objects, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted filesystem objects, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.  This option allows Ansible to fall back to unsafe methods of updating filesystem objects when atomic operations fail (however, it doesn’t force Ansible to perform unsafe writes).  IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](openssl_publickey_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |
| **safe_file_operations** | **Support:** **full** | Uses Ansible’s strict file operation functions to ensure proper permissions and avoid data corruption. |

## [See Also](openssl_publickey_module.md#id5)

> **See also:**
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
> [community.crypto.openssl_privatekey](openssl_privatekey_module.md#ansible-collections-community-crypto-openssl-privatekey-module)
> :   Generate OpenSSL private keys.
>
> [community.crypto.openssl_privatekey_pipe](openssl_privatekey_pipe_module.md#ansible-collections-community-crypto-openssl-privatekey-pipe-module)
> :   Generate OpenSSL private keys without disk access.

## [Examples](openssl_publickey_module.md#id6)

```yaml+jinja
- name: Generate an OpenSSL public key in PEM format
  community.crypto.openssl_publickey:
    path: /etc/ssl/public/ansible.com.pem
    privatekey_path: /etc/ssl/private/ansible.com.pem

- name: Generate an OpenSSL public key in PEM format from an inline key
  community.crypto.openssl_publickey:
    path: /etc/ssl/public/ansible.com.pem
    privatekey_content: "{{ private_key_content }}"

- name: Generate an OpenSSL public key in OpenSSH v2 format
  community.crypto.openssl_publickey:
    path: /etc/ssl/public/ansible.com.pem
    privatekey_path: /etc/ssl/private/ansible.com.pem
    format: OpenSSH

- name: Generate an OpenSSL public key with a passphrase protected private key
  community.crypto.openssl_publickey:
    path: /etc/ssl/public/ansible.com.pem
    privatekey_path: /etc/ssl/private/ansible.com.pem
    privatekey_passphrase: ansible

- name: Force regenerate an OpenSSL public key if it already exists
  community.crypto.openssl_publickey:
    path: /etc/ssl/public/ansible.com.pem
    privatekey_path: /etc/ssl/private/ansible.com.pem
    force: true

- name: Remove an OpenSSL public key
  community.crypto.openssl_publickey:
    path: /etc/ssl/public/ansible.com.pem
    state: absent
```

## [Return Values](openssl_publickey_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_file**  string | Name of backup file created.  **Returned:** changed and if `backup` is `true`  **Sample:** `"/path/to/publickey.pem.2019-03-09@11:22~"` |
| **filename**  string | Path to the generated TLS/SSL public key file.  **Returned:** changed or success  **Sample:** `"/etc/ssl/public/ansible.com.pem"` |
| **fingerprint**  dictionary | The fingerprint of the public key. Fingerprint will be generated for each hashlib.algorithms available.  **Returned:** changed or success  **Sample:** `{"md5": "84:75:71:72:8d:04:b5:6c:4d:37:6d:66:83:f5:4c:29", "sha1": "51:cc:7c:68:5d:eb:41:43:88:7e:1a:ae:c7:f8:24:72:ee:71:f6:10", "sha224": "b1:19:a6:6c:14:ac:33:1d:ed:18:50:d3:06:5c:b2:32:91:f1:f1:52:8c:cb:d5:75:e9:f5:9b:46", "sha256": "41:ab:c7:cb:d5:5f:30:60:46:99:ac:d4:00:70:cf:a1:76:4f:24:5d:10:24:57:5d:51:6e:09:97:df:2f:de:c7", "sha384": "85:39:50:4e:de:d9:19:33:40:70:ae:10:ab:59:24:19:51:c3:a2:e4:0b:1c:b1:6e:dd:b3:0c:d9:9e:6a:46:af:da:18:f8:ef:ae:2e:c0:9a:75:2c:9b:b3:0f:3a:5f:3d", "sha512": "fd:ed:5e:39:48:5f:9f:fe:7f:25:06:3f:79:08:cd:ee:a5:e7:b3:3d:13:82:87:1f:84:e1:f5:c7:28:77:53:94:86:56:38:69:f0:d9:35:22:01:1e:a6:60:...:0f:9b"}` |
| **format**  string | The format of the public key (PEM, OpenSSH, …).  **Returned:** changed or success  **Sample:** `"PEM"` |
| **privatekey**  string | Path to the TLS/SSL private key the public key was generated from.  Will be `none` if the private key has been provided in `privatekey_content`.  **Returned:** changed or success  **Sample:** `"/etc/ssl/private/ansible.com.pem"` |
| **publickey**  string  *added in community.crypto 1.0.0* | The (current or generated) public key’s content.  **Returned:** if `state` is `present` and `return_content` is `true` |

### Authors

- Yanis Guenane (@Spredzy)
- Felix Fontein (@felixfontein)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.crypto)
- [Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-crypto)
