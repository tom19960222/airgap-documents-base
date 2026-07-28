---
collection: ansible
version: "8"
title: "dellemc.openmanage.ome_configuration_compliance_info module – Device compliance report for devices managed in OpenManage Enterprise"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/ome_configuration_compliance_info_module.html
fetched_at: 2026-07-28T02:04:25+00:00
---
# dellemc.openmanage.ome_configuration_compliance_info module – Device compliance report for devices managed in OpenManage Enterprise

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
> see [Requirements](ome_configuration_compliance_info_module.md#ansible-collections-dellemc-openmanage-ome-configuration-compliance-info-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_configuration_compliance_info`.

New in dellemc.openmanage 3.2.0

- [Synopsis](ome_configuration_compliance_info_module.md#synopsis)
- [Requirements](ome_configuration_compliance_info_module.md#requirements)
- [Parameters](ome_configuration_compliance_info_module.md#parameters)
- [Notes](ome_configuration_compliance_info_module.md#notes)
- [Examples](ome_configuration_compliance_info_module.md#examples)
- [Return Values](ome_configuration_compliance_info_module.md#return-values)

## [Synopsis](ome_configuration_compliance_info_module.md#id1)

- This module allows the generation of a compliance report of a specific or all of devices in a configuration compliance baseline.

## [Requirements](ome_configuration_compliance_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_configuration_compliance_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **baseline**  string / required | The name of the created baseline.  A compliance report is generated even when the template is not associated with the baseline. |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **device_id**  integer | The ID of the target device which is associated with the *baseline*. |
| **device_service_tag**  string | The device service tag of the target device associated with the *baseline*.  *device_service_tag* is mutually exclusive with *device_id*. |
| **hostname**  string / required | OpenManage Enterprise IP address or hostname. |
| **password**  string / required | OpenManage Enterprise password. |
| **port**  integer | OpenManage Enterprise HTTPS port.  **Default:** `443` |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **username**  string / required | OpenManage Enterprise username. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ome_configuration_compliance_info_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to Dell OpenManage Enterprise.
> - This module supports `check_mode`.

## [Examples](ome_configuration_compliance_info_module.md#id5)

```yaml+jinja
---
- name: Retrieve the compliance report of all of the devices in the specified configuration compliance baseline.
  dellemc.openmanage.ome_configuration_compliance_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    baseline: baseline_name

- name: Retrieve the compliance report for a specific device associated with the baseline using the device ID.
  dellemc.openmanage.ome_configuration_compliance_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    baseline: baseline_name
    device_id: 10001

- name: Retrieve the compliance report for a specific device associated with the baseline using the device service tag.
  dellemc.openmanage.ome_configuration_compliance_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    baseline: baseline_name
    device_service_tag: 2HFGH3
```

## [Return Values](ome_configuration_compliance_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **compliance_info**  dictionary | Returns the compliance report information.  **Returned:** success  **Sample:** `[{"ComplianceAttributeGroups": [{"Attributes": [], "ComplianceReason": "One or more attributes on the target device(s) does not match the compliance template.", "ComplianceStatus": 2, "ComplianceSubAttributeGroups": [{"Attributes": [{"AttributeId": 75369, "ComplianceReason": "Attribute has different value from template", "ComplianceStatus": 3, "CustomId": 0, "Description": null, "DisplayName": "Workload Profile", "ExpectedValue": "HpcProfile", "Value": "NotAvailable"}], "ComplianceReason": "One or more attributes on the target device(s) does not match the compliance template.", "ComplianceStatus": 2, "ComplianceSubAttributeGroups": [], "DisplayName": "System Profile Settings", "GroupNameId": 1}], "DisplayName": "BIOS", "GroupNameId": 1}], "ComplianceStatus": "NONCOMPLIANT", "DeviceName": "WIN-PLOV8MPIP40", "DeviceType": 1000, "Id": 25011, "InventoryTime": "2021-03-18 00:01:57.809771", "Model": "PowerEdge R7525", "ServiceTag": "JHMBX53"}]` |
| **error_info**  dictionary | Details of the HTTP Error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Over all compliance report status.  **Returned:** on error  **Sample:** `"Unable to complete the operation because the entered target baseline name 'baseline' is invalid."` |

### Authors

- Felix Stephen A (@felixs88)
- Kritika Bhateja (@Kritika-Bhateja)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
