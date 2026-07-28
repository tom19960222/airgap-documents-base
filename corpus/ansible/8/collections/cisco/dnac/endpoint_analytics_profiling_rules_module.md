---
collection: ansible
version: "8"
title: "cisco.dnac.endpoint_analytics_profiling_rules module – Resource module for Endpoint Analytics Profiling Rules"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/endpoint_analytics_profiling_rules_module.html
fetched_at: 2026-07-28T01:22:16+00:00
---
# cisco.dnac.endpoint_analytics_profiling_rules module – Resource module for Endpoint Analytics Profiling Rules

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
> see [Requirements](endpoint_analytics_profiling_rules_module.md#ansible-collections-cisco-dnac-endpoint-analytics-profiling-rules-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.endpoint_analytics_profiling_rules`.

New in cisco.dnac 4.0.0

- [Synopsis](endpoint_analytics_profiling_rules_module.md#synopsis)
- [Requirements](endpoint_analytics_profiling_rules_module.md#requirements)
- [Parameters](endpoint_analytics_profiling_rules_module.md#parameters)
- [Notes](endpoint_analytics_profiling_rules_module.md#notes)
- [Examples](endpoint_analytics_profiling_rules_module.md#examples)
- [Return Values](endpoint_analytics_profiling_rules_module.md#return-values)

## [Synopsis](endpoint_analytics_profiling_rules_module.md#id1)

- Manage operations create, update and delete of the resource Endpoint Analytics Profiling Rules.
- Creates profiling rule from the request body.
- Deletes the profiling rule for the given ‘ruleId’.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](endpoint_analytics_profiling_rules_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](endpoint_analytics_profiling_rules_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **clusterId**  string | Unique identifier for ML cluster. Only applicable for ‘ML Rule’. |
| **conditionGroups**  dictionary | Endpoint Analytics Profiling Rules’s conditionGroups. |
| **condition**  dictionary | Endpoint Analytics Profiling Rules’s condition. |
| **attribute**  string | Endpoint Analytics Profiling Rules’s attribute. |
| **attributeDictionary**  string | Endpoint Analytics Profiling Rules’s attributeDictionary. |
| **operator**  string | Endpoint Analytics Profiling Rules’s operator. |
| **value**  string | Endpoint Analytics Profiling Rules’s value. |
| **conditionGroup**  list / elements=dictionary | Endpoint Analytics Profiling Rules’s conditionGroup. |
| **operator**  string | Endpoint Analytics Profiling Rules’s operator. |
| **type**  string | Endpoint Analytics Profiling Rules’s type. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **isDeleted**  boolean | Flag to indicate whether the rule was deleted.  **Choices:**   - `false` - `true` |
| **lastModifiedBy**  string | User that last modified the rule. It is read-only, and is ignored if provided as part of input request. |
| **lastModifiedOn**  integer | Timestamp (in epoch milliseconds) of last modification. It is read-only, and is ignored if provided as part of input request. |
| **pluginId**  string | Plugin for the rule. Only applicable for ‘Cisco Default’ rules. |
| **rejected**  boolean | Flag to indicate whether rule has been rejected by user or not. Only applicable for ‘ML Rule’.  **Choices:**   - `false` - `true` |
| **result**  dictionary | Endpoint Analytics Profiling Rules’s result. |
| **deviceType**  list / elements=string | List of device types determined by the current rule. |
| **hardwareManufacturer**  list / elements=string | List of hardware manufacturers determined by the current rule. |
| **hardwareModel**  list / elements=string | List of hardware models determined by the current rule. |
| **operatingSystem**  list / elements=string | List of operating systems determined by the current rule. |
| **ruleId**  string | Unique identifier for the rule. This is normally generated by the system, and client does not need to provide it for rules that need to be newly created. |
| **ruleName**  string | Human readable name for the rule. |
| **rulePriority**  integer | Priority for the rule. |
| **ruleType**  string | Type of the rule. Allowed values are ‘Cisco Default - Static’, ‘Cisco Default - Dynamic’, ‘Custom Rule’, ‘ML Rule’. |
| **ruleVersion**  integer | Version of the rule. |
| **sourcePriority**  integer | Source priority for the rule. |
| **usedAttributes**  list / elements=string | List of attributes used in the rule. Only applicable for ‘Cisco Default’ rules. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](endpoint_analytics_profiling_rules_module.md#id4)

> **Note:**
>
> - SDK Method used are policy.Policy.create_a_profiling_rule, policy.Policy.delete_an_existing_profiling_rule, policy.Policy.update_an_existing_profiling_rule,
> - Paths used are post /dna/intent/api/v1/endpoint-analytics/profiling-rules, delete /dna/intent/api/v1/endpoint-analytics/profiling-rules/{ruleId},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [Examples](endpoint_analytics_profiling_rules_module.md#id5)

```yaml+jinja
- name: Create
  cisco.dnac.endpoint_analytics_profiling_rules:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    clusterId: string
    conditionGroups:
      condition:
        attribute: string
        attributeDictionary: string
        operator: string
        value: string
      conditionGroup:
      - {}
      operator: string
      type: string
    isDeleted: true
    lastModifiedBy: string
    lastModifiedOn: 0
    pluginId: string
    rejected: true
    result:
      deviceType:
      - string
      hardwareManufacturer:
      - string
      hardwareModel:
      - string
      operatingSystem:
      - string
    ruleId: string
    ruleName: string
    rulePriority: 0
    ruleType: string
    ruleVersion: 0
    sourcePriority: 0
    usedAttributes:
    - string

- name: Update by id
  cisco.dnac.endpoint_analytics_profiling_rules:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    clusterId: string
    conditionGroups:
      condition:
        attribute: string
        attributeDictionary: string
        operator: string
        value: string
      conditionGroup:
      - {}
      operator: string
      type: string
    isDeleted: true
    lastModifiedBy: string
    lastModifiedOn: 0
    pluginId: string
    rejected: true
    result:
      deviceType:
      - string
      hardwareManufacturer:
      - string
      hardwareModel:
      - string
      operatingSystem:
      - string
    ruleId: string
    ruleName: string
    rulePriority: 0
    ruleType: string
    ruleVersion: 0
    sourcePriority: 0
    usedAttributes:
    - string

- name: Delete by id
  cisco.dnac.endpoint_analytics_profiling_rules:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    ruleId: string
```

## [Return Values](endpoint_analytics_profiling_rules_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"id": "string", "link": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
