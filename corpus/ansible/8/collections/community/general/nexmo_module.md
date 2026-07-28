---
collection: ansible
version: "8"
title: "community.general.nexmo module – Send a SMS via nexmo"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/nexmo_module.html
fetched_at: 2026-07-28T01:48:07+00:00
---
# community.general.nexmo module – Send a SMS via nexmo

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.nexmo`.

- [Synopsis](nexmo_module.md#synopsis)
- [Parameters](nexmo_module.md#parameters)
- [Attributes](nexmo_module.md#attributes)
- [Examples](nexmo_module.md#examples)

## [Synopsis](nexmo_module.md#id1)

- Send a SMS message via nexmo

Aliases: notification.nexmo

## [Parameters](nexmo_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_key**  string / required | Nexmo API Key |
| **api_secret**  string / required | Nexmo API Secret |
| **client_cert**  path | PEM formatted certificate chain file to be used for SSL client authentication.  This file can also include the key as well, and if the key is included, `client_key` is not required. |
| **client_key**  path | PEM formatted file that contains your private key to be used for SSL client authentication.  If `client_cert` contains both the certificate and key, this option is not required. |
| **dest**  list / elements=integer / required | Phone number(s) to send SMS message to |
| **force**  boolean | If `yes` do not get a cached copy.  **Choices:**   - `false` ← (default) - `true` |
| **force_basic_auth**  boolean | Credentials specified with *url_username* and *url_password* should be passed in HTTP Header.  **Choices:**   - `false` ← (default) - `true` |
| **http_agent**  string | Header to identify as, generally appears in web server logs.  **Default:** `"ansible-httpget"` |
| **msg**  string / required | Message to text to send. Messages longer than 160 characters will be split into multiple messages |
| **src**  integer / required | Nexmo Number to send from |
| **url**  string | HTTP, HTTPS, or FTP URL in the form (http|https|ftp)://[user[:pass]]@host.domain[:port]/path |
| **url_password**  string | The password for use in HTTP basic authentication.  If the *url_username* parameter is not specified, the *url_password* parameter will not be used. |
| **url_username**  string | The username for use in HTTP basic authentication.  This parameter can be used without *url_password* for sites that allow empty passwords |
| **use_gssapi**  boolean  *added in ansible-core 2.11* | Use GSSAPI to perform the authentication, typically this is for Kerberos or Kerberos through Negotiate authentication.  Requires the Python library [gssapi](https://github.com/pythongssapi/python-gssapi) to be installed.  Credentials for GSSAPI can be specified with *url_username*/*url_password* or with the GSSAPI env var `KRB5CCNAME` that specified a custom Kerberos credential cache.  NTLM authentication is `not` supported even if the GSSAPI mech for NTLM has been installed.  **Choices:**   - `false` ← (default) - `true` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` - `true` ← (default) |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](nexmo_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](nexmo_module.md#id4)

```yaml+jinja
- name: Send notification message via Nexmo
  community.general.nexmo:
    api_key: 640c8a53
    api_secret: 0ce239a6
    src: 12345678901
    dest:
      - 10987654321
      - 16789012345
    msg: '{{ inventory_hostname }} completed'
  delegate_to: localhost
```

### Authors

- Matt Martz (@sivel)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
