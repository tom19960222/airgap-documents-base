---
collection: ansible
version: "6"
title: "community.crypto.openssh_keypair module – Generate OpenSSH private and public keys"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/crypto/openssh_keypair_module.html
fetched_at: 2026-07-27T17:06:19+00:00
---
# community.crypto.openssh_keypair module – Generate OpenSSH private and public keys

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
> see [Requirements](openssh_keypair_module.md#ansible-collections-community-crypto-openssh-keypair-module-requirements) for details.
>
> To use it in a playbook, specify: `community.crypto.openssh_keypair`.

- [Synopsis](openssh_keypair_module.md#synopsis)
- [Requirements](openssh_keypair_module.md#requirements)
- [Parameters](openssh_keypair_module.md#parameters)
- [Attributes](openssh_keypair_module.md#attributes)
- [Notes](openssh_keypair_module.md#notes)
- [Examples](openssh_keypair_module.md#examples)
- [Return Values](openssh_keypair_module.md#return-values)

## [Synopsis](openssh_keypair_module.md#id1)

- This module allows one to (re)generate OpenSSH private and public keys. It uses ssh-keygen to generate keys. One can generate `rsa`, `dsa`, `rsa1`, `ed25519` or `ecdsa` private keys.

## [Requirements](openssh_keypair_module.md#id2)

The below requirements are needed on the host that executes this module.

- ssh-keygen (if *backend=openssh*)
- cryptography >= 2.6 (if *backend=cryptography* and OpenSSH < 7.8 is installed)
- cryptography >= 3.0 (if *backend=cryptography* and OpenSSH >= 7.8 is installed)

## [Parameters](openssh_keypair_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **attributes**  aliases: attr  string | The attributes the resulting filesystem object should have.  To get supported flags look at the man page for *chattr* on the target system.  This string should contain the attributes in the same order as the one displayed by *lsattr*.  The `=` operator is assumed as default, otherwise `+` or `-` operators need to be included in the string. |
| **backend**  string  added in community.crypto 1.7.0 | Selects between the `cryptography` library or the OpenSSH binary `opensshbin`.  `auto` will default to `opensshbin` unless the OpenSSH binary is not installed or when using *passphrase*.  Choices:   - `"auto"` ← (default) - `"cryptography"` - `"opensshbin"` |
| **comment**  string | Provides a new comment to the public key. |
| **force**  boolean | Should the key be regenerated even if it already exists  Choices:   - `false` ← (default) - `true` |
| **group**  string | Name of the group that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current group of the current user unless you are root, in which case it can preserve the previous ownership. |
| **mode**  any | The permissions the resulting filesystem object should have.  For those used to */usr/bin/chmod* remember that modes are actually octal numbers. You must either add a leading zero so that Ansible’s YAML parser knows it is an octal number (like `0644` or `01777`) or quote it (like `'644'` or `'1777'`) so Ansible receives a string and can do its own conversion from string into number.  Giving Ansible a number without following one of these rules will end up with a decimal number which will have unexpected results.  As of Ansible 1.8, the mode may be specified as a symbolic mode (for example, `u+rwx` or `u=rw,g=r,o=r`).  If `mode` is not specified and the destination filesystem object **does not** exist, the default `umask` on the system will be used when setting the mode for the newly created filesystem object.  If `mode` is not specified and the destination filesystem object **does** exist, the mode of the existing filesystem object will be used.  Specifying `mode` is the best way to ensure filesystem objects are created with the correct permissions. See CVE-2020-1736 for further details. |
| **owner**  string | Name of the user that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current user unless you are root, in which case it can preserve the previous ownership. |
| **passphrase**  string  added in community.crypto 1.7.0 | Passphrase used to decrypt an existing private key or encrypt a newly generated private key.  Passphrases are not supported for *type=rsa1*.  Can only be used when *backend=cryptography*, or when *backend=auto* and a required `cryptography` version is installed. |
| **path**  path / required | Name of the files containing the public and private key. The file containing the public key will have the extension `.pub`. |
| **private_key_format**  string  added in community.crypto 1.7.0 | Used when *backend=cryptography* to select a format for the private key at the provided *path*.  When set to `auto` this module will match the key format of the installed OpenSSH version.  For OpenSSH < 7.8 private keys will be in PKCS1 format except ed25519 keys which will be in OpenSSH format.  For OpenSSH >= 7.8 all private key types will be in the OpenSSH format.  Using this option when *regenerate=partial_idempotence* or *regenerate=full_idempotence* will cause a new keypair to be generated if the private key’s format does not match the value of *private_key_format*. This module will not however convert existing private keys between formats.  Choices:   - `"auto"` ← (default) - `"pkcs1"` - `"pkcs8"` - `"ssh"` |
| **regenerate**  string  added in community.crypto 1.0.0 | Allows to configure in which situations the module is allowed to regenerate private keys. The module will always generate a new key if the destination file does not exist.  By default, the key will be regenerated when it does not match the module’s options, except when the key cannot be read or the passphrase does not match. Please note that this **changed** for Ansible 2.10. For Ansible 2.9, the behavior was as if `full_idempotence` is specified.  If set to `never`, the module will fail if the key cannot be read or the passphrase is not matching, and will never regenerate an existing key.  If set to `fail`, the module will fail if the key does not correspond to the module’s options.  If set to `partial_idempotence`, the key will be regenerated if it does not conform to the module’s options. The key is **not** regenerated if it cannot be read (broken file), the key is protected by an unknown passphrase, or when they key is not protected by a passphrase, but a passphrase is specified.  If set to `full_idempotence`, the key will be regenerated if it does not conform to the module’s options. This is also the case if the key cannot be read (broken file), the key is protected by an unknown passphrase, or when they key is not protected by a passphrase, but a passphrase is specified. Make sure you have a **backup** when using this option!  If set to `always`, the module will always regenerate the key. This is equivalent to setting *force* to `true`.  Note that adjusting the comment and the permissions can be changed without regeneration. Therefore, even for `never`, the task can result in changed.  Choices:   - `"never"` - `"fail"` - `"partial_idempotence"` ← (default) - `"full_idempotence"` - `"always"` |
| **selevel**  string | The level part of the SELinux filesystem object context.  This is the MLS/MCS attribute, sometimes known as the `range`.  When set to `_default`, it will use the `level` portion of the policy if available. |
| **serole**  string | The role part of the SELinux filesystem object context.  When set to `_default`, it will use the `role` portion of the policy if available. |
| **setype**  string | The type part of the SELinux filesystem object context.  When set to `_default`, it will use the `type` portion of the policy if available. |
| **seuser**  string | The user part of the SELinux filesystem object context.  By default it uses the `system` policy, where applicable.  When set to `_default`, it will use the `user` portion of the policy if available. |
| **size**  integer | Specifies the number of bits in the private key to create. For RSA keys, the minimum size is 1024 bits and the default is 4096 bits. Generally, 2048 bits is considered sufficient. DSA keys must be exactly 1024 bits as specified by FIPS 186-2. For ECDSA keys, size determines the key length by selecting from one of three elliptic curve sizes: 256, 384 or 521 bits. Attempting to use bit lengths other than these three values for ECDSA keys will cause this module to fail. Ed25519 keys have a fixed length and the size will be ignored. |
| **state**  string | Whether the private and public keys should exist or not, taking action if the state is different from what is stated.  Choices:   - `"present"` ← (default) - `"absent"` |
| **type**  string | The algorithm used to generate the SSH private key. `rsa1` is for protocol version 1. `rsa1` is deprecated and may not be supported by every version of ssh-keygen.  Choices:   - `"rsa"` ← (default) - `"dsa"` - `"rsa1"` - `"ecdsa"` - `"ed25519"` |
| **unsafe_writes**  boolean | Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target filesystem object.  By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target filesystem objects, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted filesystem objects, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.  This option allows Ansible to fall back to unsafe methods of updating filesystem objects when atomic operations fail (however, it doesn’t force Ansible to perform unsafe writes).  IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.  Choices:   - `false` ← (default) - `true` |

## [Attributes](openssh_keypair_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support: full | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |
| **safe_file_operations** | Support: full | Uses Ansible’s strict file operation functions to ensure proper permissions and avoid data corruption. |

## [Notes](openssh_keypair_module.md#id5)

> **Note:**
>
> - In case the ssh key is broken or password protected, the module will fail. Set the *force* option to `true` if you want to regenerate the keypair.
> - In the case a custom `mode`, `group`, `owner`, or other file attribute is provided it will be applied to both key files.

## [Examples](openssh_keypair_module.md#id6)

```yaml+jinja
- name: Generate an OpenSSH keypair with the default values (4096 bits, rsa)
  community.crypto.openssh_keypair:
    path: /tmp/id_ssh_rsa

- name: Generate an OpenSSH keypair with the default values (4096 bits, rsa) and encrypted private key
  community.crypto.openssh_keypair:
    path: /tmp/id_ssh_rsa
    passphrase: super_secret_password

- name: Generate an OpenSSH rsa keypair with a different size (2048 bits)
  community.crypto.openssh_keypair:
    path: /tmp/id_ssh_rsa
    size: 2048

- name: Force regenerate an OpenSSH keypair if it already exists
  community.crypto.openssh_keypair:
    path: /tmp/id_ssh_rsa
    force: True

- name: Generate an OpenSSH keypair with a different algorithm (dsa)
  community.crypto.openssh_keypair:
    path: /tmp/id_ssh_dsa
    type: dsa
```

## [Return Values](openssh_keypair_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **comment**  string | The comment of the generated key.  Returned: changed or success  Sample: `"test@comment"` |
| **filename**  string | Path to the generated SSH private key file.  Returned: changed or success  Sample: `"/tmp/id_ssh_rsa"` |
| **fingerprint**  string | The fingerprint of the key.  Returned: changed or success  Sample: `"SHA256:r4YCZxihVjedH2OlfjVGI6Y5xAYtdCwk8VxKyzVyYfM"` |
| **public_key**  string | The public key of the generated SSH private key.  Returned: changed or success  Sample: `"ssh-rsa AAAAB3Nza(...omitted...)veL4E3Xcw=="` |
| **size**  integer | Size (in bits) of the SSH private key.  Returned: changed or success  Sample: `4096` |
| **type**  string | Algorithm used to generate the SSH private key.  Returned: changed or success  Sample: `"rsa"` |

### Authors

- David Kainz (@lolcube)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.crypto)
[Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-crypto)
