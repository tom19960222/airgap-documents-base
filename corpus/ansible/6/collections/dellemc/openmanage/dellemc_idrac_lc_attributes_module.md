---
collection: ansible
version: "6"
title: "dellemc.openmanage.dellemc_idrac_lc_attributes module – Enable or disable Collect System Inventory on Restart (CSIOR) property for all iDRAC/LC jobs"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/dellemc_idrac_lc_attributes_module.html
fetched_at: 2026-07-27T17:25:06+00:00
---
# dellemc.openmanage.dellemc_idrac_lc_attributes module – Enable or disable Collect System Inventory on Restart (CSIOR) property for all iDRAC/LC jobs

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
> see [Requirements](dellemc_idrac_lc_attributes_module.md#ansible-collections-dellemc-openmanage-dellemc-idrac-lc-attributes-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.dellemc_idrac_lc_attributes`.

New in dellemc.openmanage 1.0.0

- [Synopsis](dellemc_idrac_lc_attributes_module.md#synopsis)
- [Requirements](dellemc_idrac_lc_attributes_module.md#requirements)
- [Parameters](dellemc_idrac_lc_attributes_module.md#parameters)
- [Notes](dellemc_idrac_lc_attributes_module.md#notes)
- [Examples](dellemc_idrac_lc_attributes_module.md#examples)
- [Return Values](dellemc_idrac_lc_attributes_module.md#return-values)

## [Synopsis](dellemc_idrac_lc_attributes_module.md#id1)

- This module is responsible for enabling or disabling of Collect System Inventory on Restart (CSIOR) property for all iDRAC/LC jobs.

## [Requirements](dellemc_idrac_lc_attributes_module.md#id2)

The below requirements are needed on the host that executes this module.

- omsdk >= 1.2.488
- python >= 3.8.6

## [Parameters](dellemc_idrac_lc_attributes_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **csior**  string | Whether to Enable or Disable Collect System Inventory on Restart (CSIOR) property for all iDRAC/LC jobs.  Choices:   - `"Enabled"` ← (default) - `"Disabled"` |
| **idrac_ip**  string / required | iDRAC IP Address. |
| **idrac_password**  aliases: idrac_pwd  string / required | iDRAC user password. |
| **idrac_port**  integer | iDRAC port.  Default: `443` |
| **idrac_user**  string / required | iDRAC username. |
| **share_mnt**  string | Local mount path of the network share with read-write permission for ansible user. This option is mandatory for Network Share. |
| **share_name**  string / required | Network share or a local path. |
| **share_password**  aliases: share_pwd  string | Network share user password. This option is mandatory for CIFS Network Share. |
| **share_user**  string | Network share user in the format [‘user@domain](mailto:'user%40domain)’ or ‘domain\user’ if user is part of a domain else ‘user’. This option is mandatory for CIFS Network Share. |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](dellemc_idrac_lc_attributes_module.md#id4)

> **Note:**
>
> - This module requires ‘Administrator’ privilege for *idrac_user*.
> - Run this module from a system that has direct access to Dell EMC iDRAC.
> - This module supports `check_mode`.

## [Examples](dellemc_idrac_lc_attributes_module.md#id5)

```yaml+jinja
---
- name: Set up iDRAC LC Attributes
  dellemc.openmanage.dellemc_idrac_lc_attributes:
       idrac_ip:   "192.168.0.1"
       idrac_user: "user_name"
       idrac_password:  "user_password"
       ca_path: "/path/to/ca_cert.pem"
       share_name: "192.168.0.1:/share"
       share_mnt: "/mnt/share"
       csior: "Enabled"
```

## [Return Values](dellemc_idrac_lc_attributes_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  Returned: on HTTP error  Sample: `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **lc_attribute_status**  dictionary | Collect System Inventory on Restart (CSIOR) property for all iDRAC/LC jobs is configured.  Returned: success  Sample: `{"CompletionTime": "2020-03-30T00:06:53", "Description": "Job Instance", "EndTime": null, "Id": "JID_1234512345", "JobState": "Completed", "JobType": "ImportConfiguration", "Message": "Successfully imported and applied Server Configuration Profile.", "MessageArgs": [], "MessageArgs@odata.count": 0, "MessageId": "SYS053", "Name": "Import Configuration", "PercentComplete": 100, "StartTime": "TIME_NOW", "Status": "Success", "TargetSettingsURI": null, "retval": true}` |
| **msg**  string | Overall status of iDRAC LC attributes configuration.  Returned: always  Sample: `"Successfully configured the iDRAC LC attributes."` |

### Authors

- Felix Stephen (@felixs88)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
