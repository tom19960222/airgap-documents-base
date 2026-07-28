---
collection: ansible
version: "6"
title: "cisco.dnac.configuration_template_info module – Information module for Configuration Template"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/configuration_template_info_module.html
fetched_at: 2026-07-27T16:51:22+00:00
---
# cisco.dnac.configuration_template_info module – Information module for Configuration Template

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
> see [Requirements](configuration_template_info_module.md#ansible-collections-cisco-dnac-configuration-template-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.configuration_template_info`.

New in cisco.dnac 3.1.0

- [Synopsis](configuration_template_info_module.md#synopsis)
- [Requirements](configuration_template_info_module.md#requirements)
- [Parameters](configuration_template_info_module.md#parameters)
- [Notes](configuration_template_info_module.md#notes)
- [See Also](configuration_template_info_module.md#see-also)
- [Examples](configuration_template_info_module.md#examples)
- [Return Values](configuration_template_info_module.md#return-values)

## [Synopsis](configuration_template_info_module.md#id1)

- Get all Configuration Template.
- Get Configuration Template by id.
- Details of the template by its id.
- List the templates available.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](configuration_template_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](configuration_template_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **filterConflictingTemplates**  boolean | FilterConflictingTemplates query parameter. Filter template(s) based on confliting templates.  Choices:   - `false` - `true` |
| **headers**  dictionary | Additional headers. |
| **latestVersion**  boolean | LatestVersion query parameter. LatestVersion flag to get the latest versioned template.  Choices:   - `false` - `true` |
| **productFamily**  string | ProductFamily query parameter. Filter template(s) based on device family. |
| **productSeries**  string | ProductSeries query parameter. Filter template(s) based on device series. |
| **productType**  string | ProductType query parameter. Filter template(s) based on device type. |
| **projectId**  string | ProjectId query parameter. Filter template(s) based on project UUID. |
| **projectNames**  list / elements=string | ProjectNames query parameter. Filter template(s) based on project names. |
| **softwareType**  string | SoftwareType query parameter. Filter template(s) based software type. |
| **softwareVersion**  string | SoftwareVersion query parameter. Filter template(s) based softwareVersion. |
| **sortOrder**  string | SortOrder query parameter. Sort Order Ascending (asc) or Descending (des). |
| **tags**  list / elements=string | Tags query parameter. Filter template(s) based on tags. |
| **templateId**  string | TemplateId path parameter. TemplateId(UUID) to get details of the template. |
| **unCommitted**  boolean | UnCommitted query parameter. Filter template(s) based on template commited or not.  Choices:   - `false` - `true` |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](configuration_template_info_module.md#id4)

> **Note:**
>
> - SDK Method used are configuration_templates.ConfigurationTemplates.get_template_details, configuration_templates.ConfigurationTemplates.gets_the_templates_available,
> - Paths used are get /dna/intent/api/v1/template-programmer/template, get /dna/intent/api/v1/template-programmer/template/{templateId},
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](configuration_template_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Configuration Templates GetsDetailsOfAGivenTemplate](https://developer.cisco.com/docs/dna-center/#!gets-details-of-a-given-template)
> :   Complete reference of the GetsDetailsOfAGivenTemplate API.
>
> [Cisco DNA Center documentation for Configuration Templates GetsTheTemplatesAvailable](https://developer.cisco.com/docs/dna-center/#!gets-the-templates-available)
> :   Complete reference of the GetsTheTemplatesAvailable API.

## [Examples](configuration_template_info_module.md#id6)

```yaml+jinja
- name: Get all Configuration Template
  cisco.dnac.configuration_template_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    projectId: string
    softwareType: string
    softwareVersion: string
    productFamily: string
    productSeries: string
    productType: string
    filterConflictingTemplates: True
    tags: []
    projectNames: []
    unCommitted: True
    sortOrder: string
  register: result

- name: Get Configuration Template by id
  cisco.dnac.configuration_template_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    latestVersion: True
    templateId: string
  register: result
```

## [Return Values](configuration_template_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"author": "string", "composite": true, "containingTemplates": [{"composite": true, "description": "string", "deviceTypes": [{"productFamily": "string", "productSeries": "string", "productType": "string"}], "id": "string", "language": "string", "name": "string", "projectName": "string", "rollbackTemplateParams": [{"binding": "string", "customOrder": 0, "dataType": "string", "defaultValue": "string", "description": "string", "displayName": "string", "group": "string", "id": "string", "instructionText": "string", "key": "string", "notParam": true, "order": 0, "paramArray": true, "parameterName": "string", "provider": "string", "range": [{"id": "string", "maxValue": 0, "minValue": 0}], "required": true, "selection": {"defaultSelectedValues": ["string"], "id": "string", "selectionType": "string", "selectionValues": {}}}], "tags": [{"id": "string", "name": "string"}], "templateContent": "string", "templateParams": [{"binding": "string", "customOrder": 0, "dataType": "string", "defaultValue": "string", "description": "string", "displayName": "string", "group": "string", "id": "string", "instructionText": "string", "key": "string", "notParam": true, "order": 0, "paramArray": true, "parameterName": "string", "provider": "string", "range": [{"id": "string", "maxValue": 0, "minValue": 0}], "required": true, "selection": {"defaultSelectedValues": ["string"], "id": "string", "selectionType": "string", "selectionValues": {}}}], "version": "string"}], "createTime": 0, "customParamsOrder": true, "description": "string", "deviceTypes": [{"productFamily": "string", "productSeries": "string", "productType": "string"}], "failurePolicy": "string", "id": "string", "language": "string", "lastUpdateTime": 0, "latestVersionTime": 0, "name": "string", "parentTemplateId": "string", "projectId": "string", "projectName": "string", "rollbackTemplateContent": "string", "rollbackTemplateParams": [{"binding": "string", "customOrder": 0, "dataType": "string", "defaultValue": "string", "description": "string", "displayName": "string", "group": "string", "id": "string", "instructionText": "string", "key": "string", "notParam": true, "order": 0, "paramArray": true, "parameterName": "string", "provider": "string", "range": [{"id": "string", "maxValue": 0, "minValue": 0}], "required": true, "selection": {"defaultSelectedValues": ["string"], "id": "string", "selectionType": "string", "selectionValues": {}}}], "softwareType": "string", "softwareVariant": "string", "softwareVersion": "string", "tags": [{"id": "string", "name": "string"}], "templateContent": "string", "templateParams": [{"binding": "string", "customOrder": 0, "dataType": "string", "defaultValue": "string", "description": "string", "displayName": "string", "group": "string", "id": "string", "instructionText": "string", "key": "string", "notParam": true, "order": 0, "paramArray": true, "parameterName": "string", "provider": "string", "range": [{"id": "string", "maxValue": 0, "minValue": 0}], "required": true, "selection": {"defaultSelectedValues": ["string"], "id": "string", "selectionType": "string", "selectionValues": {}}}], "validationErrors": {"rollbackTemplateErrors": [{}], "templateErrors": [{}], "templateId": "string", "templateVersion": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
