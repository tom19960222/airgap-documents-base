---
collection: ansible
version: "8"
title: "cisco.dnac.sensor_test_template_duplicate module – Resource module for Sensor Test Template Duplicate"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/sensor_test_template_duplicate_module.html
fetched_at: 2026-07-28T01:24:51+00:00
---
# cisco.dnac.sensor_test_template_duplicate module – Resource module for Sensor Test Template Duplicate

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
> see [Requirements](sensor_test_template_duplicate_module.md#ansible-collections-cisco-dnac-sensor-test-template-duplicate-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.sensor_test_template_duplicate`.

New in cisco.dnac 3.1.0

- [Synopsis](sensor_test_template_duplicate_module.md#synopsis)
- [Requirements](sensor_test_template_duplicate_module.md#requirements)
- [Parameters](sensor_test_template_duplicate_module.md#parameters)
- [Notes](sensor_test_template_duplicate_module.md#notes)
- [See Also](sensor_test_template_duplicate_module.md#see-also)
- [Examples](sensor_test_template_duplicate_module.md#examples)
- [Return Values](sensor_test_template_duplicate_module.md#return-values)

## [Synopsis](sensor_test_template_duplicate_module.md#id1)

- Manage operation update of the resource Sensor Test Template Duplicate.
- Intent API to duplicate an existing SENSOR test template.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](sensor_test_template_duplicate_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](sensor_test_template_duplicate_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **newTemplateName**  string | New Template Name. |
| **templateName**  string | Template Name. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](sensor_test_template_duplicate_module.md#id4)

> **Note:**
>
> - SDK Method used are sensors.Sensors.duplicate_sensor_test_template,
> - Paths used are put /dna/intent/api/v1/sensorTestTemplate,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](sensor_test_template_duplicate_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Sensors DuplicateSensorTestTemplate](https://developer.cisco.com/docs/dna-center/#!duplicate-sensor-test-template)
> :   Complete reference of the DuplicateSensorTestTemplate API.

## [Examples](sensor_test_template_duplicate_module.md#id6)

```yaml+jinja
- name: Update all
  cisco.dnac.sensor_test_template_duplicate:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    newTemplateName: string
    templateName: string
```

## [Return Values](sensor_test_template_duplicate_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": {"_id": "string", "apCoverage": [{"bands": "string", "numberOfApsToTest": 0, "rssiThreshold": 0}], "connection": "string", "encryptionMode": "string", "frequency": {}, "lastModifiedTime": 0, "legacyTestSuite": true, "location": {}, "locationInfoList": [{"allSensors": true, "locationId": "string", "locationType": "string", "macAddressList": [{}], "siteHierarchy": "string"}], "modelVersion": 0, "name": "string", "numAssociatedSensor": 0, "numNeighborAPThreshold": 0, "radioAsSensorRemoved": true, "rssiThreshold": 0, "runNow": "string", "schedule": {"frequency": {"unit": "string", "value": 0}, "scheduleRange": [{"day": "string", "timeRange": [{"frequency": {"unit": "string", "value": 0}, "from": "string", "to": "string"}]}], "startTime": 0, "testScheduleMode": "string"}, "scheduleInDays": 0, "sensors": [{}], "showWlcUpgradeBanner": true, "siteHierarchy": {}, "ssids": [{"authProtocol": {}, "authType": "string", "authTypeRcvd": {}, "bands": {}, "certdownloadurl": {}, "certfilename": {}, "certpassphrase": {}, "certstatus": "string", "certxferprotocol": "string", "eapMethod": {}, "extWebAuth": true, "extWebAuthAccessUrl": {}, "extWebAuthHtmlTag": [{}], "extWebAuthPortal": {}, "extWebAuthVirtualIp": {}, "id": 0, "layer3webAuthEmailAddress": {}, "layer3webAuthpassword": {}, "layer3webAuthsecurity": {}, "layer3webAuthuserName": {}, "numAps": 0, "numSensors": 0, "password": {}, "profileName": "string", "psk": "string", "qosPolicy": "string", "scep": true, "ssid": "string", "status": "string", "tests": [{"config": [{}], "name": "string"}], "thirdParty": {"selected": true}, "username": {}, "validFrom": 0, "validTo": 0, "whiteList": true, "wlanId": 0, "wlc": {}}], "startTime": 0, "status": "string", "tenantId": {}, "testDurationEstimate": 0, "testScheduleMode": "string", "testTemplate": true, "tests": {}, "version": 0, "wlans": [{}]}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
