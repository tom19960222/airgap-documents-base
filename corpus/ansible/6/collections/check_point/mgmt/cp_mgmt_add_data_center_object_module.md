---
collection: ansible
version: "6"
title: "check_point.mgmt.cp_mgmt_add_data_center_object module – Imports a Data Center Object from a Data Center Server.<br> Data Center Object represents an object in the cloud environment."
source_url: https://docs.ansible.com/projects/ansible/6/collections/check_point/mgmt/cp_mgmt_add_data_center_object_module.html
fetched_at: 2026-07-27T16:47:36+00:00
---
# check_point.mgmt.cp_mgmt_add_data_center_object module – Imports a Data Center Object from a Data Center Server.<br> Data Center Object represents an object in the cloud environment.

> **Note:**
>
> This module is part of the [check_point.mgmt collection](https://galaxy.ansible.com/check_point/mgmt) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install check_point.mgmt`.
>
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_add_data_center_object`.

New in check_point.mgmt 2.9

- [Synopsis](cp_mgmt_add_data_center_object_module.md#synopsis)
- [Parameters](cp_mgmt_add_data_center_object_module.md#parameters)
- [Examples](cp_mgmt_add_data_center_object_module.md#examples)
- [Return Values](cp_mgmt_add_data_center_object_module.md#return-values)

## [Synopsis](cp_mgmt_add_data_center_object_module.md#id1)

- Imports a Data Center Object from a Data Center Server.<br> Data Center Object represents an object in the cloud environment, e.g. a virtual machine, cluster, network and more.<br> Use the show-data-center-content command to see the Data Center Objects that can be imported from a Data Center Server.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_add_data_center_object_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **color**  string | Color of the object. Should be one of existing colors.  Choices:   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **data_center_name**  string | Name of the Data Center Server the object is in. |
| **data_center_uid**  string | Unique identifier of the Data Center Server the object is in. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  Choices:   - `"uid"` - `"standard"` - `"full"` |
| **groups**  list / elements=string | Collection of group identifiers. |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  Choices:   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  Choices:   - `false` - `true` |
| **name**  string | Override default name on data-center. |
| **tags**  list / elements=string | Collection of tag identifiers. |
| **uid_in_data_center**  string | Unique identifier of the object in the Data Center Server. |
| **uri**  string | URI of the object in the Data Center Server. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  Choices:   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  Default: `30` |

## [Examples](cp_mgmt_add_data_center_object_module.md#id3)

```yaml+jinja
- name: add-data-center-object
  cp_mgmt_add_data_center_object:
    data_center_name: vCenter 1
    name: VM1 mgmt name
    state: present
    uri: /Datacenters/VMs/My VM1
```

## [Return Values](cp_mgmt_add_data_center_object_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_add_data_center_object**  dictionary | The checkpoint add-data-center-object output.  Returned: always. |

### Authors

- Or Soffer (@chkp-orso)

### Collection links

[Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
[Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
