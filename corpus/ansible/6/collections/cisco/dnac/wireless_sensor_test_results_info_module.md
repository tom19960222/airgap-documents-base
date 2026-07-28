---
collection: ansible
version: "6"
title: "cisco.dnac.wireless_sensor_test_results_info module – Information module for Wireless Sensor Test Results"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/wireless_sensor_test_results_info_module.html
fetched_at: 2026-07-27T16:54:58+00:00
---
# cisco.dnac.wireless_sensor_test_results_info module – Information module for Wireless Sensor Test Results

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
> see [Requirements](wireless_sensor_test_results_info_module.md#ansible-collections-cisco-dnac-wireless-sensor-test-results-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.wireless_sensor_test_results_info`.

New in cisco.dnac 3.1.0

- [Synopsis](wireless_sensor_test_results_info_module.md#synopsis)
- [Requirements](wireless_sensor_test_results_info_module.md#requirements)
- [Parameters](wireless_sensor_test_results_info_module.md#parameters)
- [Notes](wireless_sensor_test_results_info_module.md#notes)
- [See Also](wireless_sensor_test_results_info_module.md#see-also)
- [Examples](wireless_sensor_test_results_info_module.md#examples)
- [Return Values](wireless_sensor_test_results_info_module.md#return-values)

## [Synopsis](wireless_sensor_test_results_info_module.md#id1)

- Get all Wireless Sensor Test Results.
- Intent API to get SENSOR test result summary.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](wireless_sensor_test_results_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](wireless_sensor_test_results_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **endTime**  integer | EndTime query parameter. The epoch time in milliseconds. |
| **headers**  dictionary | Additional headers. |
| **siteId**  string | SiteId query parameter. Assurance site UUID. |
| **startTime**  integer | StartTime query parameter. The epoch time in milliseconds. |
| **testFailureBy**  string | TestFailureBy query parameter. Obtain failure statistics group by “area”, “building”, or “floor”. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](wireless_sensor_test_results_info_module.md#id4)

> **Note:**
>
> - SDK Method used are wireless.Wireless.sensor_test_results,
> - Paths used are get /dna/intent/api/v1/AssuranceGetSensorTestResults,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](wireless_sensor_test_results_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Wireless SensorTestResults](https://developer.cisco.com/docs/dna-center/#!sensor-test-results)
> :   Complete reference of the SensorTestResults API.

## [Examples](wireless_sensor_test_results_info_module.md#id6)

```yaml+jinja
- name: Get all Wireless Sensor Test Results
  cisco.dnac.wireless_sensor_test_results_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    siteId: string
    startTime: 0
    endTime: 0
    testFailureBy: string
  register: result
```

## [Return Values](wireless_sensor_test_results_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"failureStats": [{"errorCode": 0, "errorTitle": "string", "testCategory": "string", "testType": "string"}], "summary": {"APP_CONNECTIVITY": {"FILETRANSFER": {"failCount": 0, "passCount": 0}, "HOST_REACHABILITY": {"failCount": 0, "passCount": 0}, "WEBSERVER": {"failCount": 0, "passCount": 0}}, "EMAIL": {"MAILSERVER": {"failCount": 0, "passCount": 0}}, "NETWORK_SERVICES": {"DNS": {"failCount": 0, "passCount": 0}}, "ONBOARDING": {"ASSOC": {"failCount": 0, "passCount": 0}, "AUTH": {"failCount": 0, "passCount": 0}, "DHCP": {"failCount": 0, "passCount": 0}}, "PERFORMANCE": {"IPSLASENDER": {"failCount": 0, "passCount": 0}}, "RF_ASSESSMENT": {"DATA_RATE": {"failCount": 0, "passCount": 0}, "SNR": {"failCount": 0, "passCount": 0}}, "totalTestCount": 0}}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
