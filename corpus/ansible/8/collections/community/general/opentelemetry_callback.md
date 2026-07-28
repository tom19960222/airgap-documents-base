---
collection: ansible
version: "8"
title: "community.general.opentelemetry callback – Create distributed traces with OpenTelemetry"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/opentelemetry_callback.html
fetched_at: 2026-07-28T01:52:03+00:00
---
# community.general.opentelemetry callback – Create distributed traces with OpenTelemetry

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
> see [Requirements](opentelemetry_callback.md#ansible-collections-community-general-opentelemetry-callback-requirements) for details.
>
> To use it in a playbook, specify: `community.general.opentelemetry`.

New in community.general 3.7.0

- [Callback plugin](opentelemetry_callback.md#callback-plugin)
- [Synopsis](opentelemetry_callback.md#synopsis)
- [Requirements](opentelemetry_callback.md#requirements)
- [Parameters](opentelemetry_callback.md#parameters)
- [Examples](opentelemetry_callback.md#examples)

## [Callback plugin](opentelemetry_callback.md#id1)

This plugin is a **notification callback**. It sends information for a playbook run to other applications, services, or systems.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](opentelemetry_callback.md#id2)

- This callback creates distributed traces for each Ansible task with OpenTelemetry.
- You can configure the OpenTelemetry exporter and SDK with environment variables.
- See <https://opentelemetry-python.readthedocs.io/en/latest/exporter/otlp/otlp.html>.
- See <https://opentelemetry-python.readthedocs.io/en/latest/sdk/environment_variables.html#opentelemetry-sdk-environment-variables>.

## [Requirements](opentelemetry_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- opentelemetry-api (Python library)
- opentelemetry-exporter-otlp (Python library)
- opentelemetry-sdk (Python library)

## [Parameters](opentelemetry_callback.md#id4)

| Parameter | Comments |
| --- | --- |
| **disable_attributes_in_logs**  boolean  *added in community.general 7.1.0* | Disable populating span attributes to the logs.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_opentelemetry]   disable_attributes_in_logs = false   ``` - Environment variable: [`ANSIBLE_OPENTELEMETRY_DISABLE_ATTRIBUTES_IN_LOGS`](../../environment_variables.md#envvar-ANSIBLE_OPENTELEMETRY_DISABLE_ATTRIBUTES_IN_LOGS) |
| **disable_logs**  boolean  *added in community.general 5.8.0* | Disable sending logs.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_opentelemetry]   disable_logs = false   ``` - Environment variable: [`ANSIBLE_OPENTELEMETRY_DISABLE_LOGS`](../../environment_variables.md#envvar-ANSIBLE_OPENTELEMETRY_DISABLE_LOGS) |
| **enable_from_environment**  string  *added in community.general 3.8.0* | Whether to enable this callback only if the given environment variable exists and it is set to `true`.  This is handy when you use Configuration as Code and want to send distributed traces if running in the CI rather when running Ansible locally.  For such, it evaluates the given `enable_from_environment` value as environment variable and if set to true this plugin will be enabled.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_opentelemetry]   enable_from_environment = VALUE   ```  *added in community.general 5.3.0* - Environment variable: [`ANSIBLE_OPENTELEMETRY_ENABLE_FROM_ENVIRONMENT`](../../environment_variables.md#envvar-ANSIBLE_OPENTELEMETRY_ENABLE_FROM_ENVIRONMENT) |
| **hide_task_arguments**  boolean | Hide the arguments for a task.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_opentelemetry]   hide_task_arguments = false   ```  *added in community.general 5.3.0* - Environment variable: [`ANSIBLE_OPENTELEMETRY_HIDE_TASK_ARGUMENTS`](../../environment_variables.md#envvar-ANSIBLE_OPENTELEMETRY_HIDE_TASK_ARGUMENTS) |
| **otel_service_name**  string | The service name resource attribute.  **Default:** `"ansible"`  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_opentelemetry]   otel_service_name = ansible   ```  *added in community.general 5.3.0* - Environment variable: [`OTEL_SERVICE_NAME`](../../environment_variables.md#envvar-OTEL_SERVICE_NAME) |
| **traceparent**  string | The [W3C Trace Context header traceparent](https://www.w3.org/TR/trace-context-1/#traceparent-header).  **Default:** `"None"`  **Configuration:**   - Environment variable: [`TRACEPARENT`](../../environment_variables.md#envvar-TRACEPARENT) |

## [Examples](opentelemetry_callback.md#id5)

```yaml+jinja
examples: |
  Enable the plugin in ansible.cfg:
    [defaults]
    callbacks_enabled = community.general.opentelemetry
    [callback_opentelemetry]
    enable_from_environment = ANSIBLE_OPENTELEMETRY_ENABLED

  Set the environment variable:
    export OTEL_EXPORTER_OTLP_ENDPOINT=<your endpoint (OTLP/HTTP)>
    export OTEL_EXPORTER_OTLP_HEADERS="authorization=Bearer your_otel_token"
    export OTEL_SERVICE_NAME=your_service_name
    export ANSIBLE_OPENTELEMETRY_ENABLED=true
```

### Authors

- Victor Martinez (@v1v)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
