---
collection: ansible
version: "6"
title: "community.windows.win_toast module – Sends Toast windows notification to logged in users on Windows 10 or later hosts"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_toast_module.html
fetched_at: 2026-07-27T17:24:00+00:00
---
# community.windows.win_toast module – Sends Toast windows notification to logged in users on Windows 10 or later hosts

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/community/windows) (version 1.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_toast`.

- [Synopsis](win_toast_module.md#synopsis)
- [Parameters](win_toast_module.md#parameters)
- [Notes](win_toast_module.md#notes)
- [See Also](win_toast_module.md#see-also)
- [Examples](win_toast_module.md#examples)
- [Return Values](win_toast_module.md#return-values)

## [Synopsis](win_toast_module.md#id1)

- Sends alerts which appear in the Action Center area of the windows desktop.

## [Parameters](win_toast_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **expire**  integer | How long in seconds before the notification expires.  Default: `45` |
| **group**  string | Which notification group to add the notification to.  Default: `"Powershell"` |
| **msg**  string | The message to appear inside the notification.  May include \n to format the message to appear within the Action Center.  Default: `"Hello, World!"` |
| **popup**  boolean | If `no`, the notification will not pop up and will only appear in the Action Center.  Choices:   - `false` - `true` ← (default) |
| **tag**  string | The tag to add to the notification.  Default: `"Ansible"` |
| **title**  string | The notification title, which appears in the pop up..  Default: `"Notification HH:mm"` |

## [Notes](win_toast_module.md#id3)

> **Note:**
>
> - This module must run on a windows 10 or Server 2016 host, so ensure your play targets windows hosts, or delegates to a windows host.
> - The module does not fail if there are no logged in users to notify.
> - Messages are only sent to the local host where the module is run.
> - You must run this module with async, otherwise it will hang until the expire period has passed.

## [See Also](win_toast_module.md#id4)

> **See also:**
>
> [community.windows.win_msg](win_msg_module.md#ansible-collections-community-windows-win-msg-module)
> :   Sends a message to logged in users on Windows hosts.
>
> [community.windows.win_say](win_say_module.md#ansible-collections-community-windows-win-say-module)
> :   Text to speech module for Windows to speak messages and optionally play sounds.

## [Examples](win_toast_module.md#id5)

```yaml+jinja
- name: Warn logged in users of impending upgrade (note use of async to stop the module from waiting until notification expires).
  community.windows.win_toast:
    expire: 60
    title: System Upgrade Notification
    msg: Automated upgrade about to start.  Please save your work and log off before {{ deployment_start_time }}
  async: 60
  poll: 0
```

## [Return Values](win_toast_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **expire_at_utc**  string | Calculated utc date time when the notification expires.  Returned: always  Sample: `"07 July 2017 04:50:54"` |
| **no_toast_sent_reason**  string | Text containing the reason why a notification was not sent.  Returned: when no logged in users are detected  Sample: `"No logged in users to notify"` |
| **sent_localtime**  string | local date time when the notification was sent.  Returned: always  Sample: `"07 July 2017 05:45:54"` |
| **time_taken**  float | How long the module took to run on the remote windows host in seconds.  Returned: always  Sample: `0.3706631999999997` |
| **toast_sent**  boolean | Whether the module was able to send a toast notification or not.  Returned: always  Sample: `false` |

### Authors

- Jon Hawkesworth (@jhawkesworth)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
