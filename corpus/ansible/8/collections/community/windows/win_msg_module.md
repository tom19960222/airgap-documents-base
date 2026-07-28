---
collection: ansible
version: "8"
title: "community.windows.win_msg module – Sends a message to logged in users on Windows hosts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_msg_module.html
fetched_at: 2026-07-28T02:02:06+00:00
---
# community.windows.win_msg module – Sends a message to logged in users on Windows hosts

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/ui/repo/published/community/windows/) (version 1.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_msg`.

- [Synopsis](win_msg_module.md#synopsis)
- [Parameters](win_msg_module.md#parameters)
- [Notes](win_msg_module.md#notes)
- [See Also](win_msg_module.md#see-also)
- [Examples](win_msg_module.md#examples)
- [Return Values](win_msg_module.md#return-values)

## [Synopsis](win_msg_module.md#id1)

- Wraps the msg.exe command in order to send messages to Windows hosts.

## [Parameters](win_msg_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **display_seconds**  integer | How long to wait for receiver to acknowledge message, in seconds.  **Default:** `10` |
| **msg**  string | The text of the message to be displayed.  The message must be less than 256 characters.  **Default:** `"Hello world!"` |
| **to**  string | Who to send the message to. Can be a username, sessionname or sessionid.  **Default:** `"*"` |
| **wait**  boolean | Whether to wait for users to respond. Module will only wait for the number of seconds specified in display_seconds or 10 seconds if not specified. However, if *wait* is `yes`, the message is sent to each logged on user in turn, waiting for the user to either press ‘ok’ or for the timeout to elapse before moving on to the next user.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](win_msg_module.md#id3)

> **Note:**
>
> - This module must run on a windows host, so ensure your play targets windows hosts, or delegates to a windows host.
> - Messages are only sent to the local host where the module is run.
> - The module does not support sending to users listed in a file.
> - Setting wait to `yes` can result in long run times on systems with many logged in users.

## [See Also](win_msg_module.md#id4)

> **See also:**
>
> [community.windows.win_say](win_say_module.md#ansible-collections-community-windows-win-say-module)
> :   Text to speech module for Windows to speak messages and optionally play sounds.
>
> [community.windows.win_toast](win_toast_module.md#ansible-collections-community-windows-win-toast-module)
> :   Sends Toast windows notification to logged in users on Windows 10 or later hosts.

## [Examples](win_msg_module.md#id5)

```yaml+jinja
- name: Warn logged in users of impending upgrade
  community.windows.win_msg:
    display_seconds: 60
    msg: Automated upgrade about to start.  Please save your work and log off before {{ deployment_start_time }}
```

## [Return Values](win_msg_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **display_seconds**  string | Value of display_seconds module parameter.  **Returned:** success  **Sample:** `"10"` |
| **msg**  string | Test of the message that was sent.  **Returned:** changed  **Sample:** `"Automated upgrade about to start.  Please save your work and log off before 22 July 2016 18:00:00"` |
| **rc**  integer | The return code of the API call.  **Returned:** always  **Sample:** `0` |
| **runtime_seconds**  string | How long the module took to run on the remote windows host.  **Returned:** success  **Sample:** `"22 July 2016 17:45:51"` |
| **sent_localtime**  string | local time from windows host when the message was sent.  **Returned:** success  **Sample:** `"22 July 2016 17:45:51"` |
| **wait**  boolean | Value of wait module parameter.  **Returned:** success  **Sample:** `false` |

### Authors

- Jon Hawkesworth (@jhawkesworth)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
