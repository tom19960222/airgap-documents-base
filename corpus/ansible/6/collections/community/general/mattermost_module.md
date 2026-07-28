---
collection: ansible
version: "6"
title: "community.general.mattermost module – Send Mattermost notifications"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/mattermost_module.html
fetched_at: 2026-07-27T17:10:53+00:00
---
# community.general.mattermost module – Send Mattermost notifications

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
> To use it in a playbook, specify: `community.general.mattermost`.

- [Synopsis](mattermost_module.md#synopsis)
- [Parameters](mattermost_module.md#parameters)
- [Examples](mattermost_module.md#examples)
- [Return Values](mattermost_module.md#return-values)

## [Synopsis](mattermost_module.md#id1)

- Sends notifications to <http://your.mattermost.url> via the Incoming WebHook integration.

## [Parameters](mattermost_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_key**  string / required | Mattermost webhook api key. Log into your mattermost site, go to Menu -> Integration -> Incoming Webhook -> Add Incoming Webhook. This will give you full URL. api_key is the last part. <http://mattermost.example.com/hooks/>`API_KEY` |
| **attachments**  list / elements=dictionary  added in community.general 4.3.0 | Define a list of attachments.  For more information, see <https://developers.mattermost.com/integrate/admin-guide/admin-message-attachments/>.  Required when *text* is not set. |
| **channel**  string | Channel to send the message to. If absent, the message goes to the channel selected for the *api_key*. |
| **icon_url**  string | Url for the message sender’s icon.  Default: `"https://www.ansible.com/favicon.ico"` |
| **text**  string | Text to send. Note that the module does not handle escaping characters.  Required when *attachments* is not set. |
| **url**  string / required | Mattermost url (i.e. <http://mattermost.yourcompany.com>). |
| **username**  string | This is the sender of the message (Username Override need to be enabled by mattermost admin, see mattermost doc.  Default: `"Ansible"` |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Examples](mattermost_module.md#id3)

```yaml+jinja
- name: Send notification message via Mattermost
  community.general.mattermost:
    url: http://mattermost.example.com
    api_key: my_api_key
    text: '{{ inventory_hostname }} completed'

- name: Send notification message via Mattermost all options
  community.general.mattermost:
    url: http://mattermost.example.com
    api_key: my_api_key
    text: '{{ inventory_hostname }} completed'
    channel: notifications
    username: 'Ansible on {{ inventory_hostname }}'
    icon_url: http://www.example.com/some-image-file.png

- name: Send attachments message via Mattermost
  community.general.mattermost:
    url: http://mattermost.example.com
    api_key: my_api_key
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
```

## [Return Values](mattermost_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **payload**  string | Mattermost payload  Returned: success |
| **webhook_url**  string | URL the webhook is sent to  Returned: success |

### Authors

- Benjamin Jolivot (@bjolivot)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
