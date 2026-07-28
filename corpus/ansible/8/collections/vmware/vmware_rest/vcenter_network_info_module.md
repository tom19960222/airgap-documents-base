---
collection: ansible
version: "8"
title: "vmware.vmware_rest.vcenter_network_info module – Returns information about at most 1000 visible (subject to permission checks) networks in vCenter matching the { @ link FilterSpec}."
source_url: https://docs.ansible.com/projects/ansible/8/collections/vmware/vmware_rest/vcenter_network_info_module.html
fetched_at: 2026-07-28T02:57:54+00:00
---
# vmware.vmware_rest.vcenter_network_info module – Returns information about at most 1000 visible (subject to permission checks) networks in vCenter matching the [{@link](mailto:{%40link) FilterSpec}.

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
> see [Requirements](vcenter_network_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-network-info-module-requirements) for details.
>
> To use it in a playbook, specify: `vmware.vmware_rest.vcenter_network_info`.

New in vmware.vmware_rest 0.1.0

- [Synopsis](vcenter_network_info_module.md#synopsis)
- [Requirements](vcenter_network_info_module.md#requirements)
- [Parameters](vcenter_network_info_module.md#parameters)
- [Notes](vcenter_network_info_module.md#notes)
- [Examples](vcenter_network_info_module.md#examples)
- [Return Values](vcenter_network_info_module.md#return-values)

## [Synopsis](vcenter_network_info_module.md#id1)

- Returns information about at most 1000 visible (subject to permission checks) networks in vCenter matching the [{@link](mailto:{%40link) FilterSpec}.

## [Requirements](vcenter_network_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp

## [Parameters](vcenter_network_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **datacenters**  aliases: filter_datacenters  list / elements=string | Datacenters that must contain the network for the network to match the filter. |
| **folders**  aliases: filter_folders  list / elements=string | Folders that must contain the network for the network to match the filter. |
| **names**  aliases: filter_names  list / elements=string | Names that networks must have to match the filter (see [{@link](mailto:{%40link) Summary#name}). |
| **networks**  list / elements=string | Identifiers of networks that can match the filter. |
| **session_timeout**  float  *added in vmware.vmware_rest 2.1.0* | Timeout settings for client session.  The maximal number of seconds for the whole operation including connection establishment, request sending and response.  The default value is 300s. |
| **types**  aliases: filter_types  list / elements=string | Types that networks must have to match the filter (see [{@link](mailto:{%40link) Summary#type}). |
| **vcenter_hostname**  string / required | The hostname or IP address of the vSphere vCenter  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **vcenter_password**  string / required | The vSphere vCenter password  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **vcenter_rest_log_file**  string | You can use this optional parameter to set the location of a log file.  This file will be used to record the HTTP REST interaction.  The file will be stored on the host that run the module.  If the value is not specified in the task, the value of  environment variable `VMWARE_REST_LOG_FILE` will be used instead. |
| **vcenter_username**  string / required | The vSphere vCenter username  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **vcenter_validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vcenter_network_info_module.md#id4)

> **Note:**
>
> - Tested on vSphere 7.0.2

## [Examples](vcenter_network_info_module.md#id5)

```yaml+jinja
- name: Get the dvswitch called my-portgroup
  vmware.vmware_rest.vcenter_network_info:
    filter_types: DISTRIBUTED_PORTGROUP
    filter_names: my portrgoup
  register: my_portgroup
```

## [Return Values](vcenter_network_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **value**  list / elements=string | Get a list of the networks  **Returned:** On success  **Sample:** `[{"name": "VM Network", "network": "network-1016", "type": "STANDARD_PORTGROUP"}, {"name": "second_vswitch", "network": "network-1018", "type": "STANDARD_PORTGROUP"}, {"name": "dvswitch1-DVUplinks-1020", "network": "dvportgroup-1021", "type": "DISTRIBUTED_PORTGROUP"}, {"name": "my portrgoup", "network": "dvportgroup-1022", "type": "DISTRIBUTED_PORTGROUP"}]` |

### Authors

- Ansible Cloud Team (@ansible-collections)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vmware.vmware_rest/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/vmware.vmware_rest)
- [Repository (Sources)](https://github.com/ansible-collections/vmware.vmware_rest.git)
