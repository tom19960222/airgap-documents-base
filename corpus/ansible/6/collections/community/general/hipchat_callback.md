---
collection: ansible
version: "6"
title: "community.general.hipchat callback – post task events to hipchat"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/hipchat_callback.html
fetched_at: 2026-07-27T17:14:28+00:00
---
# community.general.hipchat callback – post task events to hipchat

> **Note:**
>
> This callback plugin is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this callback plugin,
> see [Requirements](hipchat_callback.md#ansible-collections-community-general-hipchat-callback-requirements) for details.
>
> To use it in a playbook, specify: `community.general.hipchat`.

- [Callback plugin](hipchat_callback.md#callback-plugin)
- [Synopsis](hipchat_callback.md#synopsis)
- [Requirements](hipchat_callback.md#requirements)
- [Parameters](hipchat_callback.md#parameters)

## [Callback plugin](hipchat_callback.md#id1)

This plugin is a **notification callback**. It sends information for a playbook run to other applications, services, or systems.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](hipchat_callback.md#id2)

- This callback plugin sends status updates to a HipChat channel during playbook execution.
- Before 2.4 only environment variables were available for configuring this plugin.

## [Requirements](hipchat_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- whitelist in configuration.
- prettytable (python lib)

## [Parameters](hipchat_callback.md#id4)

| Parameter | Comments |
| --- | --- |
| **api_version**  string | HipChat API version, v1 or v2.  Default: `"v1"`  Configuration:   - INI entry:  ```YAML+Jinja   [callback_hipchat]   api_version = v1   ``` - Environment variable: [`HIPCHAT_API_VERSION`](../../environment_variables.md#envvar-HIPCHAT_API_VERSION) |
| **from**  string | Name to post as  Default: `"ansible"`  Configuration:   - INI entry:  ```YAML+Jinja   [callback_hipchat]   from = ansible   ``` - Environment variable: [`HIPCHAT_FROM`](../../environment_variables.md#envvar-HIPCHAT_FROM) |
| **notify**  boolean | Add notify flag to important messages  Choices:   - `false` - `true` ← (default)   Configuration:   - INI entry:  ```YAML+Jinja   [callback_hipchat]   notify = true   ``` - Environment variable: [`HIPCHAT_NOTIFY`](../../environment_variables.md#envvar-HIPCHAT_NOTIFY) |
| **room**  string | HipChat room to post in.  Default: `"ansible"`  Configuration:   - INI entry:  ```YAML+Jinja   [callback_hipchat]   room = ansible   ``` - Environment variable: [`HIPCHAT_ROOM`](../../environment_variables.md#envvar-HIPCHAT_ROOM) |
| **token**  string / required | HipChat API token for v1 or v2 API.  Configuration:   - INI entry:  ```YAML+Jinja   [callback_hipchat]   token = VALUE   ``` - Environment variable: [`HIPCHAT_TOKEN`](../../environment_variables.md#envvar-HIPCHAT_TOKEN) |

### Authors

- Unknown

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
