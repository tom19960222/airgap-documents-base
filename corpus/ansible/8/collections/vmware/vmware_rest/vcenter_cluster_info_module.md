---
collection: ansible
version: "8"
title: "vmware.vmware_rest.vcenter_cluster_info module – Retrieves information about the cluster corresponding to { @ param . name cluster}."
source_url: https://docs.ansible.com/projects/ansible/8/collections/vmware/vmware_rest/vcenter_cluster_info_module.html
fetched_at: 2026-07-28T02:57:48+00:00
---
# vmware.vmware_rest.vcenter_cluster_info module – Retrieves information about the cluster corresponding to [{@param.name](mailto:{%40param.name) cluster}.

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
> see [Requirements](vcenter_cluster_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-cluster-info-module-requirements) for details.
>
> To use it in a playbook, specify: `vmware.vmware_rest.vcenter_cluster_info`.

New in vmware.vmware_rest 0.1.0

- [Synopsis](vcenter_cluster_info_module.md#synopsis)
- [Requirements](vcenter_cluster_info_module.md#requirements)
- [Parameters](vcenter_cluster_info_module.md#parameters)
- [Notes](vcenter_cluster_info_module.md#notes)
- [Examples](vcenter_cluster_info_module.md#examples)
- [Return Values](vcenter_cluster_info_module.md#return-values)

## [Synopsis](vcenter_cluster_info_module.md#id1)

- Retrieves information about the cluster corresponding to [{@param.name](mailto:{%40param.name) cluster}.

## [Requirements](vcenter_cluster_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp

## [Parameters](vcenter_cluster_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cluster**  string | Identifier of the cluster. Required with *state=[‘get’]* |
| **clusters**  list / elements=string | Identifiers of clusters that can match the filter. |
| **datacenters**  aliases: filter_datacenters  list / elements=string | Datacenters that must contain the cluster for the cluster to match the filter. |
| **folders**  aliases: filter_folders  list / elements=string | Folders that must contain the cluster for the cluster to match the filter. |
| **names**  aliases: filter_names  list / elements=string | Names that clusters must have to match the filter (see [{@link](mailto:{%40link) Info#name}). |
| **session_timeout**  float  *added in vmware.vmware_rest 2.1.0* | Timeout settings for client session.  The maximal number of seconds for the whole operation including connection establishment, request sending and response.  The default value is 300s. |
| **vcenter_hostname**  string / required | The hostname or IP address of the vSphere vCenter  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **vcenter_password**  string / required | The vSphere vCenter password  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **vcenter_rest_log_file**  string | You can use this optional parameter to set the location of a log file.  This file will be used to record the HTTP REST interaction.  The file will be stored on the host that run the module.  If the value is not specified in the task, the value of  environment variable `VMWARE_REST_LOG_FILE` will be used instead. |
| **vcenter_username**  string / required | The vSphere vCenter username  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **vcenter_validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vcenter_cluster_info_module.md#id4)

> **Note:**
>
> - Tested on vSphere 7.0.2

## [Examples](vcenter_cluster_info_module.md#id5)

```yaml+jinja
- name: Build a list of all the clusters
  vmware.vmware_rest.vcenter_cluster_info:
  register: all_the_clusters

- name: Retrieve details about the first cluster
  vmware.vmware_rest.vcenter_cluster_info:
    cluster: '{{ all_the_clusters.value[0].cluster }}'
  register: my_cluster_info
```

## [Return Values](vcenter_cluster_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | moid of the resource  **Returned:** On success  **Sample:** `"domain-c1006"` |
| **value**  dictionary | Retrieve details about the first cluster  **Returned:** On success  **Sample:** `{"name": "my_cluster", "resource_pool": "resgroup-1007"}` |

### Authors

- Ansible Cloud Team (@ansible-collections)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vmware.vmware_rest/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/vmware.vmware_rest)
- [Repository (Sources)](https://github.com/ansible-collections/vmware.vmware_rest.git)
