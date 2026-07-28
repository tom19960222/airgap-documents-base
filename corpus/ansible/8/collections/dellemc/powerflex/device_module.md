---
collection: ansible
version: "8"
title: "dellemc.powerflex.device module – Manage device on Dell PowerFlex"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/powerflex/device_module.html
fetched_at: 2026-07-28T02:05:08+00:00
---
# dellemc.powerflex.device module – Manage device on Dell PowerFlex

> **Note:**
>
> This module is part of the [dellemc.powerflex collection](https://galaxy.ansible.com/ui/repo/published/dellemc/powerflex/) (version 1.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.powerflex`.
> You need further requirements to be able to use this module,
> see [Requirements](device_module.md#ansible-collections-dellemc-powerflex-device-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.powerflex.device`.

New in dellemc.powerflex 1.1.0

- [Synopsis](device_module.md#synopsis)
- [Requirements](device_module.md#requirements)
- [Parameters](device_module.md#parameters)
- [Notes](device_module.md#notes)
- [Examples](device_module.md#examples)
- [Return Values](device_module.md#return-values)

## [Synopsis](device_module.md#id1)

- Managing device on PowerFlex storage system includes adding new device, getting details of device, and removing a device.

Aliases: dellemc_powerflex_device

## [Requirements](device_module.md#id2)

The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 3.5 or later.
- Ansible-core 2.13 or later.
- PyPowerFlex 1.8.0.
- Python 3.9, 3.10 or 3.11.

## [Parameters](device_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **acceleration_pool_id**  string | Acceleration Pool ID.  Used while adding an acceleration device.  Media type supported are `SSD` and `NVDIMM`.  Mutually exclusive with *acceleration_pool_name*, *storage_pool_name* and *storage_pool_id*. |
| **acceleration_pool_name**  string | Acceleration Pool Name.  Used while adding an acceleration device.  Media type supported are `SSD` and `NVDIMM`.  Mutually exclusive with *storage_pool_id*, *storage_pool_name* and *acceleration_pool_name*. |
| **current_pathname**  string | Full path of the device to be added.  Required while adding a device. |
| **device_id**  string | Device ID.  Mutually exclusive with *device_name*. |
| **device_name**  string | Device name.  Mutually exclusive with *device_id*. |
| **external_acceleration_type**  string | Device external acceleration types.  Used while adding a device.  **Choices:**   - `"Invalid"` - `"None"` - `"Read"` - `"Write"` - `"ReadAndWrite"` |
| **force**  boolean | Using the Force flag to add a device.  Use this flag, to overwrite existing data on the device.  Use this flag with caution, because all data on the device will be destroyed.  **Choices:**   - `false` ← (default) - `true` |
| **hostname**  aliases: gateway_host  string / required | IP or FQDN of the PowerFlex host. |
| **media_type**  string | Device media types.  Required while adding a device.  **Choices:**   - `"HDD"` - `"SSD"` - `"NVDIMM"` |
| **password**  string / required | The password of the PowerFlex host. |
| **port**  integer | Port number through which communication happens with PowerFlex host.  **Default:** `443` |
| **protection_domain_id**  string | Protection domain ID.  Used while identifying a storage pool along with *storage_pool_name*.  Mutually exclusive with *protection_domain_name*. |
| **protection_domain_name**  string | Protection domain name.  Used while identifying a storage pool along with *storage_pool_name*.  Mutually exclusive with *protection_domain_id*. |
| **sds_id**  string | The ID of the SDS.  Required while adding a device.  Mutually exclusive with *sds_name*. |
| **sds_name**  string | The name of the SDS.  Required while adding a device.  Mutually exclusive with *sds_id*. |
| **state**  string / required | State of the device.  **Choices:**   - `"present"` - `"absent"` |
| **storage_pool_id**  string | Storage Pool ID.  Used while adding a storage device.  Media type supported are `SSD` and `HDD`.  Mutually exclusive with *storage_pool_name*, *acceleration_pool_id* and *acceleration_pool_name*. |
| **storage_pool_name**  string | Storage Pool name.  Used while adding a storage device.  Mutually exclusive with *storage_pool_id*, *acceleration_pool_id* and *acceleration_pool_name*. |
| **timeout**  integer | Time after which connection will get terminated.  It is to be mentioned in seconds.  **Default:** `120` |
| **username**  string / required | The username of the PowerFlex host. |
| **validate_certs**  aliases: verifycert  boolean | Boolean variable to specify whether or not to validate SSL certificate.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](device_module.md#id4)

> **Note:**
>
> - The value for device_id is generated only after successful addition of the device.
> - To uniquely identify a device, either *device_id* can be passed or one of *current_pathname* or *device_name* must be passed with *sds_id* or *sds_name*.
> - It is recommended to install Rfcache driver for SSD device on SDS in order to add it to an acceleration pool.
> - The *check_mode* is not supported.
> - The modules present in the collection named as ‘dellemc.powerflex’ are built to support the Dell PowerFlex storage platform.

## [Examples](device_module.md#id5)

```yaml+jinja
- name: Add a device
  dellemc.powerflex.device:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    current_pathname: "/dev/sdb"
    sds_name: "node1"
    media_type: "HDD"
    device_name: "device2"
    storage_pool_name: "pool1"
    protection_domain_name: "domain1"
    external_acceleration_type: "ReadAndWrite"
    state: "present"
- name: Add a device with force flag
  dellemc.powerflex.device:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    current_pathname: "/dev/sdb"
    sds_name: "node1"
    media_type: "HDD"
    device_name: "device2"
    storage_pool_name: "pool1"
    protection_domain_name: "domain1"
    external_acceleration_type: "ReadAndWrite"
    force: true
    state: "present"
- name: Get device details using device_id
  dellemc.powerflex.device:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    device_id: "d7fe088900000000"
    state: "present"
- name: Get device details using (current_pathname, sds_name)
  dellemc.powerflex.device:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    current_pathname: "/dev/sdb"
    sds_name: "node0"
    state: "present"
- name: Get device details using (current_pathname, sds_id)
  dellemc.powerflex.device:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    current_pathname: "/dev/sdb"
    sds_id: "5717d71800000000"
    state: "present"
- name: Remove a device using device_id
  dellemc.powerflex.device:
   hostname: "{{hostname}}"
   username: "{{username}}"
   password: "{{password}}"
   validate_certs: "{{validate_certs}}"
   port: "{{port}}"
   device_id: "76eb7e2f00010000"
   state: "absent"
- name: Remove a device using (current_pathname, sds_id)
  dellemc.powerflex.device:
   hostname: "{{hostname}}"
   username: "{{username}}"
   password: "{{password}}"
   validate_certs: "{{validate_certs}}"
   port: "{{port}}"
   current_pathname: "/dev/sdb"
   sds_name: "node1"
   state: "absent"
```

## [Return Values](device_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether or not the resource has changed.  **Returned:** always  **Sample:** `false` |
| **device_details**  dictionary | Details of the device.  **Returned:** When device exists  **Sample:** `{"accelerationPoolId": null, "accelerationProps": null, "aggregatedState": "NeverFailed", "ataSecurityActive": false, "autoDetectMediaType": "SSD", "cacheLookAheadActive": false, "capacity": 0, "capacityLimitInKb": 365772800, "deviceCurrentPathName": "/dev/sdb", "deviceOriginalPathName": "/dev/sdb", "deviceState": "Normal", "deviceType": "Unknown", "errorState": "None", "externalAccelerationType": "None", "fglNvdimmMetadataAmortizationX100": 150, "fglNvdimmWriteCacheSize": 16, "firmwareVersion": null, "id": "b6efa59900000000", "ledSetting": "Off", "links": [{"href": "/api/instances/Device::b6efa59900000000", "rel": "self"}, {"href": "/api/instances/Device::b6efa59900000000/relationships /Statistics", "rel": "/api/Device/relationship/Statistics"}, {"href": "/api/instances/Sds::8f3bb0ce00000000", "rel": "/api/parent/relationship/sdsId"}, {"href": "/api/instances/StoragePool::e0d8f6c900000000", "rel": "/api/parent/relationship/storagePoolId"}, {"href": "/api/instances/SpSds::fedf6f2000000000", "rel": "/api/parent/relationship/spSdsId"}], "logicalSectorSizeInBytes": 0, "longSuccessfulIos": {"longWindow": null, "mediumWindow": null, "shortWindow": null}, "maxCapacityInKb": 365772800, "mediaFailing": false, "mediaType": "HDD", "modelName": null, "name": "device230", "persistentChecksumState": "Protected", "physicalSectorSizeInBytes": 0, "protectionDomainId": "9300c1f900000000", "protectionDomainName": "domain1", "raidControllerSerialNumber": null, "rfcacheErrorDeviceDoesNotExist": false, "rfcacheProps": null, "sdsId": "8f3bb0ce00000000", "sdsName": "node1", "serialNumber": null, "slotNumber": null, "spSdsId": "fedf6f2000000000", "ssdEndOfLifeState": "NeverFailed", "storagePoolId": "e0d8f6c900000000", "storagePoolName": "pool1", "storageProps": {"destFglAccDeviceId": null, "destFglNvdimmSizeMb": 0, "fglAccDeviceId": null, "fglNvdimmSizeMb": 0}, "temperatureState": "NeverFailed", "vendorName": null, "writeCacheActive": false}` |
| **accelerationPoolId**  string | Acceleration pool ID.  **Returned:** success |
| **accelerationPoolName**  string | Acceleration pool name.  **Returned:** success |
| **accelerationProps**  string | Indicates acceleration props.  **Returned:** success |
| **aggregatedState**  string | Indicates aggregated state.  **Returned:** success |
| **ataSecurityActive**  boolean | Indicates ATA security active state.  **Returned:** success |
| **autoDetectMediaType**  string | Indicates auto detection of media type.  **Returned:** success |
| **cacheLookAheadActive**  boolean | Indicates cache look ahead active state.  **Returned:** success |
| **capacity**  integer | Device capacity.  **Returned:** success |
| **capacityLimitInKb**  integer | Device capacity limit in KB.  **Returned:** success |
| **deviceCurrentPathName**  string | Device current path name.  **Returned:** success |
| **deviceOriginalPathName**  string | Device original path name.  **Returned:** success |
| **deviceState**  string | Indicates device state.  **Returned:** success |
| **deviceType**  string | Indicates device type.  **Returned:** success |
| **errorState**  string | Indicates error state.  **Returned:** success |
| **externalAccelerationType**  string | Indicates external acceleration type.  **Returned:** success |
| **fglNvdimmMetadataAmortizationX100**  integer | Indicates FGL NVDIMM meta data amortization value.  **Returned:** success |
| **fglNvdimmWriteCacheSize**  integer | Indicates FGL NVDIMM write cache size.  **Returned:** success |
| **firmwareVersion**  string | Indicates firmware version.  **Returned:** success |
| **id**  string | Device ID.  **Returned:** success |
| **ledSetting**  string | Indicates LED setting.  **Returned:** success |
| **links**  list / elements=string | Device links.  **Returned:** success |
| **href**  string | Device instance URL.  **Returned:** success |
| **rel**  string | Relationship of device with different entities.  **Returned:** success |
| **logicalSectorSizeInBytes**  integer | Logical sector size in bytes.  **Returned:** success |
| **longSuccessfulIos**  list / elements=string | Indicates long successful IOs.  **Returned:** success |
| **maxCapacityInKb**  integer | Maximum device capacity limit in KB.  **Returned:** success |
| **mediaFailing**  boolean | Indicates media failing.  **Returned:** success |
| **mediaType**  string | Indicates media type.  **Returned:** success |
| **modelName**  string | Indicates model name.  **Returned:** success |
| **name**  string | Device name.  **Returned:** success |
| **persistentChecksumState**  string | Indicates persistent checksum state.  **Returned:** success |
| **physicalSectorSizeInBytes**  integer | Physical sector size in bytes.  **Returned:** success |
| **protectionDomainId**  string | Protection domain ID.  **Returned:** success |
| **protectionDomainName**  string | Protection domain name.  **Returned:** success |
| **raidControllerSerialNumber**  string | RAID controller serial number.  **Returned:** success |
| **rfcacheErrorDeviceDoesNotExist**  boolean | Indicates RF cache error device does not exist.  **Returned:** success |
| **rfcacheProps**  string | RF cache props.  **Returned:** success |
| **sdsId**  string | SDS ID.  **Returned:** success |
| **sdsName**  string | SDS name.  **Returned:** success |
| **serialNumber**  string | Indicates Serial number.  **Returned:** success |
| **spSdsId**  string | Indicates SPs SDS ID.  **Returned:** success |
| **ssdEndOfLifeState**  string | Indicates SSD end of life state.  **Returned:** success |
| **storagePoolId**  string | Storage Pool ID.  **Returned:** success |
| **storagePoolName**  string | Storage Pool name.  **Returned:** success |
| **storageProps**  list / elements=string | Storage props.  **Returned:** success |
| **temperatureState**  string | Indicates temperature state.  **Returned:** success |
| **vendorName**  string | Indicates vendor name.  **Returned:** success |
| **writeCacheActive**  boolean | Indicates write cache active.  **Returned:** success |

### Authors

- Rajshree Khare (@khareRajshree)

### Collection links

- [Issue Tracker](https://www.dell.com/community/Automation/bd-p/Automation)
- [Repository (Sources)](https://github.com/dell/ansible-powerflex/tree/1.9.0)
