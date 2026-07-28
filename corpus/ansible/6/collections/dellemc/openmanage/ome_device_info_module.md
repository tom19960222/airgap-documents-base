---
collection: ansible
version: "6"
title: "dellemc.openmanage.ome_device_info module – Retrieves the information of devices inventoried by OpenManage Enterprise"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/ome_device_info_module.html
fetched_at: 2026-07-27T17:25:32+00:00
---
# dellemc.openmanage.ome_device_info module – Retrieves the information of devices inventoried by OpenManage Enterprise

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
> see [Requirements](ome_device_info_module.md#ansible-collections-dellemc-openmanage-ome-device-info-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_device_info`.

New in dellemc.openmanage 2.0.0

- [Synopsis](ome_device_info_module.md#synopsis)
- [Requirements](ome_device_info_module.md#requirements)
- [Parameters](ome_device_info_module.md#parameters)
- [Notes](ome_device_info_module.md#notes)
- [Examples](ome_device_info_module.md#examples)
- [Return Values](ome_device_info_module.md#return-values)

## [Synopsis](ome_device_info_module.md#id1)

- This module retrieves the list of devices in the inventory of OpenManage Enterprise along with the details of each device.

## [Requirements](ome_device_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_device_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **fact_subset**  string | `basic_inventory` returns the list of the devices.  `detailed_inventory` returns the inventory details of specified devices.  `subsystem_health` returns the health status of specified devices.  Choices:   - `"basic_inventory"` ← (default) - `"detailed_inventory"` - `"subsystem_health"` |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname. |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  Default: `443` |
| **system_query_options**  dictionary | *system_query_options* applicable for the choices of the fact_subset. Either *device_id* or *device_service_tag* is mandatory for `detailed_inventory` and `subsystem_health` or both can be applicable. |
| **device_id**  list / elements=integer | A list of unique identifier is applicable for `detailed_inventory` and `subsystem_health`. |
| **device_service_tag**  list / elements=string | A list of service tags are applicable for `detailed_inventory` and `subsystem_health`. |
| **filter**  string | For `basic_inventory`, it filters the collection of devices. *filter* query format should be aligned with OData standards. |
| **inventory_type**  string | For `detailed_inventory`, it returns details of the specified inventory type. |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](ome_device_info_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to DellEMC OpenManage Enterprise.
> - This module supports `check_mode`.

## [Examples](ome_device_info_module.md#id5)

```yaml+jinja
---
- name: Retrieve basic inventory of all devices
  dellemc.openmanage.ome_device_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"

- name: Retrieve basic inventory for devices identified by IDs 33333 or 11111 using filtering
  dellemc.openmanage.ome_device_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    fact_subset: "basic_inventory"
    system_query_options:
      filter: "Id eq 33333 or Id eq 11111"

- name: Retrieve inventory details of specified devices identified by IDs 11111 and 22222
  dellemc.openmanage.ome_device_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    fact_subset: "detailed_inventory"
    system_query_options:
      device_id:
        - 11111
        - 22222

- name: Retrieve inventory details of specified devices identified by service tags MXL1234 and MXL4567
  dellemc.openmanage.ome_device_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    fact_subset: "detailed_inventory"
    system_query_options:
      device_service_tag:
        - MXL1234
        - MXL4567

- name: Retrieve details of specified inventory type of specified devices identified by ID and service tags
  dellemc.openmanage.ome_device_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    fact_subset: "detailed_inventory"
    system_query_options:
      device_id:
        - 11111
      device_service_tag:
        - MXL1234
        - MXL4567
      inventory_type: "serverDeviceCards"

- name: Retrieve subsystem health of specified devices identified by service tags
  dellemc.openmanage.ome_device_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    fact_subset: "subsystem_health"
    system_query_options:
      device_service_tag:
        - MXL1234
        - MXL4567
```

## [Return Values](ome_device_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **device_info**  dictionary | Returns the information collected from the Device.  Returned: success  Sample: `{"value": [{"Actions": null, "AssetTag": null, "ChassisServiceTag": null, "ConnectionState": true, "DeviceManagement": [{"DnsName": "dnsname.host.com", "InstrumentationName": "MX-12345", "MacAddress": "11:10:11:10:11:10", "ManagementId": 12345, "ManagementProfile": [{"HasCreds": 0, "ManagementId": 12345, "ManagementProfileId": 12345, "ManagementURL": "https://192.168.0.1:443", "Status": 1000, "StatusDateTime": "2019-01-21 06:30:08.501"}], "ManagementType": 2, "NetworkAddress": "192.168.0.1"}], "DeviceName": "MX-0003I", "DeviceServiceTag": "MXL1234", "DeviceSubscription": null, "LastInventoryTime": "2019-01-21 06:30:08.501", "LastStatusTime": "2019-01-21 06:30:02.492", "ManagedState": 3000, "Model": "PowerEdge MX7000", "PowerState": 17, "SlotConfiguration": {}, "Status": 4000, "SystemId": 2031, "Type": 2000}]}` |
| **msg**  string | Over all device information status.  Returned: on error  Sample: `"Failed to fetch the device information"` |

### Authors

- Sajna Shetty(@Sajna-Shetty)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
