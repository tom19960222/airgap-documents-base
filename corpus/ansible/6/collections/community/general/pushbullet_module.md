---
collection: ansible
version: "6"
title: "community.general.pushbullet module – Sends notifications to Pushbullet"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/pushbullet_module.html
fetched_at: 2026-07-27T17:12:15+00:00
---
# community.general.pushbullet module – Sends notifications to Pushbullet

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](pushbullet_module.md#ansible-collections-community-general-pushbullet-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.pushbullet`.

- [Synopsis](pushbullet_module.md#synopsis)
- [Requirements](pushbullet_module.md#requirements)
- [Parameters](pushbullet_module.md#parameters)
- [Notes](pushbullet_module.md#notes)
- [Examples](pushbullet_module.md#examples)

## [Synopsis](pushbullet_module.md#id1)

- This module sends push notifications via Pushbullet to channels or devices.

## [Requirements](pushbullet_module.md#id2)

The below requirements are needed on the host that executes this module.

- pushbullet.py

## [Parameters](pushbullet_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_key**  string / required | Push bullet API token |
| **body**  string | Body of the notification, e.g. Details of the fault you’re alerting. |
| **channel**  string | The channel TAG you wish to broadcast a push notification, as seen on the “My Channels” > “Edit your channel” at Pushbullet page. |
| **device**  string | The device NAME you wish to send a push notification, as seen on the Pushbullet main page. |
| **push_type**  string | Thing you wish to push.  Choices:   - `"note"` ← (default) - `"link"` |
| **title**  string / required | Title of the notification. |
| **url**  string | URL field, used when *push_type* is `link`. |

## [Notes](pushbullet_module.md#id4)

> **Note:**
>
> - Requires pushbullet.py Python package on the remote host. You can install it via pip with ($ pip install pushbullet.py). See <https://github.com/randomchars/pushbullet.py>

## [Examples](pushbullet_module.md#id5)

```yaml+jinja
- name: Sends a push notification to a device
  community.general.pushbullet:
    api_key: "ABC123abc123ABC123abc123ABC123ab"
    device: "Chrome"
    title: "You may see this on Google Chrome"

- name: Sends a link to a device
  community.general.pushbullet:
    api_key: ABC123abc123ABC123abc123ABC123ab
    device: Chrome
    push_type: link
    title: Ansible Documentation
    body: https://docs.ansible.com/

- name: Sends a push notification to a channel
  community.general.pushbullet:
    api_key: ABC123abc123ABC123abc123ABC123ab
    channel: my-awesome-channel
    title: Broadcasting a message to the #my-awesome-channel folks

- name: Sends a push notification with title and body to a channel
  community.general.pushbullet:
    api_key: ABC123abc123ABC123abc123ABC123ab
    channel: my-awesome-channel
    title: ALERT! Signup service is down
    body: Error rate on signup service is over 90% for more than 2 minutes
```

### Authors

- Willy Barro (@willybarro)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
