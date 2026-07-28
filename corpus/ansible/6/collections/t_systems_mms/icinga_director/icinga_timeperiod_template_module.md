---
collection: ansible
version: "6"
title: "t_systems_mms.icinga_director.icinga_timeperiod_template module – Manage timeperiod templates in Icinga2"
source_url: https://docs.ansible.com/projects/ansible/6/collections/t_systems_mms/icinga_director/icinga_timeperiod_template_module.html
fetched_at: 2026-07-28T00:20:21+00:00
---
# t_systems_mms.icinga_director.icinga_timeperiod_template module – Manage timeperiod templates in Icinga2

> **Note:**
>
> This module is part of the [t_systems_mms.icinga_director collection](https://galaxy.ansible.com/t_systems_mms/icinga_director) (version 1.31.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install t_systems_mms.icinga_director`.
>
> To use it in a playbook, specify: `t_systems_mms.icinga_director.icinga_timeperiod_template`.

New in t_systems_mms.icinga_director 1.17.0

- [Synopsis](icinga_timeperiod_template_module.md#synopsis)
- [Parameters](icinga_timeperiod_template_module.md#parameters)
- [Notes](icinga_timeperiod_template_module.md#notes)
- [Examples](icinga_timeperiod_template_module.md#examples)

## [Synopsis](icinga_timeperiod_template_module.md#id1)

- Add or remove a timeperiod template to Icinga2 through the director API.

## [Parameters](icinga_timeperiod_template_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **append**  boolean  added in t_systems_mms.icinga_director 1.25.0 | Do not overwrite the whole object but instead append the defined properties.  Note - Appending to existing vars, imports or any other list/dict is not possible. You have to overwrite the complete list/dict.  Note - Variables that are set by default will also be applied, even if not set.  Choices:   - `false` - `true` |
| **client_cert**  path | PEM formatted certificate chain file to be used for SSL client authentication.  This file can also include the key as well, and if the key is included, `client_key` is not required. |
| **client_key**  path | PEM formatted file that contains your private key to be used for SSL client authentication.  If `client_cert` contains both the certificate and key, this option is not required. |
| **disabled**  boolean | Disabled objects will not be deployed.  Choices:   - `false` ← (default) - `true` |
| **display_name**  string | Alternative name for this timeperiod template. |
| **excludes**  aliases: exclude_period  list / elements=string | Exclude other time periods from this.  Default: `[]` |
| **force**  boolean | If `yes` do not get a cached copy.  Choices:   - `false` ← (default) - `true` |
| **force_basic_auth**  boolean | Credentials specified with *url_username* and *url_password* should be passed in HTTP Header.  Choices:   - `false` ← (default) - `true` |
| **http_agent**  string | Header to identify as, generally appears in web server logs.  Default: `"ansible-httpget"` |
| **imports**  list / elements=string | Importable templates, add as many as you want.  Please note that order matters when importing properties from multiple templates - last one wins.  Default: `[]` |
| **includes**  aliases: include_period  list / elements=string | Include other time periods into this.  Default: `[]` |
| **object_name**  aliases: name  string / required | Name of the time period. |
| **prefer_includes**  boolean | Whether to prefer timeperiods includes or excludes. Default to true.  Choices:   - `false` - `true` ← (default) |
| **ranges**  dictionary | A dict of days and timeperiods. |
| **state**  string | Apply feature state.  Choices:   - `"present"` ← (default) - `"absent"` |
| **update_method**  string | Define the update method.  Default: `"LegacyTimePeriod"` |
| **url**  string / required | HTTP, HTTPS, or FTP URL in the form (http|https|ftp)://[user[:pass]]@host.domain[:port]/path |
| **url_password**  string | The password for use in HTTP basic authentication.  If the *url_username* parameter is not specified, the *url_password* parameter will not be used. |
| **url_username**  string | The username for use in HTTP basic authentication.  This parameter can be used without *url_password* for sites that allow empty passwords |
| **use_gssapi**  boolean  added in ansible-core 2.11 | Use GSSAPI to perform the authentication, typically this is for Kerberos or Kerberos through Negotiate authentication.  Requires the Python library [gssapi](https://github.com/pythongssapi/python-gssapi) to be installed.  Credentials for GSSAPI can be specified with *url_username*/*url_password* or with the GSSAPI env var `KRB5CCNAME` that specified a custom Kerberos credential cache.  NTLM authentication is `not` supported even if the GSSAPI mech for NTLM has been installed.  Choices:   - `false` ← (default) - `true` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` - `true` ← (default) |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **zone**  string | Set the zone. |

## [Notes](icinga_timeperiod_template_module.md#id3)

> **Note:**
>
> - This module supports check mode.

## [Examples](icinga_timeperiod_template_module.md#id4)

```yaml+jinja
- name: Create timeperiod template
  t_systems_mms.icinga_director.icinga_timeperiod_template:
    state: present
    url: "{{ icinga_url }}"
    url_username: "{{ icinga_user }}"
    url_password: "{{ icinga_pass }}"
    object_name: "timeperiod_template"
    imports: []
    disabled: false
    prefer_includes: false
    ranges:
      monday: "00:00-23:59"
      tuesday: "00:00-23:59"
      wednesday: "00:00-23:59"
      thursday: "00:00-23:59"
      friday: "00:00-23:59"
      saturday: "00:00-23:59"
      sunday: "00:00-23:59"
    update_method: "LegacyTimePeriod"

- name: Update timeperiod template
  t_systems_mms.icinga_director.icinga_timeperiod_template:
    state: present
    url: "{{ icinga_url }}"
    url_username: "{{ icinga_user }}"
    url_password: "{{ icinga_pass }}"
    object_name: "timeperiod_template"
    display_name: "timeperiod template"
    append: true
```

### Authors

- Sebastian Gumprich (@rndmh3ro)

### Collection links

[Issue Tracker](https://github.com/T-Systems-MMS/ansible-collection-icinga-director/issues)
[Repository (Sources)](https://github.com/T-Systems-MMS/ansible-collection-icinga-director)
