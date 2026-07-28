---
collection: ansible
version: "8"
title: "dellemc.openmanage.ome_user module – Create, modify or delete a user on OpenManage Enterprise"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/ome_user_module.html
fetched_at: 2026-07-28T02:04:54+00:00
---
# dellemc.openmanage.ome_user module – Create, modify or delete a user on OpenManage Enterprise

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
> see [Requirements](ome_user_module.md#ansible-collections-dellemc-openmanage-ome-user-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_user`.

New in dellemc.openmanage 2.0.0

- [Synopsis](ome_user_module.md#synopsis)
- [Requirements](ome_user_module.md#requirements)
- [Parameters](ome_user_module.md#parameters)
- [Notes](ome_user_module.md#notes)
- [Examples](ome_user_module.md#examples)
- [Return Values](ome_user_module.md#return-values)

## [Synopsis](ome_user_module.md#id1)

- This module creates, modifies or deletes a user on OpenManage Enterprise.

## [Requirements](ome_user_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **attributes**  dictionary | Payload data for the user operations. It can take the following attributes for `present`.  UserTypeId, DirectoryServiceId, Description, Name, Password, UserName, RoleId, Locked, Enabled.  OME will throw error if required parameter is not provided for operation.  Refer OpenManage Enterprise API Reference Guide for more details.  **Default:** `{}` |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname. |
| **name**  string | Unique Name of the user to be deleted.  Either *user_id* or *name* is mandatory for `absent` operation. |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  **Default:** `443` |
| **state**  string | `present` creates a user in case the *UserName* provided inside *attributes* does not exist.  `present` modifies a user in case the *UserName* provided inside *attributes* exists.  `absent` deletes an existing user.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **user_id**  integer | Unique ID of the user to be deleted.  Either *user_id* or *name* is mandatory for `absent` operation. |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ome_user_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to Dell OpenManage Enterprise.
> - This module does not support `check_mode`.

## [Examples](ome_user_module.md#id5)

```yaml+jinja
---
- name: Create user with required parameters
  dellemc.openmanage.ome_user:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    attributes:
      UserName: "user1"
      Password: "UserPassword"
      RoleId: "10"
      Enabled: True

- name: Create user with all parameters
  dellemc.openmanage.ome_user:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    attributes:
      UserName: "user2"
      Description: "user2 description"
      Password: "UserPassword"
      RoleId: "10"
      Enabled: True
      DirectoryServiceId: 0
      UserTypeId: 1
      Locked: False
      Name: "user2"

- name: Modify existing user
  dellemc.openmanage.ome_user:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: "present"
    attributes:
      UserName: "user3"
      RoleId: "10"
      Enabled: True
      Description: "Modify user Description"

- name: Delete existing user using id
  dellemc.openmanage.ome_user:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: "absent"
    user_id: 1234

- name: Delete existing user using name
  dellemc.openmanage.ome_user:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: "absent"
    name: "name"
```

## [Return Values](ome_user_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Overall status of the user operation.  **Returned:** always  **Sample:** `"Successfully created a User"` |
| **user_status**  dictionary | Details of the user operation, when *state* is `present`.  **Returned:** When *state* is `present`.  **Sample:** `{"Description": "Test user creation", "DirectoryServiceId": 0, "Enabled": true, "Id": "61546", "IsBuiltin": false, "Locked": false, "Name": "test", "Password": null, "PlainTextPassword": null, "RoleId": "10", "UserName": "test", "UserTypeId": 1}` |

### Authors

- Sajna Shetty(@Sajna-Shetty)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
