---
collection: ansible
version: "8"
title: "community.general.splunk callback – Sends task result events to Splunk HTTP Event Collector"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/splunk_callback.html
fetched_at: 2026-07-28T01:52:06+00:00
---
# community.general.splunk callback – Sends task result events to Splunk HTTP Event Collector

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
> see [Requirements](splunk_callback.md#ansible-collections-community-general-splunk-callback-requirements) for details.
>
> To use it in a playbook, specify: `community.general.splunk`.

- [Callback plugin](splunk_callback.md#callback-plugin)
- [Synopsis](splunk_callback.md#synopsis)
- [Requirements](splunk_callback.md#requirements)
- [Parameters](splunk_callback.md#parameters)
- [Examples](splunk_callback.md#examples)

## [Callback plugin](splunk_callback.md#id1)

This plugin is a **notification callback**. It sends information for a playbook run to other applications, services, or systems.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](splunk_callback.md#id2)

- This callback plugin will send task results as JSON formatted events to a Splunk HTTP collector.
- The companion Splunk Monitoring & Diagnostics App is available here <https://splunkbase.splunk.com/app/4023/>.
- Credit to “Ryan Currah (@ryancurrah)” for original source upon which this is based.

## [Requirements](splunk_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- Whitelisting this callback plugin
- Create a HTTP Event Collector in Splunk
- Define the URL and token in `ansible.cfg`

## [Parameters](splunk_callback.md#id4)

| Parameter | Comments |
| --- | --- |
| **authtoken**  string | Token to authenticate the connection to the Splunk HTTP collector.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_splunk]   authtoken = VALUE   ``` - Environment variable: [`SPLUNK_AUTHTOKEN`](../../environment_variables.md#envvar-SPLUNK_AUTHTOKEN) |
| **batch**  string  *added in community.general 3.3.0* | Correlation ID which can be set across multiple playbook executions.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_splunk]   batch = VALUE   ``` - Environment variable: [`SPLUNK_BATCH`](../../environment_variables.md#envvar-SPLUNK_BATCH) |
| **include_milliseconds**  boolean  *added in community.general 2.0.0* | Whether to include milliseconds as part of the generated timestamp field in the event sent to the Splunk HTTP collector.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_splunk]   include_milliseconds = false   ``` - Environment variable: [`SPLUNK_INCLUDE_MILLISECONDS`](../../environment_variables.md#envvar-SPLUNK_INCLUDE_MILLISECONDS) |
| **url**  string | URL to the Splunk HTTP collector source.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_splunk]   url = VALUE   ``` - Environment variable: [`SPLUNK_URL`](../../environment_variables.md#envvar-SPLUNK_URL) |
| **validate_certs**  boolean  *added in community.general 1.0.0* | Whether to validate certificates for connections to HEC. It is not recommended to set to `false` except when you are sure that nobody can intercept the connection between this plugin and HEC, as setting it to `false` allows man-in-the-middle attacks!  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_splunk]   validate_certs = true   ``` - Environment variable: [`SPLUNK_VALIDATE_CERTS`](../../environment_variables.md#envvar-SPLUNK_VALIDATE_CERTS) |

## [Examples](splunk_callback.md#id5)

```yaml+jinja
examples: >
  To enable, add this to your ansible.cfg file in the defaults block
    [defaults]
    callback_whitelist = community.general.splunk
  Set the environment variable
    export SPLUNK_URL=http://mysplunkinstance.datapaas.io:8088/services/collector/event
    export SPLUNK_AUTHTOKEN=f23blad6-5965-4537-bf69-5b5a545blabla88
  Set the ansible.cfg variable in the callback_splunk block
    [callback_splunk]
    url = http://mysplunkinstance.datapaas.io:8088/services/collector/event
    authtoken = f23blad6-5965-4537-bf69-5b5a545blabla88
```

### Authors

- Stuart Hirst

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
