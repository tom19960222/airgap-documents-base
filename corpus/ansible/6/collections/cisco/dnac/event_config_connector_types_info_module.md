---
collection: ansible
version: "6"
title: "cisco.dnac.event_config_connector_types_info module – Information module for Event Config Connector Types"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/event_config_connector_types_info_module.html
fetched_at: 2026-07-27T16:51:51+00:00
---
# cisco.dnac.event_config_connector_types_info module – Information module for Event Config Connector Types

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
> see [Requirements](event_config_connector_types_info_module.md#ansible-collections-cisco-dnac-event-config-connector-types-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.event_config_connector_types_info`.

New in cisco.dnac 6.0.0

- [Synopsis](event_config_connector_types_info_module.md#synopsis)
- [Requirements](event_config_connector_types_info_module.md#requirements)
- [Parameters](event_config_connector_types_info_module.md#parameters)
- [Notes](event_config_connector_types_info_module.md#notes)
- [See Also](event_config_connector_types_info_module.md#see-also)
- [Examples](event_config_connector_types_info_module.md#examples)
- [Return Values](event_config_connector_types_info_module.md#return-values)

## [Synopsis](event_config_connector_types_info_module.md#id1)

- Get all Event Config Connector Types.
- Get the list of connector types.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](event_config_connector_types_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](event_config_connector_types_info_module.md#id3)

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
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](event_config_connector_types_info_module.md#id4)

> **Note:**
>
> - SDK Method used are event_management.EventManagement.get_connector_types,
> - Paths used are get /dna/system/api/v1/event/config/connector-types,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](event_config_connector_types_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Event Management GetConnectorTypes](https://developer.cisco.com/docs/dna-center/#!get-connector-types)
> :   Complete reference of the GetConnectorTypes API.

## [Examples](event_config_connector_types_info_module.md#id6)

```yaml+jinja
- name: Get all Event Config Connector Types
  cisco.dnac.event_config_connector_types_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
```

## [Return Values](event_config_connector_types_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  list / elements=dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `"[\n  {\n    \"connectorType\": \"string\",\n    \"displayName\": \"string\",\n    \"isDefaultSupported\": true,\n    \"isCustomConnector\": true\n  }\n]\n"` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
