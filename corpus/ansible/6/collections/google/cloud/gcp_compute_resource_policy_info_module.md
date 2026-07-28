---
collection: ansible
version: "6"
title: "google.cloud.gcp_compute_resource_policy_info module – Gather info for GCP ResourcePolicy"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_compute_resource_policy_info_module.html
fetched_at: 2026-07-27T17:48:32+00:00
---
# google.cloud.gcp_compute_resource_policy_info module – Gather info for GCP ResourcePolicy

> **Note:**
>
> This module is part of the [google.cloud collection](https://galaxy.ansible.com/google/cloud) (version 1.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install google.cloud`.
> You need further requirements to be able to use this module,
> see [Requirements](gcp_compute_resource_policy_info_module.md#ansible-collections-google-cloud-gcp-compute-resource-policy-info-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_resource_policy_info`.

- [Synopsis](gcp_compute_resource_policy_info_module.md#synopsis)
- [Requirements](gcp_compute_resource_policy_info_module.md#requirements)
- [Parameters](gcp_compute_resource_policy_info_module.md#parameters)
- [Notes](gcp_compute_resource_policy_info_module.md#notes)
- [Examples](gcp_compute_resource_policy_info_module.md#examples)
- [Return Values](gcp_compute_resource_policy_info_module.md#return-values)

## [Synopsis](gcp_compute_resource_policy_info_module.md#id1)

- Gather info for GCP ResourcePolicy

## [Requirements](gcp_compute_resource_policy_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_resource_policy_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **filters**  list / elements=string | A list of filter value pairs. Available filters are listed here <https://cloud.google.com/sdk/gcloud/reference/topic/filters>.  Each additional filter in the list will act be added as an AND condition (filter1 and filter2) . |
| **project**  string | The Google Cloud Platform project to use. |
| **region**  string / required | Region where resource policy resides. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |

## [Notes](gcp_compute_resource_policy_info_module.md#id4)

> **Note:**
>
> - for authentication, you can set service_account_file using the `gcp_service_account_file` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_compute_resource_policy_info_module.md#id5)

```yaml+jinja
- name: get info on a resource policy
  gcp_compute_resource_policy_info:
    region: us-central1
    filters:
    - name = test_object
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
```

## [Return Values](gcp_compute_resource_policy_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resources**  complex | List of resources  Returned: always |
| **groupPlacementPolicy**  complex | Policy for creating snapshots of persistent disks.  Returned: success |
| **availabilityDomainCount**  integer | The number of availability domains instances will be spread across. If two instances are in different availability domain, they will not be put in the same low latency network .  Returned: success |
| **collocation**  string | Collocation specifies whether to place VMs inside the same availability domain on the same low-latency network.  Specify `COLLOCATED` to enable collocation. Can only be specified with `vm_count`. If compute instances are created with a COLLOCATED policy, then exactly `vm_count` instances must be created at the same time with the resource policy attached.  Returned: success |
| **vmCount**  integer | Number of vms in this placement group.  Returned: success |
| **name**  string | The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])`? which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  Returned: success |
| **region**  string | Region where resource policy resides.  Returned: success |
| **snapshotSchedulePolicy**  complex | Policy for creating snapshots of persistent disks.  Returned: success |
| **retentionPolicy**  complex | Retention policy applied to snapshots created by this resource policy.  Returned: success |
| **maxRetentionDays**  integer | Maximum age of the snapshot that is allowed to be kept.  Returned: success |
| **onSourceDiskDelete**  string | Specifies the behavior to apply to scheduled snapshots when the source disk is deleted.  Returned: success |
| **schedule**  complex | Contains one of an `hourlySchedule`, `dailySchedule`, or `weeklySchedule`.  Returned: success |
| **dailySchedule**  complex | The policy will execute every nth day at the specified time.  Returned: success |
| **daysInCycle**  integer | The number of days between snapshots.  Returned: success |
| **startTime**  string | This must be in UTC format that resolves to one of 00:00, 04:00, 08:00, 12:00, 16:00, or 20:00. For example, both 13:00-5 and 08:00 are valid.  Returned: success |
| **hourlySchedule**  complex | The policy will execute every nth hour starting at the specified time.  Returned: success |
| **hoursInCycle**  integer | The number of hours between snapshots.  Returned: success |
| **startTime**  string | Time within the window to start the operations.  It must be in an hourly format “HH:MM”, where HH : [00-23] and MM : [00] GMT.  eg: 21:00 .  Returned: success |
| **weeklySchedule**  complex | Allows specifying a snapshot time for each day of the week.  Returned: success |
| **dayOfWeeks**  complex | May contain up to seven (one for each day of the week) snapshot times.  Returned: success |
| **day**  string | The day of the week to create the snapshot. e.g. MONDAY .  Returned: success |
| **startTime**  string | Time within the window to start the operations.  It must be in format “HH:MM”, where HH : [00-23] and MM : [00-00] GMT.  Returned: success |
| **snapshotProperties**  complex | Properties with which the snapshots are created, such as labels.  Returned: success |
| **guestFlush**  boolean | Whether to perform a ‘guest aware’ snapshot.  Returned: success |
| **labels**  dictionary | A set of key-value pairs.  Returned: success |
| **storageLocations**  list / elements=string | Cloud Storage bucket location to store the auto snapshot (regional or multi-regional) .  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
