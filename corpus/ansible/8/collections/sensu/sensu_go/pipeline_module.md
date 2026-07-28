---
collection: ansible
version: "8"
title: "sensu.sensu_go.pipeline module – Manage Sensu pipeline"
source_url: https://docs.ansible.com/projects/ansible/8/collections/sensu/sensu_go/pipeline_module.html
fetched_at: 2026-07-28T02:53:26+00:00
---
# sensu.sensu_go.pipeline module – Manage Sensu pipeline

> **Note:**
>
> This module is part of the [sensu.sensu_go collection](https://galaxy.ansible.com/ui/repo/published/sensu/sensu_go/) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install sensu.sensu_go`.
>
> To use it in a playbook, specify: `sensu.sensu_go.pipeline`.

New in sensu.sensu_go 1.14.0

- [Synopsis](pipeline_module.md#synopsis)
- [Parameters](pipeline_module.md#parameters)
- [See Also](pipeline_module.md#see-also)
- [Examples](pipeline_module.md#examples)
- [Return Values](pipeline_module.md#return-values)

## [Synopsis](pipeline_module.md#id1)

- Create, update or delete a Sensu pipeline.
- For more information, refer to the Sensu documentation at <https://docs.sensu.io/sensu-go/latest/observability-pipeline/observe-process/pipelines/>.

## [Parameters](pipeline_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth**  dictionary | Authentication parameters. Can define each of them with ENV as well. |
| **api_key**  string  *added in sensu.sensu_go 1.3.0* | The API key that should be used when authenticating. If this is not set, the value of the SENSU_API_KEY environment variable will be checked.  This replaces *auth.user* and *auth.password* parameters.  For more information about the API key, refer to the official Sensu documentation at <https://docs.sensu.io/sensu-go/latest/guides/use-apikey-feature/>. |
| **ca_path**  path  *added in sensu.sensu_go 1.5.0* | Path to the CA bundle that should be used to validate the backend certificate.  If this parameter is not set, module will use the CA bundle that python is using.  It is also possible to set this parameter via the *SENSU_CA_PATH* environment variable. |
| **password**  string | The Sensu user’s password. If this is not set the value of the SENSU_PASSWORD environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  **Default:** `"P@ssw0rd!"` |
| **url**  string | Location of the Sensu backend API. If this is not set the value of the SENSU_URL environment variable will be checked.  **Default:** `"http://localhost:8080"` |
| **user**  string | The username to use for connecting to the Sensu API. If this is not set the value of the SENSU_USER environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  **Default:** `"admin"` |
| **verify**  boolean  *added in sensu.sensu_go 1.5.0* | Flag that controls the certificate validation.  If you are using self-signed certificates, you can set this parameter to `false`.  ONLY USE THIS PARAMETER IN DEVELOPMENT SCENARIOS! In you use self-signed certificates in production, see the *auth.ca_path* parameter.  It is also possible to set this parameter via the *SENSU_VERIFY* environment variable.  **Choices:**   - `false` - `true` ← (default) |
| **labels**  dictionary | Custom metadata fields that can be accessed within Sensu, as key/value pairs.  **Default:** `{}` |
| **name**  string / required | The Sensu resource’s name. This name (in combination with the namespace where applicable) uniquely identifies the resource that Ansible operates on.  If the resource with selected name already exists, Ansible module will update it to match the specification in the task.  Consult the *name* metadata attribute specification in the upstream docs on <https://docs.sensu.io/sensu-go/latest/reference/> for more details about valid names and other restrictions. |
| **namespace**  string | RBAC namespace to operate in. If this is not set the value of the SENSU_NAMESPACE environment variable will be used.  **Default:** `"default"` |
| **state**  string | Target state of the Sensu object.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **workflows**  list / elements=dictionary | Array of workflows (by names) to use when filtering, mutating, and handling observability events with a pipeline. |
| **filters**  list / elements=dictionary | Reference for the Sensu event filters to use when filtering events for the pipeline.  Each pipeline workflow can reference more than one event filter.  If a workflow has more than one filter, Sensu applies the filters in a series, starting with the filter that is listed first. |
| **name**  string / required | Name of the Sensu event filter to use for the workflow.  You can use the built-in event filters, as well as your existing event filters, in pipeline workflows. |
| **type**  string | The sensuctl create resource type for the event filter.  Event filters should always be type EventFilter.  **Choices:**   - `"event_filter"` ← (default) |
| **handler**  dictionary / required | Reference for the Sensu handler to use for event processing in the workflow.  Each pipeline workflow must reference one handler.  Pipelines ignore any filters and mutators specified in handler definitions. |
| **name**  string / required | Name of the Sensu handler to use for the workflow.  You can use your existing handlers in pipeline workflows.  Pipelines ignore any filters and mutators specified in handler definitions. |
| **type**  string / required | The sensuctl create resource type for the handler.  **Choices:**   - `"handler"` - `"tcp_stream_handler"` - `"sumo_logic_metrics_handler"` |
| **mutator**  dictionary | Reference for the Sensu mutator to use to mutate event data for the workflow.  Each pipeline workflow can reference only one mutator. |
| **name**  string / required | Name of the Sensu mutator to use for the workflow.  You can use your existing mutators in pipeline workflows. |
| **type**  string | The sensuctl create resource type for the mutator.  Mutators should always be type Mutator.  **Choices:**   - `"mutator"` ← (default) |
| **name**  string / required | Name of the Sensu pipeline workflow. |

## [See Also](pipeline_module.md#id3)

> **See also:**
>
> [sensu.sensu_go.socket_handler](socket_handler_module.md#ansible-collections-sensu-sensu-go-socket-handler-module)
> :   Manage Sensu TCP/UDP handler.
>
> [sensu.sensu_go.handler_info](handler_info_module.md#ansible-collections-sensu-sensu-go-handler-info-module)
> :   List Sensu handlers.
>
> [sensu.sensu_go.pipe_handler](pipe_handler_module.md#ansible-collections-sensu-sensu-go-pipe-handler-module)
> :   Manage Sensu pipe handler.
>
> [sensu.sensu_go.filter](filter_module.md#ansible-collections-sensu-sensu-go-filter-module)
> :   Manage Sensu filters.
>
> [sensu.sensu_go.filter_info](filter_info_module.md#ansible-collections-sensu-sensu-go-filter-info-module)
> :   List Sensu info.
>
> [sensu.sensu_go.mutator](mutator_module.md#ansible-collections-sensu-sensu-go-mutator-module)
> :   Manage Sensu mutators.
>
> [sensu.sensu_go.mutator_info](mutator_info_module.md#ansible-collections-sensu-sensu-go-mutator-info-module)
> :   List Sensu mutators.

## [Examples](pipeline_module.md#id4)

```yaml+jinja
- name: Create a pipeline
  sensu.sensu_go.pipeline:
    name: this_pipeline
    workflows:
      - name: this-wf
        handler:
          name: this_handler
          type: tcp_stream_handler
        filters:
          - name: this_filter
          - name: this_filter_2
        mutator:
          name: this_mutator

- name: Delete pipeline
  sensu.sensu_go.pipeline:
    name: this_pipeline
    state: absent
```

## [Return Values](pipeline_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **object**  dictionary | Object representing Sensu pipeline.  **Returned:** success  **Sample:** `{"metadata": {"created_by": "admin", "name": "this_pipeline", "namespace": "default"}, "workflows": [{"filters": [{"api_version": "core/v2", "name": "this_filter", "type": "EventFilter"}, {"api_version": "core/v2", "name": "this_filter_2", "type": "EventFilter"}], "handler": {"api_version": "pipeline/v1", "name": "this_handler", "type": "TCPStreamHandler"}, "mutator": {"api_version": "core/v2", "name": "this_mutator", "type": "Mutator"}, "name": "this-wf"}]}` |

### Authors

- Domen Dobnikar (@domen_dobnikar)

### Collection links

- [Issue Tracker](https://github.com/sensu/sensu-go-ansible/issues)
- [Repository (Sources)](https://github.com/sensu/sensu-go-ansible)
