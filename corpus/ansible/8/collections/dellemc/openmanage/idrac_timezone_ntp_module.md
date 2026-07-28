---
collection: ansible
version: "8"
title: "dellemc.openmanage.idrac_timezone_ntp module – Configures time zone and NTP on iDRAC"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/idrac_timezone_ntp_module.html
fetched_at: 2026-07-28T02:04:13+00:00
---
# dellemc.openmanage.idrac_timezone_ntp module – Configures time zone and NTP on iDRAC

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
> see [Requirements](idrac_timezone_ntp_module.md#ansible-collections-dellemc-openmanage-idrac-timezone-ntp-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.idrac_timezone_ntp`.

New in dellemc.openmanage 2.1.0

- [DEPRECATED](idrac_timezone_ntp_module.md#deprecated)
- [Synopsis](idrac_timezone_ntp_module.md#synopsis)
- [Requirements](idrac_timezone_ntp_module.md#requirements)
- [Parameters](idrac_timezone_ntp_module.md#parameters)
- [Notes](idrac_timezone_ntp_module.md#notes)
- [Examples](idrac_timezone_ntp_module.md#examples)
- [Return Values](idrac_timezone_ntp_module.md#return-values)
- [Status](idrac_timezone_ntp_module.md#status)

## [DEPRECATED](idrac_timezone_ntp_module.md#id1)

Removed in:
:   major release after 2024-07-31

Why:
:   Replaced with [dellemc.openmanage.idrac_attributes](idrac_attributes_module.md#ansible-collections-dellemc-openmanage-idrac-attributes-module).

Alternative:
:   Use [dellemc.openmanage.idrac_attributes](idrac_attributes_module.md#ansible-collections-dellemc-openmanage-idrac-attributes-module) instead.

## [Synopsis](idrac_timezone_ntp_module.md#id2)

- This module allows to configure time zone and NTP on iDRAC.

## [Requirements](idrac_timezone_ntp_module.md#id3)

The below requirements are needed on the host that executes this module.

- omsdk >= 1.2.488
- python >= 3.9.6

## [Parameters](idrac_timezone_ntp_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **enable_ntp**  string | Allows to enable or disable NTP on iDRAC.  **Choices:**   - `"Enabled"` - `"Disabled"` |
| **idrac_ip**  string / required | iDRAC IP Address. |
| **idrac_password**  aliases: idrac_pwd  string / required | iDRAC user password. |
| **idrac_port**  integer | iDRAC port.  **Default:** `443` |
| **idrac_user**  string / required | iDRAC username. |
| **ntp_server_1**  string | The IP address of the NTP server 1. |
| **ntp_server_2**  string | The IP address of the NTP server 2. |
| **ntp_server_3**  string | The IP address of the NTP server 3. |
| **setup_idrac_timezone**  string | Allows to configure time zone on iDRAC. |
| **share_mnt**  string | (deprecated)Local mount path of the network share with read-write permission for ansible user. This option is mandatory for network shares.  This option is deprecated and will be removed in the later version. |
| **share_name**  string | (deprecated)Network share or a local path.  This option is deprecated and will be removed in the later version. |
| **share_password**  aliases: share_pwd  string | (deprecated)Network share user password. This option is mandatory for CIFS share.  This option is deprecated and will be removed in the later version. |
| **share_user**  string | (deprecated)Network share user name. Use the format [‘user@domain](mailto:'user%40domain)’ or ‘domain\user’ if user is part of a domain. This option is mandatory for CIFS share.  This option is deprecated and will be removed in the later version. |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](idrac_timezone_ntp_module.md#id5)

> **Note:**
>
> - This module requires ‘Administrator’ privilege for *idrac_user*.
> - Run this module from a system that has direct access to Dell iDRAC.
> - This module supports both IPv4 and IPv6 address for *idrac_ip*.
> - This module supports `check_mode`.

## [Examples](idrac_timezone_ntp_module.md#id6)

```yaml+jinja
---
- name: Configure time zone and NTP on iDRAC
  dellemc.openmanage.idrac_timezone_ntp:
       idrac_ip:   "190.168.0.1"
       idrac_user: "user_name"
       idrac_password:  "user_password"
       ca_path: "/path/to/ca_cert.pem"
       setup_idrac_timezone: "UTC"
       enable_ntp: Enabled
       ntp_server_1: "190.168.0.1"
       ntp_server_2: "190.168.0.2"
       ntp_server_3: "190.168.0.3"
```

## [Return Values](idrac_timezone_ntp_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Overall status of the timezone and ntp configuration.  **Returned:** always  **Sample:** `"Successfully configured the iDRAC time settings."` |
| **timezone_ntp_status**  dictionary | Job details of the time zone setting operation.  **Returned:** success  **Sample:** `{"@odata.context": "/redfish/v1/$metadata#DellJob.DellJob", "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Jobs/JID_861801613971", "@odata.type": "#DellJob.v1_0_0.DellJob", "CompletionTime": "2020-04-06T19:06:01", "Description": "Job Instance", "EndTime": null, "Id": "JID_861801613971", "JobState": "Completed", "JobType": "ImportConfiguration", "Message": "Successfully imported and applied Server Configuration Profile.", "MessageArgs": [], "MessageId": "SYS053", "Name": "Import Configuration", "PercentComplete": 100, "StartTime": "TIME_NOW", "Status": "Success", "TargetSettingsURI": null, "retval": true}` |

## [Status](idrac_timezone_ntp_module.md#id8)

- This module will be removed in a major release after 2024-07-31.
  *[deprecated]*
- For more information see [DEPRECATED](idrac_timezone_ntp_module.md#deprecated).

### Authors

- Felix Stephen (@felixs88)
- Anooja Vardhineni (@anooja-vardhineni)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
