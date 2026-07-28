---
collection: ansible
version: "6"
title: "community.grafana.grafana_notification_channel module – Manage Grafana Notification Channels"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/grafana/grafana_notification_channel_module.html
fetched_at: 2026-07-27T17:15:27+00:00
---
# community.grafana.grafana_notification_channel module – Manage Grafana Notification Channels

> **Note:**
>
> This module is part of the [community.grafana collection](https://galaxy.ansible.com/community/grafana) (version 1.5.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.grafana`.
>
> To use it in a playbook, specify: `community.grafana.grafana_notification_channel`.

New in community.grafana 1.1.0

- [Synopsis](grafana_notification_channel_module.md#synopsis)
- [Parameters](grafana_notification_channel_module.md#parameters)
- [Notes](grafana_notification_channel_module.md#notes)
- [Examples](grafana_notification_channel_module.md#examples)
- [Return Values](grafana_notification_channel_module.md#return-values)

## [Synopsis](grafana_notification_channel_module.md#id1)

- Create/Update/Delete Grafana Notification Channels via API.

## [Parameters](grafana_notification_channel_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **client_cert**  path | PEM formatted certificate chain file to be used for SSL client authentication.  This file can also include the key as well, and if the key is included, *client_key* is not required |
| **client_key**  path | PEM formatted file that contains your private key to be used for SSL client authentication.  If *client_cert* contains both the certificate and key, this option is not required. |
| **dingding_message_type**  list / elements=string | DingDing message type.  Choices:   - `"link"` - `"action_card"` |
| **dingding_url**  string | DingDing webhook URL. |
| **disable_resolve_message**  boolean | Disable the resolve message.  Choices:   - `false` ← (default) - `true` |
| **discord_message_content**  string | Overrides message content. |
| **discord_url**  string | Discord webhook URL. |
| **email_addresses**  list / elements=string | List of recipients. |
| **email_single**  boolean | Send single email to all recipients.  Choices:   - `false` - `true` |
| **googlechat_url**  string | Google Hangouts webhook URL. |
| **grafana_api_key**  string | The Grafana API key.  If set, `url_username` and `url_password` will be ignored. |
| **hipchat_api_key**  string | HipChat API key. |
| **hipchat_room_id**  string | HipChat room ID. |
| **hipchat_url**  string | HipChat webhook URL. |
| **include_image**  boolean | Capture a visualization image and attach it to notifications.  Choices:   - `false` ← (default) - `true` |
| **is_default**  boolean | Use this channel for all alerts.  Choices:   - `false` ← (default) - `true` |
| **kafka_topic**  string | Kafka topic name. |
| **kafka_url**  string | Kafka REST proxy URL. |
| **line_token**  string | LINE token. |
| **name**  string | The name of the notification channel.  Required when *state* is `present`. |
| **opsgenie_api_key**  string | OpsGenie API key. |
| **opsgenie_auto_close**  boolean | Automatically close alerts in OpsGenie once the alert goes back to ok.  Choices:   - `false` - `true` |
| **opsgenie_override_priority**  boolean | Allow the alert priority to be set using the og_priority tag.  Choices:   - `false` - `true` |
| **opsgenie_url**  string | OpsGenie webhook URL. |
| **org_id**  integer | The Grafana Organisation ID where the dashboard will be imported / exported.  Not used when *grafana_api_key* is set, because the grafana_api_key only belongs to one organisation..  Default: `1` |
| **pagerduty_auto_resolve**  boolean | Resolve incidents in PagerDuty once the alert goes back to ok.  Choices:   - `false` - `true` |
| **pagerduty_integration_key**  string | PagerDuty integration key. |
| **pagerduty_message_in_details**  boolean | Move the alert message from the PD summary into the custom details.  This changes the custom details object and may break event rules you have configured.  Choices:   - `false` - `true` |
| **pagerduty_severity**  list / elements=string | Alert severity in PagerDuty.  Choices:   - `"critical"` - `"error"` - `"warning"` - `"info"` |
| **prometheus_password**  string | Prometheus password. |
| **prometheus_url**  string | Prometheus API URL. |
| **prometheus_username**  string | Prometheus username. |
| **pushover_alert_sound**  string | [Alert sound in Pushover](https://pushover.net/api#sounds) |
| **pushover_api_token**  string | Pushover API token. |
| **pushover_devices**  list / elements=string | Devices list in Pushover. |
| **pushover_expire**  integer | Expire alert in `n` minutes.  Only when priority is `emergency`. |
| **pushover_ok_sound**  string | [OK sound in Pushover](https://pushover.net/api#sounds) |
| **pushover_priority**  list / elements=string | Alert priority in Pushover.  Choices:   - `"emergency"` - `"high"` - `"normal"` - `"low"` - `"lowest"` |
| **pushover_retry**  integer | Retry in `n` minutes.  Only when priority is `emergency`. |
| **pushover_user_key**  string | Pushover user key. |
| **reminder_frequency**  string | Additional notifications interval for triggered alerts.  For example `15m`. |
| **sensu_handler**  string | Sensu handler name. |
| **sensu_password**  string | Sensu password. |
| **sensu_source**  string | Source in Sensu. |
| **sensu_url**  string | Sensu webhook URL. |
| **sensu_username**  string | Sensu user. |
| **slack_icon_emoji**  string | An emoji to use for the bot’s message. |
| **slack_icon_url**  string | URL to an image to use as the icon for the bot’s message |
| **slack_mention_channel**  list / elements=string | Mention whole channel or just active members.  Choices:   - `"here"` - `"channel"` |
| **slack_mention_groups**  list / elements=string | Mention groups list. |
| **slack_mention_users**  list / elements=string | Mention users list. |
| **slack_recipient**  string | Override default Slack channel or user. |
| **slack_token**  string | Slack token. |
| **slack_url**  string | Slack webhook URL. |
| **slack_username**  string | Set the username for the bot’s message. |
| **state**  string | Status of the notification channel.  Choices:   - `"present"` ← (default) - `"absent"` |
| **teams_url**  string | Microsoft Teams webhook URL. |
| **telegram_bot_token**  string | Telegram bot token; |
| **telegram_chat_id**  string | Telegram chat id. |
| **threema_api_secret**  string | Threema Gateway API secret. |
| **threema_gateway_id**  string | 8 character Threema Gateway ID (starting with a \*). |
| **threema_recipient_id**  string | 8 character Threema ID that should receive the alerts. |
| **type**  string | The channel notification type.  Required when *state* is `present`.  Choices:   - `"dingding"` - `"discord"` - `"email"` - `"googlechat"` - `"hipchat"` - `"kafka"` - `"line"` - `"teams"` - `"opsgenie"` - `"pagerduty"` - `"prometheus"` - `"pushover"` - `"sensu"` - `"slack"` - `"telegram"` - `"threema"` - `"victorops"` - `"webhook"` |
| **uid**  string | The channel unique identifier. |
| **url**  aliases: grafana_url  string / required | The Grafana URL. |
| **url_password**  aliases: grafana_password  string | The Grafana password for API authentication.  Default: `"admin"` |
| **url_username**  aliases: grafana_user  string | The Grafana user for API authentication.  Default: `"admin"` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` - `true` ← (default) |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **victorops_auto_resolve**  boolean | Resolve incidents in VictorOps once the alert goes back to ok.  Choices:   - `false` - `true` |
| **victorops_url**  string | VictorOps webhook URL. |
| **webhook_http_method**  list / elements=string | Webhook HTTP verb to use.  Choices:   - `"POST"` - `"PUT"` |
| **webhook_password**  string | Webhook password. |
| **webhook_url**  string | Webhook URL |
| **webhook_username**  string | Webhook username. |

## [Notes](grafana_notification_channel_module.md#id3)

> **Note:**
>
> - Notification channels are replaced by contact points starting Grafana 8.3 and this module is currently not able to manage contact points.
> - The module will report execution as successful since Grafana maintains backward compatibility with previous alert management, but
> - nothing will be visible in the contact points if new alerting mechanism is enabled.

## [Examples](grafana_notification_channel_module.md#id4)

```yaml+jinja
- name: Create slack notification channel
  register: result
  grafana_notification_channel:
    uid: slack
    name: slack
    type: slack
    slack_url: https://hooks.slack.com/services/xxx/yyy/zzz
    grafana_url: "{{ grafana_url }}"
    grafana_user: "{{ grafana_username }}"
    grafana_password: "{{ grafana_password}}"

- name: Delete slack notification channel
  register: result
  grafana_notification_channel:
    state: absent
    uid: slack
    grafana_url: "{{ grafana_url }}"
    grafana_user: "{{ grafana_username }}"
    grafana_password: "{{ grafana_password}}"
```

## [Return Values](grafana_notification_channel_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **notification_channel**  dictionary | Notification channel created or updated by the module.  Returned: changed  Sample: `{"created": "2020-11-10T21:10:19.675308051+03:00", "disableResolveMessage": false, "frequency": "", "id": 37, "isDefault": false, "name": "Oops", "secureFields": {}, "sendReminder": false, "settings": {"uploadImage": false, "url": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"}, "type": "slack", "uid": "slack-oops", "updated": "2020-11-10T21:10:19.675308112+03:00"}` |

### Authors

- Aliaksandr Mianzhynski (@amenzhinsky)
- Rémi REY (@rrey)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/grafana/issues)
[Homepage](https://github.com/ansible-collections/grafana)
[Repository (Sources)](https://github.com/ansible-collections/grafana.git)
