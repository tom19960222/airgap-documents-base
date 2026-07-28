---
collection: ansible
version: "8"
title: "vmware.vmware_rest.vcenter_resourcepool module – Creates a resource pool."
source_url: https://docs.ansible.com/projects/ansible/8/collections/vmware/vmware_rest/vcenter_resourcepool_module.html
fetched_at: 2026-07-28T02:57:55+00:00
---
# vmware.vmware_rest.vcenter_resourcepool module – Creates a resource pool.

> **Note:**
>
> This module is part of the [vmware.vmware_rest collection](https://galaxy.ansible.com/ui/repo/published/vmware/vmware_rest/) (version 2.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vmware.vmware_rest`.
> You need further requirements to be able to use this module,
> see [Requirements](vcenter_resourcepool_module.md#ansible-collections-vmware-vmware-rest-vcenter-resourcepool-module-requirements) for details.
>
> To use it in a playbook, specify: `vmware.vmware_rest.vcenter_resourcepool`.

New in vmware.vmware_rest 0.3.0

- [Synopsis](vcenter_resourcepool_module.md#synopsis)
- [Requirements](vcenter_resourcepool_module.md#requirements)
- [Parameters](vcenter_resourcepool_module.md#parameters)
- [Notes](vcenter_resourcepool_module.md#notes)
- [Examples](vcenter_resourcepool_module.md#examples)
- [Return Values](vcenter_resourcepool_module.md#return-values)

## [Synopsis](vcenter_resourcepool_module.md#id1)

- Creates a resource pool.

## [Requirements](vcenter_resourcepool_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp

## [Parameters](vcenter_resourcepool_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cpu_allocation**  dictionary | Resource allocation for CPU.  Valid attributes are:  - `reservation` (int): Amount of resource that is guaranteed available to a resource pool. Reserved resources are not wasted if they are not used. If the utilization is less than the reservation, the resources can be utilized by other running virtual machines. Units are MB fo memory, and MHz for CPU. ([‘present’]) - `expandable_reservation` (bool): In a resource pool with an expandable reservation, the reservation can grow beyond the specified value, if the parent resource pool has unreserved resources. A non-expandable reservation is called a fixed reservation. ([‘present’]) - `limit` (int): The utilization of a resource pool will not exceed this limit, even if there are available resources. This is typically used to ensure a consistent performance of resource pools independent of available resources. If set to -1, then there is no fixed limit on resource usage (only bounded by available resources and shares). Units are MB for memory, and MHz for CPU. ([‘present’]) - `shares` (dict): Shares are used in case of resource contention. ([‘present’])    - Accepted keys:      - level (string): The `level` defines the possible values for the allocation level.  Accepted value for this field:  - `CUSTOM` - `HIGH` - `LOW` - `NORMAL`   - shares (integer): When [{@link](mailto:{%40link) #level} is set to CUSTOM, it is the number of shares allocated. Otherwise, this value is ignored. There is no unit for this value. It is a relative measure based on the settings for other resource pools. |
| **memory_allocation**  dictionary | Resource allocation for CPU.  Valid attributes are:  - `reservation` (int): Amount of resource that is guaranteed available to a resource pool. Reserved resources are not wasted if they are not used. If the utilization is less than the reservation, the resources can be utilized by other running virtual machines. Units are MB fo memory, and MHz for CPU. ([‘present’]) - `expandable_reservation` (bool): In a resource pool with an expandable reservation, the reservation can grow beyond the specified value, if the parent resource pool has unreserved resources. A non-expandable reservation is called a fixed reservation. ([‘present’]) - `limit` (int): The utilization of a resource pool will not exceed this limit, even if there are available resources. This is typically used to ensure a consistent performance of resource pools independent of available resources. If set to -1, then there is no fixed limit on resource usage (only bounded by available resources and shares). Units are MB for memory, and MHz for CPU. ([‘present’]) - `shares` (dict): Shares are used in case of resource contention. ([‘present’])    - Accepted keys:      - level (string): The `level` defines the possible values for the allocation level.  Accepted value for this field:  - `CUSTOM` - `HIGH` - `LOW` - `NORMAL`   - shares (integer): When [{@link](mailto:{%40link) #level} is set to CUSTOM, it is the number of shares allocated. Otherwise, this value is ignored. There is no unit for this value. It is a relative measure based on the settings for other resource pools. |
| **name**  string | Name of the resource pool. Required with *state=[‘present’]* |
| **parent**  string | Parent of the created resource pool. Required with *state=[‘present’]* |
| **resource_pool**  string | Identifier of the resource pool to be deleted. Required with *state=[‘absent’, ‘present’]* |
| **session_timeout**  float  *added in vmware.vmware_rest 2.1.0* | Timeout settings for client session.  The maximal number of seconds for the whole operation including connection establishment, request sending and response.  The default value is 300s. |
| **state**  string | **Choices:**   - `"absent"` - `"present"` ← (default) |
| **vcenter_hostname**  string / required | The hostname or IP address of the vSphere vCenter  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **vcenter_password**  string / required | The vSphere vCenter password  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **vcenter_rest_log_file**  string | You can use this optional parameter to set the location of a log file.  This file will be used to record the HTTP REST interaction.  The file will be stored on the host that run the module.  If the value is not specified in the task, the value of  environment variable `VMWARE_REST_LOG_FILE` will be used instead. |
| **vcenter_username**  string / required | The vSphere vCenter username  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **vcenter_validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vcenter_resourcepool_module.md#id4)

> **Note:**
>
> - Tested on vSphere 7.0.2

## [Examples](vcenter_resourcepool_module.md#id5)

```yaml+jinja
- name: Get the existing resource pools
  vmware.vmware_rest.vcenter_resourcepool_info:
  register: resource_pools

- name: Create an Ad hoc resource pool
  vmware.vmware_rest.vcenter_resourcepool:
    name: my_resource_pool
    parent: '{{ resource_pools.value[0].resource_pool }}'
    cpu_allocation:
      expandable_reservation: true
      limit: 40
      reservation: 0
      shares:
        level: NORMAL
    memory_allocation:
      expandable_reservation: false
      limit: 2000
      reservation: 0
      shares:
        level: NORMAL
  register: my_resource_pool

- name: Remove a resource pool
  vmware.vmware_rest.vcenter_resourcepool:
    resource_pool: '{{ my_resource_pool.id }}'
    state: absent

- name: Create a generic resource pool
  vmware.vmware_rest.vcenter_resourcepool:
    name: my_resource_pool
    parent: '{{ resource_pools.value[0].resource_pool }}'
  register: my_resource_pool

- name: Modify a resource pool
  vmware.vmware_rest.vcenter_resourcepool:
    resource_pool: '{{ my_resource_pool.id }}'
    cpu_allocation:
      expandable_reservation: true
      limit: -1
      reservation: 0
      shares:
        level: NORMAL
    memory_allocation:
      expandable_reservation: false
      limit: 1000
      reservation: 0
      shares:
        level: NORMAL
```

## [Return Values](vcenter_resourcepool_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | moid of the resource  **Returned:** On success  **Sample:** `"resgroup-1009"` |
| **value**  dictionary | Create a generic resource pool  **Returned:** On success  **Sample:** `{"cpu_allocation": {"expandable_reservation": 1, "limit": -1, "reservation": 0, "shares": {"level": "NORMAL"}}, "memory_allocation": {"expandable_reservation": 1, "limit": -1, "reservation": 0, "shares": {"level": "NORMAL"}}, "name": "my_resource_pool", "resource_pools": []}` |

### Authors

- Ansible Cloud Team (@ansible-collections)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vmware.vmware_rest/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/vmware.vmware_rest)
- [Repository (Sources)](https://github.com/ansible-collections/vmware.vmware_rest.git)
