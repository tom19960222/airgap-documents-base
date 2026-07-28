---
collection: ansible
version: "8"
title: "community.general.ldap_search module – Search for entries in a LDAP server"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/ldap_search_module.html
fetched_at: 2026-07-28T01:47:29+00:00
---
# community.general.ldap_search module – Search for entries in a LDAP server

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
> see [Requirements](ldap_search_module.md#ansible-collections-community-general-ldap-search-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.ldap_search`.

New in community.general 0.2.0

- [Synopsis](ldap_search_module.md#synopsis)
- [Requirements](ldap_search_module.md#requirements)
- [Parameters](ldap_search_module.md#parameters)
- [Attributes](ldap_search_module.md#attributes)
- [Notes](ldap_search_module.md#notes)
- [Examples](ldap_search_module.md#examples)

## [Synopsis](ldap_search_module.md#id1)

- Return the results of an LDAP search.

Aliases: net_tools.ldap.ldap_search

## [Requirements](ldap_search_module.md#id2)

The below requirements are needed on the host that executes this module.

- python-ldap

## [Parameters](ldap_search_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **attrs**  list / elements=string | A list of attributes for limiting the result. Use an actual list or a comma-separated string. |
| **base64_attributes**  list / elements=string  *added in community.general 7.0.0* | If provided, all attribute values returned that are listed in this option will be Base64 encoded.  If the special value `*` appears in this list, all attributes will be Base64 encoded.  All other attribute values will be converted to UTF-8 strings. If they contain binary data, please note that invalid UTF-8 bytes will be omitted. |
| **bind_dn**  string | A DN to bind with. If this is omitted, we’ll try a SASL bind with the EXTERNAL mechanism as default.  If this is blank, we’ll use an anonymous bind. |
| **bind_pw**  string | The password to use with `bind_dn`.  **Default:** `""` |
| **ca_path**  path  *added in community.general 6.5.0* | Set the path to PEM file with CA certs. |
| **client_cert**  path  *added in community.general 7.1.0* | PEM formatted certificate chain file to be used for SSL client authentication.  Required if `client_key` is defined. |
| **client_key**  path  *added in community.general 7.1.0* | PEM formatted file that contains your private key to be used for SSL client authentication.  Required if `client_cert` is defined. |
| **dn**  string / required | The LDAP DN to search in. |
| **filter**  string | Used for filtering the LDAP search result.  **Default:** `"(objectClass=*)"` |
| **page_size**  integer  *added in community.general 7.1.0* | The page size when performing a simple paged result search (RFC 2696). This setting can be tuned to reduce issues with timeouts and server limits.  Setting the page size to `0` (default) disables paged searching.  **Default:** `0` |
| **referrals_chasing**  string  *added in community.general 2.0.0* | Set the referrals chasing behavior.  `anonymous` follow referrals anonymously. This is the default behavior.  `disabled` disable referrals chasing. This sets `OPT_REFERRALS` to off.  **Choices:**   - `"disabled"` - `"anonymous"` ← (default) |
| **sasl_class**  string  *added in community.general 2.0.0* | The class to use for SASL authentication.  **Choices:**   - `"external"` ← (default) - `"gssapi"` |
| **schema**  boolean | Set to `true` to return the full attribute schema of entries, not their attribute values. Overrides `attrs` when provided.  **Choices:**   - `false` ← (default) - `true` |
| **scope**  string | The LDAP scope to use.  **Choices:**   - `"base"` ← (default) - `"onelevel"` - `"subordinate"` - `"children"` |
| **server_uri**  string | The `server_uri` parameter may be a comma- or whitespace-separated list of URIs containing only the schema, the host, and the port fields.  The default value lets the underlying LDAP client library look for a UNIX domain socket in its default location.  Note that when using multiple URIs you cannot determine to which URI your client gets connected.  For URIs containing additional fields, particularly when using commas, behavior is undefined.  **Default:** `"ldapi:///"` |
| **start_tls**  boolean | If true, we’ll use the START_TLS LDAP extension.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | If set to `false`, SSL certificates will not be validated.  This should only be used on sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **xorder_discovery**  string  *added in community.general 6.4.0* | Set the behavior on how to process Xordered DNs.  `enable` will perform a `ONELEVEL` search below the superior RDN to find the matching DN.  `disable` will always use the DN unmodified (as passed by the `dn` parameter).  `auto` will only perform a search if the first RDN does not contain an index number (`{x}`).  **Choices:**   - `"enable"` - `"auto"` ← (default) - `"disable"` |

## [Attributes](ldap_search_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](ldap_search_module.md#id5)

> **Note:**
>
> - The default authentication settings will attempt to use a SASL EXTERNAL bind over a UNIX domain socket. This works well with the default Ubuntu install for example, which includes a `cn=peercred,cn=external,cn=auth` ACL rule allowing root to modify the server configuration. If you need to use a simple bind to access your server, pass the credentials in `bind_dn` and `bind_pw`.

## [Examples](ldap_search_module.md#id6)

```yaml+jinja
- name: Return all entries within the 'groups' organizational unit.
  community.general.ldap_search:
    dn: "ou=groups,dc=example,dc=com"
  register: ldap_groups

- name: Return GIDs for all groups
  community.general.ldap_search:
    dn: "ou=groups,dc=example,dc=com"
    scope: "onelevel"
    attrs:
      - "gidNumber"
  register: ldap_group_gids
```

### Authors

- Sebastian Pfahl (@eryx12o45)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
