---
collection: ansible
version: "6"
title: "community.general.log_plays callback – write playbook output to log file"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/log_plays_callback.html
fetched_at: 2026-07-27T17:14:29+00:00
---
# community.general.log_plays callback – write playbook output to log file

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
> see [Requirements](log_plays_callback.md#ansible-collections-community-general-log-plays-callback-requirements) for details.
>
> To use it in a playbook, specify: `community.general.log_plays`.

- [Callback plugin](log_plays_callback.md#callback-plugin)
- [Synopsis](log_plays_callback.md#synopsis)
- [Requirements](log_plays_callback.md#requirements)
- [Parameters](log_plays_callback.md#parameters)

## [Callback plugin](log_plays_callback.md#id1)

This plugin is a **notification callback**. It sends information for a playbook run to other applications, services, or systems.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](log_plays_callback.md#id2)

- This callback writes playbook output to a file per host in the `/var/log/ansible/hosts` directory

## [Requirements](log_plays_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- Whitelist in configuration
- A writeable /var/log/ansible/hosts directory by the user executing Ansible on the controller

## [Parameters](log_plays_callback.md#id4)

| Parameter | Comments |
| --- | --- |
| **log_folder**  string | The folder where log files will be created.  Default: `"/var/log/ansible/hosts"`  Configuration:   - INI entry:  ```YAML+Jinja   [callback_log_plays]   log_folder = /var/log/ansible/hosts   ``` - Environment variable: [`ANSIBLE_LOG_FOLDER`](../../environment_variables.md#envvar-ANSIBLE_LOG_FOLDER) |

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
