---
collection: ansible
version: "8"
title: "telekom_mms.icinga_director.icinga_endpoint module – Manage endpoints in Icinga2"
source_url: https://docs.ansible.com/projects/ansible/8/collections/telekom_mms/icinga_director/icinga_endpoint_module.html
fetched_at: 2026-07-28T02:54:48+00:00
---
# telekom_mms.icinga_director.icinga_endpoint module – Manage endpoints in Icinga2

> **Note:**
>
> This module is part of the [telekom_mms.icinga_director collection](https://galaxy.ansible.com/ui/repo/published/telekom_mms/icinga_director/) (version 1.35.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install telekom_mms.icinga_director`.
>
> To use it in a playbook, specify: `telekom_mms.icinga_director.icinga_endpoint`.

New in telekom_mms.icinga_director 1.5.0

- [Synopsis](icinga_endpoint_module.md#synopsis)
- [Parameters](icinga_endpoint_module.md#parameters)
- [Notes](icinga_endpoint_module.md#notes)
- [Examples](icinga_endpoint_module.md#examples)

## [Synopsis](icinga_endpoint_module.md#id1)

- Add or remove an endpoint to Icinga2 through the director API.

## [Parameters](icinga_endpoint_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **append**  boolean  *added in telekom_mms.icinga_director 1.25.0* | Do not overwrite the whole object but instead append the defined properties.  Note - Appending to existing vars, imports or any other list/dict is not possible. You have to overwrite the complete list/dict.  Note - Variables that are set by default will also be applied, even if not set.  **Choices:**   - `false` - `true` |
| **client_cert**  path | PEM formatted certificate chain file to be used for SSL client authentication.  This file can also include the key as well, and if the key is included, `client_key` is not required. |
| **client_key**  path | PEM formatted file that contains your private key to be used for SSL client authentication.  If `client_cert` contains both the certificate and key, this option is not required. |
| **force**  boolean | If `yes` do not get a cached copy.  **Choices:**   - `false` ← (default) - `true` |
| **force_basic_auth**  boolean | Credentials specified with *url_username* and *url_password* should be passed in HTTP Header.  **Choices:**   - `false` ← (default) - `true` |
| **host**  string | The hostname/IP address of the remote Icinga 2 instance. |
| **http_agent**  string | Header to identify as, generally appears in web server logs.  **Default:** `"ansible-httpget"` |
| **log_duration**  string | Duration for keeping replay logs on connection loss. Defaults to 1d (86400 seconds). Attribute is specified in seconds. If log_duration is set to 0, replaying logs is disabled. You could also specify the value in human readable format like 10m for 10 minutes or 1h for one hour. |
| **object_name**  aliases: name  string / required | Icinga object name for this endpoint.  This is usually a fully qualified host name but it could basically be any kind of string.  To make things easier for your users we strongly suggest to use meaningful names for templates.  For example “generic-endpoint” is ugly, “Standard Linux Server” is easier to understand. |
| **port**  integer | The service name/port of the remote Icinga 2 instance. Defaults to 5665. |
| **state**  string | Apply feature state.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **url**  string / required | HTTP, HTTPS, or FTP URL in the form (http|https|ftp)://[user[:pass]]@host.domain[:port]/path |
| **url_password**  string | The password for use in HTTP basic authentication.  If the *url_username* parameter is not specified, the *url_password* parameter will not be used. |
| **url_username**  string | The username for use in HTTP basic authentication.  This parameter can be used without *url_password* for sites that allow empty passwords |
| **use_gssapi**  boolean  *added in ansible-core 2.11* | Use GSSAPI to perform the authentication, typically this is for Kerberos or Kerberos through Negotiate authentication.  Requires the Python library [gssapi](https://github.com/pythongssapi/python-gssapi) to be installed.  Credentials for GSSAPI can be specified with *url_username*/*url_password* or with the GSSAPI env var `KRB5CCNAME` that specified a custom Kerberos credential cache.  NTLM authentication is `not` supported even if the GSSAPI mech for NTLM has been installed.  **Choices:**   - `false` ← (default) - `true` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` - `true` ← (default) |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **zone**  string | The name of the zone this endpoint is part of. |

## [Notes](icinga_endpoint_module.md#id3)

> **Note:**
>
> - This module supports check mode.

## [Examples](icinga_endpoint_module.md#id4)

```yaml+jinja
- name: Create an endpoint in icinga
  telekom_mms.icinga_director.icinga_endpoint:
    state: present
    url: "{{ icinga_url }}"
    url_username: "{{ icinga_user }}"
    url_password: "{{ icinga_pass }}"
    object_name: "fooendpoint"
    host: "127.0.0.1"
    zone: "foozone"

- name: Update an endpoint in icinga
  telekom_mms.icinga_director.icinga_endpoint:
    state: present
    url: "{{ icinga_url }}"
    url_username: "{{ icinga_user }}"
    url_password: "{{ icinga_pass }}"
    object_name: "fooendpoint"
    host: "127.0.0.1"
    zone: "foozone"
    port: 5665
    append: true
```

### Authors

- Aaron Bulmahn (@arbu)

### Collection links

- [Issue Tracker](https://github.com/telekom-mms/ansible-collection-icinga-director/issues)
- [Repository (Sources)](https://github.com/telekom-mms/ansible-collection-icinga-director)
