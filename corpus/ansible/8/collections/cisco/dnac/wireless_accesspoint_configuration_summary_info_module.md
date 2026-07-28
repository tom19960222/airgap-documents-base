---
collection: ansible
version: "8"
title: "cisco.dnac.wireless_accesspoint_configuration_summary_info module – Information module for Wireless Accesspoint Configuration Summary"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/wireless_accesspoint_configuration_summary_info_module.html
fetched_at: 2026-07-28T01:25:43+00:00
---
# cisco.dnac.wireless_accesspoint_configuration_summary_info module – Information module for Wireless Accesspoint Configuration Summary

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
> see [Requirements](wireless_accesspoint_configuration_summary_info_module.md#ansible-collections-cisco-dnac-wireless-accesspoint-configuration-summary-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.wireless_accesspoint_configuration_summary_info`.

New in cisco.dnac 6.7.0

- [Synopsis](wireless_accesspoint_configuration_summary_info_module.md#synopsis)
- [Requirements](wireless_accesspoint_configuration_summary_info_module.md#requirements)
- [Parameters](wireless_accesspoint_configuration_summary_info_module.md#parameters)
- [Notes](wireless_accesspoint_configuration_summary_info_module.md#notes)
- [See Also](wireless_accesspoint_configuration_summary_info_module.md#see-also)
- [Examples](wireless_accesspoint_configuration_summary_info_module.md#examples)
- [Return Values](wireless_accesspoint_configuration_summary_info_module.md#return-values)

## [Synopsis](wireless_accesspoint_configuration_summary_info_module.md#id1)

- Get all Wireless Accesspoint Configuration Summary.
- Users can query the access point configuration information per device using the ethernet MAC address.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](wireless_accesspoint_configuration_summary_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](wireless_accesspoint_configuration_summary_info_module.md#id3)

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
| **key**  string | Key query parameter. The ethernet MAC address of Access point. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](wireless_accesspoint_configuration_summary_info_module.md#id4)

> **Note:**
>
> - SDK Method used are wireless.Wireless.get_access_point_configuration,
> - Paths used are get /dna/intent/api/v1/wireless/accesspoint-configuration/summary,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](wireless_accesspoint_configuration_summary_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Wireless GetAccessPointConfiguration](https://developer.cisco.com/docs/dna-center/#!get-access-point-configuration)
> :   Complete reference of the GetAccessPointConfiguration API.

## [Examples](wireless_accesspoint_configuration_summary_info_module.md#id6)

```yaml+jinja
- name: Get all Wireless Accesspoint Configuration Summary
  cisco.dnac.wireless_accesspoint_configuration_summary_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    key: string
  register: result
```

## [Return Values](wireless_accesspoint_configuration_summary_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"_creationOrderIndex": 0, "_isBeingChanged": true, "_orderedListOEAssocName": {}, "_orderedListOEIndex": 0, "adminStatus": "string", "apHeight": 0, "apMode": "string", "apName": "string", "authEntityClass": {}, "authEntityId": {}, "changeLogList": {}, "deployPending": "string", "displayName": "string", "ethMac": "string", "failoverPriority": "string", "instanceCreatedOn": {}, "instanceId": 0, "instanceOrigin": {}, "instanceTenantId": "string", "instanceUpdatedOn": {}, "instanceUuid": {}, "instanceVersion": 0, "internalKey": {"id": 0, "longType": "string", "type": "string", "url": "string"}, "lazyLoadedEntities": {}, "ledBrightnessLevel": 0, "ledStatus": "string", "location": "string", "macAddress": "string", "meshDTOs": [{}], "primaryControllerName": "string", "primaryIpAddress": "string", "radioDTOs": [{"_creationOrderIndex": 0, "_isBeingChanged": true, "_orderedListOEAssocName": {}, "_orderedListOEIndex": 0, "adminStatus": "string", "antennaAngle": 0, "antennaElevAngle": 0, "antennaGain": 0, "antennaPatternName": "string", "authEntityClass": {}, "authEntityId": {}, "changeLogList": {}, "channelAssignmentMode": "string", "channelNumber": 0, "channelWidth": "string", "cleanAirSI": "string", "deployPending": "string", "displayName": "string", "ifType": 0, "ifTypeValue": "string", "instanceCreatedOn": {}, "instanceId": 0, "instanceOrigin": {}, "instanceTenantId": "string", "instanceUpdatedOn": {}, "instanceUuid": {}, "instanceVersion": 0, "internalKey": {"id": 0, "longType": "string", "type": "string", "url": "string"}, "lazyLoadedEntities": {}, "macAddress": "string", "powerAssignmentMode": "string", "powerlevel": 0, "radioBand": {}, "radioRoleAssignment": {}, "slotId": 0}], "secondaryControllerName": "string", "secondaryIpAddress": "string", "tertiaryControllerName": "string", "tertiaryIpAddress": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
