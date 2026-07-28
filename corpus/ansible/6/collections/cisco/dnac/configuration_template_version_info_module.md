---
collection: ansible
version: "6"
title: "cisco.dnac.configuration_template_version_info module – Information module for Configuration Template Version"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/configuration_template_version_info_module.html
fetched_at: 2026-07-27T16:51:25+00:00
---
# cisco.dnac.configuration_template_version_info module – Information module for Configuration Template Version

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
> see [Requirements](configuration_template_version_info_module.md#ansible-collections-cisco-dnac-configuration-template-version-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.configuration_template_version_info`.

New in cisco.dnac 3.1.0

- [Synopsis](configuration_template_version_info_module.md#synopsis)
- [Requirements](configuration_template_version_info_module.md#requirements)
- [Parameters](configuration_template_version_info_module.md#parameters)
- [Notes](configuration_template_version_info_module.md#notes)
- [See Also](configuration_template_version_info_module.md#see-also)
- [Examples](configuration_template_version_info_module.md#examples)
- [Return Values](configuration_template_version_info_module.md#return-values)

## [Synopsis](configuration_template_version_info_module.md#id1)

- Get Configuration Template Version by id.
- Get all the versions of template by its id.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](configuration_template_version_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](configuration_template_version_info_module.md#id3)

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
| **templateId**  string | TemplateId path parameter. TemplateId(UUID) to get list of versioned templates. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](configuration_template_version_info_module.md#id4)

> **Note:**
>
> - SDK Method used are configuration_templates.ConfigurationTemplates.get_template_versions,
> - Paths used are get /dna/intent/api/v1/template-programmer/template/version/{templateId},
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](configuration_template_version_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Configuration Templates GetsAllTheVersionsOfAGivenTemplate](https://developer.cisco.com/docs/dna-center/#!gets-all-the-versions-of-a-given-template)
> :   Complete reference of the GetsAllTheVersionsOfAGivenTemplate API.

## [Examples](configuration_template_version_info_module.md#id6)

```yaml+jinja
- name: Get Configuration Template Version by id
  cisco.dnac.configuration_template_version_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    templateId: string
  register: result
```

## [Return Values](configuration_template_version_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  list / elements=dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `"[\n  {\n    \"composite\": true,\n    \"name\": \"string\",\n    \"projectId\": \"string\",\n    \"projectName\": \"string\",\n    \"templateId\": \"string\",\n    \"versionsInfo\": [\n      {\n        \"author\": \"string\",\n        \"description\": \"string\",\n        \"id\": \"string\",\n        \"version\": \"string\",\n        \"versionComment\": \"string\",\n        \"versionTime\": 0\n      }\n    ]\n  }\n]\n"` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
