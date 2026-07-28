---
collection: ansible
version: "8"
title: "cisco.dnac.wireless_rf_profile module – Resource module for Wireless Rf Profile"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/wireless_rf_profile_module.html
fetched_at: 2026-07-28T01:25:53+00:00
---
# cisco.dnac.wireless_rf_profile module – Resource module for Wireless Rf Profile

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
> see [Requirements](wireless_rf_profile_module.md#ansible-collections-cisco-dnac-wireless-rf-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.wireless_rf_profile`.

New in cisco.dnac 3.1.0

- [Synopsis](wireless_rf_profile_module.md#synopsis)
- [Requirements](wireless_rf_profile_module.md#requirements)
- [Parameters](wireless_rf_profile_module.md#parameters)
- [Notes](wireless_rf_profile_module.md#notes)
- [See Also](wireless_rf_profile_module.md#see-also)
- [Examples](wireless_rf_profile_module.md#examples)
- [Return Values](wireless_rf_profile_module.md#return-values)

## [Synopsis](wireless_rf_profile_module.md#id1)

- Manage operations create and delete of the resource Wireless Rf Profile.
- Create or Update RF profile.
- Delete RF profiles.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](wireless_rf_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](wireless_rf_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **channelWidth**  string | Channel Width. |
| **defaultRfProfile**  boolean | Is Default Rf Profile.  **Choices:**   - `false` - `true` |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **enableBrownField**  boolean | Enable Brown Field.  **Choices:**   - `false` - `true` |
| **enableCustom**  boolean | Enable Custom.  **Choices:**   - `false` - `true` |
| **enableRadioTypeA**  boolean | Enable Radio Type A.  **Choices:**   - `false` - `true` |
| **enableRadioTypeB**  boolean | Enable Radio Type B.  **Choices:**   - `false` - `true` |
| **enableRadioTypeC**  boolean | Enable Radio Type C (6GHz).  **Choices:**   - `false` - `true` |
| **name**  string | RF Profile Name. |
| **radioTypeAProperties**  dictionary | Wireless Rf Profile’s radioTypeAProperties. |
| **dataRates**  string | Data Rates. |
| **mandatoryDataRates**  string | Mandatory Data Rates. |
| **maxPowerLevel**  integer | Max Power Level. |
| **minPowerLevel**  integer | Rx Sop Threshold. |
| **parentProfile**  string | Parent Profile. |
| **powerThresholdV1**  integer | Power Threshold V1. |
| **radioChannels**  string | Radio Channels. |
| **rxSopThreshold**  string | Rx Sop Threshold. |
| **radioTypeBProperties**  dictionary | Wireless Rf Profile’s radioTypeBProperties. |
| **dataRates**  string | Data Rates. |
| **mandatoryDataRates**  string | Mandatory Data Rates. |
| **maxPowerLevel**  integer | Max Power Level. |
| **minPowerLevel**  integer | Min Power Level. |
| **parentProfile**  string | Parent Profile. |
| **powerThresholdV1**  integer | Power Threshold V1. |
| **radioChannels**  string | Radio Channels. |
| **rxSopThreshold**  string | Rx Sop Threshold. |
| **radioTypeCProperties**  dictionary | Wireless Rf Profile’s radioTypeCProperties. |
| **dataRates**  string | Data Rates. |
| **mandatoryDataRates**  string | Mandatory Data Rates. |
| **maxPowerLevel**  integer | Max Power Level. |
| **minPowerLevel**  integer | Min Power Level. |
| **parentProfile**  string | Parent Profile. |
| **powerThresholdV1**  integer | Power Threshold V1. |
| **radioChannels**  string | Radio Channels. |
| **rxSopThreshold**  string | Rx Sop Threshold. |
| **rfProfileName**  string | RfProfileName path parameter. RF profile name to be deleted(required) \*non-custom RF profile cannot be deleted. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](wireless_rf_profile_module.md#id4)

> **Note:**
>
> - SDK Method used are wireless.Wireless.create_or_update_rf_profile, wireless.Wireless.delete_rf_profiles,
> - Paths used are post /dna/intent/api/v1/wireless/rf-profile, delete /dna/intent/api/v1/wireless/rf-profile/{rfProfileName},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](wireless_rf_profile_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Wireless CreateOrUpdateRFProfile](https://developer.cisco.com/docs/dna-center/#!create-or-update-rf-profile)
> :   Complete reference of the CreateOrUpdateRFProfile API.
>
> [Cisco DNA Center documentation for Wireless DeleteRFProfiles](https://developer.cisco.com/docs/dna-center/#!delete-rf-profiles)
> :   Complete reference of the DeleteRFProfiles API.

## [Examples](wireless_rf_profile_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.wireless_rf_profile:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    channelWidth: string
    defaultRfProfile: true
    enableBrownField: true
    enableCustom: true
    enableRadioTypeA: true
    enableRadioTypeB: true
    enableRadioTypeC: true
    name: string
    radioTypeAProperties:
      dataRates: string
      mandatoryDataRates: string
      maxPowerLevel: 0
      minPowerLevel: 0
      parentProfile: string
      powerThresholdV1: 0
      radioChannels: string
      rxSopThreshold: string
    radioTypeBProperties:
      dataRates: string
      mandatoryDataRates: string
      maxPowerLevel: 0
      minPowerLevel: 0
      parentProfile: string
      powerThresholdV1: 0
      radioChannels: string
      rxSopThreshold: string
    radioTypeCProperties:
      dataRates: string
      mandatoryDataRates: string
      maxPowerLevel: 0
      minPowerLevel: 0
      parentProfile: string
      powerThresholdV1: 0
      radioChannels: string
      rxSopThreshold: string

- name: Delete by name
  cisco.dnac.wireless_rf_profile:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    rfProfileName: string
```

## [Return Values](wireless_rf_profile_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"executionId": "string", "executionUrl": "string", "message": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
