---
collection: ansible
version: "6"
title: "dellemc.openmanage.ome_device_location module – Configure device location settings on OpenManage Enterprise Modular"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/ome_device_location_module.html
fetched_at: 2026-07-27T17:25:33+00:00
---
# dellemc.openmanage.ome_device_location module – Configure device location settings on OpenManage Enterprise Modular

> **Note:**
>
> This module is part of the [dellemc.openmanage collection](https://galaxy.ansible.com/dellemc/openmanage) (version 5.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.openmanage`.
> You need further requirements to be able to use this module,
> see [Requirements](ome_device_location_module.md#ansible-collections-dellemc-openmanage-ome-device-location-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_device_location`.

New in dellemc.openmanage 4.2.0

- [Synopsis](ome_device_location_module.md#synopsis)
- [Requirements](ome_device_location_module.md#requirements)
- [Parameters](ome_device_location_module.md#parameters)
- [Notes](ome_device_location_module.md#notes)
- [Examples](ome_device_location_module.md#examples)
- [Return Values](ome_device_location_module.md#return-values)

## [Synopsis](ome_device_location_module.md#id1)

- This module allows to configure the device location settings of the chassis on OpenManage Enterprise Modular.

## [Requirements](ome_device_location_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_device_location_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aisle**  string | The aisle of the chassis. |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **data_center**  string | The data center name of the chassis. |
| **device_id**  integer | The ID of the chassis for which the settings need to be updated.  If the device ID is not specified, this module updates the location settings for the *hostname*.  *device_id* is mutually exclusive with *device_service_tag*. |
| **device_service_tag**  string | The service tag of the chassis for which the settings need to be updated.  If the device service tag is not specified, this module updates the location settings for the *hostname*.  *device_service_tag* is mutually exclusive with *device_id*. |
| **hostname**  string / required | OpenManage Enterprise Modular IP address or hostname. |
| **location**  string | The physical location of the chassis. |
| **password**  string / required | OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise Modular HTTPS port.  Default: `443` |
| **rack**  string | The rack name of the chassis. |
| **rack_slot**  integer | The rack slot number of the chassis. |
| **room**  string | The room of the chassis. |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **username**  string / required | OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](ome_device_location_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to Dell EMC OpenManage Enterprise Modular.
> - This module supports `check_mode`.

## [Examples](ome_device_location_module.md#id5)

```yaml+jinja
---
- name: Update device location settings of a chassis using the device ID.
  dellemc.openmanage.ome_device_location:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_id: 25011
    data_center: data center 1
    room: room 1
    aisle: aisle 1
    rack: rack 1
    rack_slot: 2
    location: location 1

- name: Update device location settings of a chassis using the device service tag.
  dellemc.openmanage.ome_device_location:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_service_tag: GHRT2RL
    data_center: data center 2
    room: room 7
    aisle: aisle 4
    rack: rack 6
    rack_slot: 22
    location: location 5

- name: Update device location settings of the host chassis.
  dellemc.openmanage.ome_device_location:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    data_center: data center 3
    room: room 3
    aisle: aisle 1
    rack: rack 7
    rack_slot: 10
    location: location 9
```

## [Return Values](ome_device_location_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  Returned: on HTTP error  Sample: `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **location_details**  dictionary | returned when location settings are updated successfully.  Returned: success  Sample: `{"Aisle": "aisle 1", "DataCenter": "data center 1", "Location": "location 1", "RackName": "rack 1", "RackSlot": 2, "Room": "room 1", "SettingType": "Location"}` |
| **msg**  string | Overall status of the device location settings.  Returned: always  Sample: `"Successfully updated the location settings."` |

### Authors

- Felix Stephen (@felixs88)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
