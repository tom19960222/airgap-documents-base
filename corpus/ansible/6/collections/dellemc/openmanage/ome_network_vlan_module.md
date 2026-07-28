---
collection: ansible
version: "6"
title: "dellemc.openmanage.ome_network_vlan module – Create, modify & delete a VLAN"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/ome_network_vlan_module.html
fetched_at: 2026-07-27T17:25:45+00:00
---
# dellemc.openmanage.ome_network_vlan module – Create, modify & delete a VLAN

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
> see [Requirements](ome_network_vlan_module.md#ansible-collections-dellemc-openmanage-ome-network-vlan-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_network_vlan`.

New in dellemc.openmanage 2.1.0

- [Synopsis](ome_network_vlan_module.md#synopsis)
- [Requirements](ome_network_vlan_module.md#requirements)
- [Parameters](ome_network_vlan_module.md#parameters)
- [Notes](ome_network_vlan_module.md#notes)
- [Examples](ome_network_vlan_module.md#examples)
- [Return Values](ome_network_vlan_module.md#return-values)

## [Synopsis](ome_network_vlan_module.md#id1)

- This module allows to,
- Create a VLAN on OpenManage Enterprise.
- Modify or delete an existing VLAN on OpenManage Enterprise.

## [Requirements](ome_network_vlan_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_network_vlan_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **description**  string | Short description of the VLAN to be created or modified. |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname. |
| **name**  string / required | Provide the *name* of the VLAN to be created, deleted or modified. |
| **new_name**  string | Provide the *name* of the VLAN to be modified. |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  Default: `443` |
| **state**  string | `present` creates a new VLAN or modifies an existing VLAN.  `absent` deletes an existing VLAN.  *WARNING* Deleting a VLAN can impact the network infrastructure.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **type**  string | Types of supported VLAN networks.  For the description of each network type, use API <https://I%28hostname>/api/NetworkConfigurationService/NetworkTypes).  Choices:   - `"General Purpose (Bronze)"` - `"General Purpose (Silver)"` - `"General Purpose (Gold)"` - `"General Purpose (Platinum)"` - `"Cluster Interconnect"` - `"Hypervisor Management"` - `"Storage - iSCSI"` - `"Storage - FCoE"` - `"Storage - Data Replication"` - `"VM Migration"` - `"VMWare FT Logging"` |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |
| **vlan_maximum**  integer | The maximum VLAN value of the range.  A single value VLAN is created if the vlan_maximum and vlan_minmum values are the same. |
| **vlan_minimum**  integer | The minimum VLAN value of the range. |

## [Notes](ome_network_vlan_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to DellEMC OpenManage Enterprise.
> - This module supports `check_mode`.

## [Examples](ome_network_vlan_module.md#id5)

```yaml+jinja
---
- name: Create a VLAN range
  dellemc.openmanage.ome_network_vlan:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    ca_path: "/path/to/ca_cert.pem"
    state: present
    name: "vlan1"
    description: "VLAN desc"
    type: "General Purpose (Bronze)"
    vlan_minimum: 35
    vlan_maximum: 40
  tags: create_vlan_range

- name: Create a VLAN with a single value
  dellemc.openmanage.ome_network_vlan:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    ca_path: "/path/to/ca_cert.pem"
    state: present
    name: "vlan2"
    description: "VLAN desc"
    type: "General Purpose (Bronze)"
    vlan_minimum: 127
    vlan_maximum: 127
  tags: create_vlan_single

- name: Modify a VLAN
  dellemc.openmanage.ome_network_vlan:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    ca_path: "/path/to/ca_cert.pem"
    state: present
    name: "vlan1"
    new_name: "vlan_gold1"
    description: "new description"
    type: "General Purpose (Gold)"
    vlan_minimum: 45
    vlan_maximum: 50
  tags: modify_vlan

- name: Delete a VLAN
  dellemc.openmanage.ome_network_vlan:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    ca_path: "/path/to/ca_cert.pem"
    state: "absent"
    name: "vlan1"
  tags: delete_vlan
```

## [Return Values](ome_network_vlan_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  Returned: on HTTP error  Sample: `{"@Message.ExtendedInfo": [{"Message": "Unable to create or update the network because the entered VLAN minimum 0 is not within a valid range ( 1  -  4000  or  4021  -  4094 ).", "MessageArgs": ["0", "1", "4000", "4021", "4094"], "MessageId": "CTEM1043", "RelatedProperties": [], "Resolution": "Enter a valid VLAN minimum as identified in the message and retry the operation.", "Severity": "Warning"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}` |
| **msg**  string | Overall status of the VLAN operation.  Returned: always  Sample: `"Successfully created the VLAN."` |
| **vlan_status**  dictionary | Details of the VLAN that is either created or modified.  Returned: when *state=present*  Sample: `{"@odata.context": "/api/$metadata#NetworkConfigurationService.Network", "@odata.id": "/api/NetworkConfigurationService/Networks(1234)", "@odata.type": "#NetworkConfigurationService.Network", "CreatedBy": "admin", "CreationTime": "2020-01-01 05:54:36.113", "Description": "VLAN description", "Id": 1234, "InternalRefNWUUId": "6d6effcc-eca4-44bd-be07-1234ab5cd67e", "Name": "vlan1", "Type": 1, "UpdatedBy": null, "UpdatedTime": "2020-01-01 05:54:36.113", "VlanMaximum": 130, "VlanMinimum": 140}` |

### Authors

- Jagadeesh N V(@jagadeeshnv)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
