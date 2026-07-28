---
collection: ansible
version: "6"
title: "google.cloud.gcp_compute_region_instance_group_manager_info module – Gather info for GCP RegionInstanceGroupManager"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_compute_region_instance_group_manager_info_module.html
fetched_at: 2026-07-27T17:48:25+00:00
---
# google.cloud.gcp_compute_region_instance_group_manager_info module – Gather info for GCP RegionInstanceGroupManager

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
> see [Requirements](gcp_compute_region_instance_group_manager_info_module.md#ansible-collections-google-cloud-gcp-compute-region-instance-group-manager-info-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_region_instance_group_manager_info`.

- [Synopsis](gcp_compute_region_instance_group_manager_info_module.md#synopsis)
- [Requirements](gcp_compute_region_instance_group_manager_info_module.md#requirements)
- [Parameters](gcp_compute_region_instance_group_manager_info_module.md#parameters)
- [Notes](gcp_compute_region_instance_group_manager_info_module.md#notes)
- [Examples](gcp_compute_region_instance_group_manager_info_module.md#examples)
- [Return Values](gcp_compute_region_instance_group_manager_info_module.md#return-values)

## [Synopsis](gcp_compute_region_instance_group_manager_info_module.md#id1)

- Gather info for GCP RegionInstanceGroupManager

## [Requirements](gcp_compute_region_instance_group_manager_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_region_instance_group_manager_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **filters**  list / elements=string | A list of filter value pairs. Available filters are listed here <https://cloud.google.com/sdk/gcloud/reference/topic/filters>.  Each additional filter in the list will act be added as an AND condition (filter1 and filter2) . |
| **project**  string | The Google Cloud Platform project to use. |
| **region**  string / required | The region the managed instance group resides. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |

## [Notes](gcp_compute_region_instance_group_manager_info_module.md#id4)

> **Note:**
>
> - for authentication, you can set service_account_file using the `gcp_service_account_file` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_compute_region_instance_group_manager_info_module.md#id5)

```yaml+jinja
- name: get info on a region instance group manager
  gcp_compute_region_instance_group_manager_info:
    region: us-central1
    filters:
    - name = test_object
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
```

## [Return Values](gcp_compute_region_instance_group_manager_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resources**  complex | List of resources  Returned: always |
| **autoHealingPolicies**  complex | The autohealing policy for this managed instance group .  Returned: success |
| **healthCheck**  string | The URL for the health check that signals autohealing.  Returned: success |
| **initialDelaySec**  integer | The number of seconds that the managed instance group waits before it applies autohealing policies to new instances or recently recreated instances .  Returned: success |
| **baseInstanceName**  string | The base instance name to use for instances in this group. The value must be 1-58 characters long. Instances are named by appending a hyphen and a random four-character string to the base instance name.  The base instance name must comply with RFC1035.  Returned: success |
| **creationTimestamp**  string | The creation timestamp for this managed instance group in RFC3339 text format.  Returned: success |
| **currentActions**  complex | The list of instance actions and the number of instances in this managed instance group that are scheduled for each of those actions.  Returned: success |
| **abandoning**  integer | The total number of instances in the managed instance group that are scheduled to be abandoned. Abandoning an instance removes it from the managed instance group without deleting it.  Returned: success |
| **creating**  integer | The number of instances in the managed instance group that are scheduled to be created or are currently being created. If the group fails to create any of these instances, it tries again until it creates the instance successfully.  If you have disabled creation retries, this field will not be populated; instead, the creatingWithoutRetries field will be populated.  Returned: success |
| **creatingWithoutRetries**  integer | The number of instances that the managed instance group will attempt to create. The group attempts to create each instance only once. If the group fails to create any of these instances, it decreases the group’s targetSize value accordingly.  Returned: success |
| **deleting**  integer | The number of instances in the managed instance group that are scheduled to be deleted or are currently being deleted.  Returned: success |
| **none**  integer | The number of instances in the managed instance group that are running and have no scheduled actions.  Returned: success |
| **recreating**  integer | The number of instances in the managed instance group that are scheduled to be recreated or are currently being being recreated.  Recreating an instance deletes the existing root persistent disk and creates a new disk from the image that is defined in the instance template.  Returned: success |
| **refreshing**  integer | The number of instances in the managed instance group that are being reconfigured with properties that do not require a restart or a recreate action. For example, setting or removing target pools for the instance.  Returned: success |
| **restarting**  integer | The number of instances in the managed instance group that are scheduled to be restarted or are currently being restarted.  Returned: success |
| **description**  string | An optional description of this resource. Provide this property when you create the resource.  Returned: success |
| **id**  integer | A unique identifier for this resource.  Returned: success |
| **instanceGroup**  dictionary | The instance group being managed.  Returned: success |
| **instanceTemplate**  dictionary | The instance template that is specified for this managed instance group. The group uses this template to create all new instances in the managed instance group.  Returned: success |
| **name**  string | The name of the managed instance group. The name must be 1-63 characters long, and comply with RFC1035.  Returned: success |
| **namedPorts**  complex | Named ports configured for the Instance Groups complementary to this Instance Group Manager.  Returned: success |
| **name**  string | The name for this named port. The name must be 1-63 characters long, and comply with RFC1035.  Returned: success |
| **port**  integer | The port number, which can be a value between 1 and 65535.  Returned: success |
| **region**  string | The region the managed instance group resides.  Returned: success |
| **targetPools**  list / elements=string | TargetPool resources to which instances in the instanceGroup field are added. The target pools automatically apply to all of the instances in the managed instance group.  Returned: success |
| **targetSize**  integer | The target number of running instances for this managed instance group. Deleting or abandoning instances reduces this number. Resizing the group changes this number.  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
