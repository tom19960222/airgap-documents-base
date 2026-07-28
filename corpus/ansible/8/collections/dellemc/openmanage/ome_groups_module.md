---
collection: ansible
version: "8"
title: "dellemc.openmanage.ome_groups module – Manages static device groups on OpenManage Enterprise"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/ome_groups_module.html
fetched_at: 2026-07-28T02:04:39+00:00
---
# dellemc.openmanage.ome_groups module – Manages static device groups on OpenManage Enterprise

> **Note:**
>
> This module is part of the [dellemc.openmanage collection](https://galaxy.ansible.com/ui/repo/published/dellemc/openmanage/) (version 7.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.openmanage`.
> You need further requirements to be able to use this module,
> see [Requirements](ome_groups_module.md#ansible-collections-dellemc-openmanage-ome-groups-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_groups`.

New in dellemc.openmanage 3.5.0

- [Synopsis](ome_groups_module.md#synopsis)
- [Requirements](ome_groups_module.md#requirements)
- [Parameters](ome_groups_module.md#parameters)
- [Notes](ome_groups_module.md#notes)
- [Examples](ome_groups_module.md#examples)
- [Return Values](ome_groups_module.md#return-values)

## [Synopsis](ome_groups_module.md#id1)

- This module allows to create, modify, and delete static device groups on OpenManage Enterprise.

## [Requirements](ome_groups_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_groups_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **description**  string | Description for the device group.  This is applicable only when *state* is `present`. |
| **group_id**  list / elements=integer | ID of the device group to be created, modified, or deleted.  If *state* is absent, multiple IDs can be provided.  This option is mutually exclusive with *name*. |
| **hostname**  string / required | OpenManage Enterprise IP address or hostname. |
| **name**  list / elements=string | Name of the device group to be created, modified, or deleted.  If *state* is absent, multiple names can be provided.  This option is case insensitive.  This option is mutually exclusive with *group_id*. |
| **new_name**  string | New name for the existing device group.  This is applicable only when *state* is `present`. |
| **parent_group_id**  integer | ID of the parent device group under which the device group to be created or modified.  This is applicable only when *state* is `present`.  This option is mutually exclusive with *parent_group_name*. |
| **parent_group_name**  string | Name of the parent device group under which the device group to be created or modified.  This is applicable only when *state* is `present`.  `NOTE` If device group with such a name does not exist, device group with *parent_group_name* is created.  This option is case insensitive.  This option is mutually exclusive with *parent_group_id*.  **Default:** `"Static Groups"` |
| **password**  string / required | OpenManage Enterprise password. |
| **port**  integer | OpenManage Enterprise HTTPS port.  **Default:** `443` |
| **state**  string | `present` allows to create or modify a device group.  `absent` allows to delete a device group.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **username**  string / required | OpenManage Enterprise username. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ome_groups_module.md#id4)

> **Note:**
>
> - This module manages only static device groups on Dell OpenManage Enterprise.
> - If a device group with the name *parent_group_name* does not exist, a new device group with the same name is created.
> - Make sure the entered parent group is not the descendant of the provided group.
> - Run this module from a system that has direct access to Dell OpenManage Enterprise.
> - This module supports `check_mode`.

## [Examples](ome_groups_module.md#id5)

```yaml+jinja
---
- name: Create a new device group
  dellemc.openmanage.ome_groups:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    name: "group 1"
    description: "Group 1 description"
    parent_group_name: "group parent 1"

- name: Modify a device group using the group ID
  dellemc.openmanage.ome_groups:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    group_id: 1234
    description: "Group description updated"
    parent_group_name: "group parent 2"

- name: Delete a device group using the device group name
  dellemc.openmanage.ome_groups:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: absent
    name: "group 1"

- name: Delete multiple device groups using the group IDs
  dellemc.openmanage.ome_groups:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: absent
    group_id:
      - 1234
      - 5678
```

## [Return Values](ome_groups_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to update group  12345  with the provided parent  54321  because a group/parent relationship already exists.", "MessageArgs": ["12345", "54321"], "MessageId": "CGRP9013", "RelatedProperties": [], "Resolution": "Make sure the entered parent ID does not create a bidirectional relationship and retry the operation.", "Severity": "Warning"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **group_ids**  list / elements=integer | List of the deleted device group IDs.  **Returned:** when *state* is `absent`  **Sample:** `[1234, 5678]` |
| **group_status**  dictionary | Details of the device group operation status.  **Returned:** success  **Sample:** `{"CreatedBy": "admin", "CreationTime": "2021-01-01 10:10:10.100", "DefinitionDescription": "UserDefined", "DefinitionId": 400, "Description": "my group description", "GlobalStatus": 5000, "HasAttributes": false, "Id": 12123, "IdOwner": 30, "MembershipTypeId": 12, "Name": "group 1", "ParentId": 12345, "TypeId": 3000, "UpdatedBy": "", "UpdatedTime": "2021-01-01 11:11:10.100", "Visible": true}` |
| **invalid_groups**  list / elements=string | List of the invalid device group IDs or names.  **Returned:** when *state* is `absent`  **Sample:** `["1234", "5678"]` |
| **msg**  string | Overall status of the device group operation.  **Returned:** always  **Sample:** `"Successfully deleted the device group(s)."` |

### Authors

- Jagadeesh N V(@jagadeeshnv)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
