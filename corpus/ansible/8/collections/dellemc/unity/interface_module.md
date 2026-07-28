---
collection: ansible
version: "8"
title: "dellemc.unity.interface module – Manage Interfaces on Unity storage system"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/unity/interface_module.html
fetched_at: 2026-07-28T02:05:25+00:00
---
# dellemc.unity.interface module – Manage Interfaces on Unity storage system

> **Note:**
>
> This module is part of the [dellemc.unity collection](https://galaxy.ansible.com/ui/repo/published/dellemc/unity/) (version 1.7.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.unity`.
> You need further requirements to be able to use this module,
> see [Requirements](interface_module.md#ansible-collections-dellemc-unity-interface-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.unity.interface`.

New in dellemc.unity 1.4.0

- [Synopsis](interface_module.md#synopsis)
- [Requirements](interface_module.md#requirements)
- [Parameters](interface_module.md#parameters)
- [Notes](interface_module.md#notes)
- [Examples](interface_module.md#examples)
- [Return Values](interface_module.md#return-values)

## [Synopsis](interface_module.md#id1)

- Managing the Interfaces on the Unity storage system includes adding Interfaces to NAS Server, getting details of interface and deleting configured interfaces.

## [Requirements](interface_module.md#id2)

The below requirements are needed on the host that executes this module.

- A Dell Unity Storage device version 5.1 or later.
- Ansible-core 2.13 or later.
- Python 3.9, 3.10 or 3.11.
- Storops Python SDK 1.2.11.

## [Parameters](interface_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ethernet_port_id**  string | ID of the ethernet port. |
| **ethernet_port_name**  string | Name of the ethernet port. |
| **gateway**  string | Gateway of network interface. |
| **interface_ip**  string / required | IP of network interface. |
| **nas_server_id**  string | ID of the NAS server for which interface will be configured. |
| **nas_server_name**  string | Name of the NAS server for which interface will be configured. |
| **netmask**  string | Netmask of network interface. |
| **password**  string / required | The password of the Unity management server. |
| **port**  integer | Port number through which communication happens with Unity management server.  **Default:** `443` |
| **prefix_length**  integer | Prefix length is mutually exclusive with *netmask*. |
| **role**  string | Indicates whether interface is configured as production or backup.  **Choices:**   - `"PRODUCTION"` - `"BACKUP"` |
| **state**  string / required | Define whether the interface should exist or not.  **Choices:**   - `"present"` - `"absent"` |
| **unispherehost**  string / required | IP or FQDN of the Unity management server. |
| **username**  string / required | The username of the Unity management server. |
| **validate_certs**  aliases: verifycert  boolean | Boolean variable to specify whether or not to validate SSL certificate.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |
| **vlan_id**  integer | Vlan id of the interface. |

## [Notes](interface_module.md#id4)

> **Note:**
>
> - The *check_mode* is supported.
> - Modify operation for interface is not supported.
> - The modules present in this collection named as ‘dellemc.unity’ are built to support the Dell Unity storage platform.

## [Examples](interface_module.md#id5)

```yaml+jinja
- name: Add Interface as Backup to NAS Server
  dellemc.unity.interface:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    nas_server_name: "dummy_nas"
    ethernet_port_name: "SP A 4-Port Card Ethernet Port 0"
    role: "BACKUP"
    interface_ip: "xx.xx.xx.xx"
    netmask: "xx.xx.xx.xx"
    gateway: "xx.xx.xx.xx"
    vlan_id: 324
    state: "present"

- name: Add Interface as Production to NAS Server
  dellemc.unity.interface:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    nas_server_name: "dummy_nas"
    ethernet_port_name: "SP A 4-Port Card Ethernet Port 0"
    role: "PRODUCTION"
    interface_ip: "xx.xx.xx.xx"
    netmask: "xx.xx.xx.xx"
    gateway: "xx.xx.xx.xx"
    vlan_id: 324
    state: "present"

- name: Get interface details
  dellemc.unity.interface:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    nas_server_name: "dummy_nas"
    interface_ip: "xx.xx.xx.xx"
    state: "present"

- name: Delete Interface
  dellemc.unity.interface:
  unispherehost: "{{unispherehost}}"
  username: "{{username}}"
  password: "{{password}}"
  validate_certs: "{{validate_certs}}"
  nas_server_name: "dummy_nas"
  interface_ip: "xx.xx.xx.xx"
  state: "absent"
```

## [Return Values](interface_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether or not the resource has changed.  **Returned:** always  **Sample:** `true` |
| **interface_details**  dictionary | Details of the interface.  **Returned:** When interface is configured for NAS Server.  **Sample:** `{"existed": true, "gateway": "xx.xx.xx.xx", "hash": 8785300560421, "health": {"UnityHealth": {"hash": 8785300565468}}, "id": "if_69", "ip_address": "10.10.10.10", "ip_port": {"UnityIpPort": {"hash": 8785300565300, "id": "spb_ocp_0_eth0"}}, "ip_protocol_version": "IpProtocolVersionEnum.IPv4", "is_disabled": false, "is_preferred": true, "mac_address": "0C:48:C6:9F:57:BF", "name": "36_APM00213404194", "nas_server": {"UnityNasServer": {"hash": 8785300565417, "id": "nas_10"}}, "netmask": "10.10.10.10", "replication_policy": null, "role": "FileInterfaceRoleEnum.PRODUCTION", "source_parameters": null, "v6_prefix_length": null, "vlan_id": 324}` |
| **existed**  boolean | Indicates if interface exists.  **Returned:** success |
| **gateway**  string | Gateway of network interface.  **Returned:** success |
| **id**  string | Unique identifier interface.  **Returned:** success |
| **ip_address**  string | IP address of interface.  **Returned:** success |
| **ip_port**  dictionary | Port on which network interface is configured.  **Returned:** success |
| **id**  string | ID of ip_port.  **Returned:** success |
| **ip_protocol_version**  string | IP protocol version.  **Returned:** success |
| **is_disabled**  boolean | Indicates whether interface is disabled.  **Returned:** success |
| **is_preferred**  boolean | Indicates whether interface is preferred.  **Returned:** success |
| **mac_address**  boolean | Mac address of ip_port.  **Returned:** success |
| **name**  boolean | System configured name of interface.  **Returned:** success |
| **nas_server**  dictionary | Details of NAS server where interface is configured.  **Returned:** success |
| **id**  string | ID of NAS Server.  **Returned:** success |

### Authors

- Meenakshi Dembi (@dembim)

### Collection links

- [Issue Tracker](https://www.dell.com/community/Automation/bd-p/Automation)
- [Repository (Sources)](https://github.com/dell/ansible-unity/tree/1.7.1)
