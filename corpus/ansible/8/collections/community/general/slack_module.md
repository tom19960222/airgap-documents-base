---
collection: ansible
version: "8"
title: "community.general.slack module – Send Slack notifications"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/slack_module.html
fetched_at: 2026-07-28T01:50:37+00:00
---
# community.general.slack module – Send Slack notifications

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
> To use it in a playbook, specify: `community.general.slack`.

- [Synopsis](slack_module.md#synopsis)
- [Parameters](slack_module.md#parameters)
- [Attributes](slack_module.md#attributes)
- [Examples](slack_module.md#examples)

## [Synopsis](slack_module.md#id1)

- The [community.general.slack](slack_module.md#ansible-collections-community-general-slack-module) module sends notifications to <http://slack.com> via the Incoming WebHook integration

Aliases: notification.slack

## [Parameters](slack_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **attachments**  list / elements=dictionary | Define a list of attachments. This list mirrors the Slack JSON API.  For more information, see <https://api.slack.com/docs/attachments>. |
| **blocks**  list / elements=dictionary  *added in community.general 1.0.0* | Define a list of blocks. This list mirrors the Slack JSON API.  For more information, see <https://api.slack.com/block-kit>. |
| **channel**  string | Channel to send the message to. If absent, the message goes to the channel selected for the `token`. |
| **color**  string | Allow text to use default colors - use the default of ‘normal’ to not send a custom color bar at the start of the message.  Allowed values for color can be one of ‘normal’, ‘good’, ‘warning’, ‘danger’, any valid 3 digit or 6 digit hex color value.  Specifying value in hex is supported since Ansible 2.8.  **Default:** `"normal"` |
| **domain**  string | Slack (sub)domain for your environment without protocol. (For example `example.slack.com`.) In Ansible 1.8 and beyond, this is deprecated and may be ignored. See token documentation for information. |
| **icon_emoji**  string | Emoji for the message sender. See Slack documentation for options.  If `icon_emoji` is set, `icon_url` will not be used. |
| **icon_url**  string | URL for the message sender’s icon.  **Default:** `"https://docs.ansible.com/favicon.ico"` |
| **link_names**  integer | Automatically create links for channels and usernames in `msg`.  **Choices:**   - `1` ← (default) - `0` |
| **message_id**  string  *added in community.general 1.2.0* | Optional. Message ID to edit, instead of posting a new message.  If supplied `channel` must be in form of `C0xxxxxxx`. use `{{ slack_response.channel_id }}` to get `channel_id` from previous task run.  Corresponds to `ts` in the Slack API (<https://api.slack.com/messaging/modifying>). |
| **msg**  string | Message to send. Note that the module does not handle escaping characters. Plain-text angle brackets and ampersands should be converted to HTML entities (e.g. & to &amp;) before sending. See Slack’s documentation (<https://api.slack.com/docs/message-formatting>) for more. |
| **parse**  string | Setting for the message parser at Slack  **Choices:**   - `"full"` - `"none"` |
| **prepend_hash**  string  *added in community.general 6.1.0* | Setting for automatically prepending a `#` symbol on the passed in `channel`.  The `auto` method prepends a `#` unless `channel` starts with one of `#`, `@`, `C0`, `GF`, `G0`, `CP`. These prefixes only cover a small set of the prefixes that should not have a `#` prepended. Since an exact condition which `channel` values must not have the `#` prefix is not known, the value `auto` for this option will be deprecated in the future. It is best to explicitly set `prepend_hash=always` or `prepend_hash=never` to obtain the needed behavior.  **Choices:**   - `"always"` - `"never"` - `"auto"` ← (default) |
| **thread_id**  string | Optional. Timestamp of parent message to thread this message. <https://api.slack.com/docs/message-threading> |
| **token**  string / required | Slack integration token. This authenticates you to the slack service. Make sure to use the correct type of token, depending on what method you use.  Webhook token: Prior to Ansible 1.8, a token looked like `3Ffe373sfhRE6y42Fg3rvf4GlK`. In Ansible 1.8 and above, Ansible adapts to the new slack API where tokens look like `G922VJP24/D921DW937/3Ffe373sfhRE6y42Fg3rvf4GlK`. If tokens are in the new format then slack will ignore any value of domain. If the token is in the old format the domain is required. Ansible has no control of when slack will get rid of the old API. When slack does that the old format will stop working. \*\* Please keep in mind the tokens are not the API tokens but are the webhook tokens. In slack these are found in the webhook URL which are obtained under the apps and integrations. The incoming webhooks can be added in that area. In some cases this may be locked by your Slack admin and you must request access. It is there that the incoming webhooks can be added. The key is on the end of the URL given to you in that section.  WebAPI token: Slack WebAPI requires a personal, bot or work application token. These tokens start with `xoxp-`, `xoxb-` or `xoxa-`, for example `xoxb-1234-56789abcdefghijklmnop`. WebAPI token is required if you intend to receive thread_id. See Slack’s documentation (<https://api.slack.com/docs/token-types>) for more information. |
| **username**  string | This is the sender of the message.  **Default:** `"Ansible"` |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](slack_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](slack_module.md#id4)

```yaml+jinja
- name: Send notification message via Slack
  community.general.slack:
    token: thetoken/generatedby/slack
    msg: '{{ inventory_hostname }} completed'
  delegate_to: localhost

- name: Send notification message via Slack all options
  community.general.slack:
    token: thetoken/generatedby/slack
    msg: '{{ inventory_hostname }} completed'
    channel: '#ansible'
    thread_id: '1539917263.000100'
    username: 'Ansible on {{ inventory_hostname }}'
    icon_url: http://www.example.com/some-image-file.png
    link_names: 0
    parse: 'none'
  delegate_to: localhost

- name: Insert a color bar in front of the message for visibility purposes and use the default webhook icon and name configured in Slack
  community.general.slack:
    token: thetoken/generatedby/slack
    msg: '{{ inventory_hostname }} is alive!'
    color: good
    username: ''
    icon_url: ''

- name: Insert a color bar in front of the message with valid hex color value
  community.general.slack:
    token: thetoken/generatedby/slack
    msg: 'This message uses color in hex value'
    color: '#00aacc'
    username: ''
    icon_url: ''

- name: Use the attachments API
  community.general.slack:
    token: thetoken/generatedby/slack
    attachments:
      - text: Display my system load on host A and B
        color: '#ff00dd'
        title: System load
        fields:
          - title: System A
            value: "load average: 0,74, 0,66, 0,63"
            short: true
          - title: System B
            value: 'load average: 5,16, 4,64, 2,43'
            short: true

- name: Use the blocks API
  community.general.slack:
    token: thetoken/generatedby/slack
    blocks:
      - type: section
        text:
          type: mrkdwn
          text: |-
            *System load*
            Display my system load on host A and B
      - type: context
        elements:
        - type: mrkdwn
          text: |-
            *System A*
            load average: 0,74, 0,66, 0,63
        - type: mrkdwn
          text: |-
            *System B*
            load average: 5,16, 4,64, 2,43

- name: Send a message with a link using Slack markup
  community.general.slack:
    token: thetoken/generatedby/slack
    msg: We sent this message using <https://www.ansible.com|Ansible>!

- name: Send a message with angle brackets and ampersands
  community.general.slack:
    token: thetoken/generatedby/slack
    msg: This message has &lt;brackets&gt; &amp; ampersands in plain text.

- name: Initial Threaded Slack message
  community.general.slack:
    channel: '#ansible'
    token: xoxb-1234-56789abcdefghijklmnop
    msg: 'Starting a thread with my initial post.'
  register: slack_response
- name: Add more info to thread
  community.general.slack:
    channel: '#ansible'
    token: xoxb-1234-56789abcdefghijklmnop
    thread_id: "{{ slack_response['ts'] }}"
    color: good
    msg: 'And this is my threaded response!'

- name: Send a message to be edited later on
  community.general.slack:
    token: thetoken/generatedby/slack
    channel: '#ansible'
    msg: Deploying something...
  register: slack_response
- name: Edit message
  community.general.slack:
    token: thetoken/generatedby/slack
    # The 'channel' option does not accept the channel name. It must use the 'channel_id',
    # which can be retrieved for example from 'slack_response' from the previous task.
    channel: "{{ slack_response.channel }}"
    msg: Deployment complete!
    message_id: "{{ slack_response.ts }}"
```

### Authors

- Ramon de la Fuente (@ramondelafuente)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
