---
collection: ansible
version: "6"
title: "community.general.logstash callback – Sends events to Logstash"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/logstash_callback.html
fetched_at: 2026-07-27T17:14:32+00:00
---
# community.general.logstash callback – Sends events to Logstash

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
> see [Requirements](logstash_callback.md#ansible-collections-community-general-logstash-callback-requirements) for details.
>
> To use it in a playbook, specify: `community.general.logstash`.

- [Callback plugin](logstash_callback.md#callback-plugin)
- [Synopsis](logstash_callback.md#synopsis)
- [Requirements](logstash_callback.md#requirements)
- [Parameters](logstash_callback.md#parameters)
- [Examples](logstash_callback.md#examples)

## [Callback plugin](logstash_callback.md#id1)

This plugin is a **notification callback**. It sends information for a playbook run to other applications, services, or systems.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](logstash_callback.md#id2)

- This callback will report facts and task events to Logstash <https://www.elastic.co/products/logstash>

## [Requirements](logstash_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- whitelisting in configuration
- logstash (python library)

## [Parameters](logstash_callback.md#id4)

| Parameter | Comments |
| --- | --- |
| **format_version**  string  added in community.general 2.0.0 | Logging format  Choices:   - `"v1"` ← (default) - `"v2"`   Configuration:   - INI entry:  ```YAML+Jinja   [callback_logstash]   format_version = v1   ``` - Environment variable: [`LOGSTASH_FORMAT_VERSION`](../../environment_variables.md#envvar-LOGSTASH_FORMAT_VERSION) |
| **port**  string | Port on which logstash is listening  Default: `5000`  Configuration:   - INI entry:  ```YAML+Jinja   [callback_logstash]   port = 5000   ```  added in community.general 1.0.0 - Environment variable: [`LOGSTASH_PORT`](../../environment_variables.md#envvar-LOGSTASH_PORT) |
| **pre_command**  string  added in community.general 2.0.0 | Executes command before run and its result is added to the `ansible_pre_command_output` logstash field.  Configuration:   - INI entry:  ```YAML+Jinja   [callback_logstash]   pre_command = VALUE   ``` - Environment variable: [`LOGSTASH_PRE_COMMAND`](../../environment_variables.md#envvar-LOGSTASH_PRE_COMMAND) |
| **server**  string | Address of the Logstash server  Default: `"localhost"`  Configuration:   - INI entry:  ```YAML+Jinja   [callback_logstash]   server = localhost   ```  added in community.general 1.0.0 - Environment variable: [`LOGSTASH_SERVER`](../../environment_variables.md#envvar-LOGSTASH_SERVER) |
| **type**  string | Message type  Default: `"ansible"`  Configuration:   - INI entry:  ```YAML+Jinja   [callback_logstash]   type = ansible   ```  added in community.general 1.0.0 - Environment variable: [`LOGSTASH_TYPE`](../../environment_variables.md#envvar-LOGSTASH_TYPE) |

## [Examples](logstash_callback.md#id5)

```yaml+jinja
ansible.cfg: |
    # Enable Callback plugin
    [defaults]
        callback_whitelist = community.general.logstash

    [callback_logstash]
        server = logstash.example.com
        port = 5000
        pre_command = git rev-parse HEAD
        type = ansible

11-input-tcp.conf: |
    # Enable Logstash TCP Input
    input {
            tcp {
                port => 5000
                codec => json
                add_field => { "[@metadata][beat]" => "notify" }
                add_field => { "[@metadata][type]" => "ansible" }
            }
        }
```

### Authors

- Yevhen Khmelenko (@ujenmr)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
