---
collection: ansible
version: "6"
title: "community.crypto.openssh_cert module – Generate OpenSSH host or user certificates."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/crypto/openssh_cert_module.html
fetched_at: 2026-07-27T17:06:19+00:00
---
# community.crypto.openssh_cert module – Generate OpenSSH host or user certificates.

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
> see [Requirements](openssh_cert_module.md#ansible-collections-community-crypto-openssh-cert-module-requirements) for details.
>
> To use it in a playbook, specify: `community.crypto.openssh_cert`.

- [Synopsis](openssh_cert_module.md#synopsis)
- [Requirements](openssh_cert_module.md#requirements)
- [Parameters](openssh_cert_module.md#parameters)
- [Attributes](openssh_cert_module.md#attributes)
- [Examples](openssh_cert_module.md#examples)
- [Return Values](openssh_cert_module.md#return-values)

## [Synopsis](openssh_cert_module.md#id1)

- Generate and regenerate OpenSSH host or user certificates.

## [Requirements](openssh_cert_module.md#id2)

The below requirements are needed on the host that executes this module.

- ssh-keygen

## [Parameters](openssh_cert_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **attributes**  aliases: attr  string | The attributes the resulting filesystem object should have.  To get supported flags look at the man page for *chattr* on the target system.  This string should contain the attributes in the same order as the one displayed by *lsattr*.  The `=` operator is assumed as default, otherwise `+` or `-` operators need to be included in the string. |
| **force**  boolean | Should the certificate be regenerated even if it already exists and is valid.  Equivalent to *regenerate=always*.  Choices:   - `false` ← (default) - `true` |
| **group**  string | Name of the group that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current group of the current user unless you are root, in which case it can preserve the previous ownership. |
| **identifier**  string | Specify the key identity when signing a public key. The identifier that is logged by the server when the certificate is used for authentication. |
| **ignore_timestamps**  boolean  added in community.crypto 2.2.0 | Whether the *valid_from* and *valid_to* timestamps should be ignored for idempotency checks.  However, the values will still be applied to a new certificate if it meets any other necessary conditions for generation/regeneration.  Choices:   - `false` ← (default) - `true` |
| **mode**  any | The permissions the resulting filesystem object should have.  For those used to */usr/bin/chmod* remember that modes are actually octal numbers. You must either add a leading zero so that Ansible’s YAML parser knows it is an octal number (like `0644` or `01777`) or quote it (like `'644'` or `'1777'`) so Ansible receives a string and can do its own conversion from string into number.  Giving Ansible a number without following one of these rules will end up with a decimal number which will have unexpected results.  As of Ansible 1.8, the mode may be specified as a symbolic mode (for example, `u+rwx` or `u=rw,g=r,o=r`).  If `mode` is not specified and the destination filesystem object **does not** exist, the default `umask` on the system will be used when setting the mode for the newly created filesystem object.  If `mode` is not specified and the destination filesystem object **does** exist, the mode of the existing filesystem object will be used.  Specifying `mode` is the best way to ensure filesystem objects are created with the correct permissions. See CVE-2020-1736 for further details. |
| **options**  list / elements=string | Specify certificate options when signing a key. The option that are valid for user certificates are:  `clear`: Clear all enabled permissions. This is useful for clearing the default set of permissions so permissions may be added individually.  `force-command=command`: Forces the execution of command instead of any shell or command specified by the user when the certificate is used for authentication.  `no-agent-forwarding`: Disable ssh-agent forwarding (permitted by default).  `no-port-forwarding`: Disable port forwarding (permitted by default).  `no-pty`: Disable PTY allocation (permitted by default).  `no-user-rc`: Disable execution of `~/.ssh/rc` by sshd (permitted by default).  `no-x11-forwarding`: Disable X11 forwarding (permitted by default)  `permit-agent-forwarding`: Allows ssh-agent forwarding.  `permit-port-forwarding`: Allows port forwarding.  `permit-pty`: Allows PTY allocation.  `permit-user-rc`: Allows execution of `~/.ssh/rc` by sshd.  `permit-x11-forwarding`: Allows X11 forwarding.  `source-address=address_list`: Restrict the source addresses from which the certificate is considered valid. The `address_list` is a comma-separated list of one or more address/netmask pairs in CIDR format.  At present, no options are valid for host keys. |
| **owner**  string | Name of the user that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current user unless you are root, in which case it can preserve the previous ownership. |
| **path**  path / required | Path of the file containing the certificate. |
| **pkcs11_provider**  string  added in community.crypto 1.1.0 | To use a signing key that resides on a PKCS#11 token, set this to the name (or full path) of the shared library to use with the token. Usually `libpkcs11.so`.  If this is set, *signing_key* needs to point to a file containing the public key of the CA. |
| **principals**  list / elements=string | Certificates may be limited to be valid for a set of principal (user/host) names. By default, generated certificates are valid for all users or hosts. |
| **public_key**  path | The path to the public key that will be signed with the signing key in order to generate the certificate.  Required if *state* is `present`. |
| **regenerate**  string  added in community.crypto 1.8.0 | When `never` the task will fail if a certificate already exists at *path* and is unreadable otherwise a new certificate will only be generated if there is no existing certificate.  When `fail` the task will fail if a certificate already exists at *path* and does not match the module’s options.  When `partial_idempotence` an existing certificate will be regenerated based on *serial*, *signature_algorithm*, *type*, *valid_from*, *valid_to*, *valid_at*, and *principals*. *valid_from* and *valid_to* can be excluded by *ignore_timestamps=true*.  When `full_idempotence` *identifier*, *options*, *public_key*, and *signing_key* are also considered when compared against an existing certificate.  `always` is equivalent to *force=true*.  Choices:   - `"never"` - `"fail"` - `"partial_idempotence"` ← (default) - `"full_idempotence"` - `"always"` |
| **selevel**  string | The level part of the SELinux filesystem object context.  This is the MLS/MCS attribute, sometimes known as the `range`.  When set to `_default`, it will use the `level` portion of the policy if available. |
| **serial_number**  integer | Specify the certificate serial number. The serial number is logged by the server when the certificate is used for authentication. The certificate serial number may be used in a KeyRevocationList. The serial number may be omitted for checks, but must be specified again for a new certificate. Note: The default value set by ssh-keygen is 0. |
| **serole**  string | The role part of the SELinux filesystem object context.  When set to `_default`, it will use the `role` portion of the policy if available. |
| **setype**  string | The type part of the SELinux filesystem object context.  When set to `_default`, it will use the `type` portion of the policy if available. |
| **seuser**  string | The user part of the SELinux filesystem object context.  By default it uses the `system` policy, where applicable.  When set to `_default`, it will use the `user` portion of the policy if available. |
| **signature_algorithm**  string  added in community.crypto 1.10.0 | As of OpenSSH 8.2 the SHA-1 signature algorithm for RSA keys has been disabled and `ssh` will refuse host certificates signed with the SHA-1 algorithm. OpenSSH 8.1 made `rsa-sha2-512` the default algorithm when acting as a CA and signing certificates with a RSA key. However, for OpenSSH versions less than 8.1 the SHA-2 signature algorithms, `rsa-sha2-256` or `rsa-sha2-512`, must be specified using this option if compatibility with newer `ssh` clients is required. Conversely if hosts using OpenSSH version 8.2 or greater must remain compatible with `ssh` clients using OpenSSH less than 7.2, then `ssh-rsa` can be used when generating host certificates (a corresponding change to the sshd_config to add `ssh-rsa` to the `CASignatureAlgorithms` keyword is also required).  Using any value for this option with a non-RSA *signing_key* will cause this module to fail.  Note: OpenSSH versions prior to 7.2 do not support SHA-2 signature algorithms for RSA keys and OpenSSH versions prior to 7.3 do not support SHA-2 signature algorithms for certificates.  See <https://www.openssh.com/txt/release-8.2> for more information.  Choices:   - `"ssh-rsa"` - `"rsa-sha2-256"` - `"rsa-sha2-512"` |
| **signing_key**  path | The path to the private openssh key that is used for signing the public key in order to generate the certificate.  If the private key is on a PKCS#11 token (*pkcs11_provider*), set this to the path to the public key instead.  Required if *state* is `present`. |
| **state**  string | Whether the host or user certificate should exist or not, taking action if the state is different from what is stated.  Choices:   - `"present"` ← (default) - `"absent"` |
| **type**  string | Whether the module should generate a host or a user certificate.  Required if *state* is `present`.  Choices:   - `"host"` - `"user"` |
| **unsafe_writes**  boolean | Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target filesystem object.  By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target filesystem objects, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted filesystem objects, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.  This option allows Ansible to fall back to unsafe methods of updating filesystem objects when atomic operations fail (however, it doesn’t force Ansible to perform unsafe writes).  IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.  Choices:   - `false` ← (default) - `true` |
| **use_agent**  boolean  added in community.crypto 1.3.0 | Should the ssh-keygen use a CA key residing in a ssh-agent.  Choices:   - `false` ← (default) - `true` |
| **valid_at**  string | Check if the certificate is valid at a certain point in time. If it is not the certificate will be regenerated. Time will always be interpreted as UTC. Mainly to be used with relative timespec for *valid_from* and / or *valid_to*. Note that if using relative time this module is NOT idempotent. |
| **valid_from**  string | The point in time the certificate is valid from. Time can be specified either as relative time or as absolute timestamp. Time will always be interpreted as UTC. Valid formats are: `[+-]timespec | YYYY-MM-DD | YYYY-MM-DDTHH:MM:SS | YYYY-MM-DD HH:MM:SS | always` where timespec can be an integer + `[w | d | h | m | s]` (for example `+32w1d2h`). Note that if using relative time this module is NOT idempotent.  The value `always` is only supported for OpenSSH 7.7 and greater, however, the value `1970-01-01T00:00:01` can be used with earlier versions as an equivalent expression.  To ignore this value during comparison with an existing certificate set *ignore_timestamps=true*.  Required if *state* is `present`. |
| **valid_to**  string | The point in time the certificate is valid to. Time can be specified either as relative time or as absolute timestamp. Time will always be interpreted as UTC. Valid formats are: `[+-]timespec | YYYY-MM-DD | YYYY-MM-DDTHH:MM:SS | YYYY-MM-DD HH:MM:SS | forever` where timespec can be an integer + `[w | d | h | m | s]` (for example `+32w1d2h`). Note that if using relative time this module is NOT idempotent.  To ignore this value during comparison with an existing certificate set *ignore_timestamps=true*.  Required if *state* is `present`. |

## [Attributes](openssh_cert_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support: full | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |
| **safe_file_operations** | Support: full | Uses Ansible’s strict file operation functions to ensure proper permissions and avoid data corruption. |

## [Examples](openssh_cert_module.md#id5)

```yaml+jinja
- name: Generate an OpenSSH user certificate that is valid forever and for all users
  community.crypto.openssh_cert:
    type: user
    signing_key: /path/to/private_key
    public_key: /path/to/public_key.pub
    path: /path/to/certificate
    valid_from: always
    valid_to: forever

# Generate an OpenSSH host certificate that is valid for 32 weeks from now and will be regenerated
# if it is valid for less than 2 weeks from the time the module is being run
- name: Generate an OpenSSH host certificate with valid_from, valid_to and valid_at parameters
  community.crypto.openssh_cert:
    type: host
    signing_key: /path/to/private_key
    public_key: /path/to/public_key.pub
    path: /path/to/certificate
    valid_from: +0s
    valid_to: +32w
    valid_at: +2w
    ignore_timestamps: true

- name: Generate an OpenSSH host certificate that is valid forever and only for example.com and examplehost
  community.crypto.openssh_cert:
    type: host
    signing_key: /path/to/private_key
    public_key: /path/to/public_key.pub
    path: /path/to/certificate
    valid_from: always
    valid_to: forever
    principals:
        - example.com
        - examplehost

- name: Generate an OpenSSH host Certificate that is valid from 21.1.2001 to 21.1.2019
  community.crypto.openssh_cert:
    type: host
    signing_key: /path/to/private_key
    public_key: /path/to/public_key.pub
    path: /path/to/certificate
    valid_from: "2001-01-21"
    valid_to: "2019-01-21"

- name: Generate an OpenSSH user Certificate with clear and force-command option
  community.crypto.openssh_cert:
    type: user
    signing_key: /path/to/private_key
    public_key: /path/to/public_key.pub
    path: /path/to/certificate
    valid_from: always
    valid_to: forever
    options:
        - "clear"
        - "force-command=/tmp/bla/foo"

- name: Generate an OpenSSH user certificate using a PKCS#11 token
  community.crypto.openssh_cert:
    type: user
    signing_key: /path/to/ca_public_key.pub
    pkcs11_provider: libpkcs11.so
    public_key: /path/to/public_key.pub
    path: /path/to/certificate
    valid_from: always
    valid_to: forever
```

## [Return Values](openssh_cert_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **filename**  string | path to the certificate  Returned: changed or success  Sample: `"/tmp/certificate-cert.pub"` |
| **info**  list / elements=string | Information about the certificate. Output of `ssh-keygen -L -f`.  Returned: change or success |
| **type**  string | type of the certificate (host or user)  Returned: changed or success  Sample: `"host"` |

### Authors

- David Kainz (@lolcube)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.crypto)
[Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-crypto)
