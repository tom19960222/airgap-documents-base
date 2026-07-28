---
collection: ansible
version: "6"
title: "dellemc.openmanage.ome_powerstate module – Performs the power management operations on OpenManage Enterprise"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/ome_powerstate_module.html
fetched_at: 2026-07-27T17:25:46+00:00
---
# dellemc.openmanage.ome_powerstate module – Performs the power management operations on OpenManage Enterprise

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
> see [Requirements](ome_powerstate_module.md#ansible-collections-dellemc-openmanage-ome-powerstate-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_powerstate`.

New in dellemc.openmanage 2.1.0

- [Synopsis](ome_powerstate_module.md#synopsis)
- [Requirements](ome_powerstate_module.md#requirements)
- [Parameters](ome_powerstate_module.md#parameters)
- [Notes](ome_powerstate_module.md#notes)
- [Examples](ome_powerstate_module.md#examples)
- [Return Values](ome_powerstate_module.md#return-values)

## [Synopsis](ome_powerstate_module.md#id1)

- This module performs the supported power management operations on OpenManage Enterprise.

## [Requirements](ome_powerstate_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_powerstate_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **device_id**  integer | Targeted device id.  *device_id* is mutually exclusive with *device_service_tag*. |
| **device_service_tag**  string | Targeted device service tag.  *device_service_tag* is mutually exclusive with *device_id*. |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname. |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  Default: `443` |
| **power_state**  string / required | Desired end power state.  Choices:   - `"on"` - `"off"` - `"coldboot"` - `"warmboot"` - `"shutdown"` |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](ome_powerstate_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to DellEMC OpenManage Enterprise.
> - This module supports `check_mode`.

## [Examples](ome_powerstate_module.md#id5)

```yaml+jinja
---
- name: Power state operation based on device id
  dellemc.openmanage.ome_powerstate:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_id: 11111
    power_state: "off"

- name: Power state operation based on device service tag
  dellemc.openmanage.ome_powerstate:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_service_tag: "KLBR111"
    power_state: "on"

- name: Power state operation based on list of device ids
  dellemc.openmanage.ome_powerstate:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_id: "{{ item.device_id }}"
    power_state: "{{ item.state }}"
  with_items:
    - { "device_id": 11111, "state": "on" }
    - { "device_id": 22222, "state": "off" }

- name: Power state operation based on list of device service tags
  dellemc.openmanage.ome_powerstate:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_service_tag: "{{ item.service_tag }}"
    power_state: "{{ item.state }}"
  with_items:
    - { "service_tag": "KLBR111", "state": "on" }
    - { "service_tag": "KLBR222", "state": "off" }
```

## [Return Values](ome_powerstate_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **job_status**  dictionary | Power state operation job and progress details from the OME.  Returned: success  Sample: `{"Builtin": false, "CreatedBy": "user", "Editable": true, "EndTime": null, "Id": 11111, "JobDescription": "DeviceAction_Task", "JobName": "DeviceAction_Task_PowerState", "JobStatus": {"Id": 1111, "Name": "New"}, "JobType": {"Id": 1, "Internal": false, "Name": "DeviceAction_Task"}, "LastRun": "2019-04-01 06:39:02.69", "LastRunStatus": {"Id": 1112, "Name": "Running"}, "NextRun": null, "Params": [{"JobId": 11111, "Key": "powerState", "Value": "2"}, {"JobId": 11111, "Key": "operationName", "Value": "POWER_CONTROL"}], "Schedule": "", "StartTime": null, "State": "Enabled", "Targets": [{"Data": "", "Id": 11112, "JobId": 11111, "TargetType": {"Id": 1000, "Name": "DEVICE"}}], "UpdatedBy": null, "Visible": true}` |
| **msg**  string | Overall power state operation job status.  Returned: always  Sample: `"Power State operation job submitted successfully."` |

### Authors

- Felix Stephen (@felixs88)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
