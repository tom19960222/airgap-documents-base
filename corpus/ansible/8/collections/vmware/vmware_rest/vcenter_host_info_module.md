---
collection: ansible
version: "8"
title: "vmware.vmware_rest.vcenter_host_info module – Returns information about at most 2500 visible (subject to permission checks) hosts in vCenter matching the { @ link FilterSpec}."
source_url: https://docs.ansible.com/projects/ansible/8/collections/vmware/vmware_rest/vcenter_host_info_module.html
fetched_at: 2026-07-28T02:57:53+00:00
---
# vmware.vmware_rest.vcenter_host_info module – Returns information about at most 2500 visible (subject to permission checks) hosts in vCenter matching the [{@link](mailto:{%40link) FilterSpec}.

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
> see [Requirements](vcenter_host_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-host-info-module-requirements) for details.
>
> To use it in a playbook, specify: `vmware.vmware_rest.vcenter_host_info`.

New in vmware.vmware_rest 0.1.0

- [Synopsis](vcenter_host_info_module.md#synopsis)
- [Requirements](vcenter_host_info_module.md#requirements)
- [Parameters](vcenter_host_info_module.md#parameters)
- [Notes](vcenter_host_info_module.md#notes)
- [Examples](vcenter_host_info_module.md#examples)
- [Return Values](vcenter_host_info_module.md#return-values)

## [Synopsis](vcenter_host_info_module.md#id1)

- Returns information about at most 2500 visible (subject to permission checks) hosts in vCenter matching the [{@link](mailto:{%40link) FilterSpec}.

## [Requirements](vcenter_host_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp

## [Parameters](vcenter_host_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **clusters**  list / elements=string | Clusters that must contain the hosts for the hosts to match the filter. |
| **connection_states**  list / elements=string | Connection states that a host must be in to match the filter (see [{@link](mailto:{%40link) Summary#connectionState}. |
| **datacenters**  aliases: filter_datacenters  list / elements=string | Datacenters that must contain the hosts for the hosts to match the filter. |
| **folders**  aliases: filter_folders  list / elements=string | Folders that must contain the hosts for the hosts to match the filter. |
| **hosts**  list / elements=string | Identifiers of hosts that can match the filter. |
| **names**  aliases: filter_names  list / elements=string | Names that hosts must have to match the filter (see [{@link](mailto:{%40link) Summary#name}). |
| **session_timeout**  float  *added in vmware.vmware_rest 2.1.0* | Timeout settings for client session.  The maximal number of seconds for the whole operation including connection establishment, request sending and response.  The default value is 300s. |
| **standalone**  boolean | If true, only hosts that are not part of a cluster can match the filter, and if false, only hosts that are are part of a cluster can match the filter.  **Choices:**   - `false` - `true` |
| **vcenter_hostname**  string / required | The hostname or IP address of the vSphere vCenter  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **vcenter_password**  string / required | The vSphere vCenter password  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **vcenter_rest_log_file**  string | You can use this optional parameter to set the location of a log file.  This file will be used to record the HTTP REST interaction.  The file will be stored on the host that run the module.  If the value is not specified in the task, the value of  environment variable `VMWARE_REST_LOG_FILE` will be used instead. |
| **vcenter_username**  string / required | The vSphere vCenter username  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **vcenter_validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vcenter_host_info_module.md#id4)

> **Note:**
>
> - Tested on vSphere 7.0.2

## [Examples](vcenter_host_info_module.md#id5)

```yaml+jinja
- name: Get a list of the hosts
  vmware.vmware_rest.vcenter_host_info:
  register: my_hosts
```

## [Return Values](vcenter_host_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **value**  list / elements=string | Get a list of the hosts  **Returned:** On success  **Sample:** `[{"connection_state": "CONNECTED", "host": "host-1013", "name": "esxi1.test", "power_state": "POWERED_ON"}]` |

### Authors

- Ansible Cloud Team (@ansible-collections)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vmware.vmware_rest/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/vmware.vmware_rest)
- [Repository (Sources)](https://github.com/ansible-collections/vmware.vmware_rest.git)
