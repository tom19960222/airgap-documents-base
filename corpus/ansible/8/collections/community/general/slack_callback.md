---
collection: ansible
version: "8"
title: "community.general.slack callback – Sends play events to a Slack channel"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/slack_callback.html
fetched_at: 2026-07-28T01:52:05+00:00
---
# community.general.slack callback – Sends play events to a Slack channel

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
> see [Requirements](slack_callback.md#ansible-collections-community-general-slack-callback-requirements) for details.
>
> To use it in a playbook, specify: `community.general.slack`.

- [Callback plugin](slack_callback.md#callback-plugin)
- [Synopsis](slack_callback.md#synopsis)
- [Requirements](slack_callback.md#requirements)
- [Parameters](slack_callback.md#parameters)

## [Callback plugin](slack_callback.md#id1)

This plugin is a **notification callback**. It sends information for a playbook run to other applications, services, or systems.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](slack_callback.md#id2)

- This is an ansible callback plugin that sends status updates to a Slack channel during playbook execution.
- Before Ansible 2.4 only environment variables were available for configuring this plugin.

## [Requirements](slack_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- whitelist in configuration
- prettytable (python library)

## [Parameters](slack_callback.md#id4)

| Parameter | Comments |
| --- | --- |
| **channel**  string | Slack room to post in.  **Default:** `"#ansible"`  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_slack]   channel = #ansible   ``` - Environment variable: [`SLACK_CHANNEL`](../../environment_variables.md#envvar-SLACK_CHANNEL) |
| **username**  string | Username to post as.  **Default:** `"ansible"`  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_slack]   username = ansible   ``` - Environment variable: [`SLACK_USERNAME`](../../environment_variables.md#envvar-SLACK_USERNAME) |
| **validate_certs**  boolean | Validate the SSL certificate of the Slack server for HTTPS URLs.  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_slack]   validate_certs = true   ``` - Environment variable: [`SLACK_VALIDATE_CERTS`](../../environment_variables.md#envvar-SLACK_VALIDATE_CERTS) |
| **webhook_url**  string / required | Slack Webhook URL.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_slack]   webhook_url = VALUE   ``` - Environment variable: [`SLACK_WEBHOOK_URL`](../../environment_variables.md#envvar-SLACK_WEBHOOK_URL) |

### Authors

- Unknown

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
