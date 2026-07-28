---
collection: ansible
version: "8"
title: "telekom_mms.icinga_director.icinga_notification module – Manage notifications in Icinga2"
source_url: https://docs.ansible.com/projects/ansible/8/collections/telekom_mms/icinga_director/icinga_notification_module.html
fetched_at: 2026-07-28T02:55:00+00:00
---
# telekom_mms.icinga_director.icinga_notification module – Manage notifications in Icinga2

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
> To use it in a playbook, specify: `telekom_mms.icinga_director.icinga_notification`.

New in telekom_mms.icinga_director 1.0.0

- [Synopsis](icinga_notification_module.md#synopsis)
- [Parameters](icinga_notification_module.md#parameters)
- [Notes](icinga_notification_module.md#notes)
- [Examples](icinga_notification_module.md#examples)

## [Synopsis](icinga_notification_module.md#id1)

- Add or remove a notification to Icinga2 through the director API.

## [Parameters](icinga_notification_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **append**  boolean  *added in telekom_mms.icinga_director 1.25.0* | Do not overwrite the whole object but instead append the defined properties.  Note - Appending to existing vars, imports or any other list/dict is not possible. You have to overwrite the complete list/dict.  Note - Variables that are set by default will also be applied, even if not set.  **Choices:**   - `false` - `true` |
| **apply_to**  string | Whether this notification should affect hosts or services.  Required if *state* is `present`.  **Choices:**   - `"host"` - `"service"` |
| **assign_filter**  string | The filter where the notification will take effect. |
| **client_cert**  path | PEM formatted certificate chain file to be used for SSL client authentication.  This file can also include the key as well, and if the key is included, `client_key` is not required. |
| **client_key**  path | PEM formatted file that contains your private key to be used for SSL client authentication.  If `client_cert` contains both the certificate and key, this option is not required. |
| **disabled**  boolean  *added in telekom_mms.icinga_director 1.9.0* | Disabled objects will not be deployed.  **Choices:**   - `false` ← (default) - `true` |
| **force**  boolean | If `yes` do not get a cached copy.  **Choices:**   - `false` ← (default) - `true` |
| **force_basic_auth**  boolean | Credentials specified with *url_username* and *url_password* should be passed in HTTP Header.  **Choices:**   - `false` ← (default) - `true` |
| **http_agent**  string | Header to identify as, generally appears in web server logs.  **Default:** `"ansible-httpget"` |
| **imports**  list / elements=string | Importable templates, add as many as you want. Required when state is `present`.  Please note that order matters when importing properties from multiple templates - last one wins.  Required if *state* is `present`. |
| **notification_interval**  string | The notification interval (in seconds). This interval is used for active notifications.  Defaults to 30 minutes. If set to 0, re-notifications are disabled. |
| **object_name**  aliases: name  string / required | Name of the notification. |
| **period**  aliases: time_period  string  *added in telekom_mms.icinga_director 1.15.0* | The name of a time period which determines when this notification should be triggered. |
| **state**  string | Apply feature state.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **states**  list / elements=string  *added in telekom_mms.icinga_director 1.9.0* | The host or service states you want to get notifications for. |
| **times_begin**  integer  *added in telekom_mms.icinga_director 1.15.0* | First notification delay.  Delay unless the first notification should be sent. |
| **times_end**  integer  *added in telekom_mms.icinga_director 1.15.0* | Last notification.  When the last notification should be sent. |
| **types**  list / elements=string | The state transition types you want to get notifications for. |
| **url**  string / required | HTTP, HTTPS, or FTP URL in the form (http|https|ftp)://[user[:pass]]@host.domain[:port]/path |
| **url_password**  string | The password for use in HTTP basic authentication.  If the *url_username* parameter is not specified, the *url_password* parameter will not be used. |
| **url_username**  string | The username for use in HTTP basic authentication.  This parameter can be used without *url_password* for sites that allow empty passwords |
| **use_gssapi**  boolean  *added in ansible-core 2.11* | Use GSSAPI to perform the authentication, typically this is for Kerberos or Kerberos through Negotiate authentication.  Requires the Python library [gssapi](https://github.com/pythongssapi/python-gssapi) to be installed.  Credentials for GSSAPI can be specified with *url_username*/*url_password* or with the GSSAPI env var `KRB5CCNAME` that specified a custom Kerberos credential cache.  NTLM authentication is `not` supported even if the GSSAPI mech for NTLM has been installed.  **Choices:**   - `false` ← (default) - `true` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` - `true` ← (default) |
| **user_groups**  list / elements=string  *added in telekom_mms.icinga_director 1.16.0* | User Groups that should be notified by this notification. |
| **users**  list / elements=string | Users that should be notified by this notification. |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **vars**  dictionary  *added in telekom_mms.icinga_director 1.9.0* | Custom properties of the notification.  **Default:** `{}` |

## [Notes](icinga_notification_module.md#id3)

> **Note:**
>
> - This module supports check mode.

## [Examples](icinga_notification_module.md#id4)

```yaml+jinja
- name: Create notification
  telekom_mms.icinga_director.icinga_notification:
    state: present
    url: "{{ icinga_url }}"
    url_username: "{{ icinga_user }}"
    url_password: "{{ icinga_pass }}"
    apply_to: host
    assign_filter: 'host.name="foohost"'
    imports:
      - foonotificationtemplate
    notification_interval: '0'
    object_name: E-Mail_host
    states:
      - Up
      - Down
    types:
      - Problem
      - Recovery
    users:
      - rb
    user_groups:
      - OnCall
    disabled: false
    time_period: "24/7"
    times_begin: 20
    times_end: 120

- name: Update notification
  telekom_mms.icinga_director.icinga_notification:
    state: present
    url: "{{ icinga_url }}"
    url_username: "{{ icinga_user }}"
    url_password: "{{ icinga_pass }}"
    object_name: E-Mail_host
    vars:
      foo: bar
    append: true
```

### Authors

- Sebastian Gumprich (@rndmh3ro) / Sebastian Gruber (sgruber94)

### Collection links

- [Issue Tracker](https://github.com/telekom-mms/ansible-collection-icinga-director/issues)
- [Repository (Sources)](https://github.com/telekom-mms/ansible-collection-icinga-director)
