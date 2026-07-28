---
collection: ansible
version: "8"
title: "dellemc.openmanage.ome_smart_fabric module – Create, modify or delete a fabric on OpenManage Enterprise Modular"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/ome_smart_fabric_module.html
fetched_at: 2026-07-28T02:04:47+00:00
---
# dellemc.openmanage.ome_smart_fabric module – Create, modify or delete a fabric on OpenManage Enterprise Modular

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
> see [Requirements](ome_smart_fabric_module.md#ansible-collections-dellemc-openmanage-ome-smart-fabric-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_smart_fabric`.

New in dellemc.openmanage 2.1.0

- [Synopsis](ome_smart_fabric_module.md#synopsis)
- [Requirements](ome_smart_fabric_module.md#requirements)
- [Parameters](ome_smart_fabric_module.md#parameters)
- [Notes](ome_smart_fabric_module.md#notes)
- [Examples](ome_smart_fabric_module.md#examples)
- [Return Values](ome_smart_fabric_module.md#return-values)

## [Synopsis](ome_smart_fabric_module.md#id1)

- This module allows to create a fabric, and modify or delete an existing fabric on OpenManage Enterprise Modular.

## [Requirements](ome_smart_fabric_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_smart_fabric_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **description**  string | Provide a short description of the fabric to be created or modified. |
| **fabric_design**  string | Specify the fabric topology.See the use API <https://www.dell.com/support/manuals/en-in/poweredge-mx7000/omem_1_20_10_ug/smartfabric-network-topologies> to know why its topology.  *fabric_design* is mandatory for fabric creation.  **Choices:**   - `"2xMX5108n_Ethernet_Switches_in_same_chassis"` - `"2xMX9116n_Fabric_Switching_Engines_in_same_chassis"` - `"2xMX9116n_Fabric_Switching_Engines_in_different_chassis"` |
| **hostname**  string / required | OpenManage Enterprise Modular IP address or hostname. |
| **name**  string / required | Provide the *name* of the fabric to be created, deleted or modified. |
| **new_name**  string | Provide the *name* of the fabric to be modified. |
| **override_LLDP_configuration**  string | Enable this configuration to allow Fabric Management Address to be included in LLDP messages.  Notes: OpenManage Enterprise Modular 1.0 does not support this option. Some software networking solutions require a single management address to be transmitted by all Ethernet switches to represent the entire fabric. Enable this feature only when connecting to such a solution.  **Choices:**   - `"Enabled"` - `"Disabled"` |
| **password**  string / required | OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise Modular HTTPS port.  **Default:** `443` |
| **primary_switch_service_tag**  string | Service tag of the first switch.  *primary_switch_service_tag* is mandatory for fabric creation.  *primary_switch_service_tag* must belong to the model selected in *fabric_design*. |
| **secondary_switch_service_tag**  string | Service tag of the second switch.  *secondary_switch_service_tag* is mandatory for fabric creation.  *secondary_switch_service_tag* must belong to the model selected in *fabric_design*. |
| **state**  string | `present` creates a new fabric or modifies an existing fabric.  `absent` deletes an existing fabric.  Notes: The create, modify, or delete fabric operation takes around 15-20 minutes to complete. It is recommended not to start an another operation until the current operation is completed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **username**  string / required | OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ome_smart_fabric_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to Dell OpenManage Enterprise Modular.
> - This module supports `check_mode`.

## [Examples](ome_smart_fabric_module.md#id5)

```yaml+jinja
---
- name: Create a fabric
  dellemc.openmanage.ome_smart_fabric:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: present
    name: "fabric1"
    description: "fabric desc"
    fabric_design: "2xMX9116n_Fabric_Switching_Engines_in_different_chassis"
    primary_switch_service_tag: "SVTG123"
    secondary_switch_service_tag: "PXYT456"
    override_LLDP_configuration: "Enabled"

- name: Modify a fabric
  dellemc.openmanage.ome_smart_fabric:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: present
    name: "fabric1"
    new_name: "fabric_gold1"
    description: "new description"

- name: Delete a fabric
  dellemc.openmanage.ome_smart_fabric:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: "absent"
    name: "fabric1"
```

## [Return Values](ome_smart_fabric_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **additional_info**  dictionary | Additional details of the fabric operation.  **Returned:** when *state=present* and additional information present in response.  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Fabric update is successful. The OverrideLLDPConfiguration attribute is not provided in the payload, so it preserves the previous value.", "MessageArgs": [], "RelatedProperties": [], "Resolution": "Please update the Fabric with the OverrideLLDPConfiguration as Disabled or Enabled if necessary.", "Severity": "Informational"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **error_info**  dictionary | Details of the HTTP Error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to perform operation, because the fabric manager was not reachable.", "MessageArgs": [], "RelatedProperties": [], "Resolution": "Make sure of the following and retry the operation: 1) There is at least one advanced I/O Module in power-on mode. For example, MX9116n Ethernet Switch and MX5108n Ethernet Switch. However, if an advanced I/O Module is available in the power-on mode, make sure that the network profile is not set when the fabric manager is in the switch-over mode. 2) If the issue persists, wait for few minutes and retry the operation.", "Severity": "Warning"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **fabric_id**  string | Returns the ID when an fabric is created, modified or deleted.  **Returned:** success  **Sample:** `"1312cceb-c3dd-4348-95c1-d8541a17d776"` |
| **msg**  string | Overall status of the fabric operation.  **Returned:** always  **Sample:** `"Fabric creation operation is initiated."` |

### Authors

- Sajna Shetty(@Sajna-Shetty)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
