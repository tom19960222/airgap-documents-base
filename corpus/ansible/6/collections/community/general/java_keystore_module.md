---
collection: ansible
version: "6"
title: "community.general.java_keystore module – Create a Java keystore in JKS format"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/java_keystore_module.html
fetched_at: 2026-07-27T17:10:10+00:00
---
# community.general.java_keystore module – Create a Java keystore in JKS format

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](java_keystore_module.md#ansible-collections-community-general-java-keystore-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.java_keystore`.

- [Synopsis](java_keystore_module.md#synopsis)
- [Requirements](java_keystore_module.md#requirements)
- [Parameters](java_keystore_module.md#parameters)
- [Notes](java_keystore_module.md#notes)
- [See Also](java_keystore_module.md#see-also)
- [Examples](java_keystore_module.md#examples)
- [Return Values](java_keystore_module.md#return-values)

## [Synopsis](java_keystore_module.md#id1)

- Bundle a x509 certificate and its private key into a Java Keystore in JKS format.

## [Requirements](java_keystore_module.md#id2)

The below requirements are needed on the host that executes this module.

- openssl in PATH (when *ssl_backend=openssl*)
- keytool in PATH
- cryptography >= 3.0 (when *ssl_backend=cryptography*)

## [Parameters](java_keystore_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **attributes**  aliases: attr  string | The attributes the resulting filesystem object should have.  To get supported flags look at the man page for *chattr* on the target system.  This string should contain the attributes in the same order as the one displayed by *lsattr*.  The `=` operator is assumed as default, otherwise `+` or `-` operators need to be included in the string. |
| **certificate**  string | Content of the certificate used to create the keystore.  If the fingerprint of the provided certificate does not match the fingerprint of the certificate bundled in the keystore, the keystore is regenerated with the provided certificate.  Exactly one of *certificate* or *certificate_path* is required. |
| **certificate_path**  path  added in community.general 3.0.0 | Location of the certificate used to create the keystore.  If the fingerprint of the provided certificate does not match the fingerprint of the certificate bundled in the keystore, the keystore is regenerated with the provided certificate.  Exactly one of *certificate* or *certificate_path* is required. |
| **dest**  path / required | Absolute path of the generated keystore. |
| **force**  boolean | Keystore is created even if it already exists.  Choices:   - `false` ← (default) - `true` |
| **group**  string | Name of the group that should own jks file. |
| **keystore_type**  string  added in community.general 3.3.0 | Type of the Java keystore.  When this option is omitted and the keystore doesn’t already exist, the behavior follows `keytool`‘s default store type which depends on Java version; `pkcs12` since Java 9 and `jks` prior (may also be `pkcs12` if new default has been backported to this version).  When this option is omitted and the keystore already exists, the current type is left untouched, unless another option leads to overwrite the keystore (in that case, this option behaves like for keystore creation).  When *keystore_type* is set, the keystore is created with this type if it doesn’t already exist, or is overwritten to match the given type in case of mismatch.  Choices:   - `"jks"` - `"pkcs12"` |
| **mode**  any | Mode the file should be. |
| **name**  string / required | Name of the certificate in the keystore.  If the provided name does not exist in the keystore, the module will re-create the keystore. This behavior changed in community.general 3.0.0, before that the module would fail when the name did not match. |
| **owner**  string | Name of the user that should own jks file. |
| **password**  string / required | Password that should be used to secure the keystore.  If the provided password fails to unlock the keystore, the module will re-create the keystore with the new passphrase. This behavior changed in community.general 3.0.0, before that the module would fail when the password did not match. |
| **private_key**  string | Content of the private key used to create the keystore.  Exactly one of *private_key* or *private_key_path* is required. |
| **private_key_passphrase**  string  added in community.general 0.2.0 | Passphrase used to read the private key, if required. |
| **private_key_path**  path  added in community.general 3.0.0 | Location of the private key used to create the keystore.  Exactly one of *private_key* or *private_key_path* is required. |
| **selevel**  string | The level part of the SELinux filesystem object context.  This is the MLS/MCS attribute, sometimes known as the `range`.  When set to `_default`, it will use the `level` portion of the policy if available. |
| **serole**  string | The role part of the SELinux filesystem object context.  When set to `_default`, it will use the `role` portion of the policy if available. |
| **setype**  string | The type part of the SELinux filesystem object context.  When set to `_default`, it will use the `type` portion of the policy if available. |
| **seuser**  string | The user part of the SELinux filesystem object context.  By default it uses the `system` policy, where applicable.  When set to `_default`, it will use the `user` portion of the policy if available. |
| **ssl_backend**  string  added in community.general 3.1.0 | Backend for loading private keys and certificates.  Choices:   - `"openssl"` ← (default) - `"cryptography"` |
| **unsafe_writes**  boolean | Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target filesystem object.  By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target filesystem objects, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted filesystem objects, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.  This option allows Ansible to fall back to unsafe methods of updating filesystem objects when atomic operations fail (however, it doesn’t force Ansible to perform unsafe writes).  IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.  Choices:   - `false` ← (default) - `true` |

## [Notes](java_keystore_module.md#id4)

> **Note:**
>
> - *certificate* and *private_key* require that their contents are available on the controller (either inline in a playbook, or with the `file` lookup), while *certificate_path* and *private_key_path* require that the files are available on the target host.
> - By design, any change of a value of options *keystore_type*, *name* or *password*, as well as changes of key or certificate materials will cause the existing *dest* to be overwritten.

## [See Also](java_keystore_module.md#id5)

> **See also:**
>
> [community.crypto.openssl_pkcs12](../crypto/openssl_pkcs12_module.md#ansible-collections-community-crypto-openssl-pkcs12-module)
> :   Generate OpenSSL PKCS#12 archive.
>
> [community.general.java_cert](java_cert_module.md#ansible-collections-community-general-java-cert-module)
> :   Uses keytool to import/remove certificate to/from java keystore (cacerts).

## [Examples](java_keystore_module.md#id6)

```yaml+jinja
- name: Create a keystore for the given certificate/private key pair (inline)
  community.general.java_keystore:
    name: example
    certificate: |
      -----BEGIN CERTIFICATE-----
      h19dUZ2co2fI/ibYiwxWk4aeNE6KWvCaTQOMQ8t6Uo2XKhpL/xnjoAgh1uCQN/69
      MG+34+RhUWzCfdZH7T8/qDxJw2kEPKluaYh7KnMsba+5jHjmtzix5QIDAQABo4IB
      -----END CERTIFICATE-----
    private_key: |
      -----BEGIN RSA PRIVATE KEY-----
      DBVFTEVDVFJJQ0lURSBERSBGUkFOQ0UxFzAVBgNVBAsMDjAwMDIgNTUyMDgxMzE3
      GLlDNMw/uHyME7gHFsqJA7O11VY6O5WQ4IDP3m/s5ZV6s+Nn6Lerz17VZ99
      -----END RSA PRIVATE KEY-----
    password: changeit
    dest: /etc/security/keystore.jks

- name: Create a keystore for the given certificate/private key pair (with files on controller)
  community.general.java_keystore:
    name: example
    certificate: "{{ lookup('file', '/path/to/certificate.crt') }}"
    private_key: "{{ lookup('file', '/path/to/private.key') }}"
    password: changeit
    dest: /etc/security/keystore.jks

- name: Create a keystore for the given certificate/private key pair (with files on target host)
  community.general.java_keystore:
    name: snakeoil
    certificate_path: /etc/ssl/certs/ssl-cert-snakeoil.pem
    private_key_path: /etc/ssl/private/ssl-cert-snakeoil.key
    password: changeit
    dest: /etc/security/keystore.jks
```

## [Return Values](java_keystore_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cmd**  string | Executed command to get action done  Returned: changed and failure  Sample: `"/usr/bin/openssl x509 -noout -in /tmp/user/1000/tmp8jd_lh23 -fingerprint -sha256"` |
| **err**  string | Output from stderr of keytool/openssl command after error of given command.  Returned: failure  Sample: `"Keystore password is too short - must be at least 6 characters "` |
| **msg**  string | Output from stdout of keytool/openssl command after execution of given command or an error.  Returned: changed and failure  Sample: `"Unable to find the current certificate fingerprint in ..."` |
| **rc**  integer | keytool/openssl command execution return value  Returned: changed and failure  Sample: `0` |

### Authors

- Guillaume Grossetie (@Mogztter)
- quidame (@quidame)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
