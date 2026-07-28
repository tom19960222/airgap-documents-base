---
collection: ansible
version: "6"
title: "google.cloud.gcp_compute_target_pool_info module – Gather info for GCP TargetPool"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_compute_target_pool_info_module.html
fetched_at: 2026-07-27T17:48:47+00:00
---
# google.cloud.gcp_compute_target_pool_info module – Gather info for GCP TargetPool

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
> see [Requirements](gcp_compute_target_pool_info_module.md#ansible-collections-google-cloud-gcp-compute-target-pool-info-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_target_pool_info`.

- [Synopsis](gcp_compute_target_pool_info_module.md#synopsis)
- [Requirements](gcp_compute_target_pool_info_module.md#requirements)
- [Parameters](gcp_compute_target_pool_info_module.md#parameters)
- [Notes](gcp_compute_target_pool_info_module.md#notes)
- [Examples](gcp_compute_target_pool_info_module.md#examples)
- [Return Values](gcp_compute_target_pool_info_module.md#return-values)

## [Synopsis](gcp_compute_target_pool_info_module.md#id1)

- Gather info for GCP TargetPool

## [Requirements](gcp_compute_target_pool_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_target_pool_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **filters**  list / elements=string | A list of filter value pairs. Available filters are listed here <https://cloud.google.com/sdk/gcloud/reference/topic/filters>.  Each additional filter in the list will act be added as an AND condition (filter1 and filter2) . |
| **project**  string | The Google Cloud Platform project to use. |
| **region**  string / required | The region where the target pool resides. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |

## [Notes](gcp_compute_target_pool_info_module.md#id4)

> **Note:**
>
> - for authentication, you can set service_account_file using the `gcp_service_account_file` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_compute_target_pool_info_module.md#id5)

```yaml+jinja
- name: get info on a target pool
  gcp_compute_target_pool_info:
    region: us-west1
    filters:
    - name = test_object
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
```

## [Return Values](gcp_compute_target_pool_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resources**  complex | List of resources  Returned: always |
| **backupPool**  dictionary | This field is applicable only when the containing target pool is serving a forwarding rule as the primary pool, and its failoverRatio field is properly set to a value between [0, 1].  backupPool and failoverRatio together define the fallback behavior of the primary target pool: if the ratio of the healthy instances in the primary pool is at or below failoverRatio, traffic arriving at the load-balanced IP will be directed to the backup pool.  In case where failoverRatio and backupPool are not set, or all the instances in the backup pool are unhealthy, the traffic will be directed back to the primary pool in the “force” mode, where traffic will be spread to the healthy instances with the best effort, or to all instances when no instance is healthy.  Returned: success |
| **creationTimestamp**  string | Creation timestamp in RFC3339 text format.  Returned: success |
| **description**  string | An optional description of this resource.  Returned: success |
| **failoverRatio**  string | This field is applicable only when the containing target pool is serving a forwarding rule as the primary pool (i.e., not as a backup pool to some other target pool). The value of the field must be in [0, 1].  If set, backupPool must also be set. They together define the fallback behavior of the primary target pool: if the ratio of the healthy instances in the primary pool is at or below this number, traffic arriving at the load-balanced IP will be directed to the backup pool.  In case where failoverRatio is not set or all the instances in the backup pool are unhealthy, the traffic will be directed back to the primary pool in the “force” mode, where traffic will be spread to the healthy instances with the best effort, or to all instances when no instance is healthy.  Returned: success |
| **healthCheck**  dictionary | A reference to a HttpHealthCheck resource.  A member instance in this pool is considered healthy if and only if the health checks pass. If not specified it means all member instances will be considered healthy at all times.  Returned: success |
| **id**  integer | The unique identifier for the resource.  Returned: success |
| **instances**  list / elements=string | A list of virtual machine instances serving this pool.  They must live in zones contained in the same region as this pool.  Returned: success |
| **name**  string | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  Returned: success |
| **region**  string | The region where the target pool resides.  Returned: success |
| **sessionAffinity**  string | Session affinity option. Must be one of these values: \* NONE: Connections from the same client IP may go to any instance in the pool.  \* CLIENT_IP: Connections from the same client IP will go to the same instance in the pool while that instance remains healthy.  \* CLIENT_IP_PROTO: Connections from the same client IP with the same IP protocol will go to the same instance in the pool while that instance remains healthy.  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
