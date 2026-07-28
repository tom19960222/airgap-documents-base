---
collection: ansible
version: "8"
title: "awx.awx.notification_template module – create, update, or destroy Automation Platform Controller notification."
source_url: https://docs.ansible.com/projects/ansible/8/collections/awx/awx/notification_template_module.html
fetched_at: 2026-07-28T01:11:39+00:00
---
# awx.awx.notification_template module – create, update, or destroy Automation Platform Controller notification.

> **Note:**
>
> This module is part of the [awx.awx collection](https://galaxy.ansible.com/ui/repo/published/awx/awx/) (version 22.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install awx.awx`.
>
> To use it in a playbook, specify: `awx.awx.notification_template`.

- [Synopsis](notification_template_module.md#synopsis)
- [Parameters](notification_template_module.md#parameters)
- [Notes](notification_template_module.md#notes)
- [Examples](notification_template_module.md#examples)

## [Synopsis](notification_template_module.md#id1)

- Create, update, or destroy Automation Platform Controller notifications. See <https://www.ansible.com/tower> for an overview.

Aliases: tower_notification, tower_notification_template

## [Parameters](notification_template_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **controller_config_file**  aliases: tower_config_file  path | Path to the controller config file.  If provided, the other locations for config files will not be considered. |
| **controller_host**  aliases: tower_host  string | URL to your Automation Platform Controller instance.  If value not set, will try environment variable `CONTROLLER_HOST` and then config files  If value not specified by any means, the value of `127.0.0.1` will be used |
| **controller_oauthtoken**  aliases: tower_oauthtoken  any  *added in awx.awx 3.7.0* | The OAuth token to use.  This value can be in one of two formats.  A string which is the token itself. (i.e. bqV5txm97wqJqtkxlMkhQz0pKhRMMX)  A dictionary structure as returned by the token module.  If value not set, will try environment variable `CONTROLLER_OAUTH_TOKEN` and then config files |
| **controller_password**  aliases: tower_password  string | Password for your controller instance.  If value not set, will try environment variable `CONTROLLER_PASSWORD` and then config files |
| **controller_username**  aliases: tower_username  string | Username for your controller instance.  If value not set, will try environment variable `CONTROLLER_USERNAME` and then config files |
| **copy_from**  string | Name or id to copy the notification from.  This will copy an existing notification and change any parameters supplied.  The new notification name will be the one provided in the name parameter.  The organization parameter is not used in this, to facilitate copy from one organization to another.  Provide the id or use the lookup plugin to provide the id if multiple notifications share the same name. |
| **description**  string | The description of the notification. |
| **messages**  dictionary | Optional custom messages for notification template. |
| **name**  string / required | The name of the notification. |
| **new_name**  string | Setting this option will change the existing name (looked up via the name field. |
| **notification_configuration**  dictionary | The notification configuration file. Note providing this field would disable all notification-configuration-related fields.  username (the mail server username)  sender (the sender email address)  recipients (the recipients email addresses)  use_tls (the TLS trigger)  host (the mail server host)  use_ssl (the SSL trigger)  password (the mail server password)  port (the mail server port)  channels (the destination Slack channels)  token (the access token)  account_token (the Twillio account token)  from_number (the source phone number)  to_numbers (the destination phone numbers)  account_sid (the Twillio account SID)  subdomain (the PagerDuty subdomain)  service_key (the PagerDuty service/integration API key)  client_name (the PagerDuty client identifier)  message_from (the label to be shown with the notification)  color (the notification color)  notify (the notify channel trigger)  url (the target URL)  headers (the HTTP headers as JSON string)  server (the IRC server address)  nickname (the IRC nickname)  targets (the destination channels or users) |
| **notification_type**  string | The type of notification to be sent.  **Choices:**   - `"email"` - `"grafana"` - `"irc"` - `"mattermost"` - `"pagerduty"` - `"rocketchat"` - `"slack"` - `"twilio"` - `"webhook"` |
| **organization**  string | The organization name, ID, or named URL the notification belongs to. |
| **request_timeout**  float | Specify the timeout Ansible should use in requests to the controller host.  Defaults to 10s, but this is handled by the shared module_utils code |
| **state**  string | Desired state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"exists"` |
| **validate_certs**  aliases: tower_verify_ssl  boolean | Whether to allow insecure connections to AWX.  If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  If value not set, will try environment variable `CONTROLLER_VERIFY_SSL` and then config files  **Choices:**   - `false` - `true` |

## [Notes](notification_template_module.md#id3)

> **Note:**
>
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](notification_template_module.md#id4)

```yaml+jinja
- name: Add Slack notification with custom messages
  notification_template:
    name: slack notification
    organization: Default
    notification_type: slack
    notification_configuration:
      channels:
        - general
      token: cefda9e2be1f21d11cdd9452f5b7f97fda977f42
    messages:
       started:
         message: "{{ '{{ job_friendly_name }}{{ job.id }} started' }}"
       success:
         message: "{{ '{{ job_friendly_name }} completed in {{ job.elapsed }} seconds' }}"
       error:
         message: "{{ '{{ job_friendly_name }} FAILED! Please look at {{ job.url }}' }}"
    state: present
    controller_config_file: "~/tower_cli.cfg"

- name: Add webhook notification
  notification_template:
    name: webhook notification
    notification_type: webhook
    notification_configuration:
      url: http://www.example.com/hook
      headers:
        X-Custom-Header: value123
    state: present
    controller_config_file: "~/tower_cli.cfg"

- name: Add email notification
  notification_template:
    name: email notification
    notification_type: email
    notification_configuration:
      username: user
      password: s3cr3t
      sender: controller@example.com
      recipients:
        - user1@example.com
      host: smtp.example.com
      port: 25
      use_tls: no
      use_ssl: no
    state: present
    controller_config_file: "~/tower_cli.cfg"

- name: Add twilio notification
  notification_template:
    name: twilio notification
    notification_type: twilio
    notification_configuration:
      account_token: a_token
      account_sid: a_sid
      from_number: '+15551112222'
      to_numbers:
        - '+15553334444'
    state: present
    controller_config_file: "~/tower_cli.cfg"

- name: Add PagerDuty notification
  notification_template:
    name: pagerduty notification
    notification_type: pagerduty
    notification_configuration:
      token: a_token
      subdomain: sub
      client_name: client
      service_key: a_key
    state: present
    controller_config_file: "~/tower_cli.cfg"

- name: Add IRC notification
  notification_template:
    name: irc notification
    notification_type: irc
    notification_configuration:
      nickname: controller
      password: s3cr3t
      targets:
        - user1
      port: 8080
      server: irc.example.com
      use_ssl: no
    state: present
    controller_config_file: "~/tower_cli.cfg"

- name: Delete notification
  notification_template:
    name: old notification
    state: absent
    controller_config_file: "~/tower_cli.cfg"

- name: Copy webhook notification
  notification_template:
    name: foo notification
    copy_from: email notification
    organization: Foo
```

### Authors

- Samuel Carpentier (@samcarpentier)

### Collection links

- [Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
- [Homepage](https://www.ansible.com/)
- [Repository (Sources)](https://github.com/ansible/awx)
