---
collection: ansible
version: "8"
title: "community.crypto.openssl_privatekey_convert module – Convert OpenSSL private keys"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/crypto/openssl_privatekey_convert_module.html
fetched_at: 2026-07-28T01:42:34+00:00
---
# community.crypto.openssl_privatekey_convert module – Convert OpenSSL private keys

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
> see [Requirements](openssl_privatekey_convert_module.md#ansible-collections-community-crypto-openssl-privatekey-convert-module-requirements) for details.
>
> To use it in a playbook, specify: `community.crypto.openssl_privatekey_convert`.

New in community.crypto 2.1.0

- [Synopsis](openssl_privatekey_convert_module.md#synopsis)
- [Requirements](openssl_privatekey_convert_module.md#requirements)
- [Parameters](openssl_privatekey_convert_module.md#parameters)
- [Attributes](openssl_privatekey_convert_module.md#attributes)
- [See Also](openssl_privatekey_convert_module.md#see-also)
- [Examples](openssl_privatekey_convert_module.md#examples)
- [Return Values](openssl_privatekey_convert_module.md#return-values)

## [Synopsis](openssl_privatekey_convert_module.md#id1)

- This module allows one to convert OpenSSL private keys.
- The default mode for the private key file will be `0600` if `mode` is not explicitly set.

## [Requirements](openssl_privatekey_convert_module.md#id2)

The below requirements are needed on the host that executes this module.

- cryptography >= 1.2.3 (older versions might work as well)

## [Parameters](openssl_privatekey_convert_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **attributes**  aliases: attr  string | The attributes the resulting filesystem object should have.  To get supported flags look at the man page for *chattr* on the target system.  This string should contain the attributes in the same order as the one displayed by *lsattr*.  The `=` operator is assumed as default, otherwise `+` or `-` operators need to be included in the string. |
| **backup**  boolean | Create a backup file including a timestamp so you can get the original private key back if you overwrote it with a new one by accident.  **Choices:**   - `false` ← (default) - `true` |
| **dest_passphrase**  string | The passphrase for the private key to store. |
| **dest_path**  path / required | Name of the file in which the generated TLS/SSL private key will be written. It will have `0600` mode if `mode` is not explicitly set. |
| **format**  string / required | Determines which format the destination private key should be written in.  Please note that not every key can be exported in any format, and that not every format supports encryption.  **Choices:**   - `"pkcs1"` - `"pkcs8"` - `"raw"` |
| **group**  string | Name of the group that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current group of the current user unless you are root, in which case it can preserve the previous ownership. |
| **mode**  any | The permissions the resulting filesystem object should have.  For those used to */usr/bin/chmod* remember that modes are actually octal numbers. You must give Ansible enough information to parse them correctly. For consistent results, quote octal numbers (for example, `'644'` or `'1777'`) so Ansible receives a string and can do its own conversion from string into number. Adding a leading zero (for example, `0755`) works sometimes, but can fail in loops and some other circumstances.  Giving Ansible a number without following either of these rules will end up with a decimal number which will have unexpected results.  As of Ansible 1.8, the mode may be specified as a symbolic mode (for example, `u+rwx` or `u=rw,g=r,o=r`).  If `mode` is not specified and the destination filesystem object **does not** exist, the default `umask` on the system will be used when setting the mode for the newly created filesystem object.  If `mode` is not specified and the destination filesystem object **does** exist, the mode of the existing filesystem object will be used.  Specifying `mode` is the best way to ensure filesystem objects are created with the correct permissions. See CVE-2020-1736 for further details. |
| **owner**  string | Name of the user that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current user unless you are root, in which case it can preserve the previous ownership.  Specifying a numeric username will be assumed to be a user ID and not a username. Avoid numeric usernames to avoid this confusion. |
| **selevel**  string | The level part of the SELinux filesystem object context.  This is the MLS/MCS attribute, sometimes known as the `range`.  When set to `_default`, it will use the `level` portion of the policy if available. |
| **serole**  string | The role part of the SELinux filesystem object context.  When set to `_default`, it will use the `role` portion of the policy if available. |
| **setype**  string | The type part of the SELinux filesystem object context.  When set to `_default`, it will use the `type` portion of the policy if available. |
| **seuser**  string | The user part of the SELinux filesystem object context.  By default it uses the `system` policy, where applicable.  When set to `_default`, it will use the `user` portion of the policy if available. |
| **src_content**  string | The content of the file containing the OpenSSL private key to convert.  Exactly one of `src_path` or `src_content` must be specified. |
| **src_passphrase**  string | The passphrase for the private key to load. |
| **src_path**  path | Name of the file containing the OpenSSL private key to convert.  Exactly one of `src_path` or `src_content` must be specified. |
| **unsafe_writes**  boolean | Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target filesystem object.  By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target filesystem objects, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted filesystem objects, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.  This option allows Ansible to fall back to unsafe methods of updating filesystem objects when atomic operations fail (however, it doesn’t force Ansible to perform unsafe writes).  IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](openssl_privatekey_convert_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |
| **safe_file_operations** | **Support:** **full** | Uses Ansible’s strict file operation functions to ensure proper permissions and avoid data corruption. |

## [See Also](openssl_privatekey_convert_module.md#id5)

> **See also:**
>
> [community.crypto.openssl_privatekey](openssl_privatekey_module.md#ansible-collections-community-crypto-openssl-privatekey-module)
> :   Generate OpenSSL private keys.
>
> [community.crypto.openssl_privatekey_pipe](openssl_privatekey_pipe_module.md#ansible-collections-community-crypto-openssl-privatekey-pipe-module)
> :   Generate OpenSSL private keys without disk access.
>
> [community.crypto.openssl_publickey](openssl_publickey_module.md#ansible-collections-community-crypto-openssl-publickey-module)
> :   Generate an OpenSSL public key from its private key.

## [Examples](openssl_privatekey_convert_module.md#id6)

```yaml+jinja
- name: Convert private key to PKCS8 format with passphrase
  community.crypto.openssl_privatekey_convert:
    src_path: /etc/ssl/private/ansible.com.pem
    dest_path: /etc/ssl/private/ansible.com.key
    dest_passphrase: '{{ private_key_passphrase }}'
    format: pkcs8
```

## [Return Values](openssl_privatekey_convert_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_file**  string | Name of backup file created.  **Returned:** changed and if `backup` is `true`  **Sample:** `"/path/to/privatekey.pem.2019-03-09@11:22~"` |

### Authors

- Felix Fontein (@felixfontein)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.crypto)
- [Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-crypto)
