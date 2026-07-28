---
collection: ansible
version: "8"
title: "dellemc.openmanage.ome_firmware_baseline_compliance_info module – Retrieves baseline compliance details on OpenManage Enterprise"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/ome_firmware_baseline_compliance_info_module.html
fetched_at: 2026-07-28T02:04:36+00:00
---
# dellemc.openmanage.ome_firmware_baseline_compliance_info module – Retrieves baseline compliance details on OpenManage Enterprise

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
> see [Requirements](ome_firmware_baseline_compliance_info_module.md#ansible-collections-dellemc-openmanage-ome-firmware-baseline-compliance-info-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_firmware_baseline_compliance_info`.

New in dellemc.openmanage 2.0.0

- [Synopsis](ome_firmware_baseline_compliance_info_module.md#synopsis)
- [Requirements](ome_firmware_baseline_compliance_info_module.md#requirements)
- [Parameters](ome_firmware_baseline_compliance_info_module.md#parameters)
- [Notes](ome_firmware_baseline_compliance_info_module.md#notes)
- [Examples](ome_firmware_baseline_compliance_info_module.md#examples)
- [Return Values](ome_firmware_baseline_compliance_info_module.md#return-values)

## [Synopsis](ome_firmware_baseline_compliance_info_module.md#id1)

- This module allows to retrieve firmware compliance for a list of devices, or against a specified baseline on OpenManage Enterprise.

## [Requirements](ome_firmware_baseline_compliance_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_firmware_baseline_compliance_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **baseline_name**  string | Name of the baseline, for which the device compliance report is generated.  This option is mandatory for generating baseline based device compliance report.  *baseline_name* is mutually exclusive with *device_ids*, *device_service_tags* and *device_group_names*. |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **device_group_names**  list / elements=string | A list of group names for device based compliance report.  Either *device_ids*, *device_service_tags* or *device_group_names* is required to generate device based compliance report.  *device_group_names* is mutually exclusive with *device_ids*, *device_service_tags* and *baseline_name*.  Devices without reports are ignored. |
| **device_ids**  list / elements=integer | A list of unique identifier for device based compliance report.  Either *device_ids*, *device_service_tags* or *device_group_names* is required to generate device based compliance report.  *device_ids* is mutually exclusive with *device_service_tags*, *device_group_names* and *baseline_name*.  Devices without reports are ignored. |
| **device_service_tags**  list / elements=string | A list of service tags for device based compliance report.  Either *device_ids*, *device_service_tags* or *device_group_names* is required to generate device based compliance report.  *device_service_tags* is mutually exclusive with *device_ids*, *device_group_names* and *baseline_name*.  Devices without reports are ignored. |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname. |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  **Default:** `443` |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ome_firmware_baseline_compliance_info_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to Dell OpenManage Enterprise.
> - This module supports `check_mode`.

## [Examples](ome_firmware_baseline_compliance_info_module.md#id5)

```yaml+jinja
---
- name: Retrieves device based compliance report for specified device IDs
  dellemc.openmanage.ome_firmware_baseline_compliance_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_ids:
        - 11111
        - 22222

- name: Retrieves device based compliance report for specified service Tags
  dellemc.openmanage.ome_firmware_baseline_compliance_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_service_tags:
        - MXL1234
        - MXL4567

- name: Retrieves device based compliance report for specified group names
  dellemc.openmanage.ome_firmware_baseline_compliance_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_group_names:
        - "group1"
        - "group2"

- name: Retrieves device compliance report for a specified baseline
  dellemc.openmanage.ome_firmware_baseline_compliance_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    baseline_name: "baseline_name"
```

## [Return Values](ome_firmware_baseline_compliance_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **baseline_compliance_info**  dictionary | Details of the baseline compliance report.  **Returned:** success  **Sample:** `[{"CatalogId": 53, "ComplianceSummary": {"ComplianceStatus": "CRITICAL", "NumberOfCritical": 2, "NumberOfDowngrade": 0, "NumberOfNormal": 0, "NumberOfWarning": 0}, "Description": "", "DeviceComplianceReports": [{"ComplianceStatus": "CRITICAL", "ComponentComplianceReports": [{"ComplianceDependencies": [], "ComplianceStatus": "DOWNGRADE", "Criticality": "Ok", "CurrentVersion": "OSC_1.1", "Id": 1258, "ImpactAssessment": "", "Name": "OS COLLECTOR 2.1", "Path": "FOLDER04118304M/2/Diagnostics_Application_JCCH7_WN64_4.0_A00_01.EXE", "PrerequisiteInfo": "", "RebootRequired": false, "SourceName": "DCIM:INSTALLED#802__OSCollector.Embedded.1", "TargetIdentifier": "101734", "UniqueIdentifier": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "UpdateAction": "DOWNGRADE", "Uri": "http://www.dell.com/support/home/us/en/19/Drivers/DriversDetails?driverId=XXXXX", "Version": "4.0"}, {"ComplianceDependencies": [], "ComplianceStatus": "CRITICAL", "Criticality": "Recommended", "CurrentVersion": "DN02", "Id": 1259, "ImpactAssessment": "", "Name": "TOSHIBA AL14SE 1.8 TB 2.5 12Gb 10K 512n SAS HDD Drive", "Path": "FOLDER04086111M/1/SAS-Drive_Firmware_VDGFM_WN64_DN03_A00.EXE", "PrerequisiteInfo": "", "RebootRequired": true, "SourceName": "DCIM:INSTALLED#304_C_Disk.Bay.1:Enclosure.Internal.0-1:RAID.Integrated.1-1", "TargetIdentifier": "103730", "UniqueIdentifier": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "UpdateAction": "UPGRADE", "Uri": "http://www.dell.com/support/home/us/en/19/Drivers/DriversDetails?driverId=XXXXX", "Version": "DN03"}], "DeviceId": 11603, "DeviceModel": "PowerEdge R630", "DeviceName": null, "DeviceTypeId": 1000, "DeviceTypeName": "CPGCGS", "FirmwareStatus": "Non-Compliant", "Id": 194, "RebootRequired": true, "ServiceTag": "MXL1234"}], "DowngradeEnabled": true, "Id": 53, "Is64Bit": false, "LastRun": "2019-09-27 05:08:16.301", "Name": "baseline1", "RepositoryId": 43, "RepositoryName": "catalog2", "RepositoryType": "CIFS", "Targets": [{"Id": 11603, "Type": {"Id": 1000, "Name": "DEVICE"}}], "TaskId": 11710, "TaskStatusId": 0}]` |
| **error_info**  dictionary | Details of http error.  **Returned:** on http error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to retrieve baseline list either because the device ID(s) entered are invalid", "Resolution": "Make sure the entered device ID(s) are valid and retry the operation.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Overall baseline compliance report status.  **Returned:** on error  **Sample:** `"Failed to fetch the compliance baseline information."` |

### Authors

- Sajna Shetty(@Sajna-Shetty)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
