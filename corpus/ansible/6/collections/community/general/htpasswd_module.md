---
collection: ansible
version: "6"
title: "community.general.htpasswd module – Manage user files for basic authentication"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/htpasswd_module.html
fetched_at: 2026-07-27T17:09:23+00:00
---
# community.general.htpasswd module – Manage user files for basic authentication

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
> see [Requirements](htpasswd_module.md#ansible-collections-community-general-htpasswd-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.htpasswd`.

- [Synopsis](htpasswd_module.md#synopsis)
- [Requirements](htpasswd_module.md#requirements)
- [Parameters](htpasswd_module.md#parameters)
- [Notes](htpasswd_module.md#notes)
- [Examples](htpasswd_module.md#examples)

## [Synopsis](htpasswd_module.md#id1)

- Add and remove username/password entries in a password file using htpasswd.
- This is used by web servers such as Apache and Nginx for basic authentication.

## [Requirements](htpasswd_module.md#id2)

The below requirements are needed on the host that executes this module.

- passlib>=1.6

## [Parameters](htpasswd_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **attributes**  aliases: attr  string | The attributes the resulting filesystem object should have.  To get supported flags look at the man page for *chattr* on the target system.  This string should contain the attributes in the same order as the one displayed by *lsattr*.  The `=` operator is assumed as default, otherwise `+` or `-` operators need to be included in the string. |
| **create**  boolean | Used with *state=present*. If specified, the file will be created if it does not already exist. If set to `false`, will fail if the file does not exist  Choices:   - `false` - `true` ← (default) |
| **crypt_scheme**  string | Encryption scheme to be used. As well as the four choices listed here, you can also use any other hash supported by passlib, such as md5_crypt and sha256_crypt, which are linux passwd hashes. If you do so the password file will not be compatible with Apache or Nginx  Some of the available choices might be: `apr_md5_crypt`, `des_crypt`, `ldap_sha1`, `plaintext`  Default: `"apr_md5_crypt"` |
| **group**  string | Name of the group that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current group of the current user unless you are root, in which case it can preserve the previous ownership. |
| **mode**  any | The permissions the resulting filesystem object should have.  For those used to */usr/bin/chmod* remember that modes are actually octal numbers. You must either add a leading zero so that Ansible’s YAML parser knows it is an octal number (like `0644` or `01777`) or quote it (like `'644'` or `'1777'`) so Ansible receives a string and can do its own conversion from string into number.  Giving Ansible a number without following one of these rules will end up with a decimal number which will have unexpected results.  As of Ansible 1.8, the mode may be specified as a symbolic mode (for example, `u+rwx` or `u=rw,g=r,o=r`).  If `mode` is not specified and the destination filesystem object **does not** exist, the default `umask` on the system will be used when setting the mode for the newly created filesystem object.  If `mode` is not specified and the destination filesystem object **does** exist, the mode of the existing filesystem object will be used.  Specifying `mode` is the best way to ensure filesystem objects are created with the correct permissions. See CVE-2020-1736 for further details. |
| **name**  aliases: username  string / required | User name to add or remove |
| **owner**  string | Name of the user that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current user unless you are root, in which case it can preserve the previous ownership. |
| **password**  string | Password associated with user.  Must be specified if user does not exist yet. |
| **path**  aliases: dest, destfile  path / required | Path to the file that contains the usernames and passwords |
| **selevel**  string | The level part of the SELinux filesystem object context.  This is the MLS/MCS attribute, sometimes known as the `range`.  When set to `_default`, it will use the `level` portion of the policy if available. |
| **serole**  string | The role part of the SELinux filesystem object context.  When set to `_default`, it will use the `role` portion of the policy if available. |
| **setype**  string | The type part of the SELinux filesystem object context.  When set to `_default`, it will use the `type` portion of the policy if available. |
| **seuser**  string | The user part of the SELinux filesystem object context.  By default it uses the `system` policy, where applicable.  When set to `_default`, it will use the `user` portion of the policy if available. |
| **state**  string | Whether the user entry should be present or not  Choices:   - `"present"` ← (default) - `"absent"` |
| **unsafe_writes**  boolean | Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target filesystem object.  By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target filesystem objects, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted filesystem objects, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.  This option allows Ansible to fall back to unsafe methods of updating filesystem objects when atomic operations fail (however, it doesn’t force Ansible to perform unsafe writes).  IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.  Choices:   - `false` ← (default) - `true` |

## [Notes](htpasswd_module.md#id4)

> **Note:**
>
> - This module depends on the *passlib* Python library, which needs to be installed on all target systems.
> - On Debian, Ubuntu, or Fedora: install *python-passlib*.
> - On RHEL or CentOS: Enable EPEL, then install *python-passlib*.

## [Examples](htpasswd_module.md#id5)

```yaml+jinja
- name: Add a user to a password file and ensure permissions are set
  community.general.htpasswd:
    path: /etc/nginx/passwdfile
    name: janedoe
    password: '9s36?;fyNp'
    owner: root
    group: www-data
    mode: 0640

- name: Remove a user from a password file
  community.general.htpasswd:
    path: /etc/apache2/passwdfile
    name: foobar
    state: absent

- name: Add a user to a password file suitable for use by libpam-pwdfile
  community.general.htpasswd:
    path: /etc/mail/passwords
    name: alex
    password: oedu2eGh
    crypt_scheme: md5_crypt
```

### Authors

- Ansible Core Team

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
