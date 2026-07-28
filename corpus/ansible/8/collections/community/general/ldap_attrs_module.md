---
collection: ansible
version: "8"
title: "community.general.ldap_attrs module – Add or remove multiple LDAP attribute values"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/ldap_attrs_module.html
fetched_at: 2026-07-28T01:47:27+00:00
---
# community.general.ldap_attrs module – Add or remove multiple LDAP attribute values

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
> see [Requirements](ldap_attrs_module.md#ansible-collections-community-general-ldap-attrs-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.ldap_attrs`.

New in community.general 0.2.0

- [Synopsis](ldap_attrs_module.md#synopsis)
- [Requirements](ldap_attrs_module.md#requirements)
- [Parameters](ldap_attrs_module.md#parameters)
- [Attributes](ldap_attrs_module.md#attributes)
- [Notes](ldap_attrs_module.md#notes)
- [Examples](ldap_attrs_module.md#examples)
- [Return Values](ldap_attrs_module.md#return-values)

## [Synopsis](ldap_attrs_module.md#id1)

- Add or remove multiple LDAP attribute values.

Aliases: net_tools.ldap.ldap_attrs

## [Requirements](ldap_attrs_module.md#id2)

The below requirements are needed on the host that executes this module.

- python-ldap

## [Parameters](ldap_attrs_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **attributes**  dictionary / required | The attribute(s) and value(s) to add or remove.  Each attribute value can be a string for single-valued attributes or a list of strings for multi-valued attributes.  If you specify values for this option in YAML, please note that you can improve readability for long string values by using YAML block modifiers as seen in the examples for this module.  Note that when using values that YAML/ansible-core interprets as other types, like `yes`, `no` (booleans), or `2.10` (float), make sure to quote them if these are meant to be strings. Otherwise the wrong values may be sent to LDAP. |
| **bind_dn**  string | A DN to bind with. If this is omitted, we’ll try a SASL bind with the EXTERNAL mechanism as default.  If this is blank, we’ll use an anonymous bind. |
| **bind_pw**  string | The password to use with `bind_dn`.  **Default:** `""` |
| **ca_path**  path  *added in community.general 6.5.0* | Set the path to PEM file with CA certs. |
| **client_cert**  path  *added in community.general 7.1.0* | PEM formatted certificate chain file to be used for SSL client authentication.  Required if `client_key` is defined. |
| **client_key**  path  *added in community.general 7.1.0* | PEM formatted file that contains your private key to be used for SSL client authentication.  Required if `client_cert` is defined. |
| **dn**  string / required | The DN of the entry to add or remove. |
| **ordered**  boolean | If `true`, prepend list values with X-ORDERED index numbers in all attributes specified in the current task. This is useful mostly with `olcAccess` attribute to easily manage LDAP Access Control Lists.  **Choices:**   - `false` ← (default) - `true` |
| **referrals_chasing**  string  *added in community.general 2.0.0* | Set the referrals chasing behavior.  `anonymous` follow referrals anonymously. This is the default behavior.  `disabled` disable referrals chasing. This sets `OPT_REFERRALS` to off.  **Choices:**   - `"disabled"` - `"anonymous"` ← (default) |
| **sasl_class**  string  *added in community.general 2.0.0* | The class to use for SASL authentication.  **Choices:**   - `"external"` ← (default) - `"gssapi"` |
| **server_uri**  string | The `server_uri` parameter may be a comma- or whitespace-separated list of URIs containing only the schema, the host, and the port fields.  The default value lets the underlying LDAP client library look for a UNIX domain socket in its default location.  Note that when using multiple URIs you cannot determine to which URI your client gets connected.  For URIs containing additional fields, particularly when using commas, behavior is undefined.  **Default:** `"ldapi:///"` |
| **start_tls**  boolean | If true, we’ll use the START_TLS LDAP extension.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | The state of the attribute values. If `present`, all given attribute values will be added if they’re missing. If `absent`, all given attribute values will be removed if present. If `exact`, the set of attribute values will be forced to exactly those provided and no others. If `state=exact` and the attribute value is empty, all values for this attribute will be removed.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"exact"` |
| **validate_certs**  boolean | If set to `false`, SSL certificates will not be validated.  This should only be used on sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **xorder_discovery**  string  *added in community.general 6.4.0* | Set the behavior on how to process Xordered DNs.  `enable` will perform a `ONELEVEL` search below the superior RDN to find the matching DN.  `disable` will always use the DN unmodified (as passed by the `dn` parameter).  `auto` will only perform a search if the first RDN does not contain an index number (`{x}`).  **Choices:**   - `"enable"` - `"auto"` ← (default) - `"disable"` |

## [Attributes](ldap_attrs_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](ldap_attrs_module.md#id5)

> **Note:**
>
> - This only deals with attributes on existing entries. To add or remove whole entries, see [community.general.ldap_entry](ldap_entry_module.md#ansible-collections-community-general-ldap-entry-module).
> - The default authentication settings will attempt to use a SASL EXTERNAL bind over a UNIX domain socket. This works well with the default Ubuntu install for example, which includes a cn=peercred,cn=external,cn=auth ACL rule allowing root to modify the server configuration. If you need to use a simple bind to access your server, pass the credentials in `bind_dn` and `bind_pw`.
> - For `state=present` and `state=absent`, all value comparisons are performed on the server for maximum accuracy. For `state=exact`, values have to be compared in Python, which obviously ignores LDAP matching rules. This should work out in most cases, but it is theoretically possible to see spurious changes when target and actual values are semantically identical but lexically distinct.

## [Examples](ldap_attrs_module.md#id6)

```yaml+jinja
- name: Configure directory number 1 for example.com
  community.general.ldap_attrs:
    dn: olcDatabase={1}hdb,cn=config
    attributes:
        olcSuffix: dc=example,dc=com
    state: exact

# The complex argument format is required here to pass a list of ACL strings.
- name: Set up the ACL
  community.general.ldap_attrs:
    dn: olcDatabase={1}hdb,cn=config
    attributes:
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
    state: exact

# An alternative approach with automatic X-ORDERED numbering
- name: Set up the ACL
  community.general.ldap_attrs:
    dn: olcDatabase={1}hdb,cn=config
    attributes:
        olcAccess:
          - >-
            to attrs=userPassword,shadowLastChange
            by self write
            by anonymous auth
            by dn="cn=admin,dc=example,dc=com" write
            by * none'
          - >-
            to dn.base="dc=example,dc=com"
            by dn="cn=admin,dc=example,dc=com" write
            by * read
    ordered: true
    state: exact

- name: Declare some indexes
  community.general.ldap_attrs:
    dn: olcDatabase={1}hdb,cn=config
    attributes:
        olcDbIndex:
            - objectClass eq
            - uid eq

- name: Set up a root user, which we can use later to bootstrap the directory
  community.general.ldap_attrs:
    dn: olcDatabase={1}hdb,cn=config
    attributes:
        olcRootDN: cn=root,dc=example,dc=com
        olcRootPW: "{SSHA}tabyipcHzhwESzRaGA7oQ/SDoBZQOGND"
    state: exact

- name: Remove an attribute with a specific value
  community.general.ldap_attrs:
    dn: uid=jdoe,ou=people,dc=example,dc=com
    attributes:
        description: "An example user account"
    state: absent
    server_uri: ldap://localhost/
    bind_dn: cn=admin,dc=example,dc=com
    bind_pw: password

- name: Remove specified attribute(s) from an entry
  community.general.ldap_attrs:
    dn: uid=jdoe,ou=people,dc=example,dc=com
    attributes:
        description: []
    state: exact
    server_uri: ldap://localhost/
    bind_dn: cn=admin,dc=example,dc=com
    bind_pw: password
```

## [Return Values](ldap_attrs_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **modlist**  list / elements=string | list of modified parameters  **Returned:** success  **Sample:** `[[2, "olcRootDN", ["cn=root,dc=example,dc=com"]]]` |

### Authors

- Jiri Tyr (@jtyr)
- Alexander Korinek (@noles)
- Maciej Delmanowski (@drybjed)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
