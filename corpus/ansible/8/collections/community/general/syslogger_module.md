---
collection: ansible
version: "8"
title: "community.general.syslogger module – Log messages in the syslog"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/syslogger_module.html
fetched_at: 2026-07-28T01:50:53+00:00
---
# community.general.syslogger module – Log messages in the syslog

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.syslogger`.

- [Synopsis](syslogger_module.md#synopsis)
- [Parameters](syslogger_module.md#parameters)
- [Attributes](syslogger_module.md#attributes)
- [Examples](syslogger_module.md#examples)
- [Return Values](syslogger_module.md#return-values)

## [Synopsis](syslogger_module.md#id1)

- Uses syslog to add log entries to the host.

Aliases: notification.syslogger

## [Parameters](syslogger_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **facility**  string | Set the log facility.  **Choices:**   - `"kern"` - `"user"` - `"mail"` - `"daemon"` ← (default) - `"auth"` - `"lpr"` - `"news"` - `"uucp"` - `"cron"` - `"syslog"` - `"local0"` - `"local1"` - `"local2"` - `"local3"` - `"local4"` - `"local5"` - `"local6"` - `"local7"` |
| **ident**  string  *added in community.general 0.2.0* | Specify the name of application name which is sending the log to syslog.  **Default:** `"ansible_syslogger"` |
| **log_pid**  boolean | Log the PID in brackets.  **Choices:**   - `false` ← (default) - `true` |
| **msg**  string / required | This is the message to place in syslog. |
| **priority**  string | Set the log priority.  **Choices:**   - `"emerg"` - `"alert"` - `"crit"` - `"err"` - `"warning"` - `"notice"` - `"info"` ← (default) - `"debug"` |

## [Attributes](syslogger_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](syslogger_module.md#id4)

```yaml+jinja
- name: Simple Usage
  community.general.syslogger:
    msg: "I will end up as daemon.info"

- name: Send a log message with err priority and user facility with log_pid
  community.general.syslogger:
    msg: "Hello from Ansible"
    priority: "err"
    facility: "user"
    log_pid: true

- name: Specify the name of application which is sending log message
  community.general.syslogger:
    ident: "MyApp"
    msg: "I want to believe"
    priority: "alert"
```

## [Return Values](syslogger_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **facility**  string | Syslog facility  **Returned:** always  **Sample:** `"info"` |
| **ident**  string  *added in community.general 0.2.0* | Name of application sending the message to log  **Returned:** always  **Sample:** `"ansible_syslogger"` |
| **log_pid**  boolean | Log PID status  **Returned:** always  **Sample:** `true` |
| **msg**  string | Message sent to syslog  **Returned:** always  **Sample:** `"Hello from Ansible"` |
| **priority**  string | Priority level  **Returned:** always  **Sample:** `"daemon"` |

### Authors

- Tim Rightnour (@garbled1)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
