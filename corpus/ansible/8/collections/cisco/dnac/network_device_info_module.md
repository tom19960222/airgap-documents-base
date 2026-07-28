---
collection: ansible
version: "8"
title: "cisco.dnac.network_device_info module – Information module for Network Device"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/network_device_info_module.html
fetched_at: 2026-07-28T01:23:26+00:00
---
# cisco.dnac.network_device_info module – Information module for Network Device

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
> see [Requirements](network_device_info_module.md#ansible-collections-cisco-dnac-network-device-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.network_device_info`.

New in cisco.dnac 3.1.0

- [Synopsis](network_device_info_module.md#synopsis)
- [Requirements](network_device_info_module.md#requirements)
- [Parameters](network_device_info_module.md#parameters)
- [Notes](network_device_info_module.md#notes)
- [See Also](network_device_info_module.md#see-also)
- [Examples](network_device_info_module.md#examples)
- [Return Values](network_device_info_module.md#return-values)

## [Synopsis](network_device_info_module.md#id1)

- Get all Network Device.
- Get Network Device by id.
- Returns list of network devices based on filter criteria such as management IP address, mac address, hostname, etc.
- Returns the network device details for the given device ID.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](network_device_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](network_device_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **associatedWlcIp**  list / elements=string | AssociatedWlcIp query parameter. |
| **collectionInterval**  list / elements=string | CollectionInterval query parameter. |
| **collectionStatus**  list / elements=string | CollectionStatus query parameter. |
| **deviceSupportLevel**  string | DeviceSupportLevel query parameter. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **errorCode**  list / elements=string | ErrorCode query parameter. |
| **errorDescription**  list / elements=string | ErrorDescription query parameter. |
| **family**  list / elements=string | Family query parameter. |
| **headers**  dictionary | Additional headers. |
| **hostname**  list / elements=string | Hostname query parameter. |
| **id**  string | Id query parameter. Accepts comma separated ids and return list of network-devices for the given ids. If invalid or not-found ids are provided, null entry will be returned in the list. |
| **license_name**  list / elements=string | License.name query parameter. |
| **license_status**  list / elements=string | License.status query parameter. |
| **license_type**  list / elements=string | License.type query parameter. |
| **limit**  integer | Limit query parameter. 1 <= limit <= 500 max. No. Of devices to be returned in the result. |
| **location**  list / elements=string | Location query parameter. |
| **locationName**  list / elements=string | LocationName query parameter. |
| **macAddress**  list / elements=string | MacAddress query parameter. |
| **managementIpAddress**  list / elements=string | ManagementIpAddress query parameter. |
| **module_equpimenttype**  list / elements=string | Module+equpimenttype query parameter. |
| **module_name**  list / elements=string | Module+name query parameter. |
| **module_operationstatecode**  list / elements=string | Module+operationstatecode query parameter. |
| **module_partnumber**  list / elements=string | Module+partnumber query parameter. |
| **module_servicestate**  list / elements=string | Module+servicestate query parameter. |
| **module_vendorequipmenttype**  list / elements=string | Module+vendorequipmenttype query parameter. |
| **notSyncedForMinutes**  list / elements=string | NotSyncedForMinutes query parameter. |
| **offset**  integer | Offset query parameter. Offset >= 1 X gives results from Xth device onwards. |
| **platformId**  list / elements=string | PlatformId query parameter. |
| **reachabilityStatus**  list / elements=string | ReachabilityStatus query parameter. |
| **role**  list / elements=string | Role query parameter. |
| **serialNumber**  list / elements=string | SerialNumber query parameter. |
| **series**  list / elements=string | Series query parameter. |
| **softwareType**  list / elements=string | SoftwareType query parameter. |
| **softwareVersion**  list / elements=string | SoftwareVersion query parameter. |
| **type**  list / elements=string | Type query parameter. |
| **upTime**  list / elements=string | UpTime query parameter. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](network_device_info_module.md#id4)

> **Note:**
>
> - SDK Method used are devices.Devices.get_device_by_id, devices.Devices.get_device_list,
> - Paths used are get /dna/intent/api/v1/network-device, get /dna/intent/api/v1/network-device/{id},
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](network_device_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Devices GetDeviceByID](https://developer.cisco.com/docs/dna-center/#!get-device-by-id)
> :   Complete reference of the GetDeviceByID API.
>
> [Cisco DNA Center documentation for Devices GetDeviceList](https://developer.cisco.com/docs/dna-center/#!get-device-list)
> :   Complete reference of the GetDeviceList API.

## [Examples](network_device_info_module.md#id6)

```yaml+jinja
- name: Get all Network Device
  cisco.dnac.network_device_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    hostname: []
    managementIpAddress: []
    macAddress: []
    locationName: []
    serialNumber: []
    location: []
    family: []
    type: []
    series: []
    collectionStatus: []
    collectionInterval: []
    notSyncedForMinutes: []
    errorCode: []
    errorDescription: []
    softwareVersion: []
    softwareType: []
    platformId: []
    role: []
    reachabilityStatus: []
    upTime: []
    associatedWlcIp: []
    license_name: []
    license_type: []
    license_status: []
    module_name: []
    module_equpimenttype: []
    module_servicestate: []
    module_vendorequipmenttype: []
    module_partnumber: []
    module_operationstatecode: []
    id: string
    deviceSupportLevel: string
    offset: 0
    limit: 0
  register: result

- name: Get Network Device by id
  cisco.dnac.network_device_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result
```

## [Return Values](network_device_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": {"apManagerInterfaceIp": "string", "associatedWlcIp": "string", "bootDateTime": "string", "collectionInterval": "string", "collectionStatus": "string", "errorCode": "string", "errorDescription": "string", "family": "string", "hostname": "string", "id": "string", "instanceTenantId": "string", "instanceUuid": "string", "interfaceCount": "string", "inventoryStatusDetail": "string", "lastUpdateTime": 0, "lastUpdated": "string", "lineCardCount": "string", "lineCardId": "string", "location": "string", "locationName": "string", "macAddress": "string", "managementIpAddress": "string", "memorySize": "string", "platformId": "string", "reachabilityFailureReason": "string", "reachabilityStatus": "string", "role": "string", "roleSource": "string", "serialNumber": "string", "series": "string", "snmpContact": "string", "snmpLocation": "string", "softwareType": "string", "softwareVersion": "string", "tagCount": "string", "tunnelUdpPort": "string", "type": "string", "upTime": "string", "waasDeviceMode": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
