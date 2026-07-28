---
collection: ansible
version: "8"
title: "t_systems_mms.icinga_director.icinga_zone module – Manage zones in Icinga2"
source_url: https://docs.ansible.com/projects/ansible/8/collections/t_systems_mms/icinga_director/icinga_zone_module.html
fetched_at: 2026-07-28T02:54:38+00:00
---
# t_systems_mms.icinga_director.icinga_zone module – Manage zones in Icinga2

> **Note:**
>
> This module is part of the [t_systems_mms.icinga_director collection](https://galaxy.ansible.com/ui/repo/published/t_systems_mms/icinga_director/) (version 1.33.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install t_systems_mms.icinga_director`.
>
> To use it in a playbook, specify: `t_systems_mms.icinga_director.icinga_zone`.

New in t_systems_mms.icinga_director 1.5.0

- [Synopsis](icinga_zone_module.md#synopsis)
- [Parameters](icinga_zone_module.md#parameters)
- [Notes](icinga_zone_module.md#notes)
- [Examples](icinga_zone_module.md#examples)

## [Synopsis](icinga_zone_module.md#id1)

- Add or remove a zone to Icinga2 through the director API.

## [Parameters](icinga_zone_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **append**  boolean  *added in t_systems_mms.icinga_director 1.25.0* | Do not overwrite the whole object but instead append the defined properties.  Note - Appending to existing vars, imports or any other list/dict is not possible. You have to overwrite the complete list/dict.  Note - Variables that are set by default will also be applied, even if not set.  **Choices:**   - `false` - `true` |
| **client_cert**  path | PEM formatted certificate chain file to be used for SSL client authentication.  This file can also include the key as well, and if the key is included, `client_key` is not required. |
| **client_key**  path | PEM formatted file that contains your private key to be used for SSL client authentication.  If `client_cert` contains both the certificate and key, this option is not required. |
| **force**  boolean | If `yes` do not get a cached copy.  **Choices:**   - `false` ← (default) - `true` |
| **force_basic_auth**  boolean | Credentials specified with *url_username* and *url_password* should be passed in HTTP Header.  **Choices:**   - `false` ← (default) - `true` |
| **http_agent**  string | Header to identify as, generally appears in web server logs.  **Default:** `"ansible-httpget"` |
| **is_global**  boolean | Whether configuration files for this zone should be synced to all endpoints.  **Choices:**   - `false` ← (default) - `true` |
| **object_name**  aliases: name  string / required | Icinga object name for this zone.  This is usually a fully qualified host name but it could basically be any kind of string.  To make things easier for your users we strongly suggest to use meaningful names for templates.  For example “generic-zone” is ugly, “Standard Linux Server” is easier to understand. |
| **parent**  string | The name of the parent zone. |
| **state**  string | Apply feature state.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **url**  string / required | HTTP, HTTPS, or FTP URL in the form (http|https|ftp)://[user[:pass]]@host.domain[:port]/path |
| **url_password**  string | The password for use in HTTP basic authentication.  If the *url_username* parameter is not specified, the *url_password* parameter will not be used. |
| **url_username**  string | The username for use in HTTP basic authentication.  This parameter can be used without *url_password* for sites that allow empty passwords |
| **use_gssapi**  boolean  *added in ansible-core 2.11* | Use GSSAPI to perform the authentication, typically this is for Kerberos or Kerberos through Negotiate authentication.  Requires the Python library [gssapi](https://github.com/pythongssapi/python-gssapi) to be installed.  Credentials for GSSAPI can be specified with *url_username*/*url_password* or with the GSSAPI env var `KRB5CCNAME` that specified a custom Kerberos credential cache.  NTLM authentication is `not` supported even if the GSSAPI mech for NTLM has been installed.  **Choices:**   - `false` ← (default) - `true` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` - `true` ← (default) |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](icinga_zone_module.md#id3)

> **Note:**
>
> - This module supports check mode.

## [Examples](icinga_zone_module.md#id4)

```yaml+jinja
- name: Create a zone in icinga
  t_systems_mms.icinga_director.icinga_zone:
    state: present
    url: "{{ icinga_url }}"
    url_username: "{{ icinga_user }}"
    url_password: "{{ icinga_pass }}"
    object_name: "foozone"

- name: Update a zone in icinga
  t_systems_mms.icinga_director.icinga_zone:
    state: present
    url: "{{ icinga_url }}"
    url_username: "{{ icinga_user }}"
    url_password: "{{ icinga_pass }}"
    object_name: "foozone"
    parent: "master"
    append: true
```

### Authors

- Aaron Bulmahn (@arbu)

### Collection links

- [Issue Tracker](https://github.com/T-Systems-MMS/ansible-collection-icinga-director/issues)
- [Repository (Sources)](https://github.com/T-Systems-MMS/ansible-collection-icinga-director)
