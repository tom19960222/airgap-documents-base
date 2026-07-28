---
collection: ansible
version: "8"
title: "community.general.lxca_cmms module – Custom module for lxca cmms inventory utility"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/lxca_cmms_module.html
fetched_at: 2026-07-28T01:47:39+00:00
---
# community.general.lxca_cmms module – Custom module for lxca cmms inventory utility

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](lxca_cmms_module.md#ansible-collections-community-general-lxca-cmms-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.lxca_cmms`.

- [Synopsis](lxca_cmms_module.md#synopsis)
- [Requirements](lxca_cmms_module.md#requirements)
- [Parameters](lxca_cmms_module.md#parameters)
- [Attributes](lxca_cmms_module.md#attributes)
- [Notes](lxca_cmms_module.md#notes)
- [Examples](lxca_cmms_module.md#examples)
- [Return Values](lxca_cmms_module.md#return-values)

## [Synopsis](lxca_cmms_module.md#id1)

- This module returns/displays a inventory details of cmms

Aliases: remote_management.lxca.lxca_cmms

## [Requirements](lxca_cmms_module.md#id2)

The below requirements are needed on the host that executes this module.

- pylxca

## [Parameters](lxca_cmms_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_url**  string / required | lxca https full web address |
| **chassis**  string | uuid of chassis, this is string with length greater than 16. |
| **command_options**  string | options to filter nodes information  **Choices:**   - `"cmms"` ← (default) - `"cmms_by_uuid"` - `"cmms_by_chassis_uuid"` |
| **login_password**  string / required | The password for use in HTTP basic authentication. |
| **login_user**  string / required | The username for use in HTTP basic authentication. |
| **uuid**  string | uuid of device, this is string with length greater than 16. |

## [Attributes](lxca_cmms_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](lxca_cmms_module.md#id5)

> **Note:**
>
> - Additional detail about pylxca can be found at <https://github.com/lenovo/pylxca>
> - Playbooks using these modules can be found at <https://github.com/lenovo/ansible.lenovo-lxca>
> - Check mode is not supported.

## [Examples](lxca_cmms_module.md#id6)

```yaml+jinja
# get all cmms info
- name: Get nodes data from LXCA
  community.general.lxca_cmms:
    login_user: USERID
    login_password: Password
    auth_url: "https://10.243.15.168"

# get specific cmms info by uuid
- name: Get nodes data from LXCA
  community.general.lxca_cmms:
    login_user: USERID
    login_password: Password
    auth_url: "https://10.243.15.168"
    uuid: "3C737AA5E31640CE949B10C129A8B01F"
    command_options: cmms_by_uuid

# get specific cmms info by chassis uuid
- name: Get nodes data from LXCA
  community.general.lxca_cmms:
    login_user: USERID
    login_password: Password
    auth_url: "https://10.243.15.168"
    chassis: "3C737AA5E31640CE949B10C129A8B01F"
    command_options: cmms_by_chassis_uuid
```

## [Return Values](lxca_cmms_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  dictionary | cmms detail from lxca  **Returned:** success  **Sample:** `{"cmmList": [{"machineType": "", "model": "", "type": "CMM", "uuid": "118D2C88C8FD11E4947B6EAE8B4BDCDF"}, {"machineType": "", "model": "", "type": "CMM", "uuid": "223D2C88C8FD11E4947B6EAE8B4BDCDF"}]}` |

### Authors

- Naval Patel (@navalkp)
- Prashant Bhosale (@prabhosa)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
