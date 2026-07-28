---
collection: ansible
version: "6"
title: "cisco.dnac.sensor_test_template_edit module – Resource module for Sensor Test Template Edit"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/sensor_test_template_edit_module.html
fetched_at: 2026-07-27T16:54:07+00:00
---
# cisco.dnac.sensor_test_template_edit module – Resource module for Sensor Test Template Edit

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
> see [Requirements](sensor_test_template_edit_module.md#ansible-collections-cisco-dnac-sensor-test-template-edit-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.sensor_test_template_edit`.

New in cisco.dnac 3.1.0

- [Synopsis](sensor_test_template_edit_module.md#synopsis)
- [Requirements](sensor_test_template_edit_module.md#requirements)
- [Parameters](sensor_test_template_edit_module.md#parameters)
- [Notes](sensor_test_template_edit_module.md#notes)
- [See Also](sensor_test_template_edit_module.md#see-also)
- [Examples](sensor_test_template_edit_module.md#examples)
- [Return Values](sensor_test_template_edit_module.md#return-values)

## [Synopsis](sensor_test_template_edit_module.md#id1)

- Manage operation update of the resource Sensor Test Template Edit.
- Intent API to deploy, schedule, or edit and existing SENSOR test template.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](sensor_test_template_edit_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](sensor_test_template_edit_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **locationInfoList**  list / elements=dictionary | Sensor Test Template Edit’s locationInfoList. |
| **allSensors**  boolean | All Sensors.  Choices:   - `false` - `true` |
| **locationId**  string | Location Id. |
| **locationType**  string | Location Type. |
| **siteHierarchy**  string | Site Hierarchy. |
| **schedule**  dictionary | Sensor Test Template Edit’s schedule. |
| **frequency**  dictionary | Sensor Test Template Edit’s frequency. |
| **unit**  string | Unit. |
| **value**  integer | Value. |
| **scheduleRange**  list / elements=dictionary | Sensor Test Template Edit’s scheduleRange. |
| **day**  string | Day. |
| **timeRange**  list / elements=dictionary | Sensor Test Template Edit’s timeRange. |
| **frequency**  dictionary | Sensor Test Template Edit’s frequency. |
| **unit**  string | Unit. |
| **value**  integer | Value. |
| **from**  string | From. |
| **to**  string | To. |
| **testScheduleMode**  string | Test Schedule Mode. |
| **templateName**  string | Template Name. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](sensor_test_template_edit_module.md#id4)

> **Note:**
>
> - SDK Method used are sensors.Sensors.edit_sensor_test_template,
> - Paths used are put /dna/intent/api/v1/AssuranceScheduleSensorTest,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](sensor_test_template_edit_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Sensors EditSensorTestTemplate](https://developer.cisco.com/docs/dna-center/#!edit-sensor-test-template)
> :   Complete reference of the EditSensorTestTemplate API.

## [Examples](sensor_test_template_edit_module.md#id6)

```yaml+jinja
- name: Update all
  cisco.dnac.sensor_test_template_edit:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    locationInfoList:
    - allSensors: true
      locationId: string
      locationType: string
      siteHierarchy: string
    schedule:
      frequency:
        unit: string
        value: 0
      scheduleRange:
      - day: string
        timeRange:
        - frequency:
            unit: string
            value: 0
          from: string
          to: string
      testScheduleMode: string
    templateName: string
```

## [Return Values](sensor_test_template_edit_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"response": {"_id": "string", "apCoverage": [{"bands": "string", "numberOfApsToTest": 0, "rssiThreshold": 0}], "connection": "string", "encryptionMode": "string", "frequency": {}, "lastModifiedTime": 0, "legacyTestSuite": true, "location": {}, "locationInfoList": [{"allSensors": true, "locationId": "string", "locationType": "string", "macAddressList": [{}], "siteHierarchy": "string"}], "modelVersion": 0, "name": "string", "numAssociatedSensor": 0, "numNeighborAPThreshold": 0, "radioAsSensorRemoved": true, "rssiThreshold": 0, "runNow": "string", "schedule": {"frequency": {"unit": "string", "value": 0}, "scheduleRange": [{"day": "string", "timeRange": [{"frequency": {"unit": "string", "value": 0}, "from": "string", "to": "string"}]}], "startTime": 0, "testScheduleMode": "string"}, "scheduleInDays": 0, "sensors": [{}], "showWlcUpgradeBanner": true, "siteHierarchy": {}, "ssids": [{"authProtocol": {}, "authType": "string", "authTypeRcvd": {}, "bands": {}, "certdownloadurl": {}, "certfilename": {}, "certpassphrase": {}, "certstatus": "string", "certxferprotocol": "string", "eapMethod": {}, "extWebAuth": true, "extWebAuthAccessUrl": {}, "extWebAuthHtmlTag": [{}], "extWebAuthPortal": {}, "extWebAuthVirtualIp": {}, "id": 0, "layer3webAuthEmailAddress": {}, "layer3webAuthpassword": {}, "layer3webAuthsecurity": {}, "layer3webAuthuserName": {}, "numAps": 0, "numSensors": 0, "password": {}, "profileName": "string", "psk": "string", "qosPolicy": "string", "scep": true, "ssid": "string", "status": "string", "tests": [{"config": [{}], "name": "string"}], "thirdParty": {"selected": true}, "username": {}, "validFrom": 0, "validTo": 0, "whiteList": true, "wlanId": 0, "wlc": {}}], "startTime": 0, "status": "string", "tenantId": "string", "testDurationEstimate": 0, "testScheduleMode": "string", "testTemplate": true, "tests": {}, "version": 0, "wlans": [{}]}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
