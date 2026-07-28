---
collection: ansible
version: "8"
title: "dellemc.openmanage.idrac_reset module – Reset iDRAC"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/idrac_reset_module.html
fetched_at: 2026-07-28T02:04:10+00:00
---
# dellemc.openmanage.idrac_reset module – Reset iDRAC

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
> see [Requirements](idrac_reset_module.md#ansible-collections-dellemc-openmanage-idrac-reset-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.idrac_reset`.

New in dellemc.openmanage 2.1.0

- [Synopsis](idrac_reset_module.md#synopsis)
- [Requirements](idrac_reset_module.md#requirements)
- [Parameters](idrac_reset_module.md#parameters)
- [Notes](idrac_reset_module.md#notes)
- [Examples](idrac_reset_module.md#examples)
- [Return Values](idrac_reset_module.md#return-values)

## [Synopsis](idrac_reset_module.md#id1)

- This module resets iDRAC.
- iDRAC is not accessible for some time after running this module. It is recommended to wait for some time, before trying to connect to iDRAC.

## [Requirements](idrac_reset_module.md#id2)

The below requirements are needed on the host that executes this module.

- omsdk >= 1.2.488
- python >= 3.9.6

## [Parameters](idrac_reset_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **idrac_ip**  string / required | iDRAC IP Address. |
| **idrac_password**  aliases: idrac_pwd  string / required | iDRAC user password. |
| **idrac_port**  integer | iDRAC port.  **Default:** `443` |
| **idrac_user**  string / required | iDRAC username. |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](idrac_reset_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to Dell iDRAC.
> - This module supports both IPv4 and IPv6 address for *idrac_ip*.
> - This module supports `check_mode`.

## [Examples](idrac_reset_module.md#id5)

```yaml+jinja
---
- name: Reset iDRAC
  dellemc.openmanage.idrac_reset:
       idrac_ip: "192.168.0.1"
       idrac_user: "user_name"
       idrac_password: "user_password"
       idrac_port: 443
       ca_path: "/path/to/ca_cert.pem"
```

## [Return Values](idrac_reset_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Status of the iDRAC reset operation.  **Returned:** always  **Sample:** `"Successfully performed iDRAC reset."` |
| **reset_status**  dictionary | Details of iDRAC reset operation.  **Returned:** always  **Sample:** `{"idracreset": {"Data": {"StatusCode": 204}, "Message": "none", "Status": "Success", "StatusCode": 204, "retval": true}}` |

### Authors

- Felix Stephen (@felixs88)
- Anooja Vardhineni (@anooja-vardhineni)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
