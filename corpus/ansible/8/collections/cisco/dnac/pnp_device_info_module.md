---
collection: ansible
version: "8"
title: "cisco.dnac.pnp_device_info module – Information module for Pnp Device"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/pnp_device_info_module.html
fetched_at: 2026-07-28T01:24:00+00:00
---
# cisco.dnac.pnp_device_info module – Information module for Pnp Device

> **Note:**
>
> This module is part of the [cisco.dnac collection](https://galaxy.ansible.com/ui/repo/published/cisco/dnac/) (version 6.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.dnac`.
> You need further requirements to be able to use this module,
> see [Requirements](pnp_device_info_module.md#ansible-collections-cisco-dnac-pnp-device-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.pnp_device_info`.

New in cisco.dnac 3.1.0

- [Synopsis](pnp_device_info_module.md#synopsis)
- [Requirements](pnp_device_info_module.md#requirements)
- [Parameters](pnp_device_info_module.md#parameters)
- [Notes](pnp_device_info_module.md#notes)
- [See Also](pnp_device_info_module.md#see-also)
- [Examples](pnp_device_info_module.md#examples)
- [Return Values](pnp_device_info_module.md#return-values)

## [Synopsis](pnp_device_info_module.md#id1)

- Get all Pnp Device.
- Get Pnp Device by id.
- Returns device details specified by device id.
- Returns list of devices based on filter crieteria. If a limit is not specified, it will default to return 50 devices. Pagination and sorting are also supported by this endpoint.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](pnp_device_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](pnp_device_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cmState**  list / elements=string | CmState query parameter. Device Connection Manager State. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **headers**  dictionary | Additional headers. |
| **hostname**  string | Hostname query parameter. Device Hostname. |
| **id**  string | Id path parameter. |
| **lastContact**  boolean | LastContact query parameter. Device Has Contacted lastContact > 0.  **Choices:**   - `false` - `true` |
| **limit**  integer | Limit query parameter. Limits number of results. |
| **macAddress**  string | MacAddress query parameter. Device Mac Address. |
| **name**  list / elements=string | Name query parameter. Device Name. |
| **offset**  integer | Offset query parameter. Index of first result. |
| **onbState**  list / elements=string | OnbState query parameter. Device Onboarding State. |
| **pid**  list / elements=string | Pid query parameter. Device ProductId. |
| **projectId**  list / elements=string | ProjectId query parameter. Device Project Id. |
| **projectName**  list / elements=string | ProjectName query parameter. Device Project Name. |
| **serialNumber**  list / elements=string | SerialNumber query parameter. Device Serial Number. |
| **siteName**  string | SiteName query parameter. Device Site Name. |
| **smartAccountId**  list / elements=string | SmartAccountId query parameter. Device Smart Account. |
| **sort**  list / elements=string | Sort query parameter. Comma seperated list of fields to sort on. |
| **sortOrder**  string | SortOrder query parameter. Sort Order Ascending (asc) or Descending (des). |
| **source**  list / elements=string | Source query parameter. Device Source. |
| **state_**  list / elements=string | State query parameter. Device State. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |
| **virtualAccountId**  list / elements=string | VirtualAccountId query parameter. Device Virtual Account. |
| **workflowId**  list / elements=string | WorkflowId query parameter. Device Workflow Id. |
| **workflowName**  list / elements=string | WorkflowName query parameter. Device Workflow Name. |

## [Notes](pnp_device_info_module.md#id4)

> **Note:**
>
> - SDK Method used are device_onboarding_pnp.DeviceOnboardingPnp.get_device_by_id, device_onboarding_pnp.DeviceOnboardingPnp.get_device_list,
> - Paths used are get /dna/intent/api/v1/onboarding/pnp-device, get /dna/intent/api/v1/onboarding/pnp-device/{id},
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](pnp_device_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Device Onboarding (PnP) GetDeviceById](https://developer.cisco.com/docs/dna-center/#!get-device-by-id)
> :   Complete reference of the GetDeviceById API.
>
> [Cisco DNA Center documentation for Device Onboarding (PnP) GetDeviceList2](https://developer.cisco.com/docs/dna-center/#!get-device-list-2)
> :   Complete reference of the GetDeviceList2 API.

## [Examples](pnp_device_info_module.md#id6)

```yaml+jinja
- name: Get all Pnp Device
  cisco.dnac.pnp_device_info:
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
    serialNumber: []
    state_: []
    onbState: []
    cmState: []
    name: []
    pid: []
    source: []
    projectId: []
    workflowId: []
    projectName: []
    workflowName: []
    smartAccountId: []
    virtualAccountId: []
    lastContact: True
    macAddress: string
    hostname: string
    siteName: string
  register: result

- name: Get Pnp Device by id
  cisco.dnac.pnp_device_info:
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

## [Return Values](pnp_device_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"_id": "string", "dayZeroConfig": {"config": "string"}, "dayZeroConfigPreview": {}, "deviceInfo": {"aaaCredentials": {"password": "string", "username": "string"}, "addedOn": 0, "addnMacAddrs": ["string"], "agentType": "string", "authStatus": "string", "authenticatedMicNumber": "string", "authenticatedSudiSerialNo": "string", "capabilitiesSupported": ["string"], "cmState": "string", "description": "string", "deviceSudiSerialNos": ["string"], "deviceType": "string", "featuresSupported": ["string"], "fileSystemList": [{"freespace": 0, "name": "string", "readable": true, "size": 0, "type": "string", "writeable": true}], "firstContact": 0, "hostname": "string", "httpHeaders": [{"key": "string", "value": "string"}], "imageFile": "string", "imageVersion": "string", "ipInterfaces": [{"ipv4Address": {}, "ipv6AddressList": [{}], "macAddress": "string", "name": "string", "status": "string"}], "lastContact": 0, "lastSyncTime": 0, "lastUpdateOn": 0, "location": {"address": "string", "altitude": "string", "latitude": "string", "longitude": "string", "siteId": "string"}, "macAddress": "string", "mode": "string", "name": "string", "neighborLinks": [{"localInterfaceName": "string", "localMacAddress": "string", "localShortInterfaceName": "string", "remoteDeviceName": "string", "remoteInterfaceName": "string", "remoteMacAddress": "string", "remotePlatform": "string", "remoteShortInterfaceName": "string", "remoteVersion": "string"}], "onbState": "string", "pid": "string", "pnpProfileList": [{"createdBy": "string", "discoveryCreated": true, "primaryEndpoint": {"certificate": "string", "fqdn": "string", "ipv4Address": {}, "ipv6Address": {}, "port": 0, "protocol": "string"}, "profileName": "string", "secondaryEndpoint": {"certificate": "string", "fqdn": "string", "ipv4Address": {}, "ipv6Address": {}, "port": 0, "protocol": "string"}}], "populateInventory": true, "preWorkflowCliOuputs": [{"cli": "string", "cliOutput": "string"}], "projectId": "string", "projectName": "string", "reloadRequested": true, "serialNumber": "string", "siteId": "string", "siteName": "string", "smartAccountId": "string", "source": "string", "stack": true, "stackInfo": {"isFullRing": true, "stackMemberList": [{"hardwareVersion": "string", "licenseLevel": "string", "licenseType": "string", "macAddress": "string", "pid": "string", "priority": 0, "role": "string", "serialNumber": "string", "softwareVersion": "string", "stackNumber": 0, "state": "string", "sudiSerialNumber": "string"}], "stackRingProtocol": "string", "supportsStackWorkflows": true, "totalMemberCount": 0, "validLicenseLevels": ["string"]}, "state": "string", "sudiRequired": true, "tags": {}, "userMicNumbers": ["string"], "userSudiSerialNos": ["string"], "virtualAccountId": "string", "workflowId": "string", "workflowName": "string"}, "runSummaryList": [{"details": "string", "errorFlag": true, "historyTaskInfo": {"addnDetails": [{"key": "string", "value": "string"}], "name": "string", "timeTaken": 0, "type": "string", "workItemList": [{"command": "string", "endTime": 0, "outputStr": "string", "startTime": 0, "state": "string", "timeTaken": 0}]}, "timestamp": 0}], "systemResetWorkflow": {"_id": "string", "addToInventory": true, "addedOn": 0, "configId": "string", "currTaskIdx": 0, "description": "string", "endTime": 0, "execTime": 0, "imageId": "string", "instanceType": "string", "lastupdateOn": 0, "name": "string", "startTime": 0, "state": "string", "tasks": [{"currWorkItemIdx": 0, "endTime": 0, "name": "string", "startTime": 0, "state": "string", "taskSeqNo": 0, "timeTaken": 0, "type": "string", "workItemList": [{"command": "string", "endTime": 0, "outputStr": "string", "startTime": 0, "state": "string", "timeTaken": 0}]}], "tenantId": "string", "type": "string", "useState": "string", "version": 0}, "systemWorkflow": {"_id": "string", "addToInventory": true, "addedOn": 0, "configId": "string", "currTaskIdx": 0, "description": "string", "endTime": 0, "execTime": 0, "imageId": "string", "instanceType": "string", "lastupdateOn": 0, "name": "string", "startTime": 0, "state": "string", "tasks": [{"currWorkItemIdx": 0, "endTime": 0, "name": "string", "startTime": 0, "state": "string", "taskSeqNo": 0, "timeTaken": 0, "type": "string", "workItemList": [{"command": "string", "endTime": 0, "outputStr": "string", "startTime": 0, "state": "string", "timeTaken": 0}]}], "tenantId": "string", "type": "string", "useState": "string", "version": 0}, "tenantId": "string", "version": 0, "workflow": {"_id": "string", "addToInventory": true, "addedOn": 0, "configId": "string", "currTaskIdx": 0, "description": "string", "endTime": 0, "execTime": 0, "imageId": "string", "instanceType": "string", "lastupdateOn": 0, "name": "string", "startTime": 0, "state": "string", "tasks": [{"currWorkItemIdx": 0, "endTime": 0, "name": "string", "startTime": 0, "state": "string", "taskSeqNo": 0, "timeTaken": 0, "type": "string", "workItemList": [{"command": "string", "endTime": 0, "outputStr": "string", "startTime": 0, "state": "string", "timeTaken": 0}]}], "tenantId": "string", "type": "string", "useState": "string", "version": 0}, "workflowParameters": {"configList": [{"configId": "string", "configParameters": [{"key": "string", "value": "string"}]}], "licenseLevel": "string", "licenseType": "string", "topOfStackSerialNumber": "string"}}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
