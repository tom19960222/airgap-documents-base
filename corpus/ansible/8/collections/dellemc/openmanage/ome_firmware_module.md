---
collection: ansible
version: "8"
title: "dellemc.openmanage.ome_firmware module – Update firmware on PowerEdge devices and its components through OpenManage Enterprise"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/ome_firmware_module.html
fetched_at: 2026-07-28T02:04:35+00:00
---
# dellemc.openmanage.ome_firmware module – Update firmware on PowerEdge devices and its components through OpenManage Enterprise

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
> see [Requirements](ome_firmware_module.md#ansible-collections-dellemc-openmanage-ome-firmware-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_firmware`.

New in dellemc.openmanage 2.0.0

- [Synopsis](ome_firmware_module.md#synopsis)
- [Requirements](ome_firmware_module.md#requirements)
- [Parameters](ome_firmware_module.md#parameters)
- [Notes](ome_firmware_module.md#notes)
- [Examples](ome_firmware_module.md#examples)
- [Return Values](ome_firmware_module.md#return-values)

## [Synopsis](ome_firmware_module.md#id1)

- This module updates the firmware of PowerEdge devices and all its components through OpenManage Enterprise.

## [Requirements](ome_firmware_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_firmware_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **baseline_name**  string | Enter the baseline name to update the firmware of all devices or list of devices that are not complaint.  This option is mutually exclusive with *dup_file* and *device_group_names*. |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **components**  list / elements=string | List of components to be updated.  If not provided, all components applicable are considered.  This option is case sensitive.  This is applicable to *device_service_tag*, *device_id*, and *baseline_name*.  **Default:** `[]` |
| **device_group_names**  list / elements=string | Enter the name of the device group that contains the devices on which firmware needs to be updated.  This option is mutually exclusive with *device_id* and *device_service_tag*. |
| **device_id**  list / elements=integer | List of ids of the targeted device.  Either *device_id* or *device_service_tag* can be used individually or together.  This option is mutually exclusive with *device_group_names* and *devices*. |
| **device_service_tag**  list / elements=string | List of service tags of the targeted devices.  Either *device_id* or *device_service_tag* can be used individually or together.  This option is mutually exclusive with *device_group_names* and *devices*. |
| **devices**  list / elements=dictionary | This option allows to select components on each device for firmware update.  This option is mutually exclusive with *dup_file*, *device_group_names*, *device_id*, and *device_service_tag*. |
| **components**  list / elements=string | The target components to be updated. If not specified, all applicable device components are considered.  **Default:** `[]` |
| **id**  integer | The id of the target device to be updated.  This option is mutually exclusive with *service_tag*. |
| **service_tag**  string | The service tag of the target device to be updated.  This option is mutually exclusive with *id*. |
| **dup_file**  path | The path of the Dell Update Package (DUP) file that contains the firmware or drivers required to update the target system device or individual device components.  This is mutually exclusive with *baseline_name*, *components*, and *devices*. |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname. |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  **Default:** `443` |
| **schedule**  string | Select the schedule for the firmware update.  if `StageForNextReboot` is chosen, the firmware will be staged and updated during the next reboot of the target device.  if `RebootNow` will apply the firmware updates immediately.  **Choices:**   - `"RebootNow"` ← (default) - `"StageForNextReboot"` |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ome_firmware_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to Dell OpenManage Enterprise.
> - This module supports `check_mode`.

## [Examples](ome_firmware_module.md#id5)

```yaml+jinja
---
- name: Update firmware from DUP file using device ids
  dellemc.openmanage.ome_firmware:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_id:
      - 11111
      - 22222
    dup_file: "/path/Chassis-System-Management_Firmware_6N9WN_WN64_1.00.01_A00.EXE"

- name: Update firmware from a DUP file using a device service tags
  dellemc.openmanage.ome_firmware:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_service_tag:
      - KLBR111
      - KLBR222
    dup_file: "/path/Network_Firmware_NTRW0_WN64_14.07.07_A00-00_01.EXE"

- name: Update firmware from a DUP file using a device group names
  dellemc.openmanage.ome_firmware:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_group_names:
      - servers
    dup_file: "/path/BIOS_87V69_WN64_2.4.7.EXE"

- name: Update firmware using baseline name
  dellemc.openmanage.ome_firmware:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    baseline_name: baseline_devices

- name: Stage firmware for the next reboot using baseline name
  dellemc.openmanage.ome_firmware:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    baseline_name: baseline_devices
    schedule: StageForNextReboot

- name: "Update firmware using baseline name and components."
  dellemc.openmanage.ome_firmware:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    baseline_name: baseline_devices
    components:
      - BIOS

- name: Update firmware of device components from a DUP file using a device ids in a baseline
  dellemc.openmanage.ome_firmware:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    baseline_name: baseline_devices
    device_id:
      - 11111
      - 22222
    components:
      - iDRAC with Lifecycle Controller

- name: Update firmware of device components from a baseline using a device service tags under a baseline
  dellemc.openmanage.ome_firmware:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    baseline_name: baseline_devices
    device_service_tag:
      - KLBR111
      - KLBR222
    components:
      - IOM-SAS

- name: Update firmware using baseline name with a device id and required components
  dellemc.openmanage.ome_firmware:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    baseline_name: baseline_devices
    devices:
      - id: 12345
        components:
         - Lifecycle Controller
      - id: 12346
        components:
          - Enterprise UEFI Diagnostics
          - BIOS

- name: "Update firmware using baseline name with a device service tag and required components."
  dellemc.openmanage.ome_firmware:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    baseline_name: baseline_devices
    devices:
      - service_tag: ABCDE12
        components:
          - PERC H740P Adapter
          - BIOS
      - service_tag: GHIJK34
        components:
          - OS Drivers Pack

- name: "Update firmware using baseline name with a device service tag or device id and required components."
  dellemc.openmanage.ome_firmware:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    baseline_name: baseline_devices
    devices:
      - service_tag: ABCDE12
        components:
          - BOSS-S1 Adapter
          - PowerEdge Server BIOS
      - id: 12345
        components:
          - iDRAC with Lifecycle Controller
```

## [Return Values](ome_firmware_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Overall firmware update status.  **Returned:** always  **Sample:** `"Successfully submitted the firmware update job."` |
| **update_status**  dictionary | The firmware update job and progress details from the OME.  **Returned:** success  **Sample:** `{"Builtin": false, "CreatedBy": "user", "Editable": true, "EndTime": "None", "Id": 11117, "JobDescription": "dup test", "JobName": "Firmware Update Task", "JobStatus": {"Id": 1111, "Name": "New"}, "JobType": {"Id": 5, "Internal": false, "Name": "Update_Task"}, "LastRun": "None", "LastRunStatus": {"Id": 1111, "Name": "NotRun"}, "NextRun": "None", "Params": [{"JobId": 11111, "Key": "signVerify", "Value": "true"}, {"JobId": 11112, "Key": "stagingValue", "Value": "false"}, {"JobId": 11113, "Key": "complianceUpdate", "Value": "false"}, {"JobId": 11114, "Key": "operationName", "Value": "INSTALL_FIRMWARE"}], "Schedule": "startnow", "StartTime": "None", "State": "Enabled", "Targets": [{"Data": "DCIM:INSTALLED#701__NIC.Mezzanine.1A-1-1=1234567654321", "Id": 11115, "JobId": 11116, "TargetType": {"Id": 1000, "Name": "DEVICE"}}], "UpdatedBy": "None", "Visible": true}` |

### Authors

- Felix Stephen (@felixs88)
- Jagadeesh N V (@jagadeeshnv)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
