---
collection: ansible
version: "8"
title: "dellemc.openmanage.idrac_user_info module – Retrieve details of all users or a specific user on iDRAC."
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/idrac_user_info_module.html
fetched_at: 2026-07-28T02:04:15+00:00
---
# dellemc.openmanage.idrac_user_info module – Retrieve details of all users or a specific user on iDRAC.

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
> see [Requirements](idrac_user_info_module.md#ansible-collections-dellemc-openmanage-idrac-user-info-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.idrac_user_info`.

New in dellemc.openmanage 7.0.0

- [Synopsis](idrac_user_info_module.md#synopsis)
- [Requirements](idrac_user_info_module.md#requirements)
- [Parameters](idrac_user_info_module.md#parameters)
- [Notes](idrac_user_info_module.md#notes)
- [Examples](idrac_user_info_module.md#examples)
- [Return Values](idrac_user_info_module.md#return-values)

## [Synopsis](idrac_user_info_module.md#id1)

- This module retrieves the list and basic details of all users or details of a specific user on iDRAC

## [Requirements](idrac_user_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](idrac_user_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **idrac_ip**  string / required | iDRAC IP Address. |
| **idrac_password**  aliases: idrac_pwd  string / required | iDRAC user password. |
| **idrac_port**  integer | iDRAC port.  **Default:** `443` |
| **idrac_user**  string / required | iDRAC username. |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **user_id**  integer | Sequential user id numbers that supports from 1 to 16.  *user_id* is mutually exclusive with *username* |
| **username**  string | Username of the account that is created in iDRAC local users.  *username* is mutually exclusive with *user_id* |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](idrac_user_info_module.md#id4)

> **Note:**
>
> - Run this module on a system that has direct access to Dell iDRAC.
> - This module supports `check_mode`.

## [Examples](idrac_user_info_module.md#id5)

```yaml+jinja
---
- name: Retrieve basic details of all user accounts.
  dellemc.openmanage.idrac_user_info:
    idrac_ip: 198.162.0.1
    idrac_user: idrac_user
    idrac_password: idrac_password
    ca_path: "/path/to/ca_cert.pem"

- name: Retrieve user details using user_id
  dellemc.openmanage.idrac_user_info:
    idrac_ip: 198.162.0.1
    idrac_user: idrac_user
    idrac_password: idrac_password
    ca_path: "/path/to/ca_cert.pem"
    user_id: 1

- name: Retrieve user details using username
  dellemc.openmanage.idrac_user_info:
    idrac_ip: 198.162.0.1
    idrac_user: idrac_user
    idrac_password: idrac_password
    ca_path: "/path/to/ca_cert.pem"
    username: user_name
```

## [Return Values](idrac_user_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Status of user information retrieval.  **Returned:** always  **Sample:** `"Successfully retrieved the user information."` |
| **user_info**  list / elements=string | Information about the user.  **Returned:** success  **Sample:** `[{"Description": "User Account", "Enabled": false, "Id": "1", "Locked": false, "Name": "User Account", "Password": null, "RoleId": "None", "UserName": ""}]` |

### Authors

- Husniya Hameed(@husniya_hameed)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
