---
collection: ansible
version: "8"
title: "dellemc.openmanage.ome_devices module – Perform device-specific operations on target devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/ome_devices_module.html
fetched_at: 2026-07-28T02:04:32+00:00
---
# dellemc.openmanage.ome_devices module – Perform device-specific operations on target devices

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
> see [Requirements](ome_devices_module.md#ansible-collections-dellemc-openmanage-ome-devices-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_devices`.

New in dellemc.openmanage 6.1.0

- [Synopsis](ome_devices_module.md#synopsis)
- [Requirements](ome_devices_module.md#requirements)
- [Parameters](ome_devices_module.md#parameters)
- [Notes](ome_devices_module.md#notes)
- [Examples](ome_devices_module.md#examples)
- [Return Values](ome_devices_module.md#return-values)

## [Synopsis](ome_devices_module.md#id1)

- Perform device-specific operations such as refresh inventory, clear iDRAC job queue, and reset iDRAC from OpenManage Enterprise.

## [Requirements](ome_devices_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_devices_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **device_action**  string | `refresh_inventory` refreshes the inventory on the target devices.  `reset_idrac` Triggers a reset on the target iDRACs.  `clear_idrac_job_queue` Clears the job queue on the target iDRACs.  A job is triggered for each action.  **Choices:**   - `"refresh_inventory"` ← (default) - `"reset_idrac"` - `"clear_idrac_job_queue"` |
| **device_ids**  list / elements=integer | IDs of the target devices.  This is mutually exclusive with *device_service_tags*. |
| **device_service_tags**  list / elements=string | Service tag of the target devices.  This is mutually exclusive with *device_ids*. |
| **hostname**  string / required | OpenManage Enterprise IP address or hostname. |
| **job_description**  string | Optional description for the job. |
| **job_name**  string | Optional name for the job. |
| **job_schedule**  string | Provide the cron string to schedule the job.  **Default:** `"startnow"` |
| **job_wait**  boolean | Provides an option to wait for the job completion.  This option is applicable when *state* is `present`.  This is applicable when *job_schedule* is `startnow`.  **Choices:**   - `false` - `true` ← (default) |
| **job_wait_timeout**  integer | The maximum wait time of *job_wait* in seconds. The job is tracked only for this duration.  This option is applicable when *job_wait* is `True`.  **Default:** `1200` |
| **password**  string / required | OpenManage Enterprise password. |
| **port**  integer | OpenManage Enterprise HTTPS port.  **Default:** `443` |
| **state**  string | `present` Allows to perform the *device_action* on the target devices.  `absent` Removes the device from OpenManage Enterprise. Job is not triggered. *job_wait*, *job_schedule*, *job_name*, and *job_description* are not applicable to this operation.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **username**  string / required | OpenManage Enterprise username. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ome_devices_module.md#id4)

> **Note:**
>
> - For `idrac_reset`, the job triggers only the iDRAC reset operation and does not track the complete reset cycle.
> - Run this module from a system that has direct access to Dell OpenManage Enterprise.
> - This module supports `check_mode`.

## [Examples](ome_devices_module.md#id5)

```yaml+jinja
---
- name: Refresh Inventory
  dellemc.openmanage.ome_devices:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_action: refresh_inventory
    device_service_tags:
      - SVCTAG1

- name: Clear iDRAC job queue
  dellemc.openmanage.ome_devices:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_action: clear_idrac_job_queue
    device_service_tags:
      - SVCTAG1

- name: Reset iDRAC using the service tag
  dellemc.openmanage.ome_devices:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_action: reset_idrac
    device_service_tags:
      - SVCTAG1

- name: Remove devices using servicetags
  dellemc.openmanage.ome_devices:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: absent
    device_service_tags:
      - SVCTAG1
      - SVCTAF2

- name: Remove devices using IDs
  dellemc.openmanage.ome_devices:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: absent
    device_ids:
      - 10235
```

## [Return Values](ome_devices_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to complete the operation because the requested URI is invalid.", "MessageArgs": [], "MessageId": "CGEN1002", "RelatedProperties": [], "Resolution": "Enter a valid URI and retry the operation.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **job**  dictionary | Job details of the devices operation.  **Returned:** success  **Sample:** `{"Builtin": false, "CreatedBy": "admin", "Editable": true, "ExecutionHistories@odata.navigationLink": "/api/JobService/Jobs(14874)/ExecutionHistories", "Id": 14874, "JobDescription": "The Refresh inventory task initiated from OpenManage Ansible Modules for devices with the ids '13216'.", "JobName": "Refresh inventory", "JobStatus": {"@odata.type": "#JobService.JobStatus", "Id": 2020, "Name": "Scheduled"}, "JobType": {"@odata.type": "#JobService.JobType", "Id": 8, "Internal": false, "Name": "Inventory_Task"}, "LastExecutionDetail": {"@odata.id": "/api/JobService/Jobs(14874)/LastExecutionDetail"}, "LastRunStatus": {"@odata.type": "#JobService.JobStatus", "Id": 2060, "Name": "Completed"}, "Params": [{"JobId": 14874, "Key": "action", "Value": "CONFIG_INVENTORY"}, {"JobId": 14874, "Key": "isCollectDriverInventory", "Value": "true"}], "Schedule": "startnow", "State": "Enabled", "Targets": [{"Data": "", "Id": 13216, "JobId": 14874, "TargetType": {"Id": 1000, "Name": "DEVICE"}}], "UpdatedBy": null, "UserGenerated": true, "Visible": true}` |
| **msg**  string | Overall status of the devices operation.  **Returned:** always  **Sample:** `"Successfully removed the device(s)."` |

### Authors

- Jagadeesh N V(@jagadeeshnv)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
