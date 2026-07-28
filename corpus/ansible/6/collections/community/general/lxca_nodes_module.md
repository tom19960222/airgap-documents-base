---
collection: ansible
version: "6"
title: "community.general.lxca_nodes module – Custom module for lxca nodes inventory utility"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/lxca_nodes_module.html
fetched_at: 2026-07-27T17:10:40+00:00
---
# community.general.lxca_nodes module – Custom module for lxca nodes inventory utility

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](lxca_nodes_module.md#ansible-collections-community-general-lxca-nodes-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.lxca_nodes`.

- [Synopsis](lxca_nodes_module.md#synopsis)
- [Requirements](lxca_nodes_module.md#requirements)
- [Parameters](lxca_nodes_module.md#parameters)
- [Notes](lxca_nodes_module.md#notes)
- [Examples](lxca_nodes_module.md#examples)
- [Return Values](lxca_nodes_module.md#return-values)

## [Synopsis](lxca_nodes_module.md#id1)

- This module returns/displays a inventory details of nodes

## [Requirements](lxca_nodes_module.md#id2)

The below requirements are needed on the host that executes this module.

- pylxca

## [Parameters](lxca_nodes_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_url**  string / required | lxca https full web address |
| **chassis**  string | uuid of chassis, this is string with length greater than 16. |
| **command_options**  string | options to filter nodes information  Choices:   - `"nodes"` ← (default) - `"nodes_by_uuid"` - `"nodes_by_chassis_uuid"` - `"nodes_status_managed"` - `"nodes_status_unmanaged"` |
| **login_password**  string / required | The password for use in HTTP basic authentication. |
| **login_user**  string / required | The username for use in HTTP basic authentication. |
| **uuid**  string | uuid of device, this is string with length greater than 16. |

## [Notes](lxca_nodes_module.md#id4)

> **Note:**
>
> - Additional detail about pylxca can be found at <https://github.com/lenovo/pylxca>
> - Playbooks using these modules can be found at <https://github.com/lenovo/ansible.lenovo-lxca>
> - Check mode is not supported.

## [Examples](lxca_nodes_module.md#id5)

```yaml+jinja
# get all nodes info
- name: Get nodes data from LXCA
  community.general.lxca_nodes:
    login_user: USERID
    login_password: Password
    auth_url: "https://10.243.15.168"
    command_options: nodes

# get specific nodes info by uuid
- name: Get nodes data from LXCA
  community.general.lxca_nodes:
    login_user: USERID
    login_password: Password
    auth_url: "https://10.243.15.168"
    uuid: "3C737AA5E31640CE949B10C129A8B01F"
    command_options: nodes_by_uuid

# get specific nodes info by chassis uuid
- name: Get nodes data from LXCA
  community.general.lxca_nodes:
    login_user: USERID
    login_password: Password
    auth_url: "https://10.243.15.168"
    chassis: "3C737AA5E31640CE949B10C129A8B01F"
    command_options: nodes_by_chassis_uuid

# get managed nodes
- name: Get nodes data from LXCA
  community.general.lxca_nodes:
    login_user: USERID
    login_password: Password
    auth_url: "https://10.243.15.168"
    command_options: nodes_status_managed

# get unmanaged nodes
- name: Get nodes data from LXCA
  community.general.lxca_nodes:
    login_user: USERID
    login_password: Password
    auth_url: "https://10.243.15.168"
    command_options: nodes_status_unmanaged
```

## [Return Values](lxca_nodes_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  dictionary | nodes detail from lxca  Returned: always  Sample: `{"nodeList": [{"machineType": "6241", "model": "AC1", "type": "Rack-TowerServer", "uuid": "118D2C88C8FD11E4947B6EAE8B4BDCDF"}, {"machineType": "8871", "model": "AC1", "type": "Rack-TowerServer", "uuid": "223D2C88C8FD11E4947B6EAE8B4BDCDF"}]}` |

### Authors

- Naval Patel (@navalkp)
- Prashant Bhosale (@prabhosa)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
