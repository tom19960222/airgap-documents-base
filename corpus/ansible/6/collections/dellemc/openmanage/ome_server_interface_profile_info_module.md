---
collection: ansible
version: "6"
title: "dellemc.openmanage.ome_server_interface_profile_info module – Retrieves the information of server interface profile on OpenManage Enterprise Modular."
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/ome_server_interface_profile_info_module.html
fetched_at: 2026-07-27T17:25:48+00:00
---
# dellemc.openmanage.ome_server_interface_profile_info module – Retrieves the information of server interface profile on OpenManage Enterprise Modular.

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
> see [Requirements](ome_server_interface_profile_info_module.md#ansible-collections-dellemc-openmanage-ome-server-interface-profile-info-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_server_interface_profile_info`.

New in dellemc.openmanage 5.1.0

- [Synopsis](ome_server_interface_profile_info_module.md#synopsis)
- [Requirements](ome_server_interface_profile_info_module.md#requirements)
- [Parameters](ome_server_interface_profile_info_module.md#parameters)
- [Notes](ome_server_interface_profile_info_module.md#notes)
- [Examples](ome_server_interface_profile_info_module.md#examples)
- [Return Values](ome_server_interface_profile_info_module.md#return-values)

## [Synopsis](ome_server_interface_profile_info_module.md#id1)

- This module allows to retrieves the information of server interface profile on OpenManage Enterprise Modular.

## [Requirements](ome_server_interface_profile_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_server_interface_profile_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **device_id**  list / elements=integer | The ID of the device.  *device_id* is mutually exclusive with *device_service_tag*. |
| **device_service_tag**  list / elements=string | The service tag of the device.  *device_service_tag* is mutually exclusive with *device_id*. |
| **hostname**  string / required | OpenManage Enterprise Modular IP address or hostname. |
| **password**  string / required | OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise Modular HTTPS port.  Default: `443` |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **username**  string / required | OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](ome_server_interface_profile_info_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to OpenManage Enterprise Modular.
> - This module supports `check_mode`.

## [Examples](ome_server_interface_profile_info_module.md#id5)

```yaml+jinja
---
- name: Retrieves the server interface profiles of all the device using device ID.
  dellemc.openmanage.ome_server_interface_profile_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_id:
      - 10001
      - 10002

- name: Retrieves the server interface profiles of all the device using device service tag.
  dellemc.openmanage.ome_server_interface_profile_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_service_tag:
      - 6GHH6H2
      - 6KHH6H3
```

## [Return Values](ome_server_interface_profile_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  Returned: on HTTP error  Sample: `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Overall status of the server interface profile information.  Returned: on success  Sample: `"Successfully retrieved the server interface profile information."` |
| **server_profiles**  list / elements=string | Returns the information of collected server interface profile information.  Returned: success  Sample: `[{"BondingTechnology": "LACP", "Id": "6KZK6K2", "ServerInterfaceProfile": [{"FabricId": "1ea6bf64-3cf0-4e06-a136-5046d874d1e7", "Id": "NIC.Mezzanine.1A-1-1", "NativeVLAN": 0, "Networks": [{"CreatedBy": "system", "CreationTime": "2018-11-27 10:22:14.140", "Description": "VLAN 1", "Id": 10001, "InternalRefNWUUId": "add035b9-a971-400d-a3fa-bb365df1d476", "Name\"": "VLAN 1", "Type": 2, "UpdatedBy": null, "UpdatedTime": "2018-11-27 10:22:14.140", "VlanMaximum": 1, "VlanMinimum": 1}], "NicBonded": true, "OnboardedPort": "59HW8X2:ethernet1/1/1"}, {"FabricId": "3ea6be04-5cf0-4e05-a136-5046d874d1e6", "Id": "NIC.Mezzanine.1A-2-1", "NativeVLAN": 0, "Networks": [{"CreatedBy": "system", "CreationTime": "2018-09-25 14:46:12.374", "Description": null, "Id": 10155, "InternalRefNWUUId": "f15a36b6-e3d3-46b2-9e7d-bf9cd66e180d", "Name": "jagvlan", "Type": 1, "UpdatedBy": null, "UpdatedTime": "2018-09-25 14:46:12.374", "VlanMaximum": 143, "VlanMinimum": 143}], "NicBonded": false, "OnboardedPort": "6H7J6Z2:ethernet1/1/1"}]}]` |

### Authors

- Felix Stephen (@felixs88)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
