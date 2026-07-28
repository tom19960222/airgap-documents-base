---
collection: ansible
version: "8"
title: "t_systems_mms.icinga_director.icinga_notification_template module – Manage notification templates in Icinga2"
source_url: https://docs.ansible.com/projects/ansible/8/collections/t_systems_mms/icinga_director/icinga_notification_template_module.html
fetched_at: 2026-07-28T02:54:13+00:00
---
# t_systems_mms.icinga_director.icinga_notification_template module – Manage notification templates in Icinga2

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
> To use it in a playbook, specify: `t_systems_mms.icinga_director.icinga_notification_template`.

New in t_systems_mms.icinga_director 1.9.0

- [Synopsis](icinga_notification_template_module.md#synopsis)
- [Parameters](icinga_notification_template_module.md#parameters)
- [Notes](icinga_notification_template_module.md#notes)
- [Examples](icinga_notification_template_module.md#examples)

## [Synopsis](icinga_notification_template_module.md#id1)

- Add or remove a notification template to Icinga2 through the director API.

## [Parameters](icinga_notification_template_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **append**  boolean  *added in t_systems_mms.icinga_director 1.25.0* | Do not overwrite the whole object but instead append the defined properties.  Note - Appending to existing vars, imports or any other list/dict is not possible. You have to overwrite the complete list/dict.  Note - Variables that are set by default will also be applied, even if not set.  **Choices:**   - `false` - `true` |
| **client_cert**  path | PEM formatted certificate chain file to be used for SSL client authentication.  This file can also include the key as well, and if the key is included, `client_key` is not required. |
| **client_key**  path | PEM formatted file that contains your private key to be used for SSL client authentication.  If `client_cert` contains both the certificate and key, this option is not required. |
| **command**  aliases: notification_command  string  *added in t_systems_mms.icinga_director 1.15.0* | Check command definition |
| **force**  boolean | If `yes` do not get a cached copy.  **Choices:**   - `false` ← (default) - `true` |
| **force_basic_auth**  boolean | Credentials specified with *url_username* and *url_password* should be passed in HTTP Header.  **Choices:**   - `false` ← (default) - `true` |
| **http_agent**  string | Header to identify as, generally appears in web server logs.  **Default:** `"ansible-httpget"` |
| **notification_interval**  string | The notification interval (in seconds). This interval is used for active notifications.  Defaults to 30 minutes. If set to 0, re-notifications are disabled. |
| **object_name**  aliases: name  string / required | Name of the notification template. |
| **period**  aliases: time_period  string  *added in t_systems_mms.icinga_director 1.15.0* | The name of a time period which determines when this notification should be triggered. |
| **state**  string | Apply feature state.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **states**  list / elements=string | The host or service states you want to get notifications for. |
| **times_begin**  integer | First notification delay.  Delay unless the first notification should be sent. |
| **times_end**  integer | Last notification.  When the last notification should be sent. |
| **types**  list / elements=string | The state transition types you want to get notifications for. |
| **url**  string / required | HTTP, HTTPS, or FTP URL in the form (http|https|ftp)://[user[:pass]]@host.domain[:port]/path |
| **url_password**  string | The password for use in HTTP basic authentication.  If the *url_username* parameter is not specified, the *url_password* parameter will not be used. |
| **url_username**  string | The username for use in HTTP basic authentication.  This parameter can be used without *url_password* for sites that allow empty passwords |
| **use_gssapi**  boolean  *added in ansible-core 2.11* | Use GSSAPI to perform the authentication, typically this is for Kerberos or Kerberos through Negotiate authentication.  Requires the Python library [gssapi](https://github.com/pythongssapi/python-gssapi) to be installed.  Credentials for GSSAPI can be specified with *url_username*/*url_password* or with the GSSAPI env var `KRB5CCNAME` that specified a custom Kerberos credential cache.  NTLM authentication is `not` supported even if the GSSAPI mech for NTLM has been installed.  **Choices:**   - `false` ← (default) - `true` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` - `true` ← (default) |
| **user_groups**  list / elements=string  *added in t_systems_mms.icinga_director 1.16.0* | User Groups that should be notified by this notification. |
| **users**  list / elements=string  *added in t_systems_mms.icinga_director 1.15.0* | Users that should be notified by this notification |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **zone**  string | Set the zone. |

## [Notes](icinga_notification_template_module.md#id3)

> **Note:**
>
> - This module supports check mode.

## [Examples](icinga_notification_template_module.md#id4)

```yaml+jinja
- name: Create notification template
  t_systems_mms.icinga_director.icinga_notification_template:
    state: present
    url: "{{ icinga_url }}"
    url_username: "{{ icinga_user }}"
    url_password: "{{ icinga_pass }}"
    object_name: foonotificationtemplate
    states:
      - Up
      - Down
    types:
      - Problem
      - Recovery
    times_begin: 20
    times_end: 120
    time_period: "24/7"
    notification_command: "mail-host-notification"
    users:
      - "rb"
    user_groups:
      - "OnCall"
    zone: "foozone"

- name: Update notification template
  t_systems_mms.icinga_director.icinga_notification_template:
    state: present
    url: "{{ icinga_url }}"
    url_username: "{{ icinga_user }}"
    url_password: "{{ icinga_pass }}"
    object_name: foonotificationtemplate
    notification_interval: '0'
    append: true
```

### Authors

- Sebastian Gumprich (@rndmh3ro) / Sebastian Gruber (sgruber94)

### Collection links

- [Issue Tracker](https://github.com/T-Systems-MMS/ansible-collection-icinga-director/issues)
- [Repository (Sources)](https://github.com/T-Systems-MMS/ansible-collection-icinga-director)
