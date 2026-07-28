---
collection: ansible
version: "6"
title: "community.general.icinga2_host module – Manage a host in Icinga2"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/icinga2_host_module.html
fetched_at: 2026-07-27T17:09:38+00:00
---
# community.general.icinga2_host module – Manage a host in Icinga2

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.icinga2_host`.

- [Synopsis](icinga2_host_module.md#synopsis)
- [Parameters](icinga2_host_module.md#parameters)
- [Examples](icinga2_host_module.md#examples)
- [Return Values](icinga2_host_module.md#return-values)

## [Synopsis](icinga2_host_module.md#id1)

- Add or remove a host to Icinga2 through the API.
- See <https://www.icinga.com/docs/icinga2/latest/doc/12-icinga2-api/>

## [Parameters](icinga2_host_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **check_command**  string | The command used to check if the host is alive.  Default: `"hostalive"` |
| **client_cert**  path | PEM formatted certificate chain file to be used for SSL client authentication. This file can also include the key as well, and if the key is included, `client_key` is not required. |
| **client_key**  path | PEM formatted file that contains your private key to be used for SSL client authentication. If `client_cert` contains both the certificate and key, this option is not required. |
| **display_name**  string | The name used to display the host.  If not specified, it defaults to the value of the *name* parameter. |
| **force**  boolean | If `yes` do not get a cached copy.  Choices:   - `false` ← (default) - `true` |
| **force_basic_auth**  boolean | httplib2, the library used by the uri module only sends authentication information when a webservice responds to an initial request with a 401 status. Since some basic auth services do not properly send a 401, logins will fail. This option forces the sending of the Basic authentication header upon initial request.  Choices:   - `false` ← (default) - `true` |
| **http_agent**  string | Header to identify as, generally appears in web server logs.  Default: `"ansible-httpget"` |
| **ip**  string / required | The IP address of the host. |
| **name**  aliases: host  string / required | Name used to create / delete the host. This does not need to be the FQDN, but does needs to be unique. |
| **state**  string | Apply feature state.  Choices:   - `"present"` ← (default) - `"absent"` |
| **template**  string | The template used to define the host.  Template cannot be modified after object creation. |
| **url**  string | HTTP, HTTPS, or FTP URL in the form (http|https|ftp)://[user[:pass]]@host.domain[:port]/path |
| **url_password**  string | The password for use in HTTP basic authentication.  If the `url_username` parameter is not specified, the `url_password` parameter will not be used. |
| **url_username**  string | The username for use in HTTP basic authentication.  This parameter can be used without `url_password` for sites that allow empty passwords. |
| **use_gssapi**  boolean  added in ansible-core 2.11 | Use GSSAPI to perform the authentication, typically this is for Kerberos or Kerberos through Negotiate authentication.  Requires the Python library [gssapi](https://github.com/pythongssapi/python-gssapi) to be installed.  Credentials for GSSAPI can be specified with *url_username*/*url_password* or with the GSSAPI env var `KRB5CCNAME` that specified a custom Kerberos credential cache.  NTLM authentication is `not` supported even if the GSSAPI mech for NTLM has been installed.  Choices:   - `false` ← (default) - `true` |
| **use_proxy**  boolean | If `false`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` - `true` ← (default) |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **variables**  dictionary | Dictionary of variables. |
| **zone**  string | The zone from where this host should be polled. |

## [Examples](icinga2_host_module.md#id3)

```yaml+jinja
- name: Add host to icinga
  community.general.icinga2_host:
    url: "https://icinga2.example.com"
    url_username: "ansible"
    url_password: "a_secret"
    state: present
    name: "{{ ansible_fqdn }}"
    ip: "{{ ansible_default_ipv4.address }}"
    variables:
      foo: "bar"
  delegate_to: 127.0.0.1
```

## [Return Values](icinga2_host_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | The data structure used for create, modify or delete of the host  Returned: always |
| **name**  string | The name used to create, modify or delete the host  Returned: always |

### Authors

- Jurgen Brand (@t794104)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
