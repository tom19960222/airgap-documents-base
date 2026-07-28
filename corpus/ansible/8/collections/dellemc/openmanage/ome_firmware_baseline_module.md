---
collection: ansible
version: "8"
title: "dellemc.openmanage.ome_firmware_baseline module – Create, modify, or delete a firmware baseline on OpenManage Enterprise or OpenManage Enterprise Modular"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/ome_firmware_baseline_module.html
fetched_at: 2026-07-28T02:04:36+00:00
---
# dellemc.openmanage.ome_firmware_baseline module – Create, modify, or delete a firmware baseline on OpenManage Enterprise or OpenManage Enterprise Modular

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
> see [Requirements](ome_firmware_baseline_module.md#ansible-collections-dellemc-openmanage-ome-firmware-baseline-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_firmware_baseline`.

New in dellemc.openmanage 2.0.0

- [Synopsis](ome_firmware_baseline_module.md#synopsis)
- [Requirements](ome_firmware_baseline_module.md#requirements)
- [Parameters](ome_firmware_baseline_module.md#parameters)
- [Notes](ome_firmware_baseline_module.md#notes)
- [Examples](ome_firmware_baseline_module.md#examples)
- [Return Values](ome_firmware_baseline_module.md#return-values)

## [Synopsis](ome_firmware_baseline_module.md#id1)

- This module allows to create, modify, or delete a firmware baseline on OpenManage Enterprise or OpenManage Enterprise Modular.

## [Requirements](ome_firmware_baseline_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_firmware_baseline_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **baseline_description**  string | Description for the baseline being created. |
| **baseline_id**  integer  *added in dellemc.openmanage 3.4.0* | ID of the existing baseline.  This option is mutually exclusive with *baseline_name*. |
| **baseline_name**  string | Name of the the baseline.  This option is mutually exclusive with *baseline_id*. |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **catalog_name**  string | Name of the catalog to be associated with the baseline. |
| **device_group_names**  list / elements=string | List of group names.  This option is mutually exclusive with *device_ids* and *device_service_tags*. |
| **device_ids**  list / elements=integer | List of device IDs.  This option is mutually exclusive with *device_service_tags* and *device_group_names*. |
| **device_service_tags**  list / elements=string | List of device service tags.  This option is mutually exclusive with *device_ids* and *device_group_names*. |
| **downgrade_enabled**  boolean | Indicates whether firmware downgrade is allowed for the devices in the baseline.  This value will be set to `True` by default, if not provided during baseline creation.  **Choices:**   - `false` - `true` |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname. |
| **is_64_bit**  boolean | Indicates if the repository contains 64-bit DUPs.  This value will be set to `True` by default, if not provided during baseline creation.  **Choices:**   - `false` - `true` |
| **job_wait**  boolean  *added in dellemc.openmanage 3.4.0* | Provides the option to wait for job completion.  This option is applicable when *state* is `present`.  **Choices:**   - `false` - `true` ← (default) |
| **job_wait_timeout**  integer  *added in dellemc.openmanage 3.4.0* | The maximum wait time of *job_wait* in seconds. The job is tracked only for this duration.  This option is applicable when *job_wait* is `True`.  **Default:** `600` |
| **new_baseline_name**  string  *added in dellemc.openmanage 3.4.0* | New name of the baseline. |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  **Default:** `443` |
| **state**  string  *added in dellemc.openmanage 3.4.0* | `present` creates or modifies a baseline.  `absent` deletes an existing baseline.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ome_firmware_baseline_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to Dell OpenManage Enterprise or OpenManage Enterprise Modular.
> - *device_group_names* option is not applicable for OpenManage Enterprise Modular.
> - This module supports `check_mode`.

## [Examples](ome_firmware_baseline_module.md#id5)

```yaml+jinja
---
- name: Create baseline for device IDs
  dellemc.openmanage.ome_firmware_baseline:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    baseline_name: "baseline_name"
    baseline_description: "baseline_description"
    catalog_name: "catalog_name"
    device_ids:
      - 1010
      - 2020

- name: Create baseline for servicetags
  dellemc.openmanage.ome_firmware_baseline:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    baseline_name: "baseline_name"
    baseline_description: "baseline_description"
    catalog_name: "catalog_name"
    device_service_tags:
      - "SVCTAG1"
      - "SVCTAG2"

- name: Create baseline for device groups without job tracking
  dellemc.openmanage.ome_firmware_baseline:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    baseline_name: "baseline_name"
    baseline_description: "baseline_description"
    catalog_name: "catalog_name"
    device_group_names:
      - "Group1"
      - "Group2"
    job_wait: no

- name: Modify an existing baseline
  dellemc.openmanage.ome_firmware_baseline:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    baseline_name: "existing_baseline_name"
    new_baseline_name: "new_baseline_name"
    baseline_description: "new baseline_description"
    catalog_name: "catalog_other"
    device_group_names:
      - "Group3"
      - "Group4"
      - "Group5"
    downgrade_enabled: no
    is_64_bit: yes

- name: Delete a baseline
  dellemc.openmanage.ome_firmware_baseline:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: absent
    baseline_name: "baseline_name"
```

## [Return Values](ome_firmware_baseline_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **baseline_id**  integer | ID of the deleted baseline.  **Returned:** When *state* is `absent`  **Sample:** `10123` |
| **baseline_status**  dictionary | Details of the baseline status.  **Returned:** success  **Sample:** `{"CatalogId": 123, "Description": "BASELINE DESCRIPTION", "DeviceComplianceReports": [], "DowngradeEnabled": true, "Id": 23, "Is64Bit": true, "Name": "my_baseline", "RepositoryId": 123, "RepositoryName": "catalog123", "RepositoryType": "HTTP", "Targets": [{"Id": 10083, "Type": {"Id": 1000, "Name": "DEVICE"}}, {"Id": 10076, "Type": {"Id": 1000, "Name": "DEVICE"}}], "TaskId": 11235, "TaskStatusId": 2060}` |
| **error_info**  dictionary | Details of http error.  **Returned:** on http error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to retrieve baseline list either because the device ID(s) entered are invalid", "Resolution": "Make sure the entered device ID(s) are valid and retry the operation.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **job_id**  integer | Job ID of the baseline task.  **Returned:** When baseline job is in running state  **Sample:** `10123` |
| **msg**  string | Overall status of the firmware baseline operation.  **Returned:** always  **Sample:** `"Successfully created the firmware baseline."` |

### Authors

- Jagadeesh N V(@jagadeeshnv)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
