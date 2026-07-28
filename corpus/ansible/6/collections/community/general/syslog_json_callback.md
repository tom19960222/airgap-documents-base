---
collection: ansible
version: "6"
title: "community.general.syslog_json callback – sends JSON events to syslog"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/syslog_json_callback.html
fetched_at: 2026-07-27T17:14:38+00:00
---
# community.general.syslog_json callback – sends JSON events to syslog

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
> see [Requirements](syslog_json_callback.md#ansible-collections-community-general-syslog-json-callback-requirements) for details.
>
> To use it in a playbook, specify: `community.general.syslog_json`.

- [Callback plugin](syslog_json_callback.md#callback-plugin)
- [Synopsis](syslog_json_callback.md#synopsis)
- [Requirements](syslog_json_callback.md#requirements)
- [Parameters](syslog_json_callback.md#parameters)

## [Callback plugin](syslog_json_callback.md#id1)

This plugin is a **notification callback**. It sends information for a playbook run to other applications, services, or systems.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](syslog_json_callback.md#id2)

- This plugin logs ansible-playbook and ansible runs to a syslog server in JSON format
- Before Ansible 2.9 only environment variables were available for configuration

## [Requirements](syslog_json_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- whitelist in configuration

## [Parameters](syslog_json_callback.md#id4)

| Parameter | Comments |
| --- | --- |
| **facility**  string | syslog facility to log as  Default: `"user"`  Configuration:   - INI entry:  ```YAML+Jinja   [callback_syslog_json]   syslog_facility = user   ``` - Environment variable: [`SYSLOG_FACILITY`](../../environment_variables.md#envvar-SYSLOG_FACILITY) |
| **port**  string | port on which the syslog server is listening  Default: `514`  Configuration:   - INI entry:  ```YAML+Jinja   [callback_syslog_json]   syslog_port = 514   ``` - Environment variable: [`SYSLOG_PORT`](../../environment_variables.md#envvar-SYSLOG_PORT) |
| **server**  string | syslog server that will receive the event  Default: `"localhost"`  Configuration:   - INI entry:  ```YAML+Jinja   [callback_syslog_json]   syslog_server = localhost   ``` - Environment variable: [`SYSLOG_SERVER`](../../environment_variables.md#envvar-SYSLOG_SERVER) |
| **setup**  boolean  added in community.general 4.5.0 | Log setup tasks.  Choices:   - `false` - `true` ← (default)   Configuration:   - INI entry:  ```YAML+Jinja   [callback_syslog_json]   syslog_setup = true   ``` - Environment variable: [`ANSIBLE_SYSLOG_SETUP`](../../environment_variables.md#envvar-ANSIBLE_SYSLOG_SETUP) |

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
