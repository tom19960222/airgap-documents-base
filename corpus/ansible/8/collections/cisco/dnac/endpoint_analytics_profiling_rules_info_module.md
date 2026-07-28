---
collection: ansible
version: "8"
title: "cisco.dnac.endpoint_analytics_profiling_rules_info module – Information module for Endpoint Analytics Profiling Rules"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/endpoint_analytics_profiling_rules_info_module.html
fetched_at: 2026-07-28T01:22:16+00:00
---
# cisco.dnac.endpoint_analytics_profiling_rules_info module – Information module for Endpoint Analytics Profiling Rules

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
> see [Requirements](endpoint_analytics_profiling_rules_info_module.md#ansible-collections-cisco-dnac-endpoint-analytics-profiling-rules-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.endpoint_analytics_profiling_rules_info`.

New in cisco.dnac 4.0.0

- [Synopsis](endpoint_analytics_profiling_rules_info_module.md#synopsis)
- [Requirements](endpoint_analytics_profiling_rules_info_module.md#requirements)
- [Parameters](endpoint_analytics_profiling_rules_info_module.md#parameters)
- [Notes](endpoint_analytics_profiling_rules_info_module.md#notes)
- [Examples](endpoint_analytics_profiling_rules_info_module.md#examples)
- [Return Values](endpoint_analytics_profiling_rules_info_module.md#return-values)

## [Synopsis](endpoint_analytics_profiling_rules_info_module.md#id1)

- Get all Endpoint Analytics Profiling Rules.
- Get Endpoint Analytics Profiling Rules by id.
- Fetches details of the profiling rule for the given ‘ruleId’.
- This API fetches the list of profiling rules. It can be used to show profiling rules in client applications, or export those from an environment. ‘POST /profiling-rules/bulk’ API can be used to import such exported rules into another environment. If this API is used to export rules to be imported into another Cisco DNA Center system, then ensure that ‘includeDeleted’ parameter is ‘true’, so that deleted rules get synchronized correctly. Use query parameters to filter the data, as required. If no filter is provided, then it will include only rules of type ‘Custom Rule’ in the response. By default, the response is limited to 500 records. Use ‘limit’ parameter to fetch higher number of records, if required. ‘GET /profiling-rules/count’ API can be used to find out the total number of rules in the system.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](endpoint_analytics_profiling_rules_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](endpoint_analytics_profiling_rules_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **headers**  dictionary | Additional headers. |
| **includeDeleted**  boolean | IncludeDeleted query parameter. Flag to indicate whether deleted rules should be part of the records fetched.  **Choices:**   - `false` - `true` |
| **limit**  integer | Limit query parameter. Maximum number of records to be fetched. If not provided, 500 records will be fetched by default. To fetch all the records in the system, provide a large value for this parameter. |
| **offset**  integer | Offset query parameter. Record offset to start data fetch at. Offset starts at zero. |
| **order**  string | Order query parameter. Order to be used for sorting. |
| **ruleId**  string | RuleId path parameter. Unique rule identifier. |
| **ruleType**  string | RuleType query parameter. Use comma-separated list of rule types to filter the data. Defaults to ‘Custom Rule’. |
| **sortBy**  string | SortBy query parameter. Name of the column to sort the results on. Please note that fetch might take more time if sorting is requested. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](endpoint_analytics_profiling_rules_info_module.md#id4)

> **Note:**
>
> - SDK Method used are policy.Policy.get_details_of_a_single_profiling_rule, policy.Policy.get_list_of_profiling_rules,
> - Paths used are get /dna/intent/api/v1/endpoint-analytics/profiling-rules, get /dna/intent/api/v1/endpoint-analytics/profiling-rules/{ruleId},
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [Examples](endpoint_analytics_profiling_rules_info_module.md#id5)

```yaml+jinja
- name: Get all Endpoint Analytics Profiling Rules
  cisco.dnac.endpoint_analytics_profiling_rules_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    ruleType: string
    includeDeleted: True
    limit: 0
    offset: 0
    sortBy: string
    order: string
  register: result

- name: Get Endpoint Analytics Profiling Rules by id
  cisco.dnac.endpoint_analytics_profiling_rules_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    ruleId: string
  register: result
```

## [Return Values](endpoint_analytics_profiling_rules_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"clusterId": "string", "conditionGroups": {"condition": {"attribute": "string", "attributeDictionary": "string", "operator": "string", "value": "string"}, "conditionGroup": [{}], "operator": "string", "type": "string"}, "isDeleted": true, "lastModifiedBy": "string", "lastModifiedOn": 0, "pluginId": "string", "rejected": true, "result": {"deviceType": ["string"], "hardwareManufacturer": ["string"], "hardwareModel": ["string"], "operatingSystem": ["string"]}, "ruleId": "string", "ruleName": "string", "rulePriority": 0, "ruleType": "string", "ruleVersion": 0, "sourcePriority": 0, "usedAttributes": ["string"]}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
