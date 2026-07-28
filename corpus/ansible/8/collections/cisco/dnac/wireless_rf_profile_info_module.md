---
collection: ansible
version: "8"
title: "cisco.dnac.wireless_rf_profile_info module – Information module for Wireless Rf Profile"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/wireless_rf_profile_info_module.html
fetched_at: 2026-07-28T01:25:54+00:00
---
# cisco.dnac.wireless_rf_profile_info module – Information module for Wireless Rf Profile

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
> see [Requirements](wireless_rf_profile_info_module.md#ansible-collections-cisco-dnac-wireless-rf-profile-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.wireless_rf_profile_info`.

New in cisco.dnac 3.1.0

- [Synopsis](wireless_rf_profile_info_module.md#synopsis)
- [Requirements](wireless_rf_profile_info_module.md#requirements)
- [Parameters](wireless_rf_profile_info_module.md#parameters)
- [Notes](wireless_rf_profile_info_module.md#notes)
- [See Also](wireless_rf_profile_info_module.md#see-also)
- [Examples](wireless_rf_profile_info_module.md#examples)
- [Return Values](wireless_rf_profile_info_module.md#return-values)

## [Synopsis](wireless_rf_profile_info_module.md#id1)

- Get all Wireless Rf Profile.
- Retrieve all RF profiles.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](wireless_rf_profile_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](wireless_rf_profile_info_module.md#id3)

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
| **rf_profile_name**  string | Rf-profile-name query parameter. RF Profile Name. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](wireless_rf_profile_info_module.md#id4)

> **Note:**
>
> - SDK Method used are wireless.Wireless.retrieve_rf_profiles,
> - Paths used are get /dna/intent/api/v1/wireless/rf-profile,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](wireless_rf_profile_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Wireless RetrieveRFProfiles](https://developer.cisco.com/docs/dna-center/#!retrieve-rf-profiles)
> :   Complete reference of the RetrieveRFProfiles API.

## [Examples](wireless_rf_profile_info_module.md#id6)

```yaml+jinja
- name: Get all Wireless Rf Profile
  cisco.dnac.wireless_rf_profile_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    rf_profile_name: string
  register: result
```

## [Return Values](wireless_rf_profile_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  list / elements=dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `"[\n  {\n    \"name\": \"string\",\n    \"parentProfileA\": \"string\",\n    \"parentProfileB\": \"string\",\n    \"enableARadioType\": true,\n    \"enableBRadioType\": true,\n    \"enableCRadioType\": true,\n    \"channelWidth\": \"string\",\n    \"aRadioChannels\": \"string\",\n    \"bRadioChannels\": \"string\",\n    \"cRadioChannels\": \"string\",\n    \"dataRatesA\": \"string\",\n    \"dataRatesB\": \"string\",\n    \"dataRatesC\": \"string\",\n    \"mandatoryDataRatesA\": \"string\",\n    \"mandatoryDataRatesB\": \"string\",\n    \"mandatoryDataRatesC\": \"string\",\n    \"enableCustom\": true,\n    \"minPowerLevelA\": \"string\",\n    \"minPowerLevelB\": \"string\",\n    \"minPowerLevelC\": \"string\",\n    \"maxPowerLevelA\": \"string\",\n    \"maxPowerLevelB\": \"string\",\n    \"powerThresholdV1A\": 0,\n    \"powerThresholdV1B\": 0,\n    \"powerThresholdV1C\": 0,\n    \"rxSopThresholdA\": \"string\",\n    \"rxSopThresholdB\": \"string\",\n    \"rxSopThresholdC\": \"string\",\n    \"defaultRfProfile\": true,\n    \"enableBrownField\": true\n  }\n]\n"` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
