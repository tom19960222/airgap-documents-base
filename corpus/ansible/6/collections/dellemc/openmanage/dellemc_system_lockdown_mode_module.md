---
collection: ansible
version: "6"
title: "dellemc.openmanage.dellemc_system_lockdown_mode module – Configures system lockdown mode for iDRAC"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/dellemc_system_lockdown_mode_module.html
fetched_at: 2026-07-27T17:25:08+00:00
---
# dellemc.openmanage.dellemc_system_lockdown_mode module – Configures system lockdown mode for iDRAC

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
> see [Requirements](dellemc_system_lockdown_mode_module.md#ansible-collections-dellemc-openmanage-dellemc-system-lockdown-mode-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.dellemc_system_lockdown_mode`.

New in dellemc.openmanage 1.0.0

- [Synopsis](dellemc_system_lockdown_mode_module.md#synopsis)
- [Requirements](dellemc_system_lockdown_mode_module.md#requirements)
- [Parameters](dellemc_system_lockdown_mode_module.md#parameters)
- [Notes](dellemc_system_lockdown_mode_module.md#notes)
- [Examples](dellemc_system_lockdown_mode_module.md#examples)
- [Return Values](dellemc_system_lockdown_mode_module.md#return-values)

## [Synopsis](dellemc_system_lockdown_mode_module.md#id1)

- This module is allows to Enable or Disable System lockdown Mode.

## [Requirements](dellemc_system_lockdown_mode_module.md#id2)

The below requirements are needed on the host that executes this module.

- omsdk >= 1.2.488
- python >= 3.8.6

## [Parameters](dellemc_system_lockdown_mode_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **idrac_ip**  string / required | iDRAC IP Address. |
| **idrac_password**  aliases: idrac_pwd  string / required | iDRAC user password. |
| **idrac_port**  integer | iDRAC port.  Default: `443` |
| **idrac_user**  string / required | iDRAC username. |
| **lockdown_mode**  string / required | Whether to Enable or Disable system lockdown mode.  Choices:   - `"Enabled"` - `"Disabled"` |
| **share_mnt**  string | Local mount path of the network share with read-write permission for ansible user. This option is mandatory for Network Share. |
| **share_name**  string / required | Network share or a local path. |
| **share_password**  aliases: share_pwd  string | Network share user password. This option is mandatory for CIFS Network Share. |
| **share_user**  string | Network share user in the format [‘user@domain](mailto:'user%40domain)’ or ‘domain\user’ if user is part of a domain else ‘user’. This option is mandatory for CIFS Network Share. |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](dellemc_system_lockdown_mode_module.md#id4)

> **Note:**
>
> - This module requires ‘Administrator’ privilege for *idrac_user*.
> - Run this module from a system that has direct access to Dell EMC iDRAC.
> - This module does not support `check_mode`.

## [Examples](dellemc_system_lockdown_mode_module.md#id5)

```yaml+jinja
---
- name: Check System  Lockdown Mode
  dellemc.openmanage.dellemc_system_lockdown_mode:
       idrac_ip:   "192.168.0.1"
       idrac_user: "user_name"
       idrac_password:  "user_password"
       ca_path: "/path/to/ca_cert.pem"
       share_name: "192.168.0.1:/share"
       share_mnt: "/mnt/share"
       lockdown_mode: "Disabled"
```

## [Return Values](dellemc_system_lockdown_mode_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  Returned: on HTTP error  Sample: `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Lockdown mode of the system is configured.  Returned: always  Sample: `"Successfully completed the lockdown mode operations."` |
| **system_lockdown_status**  dictionary | Storage configuration job and progress details from the iDRAC.  Returned: success  Sample: `{"Data": {"StatusCode": 200, "body": {"@Message.ExtendedInfo": [{"Message": "Successfully Completed Request", "MessageArgs": [], "MessageArgs@odata.count": 0, "MessageId": "Base.1.0.Success", "RelatedProperties": [], "RelatedProperties@odata.count": 0, "Resolution": "None", "Severity": "OK"}]}}, "Message": "none", "Status": "Success", "StatusCode": 200, "retval": true}` |

### Authors

- Felix Stephen (@felixs88)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
