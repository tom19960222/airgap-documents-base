---
collection: ansible
version: "8"
title: "cisco.dnac.sda_fabric_border_device_info module – Information module for Sda Fabric Border Device"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/sda_fabric_border_device_info_module.html
fetched_at: 2026-07-28T01:24:30+00:00
---
# cisco.dnac.sda_fabric_border_device_info module – Information module for Sda Fabric Border Device

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
> see [Requirements](sda_fabric_border_device_info_module.md#ansible-collections-cisco-dnac-sda-fabric-border-device-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.sda_fabric_border_device_info`.

New in cisco.dnac 3.1.0

- [Synopsis](sda_fabric_border_device_info_module.md#synopsis)
- [Requirements](sda_fabric_border_device_info_module.md#requirements)
- [Parameters](sda_fabric_border_device_info_module.md#parameters)
- [Notes](sda_fabric_border_device_info_module.md#notes)
- [See Also](sda_fabric_border_device_info_module.md#see-also)
- [Examples](sda_fabric_border_device_info_module.md#examples)
- [Return Values](sda_fabric_border_device_info_module.md#return-values)

## [Synopsis](sda_fabric_border_device_info_module.md#id1)

- Get all Sda Fabric Border Device.
- Get border device detail from SDA Fabric.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](sda_fabric_border_device_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](sda_fabric_border_device_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **deviceManagementIpAddress**  string  *added in cisco.dnac 4.0.0* | DeviceManagementIpAddress query parameter. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **headers**  dictionary | Additional headers. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](sda_fabric_border_device_info_module.md#id4)

> **Note:**
>
> - SDK Method used are sda.Sda.gets_border_device_detail,
> - Paths used are get /dna/intent/api/v1/business/sda/border-device,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](sda_fabric_border_device_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for SDA GetBorderDeviceDetailFromSDAFabric](https://developer.cisco.com/docs/dna-center/#!get-border-device-detail-from-sda-fabric)
> :   Complete reference of the GetBorderDeviceDetailFromSDAFabric API.

## [Examples](sda_fabric_border_device_info_module.md#id6)

```yaml+jinja
- name: Get all Sda Fabric Border Device
  cisco.dnac.sda_fabric_border_device_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    deviceManagementIpAddress: string
  register: result
```

## [Return Values](sda_fabric_border_device_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"description": "string", "payload": {"akcSettingsCfs": [{}], "authEntityClass": 0, "authEntityId": 0, "cfsChangeInfo": [{}], "configs": [{}], "createTime": 0, "customProvisions": [{}], "deployPending": "string", "deployed": true, "deviceInterfaceInfo": [{}], "deviceSettings": {"connectedTo": [{}], "cpu": 0, "deployPending": "string", "dhcpEnabled": true, "displayName": "string", "extConnectivitySettings": [{"deployPending": "string", "displayName": "string", "externalDomainProtocolNumber": "string", "id": "string", "instanceId": 0, "instanceTenantId": "string", "instanceVersion": 0, "interfaceUuid": "string", "l2Handoff": [{}], "l3Handoff": [{"deployPending": "string", "displayName": "string", "id": "string", "instanceId": 0, "instanceTenantId": "string", "instanceVersion": 0, "localIpAddress": "string", "remoteIpAddress": "string", "virtualNetwork": {"idRef": "string"}, "vlanId": 0}], "policyPropagationEnabled": true, "policySgtTag": 0}], "externalConnectivityIpPool": "string", "externalDomainRoutingProtocol": "string", "id": "string", "instanceId": 0, "instanceTenantId": "string", "instanceVersion": 0, "internalDomainProtocolNumber": "string", "memory": 0, "nodeType": ["string"], "storage": 0}, "displayName": "string", "id": "string", "instanceId": 0, "instanceTenantId": "string", "instanceVersion": 0, "isSeeded": true, "isStale": true, "lastUpdateTime": 0, "managedSites": [{}], "name": "string", "namespace": "string", "networkDeviceId": "string", "networkWideSettings": {"aaa": [{}], "cmx": [{}], "deployPending": "string", "dhcp": [{"id": "string", "ipAddress": {"address": "string", "addressType": "string", "id": "string", "paddedAddress": "string"}}], "displayName": "string", "dns": [{"domainName": "string", "id": "string", "ip": {"address": "string", "addressType": "string", "id": "string", "paddedAddress": "string"}}], "id": "string", "instanceId": 0, "instanceTenantId": "string", "instanceVersion": 0, "ldap": [{}], "nativeVlan": [{}], "netflow": [{}], "ntp": [{}], "snmp": [{}], "syslogs": [{}]}, "otherDevice": [{}], "provisioningState": "string", "resourceVersion": 0, "roles": ["string"], "saveWanConnectivityDetailsOnly": true, "siteId": "string", "targetIdList": [{}], "transitNetworks": [{"idRef": "string"}], "type": "string", "virtualNetwork": [{}], "wlan": [{}]}, "status": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
