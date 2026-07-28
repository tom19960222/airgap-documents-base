---
collection: ansible
version: "6"
title: "cisco.dnac.path_trace module – Resource module for Path Trace"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/path_trace_module.html
fetched_at: 2026-07-27T16:53:06+00:00
---
# cisco.dnac.path_trace module – Resource module for Path Trace

> **Note:**
>
> This module is part of the [cisco.dnac collection](https://galaxy.ansible.com/cisco/dnac) (version 6.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.dnac`.
> You need further requirements to be able to use this module,
> see [Requirements](path_trace_module.md#ansible-collections-cisco-dnac-path-trace-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.path_trace`.

New in cisco.dnac 3.1.0

- [Synopsis](path_trace_module.md#synopsis)
- [Requirements](path_trace_module.md#requirements)
- [Parameters](path_trace_module.md#parameters)
- [Notes](path_trace_module.md#notes)
- [See Also](path_trace_module.md#see-also)
- [Examples](path_trace_module.md#examples)
- [Return Values](path_trace_module.md#return-values)

## [Synopsis](path_trace_module.md#id1)

- Manage operations create and delete of the resource Path Trace.
- Initiates a new flow analysis with periodic refresh and stat collection options. Returns a request id and a task id to get results and follow progress.
- Deletes a flow analysis request by its id.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](path_trace_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](path_trace_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **controlPath**  boolean | ControlPath flag.  Choices:   - `false` - `true` |
| **destIP**  string | Path Trace’s destIP. |
| **destPort**  string | Path Trace’s destPort. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **flowAnalysisId**  string | FlowAnalysisId path parameter. Flow analysis request id. |
| **inclusions**  list / elements=string | Path Trace’s inclusions. |
| **periodicRefresh**  boolean | PeriodicRefresh flag.  Choices:   - `false` - `true` |
| **protocol**  string | Path Trace’s protocol. |
| **sourceIP**  string | Path Trace’s sourceIP. |
| **sourcePort**  string | Path Trace’s sourcePort. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](path_trace_module.md#id4)

> **Note:**
>
> - SDK Method used are path_trace.PathTrace.deletes_pathtrace_by_id, path_trace.PathTrace.initiate_a_new_pathtrace,
> - Paths used are post /dna/intent/api/v1/flow-analysis, delete /dna/intent/api/v1/flow-analysis/{flowAnalysisId},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](path_trace_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Path Trace InitiateANewPathtrace](https://developer.cisco.com/docs/dna-center/#!initiate-a-new-pathtrace)
> :   Complete reference of the InitiateANewPathtrace API.
>
> [Cisco DNA Center documentation for Path Trace DeletesPathtraceById](https://developer.cisco.com/docs/dna-center/#!deletes-pathtrace-by-id)
> :   Complete reference of the DeletesPathtraceById API.

## [Examples](path_trace_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.path_trace:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    controlPath: true
    destIP: string
    destPort: string
    inclusions:
    - string
    periodicRefresh: true
    protocol: string
    sourceIP: string
    sourcePort: string

- name: Delete by id
  cisco.dnac.path_trace:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    flowAnalysisId: string
```

## [Return Values](path_trace_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"response": {"flowAnalysisId": "string", "taskId": "string", "url": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
