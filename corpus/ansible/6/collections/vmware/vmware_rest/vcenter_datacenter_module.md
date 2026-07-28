---
collection: ansible
version: "6"
title: "vmware.vmware_rest.vcenter_datacenter module – Create a new datacenter in the vCenter inventory"
source_url: https://docs.ansible.com/projects/ansible/6/collections/vmware/vmware_rest/vcenter_datacenter_module.html
fetched_at: 2026-07-28T00:22:06+00:00
---
# vmware.vmware_rest.vcenter_datacenter module – Create a new datacenter in the vCenter inventory

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
> see [Requirements](vcenter_datacenter_module.md#ansible-collections-vmware-vmware-rest-vcenter-datacenter-module-requirements) for details.
>
> To use it in a playbook, specify: `vmware.vmware_rest.vcenter_datacenter`.

New in vmware.vmware_rest 0.1.0

- [Synopsis](vcenter_datacenter_module.md#synopsis)
- [Requirements](vcenter_datacenter_module.md#requirements)
- [Parameters](vcenter_datacenter_module.md#parameters)
- [Notes](vcenter_datacenter_module.md#notes)
- [Examples](vcenter_datacenter_module.md#examples)
- [Return Values](vcenter_datacenter_module.md#return-values)

## [Synopsis](vcenter_datacenter_module.md#id1)

- Create a new datacenter in the vCenter inventory

## [Requirements](vcenter_datacenter_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp

## [Parameters](vcenter_datacenter_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **datacenter**  string | Identifier of the datacenter to be deleted. Required with *state=[‘absent’]* |
| **folder**  string | Datacenter folder in which the new datacenter should be created. |
| **force**  boolean | If true, delete the datacenter even if it is not empty.  Choices:   - `false` - `true` |
| **name**  string | The name of the datacenter to be created. Required with *state=[‘present’]* |
| **session_timeout**  float  added in vmware.vmware_rest 2.1.0 | Timeout settings for client session.  The maximal number of seconds for the whole operation including connection establishment, request sending and response.  The default value is 300s. |
| **state**  string | Choices:   - `"absent"` - `"present"` ← (default) |
| **vcenter_hostname**  string / required | The hostname or IP address of the vSphere vCenter  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **vcenter_password**  string / required | The vSphere vCenter password  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **vcenter_rest_log_file**  string | You can use this optional parameter to set the location of a log file.  This file will be used to record the HTTP REST interaction.  The file will be stored on the host that run the module.  If the value is not specified in the task, the value of  environment variable `VMWARE_REST_LOG_FILE` will be used instead. |
| **vcenter_username**  string / required | The vSphere vCenter username  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **vcenter_validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Notes](vcenter_datacenter_module.md#id4)

> **Note:**
>
> - Tested on vSphere 7.0.2

## [Examples](vcenter_datacenter_module.md#id5)

```yaml+jinja
- name: Get a list of all the datacenters
  register: existing_datacenters
  vmware.vmware_rest.vcenter_datacenter_info:

- name: Force delete the existing DC
  vmware.vmware_rest.vcenter_datacenter:
    state: absent
    datacenter: '{{ item.datacenter }}'
    force: true
  with_items: '{{ existing_datacenters.value }}'
  until:
  - _result is not failed
  retries: 7

- name: Create datacenter my_dc
  vmware.vmware_rest.vcenter_datacenter:
    name: my_dc
    folder: '{{ my_datacenter_folder.folder }}'
```

## [Return Values](vcenter_datacenter_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Force delete the existing DC  Returned: On success  Sample: `"All items completed"` |
| **results**  list / elements=string | Force delete the existing DC  Returned: On success  Sample: `[{"_ansible_item_label": {"datacenter": "datacenter-1107", "name": "my_dc"}, "_ansible_no_log": null, "ansible_loop_var": "item", "attempts": 1, "changed": 1, "failed": 0, "invocation": {"module_args": {"datacenter": "datacenter-1107", "folder": null, "force": 1, "name": null, "session_timeout": null, "state": "absent", "vcenter_hostname": "vcenter.test", "vcenter_password": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER", "vcenter_rest_log_file": null, "vcenter_username": "administrator@vsphere.local", "vcenter_validate_certs": 0}}, "item": {"datacenter": "datacenter-1107", "name": "my_dc"}, "value": {}}]` |

### Authors

- Ansible Cloud Team (@ansible-collections)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/vmware.vmware_rest/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/vmware.vmware_rest)
[Repository (Sources)](https://github.com/ansible-collections/vmware.vmware_rest.git)
