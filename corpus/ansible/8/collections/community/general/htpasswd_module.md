---
collection: ansible
version: "8"
title: "community.general.htpasswd module – Manage user files for basic authentication"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/htpasswd_module.html
fetched_at: 2026-07-28T01:46:06+00:00
---
# community.general.htpasswd module – Manage user files for basic authentication

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
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
- [Attributes](htpasswd_module.md#attributes)
- [Notes](htpasswd_module.md#notes)
- [Examples](htpasswd_module.md#examples)

## [Synopsis](htpasswd_module.md#id1)

- Add and remove username/password entries in a password file using htpasswd.
- This is used by web servers such as Apache and Nginx for basic authentication.

Aliases: web_infrastructure.htpasswd

## [Requirements](htpasswd_module.md#id2)

The below requirements are needed on the host that executes this module.

- passlib>=1.6

## [Parameters](htpasswd_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **attributes**  aliases: attr  string | The attributes the resulting filesystem object should have.  To get supported flags look at the man page for *chattr* on the target system.  This string should contain the attributes in the same order as the one displayed by *lsattr*.  The `=` operator is assumed as default, otherwise `+` or `-` operators need to be included in the string. |
| **create**  boolean | Used with `state=present`. If `true`, the file will be created if it does not exist. Conversely, if set to `false` and the file does not exist it will fail.  **Choices:**   - `false` - `true` ← (default) |
| **group**  string | Name of the group that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current group of the current user unless you are root, in which case it can preserve the previous ownership. |
| **hash_scheme**  aliases: crypt_scheme  string | Hashing scheme to be used. As well as the four choices listed here, you can also use any other hash supported by passlib, such as `portable_apache22` and `host_apache24`; or `md5_crypt` and `sha256_crypt`, which are Linux passwd hashes. Only some schemes in addition to the four choices below will be compatible with Apache or Nginx, and supported schemes depend on passlib version and its dependencies.  See <https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtpasswdFile> parameter `default_scheme`.  Some of the available choices might be: `apr_md5_crypt`, `des_crypt`, `ldap_sha1`, `plaintext`.  **Default:** `"apr_md5_crypt"` |
| **mode**  any | The permissions the resulting filesystem object should have.  For those used to */usr/bin/chmod* remember that modes are actually octal numbers. You must give Ansible enough information to parse them correctly. For consistent results, quote octal numbers (for example, `'644'` or `'1777'`) so Ansible receives a string and can do its own conversion from string into number. Adding a leading zero (for example, `0755`) works sometimes, but can fail in loops and some other circumstances.  Giving Ansible a number without following either of these rules will end up with a decimal number which will have unexpected results.  As of Ansible 1.8, the mode may be specified as a symbolic mode (for example, `u+rwx` or `u=rw,g=r,o=r`).  If `mode` is not specified and the destination filesystem object **does not** exist, the default `umask` on the system will be used when setting the mode for the newly created filesystem object.  If `mode` is not specified and the destination filesystem object **does** exist, the mode of the existing filesystem object will be used.  Specifying `mode` is the best way to ensure filesystem objects are created with the correct permissions. See CVE-2020-1736 for further details. |
| **name**  aliases: username  string / required | User name to add or remove. |
| **owner**  string | Name of the user that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current user unless you are root, in which case it can preserve the previous ownership.  Specifying a numeric username will be assumed to be a user ID and not a username. Avoid numeric usernames to avoid this confusion. |
| **password**  string | Password associated with user.  Must be specified if user does not exist yet. |
| **path**  aliases: dest, destfile  path / required | Path to the file that contains the usernames and passwords. |
| **selevel**  string | The level part of the SELinux filesystem object context.  This is the MLS/MCS attribute, sometimes known as the `range`.  When set to `_default`, it will use the `level` portion of the policy if available. |
| **serole**  string | The role part of the SELinux filesystem object context.  When set to `_default`, it will use the `role` portion of the policy if available. |
| **setype**  string | The type part of the SELinux filesystem object context.  When set to `_default`, it will use the `type` portion of the policy if available. |
| **seuser**  string | The user part of the SELinux filesystem object context.  By default it uses the `system` policy, where applicable.  When set to `_default`, it will use the `user` portion of the policy if available. |
| **state**  string | Whether the user entry should be present or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **unsafe_writes**  boolean | Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target filesystem object.  By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target filesystem objects, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted filesystem objects, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.  This option allows Ansible to fall back to unsafe methods of updating filesystem objects when atomic operations fail (however, it doesn’t force Ansible to perform unsafe writes).  IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](htpasswd_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](htpasswd_module.md#id5)

> **Note:**
>
> - This module depends on the `passlib` Python library, which needs to be installed on all target systems.
> - On Debian, Ubuntu, or Fedora: install `python-passlib`.
> - On RHEL or CentOS: Enable EPEL, then install `python-passlib`.

## [Examples](htpasswd_module.md#id6)

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
    hash_scheme: md5_crypt
```

### Authors

- Ansible Core Team

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
