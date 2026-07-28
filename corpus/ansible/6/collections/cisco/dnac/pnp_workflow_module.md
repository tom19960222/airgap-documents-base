---
collection: ansible
version: "6"
title: "cisco.dnac.pnp_workflow module – Resource module for Pnp Workflow"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/pnp_workflow_module.html
fetched_at: 2026-07-27T16:53:25+00:00
---
# cisco.dnac.pnp_workflow module – Resource module for Pnp Workflow

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
> see [Requirements](pnp_workflow_module.md#ansible-collections-cisco-dnac-pnp-workflow-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.pnp_workflow`.

New in cisco.dnac 3.1.0

- [Synopsis](pnp_workflow_module.md#synopsis)
- [Requirements](pnp_workflow_module.md#requirements)
- [Parameters](pnp_workflow_module.md#parameters)
- [Notes](pnp_workflow_module.md#notes)
- [See Also](pnp_workflow_module.md#see-also)
- [Examples](pnp_workflow_module.md#examples)
- [Return Values](pnp_workflow_module.md#return-values)

## [Synopsis](pnp_workflow_module.md#id2)

- Manage operations create, update and delete of the resource Pnp Workflow.
- Adds a PnP Workflow along with the relevant tasks in the workflow into the PnP database.
- Deletes a workflow specified by id.
- Updates an existing workflow.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](pnp_workflow_module.md#id3)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](pnp_workflow_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **_id**  string | Pnp Workflow’s _id. |
| **addedOn**  integer | Pnp Workflow’s addedOn. |
| **addToInventory**  boolean | AddToInventory flag.  Choices:   - `false` - `true` |
| **configId**  string | Pnp Workflow’s configId. |
| **currTaskIdx**  integer | Pnp Workflow’s currTaskIdx. |
| **description**  string | Pnp Workflow’s description. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **endTime**  integer | Pnp Workflow’s endTime. |
| **execTime**  integer | Pnp Workflow’s execTime. |
| **id**  string | Id path parameter. |
| **imageId**  string | Pnp Workflow’s imageId. |
| **instanceType**  string | Pnp Workflow’s instanceType. |
| **lastupdateOn**  integer | Pnp Workflow’s lastupdateOn. |
| **name**  string | Pnp Workflow’s name. |
| **startTime**  integer | Pnp Workflow’s startTime. |
| **state_**  string | Pnp Workflow’s state. |
| **tasks**  list / elements=dictionary | Pnp Workflow’s tasks. |
| **currWorkItemIdx**  integer | Pnp Workflow’s currWorkItemIdx. |
| **endTime**  integer | Pnp Workflow’s endTime. |
| **name**  string | Pnp Workflow’s name. |
| **startTime**  integer | Pnp Workflow’s startTime. |
| **state**  string | Pnp Workflow’s state. |
| **taskSeqNo**  integer | Pnp Workflow’s taskSeqNo. |
| **timeTaken**  integer | Pnp Workflow’s timeTaken. |
| **type**  string | Pnp Workflow’s type. |
| **workItemList**  list / elements=dictionary | Pnp Workflow’s workItemList. |
| **command**  string | Pnp Workflow’s command. |
| **endTime**  integer | Pnp Workflow’s endTime. |
| **outputStr**  string | Pnp Workflow’s outputStr. |
| **startTime**  integer | Pnp Workflow’s startTime. |
| **state**  string | Pnp Workflow’s state. |
| **timeTaken**  integer | Pnp Workflow’s timeTaken. |
| **tenantId**  string | Pnp Workflow’s tenantId. |
| **type**  string | Pnp Workflow’s type. |
| **useState**  string | Pnp Workflow’s useState. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |
| **version**  integer | Pnp Workflow’s version. |

## [Notes](pnp_workflow_module.md#id5)

> **Note:**
>
> - SDK Method used are device_onboarding_pnp.DeviceOnboardingPnp.add_a_workflow, device_onboarding_pnp.DeviceOnboardingPnp.delete_workflow_by_id, device_onboarding_pnp.DeviceOnboardingPnp.update_workflow,
> - Paths used are post /dna/intent/api/v1/onboarding/pnp-workflow, delete /dna/intent/api/v1/onboarding/pnp-workflow/{id}, put /dna/intent/api/v1/onboarding/pnp-workflow/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](pnp_workflow_module.md#id6)

> **See also:**
>
> [Cisco DNA Center documentation for Device Onboarding (PnP) AddAWorkflow](https://developer.cisco.com/docs/dna-center/#!add-a-workflow)
> :   Complete reference of the AddAWorkflow API.
>
> [Cisco DNA Center documentation for Device Onboarding (PnP) DeleteWorkflowById](https://developer.cisco.com/docs/dna-center/#!delete-workflow-by-id)
> :   Complete reference of the DeleteWorkflowById API.
>
> [Cisco DNA Center documentation for Device Onboarding (PnP) UpdateWorkflow](https://developer.cisco.com/docs/dna-center/#!update-workflow)
> :   Complete reference of the UpdateWorkflow API.

## [Examples](pnp_workflow_module.md#id7)

```yaml+jinja
- name: Create
  cisco.dnac.pnp_workflow:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    _id: string
    addToInventory: true
    addedOn: 0
    configId: string
    currTaskIdx: 0
    description: string
    endTime: 0
    execTime: 0
    imageId: string
    instanceType: string
    lastupdateOn: 0
    name: string
    startTime: 0
    state_: string
    tasks:
    - currWorkItemIdx: 0
      endTime: 0
      name: string
      startTime: 0
      state: string
      taskSeqNo: 0
      timeTaken: 0
      type: string
      workItemList:
      - command: string
        endTime: 0
        outputStr: string
        startTime: 0
        state: string
        timeTaken: 0
    tenantId: string
    type: string
    useState: string
    version: 0

- name: Delete by id
  cisco.dnac.pnp_workflow:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    id: string

- name: Update by id
  cisco.dnac.pnp_workflow:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    _id: string
    addToInventory: true
    addedOn: 0
    configId: string
    currTaskIdx: 0
    description: string
    endTime: 0
    execTime: 0
    id: string
    imageId: string
    instanceType: string
    lastupdateOn: 0
    name: string
    startTime: 0
    state_: string
    tasks:
    - currWorkItemIdx: 0
      endTime: 0
      name: string
      startTime: 0
      state: string
      taskSeqNo: 0
      timeTaken: 0
      type: string
      workItemList:
      - command: string
        endTime: 0
        outputStr: string
        startTime: 0
        state: string
        timeTaken: 0
    tenantId: string
    type: string
    useState: string
    version: 0
```

## [Return Values](pnp_workflow_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"_id": "string", "addToInventory": true, "addedOn": 0, "configId": "string", "currTaskIdx": 0, "description": "string", "endTime": 0, "execTime": 0, "imageId": "string", "instanceType": "string", "lastupdateOn": 0, "name": "string", "startTime": 0, "state": "string", "tasks": [{"currWorkItemIdx": 0, "endTime": 0, "name": "string", "startTime": 0, "state": "string", "taskSeqNo": 0, "timeTaken": 0, "type": "string", "workItemList": [{"command": "string", "endTime": 0, "outputStr": "string", "startTime": 0, "state": "string", "timeTaken": 0}]}], "tenantId": "string", "type": "string", "useState": "string", "version": 0}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
