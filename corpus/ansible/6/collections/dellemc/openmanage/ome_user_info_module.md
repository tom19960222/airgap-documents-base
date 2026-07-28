---
collection: ansible
version: "6"
title: "dellemc.openmanage.ome_user_info module – Retrieves details of all accounts or a specific account on OpenManage Enterprise"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/ome_user_info_module.html
fetched_at: 2026-07-27T17:25:54+00:00
---
# dellemc.openmanage.ome_user_info module – Retrieves details of all accounts or a specific account on OpenManage Enterprise

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
> see [Requirements](ome_user_info_module.md#ansible-collections-dellemc-openmanage-ome-user-info-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_user_info`.

New in dellemc.openmanage 2.0.0

- [Synopsis](ome_user_info_module.md#synopsis)
- [Requirements](ome_user_info_module.md#requirements)
- [Parameters](ome_user_info_module.md#parameters)
- [Notes](ome_user_info_module.md#notes)
- [Examples](ome_user_info_module.md#examples)
- [Return Values](ome_user_info_module.md#return-values)

## [Synopsis](ome_user_info_module.md#id1)

- This module retrieves the list and basic details of all accounts or details of a specific account on OpenManage Enterprise.

## [Requirements](ome_user_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_user_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account_id**  integer | Unique Id of the account. |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname. |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  Default: `443` |
| **system_query_options**  dictionary | Options for filtering the output. |
| **filter**  string | Filter records for the supported values. |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](ome_user_info_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to DellEMC OpenManage Enterprise.
> - This module supports `check_mode`.

## [Examples](ome_user_info_module.md#id5)

```yaml+jinja
---
- name: Retrieve basic details of all accounts
  dellemc.openmanage.ome_user_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"

- name: Retrieve details of a specific account identified by its account ID
  dellemc.openmanage.ome_user_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    account_id: 1

- name: Get filtered user info based on user name
  dellemc.openmanage.ome_user_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    system_query_options:
      filter: "UserName eq 'test'"
```

## [Return Values](ome_user_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Over all status of fetching user facts.  Returned: on error  Sample: `"Unable to retrieve the account details."` |
| **user_info**  dictionary | Details of the user.  Returned: success  Sample: `{"192.168.0.1": {"Description": "user name description", "DirectoryServiceId": 0, "Enabled": true, "Id": "1814", "IsBuiltin": true, "Locked": false, "Name": "user_name", "Password": null, "RoleId": "10", "UserName": "user_name", "UserTypeId": 1}}` |

### Authors

- Jagadeesh N V(@jagadeeshnv)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
