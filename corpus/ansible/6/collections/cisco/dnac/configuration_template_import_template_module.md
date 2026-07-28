---
collection: ansible
version: "6"
title: "cisco.dnac.configuration_template_import_template module – Resource module for Configuration Template Import Template"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/configuration_template_import_template_module.html
fetched_at: 2026-07-27T16:51:21+00:00
---
# cisco.dnac.configuration_template_import_template module – Resource module for Configuration Template Import Template

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
> see [Requirements](configuration_template_import_template_module.md#ansible-collections-cisco-dnac-configuration-template-import-template-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.configuration_template_import_template`.

New in cisco.dnac 3.1.0

- [Synopsis](configuration_template_import_template_module.md#synopsis)
- [Requirements](configuration_template_import_template_module.md#requirements)
- [Parameters](configuration_template_import_template_module.md#parameters)
- [Notes](configuration_template_import_template_module.md#notes)
- [See Also](configuration_template_import_template_module.md#see-also)
- [Examples](configuration_template_import_template_module.md#examples)
- [Return Values](configuration_template_import_template_module.md#return-values)

## [Synopsis](configuration_template_import_template_module.md#id1)

- Manage operation create of the resource Configuration Template Import Template.
- Imports the templates provided in the DTO by project Name.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](configuration_template_import_template_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](configuration_template_import_template_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **doVersion**  boolean | DoVersion query parameter. If this flag is true then it creates a new version of the template with the imported contents in case if the templates already exists. ” If this flag is false and if template already exists, then operation fails with ‘Template already exists’ error.  Choices:   - `false` - `true` |
| **payload**  list / elements=dictionary | Configuration Template Import Template’s payload. |
| **author**  string | Author of template. |
| **composite**  boolean | Is it composite template.  Choices:   - `false` - `true` |
| **containingTemplates**  list / elements=dictionary | Configuration Template Import Template’s containingTemplates. |
| **composite**  boolean | Is it composite template.  Choices:   - `false` - `true` |
| **description**  string | Description of template. |
| **deviceTypes**  list / elements=dictionary | Configuration Template Import Template’s deviceTypes. |
| **productFamily**  string | Device family. |
| **productSeries**  string | Device series. |
| **productType**  string | Device type. |
| **id**  string | UUID of template. |
| **language**  string | Template language (JINJA or VELOCITY). |
| **name**  string | Name of template. |
| **projectName**  string | Project name. |
| **rollbackTemplateParams**  list / elements=dictionary | Configuration Template Import Template’s rollbackTemplateParams. |
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
| **notParam**  boolean | Is it not a variable.  Choices:   - `false` - `true` |
| **order**  integer | Order of template param. |
| **paramArray**  boolean | Is it an array.  Choices:   - `false` - `true` |
| **parameterName**  string | Name of template param. |
| **provider**  string | Provider. |
| **range**  list / elements=dictionary | Configuration Template Import Template’s range. |
| **id**  string | UUID of range. |
| **maxValue**  integer | Max value of range. |
| **minValue**  integer | Min value of range. |
| **required**  boolean | Is param required.  Choices:   - `false` - `true` |
| **selection**  dictionary | Configuration Template Import Template’s selection. |
| **defaultSelectedValues**  list / elements=string | Default selection values. |
| **id**  string | UUID of selection. |
| **selectionType**  string | Type of selection(SINGLE_SELECT or MULTI_SELECT). |
| **selectionValues**  dictionary | Selection values. |
| **tags**  list / elements=dictionary | Configuration Template Import Template’s tags. |
| **id**  string | UUID of tag. |
| **name**  string | Name of tag. |
| **templateContent**  string | Template content. |
| **templateParams**  list / elements=dictionary | Configuration Template Import Template’s templateParams. |
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
| **notParam**  boolean | Is it not a variable.  Choices:   - `false` - `true` |
| **order**  integer | Order of template param. |
| **paramArray**  boolean | Is it an array.  Choices:   - `false` - `true` |
| **parameterName**  string | Name of template param. |
| **provider**  string | Provider. |
| **range**  list / elements=dictionary | Configuration Template Import Template’s range. |
| **id**  string | UUID of range. |
| **maxValue**  integer | Max value of range. |
| **minValue**  integer | Min value of range. |
| **required**  boolean | Is param required.  Choices:   - `false` - `true` |
| **selection**  dictionary | Configuration Template Import Template’s selection. |
| **defaultSelectedValues**  list / elements=string | Default selection values. |
| **id**  string | UUID of selection. |
| **selectionType**  string | Type of selection(SINGLE_SELECT or MULTI_SELECT). |
| **selectionValues**  dictionary | Selection values. |
| **version**  string | Current version of template. |
| **createTime**  integer | Create time of template. |
| **customParamsOrder**  boolean | Custom Params Order.  Choices:   - `false` - `true` |
| **description**  string | Description of template. |
| **deviceTypes**  list / elements=dictionary | Configuration Template Import Template’s deviceTypes. |
| **productFamily**  string | Device family. |
| **productSeries**  string | Device series. |
| **productType**  string | Device type. |
| **failurePolicy**  string | Define failure policy if template provisioning fails. |
| **id**  string | UUID of template. |
| **language**  string | Template language (JINJA or VELOCITY). |
| **lastUpdateTime**  integer | Update time of template. |
| **latestVersionTime**  integer | Latest versioned template time. |
| **name**  string | Name of template. |
| **parentTemplateId**  string | Parent templateID. |
| **projectId**  string | Project UUID. |
| **projectName**  string | Project name. |
| **rollbackTemplateContent**  string | Rollback template content. |
| **rollbackTemplateParams**  list / elements=dictionary | Configuration Template Import Template’s rollbackTemplateParams. |
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
| **notParam**  boolean | Is it not a variable.  Choices:   - `false` - `true` |
| **order**  integer | Order of template param. |
| **paramArray**  boolean | Is it an array.  Choices:   - `false` - `true` |
| **parameterName**  string | Name of template param. |
| **provider**  string | Provider. |
| **range**  list / elements=dictionary | Configuration Template Import Template’s range. |
| **id**  string | UUID of range. |
| **maxValue**  integer | Max value of range. |
| **minValue**  integer | Min value of range. |
| **required**  boolean | Is param required.  Choices:   - `false` - `true` |
| **selection**  dictionary | Configuration Template Import Template’s selection. |
| **defaultSelectedValues**  list / elements=string | Default selection values. |
| **id**  string | UUID of selection. |
| **selectionType**  string | Type of selection(SINGLE_SELECT or MULTI_SELECT). |
| **selectionValues**  dictionary | Selection values. |
| **softwareType**  string | Applicable device software type. |
| **softwareVariant**  string | Applicable device software variant. |
| **softwareVersion**  string | Applicable device software version. |
| **tags**  list / elements=dictionary | Configuration Template Import Template’s tags. |
| **id**  string | UUID of tag. |
| **name**  string | Name of tag. |
| **templateContent**  string | Template content. |
| **templateParams**  list / elements=dictionary | Configuration Template Import Template’s templateParams. |
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
| **notParam**  boolean | Is it not a variable.  Choices:   - `false` - `true` |
| **order**  integer | Order of template param. |
| **paramArray**  boolean | Is it an array.  Choices:   - `false` - `true` |
| **parameterName**  string | Name of template param. |
| **provider**  string | Provider. |
| **range**  list / elements=dictionary | Configuration Template Import Template’s range. |
| **id**  string | UUID of range. |
| **maxValue**  integer | Max value of range. |
| **minValue**  integer | Min value of range. |
| **required**  boolean | Is param required.  Choices:   - `false` - `true` |
| **selection**  dictionary | Configuration Template Import Template’s selection. |
| **defaultSelectedValues**  list / elements=string | Default selection values. |
| **id**  string | UUID of selection. |
| **selectionType**  string | Type of selection(SINGLE_SELECT or MULTI_SELECT). |
| **selectionValues**  dictionary | Selection values. |
| **validationErrors**  dictionary | Configuration Template Import Template’s validationErrors. |
| **rollbackTemplateErrors**  list / elements=dictionary | Validation or design conflicts errors of rollback template. |
| **templateErrors**  list / elements=dictionary | Validation or design conflicts errors. |
| **templateId**  string | UUID of template. |
| **templateVersion**  string | Current version of template. |
| **version**  string | Current version of template. |
| **projectName**  string | ProjectName path parameter. Project name to create template under the project. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](configuration_template_import_template_module.md#id4)

> **Note:**
>
> - SDK Method used are configuration_templates.ConfigurationTemplates.imports_the_templates_provided,
> - Paths used are post /dna/intent/api/v1/template-programmer/project/name/{projectName}/template/importtemplates,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](configuration_template_import_template_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Configuration Templates ImportsTheTemplatesProvided](https://developer.cisco.com/docs/dna-center/#!imports-the-templates-provided)
> :   Complete reference of the ImportsTheTemplatesProvided API.

## [Examples](configuration_template_import_template_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.configuration_template_import_template:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    doVersion: true
    payload:
    - author: string
      composite: true
      containingTemplates:
      - composite: true
        description: string
        deviceTypes:
        - productFamily: string
          productSeries: string
          productType: string
        id: string
        language: string
        name: string
        projectName: string
        rollbackTemplateParams:
        - binding: string
          customOrder: 0
          dataType: string
          defaultValue: string
          description: string
          displayName: string
          group: string
          id: string
          instructionText: string
          key: string
          notParam: true
          order: 0
          paramArray: true
          parameterName: string
          provider: string
          range:
          - id: string
            maxValue: 0
            minValue: 0
          required: true
          selection:
            defaultSelectedValues:
            - string
            id: string
            selectionType: string
            selectionValues: {}
        tags:
        - id: string
          name: string
        templateContent: string
        templateParams:
        - binding: string
          customOrder: 0
          dataType: string
          defaultValue: string
          description: string
          displayName: string
          group: string
          id: string
          instructionText: string
          key: string
          notParam: true
          order: 0
          paramArray: true
          parameterName: string
          provider: string
          range:
          - id: string
            maxValue: 0
            minValue: 0
          required: true
          selection:
            defaultSelectedValues:
            - string
            id: string
            selectionType: string
            selectionValues: {}
        version: string
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
      rollbackTemplateContent: string
      rollbackTemplateParams:
      - binding: string
        customOrder: 0
        dataType: string
        defaultValue: string
        description: string
        displayName: string
        group: string
        id: string
        instructionText: string
        key: string
        notParam: true
        order: 0
        paramArray: true
        parameterName: string
        provider: string
        range:
        - id: string
          maxValue: 0
          minValue: 0
        required: true
        selection:
          defaultSelectedValues:
          - string
          id: string
          selectionType: string
          selectionValues: {}
      softwareType: string
      softwareVariant: string
      softwareVersion: string
      tags:
      - id: string
        name: string
      templateContent: string
      templateParams:
      - binding: string
        customOrder: 0
        dataType: string
        defaultValue: string
        description: string
        displayName: string
        group: string
        id: string
        instructionText: string
        key: string
        notParam: true
        order: 0
        paramArray: true
        parameterName: string
        provider: string
        range:
        - id: string
          maxValue: 0
          minValue: 0
        required: true
        selection:
          defaultSelectedValues:
          - string
          id: string
          selectionType: string
          selectionValues: {}
      validationErrors:
        rollbackTemplateErrors:
        - {}
        templateErrors:
        - {}
        templateId: string
        templateVersion: string
      version: string
    projectName: string
```

## [Return Values](configuration_template_import_template_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"response": {"taskId": "string", "url": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
