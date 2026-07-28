---
collection: ansible
version: "8"
title: "community.general.mail callback – Sends failure events via email"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/mail_callback.html
fetched_at: 2026-07-28T01:52:01+00:00
---
# community.general.mail callback – Sends failure events via email

> **Note:**
>
> This callback plugin is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this callback plugin,
> see [Requirements](mail_callback.md#ansible-collections-community-general-mail-callback-requirements) for details.
>
> To use it in a playbook, specify: `community.general.mail`.

- [Callback plugin](mail_callback.md#callback-plugin)
- [Synopsis](mail_callback.md#synopsis)
- [Requirements](mail_callback.md#requirements)
- [Parameters](mail_callback.md#parameters)

## [Callback plugin](mail_callback.md#id1)

This plugin is a **notification callback**. It sends information for a playbook run to other applications, services, or systems.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](mail_callback.md#id2)

- This callback will report failures via email.

## [Requirements](mail_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- whitelisting in configuration

## [Parameters](mail_callback.md#id4)

| Parameter | Comments |
| --- | --- |
| **bcc**  list / elements=string | BCC’d recipients.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_mail]   bcc = VALUE   ``` |
| **cc**  list / elements=string | CC’d recipients.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_mail]   cc = VALUE   ``` |
| **mta**  string | Mail Transfer Agent, server that accepts SMTP.  **Default:** `"localhost"`  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_mail]   smtphost = localhost   ``` - Environment variable: [`SMTPHOST`](../../environment_variables.md#envvar-SMTPHOST) |
| **mtaport**  integer | Mail Transfer Agent Port.  Port at which server SMTP.  **Default:** `25`  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_mail]   smtpport = 25   ``` |
| **sender**  string / required | Mail sender.  This is required since community.general 6.0.0.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_mail]   sender = VALUE   ``` |
| **to**  list / elements=string | Mail recipient.  **Default:** `["root"]`  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_mail]   to = root   ``` |

### Authors

- Dag Wieers (@dagwieers)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
