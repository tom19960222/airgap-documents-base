---
collection: ansible
version: "6"
title: "cisco.dnac.network_device module – Resource module for Network Device"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/network_device_module.html
fetched_at: 2026-07-27T16:52:37+00:00
---
# cisco.dnac.network_device module – Resource module for Network Device

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
> see [Requirements](network_device_module.md#ansible-collections-cisco-dnac-network-device-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.network_device`.

New in cisco.dnac 3.1.0

- [Synopsis](network_device_module.md#synopsis)
- [Requirements](network_device_module.md#requirements)
- [Parameters](network_device_module.md#parameters)
- [Notes](network_device_module.md#notes)
- [See Also](network_device_module.md#see-also)
- [Examples](network_device_module.md#examples)
- [Return Values](network_device_module.md#return-values)

## [Synopsis](network_device_module.md#id1)

- Manage operations create, update and delete of the resource Network Device.
- Adds the device with given credential.
- Deletes the network device for the given Id.
- Sync the devices provided as input.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](network_device_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](network_device_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cleanConfig**  boolean  added in cisco.dnac 4.0.0 | CleanConfig query parameter.  Choices:   - `false` - `true` |
| **cliTransport**  string | Network Device’s cliTransport. |
| **computeDevice**  boolean | ComputeDevice flag.  Choices:   - `false` - `true` |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **enablePassword**  string | Network Device’s enablePassword. |
| **extendedDiscoveryInfo**  string | Network Device’s extendedDiscoveryInfo. |
| **httpPassword**  string | Network Device’s httpPassword. |
| **httpPort**  string | Network Device’s httpPort. |
| **httpSecure**  boolean | HttpSecure flag.  Choices:   - `false` - `true` |
| **httpUserName**  string | Network Device’s httpUserName. |
| **id**  string | Id path parameter. Device ID. |
| **ipAddress**  list / elements=string | Network Device’s ipAddress. |
| **merakiOrgId**  list / elements=string | Network Device’s merakiOrgId. |
| **netconfPort**  string | Network Device’s netconfPort. |
| **password**  string | Network Device’s password. |
| **serialNumber**  string | Network Device’s serialNumber. |
| **snmpAuthPassphrase**  string | Network Device’s snmpAuthPassphrase. |
| **snmpAuthProtocol**  string | Network Device’s snmpAuthProtocol. |
| **snmpMode**  string | Network Device’s snmpMode. |
| **snmpPrivPassphrase**  string | Network Device’s snmpPrivPassphrase. |
| **snmpPrivProtocol**  string | Network Device’s snmpPrivProtocol. |
| **snmpRetry**  integer | Network Device’s snmpRetry. |
| **snmpROCommunity**  string | Network Device’s snmpROCommunity. |
| **snmpRWCommunity**  string | Network Device’s snmpRWCommunity. |
| **snmpTimeout**  integer | Network Device’s snmpTimeout. |
| **snmpUserName**  string | Network Device’s snmpUserName. |
| **snmpVersion**  string | Network Device’s snmpVersion. |
| **type**  string | Network Device’s type. |
| **updateMgmtIPaddressList**  list / elements=dictionary | Network Device’s updateMgmtIPaddressList. |
| **existMgmtIpAddress**  string | Network Device’s existMgmtIpAddress. |
| **newMgmtIpAddress**  string | Network Device’s newMgmtIpAddress. |
| **userName**  string | Network Device’s userName. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](network_device_module.md#id4)

> **Note:**
>
> - SDK Method used are devices.Devices.add_device, devices.Devices.delete_device_by_id, devices.Devices.sync_devices,
> - Paths used are post /dna/intent/api/v1/network-device, delete /dna/intent/api/v1/network-device/{id}, put /dna/intent/api/v1/network-device,
> - Removed ‘managementIpAddress’ options in v4.3.0.
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](network_device_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Devices AddDevice2](https://developer.cisco.com/docs/dna-center/#!add-device)
> :   Complete reference of the AddDevice2 API.
>
> [Cisco DNA Center documentation for Devices DeleteDeviceById](https://developer.cisco.com/docs/dna-center/#!delete-device-by-id)
> :   Complete reference of the DeleteDeviceById API.
>
> [Cisco DNA Center documentation for Devices SyncDevices2](https://developer.cisco.com/docs/dna-center/#!sync-devices)
> :   Complete reference of the SyncDevices2 API.

## [Examples](network_device_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.network_device:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    cliTransport: string
    computeDevice: true
    enablePassword: string
    extendedDiscoveryInfo: string
    httpPassword: string
    httpPort: string
    httpSecure: true
    httpUserName: string
    ipAddress:
    - string
    merakiOrgId:
    - string
    netconfPort: string
    password: string
    serialNumber: string
    snmpAuthPassphrase: string
    snmpAuthProtocol: string
    snmpMode: string
    snmpPrivPassphrase: string
    snmpPrivProtocol: string
    snmpROCommunity: string
    snmpRWCommunity: string
    snmpRetry: 0
    snmpTimeout: 0
    snmpUserName: string
    snmpVersion: string
    type: string
    updateMgmtIPaddressList:
    - existMgmtIpAddress: string
      newMgmtIpAddress: string
    userName: string

- name: Update all
  cisco.dnac.network_device:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    cliTransport: string
    computeDevice: true
    enablePassword: string
    extendedDiscoveryInfo: string
    httpPassword: string
    httpPort: string
    httpSecure: true
    httpUserName: string
    ipAddress:
    - string
    merakiOrgId:
    - string
    netconfPort: string
    password: string
    serialNumber: string
    snmpAuthPassphrase: string
    snmpAuthProtocol: string
    snmpMode: string
    snmpPrivPassphrase: string
    snmpPrivProtocol: string
    snmpROCommunity: string
    snmpRWCommunity: string
    snmpRetry: 0
    snmpTimeout: 0
    snmpUserName: string
    snmpVersion: string
    type: string
    updateMgmtIPaddressList:
    - existMgmtIpAddress: string
      newMgmtIpAddress: string
    userName: string

- name: Delete by id
  cisco.dnac.network_device:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    cleanConfig: true
    id: string
```

## [Return Values](network_device_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"response": {"taskId": "string", "url": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
