---
collection: ansible
version: "8"
title: "dellemc.unity.host module – Manage Host operations on Unity"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/unity/host_module.html
fetched_at: 2026-07-28T02:05:23+00:00
---
# dellemc.unity.host module – Manage Host operations on Unity

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
> see [Requirements](host_module.md#ansible-collections-dellemc-unity-host-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.unity.host`.

New in dellemc.unity 1.1.0

- [Synopsis](host_module.md#synopsis)
- [Requirements](host_module.md#requirements)
- [Parameters](host_module.md#parameters)
- [Notes](host_module.md#notes)
- [Examples](host_module.md#examples)
- [Return Values](host_module.md#return-values)

## [Synopsis](host_module.md#id1)

- The Host module contains the operations Creation of a Host, Addition of initiators to Host, Removal of initiators from Host, Modification of host attributes, Get details of a Host, Deletion of a Host, Addition of network address to Host, Removal of network address from Host.

Aliases: dellemc_unity_host

## [Requirements](host_module.md#id2)

The below requirements are needed on the host that executes this module.

- A Dell Unity Storage device version 5.1 or later.
- Ansible-core 2.13 or later.
- Python 3.9, 3.10 or 3.11.
- Storops Python SDK 1.2.11.

## [Parameters](host_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  string | Host description. |
| **host_id**  string | Unique identifier of the host.  Host Id is auto generated during creation.  Except create, all other operations require either *host_id* or Ihost_name). |
| **host_name**  string | Name of the host.  Mandatory for host creation. |
| **host_os**  string | Operating system running on the host.  **Choices:**   - `"AIX"` - `"Citrix XenServer"` - `"HP-UX"` - `"IBM VIOS"` - `"Linux"` - `"Mac OS"` - `"Solaris"` - `"VMware ESXi"` - `"Windows Client"` - `"Windows Server"` |
| **initiator_state**  string | State of the initiator.  **Choices:**   - `"present-in-host"` - `"absent-in-host"` |
| **initiators**  list / elements=string | List of initiators to be added/removed to/from host. |
| **network_address**  string | Network address to be added/removed to/from the host.  Enter valid IPV4 or host name. |
| **network_address_state**  string | State of the Network address.  **Choices:**   - `"present-in-host"` - `"absent-in-host"` |
| **new_host_name**  string | New name for the host.  Only required in rename host operation. |
| **password**  string / required | The password of the Unity management server. |
| **port**  integer | Port number through which communication happens with Unity management server.  **Default:** `443` |
| **state**  string / required | State of the host.  **Choices:**   - `"present"` - `"absent"` |
| **unispherehost**  string / required | IP or FQDN of the Unity management server. |
| **username**  string / required | The username of the Unity management server. |
| **validate_certs**  aliases: verifycert  boolean | Boolean variable to specify whether or not to validate SSL certificate.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](host_module.md#id4)

> **Note:**
>
> - The *check_mode* is not supported.
> - The modules present in this collection named as ‘dellemc.unity’ are built to support the Dell Unity storage platform.

## [Examples](host_module.md#id5)

```yaml+jinja
- name: Create empty Host
  dellemc.unity.host:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    host_name: "ansible-test-host"
    host_os: "Linux"
    description: "ansible-test-host"
    state: "present"

- name: Create Host with Initiators
  dellemc.unity.host:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    host_name: "ansible-test-host-1"
    host_os: "Linux"
    description: "ansible-test-host-1"
    initiators:
      - "iqn.1994-05.com.redhat:c38e6e8cfd81"
      - "20:00:00:90:FA:13:81:8D:10:00:00:90:FA:13:81:8D"
    initiator_state: "present-in-host"
    state: "present"

- name: Modify Host using host_id
  dellemc.unity.host:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    host_id: "Host_253"
    new_host_name: "ansible-test-host-2"
    host_os: "Mac OS"
    description: "Ansible tesing purpose"
    state: "present"

- name: Add Initiators to Host
  dellemc.unity.host:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    host_name: "ansible-test-host-2"
    initiators:
      - "20:00:00:90:FA:13:81:8C:10:00:00:90:FA:13:81:8C"
    initiator_state: "present-in-host"
    state: "present"

- name: Get Host details using host_name
  dellemc.unity.host:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    host_name: "ansible-test-host-2"
    state: "present"

- name: Get Host details using host_id
  dellemc.unity.host:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    host_id: "Host_253"
    state: "present"

- name: Delete Host
  dellemc.unity.host:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    host_name: "ansible-test-host-2"
    state: "absent"

- name: Add network address to Host
  dellemc.unity.host:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    host_name: "{{host_name}}"
    network_address: "192.168.1.2"
    network_address_state: "present-in-host"
    state: "present"

- name: Delete network address from Host
  dellemc.unity.host:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    host_name: "{{host_name}}"
    network_address: "192.168.1.2"
    network_address_state: "absent-in-host"
    state: "present"
```

## [Return Values](host_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether or not the resource has changed.  **Returned:** always  **Sample:** `true` |
| **host_details**  dictionary | Details of the host.  **Returned:** When host exists.  **Sample:** `{"auto_manage_type": "HostManageEnum.UNKNOWN", "datastores": null, "description": "ansible-test-host-1", "existed": true, "fc_host_initiators": [{"id": "HostInitiator_1", "name": "HostName_1", "paths": [{"id": "HostInitiator_1_Id1", "is_logged_in": true}, {"id": "HostInitiator_1_Id2", "is_logged_in": true}]}], "hash": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER", "health": {"UnityHealth": {"hash": 8764429420954}}, "host_container": null, "host_luns": [], "host_polled_uuid": null, "host_pushed_uuid": null, "host_uuid": null, "host_v_vol_datastore": null, "id": "Host_2198", "iscsi_host_initiators": [{"id": "HostInitiator_2", "name": "HostName_2", "paths": [{"id": "HostInitiator_2_Id1", "is_logged_in": true}, {"id": "HostInitiator_2_Id2", "is_logged_in": true}]}], "last_poll_time": null, "name": "ansible-test-host-1", "network_addresses": [], "os_type": "Linux", "registration_type": null, "storage_resources": null, "tenant": null, "type": "HostTypeEnum.HOST_MANUAL", "vms": null}` |
| **description**  string | Description about the host.  **Returned:** success |
| **fc_host_initiators**  list / elements=string | Details of the FC initiators associated with the host.  **Returned:** success |
| **id**  string | Unique identifier of the FC initiator path.  **Returned:** success |
| **name**  string | FC Qualified Name (WWN) of the initiator.  **Returned:** success |
| **paths**  list / elements=string | Details of the paths associated with the FC initiator.  **Returned:** success |
| **id**  string | Unique identifier of the path.  **Returned:** success |
| **is_logged_in**  boolean | Indicates whether the host initiator is logged into the storage system.  **Returned:** success |
| **host_luns**  list / elements=string | Details of luns attached to host.  **Returned:** success |
| **id**  string | The system ID given to the host.  **Returned:** success |
| **iscsi_host_initiators**  list / elements=string | Details of the ISCSI initiators associated with the host.  **Returned:** success |
| **id**  string | Unique identifier of the ISCSI initiator path.  **Returned:** success |
| **name**  string | ISCSI Qualified Name (IQN) of the initiator.  **Returned:** success |
| **paths**  list / elements=string | Details of the paths associated with the ISCSI initiator.  **Returned:** success |
| **id**  string | Unique identifier of the path.  **Returned:** success |
| **is_logged_in**  boolean | Indicates whether the host initiator is logged into the storage system.  **Returned:** success |
| **name**  string | The name of the host.  **Returned:** success |
| **network_addresses**  list / elements=string | List of network addresses mapped to the host.  **Returned:** success |
| **os_type**  string | Operating system running on the host.  **Returned:** success |
| **type**  string | HostTypeEnum of the host.  **Returned:** success |

### Authors

- Rajshree Khare (@kharer5)

### Collection links

- [Issue Tracker](https://www.dell.com/community/Automation/bd-p/Automation)
- [Repository (Sources)](https://github.com/dell/ansible-unity/tree/1.7.1)
