---
collection: ansible
version: "6"
title: "dellemc.openmanage.ome_smart_fabric_uplink module – Create, modify or delete a uplink for a fabric on OpenManage Enterprise Modular"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/ome_smart_fabric_uplink_module.html
fetched_at: 2026-07-27T17:25:50+00:00
---
# dellemc.openmanage.ome_smart_fabric_uplink module – Create, modify or delete a uplink for a fabric on OpenManage Enterprise Modular

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
> see [Requirements](ome_smart_fabric_uplink_module.md#ansible-collections-dellemc-openmanage-ome-smart-fabric-uplink-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_smart_fabric_uplink`.

New in dellemc.openmanage 2.1.0

- [Synopsis](ome_smart_fabric_uplink_module.md#synopsis)
- [Requirements](ome_smart_fabric_uplink_module.md#requirements)
- [Parameters](ome_smart_fabric_uplink_module.md#parameters)
- [Notes](ome_smart_fabric_uplink_module.md#notes)
- [Examples](ome_smart_fabric_uplink_module.md#examples)
- [Return Values](ome_smart_fabric_uplink_module.md#return-values)

## [Synopsis](ome_smart_fabric_uplink_module.md#id1)

- This module allows to create, modify or delete an uplink for a fabric.

## [Requirements](ome_smart_fabric_uplink_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_smart_fabric_uplink_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **description**  string | Provide a short description for the uplink to be created or modified. |
| **fabric_name**  string / required | Provide the *fabric_name* of the fabric for which the uplink is to be configured. |
| **hostname**  string / required | OpenManage Enterprise Modular IP address or hostname. |
| **name**  string / required | Provide the *name* of the uplink to be created, modified or deleted. |
| **new_name**  string | Provide the new *new_name* for the uplink. |
| **password**  string / required | OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise Modular HTTPS port.  Default: `443` |
| **primary_switch_ports**  list / elements=string | The IOM slots to be connected to the primary switch.  *primary_switch_service_tag* is mandatory for this option. |
| **primary_switch_service_tag**  string | Service tag of the primary switch. |
| **secondary_switch_ports**  list / elements=string | The IOM slots to be connected to the secondary switch.  *secondary_switch_service_tag* is mandatory for this option. |
| **secondary_switch_service_tag**  string | Service tag of the secondary switch. |
| **state**  string | `present` - Creates a new uplink with the provided *name*. - Modifies an existing uplink with the provided *name*.  `absent` – Deletes the uplink with the provided *name*.  *WARNING* Delete operation can impact the network infrastructure.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tagged_networks**  list / elements=string | VLANs to be associated with the uplink *name*. |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **ufd_enable**  string | Add or Remove the uplink to the Uplink Failure Detection (UFD) group. The UFD group identifies the loss of connectivity to the upstream switch and notifies the servers that are connected to the switch. During an uplink failure, the switch disables the corresponding downstream server ports. The downstream servers can then select alternate connectivity routes, if available.  *WARNING* The firmware version of the I/O Module running the Fabric Manager must support this configuration feature. If not, uplink creation will be successful with an appropriate error message in response.  Choices:   - `"Enabled"` - `"Disabled"` |
| **untagged_network**  string | Specify the name of the VLAN to be added as untagged to the uplink. |
| **uplink_type**  string | Specify the uplink type.  *NOTE* The uplink type cannot be changed for an existing uplink.  Choices:   - `"Ethernet"` - `"FCoE"` - `"FC Gateway"` - `"FC Direct Attach"` - `"Ethernet - No Spanning Tree"` |
| **username**  string / required | OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](ome_smart_fabric_uplink_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to DellEMC OpenManage Enterprise Modular.
> - This module supports `check_mode`.

## [Examples](ome_smart_fabric_uplink_module.md#id5)

```yaml+jinja
---
- name: Create an Uplink
  dellemc.openmanage.ome_smart_fabric_uplink:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: "present"
    fabric_name: "fabric1"
    name: "uplink1"
    description: "CREATED from OMAM"
    uplink_type: "Ethernet"
    ufd_enable: "Enabled"
    primary_switch_service_tag: "ABC1234"
    primary_switch_ports:
      - ethernet1/1/13
      - ethernet1/1/14
    secondary_switch_service_tag: "XYZ1234"
    secondary_switch_ports:
      - ethernet1/1/13
      - ethernet1/1/14
    tagged_networks:
      - vlan1
      - vlan3
    untagged_network: vlan2
  tags: create_uplink

- name: Modify an existing uplink
  dellemc.openmanage.ome_smart_fabric_uplink:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: "present"
    fabric_name: "fabric1"
    name: "uplink1"
    new_name: "uplink2"
    description: "Modified from OMAM"
    uplink_type: "Ethernet"
    ufd_enable: "Disabled"
    primary_switch_service_tag: "DEF1234"
    primary_switch_ports:
      - ethernet1/2/13
      - ethernet1/2/14
    secondary_switch_service_tag: "TUV1234"
    secondary_switch_ports:
      - ethernet1/2/13
      - ethernet1/2/14
    tagged_networks:
      - vlan11
      - vlan33
    untagged_network: vlan22
  tags: modify_uplink

- name: Delete an Uplink
  dellemc.openmanage.ome_smart_fabric_uplink:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: "absent"
    fabric_name: "fabric1"
    name: "uplink1"
  tags: delete_uplink

- name: Modify an Uplink name
  dellemc.openmanage.ome_smart_fabric_uplink:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: "present"
    fabric_name: "fabric1"
    name: "uplink1"
    new_name: "uplink2"
  tags: modify_uplink_name

- name: Modify Uplink ports
  dellemc.openmanage.ome_smart_fabric_uplink:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: "present"
    fabric_name: "fabric1"
    name: "uplink1"
    description: "uplink ports modified"
    primary_switch_service_tag: "ABC1234"
    primary_switch_ports:
      - ethernet1/1/6
      - ethernet1/1/7
    secondary_switch_service_tag: "XYZ1234"
    secondary_switch_ports:
      - ethernet1/1/9
      - ethernet1/1/10
  tags: modify_ports

- name: Modify Uplink networks
  dellemc.openmanage.ome_smart_fabric_uplink:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: "present"
    fabric_name: "fabric1"
    name: "create1"
    description: "uplink networks modified"
    tagged_networks:
      - vlan4
  tags: modify_networks
```

## [Return Values](ome_smart_fabric_uplink_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **additional_info**  dictionary | Additional details of the fabric operation.  Returned: when *state=present* and additional information present in response.  Sample: `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to configure the Uplink Failure Detection mode on the uplink because the firmware version of the I/O Module running the Fabric Manager does not support the configuration feature.", "MessageArgs": [], "MessageId": "CDEV7151", "RelatedProperties": [], "Resolution": "Update the firmware version of the I/O Module running the Fabric Manager and retry the operation. For information about the recommended I/O Module firmware versions, see the OpenManage Enterprise-Modular User's Guide available on the support site.", "Severity": "Informational"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **error_info**  dictionary | Details of the HTTP Error.  Returned: on HTTP error  Sample: `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to complete the request because the resource URI does not exist or is not implemented.", "MessageArgs": [], "MessageId": "CGEN1006", "RelatedProperties": [], "Resolution": "Check the request resource URI. Refer to the OpenManage Enterprise-Modular User's Guide for more information about resource URI and its properties.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Overall status of the uplink operation.  Returned: always  Sample: `"Successfully modified the uplink."` |
| **uplink_id**  string | Returns the ID when an uplink is created or modified.  Returned: when *state=present*  Sample: `"ddc3d260-fd71-46a1-97f9-708e12345678"` |

### Authors

- Jagadeesh N V(@jagadeeshnv)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
