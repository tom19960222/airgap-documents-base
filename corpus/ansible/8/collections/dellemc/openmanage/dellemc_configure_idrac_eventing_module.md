---
collection: ansible
version: "8"
title: "dellemc.openmanage.dellemc_configure_idrac_eventing module – Configures the iDRAC eventing related attributes"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/dellemc_configure_idrac_eventing_module.html
fetched_at: 2026-07-28T02:03:56+00:00
---
# dellemc.openmanage.dellemc_configure_idrac_eventing module – Configures the iDRAC eventing related attributes

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
> see [Requirements](dellemc_configure_idrac_eventing_module.md#ansible-collections-dellemc-openmanage-dellemc-configure-idrac-eventing-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.dellemc_configure_idrac_eventing`.

New in dellemc.openmanage 1.0.0

- [DEPRECATED](dellemc_configure_idrac_eventing_module.md#deprecated)
- [Synopsis](dellemc_configure_idrac_eventing_module.md#synopsis)
- [Requirements](dellemc_configure_idrac_eventing_module.md#requirements)
- [Parameters](dellemc_configure_idrac_eventing_module.md#parameters)
- [Notes](dellemc_configure_idrac_eventing_module.md#notes)
- [Examples](dellemc_configure_idrac_eventing_module.md#examples)
- [Return Values](dellemc_configure_idrac_eventing_module.md#return-values)
- [Status](dellemc_configure_idrac_eventing_module.md#status)

## [DEPRECATED](dellemc_configure_idrac_eventing_module.md#id1)

Removed in:
:   major release after 2024-07-31

Why:
:   Replaced with [dellemc.openmanage.idrac_attributes](idrac_attributes_module.md#ansible-collections-dellemc-openmanage-idrac-attributes-module).

Alternative:
:   Use [dellemc.openmanage.idrac_attributes](idrac_attributes_module.md#ansible-collections-dellemc-openmanage-idrac-attributes-module) instead.

## [Synopsis](dellemc_configure_idrac_eventing_module.md#id2)

- This module allows to configure the iDRAC eventing related attributes.

## [Requirements](dellemc_configure_idrac_eventing_module.md#id3)

The below requirements are needed on the host that executes this module.

- omsdk >= 1.2.503
- python >= 3.9.6

## [Parameters](dellemc_configure_idrac_eventing_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **address**  string | Email address for SNMP Trap. |
| **alert_number**  integer | Alert number for Email configuration. |
| **authentication**  string | Simple Mail Transfer Protocol Authentication.  **Choices:**   - `"Enabled"` - `"Disabled"` |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **custom_message**  string | Custom message for SNMP Trap reference. |
| **destination**  string | Destination for SNMP Trap. |
| **destination_number**  integer | Destination number for SNMP Trap. |
| **email_alert_state**  string | Whether to Enable or Disable Email alert.  **Choices:**   - `"Enabled"` - `"Disabled"` |
| **enable_alerts**  string | Whether to Enable or Disable iDRAC alerts.  **Choices:**   - `"Enabled"` - `"Disabled"` |
| **idrac_ip**  string / required | iDRAC IP Address. |
| **idrac_password**  aliases: idrac_pwd  string / required | iDRAC user password. |
| **idrac_port**  integer | iDRAC port.  **Default:** `443` |
| **idrac_user**  string / required | iDRAC username. |
| **password**  string | Password for SMTP authentication. |
| **share_mnt**  string | (deprecated)Local mount path of the network share with read-write permission for ansible user. This option is mandatory for Network Share.  This option is deprecated and will be removed in the later version. |
| **share_name**  string | (deprecated)Network share or a local path.  This option is deprecated and will be removed in the later version. |
| **share_password**  aliases: share_pwd  string | (deprecated)Network share user password. This option is mandatory for CIFS Network Share.  This option is deprecated and will be removed in the later version. |
| **share_user**  string | (deprecated)Network share user in the format [‘user@domain](mailto:'user%40domain)’ or ‘domain\user’ if user is part of a domain else ‘user’. This option is mandatory for CIFS Network Share.  This option is deprecated and will be removed in the later version. |
| **smtp_ip_address**  string | Enter the IPv4 or IPv6 address of the SMTP server or the FQDN or DNS name. |
| **smtp_port**  string | SMTP Port number for access. |
| **snmp_trap_state**  string | Whether to Enable or Disable SNMP alert.  **Choices:**   - `"Enabled"` - `"Disabled"` |
| **snmp_v3_username**  string | SNMP v3 username for SNMP Trap. |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **username**  string | Username for SMTP authentication. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](dellemc_configure_idrac_eventing_module.md#id5)

> **Note:**
>
> - This module requires ‘Administrator’ privilege for *idrac_user*.
> - Run this module from a system that has direct access to Dell iDRAC.
> - This module supports both IPv4 and IPv6 address for *idrac_ip*.
> - This module supports `check_mode`.

## [Examples](dellemc_configure_idrac_eventing_module.md#id6)

```yaml+jinja
---
- name: Configure the iDRAC eventing attributes
  dellemc.openmanage.dellemc_configure_idrac_eventing:
       idrac_ip:   "192.168.0.1"
       idrac_user: "user_name"
       idrac_password:  "user_password"
       ca_path: "/path/to/ca_cert.pem"
       destination_number: "2"
       destination: "1.1.1.1"
       snmp_v3_username: "None"
       snmp_trap_state: "Enabled"
       email_alert_state: "Disabled"
       alert_number: "1"
       address: "alert_email@company.com"
       custom_message: "Custom Message"
       enable_alerts: "Disabled"
       authentication: "Enabled"
       smtp_ip_address: "192.168.0.1"
       smtp_port: "25"
       username: "username"
       password: "password"
```

## [Return Values](dellemc_configure_idrac_eventing_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **eventing_status**  dictionary | Configures the iDRAC eventing attributes.  **Returned:** success  **Sample:** `{"CompletionTime": "2020-04-02T02:43:28", "Description": "Job Instance", "EndTime": null, "Id": "JID_12345123456", "JobState": "Completed", "JobType": "ImportConfiguration", "Message": "Successfully imported and applied Server Configuration Profile.", "MessageArgs": [], "MessageId": "SYS053", "Name": "Import Configuration", "PercentComplete": 100, "StartTime": "TIME_NOW", "Status": "Success", "TargetSettingsURI": null, "retval": true}` |
| **msg**  string | Successfully configured the iDRAC eventing settings.  **Returned:** always  **Sample:** `"Successfully configured the iDRAC eventing settings."` |

## [Status](dellemc_configure_idrac_eventing_module.md#id8)

- This module will be removed in a major release after 2024-07-31.
  *[deprecated]*
- For more information see [DEPRECATED](dellemc_configure_idrac_eventing_module.md#deprecated).

### Authors

- Felix Stephen (@felixs88)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
