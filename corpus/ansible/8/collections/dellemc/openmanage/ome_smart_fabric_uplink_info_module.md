---
collection: ansible
version: "8"
title: "dellemc.openmanage.ome_smart_fabric_uplink_info module – Retrieve details of fabric uplink on OpenManage Enterprise Modular."
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/ome_smart_fabric_uplink_info_module.html
fetched_at: 2026-07-28T02:04:49+00:00
---
# dellemc.openmanage.ome_smart_fabric_uplink_info module – Retrieve details of fabric uplink on OpenManage Enterprise Modular.

> **Note:**
>
> This module is part of the [dellemc.openmanage collection](https://galaxy.ansible.com/ui/repo/published/dellemc/openmanage/) (version 7.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.openmanage`.
> You need further requirements to be able to use this module,
> see [Requirements](ome_smart_fabric_uplink_info_module.md#ansible-collections-dellemc-openmanage-ome-smart-fabric-uplink-info-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_smart_fabric_uplink_info`.

New in dellemc.openmanage 7.1.0

- [Synopsis](ome_smart_fabric_uplink_info_module.md#synopsis)
- [Requirements](ome_smart_fabric_uplink_info_module.md#requirements)
- [Parameters](ome_smart_fabric_uplink_info_module.md#parameters)
- [Notes](ome_smart_fabric_uplink_info_module.md#notes)
- [Examples](ome_smart_fabric_uplink_info_module.md#examples)
- [Return Values](ome_smart_fabric_uplink_info_module.md#return-values)

## [Synopsis](ome_smart_fabric_uplink_info_module.md#id1)

- This module retrieve details of fabric uplink on OpenManage Enterprise Modular.

## [Requirements](ome_smart_fabric_uplink_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.9.6

## [Parameters](ome_smart_fabric_uplink_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **fabric_id**  string | Unique id of the fabric.  *fabric_id* is mutually exclusive with *fabric_name*. |
| **fabric_name**  string | Unique name of the fabric.  *fabric_name* is mutually exclusive with *fabric_id*. |
| **hostname**  string / required | OpenManage Enterprise Modular IP address or hostname. |
| **password**  string / required | OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise Modular HTTPS port.  **Default:** `443` |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **uplink_id**  string | Unique id of the uplink.  *uplink_id* is mutually exclusive with *uplink_name*.  *fabric_id* or *fabric_name* is required along with *uplink_id*. |
| **uplink_name**  string | Unique name of the uplink.  *uplink_name* is mutually exclusive with *uplink_id*.  *fabric_id* or *fabric_name* is required along with *uplink_name*. |
| **username**  string / required | OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ome_smart_fabric_uplink_info_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to Dell OpenManage Enterprise Modular.
> - This module supports `check_mode`.

## [Examples](ome_smart_fabric_uplink_info_module.md#id5)

```yaml+jinja
---
- name: Retrieve all fabric uplink information using fabric_id.
  dellemc.openmanage.ome_smart_fabric_uplink_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    fabric_id: "61c20a59-9ed5-4ae5-b850-5e5acf42d2f2"

- name: Retrieve all fabric uplink information using fabric_name.
  dellemc.openmanage.ome_smart_fabric_uplink_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    fabric_name: "f1"

- name: Retrieve specific fabric information using uplink_id.
  dellemc.openmanage.ome_smart_fabric_uplink_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    fabric_id: "61c20a59-9ed5-4ae5-b850-5e5acf42d2f2"
    uplink_id: "1ad54420-b145-49a1-9779-21a579ef6f2d"

- name: Retrieve specific fabric information using uplink_name.
  dellemc.openmanage.ome_smart_fabric_uplink_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    fabric_id: "61c20a59-9ed5-4ae5-b850-5e5acf42d2f2"
    uplink_name: "u1"
```

## [Return Values](ome_smart_fabric_uplink_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to complete the request because the resource URI does not exist or is not implemented.", "MessageArgs": [], "MessageId": "CGEN1006", "RelatedProperties": [], "Resolution": "Check the request resource URI. Refer to the OpenManage Enterprise-Modular User's Guide for more information about resource URI and its properties.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Status of fabric uplink information retrieval.  **Returned:** always  **Sample:** `"Successfully retrieved the fabric uplink information."` |
| **uplink_info**  list / elements=string | Information about the fabric uplink.  **Returned:** on success  **Sample:** `[{"Description": "", "Id": "1ad54420-b145-49a1-9779-21a579ef6f2d", "MediaType": "Ethernet", "Name": "u1", "NativeVLAN": 1, "Networks": [{"CreatedBy": "system", "CreationTime": "2018-09-25 14:46:12.374", "Description": null, "Id": 10155, "InternalRefNWUUId": "f15a36b6-e3d3-46b2-9e7d-bf9cd66e180d", "Name": "testvlan", "Type": 1, "UpdatedBy": "root", "UpdatedTime": "2019-06-27 15:06:22.836", "VlanMaximum": 143, "VlanMinimum": 143}], "Ports": [{"AdminStatus": "Enabled", "BlinkStatus": "OFF", "ConfiguredSpeed": "0", "CurrentSpeed": "0", "Description": "", "Id": "SVCTAG1:ethernet1/1/35", "MaxSpeed": "0", "MediaType": "Ethernet", "Name": "", "NodeServiceTag": "SVCTAG1", "OpticsType": "NotPresent", "PortNumber": "ethernet1/1/35", "Role": "Uplink", "Status": "Down", "Type": "PhysicalEthernet"}, {"AdminStatus": "Enabled", "BlinkStatus": "OFF", "ConfiguredSpeed": "0", "CurrentSpeed": "0", "Description": "", "Id": "SVCTAG1:ethernet1/1/35", "MaxSpeed": "0", "MediaType": "Ethernet", "Name": "", "NodeServiceTag": "SVCTAG1", "OpticsType": "NotPresent", "PortNumber": "ethernet1/1/35", "Role": "Uplink", "Status": "Down", "Type": "PhysicalEthernet"}], "Summary": {"NetworkCount": 1, "PortCount": 2}, "UfdEnable": "Disabled"}]` |

### Authors

- Husniya Hameed(@husniya_hameed)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
