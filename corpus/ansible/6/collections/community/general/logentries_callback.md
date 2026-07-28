---
collection: ansible
version: "6"
title: "community.general.logentries callback – Sends events to Logentries"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/logentries_callback.html
fetched_at: 2026-07-27T17:14:31+00:00
---
# community.general.logentries callback – Sends events to Logentries

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
> see [Requirements](logentries_callback.md#ansible-collections-community-general-logentries-callback-requirements) for details.
>
> To use it in a playbook, specify: `community.general.logentries`.

- [Callback plugin](logentries_callback.md#callback-plugin)
- [Synopsis](logentries_callback.md#synopsis)
- [Requirements](logentries_callback.md#requirements)
- [Parameters](logentries_callback.md#parameters)
- [Examples](logentries_callback.md#examples)

## [Callback plugin](logentries_callback.md#id1)

This plugin is a **notification callback**. It sends information for a playbook run to other applications, services, or systems.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](logentries_callback.md#id2)

- This callback plugin will generate JSON objects and send them to Logentries via TCP for auditing/debugging purposes.
- Before 2.4, if you wanted to use an ini configuration, the file must be placed in the same directory as this plugin and named logentries.ini
- In 2.4 and above you can just put it in the main Ansible configuration file.

## [Requirements](logentries_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- whitelisting in configuration
- certifi (python library)
- flatdict (python library), if you want to use the ‘flatten’ option

## [Parameters](logentries_callback.md#id4)

| Parameter | Comments |
| --- | --- |
| **api**  string | URI to the Logentries API  Default: `"data.logentries.com"`  Configuration:   - INI entry:  ```YAML+Jinja   [callback_logentries]   api = data.logentries.com   ``` - Environment variable: [`LOGENTRIES_API`](../../environment_variables.md#envvar-LOGENTRIES_API) |
| **flatten**  boolean | flatten complex data structures into a single dictionary with complex keys  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [callback_logentries]   flatten = false   ``` - Environment variable: [`LOGENTRIES_FLATTEN`](../../environment_variables.md#envvar-LOGENTRIES_FLATTEN) |
| **port**  string | HTTP port to use when connecting to the API  Default: `80`  Configuration:   - INI entry:  ```YAML+Jinja   [callback_logentries]   port = 80   ``` - Environment variable: [`LOGENTRIES_PORT`](../../environment_variables.md#envvar-LOGENTRIES_PORT) |
| **tls_port**  string | Port to use when connecting to the API when TLS is enabled  Default: `443`  Configuration:   - INI entry:  ```YAML+Jinja   [callback_logentries]   tls_port = 443   ``` - Environment variable: [`LOGENTRIES_TLS_PORT`](../../environment_variables.md#envvar-LOGENTRIES_TLS_PORT) |
| **token**  string / required | The logentries “TCP token”  Configuration:   - INI entry:  ```YAML+Jinja   [callback_logentries]   token = VALUE   ``` - Environment variable: [`LOGENTRIES_ANSIBLE_TOKEN`](../../environment_variables.md#envvar-LOGENTRIES_ANSIBLE_TOKEN) |
| **use_tls**  boolean | Toggle to decide whether to use TLS to encrypt the communications with the API server  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [callback_logentries]   use_tls = false   ``` - Environment variable: [`LOGENTRIES_USE_TLS`](../../environment_variables.md#envvar-LOGENTRIES_USE_TLS) |

## [Examples](logentries_callback.md#id5)

```yaml+jinja
examples: >
  To enable, add this to your ansible.cfg file in the defaults block

    [defaults]
    callback_whitelist = community.general.logentries

  Either set the environment variables
    export LOGENTRIES_API=data.logentries.com
    export LOGENTRIES_PORT=10000
    export LOGENTRIES_ANSIBLE_TOKEN=dd21fc88-f00a-43ff-b977-e3a4233c53af

  Or in the main Ansible config file
    [callback_logentries]
    api = data.logentries.com
    port = 10000
    tls_port = 20000
    use_tls = no
    token = dd21fc88-f00a-43ff-b977-e3a4233c53af
    flatten = False
```

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
