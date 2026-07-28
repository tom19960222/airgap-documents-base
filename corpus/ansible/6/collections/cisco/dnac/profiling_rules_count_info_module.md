---
collection: ansible
version: "6"
title: "cisco.dnac.profiling_rules_count_info module – Information module for Profiling Rules Count"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/profiling_rules_count_info_module.html
fetched_at: 2026-07-27T16:53:27+00:00
---
# cisco.dnac.profiling_rules_count_info module – Information module for Profiling Rules Count

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
> see [Requirements](profiling_rules_count_info_module.md#ansible-collections-cisco-dnac-profiling-rules-count-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.profiling_rules_count_info`.

New in cisco.dnac 4.0.0

- [Synopsis](profiling_rules_count_info_module.md#synopsis)
- [Requirements](profiling_rules_count_info_module.md#requirements)
- [Parameters](profiling_rules_count_info_module.md#parameters)
- [Notes](profiling_rules_count_info_module.md#notes)
- [Examples](profiling_rules_count_info_module.md#examples)
- [Return Values](profiling_rules_count_info_module.md#return-values)

## [Synopsis](profiling_rules_count_info_module.md#id1)

- Get all Profiling Rules Count.
- This API fetches the count of profiling rules based on the filter values provided in the query parameters. The filter parameters are same as that of ‘GET /profiling-rules’ API, excluding the pagination and sort parameters.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](profiling_rules_count_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.4.9
- python >= 3.5

## [Parameters](profiling_rules_count_info_module.md#id3)

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
| **includeDeleted**  boolean | IncludeDeleted query parameter. Flag to indicate whether deleted rules should be part of the records fetched.  Choices:   - `false` - `true` |
| **ruleType**  string | RuleType query parameter. Use comma-separated list of rule types to filter the data. Defaults to ‘Custom Rule’. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](profiling_rules_count_info_module.md#id4)

> **Note:**
>
> - SDK Method used are policy.Policy.get_count_of_profiling_rules,
> - Paths used are get /dna/intent/api/v1/endpoint-analytics/profiling-rules/count,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [Examples](profiling_rules_count_info_module.md#id5)

```yaml+jinja
- name: Get all Profiling Rules Count
  cisco.dnac.profiling_rules_count_info:
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
  register: result
```

## [Return Values](profiling_rules_count_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"count": 0}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
