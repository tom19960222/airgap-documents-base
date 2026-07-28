---
collection: ansible
version: "8"
title: "cisco.dnac.network_device_with_snmp_v3_des_info module – Information module for Network Device With Snmp V3 Des"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/network_device_with_snmp_v3_des_info_module.html
fetched_at: 2026-07-28T01:23:42+00:00
---
# cisco.dnac.network_device_with_snmp_v3_des_info module – Information module for Network Device With Snmp V3 Des

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
> see [Requirements](network_device_with_snmp_v3_des_info_module.md#ansible-collections-cisco-dnac-network-device-with-snmp-v3-des-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.network_device_with_snmp_v3_des_info`.

New in cisco.dnac 3.1.0

- [Synopsis](network_device_with_snmp_v3_des_info_module.md#synopsis)
- [Requirements](network_device_with_snmp_v3_des_info_module.md#requirements)
- [Parameters](network_device_with_snmp_v3_des_info_module.md#parameters)
- [Notes](network_device_with_snmp_v3_des_info_module.md#notes)
- [See Also](network_device_with_snmp_v3_des_info_module.md#see-also)
- [Examples](network_device_with_snmp_v3_des_info_module.md#examples)
- [Return Values](network_device_with_snmp_v3_des_info_module.md#return-values)

## [Synopsis](network_device_with_snmp_v3_des_info_module.md#id1)

- Get all Network Device With Snmp V3 Des.
- Returns devices added to Cisco DNA center with snmp v3 DES, where siteId is mandatory & accepts offset, limit, sortby, order which are optional.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](network_device_with_snmp_v3_des_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](network_device_with_snmp_v3_des_info_module.md#id3)

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
| **limit**  integer | Limit query parameter. Default value is 500. |
| **offset**  integer | Offset query parameter. Row Number. Default value is 1. |
| **order**  string | Order query parameter. |
| **siteId**  string | SiteId path parameter. |
| **sortBy**  string | SortBy query parameter. Sort By. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](network_device_with_snmp_v3_des_info_module.md#id4)

> **Note:**
>
> - SDK Method used are devices.Devices.get_devices_with_snmpv3_des,
> - Paths used are get /dna/intent/api/v1/network-device/insight/{siteId}/insecure-connection,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](network_device_with_snmp_v3_des_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Devices ReturnsDevicesAddedToCiscoDNACenterWithSnmpV3DES](https://developer.cisco.com/docs/dna-center/#!returns-devices-added-to-cisco-dna-center-with-snmp-v-3-des)
> :   Complete reference of the ReturnsDevicesAddedToCiscoDNACenterWithSnmpV3DES API.

## [Examples](network_device_with_snmp_v3_des_info_module.md#id6)

```yaml+jinja
- name: Get all Network Device With Snmp V3 Des
  cisco.dnac.network_device_with_snmp_v3_des_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    offset: 0
    limit: 0
    sortBy: string
    order: string
    siteId: string
  register: result
```

## [Return Values](network_device_with_snmp_v3_des_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": [{"family": "string", "hostname": "string", "id": "string", "lastUpdated": "string", "managementIpAddress": "string", "reachabilityStatus": "string", "type": "string", "upTime": "string"}], "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
