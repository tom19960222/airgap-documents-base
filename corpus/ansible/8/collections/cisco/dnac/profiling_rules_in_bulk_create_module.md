---
collection: ansible
version: "8"
title: "cisco.dnac.profiling_rules_in_bulk_create module – Resource module for Profiling Rules In Bulk Create"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/profiling_rules_in_bulk_create_module.html
fetched_at: 2026-07-28T01:24:12+00:00
---
# cisco.dnac.profiling_rules_in_bulk_create module – Resource module for Profiling Rules In Bulk Create

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
> see [Requirements](profiling_rules_in_bulk_create_module.md#ansible-collections-cisco-dnac-profiling-rules-in-bulk-create-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.profiling_rules_in_bulk_create`.

New in cisco.dnac 4.0.0

- [Synopsis](profiling_rules_in_bulk_create_module.md#synopsis)
- [Requirements](profiling_rules_in_bulk_create_module.md#requirements)
- [Parameters](profiling_rules_in_bulk_create_module.md#parameters)
- [Notes](profiling_rules_in_bulk_create_module.md#notes)
- [Examples](profiling_rules_in_bulk_create_module.md#examples)
- [Return Values](profiling_rules_in_bulk_create_module.md#return-values)

## [Synopsis](profiling_rules_in_bulk_create_module.md#id1)

- Manage operation create of the resource Profiling Rules In Bulk Create.
- This API imports the given list of profiling rules. For each record, 1) If ‘ruleType’ for a record is not ‘Custom Rule’, then it is rejected. 2) If ‘ruleId’ is provided in the input record,

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](profiling_rules_in_bulk_create_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](profiling_rules_in_bulk_create_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **profilingRules**  list / elements=dictionary | Profiling Rules In Bulk Create’s profilingRules. |
| **clusterId**  string | Unique identifier for ML cluster. Only applicable for ‘ML Rule’. |
| **conditionGroups**  dictionary | Profiling Rules In Bulk Create’s conditionGroups. |
| **condition**  dictionary | Profiling Rules In Bulk Create’s condition. |
| **attribute**  string | Profiling Rules In Bulk Create’s attribute. |
| **attributeDictionary**  string | Profiling Rules In Bulk Create’s attributeDictionary. |
| **operator**  string | Profiling Rules In Bulk Create’s operator. |
| **value**  string | Profiling Rules In Bulk Create’s value. |
| **conditionGroup**  list / elements=dictionary | Profiling Rules In Bulk Create’s conditionGroup. |
| **operator**  string | Profiling Rules In Bulk Create’s operator. |
| **type**  string | Profiling Rules In Bulk Create’s type. |
| **isDeleted**  boolean | Flag to indicate whether the rule was deleted.  **Choices:**   - `false` - `true` |
| **lastModifiedBy**  string | User that last modified the rule. It is read-only, and is ignored if provided as part of input request. |
| **lastModifiedOn**  integer | Timestamp (in epoch milliseconds) of last modification. It is read-only, and is ignored if provided as part of input request. |
| **pluginId**  string | Plugin for the rule. Only applicable for ‘Cisco Default’ rules. |
| **rejected**  boolean | Flag to indicate whether rule has been rejected by user or not. Only applicable for ‘ML Rule’.  **Choices:**   - `false` - `true` |
| **result**  dictionary | Profiling Rules In Bulk Create’s result. |
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

## [Notes](profiling_rules_in_bulk_create_module.md#id4)

> **Note:**
>
> - SDK Method used are policy.Policy.import_profiling_rules_in_bulk,
> - Paths used are post /dna/intent/api/v1/endpoint-analytics/profiling-rules/bulk,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [Examples](profiling_rules_in_bulk_create_module.md#id5)

```yaml+jinja
- name: Create
  cisco.dnac.profiling_rules_in_bulk_create:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    profilingRules:
    - clusterId: string
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
```

## [Return Values](profiling_rules_in_bulk_create_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
