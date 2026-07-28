---
collection: ansible
version: "6"
title: "dellemc.openmanage.ome_diagnostics module – Export technical support logs(TSR) to network share location"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/ome_diagnostics_module.html
fetched_at: 2026-07-27T17:25:37+00:00
---
# dellemc.openmanage.ome_diagnostics module – Export technical support logs(TSR) to network share location

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
> see [Requirements](ome_diagnostics_module.md#ansible-collections-dellemc-openmanage-ome-diagnostics-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_diagnostics`.

New in dellemc.openmanage 3.6.0

- [Synopsis](ome_diagnostics_module.md#synopsis)
- [Requirements](ome_diagnostics_module.md#requirements)
- [Parameters](ome_diagnostics_module.md#parameters)
- [Notes](ome_diagnostics_module.md#notes)
- [Examples](ome_diagnostics_module.md#examples)
- [Return Values](ome_diagnostics_module.md#return-values)

## [Synopsis](ome_diagnostics_module.md#id1)

- This module allows to export SupportAssist collection logs from OpenManage Enterprise and OpenManage Enterprise Modular and application logs from OpenManage Enterprise Modular to a CIFS or NFS share.

## [Requirements](ome_diagnostics_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_diagnostics_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **device_group_name**  string | Name of the device group to export `support_assist_collection` or `supportassist_collection` logs of all devices within the group.  This is applicable for `support_assist_collection` and `supportassist_collection` logs.  This option is not applicable for OpenManage Enterprise Modular.  This option is mutually exclusive with *device_ids* and *device_service_tags*. |
| **device_ids**  list / elements=integer | List of target device IDs.  This is applicable for `support_assist_collection` and `supportassist_collection` logs.  This option is mutually exclusive with *device_service_tags* and *device_group_name*. |
| **device_service_tags**  list / elements=string | List of target identifier.  This is applicable for `support_assist_collection` and `supportassist_collection` logs.  This option is mutually exclusive with *device_ids* and *device_group_name*. |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname. |
| **job_wait**  boolean | Whether to wait for the Job completion or not.  The maximum wait time is *job_wait_timeout*.  Choices:   - `false` - `true` ← (default) |
| **job_wait_timeout**  integer | The maximum wait time of *job_wait* in minutes.  This option is applicable *job_wait* is true.  Default: `60` |
| **lead_chassis_only**  boolean | Extract the logs from Lead chassis only.  *lead_chassis_only* is only applicable when *log_type* is `application` on OpenManage Enterprise Modular.  Choices:   - `false` ← (default) - `true` |
| **log_selectors**  list / elements=string | By default, the SupportAssist logs contain only hardware logs. To collect additional logs such as OS logs, RAID logs or Debug logs, specify the log types to be collected in the choices list.  If the log types are not specified, only the hardware logs are exported.  `OS_LOGS` to collect OS Logs.  `RAID_LOGS` to collect RAID controller logs.  `DEBUG_LOGS` to collect Debug logs.  This option is applicable only for `support_assist_collection` and `supportassist_collection` of *log_type*.  Choices:   - `"OS_LOGS"` - `"RAID_LOGS"` - `"DEBUG_LOGS"` |
| **log_type**  string | `application` is applicable for OpenManage Enterprise Modular to export the application log bundle.  `support_assist_collection` and `supportassist_collection` is applicable for one or more devices to export SupportAssist logs.  `support_assist_collection` and `supportassist_collection` supports both OpenManage Enterprise and OpenManage Enterprise Modular.  `support_assist_collection` and `supportassist_collection` does not support export of `OS_LOGS` from OpenManage Enterprise. If tried to export, the tasks will complete with errors, and the module fails.  Choices:   - `"application"` - `"support_assist_collection"` ← (default) - `"supportassist_collection"` |
| **mask_sensitive_info**  boolean | Select this option to mask the personal identification information such as IPAddress, DNS, alert destination, email, gateway, inet6, MacAddress, netmask etc.  This option is applicable for `application` of *log_type*.  Choices:   - `false` ← (default) - `true` |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  Default: `443` |
| **share_address**  string / required | Network share IP address. |
| **share_domain**  string | Network share domain name.  This option is applicable for `CIFS` if *share_type*. |
| **share_name**  string / required | Network share path.  Filename is auto generated and should not be provided as part of *share_name*. |
| **share_password**  string | Network share password  This option is applicable for `CIFS` of *share_type*. |
| **share_type**  string / required | Network share type  Choices:   - `"NFS"` - `"CIFS"` |
| **share_user**  string | Network share username.  This option is applicable for `CIFS` of *share_type*. |
| **test_connection**  boolean | Test the availability of the network share location.  *job_wait* and *job_wait_timeout* options are not applicable for *test_connection*.  Choices:   - `false` ← (default) - `true` |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](ome_diagnostics_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to OpenManage Enterprise.
> - This module performs the test connection and device validations. It does not create a job for copying the logs in check mode and always reports as changes found.
> - This module supports `check_mode`.

## [Examples](ome_diagnostics_module.md#id5)

```yaml+jinja
---
- name: Export application log using CIFS share location
  dellemc.openmanage.ome_diagnostics:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    share_type: CIFS
    share_address: "192.168.0.2"
    share_user: share_username
    share_password: share_password
    share_name: cifs_share
    log_type: application
    mask_sensitive_info: false
    test_connection: true

- name: Export application log using NFS share location
  dellemc.openmanage.ome_diagnostics:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    share_address: "192.168.0.3"
    share_type: NFS
    share_name: nfs_share
    log_type: application
    mask_sensitive_info: true
    test_connection: true

- name: Export SupportAssist log using CIFS share location
  dellemc.openmanage.ome_diagnostics:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    share_address: "192.168.0.3"
    share_user: share_username
    share_password: share_password
    share_name: cifs_share
    share_type: CIFS
    log_type: support_assist_collection
    device_ids: [10011, 10022]
    log_selectors: [OS_LOGS]
    test_connection: true

- name: Export SupportAssist log using NFS share location
  dellemc.openmanage.ome_diagnostics:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    share_address: "192.168.0.3"
    share_type: NFS
    share_name: nfs_share
    log_type: support_assist_collection
    device_group_name: group_name
    test_connection: true
```

## [Return Values](ome_diagnostics_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  Returned: on HTTP error  Sample: `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **jog_status**  dictionary | Details of the export log operation status.  Returned: success  Sample: `{"Builtin": false, "CreatedBy": "root", "Editable": true, "EndTime": "None", "Id": 12778, "JobDescription": "Export device log", "JobName": "Export Log", "JobStatus": {"Id": 2080, "Name": "New"}, "JobType": {"Id": 18, "Internal": false, "Name": "DebugLogs_Task"}, "LastRun": "2021-07-06 10:52:50.519", "LastRunStatus": {"Id": 2060, "Name": "Completed"}, "NextRun": "None", "Params": [{"JobId": 12778, "Key": "maskSensitiveInfo", "Value": "FALSE"}, {"JobId": 12778, "Key": "password", "Value": "tY86w7q92u0QzvykuF0gQQ"}, {"JobId": 12778, "Key": "userName", "Value": "administrator"}, {"JobId": 12778, "Key": "shareName", "Value": "iso"}, {"JobId": 12778, "Key": "OPERATION_NAME", "Value": "EXTRACT_LOGS"}, {"JobId": 12778, "Key": "shareType", "Value": "CIFS"}, {"JobId": 12778, "Key": "shareAddress", "Value": "100.96.32.142"}], "Schedule": "startnow", "StartTime": "None", "State": "Enabled", "Targets": [{"Data": "", "Id": 10053, "JobId": 12778, "TargetType": {"Id": 1000, "Name": "DEVICE"}}], "UpdatedBy": "None", "UserGenerated": true, "Visible": true}` |
| **msg**  string | Overall status of the export log.  Returned: always  Sample: `"Export log job completed successfully."` |

### Authors

- Felix Stephen (@felixs88)
- Sachin Apagundi(@sachin-apa)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
