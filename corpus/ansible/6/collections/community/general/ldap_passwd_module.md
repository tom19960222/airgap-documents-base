---
collection: ansible
version: "6"
title: "community.general.ldap_passwd module – Set passwords in LDAP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/ldap_passwd_module.html
fetched_at: 2026-07-27T17:10:29+00:00
---
# community.general.ldap_passwd module – Set passwords in LDAP

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
> see [Requirements](ldap_passwd_module.md#ansible-collections-community-general-ldap-passwd-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.ldap_passwd`.

- [Synopsis](ldap_passwd_module.md#synopsis)
- [Requirements](ldap_passwd_module.md#requirements)
- [Parameters](ldap_passwd_module.md#parameters)
- [Notes](ldap_passwd_module.md#notes)
- [Examples](ldap_passwd_module.md#examples)
- [Return Values](ldap_passwd_module.md#return-values)

## [Synopsis](ldap_passwd_module.md#id1)

- Set a password for an LDAP entry. This module only asserts that a given password is valid for a given entry. To assert the existence of an entry, see [community.general.ldap_entry](ldap_entry_module.md#ansible-collections-community-general-ldap-entry-module).

## [Requirements](ldap_passwd_module.md#id2)

The below requirements are needed on the host that executes this module.

- python-ldap

## [Parameters](ldap_passwd_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **bind_dn**  string | A DN to bind with. If this is omitted, we’ll try a SASL bind with the EXTERNAL mechanism as default.  If this is blank, we’ll use an anonymous bind. |
| **bind_pw**  string | The password to use with *bind_dn*.  Default: `""` |
| **dn**  string / required | The DN of the entry to add or remove. |
| **passwd**  string | The (plaintext) password to be set for *dn*. |
| **referrals_chasing**  string  added in community.general 2.0.0 | Set the referrals chasing behavior.  `anonymous` follow referrals anonymously. This is the default behavior.  `disabled` disable referrals chasing. This sets `OPT_REFERRALS` to off.  Choices:   - `"disabled"` - `"anonymous"` ← (default) |
| **sasl_class**  string  added in community.general 2.0.0 | The class to use for SASL authentication.  possible choices are `external`, `gssapi`.  Choices:   - `"external"` ← (default) - `"gssapi"` |
| **server_uri**  string | The *server_uri* parameter may be a comma- or whitespace-separated list of URIs containing only the schema, the host, and the port fields.  The default value lets the underlying LDAP client library look for a UNIX domain socket in its default location.  Note that when using multiple URIs you cannot determine to which URI your client gets connected.  For URIs containing additional fields, particularly when using commas, behavior is undefined.  Default: `"ldapi:///"` |
| **start_tls**  boolean | If true, we’ll use the START_TLS LDAP extension.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | If set to `false`, SSL certificates will not be validated.  This should only be used on sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](ldap_passwd_module.md#id4)

> **Note:**
>
> - The default authentication settings will attempt to use a SASL EXTERNAL bind over a UNIX domain socket. This works well with the default Ubuntu install for example, which includes a cn=peercred,cn=external,cn=auth ACL rule allowing root to modify the server configuration. If you need to use a simple bind to access your server, pass the credentials in *bind_dn* and *bind_pw*.

## [Examples](ldap_passwd_module.md#id5)

```yaml+jinja
- name: Set a password for the admin user
  community.general.ldap_passwd:
    dn: cn=admin,dc=example,dc=com
    passwd: "{{ vault_secret }}"

- name: Setting passwords in bulk
  community.general.ldap_passwd:
    dn: "{{ item.key }}"
    passwd: "{{ item.value }}"
  with_dict:
    alice: alice123123
    bob:   "|30b!"
    admin: "{{ vault_secret }}"
```

## [Return Values](ldap_passwd_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **modlist**  list / elements=string | list of modified parameters  Returned: success  Sample: `[[2, "olcRootDN", ["cn=root,dc=example,dc=com"]]]` |

### Authors

- Keller Fuchs (@KellerFuchs)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
