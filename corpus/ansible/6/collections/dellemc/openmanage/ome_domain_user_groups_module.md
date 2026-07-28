---
collection: ansible
version: "6"
title: "dellemc.openmanage.ome_domain_user_groups module – Create, modify, or delete an Active Directory user group on OpenManage Enterprise and OpenManage Enterprise Modular"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/ome_domain_user_groups_module.html
fetched_at: 2026-07-27T17:25:38+00:00
---
# dellemc.openmanage.ome_domain_user_groups module – Create, modify, or delete an Active Directory user group on OpenManage Enterprise and OpenManage Enterprise Modular

> **Note:**
>
> This module is part of the [dellemc.openmanage collection](https://galaxy.ansible.com/dellemc/openmanage) (version 5.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.openmanage`.
> You need further requirements to be able to use this module,
> see [Requirements](ome_domain_user_groups_module.md#ansible-collections-dellemc-openmanage-ome-domain-user-groups-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_domain_user_groups`.

New in dellemc.openmanage 4.0.0

- [Synopsis](ome_domain_user_groups_module.md#synopsis)
- [Requirements](ome_domain_user_groups_module.md#requirements)
- [Parameters](ome_domain_user_groups_module.md#parameters)
- [Notes](ome_domain_user_groups_module.md#notes)
- [Examples](ome_domain_user_groups_module.md#examples)
- [Return Values](ome_domain_user_groups_module.md#return-values)

## [Synopsis](ome_domain_user_groups_module.md#id1)

- This module allows to create, modify, or delete an Active Directory user group on OpenManage Enterprise and OpenManage Enterprise Modular.

## [Requirements](ome_domain_user_groups_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_domain_user_groups_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **directory_id**  integer | The ID of the Active Directory.  *directory_id* is mutually exclusive with *directory_name*. |
| **directory_name**  string | The directory name set while adding the Active Directory.  *directory_name* is mutually exclusive with *directory_id*. |
| **domain_password**  string | Active directory domain password. |
| **domain_username**  string | Active directory domain username.  Example: [username@domain](mailto:username%40domain) or domain\username. |
| **group_name**  string / required | The desired Active Directory user group name to be imported or removed.  Examples for user group name: Administrator or Account Operators or Access Control Assistance Operator.  *group_name* value is case insensitive. |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname. |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  Default: `443` |
| **role**  string | The desired roles and privilege for the imported Active Directory user group.  OpenManage Enterprise Modular Roles: CHASSIS ADMINISTRATOR, COMPUTE MANAGER, STORAGE MANAGER, FABRIC MANAGER, VIEWER.  OpenManage Enterprise Roles: ADMINISTRATOR, DEVICE MANAGER, VIEWER.  *role* value is case insensitive. |
| **state**  string | `present` imports or modifies the Active Directory user group.  `absent` deletes an existing Active Directory user group.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](ome_domain_user_groups_module.md#id4)

> **Note:**
>
> - This module supports `check_mode` and idempotency.
> - Run this module from a system that has direct access to OpenManage Enterprise or OpenManage Enterprise Modular.

## [Examples](ome_domain_user_groups_module.md#id5)

```yaml+jinja
---
- name: Create Active Directory user group
  dellemc.openmanage.ome_domain_user_groups:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: present
    group_name: account operators
    directory_name: directory_name
    role: administrator
    domain_username: username@domain
    domain_password: domain_password

- name: Update Active Directory user group
  dellemc.openmanage.ome_domain_user_groups:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: present
    group_name: account operators
    role: viewer

- name: Delete active directory user group
  dellemc.openmanage.ome_domain_user_groups:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: absent
    group_name: administrators
```

## [Return Values](ome_domain_user_groups_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **domain_user_status**  dictionary | Details of the domain user operation, when *state* is `present`.  Returned: When *state* is `present`.  Sample: `{"Description": null, "DirectoryServiceId": 16097, "Enabled": true, "Id": "16617", "IsBuiltin": false, "IsVisible": true, "Locked": false, "Name": "Account Operators", "ObjectGuid": "a491859c-031e-42a3-ae5e-0ab148ecf1d6", "ObjectSid": null, "Oem": null, "Password": null, "PlainTextPassword": null, "RoleId": "16", "UserName": "Account Operators", "UserTypeId": 2}` |
| **error_info**  dictionary | Details of the HTTP Error.  Returned: on HTTP error  Sample: `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Overall status of the Active Directory user group operation.  Returned: always  Sample: `"Successfully imported the active directory user group."` |

### Authors

- Felix Stephen (@felixs88)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
