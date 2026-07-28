---
collection: ansible
version: "8"
title: "t_systems_mms.icinga_director.icinga_servicegroup_info module – Query servicegroups in Icinga2"
source_url: https://docs.ansible.com/projects/ansible/8/collections/t_systems_mms/icinga_director/icinga_servicegroup_info_module.html
fetched_at: 2026-07-28T02:54:23+00:00
---
# t_systems_mms.icinga_director.icinga_servicegroup_info module – Query servicegroups in Icinga2

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
> To use it in a playbook, specify: `t_systems_mms.icinga_director.icinga_servicegroup_info`.

New in t_systems_mms.icinga_director 1.13.0

- [Synopsis](icinga_servicegroup_info_module.md#synopsis)
- [Parameters](icinga_servicegroup_info_module.md#parameters)
- [Notes](icinga_servicegroup_info_module.md#notes)
- [Examples](icinga_servicegroup_info_module.md#examples)
- [Return Values](icinga_servicegroup_info_module.md#return-values)

## [Synopsis](icinga_servicegroup_info_module.md#id1)

- Get a list of servicegroup objects from Icinga2 through the director API.

## [Parameters](icinga_servicegroup_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **client_cert**  path | PEM formatted certificate chain file to be used for SSL client authentication.  This file can also include the key as well, and if the key is included, `client_key` is not required. |
| **client_key**  path | PEM formatted file that contains your private key to be used for SSL client authentication.  If `client_cert` contains both the certificate and key, this option is not required. |
| **force**  boolean | If `yes` do not get a cached copy.  **Choices:**   - `false` ← (default) - `true` |
| **force_basic_auth**  boolean | Credentials specified with *url_username* and *url_password* should be passed in HTTP Header.  **Choices:**   - `false` ← (default) - `true` |
| **http_agent**  string | Header to identify as, generally appears in web server logs.  **Default:** `"ansible-httpget"` |
| **query**  string | Text to filter search results.  The text is matched on object_name.  Only objects containing this text will be returned in the resultset.  Requires Icinga Director 1.8.0+, in earlier versions this parameter is ignored and all objects are returned.  **Default:** `""` |
| **resolved**  boolean | Resolve all inherited object properties and omit templates in output.  **Choices:**   - `false` ← (default) - `true` |
| **url**  string / required | HTTP, HTTPS, or FTP URL in the form (http|https|ftp)://[user[:pass]]@host.domain[:port]/path |
| **url_password**  string | The password for use in HTTP basic authentication.  If the *url_username* parameter is not specified, the *url_password* parameter will not be used. |
| **url_username**  string | The username for use in HTTP basic authentication.  This parameter can be used without *url_password* for sites that allow empty passwords |
| **use_gssapi**  boolean  *added in ansible-core 2.11* | Use GSSAPI to perform the authentication, typically this is for Kerberos or Kerberos through Negotiate authentication.  Requires the Python library [gssapi](https://github.com/pythongssapi/python-gssapi) to be installed.  Credentials for GSSAPI can be specified with *url_username*/*url_password* or with the GSSAPI env var `KRB5CCNAME` that specified a custom Kerberos credential cache.  NTLM authentication is `not` supported even if the GSSAPI mech for NTLM has been installed.  **Choices:**   - `false` ← (default) - `true` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` - `true` ← (default) |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](icinga_servicegroup_info_module.md#id3)

> **Note:**
>
> - This module supports check mode.

## [Examples](icinga_servicegroup_info_module.md#id4)

```yaml+jinja
- name: Query a servicegroup in icinga
  t_systems_mms.icinga_director.icinga_servicegroup_info:
    url: "{{ icinga_url }}"
    url_username: "{{ icinga_user }}"
    url_password: "{{ icinga_pass }}"
    query: "fooservicegroup"
```

## [Return Values](icinga_servicegroup_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **objects**  list / elements=string | A list of returned Director objects.  The list contains all objects matching the query filter.  If the filter does not match any object, the list will be empty.  **Returned:** always |

### Authors

- Martin Schurz (@schurzi)

### Collection links

- [Issue Tracker](https://github.com/T-Systems-MMS/ansible-collection-icinga-director/issues)
- [Repository (Sources)](https://github.com/T-Systems-MMS/ansible-collection-icinga-director)
