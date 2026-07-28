---
collection: ansible
version: "6"
title: "cisco.dnac.template_preview module – Resource module for Template Preview"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/template_preview_module.html
fetched_at: 2026-07-27T16:54:39+00:00
---
# cisco.dnac.template_preview module – Resource module for Template Preview

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
> see [Requirements](template_preview_module.md#ansible-collections-cisco-dnac-template-preview-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.template_preview`.

New in cisco.dnac 3.1.0

- [Synopsis](template_preview_module.md#synopsis)
- [Requirements](template_preview_module.md#requirements)
- [Parameters](template_preview_module.md#parameters)
- [Notes](template_preview_module.md#notes)
- [See Also](template_preview_module.md#see-also)
- [Examples](template_preview_module.md#examples)
- [Return Values](template_preview_module.md#return-values)

## [Synopsis](template_preview_module.md#id1)

- Manage operation update of the resource Template Preview.
- API to preview a template.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](template_preview_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](template_preview_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **deviceId**  string | UUID of device to get template preview. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **params**  dictionary | Params to render preview. |
| **resourceParams**  list / elements=dictionary | Resource params to render preview. |
| **templateId**  string | UUID of template to get template preview. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](template_preview_module.md#id4)

> **Note:**
>
> - SDK Method used are configuration_templates.ConfigurationTemplates.preview_template,
> - Paths used are put /dna/intent/api/v1/template-programmer/template/preview,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](template_preview_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Configuration Templates PreviewTemplate](https://developer.cisco.com/docs/dna-center/#!preview-template)
> :   Complete reference of the PreviewTemplate API.

## [Examples](template_preview_module.md#id6)

```yaml+jinja
- name: Update all
  cisco.dnac.template_preview:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    deviceId: string
    params: {}
    resourceParams:
    - {}
    templateId: string
```

## [Return Values](template_preview_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"cliPreview": "string", "deviceId": "string", "templateId": "string", "validationErrors": {}}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
