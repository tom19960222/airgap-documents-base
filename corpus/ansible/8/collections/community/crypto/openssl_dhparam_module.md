---
collection: ansible
version: "8"
title: "community.crypto.openssl_dhparam module – Generate OpenSSL Diffie-Hellman Parameters"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/crypto/openssl_dhparam_module.html
fetched_at: 2026-07-28T01:42:32+00:00
---
# community.crypto.openssl_dhparam module – Generate OpenSSL Diffie-Hellman Parameters

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
> see [Requirements](openssl_dhparam_module.md#ansible-collections-community-crypto-openssl-dhparam-module-requirements) for details.
>
> To use it in a playbook, specify: `community.crypto.openssl_dhparam`.

- [Synopsis](openssl_dhparam_module.md#synopsis)
- [Requirements](openssl_dhparam_module.md#requirements)
- [Parameters](openssl_dhparam_module.md#parameters)
- [Attributes](openssl_dhparam_module.md#attributes)
- [See Also](openssl_dhparam_module.md#see-also)
- [Examples](openssl_dhparam_module.md#examples)
- [Return Values](openssl_dhparam_module.md#return-values)

## [Synopsis](openssl_dhparam_module.md#id1)

- This module allows one to (re)generate OpenSSL DH-params.
- This module uses file common arguments to specify generated file permissions.
- Please note that the module regenerates existing DH params if they do not match the module’s options. If you are concerned that this could overwrite your existing DH params, consider using the `backup` option.
- The module can use the cryptography Python library, or the `openssl` executable. By default, it tries to detect which one is available. This can be overridden with the `select_crypto_backend` option.

## [Requirements](openssl_dhparam_module.md#id2)

The below requirements are needed on the host that executes this module.

- Either cryptography >= 2.0
- Or OpenSSL binary `openssl`

## [Parameters](openssl_dhparam_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **attributes**  aliases: attr  string | The attributes the resulting filesystem object should have.  To get supported flags look at the man page for *chattr* on the target system.  This string should contain the attributes in the same order as the one displayed by *lsattr*.  The `=` operator is assumed as default, otherwise `+` or `-` operators need to be included in the string. |
| **backup**  boolean | Create a backup file including a timestamp so you can get the original DH params back if you overwrote them with new ones by accident.  **Choices:**   - `false` ← (default) - `true` |
| **force**  boolean | Should the parameters be regenerated even it it already exists.  **Choices:**   - `false` ← (default) - `true` |
| **group**  string | Name of the group that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current group of the current user unless you are root, in which case it can preserve the previous ownership. |
| **mode**  any | The permissions the resulting filesystem object should have.  For those used to */usr/bin/chmod* remember that modes are actually octal numbers. You must give Ansible enough information to parse them correctly. For consistent results, quote octal numbers (for example, `'644'` or `'1777'`) so Ansible receives a string and can do its own conversion from string into number. Adding a leading zero (for example, `0755`) works sometimes, but can fail in loops and some other circumstances.  Giving Ansible a number without following either of these rules will end up with a decimal number which will have unexpected results.  As of Ansible 1.8, the mode may be specified as a symbolic mode (for example, `u+rwx` or `u=rw,g=r,o=r`).  If `mode` is not specified and the destination filesystem object **does not** exist, the default `umask` on the system will be used when setting the mode for the newly created filesystem object.  If `mode` is not specified and the destination filesystem object **does** exist, the mode of the existing filesystem object will be used.  Specifying `mode` is the best way to ensure filesystem objects are created with the correct permissions. See CVE-2020-1736 for further details. |
| **owner**  string | Name of the user that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current user unless you are root, in which case it can preserve the previous ownership.  Specifying a numeric username will be assumed to be a user ID and not a username. Avoid numeric usernames to avoid this confusion. |
| **path**  path / required | Name of the file in which the generated parameters will be saved. |
| **return_content**  boolean  *added in community.crypto 1.0.0* | If set to `true`, will return the (current or generated) DH parameter’s content as `dhparams`.  **Choices:**   - `false` ← (default) - `true` |
| **select_crypto_backend**  string  *added in community.crypto 1.0.0* | Determines which crypto backend to use.  The default choice is `auto`, which tries to use `cryptography` if available, and falls back to `openssl`.  If set to `openssl`, will try to use the OpenSSL `openssl` executable.  If set to `cryptography`, will try to use the [cryptography](https://cryptography.io/) library.  **Choices:**   - `"auto"` ← (default) - `"cryptography"` - `"openssl"` |
| **selevel**  string | The level part of the SELinux filesystem object context.  This is the MLS/MCS attribute, sometimes known as the `range`.  When set to `_default`, it will use the `level` portion of the policy if available. |
| **serole**  string | The role part of the SELinux filesystem object context.  When set to `_default`, it will use the `role` portion of the policy if available. |
| **setype**  string | The type part of the SELinux filesystem object context.  When set to `_default`, it will use the `type` portion of the policy if available. |
| **seuser**  string | The user part of the SELinux filesystem object context.  By default it uses the `system` policy, where applicable.  When set to `_default`, it will use the `user` portion of the policy if available. |
| **size**  integer | Size (in bits) of the generated DH-params.  **Default:** `4096` |
| **state**  string | Whether the parameters should exist or not, taking action if the state is different from what is stated.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **unsafe_writes**  boolean | Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target filesystem object.  By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target filesystem objects, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted filesystem objects, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.  This option allows Ansible to fall back to unsafe methods of updating filesystem objects when atomic operations fail (however, it doesn’t force Ansible to perform unsafe writes).  IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](openssl_dhparam_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |
| **safe_file_operations** | **Support:** **full** | Uses Ansible’s strict file operation functions to ensure proper permissions and avoid data corruption. |

## [See Also](openssl_dhparam_module.md#id5)

> **See also:**
>
> [community.crypto.x509_certificate](x509_certificate_module.md#ansible-collections-community-crypto-x509-certificate-module)
> :   Generate and/or check OpenSSL certificates.
>
> [community.crypto.openssl_csr](openssl_csr_module.md#ansible-collections-community-crypto-openssl-csr-module)
> :   Generate OpenSSL Certificate Signing Request (CSR).
>
> [community.crypto.openssl_pkcs12](openssl_pkcs12_module.md#ansible-collections-community-crypto-openssl-pkcs12-module)
> :   Generate OpenSSL PKCS#12 archive.
>
> [community.crypto.openssl_privatekey](openssl_privatekey_module.md#ansible-collections-community-crypto-openssl-privatekey-module)
> :   Generate OpenSSL private keys.
>
> [community.crypto.openssl_publickey](openssl_publickey_module.md#ansible-collections-community-crypto-openssl-publickey-module)
> :   Generate an OpenSSL public key from its private key.

## [Examples](openssl_dhparam_module.md#id6)

```yaml+jinja
- name: Generate Diffie-Hellman parameters with the default size (4096 bits)
  community.crypto.openssl_dhparam:
    path: /etc/ssl/dhparams.pem

- name: Generate DH Parameters with a different size (2048 bits)
  community.crypto.openssl_dhparam:
    path: /etc/ssl/dhparams.pem
    size: 2048

- name: Force regenerate an DH parameters if they already exist
  community.crypto.openssl_dhparam:
    path: /etc/ssl/dhparams.pem
    force: true
```

## [Return Values](openssl_dhparam_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_file**  string | Name of backup file created.  **Returned:** changed and if `backup` is `true`  **Sample:** `"/path/to/dhparams.pem.2019-03-09@11:22~"` |
| **dhparams**  string  *added in community.crypto 1.0.0* | The (current or generated) DH params’ content.  **Returned:** if `state` is `present` and `return_content` is `true` |
| **filename**  string | Path to the generated Diffie-Hellman parameters.  **Returned:** changed or success  **Sample:** `"/etc/ssl/dhparams.pem"` |
| **size**  integer | Size (in bits) of the Diffie-Hellman parameters.  **Returned:** changed or success  **Sample:** `4096` |

### Authors

- Thom Wiggers (@thomwiggers)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.crypto)
- [Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-crypto)
