---
collection: ansible
version: "8"
title: "cisco.dnac.template_intent module – Resource module for Template functions"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/template_intent_module.html
fetched_at: 2026-07-28T01:25:28+00:00
---
# cisco.dnac.template_intent module – Resource module for Template functions

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
> see [Requirements](template_intent_module.md#ansible-collections-cisco-dnac-template-intent-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.template_intent`.

New in cisco.dnac 6.6.0

- [Synopsis](template_intent_module.md#synopsis)
- [Requirements](template_intent_module.md#requirements)
- [Parameters](template_intent_module.md#parameters)
- [Notes](template_intent_module.md#notes)
- [Examples](template_intent_module.md#examples)
- [Return Values](template_intent_module.md#return-values)

## [Synopsis](template_intent_module.md#id1)

- Manage operations create, update and delete of the resource Configuration Template.
- API to create a template by project name and template name.
- API to update a template by template name and project name.
- API to delete a template by template name and project name.

## [Requirements](template_intent_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk == 2.4.5
- python >= 3.5

## [Parameters](template_intent_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary / required | List of details of templates being managed. |
| **author**  string | Author of template. |
| **composite**  boolean | Is it composite template.  **Choices:**   - `false` - `true` |
| **containingTemplates**  list / elements=dictionary | Configuration Template Create’s containingTemplates. |
| **composite**  boolean | Is it composite template.  **Choices:**   - `false` - `true` |
| **description**  string | Description of template. |
| **deviceTypes**  list / elements=dictionary | deviceTypes on which templates would be applied. |
| **productFamily**  string | Device family. |
| **productSeries**  string | Device series. |
| **productType**  string | Device type. |
| **id**  string | UUID of template. |
| **language**  string | Template language  **Choices:**   - `"JINJA"` - `"VELOCITY"` |
| **name**  string | Name of template. |
| **projectDescription**  string | Description of the project created. |
| **projectName**  string / required | Name of the project under which templates are managed. |
| **rollbackTemplateParams**  list / elements=dictionary | Params required for template rollback. |
| **binding**  string | Bind to source. |
| **customOrder**  integer | CustomOrder of template param. |
| **dataType**  string | Datatype of template param. |
| **defaultValue**  string | Default value of template param. |
| **description**  string | Description of template param. |
| **displayName**  string | Display name of param. |
| **group**  string | Group. |
| **id**  string | UUID of template param. |
| **instructionText**  string | Instruction text for param. |
| **key**  string | Key. |
| **notParam**  boolean | Is it not a variable.  **Choices:**   - `false` - `true` |
| **order**  integer | Order of template param. |
| **paramArray**  boolean | Is it an array.  **Choices:**   - `false` - `true` |
| **parameterName**  string | Name of template param. |
| **provider**  string | Provider. |
| **range**  list / elements=dictionary | Configuration Template Create’s range. |
| **id**  string | UUID of range. |
| **maxValue**  integer | Max value of range. |
| **minValue**  integer | Min value of range. |
| **required**  boolean | Is param required.  **Choices:**   - `false` - `true` |
| **selection**  dictionary | Configuration Template Create’s selection. |
| **defaultSelectedValues**  list / elements=string | Default selection values. |
| **id**  string | UUID of selection. |
| **selectionType**  string | Type of selection(SINGLE_SELECT or MULTI_SELECT). |
| **selectionValues**  dictionary | Selection values. |
| **tags**  list / elements=dictionary | Configuration Template Create’s tags. |
| **id**  string | UUID of tag. |
| **name**  string | Name of tag. |
| **templateContent**  string | Template content. |
| **templateParams**  list / elements=dictionary | Configuration Template Create’s templateParams. |
| **binding**  string | Bind to source. |
| **customOrder**  integer | CustomOrder of template param. |
| **dataType**  string | Datatype of template param. |
| **defaultValue**  string | Default value of template param. |
| **description**  string | Description of template param. |
| **displayName**  string | Display name of param. |
| **group**  string | Group. |
| **id**  string | UUID of template param. |
| **instructionText**  string | Instruction text for param. |
| **key**  string | Key. |
| **notParam**  boolean | Is it not a variable.  **Choices:**   - `false` - `true` |
| **order**  integer | Order of template param. |
| **paramArray**  boolean | Is it an array.  **Choices:**   - `false` - `true` |
| **parameterName**  string | Name of template param. |
| **provider**  string | Provider. |
| **range**  list / elements=dictionary | Configuration Template Create’s range. |
| **id**  string | UUID of range. |
| **maxValue**  integer | Max value of range. |
| **minValue**  integer | Min value of range. |
| **required**  boolean | Is param required.  **Choices:**   - `false` - `true` |
| **selection**  dictionary | Configuration Template Create’s selection. |
| **defaultSelectedValues**  list / elements=string | Default selection values. |
| **id**  string | UUID of selection. |
| **selectionType**  string | Type of selection(SINGLE_SELECT or MULTI_SELECT). |
| **selectionValues**  dictionary | Selection values. |
| **version**  string | Current version of template. |
| **createTime**  integer | Create time of template. |
| **customParamsOrder**  boolean | Custom Params Order.  **Choices:**   - `false` - `true` |
| **deviceTypes**  list / elements=dictionary | Configuration Template Create’s deviceTypes. This field is mandatory to create a new template. |
| **productFamily**  string | Device family. |
| **productSeries**  string | Device series. |
| **productType**  string | Device type. |
| **failurePolicy**  string | Define failure policy if template provisioning fails. |
| **language**  string | Template language  **Choices:**   - `"JINJA"` - `"VELOCITY"` |
| **lastUpdateTime**  integer | Update time of template. |
| **latestVersionTime**  integer | Latest versioned template time. |
| **parentTemplateId**  string | Parent templateID. |
| **projectDescription**  string | Project Description. |
| **projectId**  string | Project UUID. |
| **projectName**  string | Project name. |
| **rollbackTemplateContent**  string | Rollback template content. |
| **rollbackTemplateParams**  list / elements=dictionary | Configuration Template Create’s rollbackTemplateParams. |
| **binding**  string | Bind to source. |
| **customOrder**  integer | CustomOrder of template param. |
| **dataType**  string | Datatype of template param. |
| **defaultValue**  string | Default value of template param. |
| **description**  string | Description of template param. |
| **displayName**  string | Display name of param. |
| **group**  string | Group. |
| **id**  string | UUID of template param. |
| **instructionText**  string | Instruction text for param. |
| **key**  string | Key. |
| **notParam**  boolean | Is it not a variable.  **Choices:**   - `false` - `true` |
| **order**  integer | Order of template param. |
| **paramArray**  boolean | Is it an array.  **Choices:**   - `false` - `true` |
| **parameterName**  string | Name of template param. |
| **provider**  string | Provider. |
| **range**  list / elements=dictionary | Configuration Template Create’s range. |
| **id**  string | UUID of range. |
| **maxValue**  integer | Max value of range. |
| **minValue**  integer | Min value of range. |
| **required**  boolean | Is param required.  **Choices:**   - `false` - `true` |
| **selection**  dictionary | Configuration Template Create’s selection. |
| **defaultSelectedValues**  list / elements=string | Default selection values. |
| **id**  string | UUID of selection. |
| **selectionType**  string | Type of selection(SINGLE_SELECT or MULTI_SELECT). |
| **selectionValues**  dictionary | Selection values. |
| **softwareType**  string | Applicable device software type. This field is mandatory to create a new template. |
| **softwareVariant**  string | Applicable device software variant. |
| **softwareVersion**  string | Applicable device software version. |
| **template_description**  string | Description of template. |
| **template_tag**  list / elements=dictionary | Configuration Template Create’s tags. |
| **id**  string | UUID of tag. |
| **name**  string | Name of tag. |
| **templateContent**  string | Template content. |
| **templateName**  string | Name of template. This field is mandatory to create a new template. |
| **templateParams**  list / elements=dictionary | Configuration Template Create’s templateParams. |
| **binding**  string | Bind to source. |
| **customOrder**  integer | CustomOrder of template param. |
| **dataType**  string | Datatype of template param. |
| **defaultValue**  string | Default value of template param. |
| **description**  string | Description of template param. |
| **displayName**  string | Display name of param. |
| **group**  string | Group. |
| **id**  string | UUID of template param. |
| **instructionText**  string | Instruction text for param. |
| **key**  string | Key. |
| **notParam**  boolean | Is it not a variable.  **Choices:**   - `false` - `true` |
| **order**  integer | Order of template param. |
| **paramArray**  boolean | Is it an array.  **Choices:**   - `false` - `true` |
| **parameterName**  string | Name of template param. |
| **provider**  string | Provider. |
| **range**  list / elements=dictionary | Configuration Template Create’s range. |
| **id**  string | UUID of range. |
| **maxValue**  integer | Max value of range. |
| **minValue**  integer | Min value of range. |
| **required**  boolean | Is param required.  **Choices:**   - `false` - `true` |
| **selection**  dictionary | Configuration Template Create’s selection. |
| **defaultSelectedValues**  list / elements=string | Default selection values. |
| **id**  string | UUID of selection. |
| **selectionType**  string | Type of selection(SINGLE_SELECT or MULTI_SELECT). |
| **selectionValues**  dictionary | Selection values. |
| **validationErrors**  dictionary | Configuration Template Create’s validationErrors. |
| **rollbackTemplateErrors**  list / elements=dictionary | Validation or design conflicts errors of rollback template. |
| **templateErrors**  list / elements=dictionary | Validation or design conflicts errors. |
| **templateId**  string | UUID of template. |
| **templateVersion**  string | Current version of template. |
| **version**  string | Current version of template. |
| **versionDescription**  string | Template version comments. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_log**  boolean | Flag for logging playbook execution details. If set to true the log file will be created at the location of the execution with the name dnac.log  **Choices:**   - `false` ← (default) - `true` |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  string | The Cisco DNA Center port.  **Default:** `"443"` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.2.3.3"` |
| **state**  string | The state of DNAC after module completion.  **Choices:**   - `"merged"` ← (default) - `"deleted"` |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](template_intent_module.md#id4)

> **Note:**
>
> - SDK Method used are configuration_templates.ConfigurationTemplates.create_template, configuration_templates.ConfigurationTemplates.deletes_the_template, configuration_templates.ConfigurationTemplates.update_template,
> - Paths used are post /dna/intent/api/v1/template-programmer/project/{projectId}/template, delete /dna/intent/api/v1/template-programmer/template/{templateId}, put /dna/intent/api/v1/template-programmer/template,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [Examples](template_intent_module.md#id5)

```yaml+jinja
- name: Create a new template
  cisco.dnac.template_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    state: merged
    config:
        author: string
        composite: true
        createTime: 0
        customParamsOrder: true
        description: string
        deviceTypes:
        - productFamily: string
          productSeries: string
          productType: string
        failurePolicy: string
        id: string
        language: string
        lastUpdateTime: 0
        latestVersionTime: 0
        name: string
        parentTemplateId: string
        projectId: string
        projectName: string
        projectDescription: string
        rollbackTemplateContent: string
        softwareType: string
        softwareVariant: string
        softwareVersion: string
        tags:
        - id: string
          name: string
        templateContent: string
        validationErrors:
            rollbackTemplateErrors:
            - {}
            templateErrors:
            - {}
            templateId: string
            templateVersion: string
        version: string
```

## [Return Values](template_intent_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **response_1**  dictionary | A dictionary with versioning details of the template as returned by the DNAC Python SDK  **Returned:** always  **Sample:** `"{\n  \"response\": {\n                    \"endTime\": 0,\n                    \"version\": 0,\n                    \"data\": String,\n                    \"startTime\": 0,\n                    \"username\": String,\n                    \"progress\": String,\n                    \"serviceType\": String, \"rootId\": String,\n                    \"isError\": bool,\n                    \"instanceTenantId\": String,\n                    \"id\": String\n                    \"version\": 0\n              },\n  \"msg\": String\n}\n"` |
| **response_2**  list / elements=string | A list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `["{\n  \"response\": []", "\n  \"msg\": String\n}\n"]` |
| **response_3**  dictionary | A dictionary with the exisiting template deatails as returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `"{\n  \"response\": {},\n  \"msg\": String\n}\n"` |

### Authors

- Madhan Sankaranarayanan (@madhansansel) Rishita Chowdhary (@rishitachowdhary)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
