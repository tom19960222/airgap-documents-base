---
collection: ansible
version: "8"
title: "community.general.ocapi_info module – Manages Out-Of-Band controllers using Open Composable API (OCAPI)"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/ocapi_info_module.html
fetched_at: 2026-07-28T01:48:14+00:00
---
# community.general.ocapi_info module – Manages Out-Of-Band controllers using Open Composable API (OCAPI)

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.ocapi_info`.

New in community.general 6.3.0

- [Synopsis](ocapi_info_module.md#synopsis)
- [Parameters](ocapi_info_module.md#parameters)
- [Attributes](ocapi_info_module.md#attributes)
- [Examples](ocapi_info_module.md#examples)
- [Return Values](ocapi_info_module.md#return-values)

## [Synopsis](ocapi_info_module.md#id1)

- Builds OCAPI URIs locally and sends them to remote OOB controllers to get information back.

## [Parameters](ocapi_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **baseuri**  string / required | Base URI of OOB controller. |
| **category**  string / required | Category to execute on OOB controller. |
| **command**  string / required | Command to execute on OOB controller. |
| **job_name**  string | Name of job for fetching status. |
| **password**  string / required | Password for authenticating to OOB controller. |
| **proxy_slot_number**  integer | For proxied inband requests, the slot number of the IOM. Only applies if `baseuri` is a proxy server. |
| **timeout**  integer | Timeout in seconds for URL requests to OOB controller.  **Default:** `10` |
| **username**  string / required | Username for authenticating to OOB controller. |

## [Attributes](ocapi_info_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](ocapi_info_module.md#id4)

```yaml+jinja
- name: Get job status
  community.general.ocapi_info:
    category: Status
    command: JobStatus
    baseuri: "http://iom1.wdc.com"
    jobName: FirmwareUpdate
    username: "{{ username }}"
    password: "{{ password }}"
```

## [Return Values](ocapi_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **details**  list / elements=string | Details of the relevant operation. Applies to `command=JobStatus`.  **Returned:** when supported |
| **msg**  string | Message with action result or error description.  **Returned:** always  **Sample:** `"Action was successful"` |
| **operationHealth**  string | Health of the operation. Applies to `command=JobStatus`. See OCAPI documentation for details.  **Returned:** when supported  **Sample:** `"OK"` |
| **operationHealthId**  string | Integer value for health of the operation (corresponds to `operationHealth`). Applies to `command=JobStatus`. See OCAPI documentation for details.  **Returned:** when supported  **Sample:** `"OK"` |
| **operationStatus**  string | Status of the relevant operation. Applies to `command=JobStatus`. See OCAPI documentation for details.  **Returned:** when supported  **Sample:** `"Activate needed"` |
| **operationStatusId**  integer | Integer value of status (corresponds to operationStatus). Applies to `command=JobStatus`. See OCAPI documentation for details.  **Returned:** when supported  **Sample:** `65540` |
| **percentComplete**  integer | Percent complete of the relevant operation. Applies to `command=JobStatus`.  **Returned:** when supported  **Sample:** `99` |
| **status**  dictionary | Dictionary containing status information. See OCAPI documentation for details.  **Returned:** when supported  **Sample:** `{"Details": ["None"], "Health": [{"ID": 5, "Name": "OK"}], "State": {"ID": 16, "Name": "In service"}}` |

### Authors

- Mike Moerk (@mikemoerk)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
