---
collection: ansible
version: "8"
title: "community.general.elastic callback – Create distributed traces for each Ansible task in Elastic APM"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/elastic_callback.html
fetched_at: 2026-07-28T01:51:55+00:00
---
# community.general.elastic callback – Create distributed traces for each Ansible task in Elastic APM

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
> see [Requirements](elastic_callback.md#ansible-collections-community-general-elastic-callback-requirements) for details.
>
> To use it in a playbook, specify: `community.general.elastic`.

New in community.general 3.8.0

- [Callback plugin](elastic_callback.md#callback-plugin)
- [Synopsis](elastic_callback.md#synopsis)
- [Requirements](elastic_callback.md#requirements)
- [Parameters](elastic_callback.md#parameters)
- [Examples](elastic_callback.md#examples)

## [Callback plugin](elastic_callback.md#id1)

This plugin is a **notification callback**. It sends information for a playbook run to other applications, services, or systems.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](elastic_callback.md#id2)

- This callback creates distributed traces for each Ansible task in Elastic APM.
- You can configure the plugin with environment variables.
- See <https://www.elastic.co/guide/en/apm/agent/python/current/configuration.html>.

## [Requirements](elastic_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- elastic-apm (Python library)

## [Parameters](elastic_callback.md#id4)

| Parameter | Comments |
| --- | --- |
| **apm_api_key**  string | Use the APM API key  **Configuration:**   - Environment variable: [`ELASTIC_APM_API_KEY`](../../environment_variables.md#envvar-ELASTIC_APM_API_KEY) |
| **apm_secret_token**  string | Use the APM server token  **Configuration:**   - Environment variable: [`ELASTIC_APM_SECRET_TOKEN`](../../environment_variables.md#envvar-ELASTIC_APM_SECRET_TOKEN) |
| **apm_server_url**  string | Use the APM server and its environment variables.  **Configuration:**   - Environment variable: [`ELASTIC_APM_SERVER_URL`](../../environment_variables.md#envvar-ELASTIC_APM_SERVER_URL) |
| **apm_service_name**  string | The service name resource attribute.  **Default:** `"ansible"`  **Configuration:**   - Environment variable: [`ELASTIC_APM_SERVICE_NAME`](../../environment_variables.md#envvar-ELASTIC_APM_SERVICE_NAME) |
| **apm_verify_server_cert**  boolean | Verifies the SSL certificate if an HTTPS connection.  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - Environment variable: [`ELASTIC_APM_VERIFY_SERVER_CERT`](../../environment_variables.md#envvar-ELASTIC_APM_VERIFY_SERVER_CERT) |
| **hide_task_arguments**  boolean | Hide the arguments for a task.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - Environment variable: [`ANSIBLE_OPENTELEMETRY_HIDE_TASK_ARGUMENTS`](../../environment_variables.md#envvar-ANSIBLE_OPENTELEMETRY_HIDE_TASK_ARGUMENTS) |
| **traceparent**  string | The [W3C Trace Context header traceparent](https://www.w3.org/TR/trace-context-1/#traceparent-header).  **Configuration:**   - Environment variable: [`TRACEPARENT`](../../environment_variables.md#envvar-TRACEPARENT) |

## [Examples](elastic_callback.md#id5)

```yaml+jinja
examples: |
  Enable the plugin in ansible.cfg:
    [defaults]
    callbacks_enabled = community.general.elastic

  Set the environment variable:
    export ELASTIC_APM_SERVER_URL=<your APM server URL)>
    export ELASTIC_APM_SERVICE_NAME=your_service_name
    export ELASTIC_APM_API_KEY=your_APM_API_KEY
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
