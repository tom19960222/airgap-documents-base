---
collection: ansible
version: "6"
title: "dellemc.openmanage.idrac_lifecycle_controller_job_status_info module – Get the status of a Lifecycle Controller job"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/idrac_lifecycle_controller_job_status_info_module.html
fetched_at: 2026-07-27T17:25:12+00:00
---
# dellemc.openmanage.idrac_lifecycle_controller_job_status_info module – Get the status of a Lifecycle Controller job

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
> see [Requirements](idrac_lifecycle_controller_job_status_info_module.md#ansible-collections-dellemc-openmanage-idrac-lifecycle-controller-job-status-info-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.idrac_lifecycle_controller_job_status_info`.

New in dellemc.openmanage 2.1.0

- [Synopsis](idrac_lifecycle_controller_job_status_info_module.md#synopsis)
- [Requirements](idrac_lifecycle_controller_job_status_info_module.md#requirements)
- [Parameters](idrac_lifecycle_controller_job_status_info_module.md#parameters)
- [Notes](idrac_lifecycle_controller_job_status_info_module.md#notes)
- [Examples](idrac_lifecycle_controller_job_status_info_module.md#examples)
- [Return Values](idrac_lifecycle_controller_job_status_info_module.md#return-values)

## [Synopsis](idrac_lifecycle_controller_job_status_info_module.md#id1)

- This module shows the status of a specific Lifecycle Controller job using its job ID.

## [Requirements](idrac_lifecycle_controller_job_status_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- omsdk >= 1.2.488
- python >= 3.8.6

## [Parameters](idrac_lifecycle_controller_job_status_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **idrac_ip**  string / required | iDRAC IP Address. |
| **idrac_password**  aliases: idrac_pwd  string / required | iDRAC user password. |
| **idrac_port**  integer | iDRAC port.  Default: `443` |
| **idrac_user**  string / required | iDRAC username. |
| **job_id**  string / required | JOB ID in the format “JID_123456789012”. |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](idrac_lifecycle_controller_job_status_info_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to DellEMC iDRAC.
> - This module supports `check_mode`.

## [Examples](idrac_lifecycle_controller_job_status_info_module.md#id5)

```yaml+jinja
---
- name: Show status of a Lifecycle Control job
  dellemc.openmanage.idrac_lifecycle_controller_job_status_info:
       idrac_ip:  "192.168.0.1"
       idrac_user:  "user_name"
       idrac_password:  "user_password"
       ca_path: "/path/to/ca_cert.pem"
       job_id:  "JID_1234567890"
```

## [Return Values](idrac_lifecycle_controller_job_status_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  Returned: on HTTP error  Sample: `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **job_info**  dictionary | Displays the status of a Lifecycle Controller job.  Returned: success  Sample: `{"ElapsedTimeSinceCompletion": "8742", "InstanceID": "JID_844222910040", "JobStartTime": "NA", "JobStatus": "Completed", "JobUntilTime": "NA", "Message": "Job completed successfully.", "MessageArguments": "NA", "MessageID": "RED001", "Name": "update:DCIM:INSTALLED#iDRAC.Embedded.1-1#IDRACinfo", "PercentComplete": "100", "Status": "Success"}` |
| **msg**  string | Overall status of the job facts operation.  Returned: always  Sample: `"Successfully fetched the job info."` |

### Authors

- Rajeev Arakkal (@rajeevarakkal)
- Anooja Vardhineni (@anooja-vardhineni)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
