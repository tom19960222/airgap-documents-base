---
collection: ansible
version: "6"
title: "dellemc.openmanage.ome_job_info module – Get job details for a given job ID or an entire job queue on OpenMange Enterprise"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/ome_job_info_module.html
fetched_at: 2026-07-27T17:25:44+00:00
---
# dellemc.openmanage.ome_job_info module – Get job details for a given job ID or an entire job queue on OpenMange Enterprise

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
> see [Requirements](ome_job_info_module.md#ansible-collections-dellemc-openmanage-ome-job-info-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_job_info`.

New in dellemc.openmanage 2.0.0

- [Synopsis](ome_job_info_module.md#synopsis)
- [Requirements](ome_job_info_module.md#requirements)
- [Parameters](ome_job_info_module.md#parameters)
- [Notes](ome_job_info_module.md#notes)
- [Examples](ome_job_info_module.md#examples)
- [Return Values](ome_job_info_module.md#return-values)

## [Synopsis](ome_job_info_module.md#id1)

- This module retrieves job details for a given job ID or an entire job queue on OpenMange Enterprise.

## [Requirements](ome_job_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_job_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname. |
| **job_id**  integer | Unique ID of the job. |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  Default: `443` |
| **system_query_options**  dictionary | Options for pagination of the output. |
| **filter**  string | Filter records by the values supported. |
| **skip**  integer | Number of records to skip. Default value is 0. |
| **top**  integer | Number of records to return. Default value is 100. |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](ome_job_info_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to DellEMC OpenManage Enterprise.
> - This module supports `check_mode`.

## [Examples](ome_job_info_module.md#id5)

```yaml+jinja
---
- name: Get all jobs details
  dellemc.openmanage.ome_job_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"

- name: Get job details for id
  dellemc.openmanage.ome_job_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    job_id: 12345

- name: Get filtered job details
  dellemc.openmanage.ome_job_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    system_query_options:
      top: 2
      skip: 1
      filter: "JobType/Id eq 8"
```

## [Return Values](ome_job_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **job_info**  dictionary | Details of the OpenManage Enterprise jobs.  Returned: success  Sample: `{"value": [{"Builtin": false, "CreatedBy": "system", "Editable": true, "EndTime": null, "Id": 12345, "JobDescription": "Refresh Inventory for Device", "JobName": "Refresh Inventory for Device", "JobStatus": {"Id": 2080, "Name": "New"}, "JobType": {"Id": 8, "Internal": false, "Name": "Inventory_Task"}, "LastRun": "2000-01-29 10:51:34.776", "LastRunStatus": {"Id": 2060, "Name": "Completed"}, "NextRun": null, "Params": [], "Schedule": "", "StartTime": null, "State": "Enabled", "Targets": [{"Data": "''", "Id": 123123, "JobId": 12345, "TargetType": {"Id": 1000, "Name": "DEVICE"}}], "UpdatedBy": null, "Visible": true}]}` |
| **msg**  string | Overall status of the job facts operation.  Returned: always  Sample: `"Successfully fetched the job info"` |

### Authors

- Jagadeesh N V(@jagadeeshnv)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
