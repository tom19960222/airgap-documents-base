---
collection: ansible
version: "8"
title: "dellemc.powerflex.mdm_cluster module – Manage MDM cluster on Dell PowerFlex"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/powerflex/mdm_cluster_module.html
fetched_at: 2026-07-28T02:05:10+00:00
---
# dellemc.powerflex.mdm_cluster module – Manage MDM cluster on Dell PowerFlex

> **Note:**
>
> This module is part of the [dellemc.powerflex collection](https://galaxy.ansible.com/ui/repo/published/dellemc/powerflex/) (version 1.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.powerflex`.
> You need further requirements to be able to use this module,
> see [Requirements](mdm_cluster_module.md#ansible-collections-dellemc-powerflex-mdm-cluster-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.powerflex.mdm_cluster`.

New in dellemc.powerflex 1.3.0

- [Synopsis](mdm_cluster_module.md#synopsis)
- [Requirements](mdm_cluster_module.md#requirements)
- [Parameters](mdm_cluster_module.md#parameters)
- [Notes](mdm_cluster_module.md#notes)
- [Examples](mdm_cluster_module.md#examples)
- [Return Values](mdm_cluster_module.md#return-values)

## [Synopsis](mdm_cluster_module.md#id1)

- Managing MDM cluster and MDMs on PowerFlex storage system includes adding/removing standby MDM, modify MDM name and virtual interface.
- It also includes getting details of MDM cluster, modify MDM cluster ownership, cluster mode, and performance profile.

## [Requirements](mdm_cluster_module.md#id2)

The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 3.5 or later.
- Ansible-core 2.13 or later.
- PyPowerFlex 1.8.0.
- Python 3.9, 3.10 or 3.11.

## [Parameters](mdm_cluster_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **clear_interfaces**  boolean | Clear all virtual IP interfaces.  The *clear_interfaces* is mutually exclusive with *virtual_ip_interfaces*.  **Choices:**   - `false` - `true` |
| **cluster_mode**  string | Mode of the cluster.  **Choices:**   - `"OneNode"` - `"ThreeNodes"` - `"FiveNodes"` |
| **hostname**  aliases: gateway_host  string / required | IP or FQDN of the PowerFlex host. |
| **is_primary**  boolean | Set *is_primary* as `true` to change MDM cluster ownership from the current master MDM to different MDM.  Set *is_primary* as `false`, will return MDM cluster details.  New owner MDM must be an MDM with a manager role.  **Choices:**   - `false` - `true` |
| **mdm**  list / elements=dictionary | Specifies parameters to add/remove MDMs to/from the MDM cluster. |
| **mdm_id**  string | ID of MDM that will be added/removed to/from the cluster. |
| **mdm_name**  string | Name of MDM that will be added/removed to/from the cluster. |
| **mdm_type**  string / required | Type of the MDM.  Either *mdm_id* or *mdm_name* must be passed with mdm_type.  **Choices:**   - `"Secondary"` - `"TieBreaker"` |
| **mdm_id**  string | The ID of the MDM.  Mutually exclusive with *mdm_name*. |
| **mdm_name**  string | The name of the MDM. It is unique across the PowerFlex array.  Mutually exclusive with *mdm_id*.  If mdm_name passed in add standby operation, then same name will be assigned to the new standby mdm. |
| **mdm_new_name**  string | To rename the MDM. |
| **mdm_state**  string | Mapping state of MDM.  **Choices:**   - `"present-in-cluster"` - `"absent-in-cluster"` |
| **password**  string / required | The password of the PowerFlex host. |
| **performance_profile**  string | Apply performance profile to cluster MDMs.  **Choices:**   - `"Compact"` - `"HighPerformance"` |
| **port**  integer | Port number through which communication happens with PowerFlex host.  **Default:** `443` |
| **standby_mdm**  dictionary | Specifies add standby MDM parameters. |
| **allow_multiple_ips**  boolean | Allow the added node to have different number of IPs from the primary node.  **Choices:**   - `false` - `true` |
| **management_ips**  list / elements=string | List of management IPs to manage MDM. It can contain IPv4 addresses. |
| **mdm_ips**  list / elements=string / required | List of MDM IPs that will be assigned to new MDM. It can contain IPv4 addresses. |
| **port**  integer | Specifies the port of new MDM. |
| **role**  string / required | Role of new MDM.  **Choices:**   - `"Manager"` - `"TieBreaker"` |
| **virtual_interfaces**  list / elements=string | List of NIC interfaces that will be used for virtual IP addresses. |
| **state**  string / required | State of the MDM cluster.  **Choices:**   - `"present"` - `"absent"` |
| **timeout**  integer | Time after which connection will get terminated.  It is to be mentioned in seconds.  **Default:** `120` |
| **username**  string / required | The username of the PowerFlex host. |
| **validate_certs**  aliases: verifycert  boolean | Boolean variable to specify whether or not to validate SSL certificate.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |
| **virtual_ip_interfaces**  list / elements=string | List of interfaces to be used for virtual IPs.  The order of interfaces must be matched with virtual IPs assigned to the cluster.  Interfaces of the primary and secondary type MDMs are allowed to modify.  The *virtual_ip_interfaces* is mutually exclusive with *clear_interfaces*. |

## [Notes](mdm_cluster_module.md#id4)

> **Note:**
>
> - Parameters *mdm_name* or *mdm_id* are mandatory for rename and modify virtual IP interfaces.
> - Parameters *mdm_name* or *mdm_id* are not required while modifying performance profile.
> - For change MDM cluster ownership operation, only changed as true will be returned and for idempotency case MDM cluster details will be returned.
> - Reinstall all SDC after changing ownership to some newly added MDM.
> - To add manager standby MDM, MDM package must be installed with manager role.
> - The *check_mode* is supported.
> - The modules present in the collection named as ‘dellemc.powerflex’ are built to support the Dell PowerFlex storage platform.

## [Examples](mdm_cluster_module.md#id5)

```yaml+jinja
- name: Add a standby MDM
  dellemc.powerflex.mdm_cluster:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    mdm_name: "mdm_1"
    standby_mdm:
      mdm_ips:
        - "10.x.x.x"
      role: "TieBreaker"
      management_ips:
        - "10.x.y.z"
    state: "present"

- name: Remove a standby MDM
  dellemc.powerflex.mdm_cluster:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    mdm_name: "mdm_1"
    state: "absent"

- name: Switch cluster mode from 3 node to 5 node MDM cluster
  dellemc.powerflex.mdm_cluster:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    cluster_mode: "FiveNodes"
    mdm:
      - mdm_id: "5f091a8a013f1100"
        mdm_type: "Secondary"
      - mdm_name: "mdm_1"
        mdm_type: "TieBreaker"
    sdc_state: "present-in-cluster"
    state: "present"

- name: Switch cluster mode from 5 node to 3 node MDM cluster
  dellemc.powerflex.mdm_cluster:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    cluster_mode: "ThreeNodes"
    mdm:
      - mdm_id: "5f091a8a013f1100"
        mdm_type: "Secondary"
      - mdm_name: "mdm_1"
        mdm_type: "TieBreaker"
    sdc_state: "absent-in-cluster"
    state: "present"

- name: Get the details of the MDM cluster
  dellemc.powerflex.mdm_cluster:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    state: "present"

- name: Change ownership of MDM cluster
  dellemc.powerflex.mdm_cluster:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    mdm_name: "mdm_2"
    is_primary: true
    state: "present"

- name: Modify performance profile
  dellemc.powerflex.mdm_cluster:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    performance_profile: "HighPerformance"
    state: "present"

- name: Rename the MDM
  dellemc.powerflex.mdm_cluster:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    mdm_name: "mdm_1"
    mdm_new_name: "new_mdm_1"
    state: "present"

- name: Modify virtual IP interface of the MDM
  dellemc.powerflex.mdm_cluster:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    mdm_name: "mdm_1"
    virtual_ip_interface:
        - "ens224"
    state: "present"

- name: Clear virtual IP interface of the MDM
  dellemc.powerflex.mdm_cluster:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    mdm_name: "mdm_1"
    clear_interfaces: true
    state: "present"
```

## [Return Values](mdm_cluster_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether or not the resource has changed.  **Returned:** always  **Sample:** `false` |
| **mdm_cluster_details**  dictionary | Details of the MDM cluster.  **Returned:** When MDM cluster exists  **Sample:** `{"clusterMode": "ThreeNodes", "clusterState": "ClusteredNormal", "goodNodesNum": 3, "goodReplicasNum": 2, "id": "cdd883cf00000002", "master": {"id": "5908d328581d1400", "ips": ["10.x.y.z"], "managementIPs": ["10.x.y.z"], "name": "sample_mdm", "opensslVersion": "OpenSSL 1.0.2k-fips  26 Jan 2017", "port": 9011, "role": "Manager", "status": "Normal", "versionInfo": "R3_6.0.0", "virtualInterfaces": ["ens1"]}, "perfProfile": "HighPerformance", "slaves": [{"id": "5908d328581d1401", "ips": ["10.x.x.z"], "managementIPs": ["10.x.x.z"], "name": "sample_mdm1", "opensslVersion": "OpenSSL 1.0.2k-fips  26 Jan 2017", "port": 9011, "role": "Manager", "status": "Normal", "versionInfo": "R3_6.0.0", "virtualInterfaces": ["ens1"]}], "standbyMDMs": [{"id": "5908d328581d1403", "ips": ["10.x.z.z"], "managementIPs": ["10.x.z.z"], "opensslVersion": "N/A", "port": 9011, "role": "TieBreaker", "status": "Normal", "versionInfo": "R3_6.0.0", "virtualInterfaces": []}], "tieBreakers": [{"id": "5908d328581d1402", "ips": ["10.x.y.y"], "managementIPs": [], "opensslVersion": "N/A", "port": 9011, "role": "TieBreaker", "status": "Normal", "versionInfo": "R3_6.0.0", "virtualInterfaces": []}]}` |
| **clusterMode**  string | Mode of the MDM cluster.  **Returned:** success |
| **clusterState**  string | State of the MDM cluster.  **Returned:** success |
| **goodNodesNum**  integer | Number of Nodes in MDM cluster.  **Returned:** success |
| **goodReplicasNum**  integer | Number of nodes for Replication.  **Returned:** success |
| **id**  string | The ID of the MDM cluster.  **Returned:** success |
| **master**  dictionary | The details of the master MDM.  **Returned:** success |
| **id**  string | ID of the MDM.  **Returned:** success |
| **ips**  list / elements=string | List of IPs for master MDM.  **Returned:** success |
| **managementIPs**  list / elements=string | List of management IPs for master MDM.  **Returned:** success |
| **name**  string | Name of the MDM.  **Returned:** success |
| **opensslVersion**  string | OpenSSL version.  **Returned:** success |
| **port**  string | Port of the MDM.  **Returned:** success |
| **role**  string | Role of MDM.  **Returned:** success |
| **status**  string | Status of MDM.  **Returned:** success |
| **versionInfo**  string | Version of MDM.  **Returned:** success |
| **virtualInterfaces**  list / elements=string | List of virtual interfaces  **Returned:** success |
| **name**  string | Name of MDM cluster.  **Returned:** success |
| **slaves**  list / elements=dictionary | The list of the secondary MDMs.  **Returned:** success |
| **id**  string | ID of the MDM.  **Returned:** success |
| **ips**  list / elements=string | List of IPs for secondary MDM.  **Returned:** success |
| **managementIPs**  list / elements=string | List of management IPs for secondary MDM.  **Returned:** success |
| **name**  string | Name of the MDM.  **Returned:** success |
| **opensslVersion**  string | OpenSSL version.  **Returned:** success |
| **port**  string | Port of the MDM.  **Returned:** success |
| **role**  string | Role of MDM.  **Returned:** success |
| **status**  string | Status of MDM.  **Returned:** success |
| **versionInfo**  string | Version of MDM.  **Returned:** success |
| **virtualInterfaces**  list / elements=string | List of virtual interfaces  **Returned:** success |
| **standbyMDMs**  list / elements=dictionary | The list of the standby MDMs.  **Returned:** success |
| **id**  string | ID of the MDM.  **Returned:** success |
| **ips**  list / elements=string | List of IPs for MDM.  **Returned:** success |
| **managementIPs**  list / elements=string | List of management IPs for MDM.  **Returned:** success |
| **name**  string | Name of the MDM.  **Returned:** success |
| **opensslVersion**  string | OpenSSL version.  **Returned:** success |
| **port**  string | Port of the MDM.  **Returned:** success |
| **role**  string | Role of MDM.  **Returned:** success |
| **status**  string | Status of MDM.  **Returned:** success |
| **versionInfo**  string | Version of MDM.  **Returned:** success |
| **virtualInterfaces**  list / elements=string | List of virtual interfaces.  **Returned:** success |
| **tieBreakers**  list / elements=dictionary | The list of the TieBreaker MDMs.  **Returned:** success |
| **id**  string | ID of the MDM.  **Returned:** success |
| **ips**  list / elements=string | List of IPs for tie-breaker MDM.  **Returned:** success |
| **managementIPs**  list / elements=string | List of management IPs for tie-breaker MDM.  **Returned:** success |
| **name**  string | Name of the MDM.  **Returned:** success |
| **opensslVersion**  string | OpenSSL version.  **Returned:** success |
| **port**  string | Port of the MDM.  **Returned:** success |
| **role**  string | Role of MDM.  **Returned:** success |
| **status**  string | Status of MDM.  **Returned:** success |
| **versionInfo**  string | Version of MDM.  **Returned:** success |
| **virtualIps**  list / elements=string | List of virtual IPs.  **Returned:** success |

### Authors

- Bhavneet Sharma (@sharmb5)

### Collection links

- [Issue Tracker](https://www.dell.com/community/Automation/bd-p/Automation)
- [Repository (Sources)](https://github.com/dell/ansible-powerflex/tree/1.9.0)
