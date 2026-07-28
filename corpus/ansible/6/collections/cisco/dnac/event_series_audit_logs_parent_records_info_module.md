---
collection: ansible
version: "6"
title: "cisco.dnac.event_series_audit_logs_parent_records_info module – Information module for Event Series Audit Logs Parent Records"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/event_series_audit_logs_parent_records_info_module.html
fetched_at: 2026-07-27T16:51:55+00:00
---
# cisco.dnac.event_series_audit_logs_parent_records_info module – Information module for Event Series Audit Logs Parent Records

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
> see [Requirements](event_series_audit_logs_parent_records_info_module.md#ansible-collections-cisco-dnac-event-series-audit-logs-parent-records-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.event_series_audit_logs_parent_records_info`.

New in cisco.dnac 3.1.0

- [Synopsis](event_series_audit_logs_parent_records_info_module.md#synopsis)
- [Requirements](event_series_audit_logs_parent_records_info_module.md#requirements)
- [Parameters](event_series_audit_logs_parent_records_info_module.md#parameters)
- [Notes](event_series_audit_logs_parent_records_info_module.md#notes)
- [See Also](event_series_audit_logs_parent_records_info_module.md#see-also)
- [Examples](event_series_audit_logs_parent_records_info_module.md#examples)
- [Return Values](event_series_audit_logs_parent_records_info_module.md#return-values)

## [Synopsis](event_series_audit_logs_parent_records_info_module.md#id1)

- Get all Event Series Audit Logs Parent Records.
- Get Parent Audit Log Event instances from the Event-Hub.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](event_series_audit_logs_parent_records_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](event_series_audit_logs_parent_records_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **category**  string | Category query parameter. Audit Log notification’s event category. Supported values INFO, WARN, ERROR, ALERT, TASK_PROGRESS, TASK_FAILURE, TASK_COMPLETE, COMMAND, QUERY, CONVERSATION. |
| **context**  string | Context query parameter. Audit Log notification’s event correlationId. |
| **description**  string | Description query parameter. String full/partial search - (Provided input string is case insensitively matched for records). |
| **deviceId**  string | DeviceId query parameter. Audit Log notification’s deviceId. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **domain**  string | Domain query parameter. Audit Log notification’s event domain. |
| **endTime**  integer | EndTime query parameter. End Time in milliseconds since Epoch Eg. 1597961437211 (when provided startTime is mandatory). |
| **eventHierarchy**  string | EventHierarchy query parameter. Audit Log notification’s event eventHierarchy. Example “US.CA.San Jose” OR “US.CA” OR “CA.San Jose” - Delimiter for hierarchy separation is “.”. |
| **eventId**  string | EventId query parameter. Audit Log notification’s event ID. |
| **headers**  dictionary | Additional headers. |
| **instanceId**  string | InstanceId query parameter. InstanceID of the Audit Log. |
| **isSystemEvents**  boolean | IsSystemEvents query parameter. Parameter to filter system generated audit-logs.  Choices:   - `false` - `true` |
| **limit**  integer | Limit query parameter. Number of Audit Log records to be returned per page. |
| **name**  string | Name query parameter. Audit Log notification event name. |
| **offset**  integer | Offset query parameter. Position of a particular Audit Log record in the data. |
| **order**  string | Order query parameter. Order of the sorted Audit Log records. Default value is desc by timestamp. Supported values asc, desc. |
| **severity**  string | Severity query parameter. Audit Log notification’s event severity. Supported values 1, 2, 3, 4, 5. |
| **siteId**  string | SiteId query parameter. Audit Log notification’s siteId. |
| **sortBy**  string | SortBy query parameter. Sort the Audit Logs by certain fields. Supported values are event notification header attributes. |
| **source**  string | Source query parameter. Audit Log notification’s event source. |
| **startTime**  integer | StartTime query parameter. Start Time in milliseconds since Epoch Eg. 1597950637211 (when provided endTime is mandatory). |
| **subDomain**  string | SubDomain query parameter. Audit Log notification’s event sub-domain. |
| **userId**  string | UserId query parameter. Audit Log notification’s event userId. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](event_series_audit_logs_parent_records_info_module.md#id4)

> **Note:**
>
> - SDK Method used are event_management.EventManagement.get_auditlog_parent_records,
> - Paths used are get /dna/data/api/v1/event/event-series/audit-log/parent-records,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](event_series_audit_logs_parent_records_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Event Management GetAuditLogParentRecords](https://developer.cisco.com/docs/dna-center/#!get-audit-log-parent-records)
> :   Complete reference of the GetAuditLogParentRecords API.

## [Examples](event_series_audit_logs_parent_records_info_module.md#id6)

```yaml+jinja
- name: Get all Event Series Audit Logs Parent Records
  cisco.dnac.event_series_audit_logs_parent_records_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    instanceId: string
    name: string
    eventId: string
    category: string
    severity: string
    domain: string
    subDomain: string
    source: string
    userId: string
    context: string
    eventHierarchy: string
    siteId: string
    deviceId: string
    isSystemEvents: True
    description: string
    offset: 0
    limit: 0
    startTime: 0
    endTime: 0
    sortBy: string
    order: string
  register: result
```

## [Return Values](event_series_audit_logs_parent_records_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  list / elements=dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `"[\n  {\n    \"version\": \"string\",\n    \"instanceId\": \"string\",\n    \"eventId\": \"string\",\n    \"namespace\": \"string\",\n    \"name\": \"string\",\n    \"description\": \"string\",\n    \"type\": \"string\",\n    \"category\": \"string\",\n    \"domain\": \"string\",\n    \"subDomain\": \"string\",\n    \"severity\": 0,\n    \"source\": \"string\",\n    \"timestamp\": 0,\n    \"tags\": [\n      {}\n    ],\n    \"details\": {},\n    \"ciscoDnaEventLink\": {},\n    \"note\": {},\n    \"tntId\": \"string\",\n    \"context\": \"string\",\n    \"userId\": \"string\",\n    \"i18n\": \"string\",\n    \"eventHierarchy\": {},\n    \"message\": \"string\",\n    \"messageParams\": {},\n    \"additionalDetails\": {},\n    \"parentInstanceId\": {},\n    \"network\": {},\n    \"childCount\": 0,\n    \"tenantId\": \"string\"\n  }\n]\n"` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
