---
collection: ansible
version: "8"
title: "cisco.dnac.wireless_accespoint_configuration module – Resource module for Wireless Accespoint Configuration"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/wireless_accespoint_configuration_module.html
fetched_at: 2026-07-28T01:25:42+00:00
---
# cisco.dnac.wireless_accespoint_configuration module – Resource module for Wireless Accespoint Configuration

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
> see [Requirements](wireless_accespoint_configuration_module.md#ansible-collections-cisco-dnac-wireless-accespoint-configuration-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.wireless_accespoint_configuration`.

New in cisco.dnac 6.7.0

- [Synopsis](wireless_accespoint_configuration_module.md#synopsis)
- [Requirements](wireless_accespoint_configuration_module.md#requirements)
- [Parameters](wireless_accespoint_configuration_module.md#parameters)
- [Notes](wireless_accespoint_configuration_module.md#notes)
- [See Also](wireless_accespoint_configuration_module.md#see-also)
- [Examples](wireless_accespoint_configuration_module.md#examples)
- [Return Values](wireless_accespoint_configuration_module.md#return-values)

## [Synopsis](wireless_accespoint_configuration_module.md#id1)

- Manage operation create of the resource Wireless Accespoint Configuration.
- User can configure multiple access points with required options using this intent API.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](wireless_accespoint_configuration_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](wireless_accespoint_configuration_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **adminStatus**  boolean | Configure the access point’s admin status. Set this parameter’s value to “true” to enable it and “false” to disable it.  **Choices:**   - `false` - `true` |
| **apHeight**  integer | Configure the height of the access point by setting a value between 3 and height of the floor. |
| **apList**  list / elements=dictionary | Wireless Accespoint Configuration’s apList. |
| **apName**  string | The current host name of the access point. |
| **apNameNew**  string | The modified hostname of the access point. |
| **macAddress**  string | The ethernet MAC address of the access point. |
| **apMode**  integer | Configure the access point’s mode for local/flexconnect mode, set “0”; for monitor mode, set “1”; for sniffer mode, set “4”; and for bridge/flex+bridge mode, set “5”. |
| **configureAdminStatus**  boolean | To change the access point’s admin status, set this parameter’s value to “true”.  **Choices:**   - `false` - `true` |
| **configureApHeight**  boolean | To change the access point’s height, set this parameter’s value to “true”.  **Choices:**   - `false` - `true` |
| **configureApMode**  boolean | To change the access point’s mode, set this parameter’s value to “true”.  **Choices:**   - `false` - `true` |
| **configureFailoverPriority**  boolean | To change the access point’s failover priority, set this parameter’s value to “true”.  **Choices:**   - `false` - `true` |
| **configureHAController**  boolean | To change the access point’s HA controller, set this parameter’s value to “true”.  **Choices:**   - `false` - `true` |
| **configureLedBrightnessLevel**  boolean | To change the access point’s LED brightness level, set this parameter’s value to “true”.  **Choices:**   - `false` - `true` |
| **configureLedStatus**  boolean | To change the access point’s LED status, set this parameter’s value to “true”.  **Choices:**   - `false` - `true` |
| **configureLocation**  boolean | To change the access point’s location, set this parameter’s value to “true”.  **Choices:**   - `false` - `true` |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **failoverPriority**  integer | Configure the acess point’s failover priority for low, set “1”; for medium, set “2”; for high, set “3”; and for critical, set “4”. |
| **ledBrightnessLevel**  integer | Configure the access point’s LED brightness level by setting a value between 1 and 8. |
| **ledStatus**  boolean | Configure the access point’s LED status. Set “true” to enable its status and “false” to disable it.  **Choices:**   - `false` - `true` |
| **location**  string | Configure the access point’s location. |
| **primaryControllerName**  string | Configure the hostname for an access point’s primary controller. |
| **primaryIpAddress**  dictionary | Wireless Accespoint Configuration’s primaryIpAddress. |
| **address**  string | Configure the IP address for an access point’s primary controller. |
| **radioConfigurations**  list / elements=dictionary | Wireless Accespoint Configuration’s radioConfigurations. |
| **adminStatus**  boolean | Configure the admin status on the specified radio for an access point. Set this parameter’s value to “true” to enable it and “false” to disable it.  **Choices:**   - `false` - `true` |
| **antennaCableName**  string | Configure the antenna cable name on the specified radio for an access point. If cable loss needs to be configured, set this parameter’s value to “other”. |
| **antennaDegree**  integer | Configure the antenna degree on the specified radio for an access point. |
| **antennaElevAngleDegree**  integer | Configure the antenna elevation angle on the specified radio for an access point. |
| **antennaElevAngleSign**  integer | Configure the antenna elevation angle direction on the specified radio for an access point for up, set “1”; for down, set “-1”. |
| **antennaGain**  integer | Configure the antenna gain on the specified radio for an access point by setting a decimal value (in dBi). |
| **antennaPatternName**  string | Configure the antenna pattern name on the specified radio for an access point. If antenna gain needs to be configured, set this parameter’s value to “other”. |
| **cableLoss**  integer | Configure the cable loss on the specified radio for an access point by setting a decimal value (in dBi). |
| **channelAssignmentMode**  integer | Configure the channel assignment mode on the specified radio for an access point for global mode, set “1”; and for custom mode, set “2”. |
| **channelNumber**  integer | Configure the channel number on the specified radio for an access point. |
| **channelWidth**  integer | Configure the channel width on the specified radio for an access point for 20 MHz, set “3”; for 40 MHz, set “4”; for 80 MHz, set “5”; and for 160 MHz, set “6”. |
| **cleanAirSI**  integer | Configure CleanAir or Spectrum Intelligence on the specified radio for an access point. Set this parameter’s value to “0” to disable the feature or “1” to enable it. |
| **configureAdminStatus**  boolean | To change the admin status on the specified radio for an access point, set this parameter’s value to “true”.  **Choices:**   - `false` - `true` |
| **configureAntennaCable**  boolean | To change the antenna cable name on the specified radio for an access point, set this parameter’s value to “true”.  **Choices:**   - `false` - `true` |
| **configureAntennaDegree**  boolean | To change the antenna degree on the specified radio for an access point, set this parameter’s value to “true”.  **Choices:**   - `false` - `true` |
| **configureAntennaPatternName**  boolean | To change the antenna pattern name on the specified radio for an access point, set the value for this parameter to “true”.  **Choices:**   - `false` - `true` |
| **configureChannel**  boolean | To change the channel on the specified radio for an access point, set this parameter’s value to “true”.  **Choices:**   - `false` - `true` |
| **configureChannelWidth**  boolean | To change the channel width on the specified radio for an access point, set this parameter’s value to “true”.  **Choices:**   - `false` - `true` |
| **configureCleanAirSI**  boolean | To enable or disable either CleanAir or Spectrum Intelligence on the specified radio for an access point, set this parameter’s value to “true”.  **Choices:**   - `false` - `true` |
| **configureElevAngleDegree**  boolean | To change the elevation angle degree on the specified radio for an access point, set this parameter’s value to “true”.  **Choices:**   - `false` - `true` |
| **configurePower**  boolean | To change the power assignment mode on the specified radio for an access point, set this parameter’s value to “true”.  **Choices:**   - `false` - `true` |
| **configureRadioRoleAssignment**  boolean | To change the radio role on the specified radio for an access point, set this parameter’s value to “true”.  **Choices:**   - `false` - `true` |
| **powerAssignmentMode**  integer | Configure the power assignment mode on the specified radio for an access point for global mode, set “1”; and for custom mode, set “2”. |
| **powerlevel**  integer | Configure the power level on the specified radio for an access point by setting a value between 1 and 8. |
| **radioBand**  string | Configure the band on the specified radio for an access point for 2.4 GHz, set “RADIO24”; for 5 GHz, set “RADIO5”. |
| **radioRoleAssignment**  string | Configure one of the following roles on the specified radio for an access point “auto”, “serving”, or “monitor”. |
| **radioType**  integer | Configure an access point’s radio band for 2.4 GHz, set “1”; for 5 GHz, set “2”; for XOR, set “3”; and for 6 GHz, set “6”. |
| **secondaryControllerName**  string | Configure the hostname for an access point’s secondary controller. |
| **secondaryIpAddress**  dictionary | Wireless Accespoint Configuration’s secondaryIpAddress. |
| **address**  string | Configure the IP address for an access point’s secondary controller. |
| **tertiaryControllerName**  string | Configure the hostname for an access point’s tertiary controller. |
| **tertiaryIpAddress**  dictionary | Wireless Accespoint Configuration’s tertiaryIpAddress. |
| **address**  string | Configure the IP address for an access point’s tertiary controller. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](wireless_accespoint_configuration_module.md#id4)

> **Note:**
>
> - SDK Method used are wireless.Wireless.configure_access_points,
> - Paths used are post /dna/intent/api/v1/wireless/accesspoint-configuration,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](wireless_accespoint_configuration_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Wireless ConfigureAccessPoints](https://developer.cisco.com/docs/dna-center/#!configure-access-points)
> :   Complete reference of the ConfigureAccessPoints API.

## [Examples](wireless_accespoint_configuration_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.wireless_accespoint_configuration:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    adminStatus: true
    apHeight: 0
    apList:
    - apName: string
      apNameNew: string
      macAddress: string
    apMode: 0
    configureAdminStatus: true
    configureApHeight: true
    configureApMode: true
    configureFailoverPriority: true
    configureHAController: true
    configureLedBrightnessLevel: true
    configureLedStatus: true
    configureLocation: true
    failoverPriority: 0
    ledBrightnessLevel: 0
    ledStatus: true
    location: string
    primaryControllerName: string
    primaryIpAddress:
      address: string
    radioConfigurations:
    - adminStatus: true
      antennaCableName: string
      antennaDegree: 0
      antennaElevAngleDegree: 0
      antennaElevAngleSign: 0
      antennaGain: 0
      antennaPatternName: string
      cableLoss: 0
      channelAssignmentMode: 0
      channelNumber: 0
      channelWidth: 0
      cleanAirSI: 0
      configureAdminStatus: true
      configureAntennaCable: true
      configureAntennaDegree: true
      configureAntennaPatternName: true
      configureChannel: true
      configureChannelWidth: true
      configureCleanAirSI: true
      configureElevAngleDegree: true
      configurePower: true
      configureRadioRoleAssignment: true
      powerAssignmentMode: 0
      powerlevel: 0
      radioBand: string
      radioRoleAssignment: string
      radioType: 0
    secondaryControllerName: string
    secondaryIpAddress:
      address: string
    tertiaryControllerName: string
    tertiaryIpAddress:
      address: string
```

## [Return Values](wireless_accespoint_configuration_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": {"taskId": "string", "url": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
