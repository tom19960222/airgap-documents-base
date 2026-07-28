---
collection: ansible
version: "6"
title: "dellemc.openmanage.ome_firmware_baseline_info module – Retrieves baseline details from OpenManage Enterprise"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/ome_firmware_baseline_info_module.html
fetched_at: 2026-07-27T17:25:41+00:00
---
# dellemc.openmanage.ome_firmware_baseline_info module – Retrieves baseline details from OpenManage Enterprise

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
> see [Requirements](ome_firmware_baseline_info_module.md#ansible-collections-dellemc-openmanage-ome-firmware-baseline-info-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_firmware_baseline_info`.

New in dellemc.openmanage 2.0.0

- [Synopsis](ome_firmware_baseline_info_module.md#synopsis)
- [Requirements](ome_firmware_baseline_info_module.md#requirements)
- [Parameters](ome_firmware_baseline_info_module.md#parameters)
- [Notes](ome_firmware_baseline_info_module.md#notes)
- [Examples](ome_firmware_baseline_info_module.md#examples)
- [Return Values](ome_firmware_baseline_info_module.md#return-values)

## [Synopsis](ome_firmware_baseline_info_module.md#id1)

- This module retrieves the list and details of all the baselines on OpenManage Enterprise.

## [Requirements](ome_firmware_baseline_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_firmware_baseline_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **baseline_name**  string | Name of the baseline.If *baseline_name* is not provided, all the available firmware baselines are returned. |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname. |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  Default: `443` |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](ome_firmware_baseline_info_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to DellEMC OpenManage Enterprise.
> - This module supports `check_mode`.

## [Examples](ome_firmware_baseline_info_module.md#id5)

```yaml+jinja
---
- name: Retrieve details of all the available firmware baselines
  dellemc.openmanage.ome_firmware_baseline_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"

- name: Retrieve details of a specific firmware baseline identified by its baseline name
  dellemc.openmanage.ome_firmware_baseline_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    baseline_name: "baseline_name"
```

## [Return Values](ome_firmware_baseline_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **baseline_info**  dictionary | Details of the baselines.  Returned: success  Sample: `{"@odata.id": "/api/UpdateService/Baselines(239)", "@odata.type": "#UpdateService.Baselines", "CatalogId": 22, "ComplianceSummary": {"ComplianceStatus": "CRITICAL", "NumberOfCritical": 1, "NumberOfDowngrade": 0, "NumberOfNormal": 0, "NumberOfWarning": 0}, "Description": "baseline_description", "DeviceComplianceReports@odata.navigationLink": "/api/UpdateService/Baselines(239)/DeviceComplianceReports", "DowngradeEnabled": true, "Id": 239, "Is64Bit": true, "LastRun": "2020-05-22 16:42:40.307", "Name": "baseline_name", "RepositoryId": 12, "RepositoryName": "HTTP DELL", "RepositoryType": "DELL_ONLINE", "Targets": [{"Id": 10342, "Type": {"Id": 1000, "Name": "DEVICE"}}], "TaskId": 41415, "TaskStatusId": 2060}` |
| **msg**  string | Overall baseline information.  Returned: on error  Sample: `"Successfully fetched firmware baseline information."` |

### Authors

- Sajna Shetty(@Sajna-Shetty)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
