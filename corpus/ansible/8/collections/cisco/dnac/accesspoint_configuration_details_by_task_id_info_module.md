---
collection: ansible
version: "8"
title: "cisco.dnac.accesspoint_configuration_details_by_task_id_info module – Information module for Accesspoint Configuration Details By Task Id"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/accesspoint_configuration_details_by_task_id_info_module.html
fetched_at: 2026-07-28T01:21:11+00:00
---
# cisco.dnac.accesspoint_configuration_details_by_task_id_info module – Information module for Accesspoint Configuration Details By Task Id

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
> see [Requirements](accesspoint_configuration_details_by_task_id_info_module.md#ansible-collections-cisco-dnac-accesspoint-configuration-details-by-task-id-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.accesspoint_configuration_details_by_task_id_info`.

New in cisco.dnac 6.7.0

- [Synopsis](accesspoint_configuration_details_by_task_id_info_module.md#synopsis)
- [Requirements](accesspoint_configuration_details_by_task_id_info_module.md#requirements)
- [Parameters](accesspoint_configuration_details_by_task_id_info_module.md#parameters)
- [Notes](accesspoint_configuration_details_by_task_id_info_module.md#notes)
- [See Also](accesspoint_configuration_details_by_task_id_info_module.md#see-also)
- [Examples](accesspoint_configuration_details_by_task_id_info_module.md#examples)
- [Return Values](accesspoint_configuration_details_by_task_id_info_module.md#return-values)

## [Synopsis](accesspoint_configuration_details_by_task_id_info_module.md#id1)

- Get Accesspoint Configuration Details By Task Id by id.
- Users can query the access point configuration result using this intent API.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](accesspoint_configuration_details_by_task_id_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](accesspoint_configuration_details_by_task_id_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **headers**  dictionary | Additional headers. |
| **task_id**  string | Task_id path parameter. Task id information of ap config. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](accesspoint_configuration_details_by_task_id_info_module.md#id4)

> **Note:**
>
> - SDK Method used are wireless.Wireless.get_access_point_configuration_task_result,
> - Paths used are get /dna/intent/api/v1/wireless/accesspoint-configuration/details/{task_id},
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](accesspoint_configuration_details_by_task_id_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Wireless GetAccessPointConfigurationTaskResult](https://developer.cisco.com/docs/dna-center/#!get-access-point-configuration-task-result)
> :   Complete reference of the GetAccessPointConfigurationTaskResult API.

## [Examples](accesspoint_configuration_details_by_task_id_info_module.md#id6)

```yaml+jinja
- name: Get Accesspoint Configuration Details By Task Id by id
  cisco.dnac.accesspoint_configuration_details_by_task_id_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    task_id: string
  register: result
```

## [Return Values](accesspoint_configuration_details_by_task_id_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  list / elements=dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `"[\n  {\n    \"instanceUuid\": {},\n    \"instanceId\": 0,\n    \"authEntityId\": {},\n    \"displayName\": \"string\",\n    \"authEntityClass\": {},\n    \"instanceTenantId\": \"string\",\n    \"_orderedListOEIndex\": 0,\n    \"_orderedListOEAssocName\": {},\n    \"_creationOrderIndex\": 0,\n    \"_isBeingChanged\": true,\n    \"deployPending\": \"string\",\n    \"instanceCreatedOn\": {},\n    \"instanceUpdatedOn\": {},\n    \"changeLogList\": {},\n    \"instanceOrigin\": {},\n    \"lazyLoadedEntities\": {},\n    \"instanceVersion\": 0,\n    \"apName\": \"string\",\n    \"controllerName\": \"string\",\n    \"locationHeirarchy\": \"string\",\n    \"macAddress\": \"string\",\n    \"status\": \"string\",\n    \"statusDetails\": \"string\",\n    \"internalKey\": {\n      \"type\": \"string\",\n      \"id\": 0,\n      \"longType\": \"string\",\n      \"url\": \"string\"\n    }\n  }\n]\n"` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
