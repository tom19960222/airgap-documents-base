---
collection: ansible
version: "6"
title: "dellemc.openmanage.ome_application_network_time module – Updates the network time on OpenManage Enterprise"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/ome_application_network_time_module.html
fetched_at: 2026-07-27T17:25:27+00:00
---
# dellemc.openmanage.ome_application_network_time module – Updates the network time on OpenManage Enterprise

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
> see [Requirements](ome_application_network_time_module.md#ansible-collections-dellemc-openmanage-ome-application-network-time-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_application_network_time`.

New in dellemc.openmanage 2.1.0

- [Synopsis](ome_application_network_time_module.md#synopsis)
- [Requirements](ome_application_network_time_module.md#requirements)
- [Parameters](ome_application_network_time_module.md#parameters)
- [Notes](ome_application_network_time_module.md#notes)
- [Examples](ome_application_network_time_module.md#examples)
- [Return Values](ome_application_network_time_module.md#return-values)

## [Synopsis](ome_application_network_time_module.md#id1)

- This module allows the configuration of network time on OpenManage Enterprise.

## [Requirements](ome_application_network_time_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_application_network_time_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **enable_ntp**  boolean / required | Enables or disables Network Time Protocol(NTP).  If *enable_ntp* is false, then the NTP addresses reset to their default values.  Choices:   - `false` - `true` |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname. |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  Default: `443` |
| **primary_ntp_address**  string | The primary NTP address.  This option is applicable when *enable_ntp* is true. |
| **secondary_ntp_address1**  string | The first secondary NTP address.  This option is applicable when *enable_ntp* is true. |
| **secondary_ntp_address2**  string | The second secondary NTP address.  This option is applicable when *enable_ntp* is true. |
| **system_time**  string | Time in the current system.  This option is only applicable when *enable_ntp* is false.  This option must be provided in following format ‘yyyy-mm-dd hh:mm:ss’. |
| **time_zone**  string | The valid timezone ID to be used.  This option is applicable for both system time and NTP time synchronization. |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](ome_application_network_time_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to DellEMC OpenManage Enterprise.
> - This module supports `check_mode`.

## [Examples](ome_application_network_time_module.md#id5)

```yaml+jinja
---
- name: Configure system time
  dellemc.openmanage.ome_application_network_time:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    enable_ntp: false
    system_time: "2020-03-31 21:35:18"
    time_zone: "TZ_ID_11"

- name: Configure NTP server for time synchronization
  dellemc.openmanage.ome_application_network_time:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    enable_ntp: true
    time_zone: "TZ_ID_66"
    primary_ntp_address: "192.168.0.2"
    secondary_ntp_address1: "192.168.0.2"
    secondary_ntp_address2: "192.168.0.4"
```

## [Return Values](ome_application_network_time_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP error.  Returned: on HTTP error  Sample: `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to complete the request because the input value for  SystemTime  is missing or an invalid value is entered.", "MessageArgs": ["SystemTime"], "MessageId": "CGEN6002", "RelatedProperties": [], "Resolution": "Enter a valid value and retry the operation.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Overall status of the network time configuration change.  Returned: always  Sample: `"Successfully configured network time."` |
| **proxy_configuration**  dictionary | Updated application network time configuration.  Returned: success  Sample: `{"EnableNTP": false, "JobId": null, "PrimaryNTPAddress": null, "SecondaryNTPAddress1": null, "SecondaryNTPAddress2": null, "SystemTime": null, "TimeSource": "Local Clock", "TimeZone": "TZ_ID_1", "TimeZoneIdLinux": null, "TimeZoneIdWindows": null, "UtcTime": null}` |

### Authors

- Sajna Shetty(@Sajna-Shetty)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
