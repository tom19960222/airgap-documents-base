---
collection: ansible
version: "8"
title: "community.crypto.openssl_pkcs12 module – Generate OpenSSL PKCS#12 archive"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/crypto/openssl_pkcs12_module.html
fetched_at: 2026-07-28T01:42:33+00:00
---
# community.crypto.openssl_pkcs12 module – Generate OpenSSL PKCS#12 archive

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
> see [Requirements](openssl_pkcs12_module.md#ansible-collections-community-crypto-openssl-pkcs12-module-requirements) for details.
>
> To use it in a playbook, specify: `community.crypto.openssl_pkcs12`.

- [Synopsis](openssl_pkcs12_module.md#synopsis)
- [Requirements](openssl_pkcs12_module.md#requirements)
- [Parameters](openssl_pkcs12_module.md#parameters)
- [Attributes](openssl_pkcs12_module.md#attributes)
- [See Also](openssl_pkcs12_module.md#see-also)
- [Examples](openssl_pkcs12_module.md#examples)
- [Return Values](openssl_pkcs12_module.md#return-values)

## [Synopsis](openssl_pkcs12_module.md#id1)

- This module allows one to (re-)generate PKCS#12.
- The module can use the cryptography Python library, or the pyOpenSSL Python library. By default, it tries to detect which one is available, assuming none of the `iter_size` and `maciter_size` options are used. This can be overridden with the `select_crypto_backend` option.

## [Requirements](openssl_pkcs12_module.md#id2)

The below requirements are needed on the host that executes this module.

- PyOpenSSL >= 0.15, < 23.3.0 or cryptography >= 3.0

## [Parameters](openssl_pkcs12_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **action**  string | `export` or `parse` a PKCS#12.  **Choices:**   - `"export"` ← (default) - `"parse"` |
| **attributes**  aliases: attr  string | The attributes the resulting filesystem object should have.  To get supported flags look at the man page for *chattr* on the target system.  This string should contain the attributes in the same order as the one displayed by *lsattr*.  The `=` operator is assumed as default, otherwise `+` or `-` operators need to be included in the string. |
| **backup**  boolean | Create a backup file including a timestamp so you can get the original output file back if you overwrote it with a new one by accident.  **Choices:**   - `false` ← (default) - `true` |
| **certificate_path**  path | The path to read certificates and private keys from.  Must be in PEM format. |
| **encryption_level**  string  *added in community.crypto 2.8.0* | Determines the encryption level used.  `auto` uses the default of the selected backend. For `cryptography`, this is what the cryptography library’s specific version considers the best available encryption.  `compatibility2022` uses compatibility settings for older software in 2022. This is only supported by the `cryptography` backend if cryptography >= 38.0.0 is available.  **Note** that this option is **not used for idempotency**.  **Choices:**   - `"auto"` ← (default) - `"compatibility2022"` |
| **force**  boolean | Should the file be regenerated even if it already exists.  **Choices:**   - `false` ← (default) - `true` |
| **friendly_name**  aliases: name  string | Specifies the friendly name for the certificate and private key. |
| **group**  string | Name of the group that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current group of the current user unless you are root, in which case it can preserve the previous ownership. |
| **iter_size**  integer | Number of times to repeat the encryption step.  This is **not considered during idempotency checks**.  This is only used by the `pyopenssl` backend, or when `encryption_level=compatibility2022`.  When using it, the default is `2048` for `pyopenssl` and `50000` for `cryptography`. |
| **maciter_size**  integer | Number of times to repeat the MAC step.  This is **not considered during idempotency checks**.  This is only used by the `pyopenssl` backend. When using it, the default is `1`. |
| **mode**  any | The permissions the resulting filesystem object should have.  For those used to */usr/bin/chmod* remember that modes are actually octal numbers. You must give Ansible enough information to parse them correctly. For consistent results, quote octal numbers (for example, `'644'` or `'1777'`) so Ansible receives a string and can do its own conversion from string into number. Adding a leading zero (for example, `0755`) works sometimes, but can fail in loops and some other circumstances.  Giving Ansible a number without following either of these rules will end up with a decimal number which will have unexpected results.  As of Ansible 1.8, the mode may be specified as a symbolic mode (for example, `u+rwx` or `u=rw,g=r,o=r`).  If `mode` is not specified and the destination filesystem object **does not** exist, the default `umask` on the system will be used when setting the mode for the newly created filesystem object.  If `mode` is not specified and the destination filesystem object **does** exist, the mode of the existing filesystem object will be used.  Specifying `mode` is the best way to ensure filesystem objects are created with the correct permissions. See CVE-2020-1736 for further details. |
| **other_certificates**  aliases: ca_certificates  list / elements=path | List of other certificates to include. Pre Ansible 2.8 this parameter was called `ca_certificates`.  Assumes there is one PEM-encoded certificate per file. If a file contains multiple PEM certificates, set `other_certificates_parse_all` to `true`. |
| **other_certificates_parse_all**  boolean  *added in community.crypto 1.4.0* | If set to `true`, assumes that the files mentioned in `other_certificates` can contain more than one certificate per file (or even none per file).  **Choices:**   - `false` ← (default) - `true` |
| **owner**  string | Name of the user that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current user unless you are root, in which case it can preserve the previous ownership.  Specifying a numeric username will be assumed to be a user ID and not a username. Avoid numeric usernames to avoid this confusion. |
| **passphrase**  string | The PKCS#12 password.  **Note:** PKCS12 encryption is not secure and should not be used as a security mechanism. If you need to store or send a PKCS12 file safely, you should additionally encrypt it with something else. |
| **path**  path / required | Filename to write the PKCS#12 file to. |
| **privatekey_content**  string  *added in community.crypto 2.3.0* | Content of the private key file.  Mutually exclusive with `privatekey_path`. |
| **privatekey_passphrase**  string | Passphrase source to decrypt any input private keys with. |
| **privatekey_path**  path | File to read private key from.  Mutually exclusive with `privatekey_content`. |
| **return_content**  boolean  *added in community.crypto 1.0.0* | If set to `true`, will return the (current or generated) PKCS#12’s content as `pkcs12`.  **Choices:**   - `false` ← (default) - `true` |
| **select_crypto_backend**  string  *added in community.crypto 1.7.0* | Determines which crypto backend to use.  The default choice is `auto`, which tries to use `cryptography` if available, and falls back to `pyopenssl`. If `iter_size` is used together with `encryption_level` is not `compatibility2022`, or if `maciter_size` is used, `auto` will always result in `pyopenssl` to be chosen for backwards compatibility.  If set to `pyopenssl`, will try to use the [pyOpenSSL](https://pypi.org/project/pyOpenSSL/) library.  If set to `cryptography`, will try to use the [cryptography](https://cryptography.io/) library.  **Choices:**   - `"auto"` ← (default) - `"cryptography"` - `"pyopenssl"` |
| **selevel**  string | The level part of the SELinux filesystem object context.  This is the MLS/MCS attribute, sometimes known as the `range`.  When set to `_default`, it will use the `level` portion of the policy if available. |
| **serole**  string | The role part of the SELinux filesystem object context.  When set to `_default`, it will use the `role` portion of the policy if available. |
| **setype**  string | The type part of the SELinux filesystem object context.  When set to `_default`, it will use the `type` portion of the policy if available. |
| **seuser**  string | The user part of the SELinux filesystem object context.  By default it uses the `system` policy, where applicable.  When set to `_default`, it will use the `user` portion of the policy if available. |
| **src**  path | PKCS#12 file path to parse. |
| **state**  string | Whether the file should exist or not. All parameters except `path` are ignored when state is `absent`.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **unsafe_writes**  boolean | Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target filesystem object.  By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target filesystem objects, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted filesystem objects, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.  This option allows Ansible to fall back to unsafe methods of updating filesystem objects when atomic operations fail (however, it doesn’t force Ansible to perform unsafe writes).  IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](openssl_pkcs12_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |
| **safe_file_operations** | **Support:** **full** | Uses Ansible’s strict file operation functions to ensure proper permissions and avoid data corruption. |

## [See Also](openssl_pkcs12_module.md#id5)

> **See also:**
>
> [community.crypto.x509_certificate](x509_certificate_module.md#ansible-collections-community-crypto-x509-certificate-module)
> :   Generate and/or check OpenSSL certificates.
>
> [community.crypto.openssl_csr](openssl_csr_module.md#ansible-collections-community-crypto-openssl-csr-module)
> :   Generate OpenSSL Certificate Signing Request (CSR).
>
> [community.crypto.openssl_dhparam](openssl_dhparam_module.md#ansible-collections-community-crypto-openssl-dhparam-module)
> :   Generate OpenSSL Diffie-Hellman Parameters.
>
> [community.crypto.openssl_privatekey](openssl_privatekey_module.md#ansible-collections-community-crypto-openssl-privatekey-module)
> :   Generate OpenSSL private keys.
>
> [community.crypto.openssl_publickey](openssl_publickey_module.md#ansible-collections-community-crypto-openssl-publickey-module)
> :   Generate an OpenSSL public key from its private key.

## [Examples](openssl_pkcs12_module.md#id6)

```yaml+jinja
- name: Generate PKCS#12 file
  community.crypto.openssl_pkcs12:
    action: export
    path: /opt/certs/ansible.p12
    friendly_name: raclette
    privatekey_path: /opt/certs/keys/key.pem
    certificate_path: /opt/certs/cert.pem
    other_certificates: /opt/certs/ca.pem
    # Note that if /opt/certs/ca.pem contains multiple certificates,
    # only the first one will be used. See the other_certificates_parse_all
    # option for changing this behavior.
    state: present

- name: Generate PKCS#12 file
  community.crypto.openssl_pkcs12:
    action: export
    path: /opt/certs/ansible.p12
    friendly_name: raclette
    privatekey_content: '{{ private_key_contents }}'
    certificate_path: /opt/certs/cert.pem
    other_certificates_parse_all: true
    other_certificates:
      - /opt/certs/ca_bundle.pem
        # Since we set other_certificates_parse_all to true, all
        # certificates in the CA bundle are included and not just
        # the first one.
      - /opt/certs/intermediate.pem
        # In case this file has multiple certificates in it,
        # all will be included as well.
    state: present

- name: Change PKCS#12 file permission
  community.crypto.openssl_pkcs12:
    action: export
    path: /opt/certs/ansible.p12
    friendly_name: raclette
    privatekey_path: /opt/certs/keys/key.pem
    certificate_path: /opt/certs/cert.pem
    other_certificates: /opt/certs/ca.pem
    state: present
    mode: '0600'

- name: Regen PKCS#12 file
  community.crypto.openssl_pkcs12:
    action: export
    src: /opt/certs/ansible.p12
    path: /opt/certs/ansible.p12
    friendly_name: raclette
    privatekey_path: /opt/certs/keys/key.pem
    certificate_path: /opt/certs/cert.pem
    other_certificates: /opt/certs/ca.pem
    state: present
    mode: '0600'
    force: true

- name: Dump/Parse PKCS#12 file
  community.crypto.openssl_pkcs12:
    action: parse
    src: /opt/certs/ansible.p12
    path: /opt/certs/ansible.pem
    state: present

- name: Remove PKCS#12 file
  community.crypto.openssl_pkcs12:
    path: /opt/certs/ansible.p12
    state: absent
```

## [Return Values](openssl_pkcs12_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_file**  string | Name of backup file created.  **Returned:** changed and if `backup` is `true`  **Sample:** `"/path/to/ansible.com.pem.2019-03-09@11:22~"` |
| **filename**  string | Path to the generate PKCS#12 file.  **Returned:** changed or success  **Sample:** `"/opt/certs/ansible.p12"` |
| **pkcs12**  string  *added in community.crypto 1.0.0* | The (current or generated) PKCS#12’s content Base64 encoded.  **Returned:** if `state` is `present` and `return_content` is `true` |
| **privatekey**  string | Path to the TLS/SSL private key the public key was generated from.  **Returned:** changed or success  **Sample:** `"/etc/ssl/private/ansible.com.pem"` |

### Authors

- Guillaume Delpierre (@gdelpierre)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.crypto)
- [Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-crypto)
