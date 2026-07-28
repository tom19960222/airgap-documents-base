---
collection: ansible
version: "8"
title: "cisco.dnac.event_artifact_info module – Information module for Event Artifact"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/event_artifact_info_module.html
fetched_at: 2026-07-28T01:22:20+00:00
---
# cisco.dnac.event_artifact_info module – Information module for Event Artifact

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
> see [Requirements](event_artifact_info_module.md#ansible-collections-cisco-dnac-event-artifact-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.event_artifact_info`.

New in cisco.dnac 3.1.0

- [Synopsis](event_artifact_info_module.md#synopsis)
- [Requirements](event_artifact_info_module.md#requirements)
- [Parameters](event_artifact_info_module.md#parameters)
- [Notes](event_artifact_info_module.md#notes)
- [See Also](event_artifact_info_module.md#see-also)
- [Examples](event_artifact_info_module.md#examples)
- [Return Values](event_artifact_info_module.md#return-values)

## [Synopsis](event_artifact_info_module.md#id1)

- Get all Event Artifact.
- Gets the list of artifacts based on provided offset and limit.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](event_artifact_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](event_artifact_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **eventIds**  string | EventIds query parameter. List of eventIds. |
| **headers**  dictionary | Additional headers. |
| **limit**  integer | Limit query parameter. |
| **offset**  integer | Offset query parameter. Record start offset. |
| **order**  string | Order query parameter. Sorting order (asc/desc). |
| **search**  string | Search query parameter. Findd matches in name, description, eventId, type, category. |
| **sortBy**  string | SortBy query parameter. Sort by field. |
| **tags**  string | Tags query parameter. Tags defined. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](event_artifact_info_module.md#id4)

> **Note:**
>
> - SDK Method used are event_management.EventManagement.get_eventartifacts,
> - Paths used are get /dna/system/api/v1/event/artifact,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](event_artifact_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Event Management GetEventArtifacts](https://developer.cisco.com/docs/dna-center/#!get-event-artifacts)
> :   Complete reference of the GetEventArtifacts API.

## [Examples](event_artifact_info_module.md#id6)

```yaml+jinja
- name: Get all Event Artifact
  cisco.dnac.event_artifact_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    eventIds: string
    tags: string
    offset: 0
    limit: 0
    sortBy: string
    order: string
    search: string
  register: result
```

## [Return Values](event_artifact_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  list / elements=dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `"[\n  {\n    \"version\": \"string\",\n    \"artifactId\": \"string\",\n    \"namespace\": \"string\",\n    \"name\": \"string\",\n    \"description\": \"string\",\n    \"domain\": \"string\",\n    \"subDomain\": \"string\",\n    \"tags\": [\n      \"string\"\n    ],\n    \"isTemplateEnabled\": true,\n    \"ciscoDNAEventLink\": \"string\",\n    \"note\": \"string\",\n    \"isPrivate\": true,\n    \"eventPayload\": {\n      \"eventId\": \"string\",\n      \"version\": \"string\",\n      \"category\": \"string\",\n      \"type\": \"string\",\n      \"source\": \"string\",\n      \"severity\": \"string\",\n      \"details\": {\n        \"device_ip\": \"string\",\n        \"message\": \"string\"\n      },\n      \"additionalDetails\": {}\n    },\n    \"eventTemplates\": [\n      {}\n    ],\n    \"isTenantAware\": true,\n    \"supportedConnectorTypes\": [\n      \"string\"\n    ],\n    \"tenantId\": \"string\"\n  }\n]\n"` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
