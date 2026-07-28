---
collection: ansible
version: "6"
title: "cisco.dnac.pnp_workflow_info module – Information module for Pnp Workflow"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/pnp_workflow_info_module.html
fetched_at: 2026-07-27T16:53:26+00:00
---
# cisco.dnac.pnp_workflow_info module – Information module for Pnp Workflow

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
> see [Requirements](pnp_workflow_info_module.md#ansible-collections-cisco-dnac-pnp-workflow-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.pnp_workflow_info`.

New in cisco.dnac 3.1.0

- [Synopsis](pnp_workflow_info_module.md#synopsis)
- [Requirements](pnp_workflow_info_module.md#requirements)
- [Parameters](pnp_workflow_info_module.md#parameters)
- [Notes](pnp_workflow_info_module.md#notes)
- [See Also](pnp_workflow_info_module.md#see-also)
- [Examples](pnp_workflow_info_module.md#examples)
- [Return Values](pnp_workflow_info_module.md#return-values)

## [Synopsis](pnp_workflow_info_module.md#id1)

- Get all Pnp Workflow.
- Get Pnp Workflow by id.
- Returns a workflow specified by id.
- Returns the list of workflows based on filter criteria. If a limit is not specified, it will default to return 50 workflows. Pagination and sorting are also supported by this endpoint.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](pnp_workflow_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](pnp_workflow_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **headers**  dictionary | Additional headers. |
| **id**  string | Id path parameter. |
| **limit**  integer | Limit query parameter. Limits number of results. |
| **name**  list / elements=string | Name query parameter. Workflow Name. |
| **offset**  integer | Offset query parameter. Index of first result. |
| **sort**  list / elements=string | Sort query parameter. Comma seperated lost of fields to sort on. |
| **sortOrder**  string | SortOrder query parameter. Sort Order Ascending (asc) or Descending (des). |
| **type**  list / elements=string | Type query parameter. Workflow Type. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](pnp_workflow_info_module.md#id4)

> **Note:**
>
> - SDK Method used are device_onboarding_pnp.DeviceOnboardingPnp.get_workflow_by_id, device_onboarding_pnp.DeviceOnboardingPnp.get_workflows,
> - Paths used are get /dna/intent/api/v1/onboarding/pnp-workflow, get /dna/intent/api/v1/onboarding/pnp-workflow/{id},
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](pnp_workflow_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Device Onboarding (PnP) GetWorkflowById](https://developer.cisco.com/docs/dna-center/#!get-workflow-by-id)
> :   Complete reference of the GetWorkflowById API.
>
> [Cisco DNA Center documentation for Device Onboarding (PnP) GetWorkflows](https://developer.cisco.com/docs/dna-center/#!get-workflows)
> :   Complete reference of the GetWorkflows API.

## [Examples](pnp_workflow_info_module.md#id6)

```yaml+jinja
- name: Get all Pnp Workflow
  cisco.dnac.pnp_workflow_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    limit: 0
    offset: 0
    sort: []
    sortOrder: string
    type: []
    name: []
  register: result

- name: Get Pnp Workflow by id
  cisco.dnac.pnp_workflow_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result
```

## [Return Values](pnp_workflow_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"_id": "string", "addToInventory": true, "addedOn": 0, "configId": "string", "currTaskIdx": 0, "description": "string", "endTime": 0, "execTime": 0, "imageId": "string", "instanceType": "string", "lastupdateOn": 0, "name": "string", "startTime": 0, "state": "string", "tasks": [{"currWorkItemIdx": 0, "endTime": 0, "name": "string", "startTime": 0, "state": "string", "taskSeqNo": 0, "timeTaken": 0, "type": "string", "workItemList": [{"command": "string", "endTime": 0, "outputStr": "string", "startTime": 0, "state": "string", "timeTaken": 0}]}], "tenantId": "string", "type": "string", "useState": "string", "version": 0}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
