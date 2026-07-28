---
collection: ansible
version: "8"
title: "dellemc.openmanage.ome_application_console_preferences module – Configure console preferences on OpenManage Enterprise."
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/ome_application_console_preferences_module.html
fetched_at: 2026-07-28T02:04:19+00:00
---
# dellemc.openmanage.ome_application_console_preferences module – Configure console preferences on OpenManage Enterprise.

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
> see [Requirements](ome_application_console_preferences_module.md#ansible-collections-dellemc-openmanage-ome-application-console-preferences-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_application_console_preferences`.

New in dellemc.openmanage 5.2.0

- [Synopsis](ome_application_console_preferences_module.md#synopsis)
- [Requirements](ome_application_console_preferences_module.md#requirements)
- [Parameters](ome_application_console_preferences_module.md#parameters)
- [Notes](ome_application_console_preferences_module.md#notes)
- [Examples](ome_application_console_preferences_module.md#examples)
- [Return Values](ome_application_console_preferences_module.md#return-values)

## [Synopsis](ome_application_console_preferences_module.md#id1)

- This module allows user to configure the console preferences on OpenManage Enterprise.

## [Requirements](ome_application_console_preferences_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_application_console_preferences_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **builtin_appliance_share**  dictionary | The external network share that the appliance must access to complete operations. |
| **cifs_options**  string | The SMB protocol version.  *cifs_options* is required *share_options* is `CIFS`.  `V1` to enable SMBv1.  `V2` to enable SMBv2  **Choices:**   - `"V1"` - `"V2"` |
| **share_options**  string | The share options.  `CIFS` to select CIFS share type.  `HTTPS` to select HTTPS share type.  **Choices:**   - `"CIFS"` - `"HTTPS"` |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **device_health**  dictionary | The time after which the health of the devices must be automatically monitored and updated on the OpenManage Enterprise dashboard. |
| **health_and_power_state_on_connection_lost**  string | The latest recorded device health.  `last_known` to display the latest recorded device health when the power connection was lost.  `unknown` to display the latest recorded device health when the device status moved to unknown.  **Choices:**   - `"last_known"` - `"unknown"` |
| **health_check_interval**  integer | The frequency at which the device health must be recorded and data stored. |
| **health_check_interval_unit**  string | The time unit of the frequency at which the device health must be recorded and data stored.  `Hourly` to set the frequency in hours.  `Minutes` to set the frequency in minutes.  **Choices:**   - `"Hourly"` - `"Minutes"` |
| **discovery_settings**  dictionary | The device naming to be used by the OpenManage Enterprise to identify the discovered iDRACs and other devices. |
| **common_mac_addresses**  string | The common MAC addresses separated by a comma. |
| **general_device_naming**  string | Applicable to all the discovered devices other than the iDRACs.  `DNS` to use the DNS name.  `NETBIOS` to use the NetBIOS name.  **Choices:**   - `"DNS"` ← (default) - `"NETBIOS"` |
| **invalid_device_hostname**  string | The invalid hostnames separated by a comma. |
| **server_device_naming**  string | Applicable to iDRACs only.  `IDRAC_HOSTNAME` to use the iDRAC hostname.  `IDRAC_SYSTEM_HOSTNAME` to use the system hostname.  **Choices:**   - `"IDRAC_HOSTNAME"` - `"IDRAC_SYSTEM_HOSTNAME"` ← (default) |
| **email_sender_settings**  string | The email address of the user who is sending an email message. |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname. |
| **metrics_collection_settings**  integer | The frequency of the PowerManager extension data maintenance and purging. |
| **mx7000_onboarding_preferences**  string | Alert-forwarding behavior on chassis when they are onboarded.  `all` to receive all alert.  `chassis` to receive chassis category alerts only.  **Choices:**   - `"all"` - `"chassis"` |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  **Default:** `443` |
| **report_row_limit**  integer | The maximum number of rows that you can view on OpenManage Enterprise reports. |
| **server_initiated_discovery**  dictionary | Server initiated discovery settings. |
| **device_discovery_approval_policy**  string | Discovery approval policies.  `Automatic` allows servers with iDRAC Firmware version 4.00.00.00, which are on the same network as the console, to be discovered automatically by the console.  `Manual` for the servers to be discovered by the user manually.  **Choices:**   - `"Automatic"` - `"Manual"` |
| **set_trap_destination**  boolean | Trap destination settings.  **Choices:**   - `false` - `true` |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **trap_forwarding_format**  string | The trap forwarding format.  `Original` to retain the trap data as is.  `Normalized` to normalize the trap data.  **Choices:**   - `"Original"` - `"Normalized"` |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ome_application_console_preferences_module.md#id4)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ome_application_console_preferences_module.md#id5)

```yaml+jinja
---
- name: Update Console preferences with all the settings.
  dellemc.openmanage.ome_application_console_preferences:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    report_row_limit: 123
    device_health:
      health_check_interval: 1
      health_check_interval_unit: Hourly
      health_and_power_state_on_connection_lost: last_known
    discovery_settings:
      general_device_naming: DNS
      server_device_naming: IDRAC_HOSTNAME
      invalid_device_hostname: "localhost"
      common_mac_addresses: "::"
    server_initiated_discovery:
      device_discovery_approval_policy: Automatic
      set_trap_destination: True
    mx7000_onboarding_preferences: all
    builtin_appliance_share:
      share_options: CIFS
      cifs_options: V1
    email_sender_settings: "admin@dell.com"
    trap_forwarding_format: Normalized
    metrics_collection_settings: 31

- name: Update Console preferences with report and device health settings.
  dellemc.openmanage.ome_application_console_preferences:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    report_row_limit: 236
    device_health:
      health_check_interval: 10
      health_check_interval_unit: Hourly
      health_and_power_state_on_connection_lost: last_known

- name: Update Console preferences with invalid device health settings.
  dellemc.openmanage.ome_application_console_preferences:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_health:
      health_check_interval: 65
      health_check_interval_unit: Minutes

- name: Update Console preferences with discovery and built in appliance share settings.
  dellemc.openmanage.ome_application_console_preferences:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    discovery_settings:
      general_device_naming: DNS
      server_device_naming: IDRAC_SYSTEM_HOSTNAME
      invalid_device_hostname: "localhost"
      common_mac_addresses: "00:53:45:00:00:00"
    builtin_appliance_share:
      share_options: CIFS
      cifs_options: V1

- name: Update Console preferences with server initiated discovery, mx7000 onboarding preferences, email sender,
    trap forwarding format, and metrics collection settings.
  dellemc.openmanage.ome_application_console_preferences:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    server_initiated_discovery:
      device_discovery_approval_policy: Automatic
      set_trap_destination: True
    mx7000_onboarding_preferences: chassis
    email_sender_settings: "admin@dell.com"
    trap_forwarding_format: Original
    metrics_collection_settings: 365
```

## [Return Values](ome_application_console_preferences_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **console_preferences**  list / elements=string | Details of the console preferences.  **Returned:** on success  **Sample:** `[{"DataType": "java.lang.String", "DefaultValue": "SLOT_NAME", "GroupName": "DISCOVERY_SETTING", "Name": "DEVICE_PREFERRED_NAME", "Value": "PREFER_DNS,PREFER_IDRAC_SYSTEM_HOSTNAME"}, {"DataType": "java.lang.String", "DefaultValue": "", "GroupName": "DISCOVERY_SETTING", "Name": "INVALID_DEVICE_HOSTNAME", "Value": "localhost,localhost.localdomain,not defined,pv132t,pv136t,default,dell,idrac-"}, {"DataType": "java.lang.String", "DefaultValue": "", "GroupName": "DISCOVERY_SETTING", "Name": "COMMON_MAC_ADDRESSES", "Value": "00:53:45:00:00:00,33:50:6F:45:30:30,50:50:54:50:30:30,00:00:FF:FF:FF:FF,20:41:53:59:4E:FF,00:00:00:00:00:00,20:41:53:59:4e:ff,00:00:00:00:00:00"}, {"DataType": "java.lang.String", "DefaultValue": "CIFS", "GroupName": "BUILT_IN_APPLIANCE_SHARE_SETTINGS", "Name": "SHARE_TYPE", "Value": "CIFS"}, {"DataType": "java.lang.String", "DefaultValue": "AsIs", "GroupName": "", "Name": "TRAP_FORWARDING_SETTING", "Value": "Normalized"}, {"DataType": "java.lang.Integer", "DefaultValue": "365", "GroupName": "", "Name": "DATA_PURGE_INTERVAL", "Value": "3650000"}, {"DataType": "java.lang.String", "DefaultValue": "last_known", "GroupName": "CONSOLE_CONNECTION_SETTING", "Name": "CONSOLE_CONNECTION_SETTING", "Value": "last_known"}, {"DataType": "java.lang.String", "DefaultValue": "V2", "GroupName": "CIFS_PROTOCOL_SETTINGS", "Name": "MIN_PROTOCOL_VERSION", "Value": "V1"}, {"DataType": "java.lang.Integer", "DefaultValue": "2000", "GroupName": "", "Name": "ALERT_ACKNOWLEDGEMENT_VIEW", "Value": "2000"}, {"DataType": "java.lang.Boolean", "DefaultValue": "false", "GroupName": "CONSOLE_UPDATE_SETTING_GROUP", "Name": "AUTO_CONSOLE_UPDATE_AFTER_DOWNLOAD", "Value": "false"}, {"DataType": "java.lang.Boolean", "DefaultValue": "false", "GroupName": "", "Name": "NODE_INITIATED_DISCOVERY_SET_TRAP_DESTINATION", "Value": "false"}, {"DataType": "java.lang.Integer", "DefaultValue": "0", "GroupName": "", "Name": "REPORTS_MAX_RESULTS_LIMIT", "Value": "2000000000000000000000000"}, {"DataType": "java.lang.String", "DefaultValue": "omcadmin@dell.com", "GroupName": "", "Name": "EMAIL_SENDER", "Value": "admin1@dell.com@dell.com@dell.com"}, {"DataType": "java.lang.String", "DefaultValue": "all", "GroupName": "", "Name": "MX7000_ONBOARDING_PREF", "Value": "test_chassis"}, {"DataType": "java.lang.String", "DefaultValue": "Automatic", "GroupName": "", "Name": "DISCOVERY_APPROVAL_POLICY", "Value": "Automatic_test"}]` |
| **error_info**  dictionary | Details of the HTTP error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to complete the request because the resource URI does not exist or is not implemented.", "MessageArgs": [], "MessageId": "CGEN1006", "RelatedProperties": [], "Resolution": "Enter a valid URI and retry the operation.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Overall status of the console preferences.  **Returned:** always  **Sample:** `"Successfully update the console preferences."` |

### Authors

- Sachin Apagundi(@sachin-apa)
- Husniya Hameed (@husniya-hameed)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
