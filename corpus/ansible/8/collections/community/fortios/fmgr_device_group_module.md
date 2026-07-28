---
collection: ansible
version: "8"
title: "community.fortios.fmgr_device_group module – Alter FortiManager device groups."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/fortios/fmgr_device_group_module.html
fetched_at: 2026-07-28T01:44:08+00:00
---
# community.fortios.fmgr_device_group module – Alter FortiManager device groups.

> **Note:**
>
> This module is part of the [community.fortios collection](https://galaxy.ansible.com/ui/repo/published/community/fortios/) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.fortios`.
>
> To use it in a playbook, specify: `community.fortios.fmgr_device_group`.

- [Synopsis](fmgr_device_group_module.md#synopsis)
- [Parameters](fmgr_device_group_module.md#parameters)
- [Notes](fmgr_device_group_module.md#notes)
- [Examples](fmgr_device_group_module.md#examples)
- [Return Values](fmgr_device_group_module.md#return-values)

## [Synopsis](fmgr_device_group_module.md#id1)

- Add or edit device groups and assign devices to device groups FortiManager Device Manager using JSON RPC API.

## [Parameters](fmgr_device_group_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string | The ADOM the configuration should belong to.  **Default:** `"root"` |
| **grp_desc**  string | The description of the device group. |
| **grp_members**  string | A comma separated list of device names or device groups to be added as members to the device group.  If Group Members are defined, and mode=”delete”, only group members will be removed.  If you want to delete a group itself, you must omit this parameter from the task in playbook. |
| **grp_name**  string | The name of the device group. |
| **mode**  string | Sets one of three modes for managing the object.  Allows use of soft-adds instead of overwriting existing values  **Choices:**   - `"add"` ← (default) - `"set"` - `"delete"` - `"update"` |
| **vdom**  string | The VDOM of the Fortigate you want to add, must match the device in FMGR. Usually root.  **Default:** `"root"` |

## [Notes](fmgr_device_group_module.md#id3)

> **Note:**
>
> - Full Documentation at <https://ftnt-ansible-docs.readthedocs.io/en/latest/>.

## [Examples](fmgr_device_group_module.md#id4)

```yaml+jinja
- name: CREATE DEVICE GROUP
  community.fortios.fmgr_device_group:
    grp_name: "TestGroup"
    grp_desc: "CreatedbyAnsible"
    adom: "ansible"
    mode: "add"

- name: CREATE DEVICE GROUP 2
  community.fortios.fmgr_device_group:
    grp_name: "AnsibleGroup"
    grp_desc: "CreatedbyAnsible"
    adom: "ansible"
    mode: "add"

- name: ADD DEVICES TO DEVICE GROUP
  community.fortios.fmgr_device_group:
    mode: "add"
    grp_name: "TestGroup"
    grp_members: "FGT1,FGT2"
    adom: "ansible"
    vdom: "root"

- name: REMOVE DEVICES TO DEVICE GROUP
  community.fortios.fmgr_device_group:
    mode: "delete"
    grp_name: "TestGroup"
    grp_members: "FGT1,FGT2"
    adom: "ansible"

- name: DELETE DEVICE GROUP
  community.fortios.fmgr_device_group:
    grp_name: "AnsibleGroup"
    grp_desc: "CreatedbyAnsible"
    mode: "delete"
    adom: "ansible"
```

## [Return Values](fmgr_device_group_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_result**  string | full API response, includes status code and message  **Returned:** always |

### Authors

- Luke Weighall (@lweighall)
- Andrew Welsh (@Ghilli3)
- Jim Huber (@p4r4n0y1ng)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.fortios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.fortios)
