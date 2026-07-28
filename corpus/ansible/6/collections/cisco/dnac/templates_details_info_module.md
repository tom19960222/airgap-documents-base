---
collection: ansible
version: "6"
title: "cisco.dnac.templates_details_info module – Information module for Templates Details"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/templates_details_info_module.html
fetched_at: 2026-07-27T16:54:39+00:00
---
# cisco.dnac.templates_details_info module – Information module for Templates Details

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
> see [Requirements](templates_details_info_module.md#ansible-collections-cisco-dnac-templates-details-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.templates_details_info`.

New in cisco.dnac 4.0.0

- [Synopsis](templates_details_info_module.md#synopsis)
- [Requirements](templates_details_info_module.md#requirements)
- [Parameters](templates_details_info_module.md#parameters)
- [Notes](templates_details_info_module.md#notes)
- [See Also](templates_details_info_module.md#see-also)
- [Examples](templates_details_info_module.md#examples)
- [Return Values](templates_details_info_module.md#return-values)

## [Synopsis](templates_details_info_module.md#id1)

- Get all Templates Details.
- Get templates details.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](templates_details_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](templates_details_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allTemplateAttributes**  boolean | AllTemplateAttributes query parameter. Return all template attributes.  Choices:   - `false` - `true` |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **filterConflictingTemplates**  boolean | FilterConflictingTemplates query parameter. Filter template(s) based on confliting templates.  Choices:   - `false` - `true` |
| **headers**  dictionary | Additional headers. |
| **id**  string | Id query parameter. Id of template to be searched. |
| **includeVersionDetails**  boolean | IncludeVersionDetails query parameter. Include template version details.  Choices:   - `false` - `true` |
| **limit**  integer | Limit query parameter. Limits number of results. |
| **name**  string | Name query parameter. Name of template to be searched. |
| **offset**  integer | Offset query parameter. Index of first result. |
| **productFamily**  string | ProductFamily query parameter. Filter template(s) based on device family. |
| **productSeries**  string | ProductSeries query parameter. Filter template(s) based on device series. |
| **productType**  string | ProductType query parameter. Filter template(s) based on device type. |
| **projectId**  string | ProjectId query parameter. Filter template(s) based on project id. |
| **projectName**  string | ProjectName query parameter. Filter template(s) based on project name. |
| **softwareType**  string | SoftwareType query parameter. Filter template(s) based software type. |
| **softwareVersion**  string | SoftwareVersion query parameter. Filter template(s) based softwareVersion. |
| **sortOrder**  string | SortOrder query parameter. Sort Order Ascending (asc) or Descending (dsc). |
| **tags**  list / elements=string | Tags query parameter. Filter template(s) based on tags. |
| **unCommitted**  boolean | UnCommitted query parameter. Return uncommitted template.  Choices:   - `false` - `true` |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](templates_details_info_module.md#id4)

> **Note:**
>
> - SDK Method used are configuration_templates.ConfigurationTemplates.get_templates_details,
> - Paths used are get /dna/intent/api/v2/template-programmer/template,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](templates_details_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Configuration Templates GetTemplatesDetails](https://developer.cisco.com/docs/dna-center/#!get-template-s-details)
> :   Complete reference of the GetTemplatesDetails API.

## [Examples](templates_details_info_module.md#id6)

```yaml+jinja
- name: Get all Templates Details
  cisco.dnac.templates_details_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
    name: string
    projectId: string
    projectName: string
    softwareType: string
    softwareVersion: string
    productFamily: string
    productSeries: string
    productType: string
    filterConflictingTemplates: True
    tags: []
    unCommitted: True
    sortOrder: string
    allTemplateAttributes: True
    includeVersionDetails: True
    offset: 0
    limit: 0
  register: result
```

## [Return Values](templates_details_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"response": [{"author": "string", "composite": true, "containingTemplates": [{"composite": true, "description": "string", "deviceTypes": [{"productFamily": "string", "productSeries": "string", "productType": "string"}], "id": "string", "language": "string", "name": "string", "projectName": "string", "rollbackTemplateParams": [{"binding": "string", "customOrder": 0, "dataType": "string", "defaultValue": "string", "description": "string", "displayName": "string", "group": "string", "id": "string", "instructionText": "string", "key": "string", "notParam": true, "order": 0, "paramArray": true, "parameterName": "string", "provider": "string", "range": [{"id": "string", "maxValue": 0, "minValue": 0}], "required": true, "selection": {"defaultSelectedValues": ["string"], "id": "string", "selectionType": "string", "selectionValues": {}}}], "tags": [{"id": "string", "name": "string"}], "templateContent": "string", "templateParams": [{"binding": "string", "customOrder": 0, "dataType": "string", "defaultValue": "string", "description": "string", "displayName": "string", "group": "string", "id": "string", "instructionText": "string", "key": "string", "notParam": true, "order": 0, "paramArray": true, "parameterName": "string", "provider": "string", "range": [{"id": "string", "maxValue": 0, "minValue": 0}], "required": true, "selection": {"defaultSelectedValues": ["string"], "id": "string", "selectionType": "string", "selectionValues": {}}}], "version": "string"}], "createTime": 0, "customParamsOrder": true, "description": "string", "deviceTypes": [{"productFamily": "string", "productSeries": "string", "productType": "string"}], "documentDatabase": true, "failurePolicy": "string", "id": "string", "language": "string", "lastUpdateTime": 0, "latestVersionTime": 0, "name": "string", "parentTemplateId": "string", "projectAssociated": true, "projectId": "string", "projectName": "string", "rollbackTemplateContent": "string", "rollbackTemplateParams": [{"binding": "string", "customOrder": 0, "dataType": "string", "defaultValue": "string", "description": "string", "displayName": "string", "group": "string", "id": "string", "instructionText": "string", "key": "string", "notParam": true, "order": 0, "paramArray": true, "parameterName": "string", "provider": "string", "range": [{"id": "string", "maxValue": 0, "minValue": 0}], "required": true, "selection": {"defaultSelectedValues": ["string"], "id": "string", "selectionType": "string", "selectionValues": {}}}], "softwareType": "string", "softwareVariant": "string", "softwareVersion": "string", "tags": [{"id": "string", "name": "string"}], "templateContent": "string", "templateParams": [{"binding": "string", "customOrder": 0, "dataType": "string", "defaultValue": "string", "description": "string", "displayName": "string", "group": "string", "id": "string", "instructionText": "string", "key": "string", "notParam": true, "order": 0, "paramArray": true, "parameterName": "string", "provider": "string", "range": [{"id": "string", "maxValue": 0, "minValue": 0}], "required": true, "selection": {"defaultSelectedValues": ["string"], "id": "string", "selectionType": "string", "selectionValues": {}}}], "validationErrors": {"rollbackTemplateErrors": [{}], "templateErrors": [{}], "templateId": "string", "templateVersion": "string"}, "version": "string", "versionsInfo": [{"author": "string", "description": "string", "id": "string", "version": "string", "versionComment": "string", "versionTime": 0}]}], "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
