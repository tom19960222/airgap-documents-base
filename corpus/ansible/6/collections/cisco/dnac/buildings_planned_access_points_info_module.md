---
collection: ansible
version: "6"
title: "cisco.dnac.buildings_planned_access_points_info module – Information module for Buildings Planned Access Points"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/buildings_planned_access_points_info_module.html
fetched_at: 2026-07-27T16:51:02+00:00
---
# cisco.dnac.buildings_planned_access_points_info module – Information module for Buildings Planned Access Points

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
> see [Requirements](buildings_planned_access_points_info_module.md#ansible-collections-cisco-dnac-buildings-planned-access-points-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.buildings_planned_access_points_info`.

New in cisco.dnac 6.0.0

- [Synopsis](buildings_planned_access_points_info_module.md#synopsis)
- [Requirements](buildings_planned_access_points_info_module.md#requirements)
- [Parameters](buildings_planned_access_points_info_module.md#parameters)
- [Notes](buildings_planned_access_points_info_module.md#notes)
- [See Also](buildings_planned_access_points_info_module.md#see-also)
- [Examples](buildings_planned_access_points_info_module.md#examples)
- [Return Values](buildings_planned_access_points_info_module.md#return-values)

## [Synopsis](buildings_planned_access_points_info_module.md#id1)

- Get all Buildings Planned Access Points.
- Provides a list of Planned Access Points for the Building it is requested for.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](buildings_planned_access_points_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](buildings_planned_access_points_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **buildingId**  string | BuildingId path parameter. Building Id. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **headers**  dictionary | Additional headers. |
| **limit**  integer | Limit query parameter. |
| **offset**  integer | Offset query parameter. |
| **radios**  boolean | Radios query parameter. Inlcude planned radio details.  Choices:   - `false` - `true` |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](buildings_planned_access_points_info_module.md#id4)

> **Note:**
>
> - SDK Method used are devices.Devices.get_planned_access_points_for_building,
> - Paths used are get /dna/intent/api/v1/buildings/{buildingId}/planned-access-points,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](buildings_planned_access_points_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Devices GetPlannedAccessPointsForBuilding](https://developer.cisco.com/docs/dna-center/#!get-planned-access-points-for-building)
> :   Complete reference of the GetPlannedAccessPointsForBuilding API.

## [Examples](buildings_planned_access_points_info_module.md#id6)

```yaml+jinja
- name: Get all Buildings Planned Access Points
  cisco.dnac.buildings_planned_access_points_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    limit: 0
    offset: 0
    radios: True
    buildingId: string
  register: result
```

## [Return Values](buildings_planned_access_points_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"response": [{"attributes": {"createDate": 0, "domain": "string", "heirarchyName": "string", "id": 0, "instanceUuid": "string", "macaddress": {}, "name": "string", "source": "string", "typeString": "string"}, "isSensor": true, "location": {}, "position": {"x": 0, "y": 0, "z": 0}, "radioCount": 0, "radios": [{"antenna": {"azimuthAngle": 0, "elevationAngle": 0, "gain": 0, "mode": "string", "name": "string", "type": "string"}, "attributes": {"channel": {}, "channelString": {}, "id": 0, "ifMode": "string", "ifTypeString": "string", "ifTypeSubband": "string", "instanceUuid": "string", "slotId": 0}, "isSensor": true}]}], "total": 0, "version": 0}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
