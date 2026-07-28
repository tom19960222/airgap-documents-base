---
collection: ansible
version: "8"
title: "dellemc.openmanage.ome_configuration_compliance_baseline module – Create, modify, and delete a configuration compliance baseline and remediate non-compliant devices on OpenManage Enterprise"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/ome_configuration_compliance_baseline_module.html
fetched_at: 2026-07-28T02:04:25+00:00
---
# dellemc.openmanage.ome_configuration_compliance_baseline module – Create, modify, and delete a configuration compliance baseline and remediate non-compliant devices on OpenManage Enterprise

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
> see [Requirements](ome_configuration_compliance_baseline_module.md#ansible-collections-dellemc-openmanage-ome-configuration-compliance-baseline-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_configuration_compliance_baseline`.

New in dellemc.openmanage 3.2.0

- [Synopsis](ome_configuration_compliance_baseline_module.md#synopsis)
- [Requirements](ome_configuration_compliance_baseline_module.md#requirements)
- [Parameters](ome_configuration_compliance_baseline_module.md#parameters)
- [Notes](ome_configuration_compliance_baseline_module.md#notes)
- [Examples](ome_configuration_compliance_baseline_module.md#examples)
- [Return Values](ome_configuration_compliance_baseline_module.md#return-values)

## [Synopsis](ome_configuration_compliance_baseline_module.md#id1)

- This module allows to create, modify, and delete a configuration compliance baseline on OpenManage Enterprise. This module also allows to remediate devices that are non-compliant with the baseline by changing the attributes of devices to match with the associated baseline attributes.

## [Requirements](ome_configuration_compliance_baseline_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_configuration_compliance_baseline_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **command**  string | `create` creates a configuration baseline from an existing compliance template.`create` supports `check_mode` or idempotency checking for only *names*.  `modify` modifies an existing baseline.Only *names*, *description*, *device_ids*, *device_service_tags*, and *device_group_names* can be modified  *WARNING* When a baseline is modified, the provided *device_ids*, *device_group_names*, and *device_service_tags* replaces the devices previously present in the baseline.  `delete` deletes the list of configuration compliance baselines based on the baseline name. Invalid baseline names are ignored.  `remediate` remediates devices that are non-compliant with the baseline by changing the attributes of devices to match with the associated baseline attributes.  `remediate` is performed on all the non-compliant devices if either *device_ids*, or *device_service_tags* is not provided.  **Choices:**   - `"create"` ← (default) - `"modify"` - `"delete"` - `"remediate"` |
| **description**  string | Description of the compliance baseline.  This option is applicable when *command* is `create`, or `modify`. |
| **device_group_names**  list / elements=string | Name of the target device group.  This option is applicable when *command* is `create`, or `modify` and is mutually exclusive with *device_ids* and *device_service_tag*. |
| **device_ids**  list / elements=integer | IDs of the target devices.  This option is applicable when *command* is `create`, `modify`, or `remediate`, and is mutually exclusive with *device_service_tag* and *device_group_names*. |
| **device_service_tags**  list / elements=string | Service tag of the target device.  This option is applicable when *command* is `create`, `modify`, or `remediate` and is mutually exclusive with *device_ids* and *device_group_names*. |
| **hostname**  string / required | OpenManage Enterprise IP address or hostname. |
| **job_wait**  boolean | Provides the option to wait for job completion.  This option is applicable when *command* is `create`, `modify`, or `remediate`.  **Choices:**   - `false` - `true` ← (default) |
| **job_wait_timeout**  integer | The maximum wait time of *job_wait* in seconds.The job will only be tracked for this duration.  This option is applicable when *job_wait* is `True`.  **Default:** `10800` |
| **names**  list / elements=string / required | Name(s) of the configuration compliance baseline.  This option is applicable when *command* is `create`, `modify`, or `delete`.  Provide the list of configuration compliance baselines names that are supported when *command* is `delete`. |
| **new_name**  string | New name of the compliance baseline to be modified.  This option is applicable when *command* is `modify`. |
| **password**  string / required | OpenManage Enterprise password. |
| **port**  integer | OpenManage Enterprise HTTPS port.  **Default:** `443` |
| **template_id**  integer | ID of the deployment template to be used for creating a compliance baseline.  This option is applicable when *command* is `create` and is mutually exclusive with *template_name*. |
| **template_name**  string | Name of the compliance template for creating the compliance baseline(s).  Name of the deployment template to be used for creating a compliance baseline.  This option is applicable when *command* is `create` and is mutually exclusive with *template_id*. |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **username**  string / required | OpenManage Enterprise username. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ome_configuration_compliance_baseline_module.md#id4)

> **Note:**
>
> - This module supports `check_mode`.
> - Ensure that the devices have the required licenses to perform the baseline compliance operations.

## [Examples](ome_configuration_compliance_baseline_module.md#id5)

```yaml+jinja
---
- name: Create a configuration compliance baseline using device IDs
  dellemc.openmanage.ome_configuration_compliance_baseline:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    names: "baseline1"
    template_name: "template1"
    description: "description of baseline"
    device_ids:
      - 1111
      - 2222

- name: Create a configuration compliance baseline using device service tags
  dellemc.openmanage.ome_configuration_compliance_baseline:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    names: "baseline1"
    template_id: 1234
    description: "description of baseline"
    device_service_tags:
      - "SVCTAG1"
      - "SVCTAG2"

- name: Create a configuration compliance baseline using group names
  dellemc.openmanage.ome_configuration_compliance_baseline:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    names: "baseline2"
    template_id: 2
    job_wait_timeout: 1000
    description: "description of baseline"
    device_group_names:
      - "Group1"
      - "Group2"

- name: Delete the configuration compliance baselines
  dellemc.openmanage.ome_configuration_compliance_baseline:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: delete
    names:
      - baseline1
      - baseline2

- name: Modify a configuration compliance baseline using group names
  dellemc.openmanage.ome_configuration_compliance_baseline:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: modify
    names: "baseline1"
    new_name: "baseline_update"
    template_name: "template2"
    description: "new description of baseline"
    job_wait_timeout: 1000
    device_group_names:
      - Group1

- name: Remediate specific non-compliant devices to a configuration compliance baseline using device IDs
  dellemc.openmanage.ome_configuration_compliance_baseline:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: "remediate"
    names: "baseline1"
    device_ids:
      - 1111

- name: Remediate specific non-compliant devices to a configuration compliance baseline using device service tags
  dellemc.openmanage.ome_configuration_compliance_baseline:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: "remediate"
    names: "baseline1"
    device_service_tags:
      - "SVCTAG1"
      - "SVCTAG2"

- name: Remediate all the non-compliant devices to a configuration compliance baseline
  dellemc.openmanage.ome_configuration_compliance_baseline:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: "remediate"
    names: "baseline1"
```

## [Return Values](ome_configuration_compliance_baseline_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **compliance_status**  dictionary | Status of compliance baseline operation.  **Returned:** when *command* is `create` or `modify`  **Sample:** `{"BaselineTargets": [{"Id": 1111, "Type": {"Id": 1000, "Name": "DEVICE"}}], "ConfigComplianceSummary": {"ComplianceStatus": "OK", "NumberOfCritical": 0, "NumberOfIncomplete": 0, "NumberOfNormal": 0, "NumberOfWarning": 0}, "Description": null, "Id": 13, "LastRun": "2021-02-27 13:15:13.751", "Name": "baseline1", "PercentageComplete": "100", "TaskId": 26584, "TaskStatus": 2070, "TemplateId": 102, "TemplateName": "one", "TemplateType": 2}` |
| **error_info**  dictionary | Details of the HTTP Error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **incompatible_devices**  list / elements=string | Details of the devices which cannot be used to perform baseline compliance operations  **Returned:** when *device_service_tags* or *device_ids* contains incompatible devices for `create` or `modify`  **Sample:** `[1234, 5678]` |
| **job_id**  integer | Task ID created when *command* is `remediate`.  **Returned:** when *command* is `remediate`  **Sample:** `14123` |
| **msg**  string | Overall status of the configuration compliance baseline operation.  **Returned:** always  **Sample:** `"Successfully created the configuration compliance baseline."` |

### Authors

- Sajna Shetty(@Sajna-Shetty)
- Abhishek Sinha(@Abhishek-Dell)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
