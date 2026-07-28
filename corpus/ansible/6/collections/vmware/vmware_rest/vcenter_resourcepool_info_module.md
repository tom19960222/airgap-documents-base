---
collection: ansible
version: "6"
title: "vmware.vmware_rest.vcenter_resourcepool_info module – Retrieves information about the resource pool indicated by { @ param . name resourcePool}."
source_url: https://docs.ansible.com/projects/ansible/6/collections/vmware/vmware_rest/vcenter_resourcepool_info_module.html
fetched_at: 2026-07-28T00:22:12+00:00
---
# vmware.vmware_rest.vcenter_resourcepool_info module – Retrieves information about the resource pool indicated by [{@param.name](mailto:{%40param.name) resourcePool}.

> **Note:**
>
> This module is part of the [vmware.vmware_rest collection](https://galaxy.ansible.com/vmware/vmware_rest) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vmware.vmware_rest`.
> You need further requirements to be able to use this module,
> see [Requirements](vcenter_resourcepool_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-resourcepool-info-module-requirements) for details.
>
> To use it in a playbook, specify: `vmware.vmware_rest.vcenter_resourcepool_info`.

New in vmware.vmware_rest 0.3.0

- [Synopsis](vcenter_resourcepool_info_module.md#synopsis)
- [Requirements](vcenter_resourcepool_info_module.md#requirements)
- [Parameters](vcenter_resourcepool_info_module.md#parameters)
- [Notes](vcenter_resourcepool_info_module.md#notes)
- [Examples](vcenter_resourcepool_info_module.md#examples)
- [Return Values](vcenter_resourcepool_info_module.md#return-values)

## [Synopsis](vcenter_resourcepool_info_module.md#id1)

- Retrieves information about the resource pool indicated by [{@param.name](mailto:{%40param.name) resourcePool}.

## [Requirements](vcenter_resourcepool_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp

## [Parameters](vcenter_resourcepool_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **clusters**  list / elements=string | Clusters that must contain the resource pool for the resource pool to match the filter. |
| **datacenters**  aliases: filter_datacenters  list / elements=string | Datacenters that must contain the resource pool for the resource pool to match the filter. |
| **hosts**  list / elements=string | Hosts that must contain the resource pool for the resource pool to match the filter. |
| **names**  aliases: filter_names  list / elements=string | Names that resource pools must have to match the filter (see [{@link](mailto:{%40link) Info#name}). |
| **parent_resource_pools**  list / elements=string | Resource pools that must contain the resource pool for the resource pool to match the filter. |
| **resource_pool**  string | Identifier of the resource pool for which information should be retrieved. Required with *state=[‘get’]* |
| **resource_pools**  list / elements=string | Identifiers of resource pools that can match the filter. |
| **session_timeout**  float  added in vmware.vmware_rest 2.1.0 | Timeout settings for client session.  The maximal number of seconds for the whole operation including connection establishment, request sending and response.  The default value is 300s. |
| **vcenter_hostname**  string / required | The hostname or IP address of the vSphere vCenter  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **vcenter_password**  string / required | The vSphere vCenter password  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **vcenter_rest_log_file**  string | You can use this optional parameter to set the location of a log file.  This file will be used to record the HTTP REST interaction.  The file will be stored on the host that run the module.  If the value is not specified in the task, the value of  environment variable `VMWARE_REST_LOG_FILE` will be used instead. |
| **vcenter_username**  string / required | The vSphere vCenter username  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **vcenter_validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Notes](vcenter_resourcepool_info_module.md#id4)

> **Note:**
>
> - Tested on vSphere 7.0.2

## [Examples](vcenter_resourcepool_info_module.md#id5)

```yaml+jinja
- name: Get the existing resource pools
  vmware.vmware_rest.vcenter_resourcepool_info:
  register: resource_pools

- name: Get the existing resource pool
  vmware.vmware_rest.vcenter_resourcepool_info:
    resource_pool: '{{ resource_pools.value[0].resource_pool }}'
  register: my_resource_pool

- name: Create a generic resource pool
  vmware.vmware_rest.vcenter_resourcepool:
    name: my_resource_pool
    parent: '{{ resource_pools.value[0].resource_pool }}'
  register: my_resource_pool

- name: Read details from a specific resource pool
  vmware.vmware_rest.vcenter_resourcepool_info:
    resource_pool: '{{ my_resource_pool.id }}'
  register: my_resource_pool
```

## [Return Values](vcenter_resourcepool_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | moid of the resource  Returned: On success  Sample: `"resgroup-1143"` |
| **value**  dictionary | Read details from a specific resource pool  Returned: On success  Sample: `{"cpu_allocation": {"expandable_reservation": 1, "limit": -1, "reservation": 0, "shares": {"level": "NORMAL"}}, "memory_allocation": {"expandable_reservation": 0, "limit": 1000, "reservation": 0, "shares": {"level": "NORMAL"}}, "name": "my_resource_pool", "resource_pools": []}` |

### Authors

- Ansible Cloud Team (@ansible-collections)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/vmware.vmware_rest/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/vmware.vmware_rest)
[Repository (Sources)](https://github.com/ansible-collections/vmware.vmware_rest.git)
