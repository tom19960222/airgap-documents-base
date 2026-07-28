---
collection: ansible
version: "8"
title: "cisco.dnac.event_series_info module – Information module for Event Series"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/event_series_info_module.html
fetched_at: 2026-07-28T01:22:28+00:00
---
# cisco.dnac.event_series_info module – Information module for Event Series

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
> see [Requirements](event_series_info_module.md#ansible-collections-cisco-dnac-event-series-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.event_series_info`.

New in cisco.dnac 3.1.0

- [Synopsis](event_series_info_module.md#synopsis)
- [Requirements](event_series_info_module.md#requirements)
- [Parameters](event_series_info_module.md#parameters)
- [Notes](event_series_info_module.md#notes)
- [See Also](event_series_info_module.md#see-also)
- [Examples](event_series_info_module.md#examples)
- [Return Values](event_series_info_module.md#return-values)

## [Synopsis](event_series_info_module.md#id1)

- Get all Event Series.
- Get the list of Published Notifications.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](event_series_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](event_series_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **category**  string | Category query parameter. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **domain**  string | Domain query parameter. |
| **endTime**  integer | EndTime query parameter. End Time in milliseconds. |
| **eventIds**  string | EventIds query parameter. The registered EventId should be provided. |
| **headers**  dictionary | Additional headers. |
| **limit**  integer | Limit query parameter. |
| **namespace**  string | Namespace query parameter. |
| **offset**  integer | Offset query parameter. Start Offset. |
| **order**  string | Order query parameter. Ascending/Descending order asc/desc. |
| **severity**  string | Severity query parameter. |
| **siteId**  string | SiteId query parameter. Site Id. |
| **sortBy**  string | SortBy query parameter. Sort By column. |
| **source**  string | Source query parameter. |
| **startTime**  integer | StartTime query parameter. Start Time in milliseconds. |
| **subDomain**  string | SubDomain query parameter. Sub Domain. |
| **tags**  string | Tags query parameter. |
| **type**  string | Type query parameter. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](event_series_info_module.md#id4)

> **Note:**
>
> - SDK Method used are event_management.EventManagement.get_notifications,
> - Paths used are get /dna/intent/api/v1/event/event-series,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](event_series_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Event Management GetNotifications](https://developer.cisco.com/docs/dna-center/#!get-notifications)
> :   Complete reference of the GetNotifications API.

## [Examples](event_series_info_module.md#id6)

```yaml+jinja
- name: Get all Event Series
  cisco.dnac.event_series_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    eventIds: string
    startTime: 0
    endTime: 0
    category: string
    type: string
    severity: string
    domain: string
    subDomain: string
    source: string
    offset: 0
    limit: 0
    sortBy: string
    order: string
    tags: string
    namespace: string
    siteId: string
  register: result
```

## [Return Values](event_series_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  list / elements=dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `"[\n  {\n    \"eventId\": \"string\",\n    \"instanceId\": \"string\",\n    \"namespace\": \"string\",\n    \"name\": \"string\",\n    \"description\": \"string\",\n    \"version\": \"string\",\n    \"category\": \"string\",\n    \"domain\": \"string\",\n    \"subDomain\": \"string\",\n    \"type\": \"string\",\n    \"severity\": \"string\",\n    \"source\": \"string\",\n    \"timestamp\": \"string\",\n    \"details\": \"string\",\n    \"eventHierarchy\": \"string\",\n    \"network\": {\n      \"siteId\": \"string\",\n      \"deviceId\": \"string\"\n    }\n  }\n]\n"` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
