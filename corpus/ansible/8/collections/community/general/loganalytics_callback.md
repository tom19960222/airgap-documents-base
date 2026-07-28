---
collection: ansible
version: "8"
title: "community.general.loganalytics callback – Posts task results to Azure Log Analytics"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/loganalytics_callback.html
fetched_at: 2026-07-28T01:51:58+00:00
---
# community.general.loganalytics callback – Posts task results to Azure Log Analytics

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
> see [Requirements](loganalytics_callback.md#ansible-collections-community-general-loganalytics-callback-requirements) for details.
>
> To use it in a playbook, specify: `community.general.loganalytics`.

New in community.general 2.4.0

- [Callback plugin](loganalytics_callback.md#callback-plugin)
- [Synopsis](loganalytics_callback.md#synopsis)
- [Requirements](loganalytics_callback.md#requirements)
- [Parameters](loganalytics_callback.md#parameters)
- [Examples](loganalytics_callback.md#examples)

## [Callback plugin](loganalytics_callback.md#id1)

This plugin is a **notification callback**. It sends information for a playbook run to other applications, services, or systems.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](loganalytics_callback.md#id2)

- This callback plugin will post task results in JSON formatted to an Azure Log Analytics workspace.
- Credits to authors of splunk callback plugin.

## [Requirements](loganalytics_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- Whitelisting this callback plugin.
- An Azure log analytics work space has been established.

## [Parameters](loganalytics_callback.md#id4)

| Parameter | Comments |
| --- | --- |
| **shared_key**  string / required | Shared key to connect to Azure log analytics workspace.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_loganalytics]   shared_key = VALUE   ``` - Environment variable: [`WORKSPACE_SHARED_KEY`](../../environment_variables.md#envvar-WORKSPACE_SHARED_KEY) |
| **workspace_id**  string / required | Workspace ID of the Azure log analytics workspace.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_loganalytics]   workspace_id = VALUE   ``` - Environment variable: [`WORKSPACE_ID`](../../environment_variables.md#envvar-WORKSPACE_ID) |

## [Examples](loganalytics_callback.md#id5)

```yaml+jinja
examples: |
  Whitelist the plugin in ansible.cfg:
    [defaults]
    callback_whitelist = community.general.loganalytics
  Set the environment variable:
    export WORKSPACE_ID=01234567-0123-0123-0123-01234567890a
    export WORKSPACE_SHARED_KEY=dZD0kCbKl3ehZG6LHFMuhtE0yHiFCmetzFMc2u+roXIUQuatqU924SsAAAAPemhjbGlAemhjbGktTUJQAQIDBA==
  Or configure the plugin in ansible.cfg in the callback_loganalytics block:
    [callback_loganalytics]
    workspace_id = 01234567-0123-0123-0123-01234567890a
    shared_key = dZD0kCbKl3ehZG6LHFMuhtE0yHiFCmetzFMc2u+roXIUQuatqU924SsAAAAPemhjbGlAemhjbGktTUJQAQIDBA==
```

### Authors

- Cyrus Li (@zhcli)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
