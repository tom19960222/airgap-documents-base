---
collection: ansible
version: "6"
title: "cisco.dnac.configuration_template_deploy module – Resource module for Configuration Template Deploy"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/configuration_template_deploy_module.html
fetched_at: 2026-07-27T16:51:17+00:00
---
# cisco.dnac.configuration_template_deploy module – Resource module for Configuration Template Deploy

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
> see [Requirements](configuration_template_deploy_module.md#ansible-collections-cisco-dnac-configuration-template-deploy-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.configuration_template_deploy`.

New in cisco.dnac 3.1.0

- [Synopsis](configuration_template_deploy_module.md#synopsis)
- [Requirements](configuration_template_deploy_module.md#requirements)
- [Parameters](configuration_template_deploy_module.md#parameters)
- [Notes](configuration_template_deploy_module.md#notes)
- [See Also](configuration_template_deploy_module.md#see-also)
- [Examples](configuration_template_deploy_module.md#examples)
- [Return Values](configuration_template_deploy_module.md#return-values)

## [Synopsis](configuration_template_deploy_module.md#id1)

- Manage operation create of the resource Configuration Template Deploy.
- API to deploy a template.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](configuration_template_deploy_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](configuration_template_deploy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **forcePushTemplate**  boolean | ForcePushTemplate flag.  Choices:   - `false` - `true` |
| **isComposite**  boolean | Composite template flag.  Choices:   - `false` - `true` |
| **mainTemplateId**  string | Main template UUID of versioned template. |
| **memberTemplateDeploymentInfo**  list / elements=dictionary | MemberTemplateDeploymentInfo. |
| **targetInfo**  list / elements=dictionary | Configuration Template Deploy’s targetInfo. |
| **hostName**  string | Hostname of device is required if targetType is MANAGED_DEVICE_HOSTNAME. |
| **id**  string | UUID of target is required if targetType is MANAGED_DEVICE_UUID. |
| **params**  dictionary | Template params/values to be provisioned. |
| **resourceParams**  list / elements=dictionary | Resource params to be provisioned. |
| **type**  string | Target type of device. |
| **versionedTemplateId**  string | Versioned templateUUID to be provisioned. |
| **templateId**  string | UUID of template to be provisioned. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](configuration_template_deploy_module.md#id4)

> **Note:**
>
> - SDK Method used are configuration_templates.ConfigurationTemplates.deploy_template,
> - Paths used are post /dna/intent/api/v1/template-programmer/template/deploy,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](configuration_template_deploy_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Configuration Templates DeployTemplate](https://developer.cisco.com/docs/dna-center/#!deploy-template)
> :   Complete reference of the DeployTemplate API.

## [Examples](configuration_template_deploy_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.configuration_template_deploy:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    forcePushTemplate: true
    isComposite: true
    mainTemplateId: string
    memberTemplateDeploymentInfo:
    - {}
    targetInfo:
    - hostName: string
      id: string
      params: {}
      resourceParams:
      - {}
      type: string
      versionedTemplateId: string
    templateId: string
```

## [Return Values](configuration_template_deploy_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"deploymentId": "string", "deploymentName": "string", "devices": [{"detailedStatusMessage": "string", "deviceId": "string", "duration": "string", "endTime": "string", "identifier": "string", "ipAddress": "string", "name": "string", "startTime": "string", "status": "string", "targetType": "string"}], "duration": "string", "endTime": "string", "projectName": "string", "startTime": "string", "status": "string", "statusMessage": "string", "templateName": "string", "templateVersion": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
