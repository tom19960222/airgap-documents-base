---
collection: ansible
version: "8"
title: "cisco.dnac.inventory_intent module – Resource module for Network Device"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/inventory_intent_module.html
fetched_at: 2026-07-28T01:22:59+00:00
---
# cisco.dnac.inventory_intent module – Resource module for Network Device

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
> see [Requirements](inventory_intent_module.md#ansible-collections-cisco-dnac-inventory-intent-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.inventory_intent`.

New in cisco.dnac 6.8.0

- [Synopsis](inventory_intent_module.md#synopsis)
- [Requirements](inventory_intent_module.md#requirements)
- [Parameters](inventory_intent_module.md#parameters)
- [Notes](inventory_intent_module.md#notes)
- [See Also](inventory_intent_module.md#see-also)
- [Examples](inventory_intent_module.md#examples)
- [Return Values](inventory_intent_module.md#return-values)

## [Synopsis](inventory_intent_module.md#id1)

- Manage operations create, update and delete of the resource Network Device.
- Adds the device with given credential.
- Deletes the network device for the given Id.
- Sync the devices provided as input.

## [Requirements](inventory_intent_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](inventory_intent_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary / required | List of devices with credentails to perform Add/Update/Delete/Resync operation |
| **cliTransport**  string | Network Device’s cliTransport.Required for Adding Network Devices. |
| **computeDevice**  boolean | ComputeDevice flag.  **Choices:**   - `false` - `true` |
| **enablePassword**  string | Network Device’s enablePassword. |
| **extendedDiscoveryInfo**  string | Network Device’s extendedDiscoveryInfo. |
| **httpPassword**  string | Network Device’s httpPassword.Required for Adding Compute, Meraki, Firepower Management Devices. |
| **httpPort**  string | Network Device’s httpPort.Required for Adding Compute, Firepower Management Devices. |
| **httpSecure**  boolean | HttpSecure flag.  **Choices:**   - `false` - `true` |
| **httpUserName**  string | Network Device’s httpUserName.Required for Adding Compute,Firepower Management Devices. |
| **id**  string | Id path parameter. Device ID.Required for Deleting Device. |
| **ipAddress**  list / elements=string | Network Device’s ipAddress.Required for Adding/Deleting/Resyncing Device except Meraki Devices. |
| **merakiOrgId**  list / elements=string | Network Device’s merakiOrgId. |
| **netconfPort**  string | Network Device’s netconfPort. |
| **password**  string | Network Device’s password.Required for Adding Network Device. |
| **serialNumber**  string | Network Device’s serialNumber. |
| **snmpAuthPassphrase**  string | Network Device’s snmpAuthPassphrase.Required for Adding Network, Compute, Third Party Devices. |
| **snmpAuthProtocol**  string | Network Device’s snmpAuthProtocol.  **Default:** `"SHA"` |
| **snmpMode**  string | Network Device’s snmpMode.  **Default:** `"AUTHPRIV"` |
| **snmpPrivPassphrase**  string | Network Device’s snmpPrivPassphrase.Required for Adding Network, Compute, Third Party Devices. |
| **snmpPrivProtocol**  string | Network Device’s snmpPrivProtocol.Required for Adding Network, Compute, Third Party Devices.  **Default:** `"AES128"` |
| **snmpRetry**  integer | Network Device’s snmpRetry.  **Default:** `3` |
| **snmpROCommunity**  string | Network Device’s snmpROCommunity.Required for Adding V2C Devices.  **Default:** `"public"` |
| **snmpRWCommunity**  string | Network Device’s snmpRWCommunity.Required for Adding V2C Devices.  **Default:** `"private"` |
| **snmpTimeout**  integer | Network Device’s snmpTimeout.  **Default:** `5` |
| **snmpUserName**  string | Network Device’s snmpUserName.Required for Adding Network, Compute, Third Party Devices. |
| **snmpVersion**  string | Network Device’s snmpVersion.  **Default:** `"v3"` |
| **type**  string | Network Device’s type.  **Default:** `"NETWORK_DEVICE"` |
| **updateMgmtIPaddressList**  list / elements=dictionary | Network Device’s updateMgmtIPaddressList. |
| **existMgmtIpAddress**  string | Network Device’s existMgmtIpAddress. |
| **newMgmtIpAddress**  string | Network Device’s newMgmtIpAddress. |
| **userName**  string | Network Device’s userName.Required for Adding Network Device. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_log**  boolean | Flag for logging playbook execution details. If set to true the log file will be created at the location of the execution with the name dnac.log  **Choices:**   - `false` ← (default) - `true` |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  string | The Cisco DNA Center port.  **Default:** `"443"` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.2.3.3"` |
| **state**  string | The state of Cisco DNA Center after module completion.  **Choices:**   - `"merged"` ← (default) - `"deleted"` |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](inventory_intent_module.md#id4)

> **Note:**
>
> - SDK Method used are devices.Devices.add_device, devices.Devices.delete_device_by_id, devices.Devices.sync_devices,
> - Paths used are post /dna/intent/api/v1/network-device, delete /dna/intent/api/v1/network-device/{id}, put /dna/intent/api/v1/network-device,
> - Removed ‘managementIpAddress’ options in v4.3.0.
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](inventory_intent_module.md#id5)

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

## [Examples](inventory_intent_module.md#id6)

```yaml+jinja
- name: Add new device in Inventory with full credentials
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: False
    state: merged
    config:
      - cliTransport: string
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
        snmpRetry: 3
        snmpTimeout: 5
        snmpUserName: string
        snmpVersion: string
        type: string
        updateMgmtIPaddressList:
        - existMgmtIpAddress: string
          newMgmtIpAddress: string
        userName: string
        deviceResync: false

- name: Add new Compute device in Inventory with full credentials.Inputs needed for Compute Device
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: False
    state: merged
    config:
      - ipAddress: string
        httpUserName: string
        httpPassword: string
        httpPort: string
        snmpAuthPassphrase: string
        snmpAuthProtocol: string
        snmpMode: string
        snmpPrivPassphrase: string
        snmpPrivProtocol: string
        snmpRetry:  3
        snmpTimeout: 5
        snmpUserName: string
        userName: string
        deviceResync: false
        type: "COMPUTE_DEVICE"

- name: Add new Meraki device in Inventory with full credentials.Inputs needed for Meraki Device.
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: False
    state: merged
    config:
      - httpPassword: string
        deviceResync: false
        type: "MERAKI_DASHBOARD"

- name: Add new Firepower Management device in Inventory with full credentials.Input needed to add Device.
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: False
    state: merged
    config:
      - ipAddress: string
        httpUserName: string
        httpPassword: string
        httpPort: string
        deviceResync: false
        type: "FIREPOWER_MANAGEMENT_SYSTEM"

- name: Add new Third Party device in Inventory with full credentials.Input needed to add Device.
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: False
    state: merged
    config:
      - ipAddress: string
        snmpAuthPassphrase: string
        snmpAuthProtocol: string
        snmpMode: string
        snmpPrivPassphrase: string
        snmpPrivProtocol: string
        snmpRetry:  3
        snmpTimeout: 5
        snmpUserName: string
        deviceResync: false
        type: "THIRD_PARTY_DEVICE"

- name: Resync Device with IP Addresses
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: False
    state: merged
    config:
      - ipAddress: string
        deviceResync: True
        forceSync: False

- name: Delete Device by id
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: False
    state: deleted
    config:
      - cleanConfig: false
        id: string
```

## [Return Values](inventory_intent_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNA Center Python SDK  **Returned:** always  **Sample:** `{"response": {"taskId": "string", "url": "string"}, "version": "string"}` |

### Authors

- Abhishek Maheshwari (@abmahesh) Madhan Sankaranarayanan (@madhansansel)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
