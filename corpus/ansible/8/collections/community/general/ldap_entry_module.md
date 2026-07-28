---
collection: ansible
version: "8"
title: "community.general.ldap_entry module – Add or remove LDAP entries"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/ldap_entry_module.html
fetched_at: 2026-07-28T01:47:27+00:00
---
# community.general.ldap_entry module – Add or remove LDAP entries

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
> see [Requirements](ldap_entry_module.md#ansible-collections-community-general-ldap-entry-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.ldap_entry`.

- [Synopsis](ldap_entry_module.md#synopsis)
- [Requirements](ldap_entry_module.md#requirements)
- [Parameters](ldap_entry_module.md#parameters)
- [Attributes](ldap_entry_module.md#attributes)
- [Notes](ldap_entry_module.md#notes)
- [Examples](ldap_entry_module.md#examples)

## [Synopsis](ldap_entry_module.md#id1)

- Add or remove LDAP entries. This module only asserts the existence or non-existence of an LDAP entry, not its attributes. To assert the attribute values of an entry, see [community.general.ldap_attrs](ldap_attrs_module.md#ansible-collections-community-general-ldap-attrs-module).

Aliases: net_tools.ldap.ldap_entry

## [Requirements](ldap_entry_module.md#id2)

The below requirements are needed on the host that executes this module.

- python-ldap

## [Parameters](ldap_entry_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **attributes**  dictionary | If `state=present`, attributes necessary to create an entry. Existing entries are never modified. To assert specific attribute values on an existing entry, use [community.general.ldap_attrs](ldap_attrs_module.md#ansible-collections-community-general-ldap-attrs-module) module instead.  Each attribute value can be a string for single-valued attributes or a list of strings for multi-valued attributes.  If you specify values for this option in YAML, please note that you can improve readability for long string values by using YAML block modifiers as seen in the examples for this module.  Note that when using values that YAML/ansible-core interprets as other types, like `yes`, `no` (booleans), or `2.10` (float), make sure to quote them if these are meant to be strings. Otherwise the wrong values may be sent to LDAP.  **Default:** `{}` |
| **bind_dn**  string | A DN to bind with. If this is omitted, we’ll try a SASL bind with the EXTERNAL mechanism as default.  If this is blank, we’ll use an anonymous bind. |
| **bind_pw**  string | The password to use with `bind_dn`.  **Default:** `""` |
| **ca_path**  path  *added in community.general 6.5.0* | Set the path to PEM file with CA certs. |
| **client_cert**  path  *added in community.general 7.1.0* | PEM formatted certificate chain file to be used for SSL client authentication.  Required if `client_key` is defined. |
| **client_key**  path  *added in community.general 7.1.0* | PEM formatted file that contains your private key to be used for SSL client authentication.  Required if `client_cert` is defined. |
| **dn**  string / required | The DN of the entry to add or remove. |
| **objectClass**  list / elements=string | If `state=present`, value or list of values to use when creating the entry. It can either be a string or an actual list of strings. |
| **recursive**  boolean  *added in community.general 4.6.0* | If `state=delete`, a flag indicating whether a single entry or the whole branch must be deleted.  **Choices:**   - `false` ← (default) - `true` |
| **referrals_chasing**  string  *added in community.general 2.0.0* | Set the referrals chasing behavior.  `anonymous` follow referrals anonymously. This is the default behavior.  `disabled` disable referrals chasing. This sets `OPT_REFERRALS` to off.  **Choices:**   - `"disabled"` - `"anonymous"` ← (default) |
| **sasl_class**  string  *added in community.general 2.0.0* | The class to use for SASL authentication.  **Choices:**   - `"external"` ← (default) - `"gssapi"` |
| **server_uri**  string | The `server_uri` parameter may be a comma- or whitespace-separated list of URIs containing only the schema, the host, and the port fields.  The default value lets the underlying LDAP client library look for a UNIX domain socket in its default location.  Note that when using multiple URIs you cannot determine to which URI your client gets connected.  For URIs containing additional fields, particularly when using commas, behavior is undefined.  **Default:** `"ldapi:///"` |
| **start_tls**  boolean | If true, we’ll use the START_TLS LDAP extension.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | The target state of the entry.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | If set to `false`, SSL certificates will not be validated.  This should only be used on sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **xorder_discovery**  string  *added in community.general 6.4.0* | Set the behavior on how to process Xordered DNs.  `enable` will perform a `ONELEVEL` search below the superior RDN to find the matching DN.  `disable` will always use the DN unmodified (as passed by the `dn` parameter).  `auto` will only perform a search if the first RDN does not contain an index number (`{x}`).  **Choices:**   - `"enable"` - `"auto"` ← (default) - `"disable"` |

## [Attributes](ldap_entry_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](ldap_entry_module.md#id5)

> **Note:**
>
> - The default authentication settings will attempt to use a SASL EXTERNAL bind over a UNIX domain socket. This works well with the default Ubuntu install for example, which includes a cn=peercred,cn=external,cn=auth ACL rule allowing root to modify the server configuration. If you need to use a simple bind to access your server, pass the credentials in `bind_dn` and `bind_pw`.

## [Examples](ldap_entry_module.md#id6)

```yaml+jinja
- name: Make sure we have a parent entry for users
  community.general.ldap_entry:
    dn: ou=users,dc=example,dc=com
    objectClass: organizationalUnit

- name: Make sure we have an admin user
  community.general.ldap_entry:
    dn: cn=admin,dc=example,dc=com
    objectClass:
      - simpleSecurityObject
      - organizationalRole
    attributes:
      description: An LDAP administrator
      userPassword: "{SSHA}tabyipcHzhwESzRaGA7oQ/SDoBZQOGND"

- name: Set possible values for attributes elements
  community.general.ldap_entry:
    dn: cn=admin,dc=example,dc=com
    objectClass:
      - simpleSecurityObject
      - organizationalRole
    attributes:
      description: An LDAP Administrator
      roleOccupant:
      - cn=Chocs Puddington,ou=Information Technology,dc=example,dc=com
      - cn=Alice Stronginthebrain,ou=Information Technology,dc=example,dc=com
      olcAccess:
      - >-
        {0}to attrs=userPassword,shadowLastChange
        by self write
        by anonymous auth
        by dn="cn=admin,dc=example,dc=com" write
        by * none'
      - >-
        {1}to dn.base="dc=example,dc=com"
        by dn="cn=admin,dc=example,dc=com" write
        by * read

- name: Get rid of an old entry
  community.general.ldap_entry:
    dn: ou=stuff,dc=example,dc=com
    state: absent
    server_uri: ldap://localhost/
    bind_dn: cn=admin,dc=example,dc=com
    bind_pw: password

#
# The same as in the previous example but with the authentication details
# stored in the ldap_auth variable:
#
# ldap_auth:
#   server_uri: ldap://localhost/
#   bind_dn: cn=admin,dc=example,dc=com
#   bind_pw: password
#
# In the example below, 'args' is a task keyword, passed at the same level as the module
- name: Get rid of an old entry
  community.general.ldap_entry:
    dn: ou=stuff,dc=example,dc=com
    state: absent
  args: "{{ ldap_auth }}"
```

### Authors

- Jiri Tyr (@jtyr)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
