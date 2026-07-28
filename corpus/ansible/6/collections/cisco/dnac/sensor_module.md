---
collection: ansible
version: "6"
title: "cisco.dnac.sensor module – Resource module for Sensor"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/sensor_module.html
fetched_at: 2026-07-27T16:54:04+00:00
---
# cisco.dnac.sensor module – Resource module for Sensor

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
> see [Requirements](sensor_module.md#ansible-collections-cisco-dnac-sensor-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.sensor`.

New in cisco.dnac 3.1.0

- [Synopsis](sensor_module.md#synopsis)
- [Requirements](sensor_module.md#requirements)
- [Parameters](sensor_module.md#parameters)
- [Notes](sensor_module.md#notes)
- [See Also](sensor_module.md#see-also)
- [Examples](sensor_module.md#examples)
- [Return Values](sensor_module.md#return-values)

## [Synopsis](sensor_module.md#id1)

- Manage operations create and delete of the resource Sensor.
- Intent API to create a SENSOR test template with a new SSID, existing SSID, or both new and existing SSID.
- Intent API to delete an existing SENSOR test template.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](sensor_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](sensor_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **apCoverage**  list / elements=dictionary | Sensor’s apCoverage. |
| **bands**  string | Bands. |
| **numberOfApsToTest**  string | Number Of Aps To Test. |
| **rssiThreshold**  string | Rssi Threshold. |
| **connection**  string | Connection. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **modelVersion**  integer | Model Version. |
| **name**  string | Name. |
| **ssids**  list / elements=dictionary | Sensor’s ssids. |
| **authType**  string | Auth Type. |
| **categories**  list / elements=string | Categories. |
| **profileName**  string | Profile Name. |
| **psk**  string | Psk. |
| **qosPolicy**  string | Qos Policy. |
| **ssid**  string | Ssid. |
| **tests**  list / elements=dictionary | Sensor’s tests. |
| **config**  list / elements=dictionary | Config. |
| **name**  string | Name. |
| **thirdParty**  dictionary | Sensor’s thirdParty. |
| **selected**  boolean | Selected.  Choices:   - `false` - `true` |
| **templateName**  string | TemplateName query parameter. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](sensor_module.md#id4)

> **Note:**
>
> - SDK Method used are sensors.Sensors.create_sensor_test_template, sensors.Sensors.delete_sensor_test,
> - Paths used are post /dna/intent/api/v1/sensor, delete /dna/intent/api/v1/sensor,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](sensor_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Sensors CreateSensorTestTemplate](https://developer.cisco.com/docs/dna-center/#!create-sensor-test-template)
> :   Complete reference of the CreateSensorTestTemplate API.
>
> [Cisco DNA Center documentation for Sensors DeleteSensorTest](https://developer.cisco.com/docs/dna-center/#!delete-sensor-test)
> :   Complete reference of the DeleteSensorTest API.

## [Examples](sensor_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.sensor:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    apCoverage:
    - bands: string
      numberOfApsToTest: string
      rssiThreshold: string
    connection: string
    modelVersion: 0
    name: string
    ssids:
    - authType: string
      categories:
      - string
      profileName: string
      psk: string
      qosPolicy: string
      ssid: string
      tests:
      - config:
        - {}
        name: string
      thirdParty:
        selected: true

- name: Delete all
  cisco.dnac.sensor:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    templateName: string
```

## [Return Values](sensor_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"response": {"_id": "string", "apCoverage": [{"bands": "string", "numberOfApsToTest": 0, "rssiThreshold": 0}], "connection": "string", "encryptionMode": "string", "frequency": {}, "lastModifiedTime": 0, "legacyTestSuite": true, "location": {}, "locationInfoList": [{}], "modelVersion": 0, "name": "string", "numAssociatedSensor": 0, "numNeighborAPThreshold": 0, "radioAsSensorRemoved": true, "rssiThreshold": 0, "runNow": "string", "schedule": {}, "scheduleInDays": 0, "sensors": [{}], "showWlcUpgradeBanner": true, "siteHierarchy": {}, "ssids": [{"authProtocol": {}, "authType": "string", "authTypeRcvd": {}, "bands": {}, "certdownloadurl": {}, "certfilename": {}, "certpassphrase": {}, "certstatus": "string", "certxferprotocol": "string", "eapMethod": {}, "extWebAuth": true, "extWebAuthAccessUrl": {}, "extWebAuthHtmlTag": [{}], "extWebAuthPortal": {}, "extWebAuthVirtualIp": {}, "id": 0, "layer3webAuthEmailAddress": {}, "layer3webAuthpassword": {}, "layer3webAuthsecurity": {}, "layer3webAuthuserName": {}, "numAps": 0, "numSensors": 0, "password": {}, "profileName": "string", "psk": "string", "qosPolicy": "string", "scep": true, "ssid": "string", "status": "string", "tests": [{"config": [{}], "name": "string"}], "thirdParty": {"selected": true}, "username": {}, "validFrom": 0, "validTo": 0, "whiteList": true, "wlanId": 0, "wlc": {}}], "startTime": 0, "status": "string", "tenantId": {}, "testDurationEstimate": 0, "testScheduleMode": "string", "testTemplate": true, "tests": {}, "version": 0, "wlans": [{}]}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
