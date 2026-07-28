---
collection: ansible
version: "6"
title: "community.zabbix.zabbix_mediatype module – Create/Update/Delete Zabbix media types"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/zabbix/zabbix_mediatype_module.html
fetched_at: 2026-07-27T17:24:17+00:00
---
# community.zabbix.zabbix_mediatype module – Create/Update/Delete Zabbix media types

> **Note:**
>
> This module is part of the [community.zabbix collection](https://galaxy.ansible.com/community/zabbix) (version 1.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.zabbix`.
> You need further requirements to be able to use this module,
> see [Requirements](zabbix_mediatype_module.md#ansible-collections-community-zabbix-zabbix-mediatype-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_mediatype`.

- [Synopsis](zabbix_mediatype_module.md#synopsis)
- [Requirements](zabbix_mediatype_module.md#requirements)
- [Parameters](zabbix_mediatype_module.md#parameters)
- [Notes](zabbix_mediatype_module.md#notes)
- [Examples](zabbix_mediatype_module.md#examples)

## [Synopsis](zabbix_mediatype_module.md#id1)

- This module allows you to create, modify and delete Zabbix media types.

## [Requirements](zabbix_mediatype_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](zabbix_mediatype_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **attempt_interval**  string | The interval between retry attempts.  Possible range is 0-60s in Zabbix < 5.0 or 0-1h in Zabbix >= 5.0.  Works only with Zabbix versions 3.4 or newer.  Default: `"10s"` |
| **description**  string | Description of the media type.  Works only with Zabbix versions 4.4 or newer.  Default: `""` |
| **event_menu**  boolean | Can be used when *type=webhook*.  Includes entry in Event menu with link to created external ticket.  Choices:   - `false` ← (default) - `true` |
| **event_menu_name**  string | Requred when *event_menu=True*.  Event menu entry name. |
| **event_menu_url**  string | Requred when *event_menu=True*.  Event menu entry underlying URL. |
| **gsm_modem**  string | Serial device name of the gsm modem.  Required when *type=sms*. |
| **login_password**  string | Zabbix user password.  If not set the environment variable `ZABBIX_PASSWORD` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **login_user**  string | Zabbix user name.  If not set the environment variable `ZABBIX_USERNAME` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **max_attempts**  integer | The maximum number of attempts to send an alert.  Possible range is 0-10.  Works only with Zabbix versions 3.4 or newer.  Default: `3` |
| **max_sessions**  integer | The maximum number of alerts that can be processed in parallel.  Possible value is 1 when *type=sms* and 0-100 otherwise.  Works only with Zabbix versions 3.4 or newer.  Default: `1` |
| **message_templates**  list / elements=dictionary | Default notification messages for the event types.  Works only with Zabbix versions 5.0 or newer.  Default: `[]` |
| **body**  string | Body of the default message.  May contain macros.  Default: `""` |
| **eventsource**  string | Event source.  Required when *recovery* is used.  Choices:   - `"triggers"` - `"discovery"` - `"autoregistration"` - `"internal"` |
| **recovery**  string | Operation mode.  Required when *eventsource* is used.  Choices:   - `"operations"` - `"recovery_operations"` - `"update_operations"` |
| **subject**  string | Subject of the default message.  May contain macros and is limited to 255 characters.  Default: `""` |
| **message_text_limit**  string | The message text limit.  Required when *type=ez_texting*.  160 characters for USA and 136 characters for Canada.  Choices:   - `"USA"` - `"Canada"` |
| **name**  string / required | Name of the media type. |
| **password**  string | Authentication password.  Required when *type=jabber* or *type=ez_texting*.  Required when *type=email* and *smtp_authentication=true*. |
| **process_tags**  boolean | Can be used when *type=webhook*.  Process returned JSON property values as tags.  These tags are added to the already existing (if any) problem event tags in Zabbix.  Choices:   - `false` ← (default) - `true` |
| **script_name**  string | The name of the executed script.  Required when *type=script*. |
| **script_params**  list / elements=string | List of script parameters.  Required when *type=script*. |
| **server_url**  aliases: url  string | URL of Zabbix server, with protocol (http or https). `url` is an alias for `server_url`.  If not set the environment variable `ZABBIX_SERVER` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **smtp_authentication**  boolean | Whether SMTP authentication with username and password should be enabled or not.  If set to `true`, `username` and `password` should be specified.  Choices:   - `false` ← (default) - `true` |
| **smtp_email**  string | Email address from which notifications will be sent.  Required when *type=email*. |
| **smtp_helo**  string | SMTP HELO.  Required when *type=email*.  Default: `"localhost"` |
| **smtp_security**  string | SMTP connection security level to use.  Choices:   - `"None"` - `"STARTTLS"` - `"SSL/TLS"` |
| **smtp_server**  string | SMTP server host.  Required when *type=email*.  Default: `"localhost"` |
| **smtp_server_port**  integer | SMTP server port.  Required when *type=email*.  Default: `25` |
| **smtp_verify_host**  boolean | SSL verify host for SMTP.  Can be specified when *smtp_security=STARTTLS* or *smtp_security=SSL/TLS*  Choices:   - `false` ← (default) - `true` |
| **smtp_verify_peer**  boolean | SSL verify peer for SMTP.  Can be specified when *smtp_security=STARTTLS* or *smtp_security=SSL/TLS*  Choices:   - `false` ← (default) - `true` |
| **state**  string | Desired state of the mediatype.  On `present`, it will create a mediatype if it does not exist or update the mediatype if the associated data is different.  On `absent`, it will remove the mediatype if it exists.  Choices:   - `"present"` ← (default) - `"absent"` |
| **status**  string | Whether the media type is enabled or no.  Choices:   - `"enabled"` ← (default) - `"disabled"` |
| **timeout**  integer | The timeout of API request (seconds).  This option is deprecated with the move to httpapi connection and will be removed in the next release  Default: `10` |
| **type**  string / required | Type of the media type.  Media types *jabber* and *ez_texting* works only with Zabbix versions 4.2 or older.  Media type *webhook* works only with Zabbix versions 4.4 or newer.  Choices:   - `"email"` - `"script"` - `"sms"` - `"webhook"` - `"jabber"` - `"ez_texting"` |
| **username**  string | Username or Jabber identifier.  Required when *type=jabber* or *type=ez_texting*.  Required when *type=email* and *smtp_authentication=true*. |
| **validate_certs**  boolean | If set to False, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If not set the environment variable `ZABBIX_VALIDATE_CERTS` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release  Choices:   - `false` - `true` ← (default) |
| **webhook_params**  list / elements=dictionary | Can be used when *type=webhook*.  Webhook variables that are passed to webhook script when executed.  Default: `[]` |
| **name**  string / required | Name of the parameter. |
| **value**  string | Value of the parameter.  All macros that are supported in problem notifications are supported in the parameters.  Values are URL-encoded automatically. Values from macros are resolved and then URL-encoded automatically.  Default: `""` |
| **webhook_script**  string | Required when *type=webhook*.  JavaScript code that will perform webhook operation.  This code has access to all parameters in *webhook_params*.  It may perform HTTP GET, POST, PUT and DELETE requests and has control over HTTP headers and request body.  It may return OK status along with an optional list of tags and tag values or an error string.  Works only with Zabbix versions 4.4 or newer. |
| **webhook_timeout**  string | Can be used when *type=webhook*.  Execution timeout for JavaScript code in *webhook_script*.  Possible values are 1-60s.  Default: `"30s"` |

## [Notes](zabbix_mediatype_module.md#id4)

> **Note:**
>
> - If you use *login_password=zabbix*, the word “zabbix” is replaced by “\*\*\*\*\*\*\*\*” in all module output, because *login_password* uses `no_log`. See [this FAQ](https://docs.ansible.com/ansible/latest/network/user_guide/faq.html#why-is-my-output-sometimes-replaced-with) for more information.

## [Examples](zabbix_mediatype_module.md#id5)

```yaml+jinja
# Set following variables for Zabbix Server host in play or inventory
- name: Set connection specific variables
  set_fact:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 80
    ansible_httpapi_use_ssl: false
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: 'zabbixeu'  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu

# If you want to use Username and Password to be authenticated by Zabbix Server
- name: Set credentials to access Zabbix Server API
  set_fact:
    ansible_user: Admin
    ansible_httpapi_pass: zabbix

# If you want to use API token to be authenticated by Zabbix Server
# https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/administration/general#api-tokens
- name: Set API token
  set_fact:
    ansible_zabbix_auth_key: 8ec0d52432c15c91fcafe9888500cf9a607f44091ab554dbee860f6b44fac895

- name: 'Create an email mediatype with SMTP authentication'
  community.zabbix.zabbix_mediatype:
    name: "Ops email"
    type: 'email'
    smtp_server: 'example.com'
    smtp_server_port: 2000
    smtp_email: 'ops@example.com'
    smtp_authentication: true
    username: 'smtp_user'
    password: 'smtp_pass'

- name: 'Create a script mediatype'
  community.zabbix.zabbix_mediatype:
    name: "my script"
    type: 'script'
    script_name: 'my_script.py'
    script_params:
      - 'arg1'
      - 'arg2'

- name: 'Create a jabber mediatype'
  community.zabbix.zabbix_mediatype:
    name: "My jabber"
    type: 'jabber'
    username: 'jabber_id'
    password: 'jabber_pass'

- name: 'Create a SMS mediatype'
  community.zabbix.zabbix_mediatype:
    name: "My SMS Mediatype"
    type: 'sms'
    gsm_modem: '/dev/ttyS0'

# Supported since Zabbix 4.4
- name: 'Create a webhook mediatype'
  community.zabbix.zabbix_mediatype:
    name: "My webhook Mediatype"
    type: 'webhook'
    webhook_script: "{{ lookup('file', 'slack.js') }}"
    webhook_params:
      - name: alert_message
        value: '{ALERT.MESSAGE}'
      - name: zabbix_url
        value: '{$ZABBIX.URL}'
    process_tags: True
    event_menu: true
    event_menu_name: "Open in Slack: '{EVENT.TAGS.__channel_name}'"
    event_menu_url: '{EVENT.TAGS.__message_link}'

# Supported since Zabbix 5.0
- name: 'Create an email mediatype with message templates'
  community.zabbix.zabbix_mediatype:
    name: "Ops email"
    type: 'email'
    smtp_email: 'ops@example.com'
    message_templates:
      - eventsource: triggers
        recovery: operations
        subject: "Problem: {EVENT.NAME}"
        body: "Problem started at {EVENT.TIME} on {EVENT.DATE}\r\nProblem name: {EVENT.NAME}\r\n"
      - eventsource: triggers
        recovery: recovery_operations
        subject: "Resolved: {EVENT.NAME}"
        body: "Problem resolved at {EVENT.TIME} on {EVENT.DATE}\r\nProblem name: {EVENT.NAME}\r\n"
      - eventsource: triggers
        recovery: update_operations
        subject: "Updated problem: {EVENT.NAME}"
        body: "{USER.FULLNAME} {EVENT.UPDATE.ACTION} problem at {EVENT.UPDATE.DATE} {EVENT.UPDATE.TIME}.\r\n"
      - eventsource: discovery
        recovery: operations
        subject: "Discovery: {DISCOVERY.DEVICE.STATUS} {DISCOVERY.DEVICE.IPADDRESS}"
        body: "Discovery rule: {DISCOVERY.RULE.NAME}\r\n\r\nDevice IP: {DISCOVERY.DEVICE.IPADDRESS}"
      - eventsource: autoregistration
        recovery: operations
        subject: "Autoregistration: {HOST.HOST}"
        body: "Host name: {HOST.HOST}\r\nHost IP: {HOST.IP}\r\nAgent port: {HOST.PORT}"
```

### Authors

- Ruben Tsirunyan (@rubentsirunyan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
[Homepage](https://github.com/ansible-collections/community.zabbix)
[Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
