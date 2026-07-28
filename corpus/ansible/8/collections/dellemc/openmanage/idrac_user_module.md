---
collection: ansible
version: "8"
title: "dellemc.openmanage.idrac_user module – Configure settings for user accounts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/idrac_user_module.html
fetched_at: 2026-07-28T02:04:14+00:00
---
# dellemc.openmanage.idrac_user module – Configure settings for user accounts

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
> see [Requirements](idrac_user_module.md#ansible-collections-dellemc-openmanage-idrac-user-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.idrac_user`.

New in dellemc.openmanage 2.1.0

- [Synopsis](idrac_user_module.md#synopsis)
- [Requirements](idrac_user_module.md#requirements)
- [Parameters](idrac_user_module.md#parameters)
- [Notes](idrac_user_module.md#notes)
- [Examples](idrac_user_module.md#examples)
- [Return Values](idrac_user_module.md#return-values)

## [Synopsis](idrac_user_module.md#id1)

- This module allows to perform the following,
- Add a new user account.
- Edit a user account.
- Enable or Disable a user account.

## [Requirements](idrac_user_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](idrac_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **authentication_protocol**  string | This option allows to configure one of the following authentication protocol types to authenticate the iDRAC user.  Secure Hash Algorithm `SHA`.  Message Digest 5 `MD5`.  An authentication protocol is not configured if `None` is selected.  **Choices:**   - `"None"` - `"SHA"` - `"MD5"` |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **enable**  boolean | Provide the option to enable or disable a user from logging in to iDRAC.  **Choices:**   - `false` - `true` |
| **idrac_ip**  string / required | iDRAC IP Address. |
| **idrac_password**  aliases: idrac_pwd  string / required | iDRAC user password. |
| **idrac_port**  integer | iDRAC port.  **Default:** `443` |
| **idrac_user**  string / required | iDRAC username. |
| **ipmi_lan_privilege**  string | The Intelligent Platform Management Interface LAN privilege level assigned to the user.  **Choices:**   - `"Administrator"` - `"Operator"` - `"User"` - `"No Access"` |
| **ipmi_serial_privilege**  string | The Intelligent Platform Management Interface Serial Port privilege level assigned to the user.  This option is only applicable for rack and tower servers.  **Choices:**   - `"Administrator"` - `"Operator"` - `"User"` - `"No Access"` |
| **new_user_name**  string | Provide the *user_name* for the account to be modified. |
| **privacy_protocol**  string | This option allows to configure one of the following privacy encryption protocols for the iDRAC user.  Data Encryption Standard `DES`.  Advanced Encryption Standard `AES`.  A privacy protocol is not configured if `None` is selected.  **Choices:**   - `"None"` - `"DES"` - `"AES"` |
| **privilege**  string | Following are the role-based privileges.  A user with `Administrator` privilege can log in to iDRAC, and then configure iDRAC, configure users, clear logs, control and configure system, access virtual console, access virtual media, test alerts, and execute debug commands.  A user with `Operator` privilege can log in to iDRAC, and then configure iDRAC, control and configure system, access virtual console, access virtual media, and execute debug commands.  A user with `ReadOnly` privilege can only log in to iDRAC.  A user with `None`, no privileges assigned.  **Choices:**   - `"Administrator"` - `"ReadOnly"` - `"Operator"` - `"None"` |
| **protocol_enable**  boolean | Enables protocol for the iDRAC user.  **Choices:**   - `false` - `true` |
| **sol_enable**  boolean | Enables Serial Over Lan (SOL) for an iDRAC user.  **Choices:**   - `false` - `true` |
| **state**  string | Select `present` to create or modify a user account.  Select `absent` to remove a user account.  Ensure Lifecycle Controller is available because the user operation uses the capabilities of Lifecycle Controller.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **user_name**  string / required | Provide the *user_name* of the account to be created, deleted or modified. |
| **user_password**  string | Provide the password for the user account. The password can be changed when the user account is modified.  To ensure security, the *user_password* must be at least eight characters long and must contain lowercase and upper-case characters, numbers, and special characters. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](idrac_user_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to Dell iDRAC.
> - This module supports `check_mode`.

## [Examples](idrac_user_module.md#id5)

```yaml+jinja
---
- name: Configure a new iDRAC user
  dellemc.openmanage.idrac_user:
    idrac_ip: 198.162.0.1
    idrac_user: idrac_user
    idrac_password: idrac_password
    ca_path: "/path/to/ca_cert.pem"
    state: present
    user_name: user_name
    user_password: user_password
    privilege: Administrator
    ipmi_lan_privilege: Administrator
    ipmi_serial_privilege: Administrator
    enable: true
    sol_enable: true
    protocol_enable: true
    authentication_protocol: SHA
    privacy_protocol: AES

- name: Modify existing iDRAC user username and password
  dellemc.openmanage.idrac_user:
    idrac_ip: 198.162.0.1
    idrac_user: idrac_user
    idrac_password: idrac_password
    ca_path: "/path/to/ca_cert.pem"
    state: present
    user_name: user_name
    new_user_name: new_user_name
    user_password: user_password

- name: Delete existing iDRAC user account
  dellemc.openmanage.idrac_user:
    idrac_ip: 198.162.0.1
    idrac_user: idrac_user
    idrac_password: idrac_password
    ca_path: "/path/to/ca_cert.pem"
    state: absent
    user_name: user_name
```

## [Return Values](idrac_user_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Status of the iDRAC user configuration.  **Returned:** always  **Sample:** `"Successfully created user account details."` |
| **status**  dictionary | Configures the iDRAC users attributes.  **Returned:** success  **Sample:** `{"@Message.ExtendedInfo": [{"Message": "Successfully Completed Request", "MessageArgs": [], "MessageArgs@odata.count": 0, "MessageId": "Base.1.5.Success", "RelatedProperties": [], "RelatedProperties@odata.count": 0, "Resolution": "None", "Severity": "OK"}, {"Message": "The operation successfully completed.", "MessageArgs": [], "MessageArgs@odata.count": 0, "MessageId": "IDRAC.2.1.SYS413", "RelatedProperties": [], "RelatedProperties@odata.count": 0, "Resolution": "No response action is required.", "Severity": "Informational"}]}` |

### Authors

- Felix Stephen (@felixs88)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
