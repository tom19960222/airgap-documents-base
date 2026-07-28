---
collection: ansible
version: "6"
title: "community.general.logdna callback – Sends playbook logs to LogDNA"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/logdna_callback.html
fetched_at: 2026-07-27T17:14:30+00:00
---
# community.general.logdna callback – Sends playbook logs to LogDNA

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
> see [Requirements](logdna_callback.md#ansible-collections-community-general-logdna-callback-requirements) for details.
>
> To use it in a playbook, specify: `community.general.logdna`.

- [Callback plugin](logdna_callback.md#callback-plugin)
- [Synopsis](logdna_callback.md#synopsis)
- [Requirements](logdna_callback.md#requirements)
- [Parameters](logdna_callback.md#parameters)

## [Callback plugin](logdna_callback.md#id1)

This plugin is an **aggregate callback**. It adds additional console output next to the configured stdout callback.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](logdna_callback.md#id2)

- This callback will report logs from playbook actions, tasks, and events to LogDNA (<https://app.logdna.com>)

## [Requirements](logdna_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- LogDNA Python Library (<https://github.com/logdna/python>)
- whitelisting in configuration

## [Parameters](logdna_callback.md#id4)

| Parameter | Comments |
| --- | --- |
| **conf_hostname**  string | Alternative Host Name; the current host name by default  Configuration:   - INI entry:  ```YAML+Jinja   [callback_logdna]   conf_hostname = VALUE   ``` - Environment variable: [`LOGDNA_HOSTNAME`](../../environment_variables.md#envvar-LOGDNA_HOSTNAME) |
| **conf_key**  string / required | LogDNA Ingestion Key  Configuration:   - INI entry:  ```YAML+Jinja   [callback_logdna]   conf_key = VALUE   ``` - Environment variable: [`LOGDNA_INGESTION_KEY`](../../environment_variables.md#envvar-LOGDNA_INGESTION_KEY) |
| **conf_tags**  string | Tags  Default: `"ansible"`  Configuration:   - INI entry:  ```YAML+Jinja   [callback_logdna]   conf_tags = ansible   ``` - Environment variable: [`LOGDNA_TAGS`](../../environment_variables.md#envvar-LOGDNA_TAGS) |
| **plugin_ignore_errors**  boolean | Whether to ignore errors on failing or not  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [callback_logdna]   plugin_ignore_errors = false   ``` - Environment variable: [`ANSIBLE_IGNORE_ERRORS`](../../environment_variables.md#envvar-ANSIBLE_IGNORE_ERRORS) |

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
