---
collection: ansible
version: "8"
title: "dellemc.openmanage.ome_network_vlan_info module – Retrieves the information about networks VLAN(s) present in OpenManage Enterprise"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/ome_network_vlan_info_module.html
fetched_at: 2026-07-28T02:04:42+00:00
---
# dellemc.openmanage.ome_network_vlan_info module – Retrieves the information about networks VLAN(s) present in OpenManage Enterprise

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
> see [Requirements](ome_network_vlan_info_module.md#ansible-collections-dellemc-openmanage-ome-network-vlan-info-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_network_vlan_info`.

New in dellemc.openmanage 2.1.0

- [Synopsis](ome_network_vlan_info_module.md#synopsis)
- [Requirements](ome_network_vlan_info_module.md#requirements)
- [Parameters](ome_network_vlan_info_module.md#parameters)
- [Notes](ome_network_vlan_info_module.md#notes)
- [Examples](ome_network_vlan_info_module.md#examples)
- [Return Values](ome_network_vlan_info_module.md#return-values)

## [Synopsis](ome_network_vlan_info_module.md#id1)

- This module allows to retrieve the following. - A list of all the network VLANs with their detailed information. - Information about a specific network VLAN using VLAN *id* or VLAN *name*.

## [Requirements](ome_network_vlan_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_network_vlan_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname. |
| **id**  integer | A unique identifier of the network VLAN available in the device.  *id* and *name* are mutually exclusive. |
| **name**  string | A unique name of the network VLAN available in the device.  *name* and *id* are mutually exclusive. |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  **Default:** `443` |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ome_network_vlan_info_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to Dell OpenManage Enterprise.
> - This module supports `check_mode`.

## [Examples](ome_network_vlan_info_module.md#id5)

```yaml+jinja
---
- name: Retrieve information about all network VLANs(s) available in the device
  dellemc.openmanage.ome_network_vlan_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"

- name: Retrieve information about a network VLAN using the VLAN ID
  dellemc.openmanage.ome_network_vlan_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    id: 12345

- name: Retrieve information about a network VLAN using the VLAN name
  dellemc.openmanage.ome_network_vlan_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    name: "Network VLAN - 1"
```

## [Return Values](ome_network_vlan_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Detailed information of the network VLAN(s).  **Returned:** success  **Sample:** `"{'msg': 'Successfully retrieved the network VLAN information.', 'network_vlan_info': [{'CreatedBy': 'admin', 'CreationTime': '2020-09-02 18:48:42.129', 'Description': 'Description of Logical Network - 1', 'Id': 20057, 'InternalRefNWUUId': '42b9903d-93f8-4184-adcf-0772e4492f71', 'Name': 'Network VLAN - 1', 'Type': {'Description': 'This is the network for general purpose traffic. QOS Priority : Bronze.', 'Id': 1, 'Name': 'General Purpose (Bronze)', 'NetworkTrafficType': 'Ethernet', 'QosType': {'Id': 4, 'Name': 'Bronze'}, 'VendorCode': 'GeneralPurpose'}, 'UpdatedBy': None, 'UpdatedTime': '2020-09-02 18:48:42.129', 'VlanMaximum': 111, 'VlanMinimum': 111}, {'CreatedBy': 'admin', 'CreationTime': '2020-09-02 18:49:11.507', 'Description': 'Description of Logical Network - 2', 'Id': 20058, 'InternalRefNWUUId': 'e46ccb3f-ef57-4617-ac76-46c56594005c', 'Name': 'Network VLAN - 2', 'Type': {'Description': 'This is the network for general purpose traffic. QOS Priority : Silver.', 'Id': 2, 'Name': 'General Purpose (Silver)', 'NetworkTrafficType': 'Ethernet', 'QosType': {'Id': 3, 'Name': 'Silver'}, 'VendorCode': 'GeneralPurpose'}, 'UpdatedBy': None, 'UpdatedTime': '2020-09-02 18:49:11.507', 'VlanMaximum': 112, 'VlanMinimum': 112}]}"` |

### Authors

- Deepak Joshi(@deepakjoshishri)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
