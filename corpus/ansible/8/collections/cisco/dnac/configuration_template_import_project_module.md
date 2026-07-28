---
collection: ansible
version: "8"
title: "cisco.dnac.configuration_template_import_project module – Resource module for Configuration Template Import Project"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/configuration_template_import_project_module.html
fetched_at: 2026-07-28T01:21:43+00:00
---
# cisco.dnac.configuration_template_import_project module – Resource module for Configuration Template Import Project

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
> see [Requirements](configuration_template_import_project_module.md#ansible-collections-cisco-dnac-configuration-template-import-project-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.configuration_template_import_project`.

New in cisco.dnac 3.1.0

- [Synopsis](configuration_template_import_project_module.md#synopsis)
- [Requirements](configuration_template_import_project_module.md#requirements)
- [Parameters](configuration_template_import_project_module.md#parameters)
- [Notes](configuration_template_import_project_module.md#notes)
- [See Also](configuration_template_import_project_module.md#see-also)
- [Examples](configuration_template_import_project_module.md#examples)
- [Return Values](configuration_template_import_project_module.md#return-values)

## [Synopsis](configuration_template_import_project_module.md#id1)

- Manage operation create of the resource Configuration Template Import Project.
- Imports the Projects provided in the DTO.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](configuration_template_import_project_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](configuration_template_import_project_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **doVersion**  boolean | DoVersion query parameter. If this flag is true then it creates a new version of the template with the imported contents in case if the templates already exists. ” If this flag is false and if template already exists, then operation fails with ‘Template already exists’ error.  **Choices:**   - `false` - `true` |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](configuration_template_import_project_module.md#id4)

> **Note:**
>
> - SDK Method used are configuration_templates.ConfigurationTemplates.imports_the_projects_provided,
> - Paths used are post /dna/intent/api/v1/template-programmer/project/importprojects,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](configuration_template_import_project_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Configuration Templates ImportsTheProjectsProvided](https://developer.cisco.com/docs/dna-center/#!imports-the-projects-provided)
> :   Complete reference of the ImportsTheProjectsProvided API.

## [Examples](configuration_template_import_project_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.configuration_template_import_project:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    doVersion: true
```

## [Return Values](configuration_template_import_project_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": {"taskId": "string", "url": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
