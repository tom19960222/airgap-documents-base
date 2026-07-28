---
collection: ansible
version: "8"
title: "google.cloud.gcp_compute_autoscaler_info module – Gather info for GCP Autoscaler"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_compute_autoscaler_info_module.html
fetched_at: 2026-07-28T02:31:54+00:00
---
# google.cloud.gcp_compute_autoscaler_info module – Gather info for GCP Autoscaler

> **Note:**
>
> This module is part of the [google.cloud collection](https://galaxy.ansible.com/ui/repo/published/google/cloud/) (version 1.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install google.cloud`.
> You need further requirements to be able to use this module,
> see [Requirements](gcp_compute_autoscaler_info_module.md#ansible-collections-google-cloud-gcp-compute-autoscaler-info-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_autoscaler_info`.

- [Synopsis](gcp_compute_autoscaler_info_module.md#synopsis)
- [Requirements](gcp_compute_autoscaler_info_module.md#requirements)
- [Parameters](gcp_compute_autoscaler_info_module.md#parameters)
- [Notes](gcp_compute_autoscaler_info_module.md#notes)
- [Examples](gcp_compute_autoscaler_info_module.md#examples)
- [Return Values](gcp_compute_autoscaler_info_module.md#return-values)

## [Synopsis](gcp_compute_autoscaler_info_module.md#id1)

- Gather info for GCP Autoscaler

## [Requirements](gcp_compute_autoscaler_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_autoscaler_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **filters**  list / elements=string | A list of filter value pairs. Available filters are listed here <https://cloud.google.com/sdk/gcloud/reference/topic/filters>.  Each additional filter in the list will act be added as an AND condition (filter1 and filter2) . |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **zone**  string / required | URL of the zone where the instance group resides. |

## [Notes](gcp_compute_autoscaler_info_module.md#id4)

> **Note:**
>
> - for authentication, you can set service_account_file using the `GCP_SERVICE_ACCOUNT_FILE` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set access_token using the `GCP_ACCESS_TOKEN` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_compute_autoscaler_info_module.md#id5)

```yaml+jinja
- name: get info on an autoscaler
  gcp_compute_autoscaler_info:
    zone: us-central1-a
    filters:
    - name = test_object
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
```

## [Return Values](gcp_compute_autoscaler_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resources**  complex | List of resources  **Returned:** always |
| **autoscalingPolicy**  complex | The configuration parameters for the autoscaling algorithm. You can define one or more of the policies for an autoscaler: cpuUtilization, customMetricUtilizations, and loadBalancingUtilization.  If none of these are specified, the default will be to autoscale based on cpuUtilization to 0.6 or 60%.  **Returned:** success |
| **coolDownPeriodSec**  integer | The number of seconds that the autoscaler should wait before it starts collecting information from a new instance. This prevents the autoscaler from collecting information when the instance is initializing, during which the collected usage would not be reliable. The default time autoscaler waits is 60 seconds.  Virtual machine initialization times might vary because of numerous factors. We recommend that you test how long an instance may take to initialize. To do this, create an instance and time the startup process.  **Returned:** success |
| **cpuUtilization**  complex | Defines the CPU utilization policy that allows the autoscaler to scale based on the average CPU utilization of a managed instance group.  **Returned:** success |
| **predictiveMethod**  string | Indicates whether predictive autoscaling based on CPU metric is enabled. Valid values are: - NONE (default). No predictive method is used. The autoscaler scales the group to meet current demand based on real-time metrics.   - OPTIMIZE_AVAILABILITY. Predictive autoscaling improves availability by monitoring daily and weekly load patterns and scaling out ahead of anticipated demand.   **Returned:** success |
| **utilizationTarget**  string | The target CPU utilization that the autoscaler should maintain.  Must be a float value in the range (0, 1]. If not specified, the default is 0.6.  If the CPU level is below the target utilization, the autoscaler scales down the number of instances until it reaches the minimum number of instances you specified or until the average CPU of your instances reaches the target utilization.  If the average CPU is above the target utilization, the autoscaler scales up until it reaches the maximum number of instances you specified or until the average utilization reaches the target utilization.  **Returned:** success |
| **customMetricUtilizations**  complex | Configuration parameters of autoscaling based on a custom metric.  **Returned:** success |
| **metric**  string | The identifier (type) of the Stackdriver Monitoring metric.  The metric cannot have negative values.  The metric must have a value type of INT64 or DOUBLE.  **Returned:** success |
| **utilizationTarget**  string | The target value of the metric that autoscaler should maintain. This must be a positive value. A utilization metric scales number of virtual machines handling requests to increase or decrease proportionally to the metric.  For example, a good metric to use as a utilizationTarget is www.googleapis.com/compute/instance/network/received_bytes_count.  The autoscaler will work to keep this value constant for each of the instances.  **Returned:** success |
| **utilizationTargetType**  string | Defines how target utilization value is expressed for a Stackdriver Monitoring metric.  **Returned:** success |
| **loadBalancingUtilization**  complex | Configuration parameters of autoscaling based on a load balancer.  **Returned:** success |
| **utilizationTarget**  string | Fraction of backend capacity utilization (set in HTTP(s) load balancing configuration) that autoscaler should maintain. Must be a positive float value. If not defined, the default is 0.8.  **Returned:** success |
| **maxNumReplicas**  integer | The maximum number of instances that the autoscaler can scale up to. This is required when creating or updating an autoscaler. The maximum number of replicas should not be lower than minimal number of replicas.  **Returned:** success |
| **minNumReplicas**  integer | The minimum number of replicas that the autoscaler can scale down to. This cannot be less than 0. If not provided, autoscaler will choose a default value depending on maximum number of instances allowed.  **Returned:** success |
| **mode**  string | Defines operating mode for this policy.  **Returned:** success |
| **scaleInControl**  complex | Defines scale in controls to reduce the risk of response latency and outages due to abrupt scale-in events .  **Returned:** success |
| **maxScaledInReplicas**  complex | A nested object resource.  **Returned:** success |
| **fixed**  integer | Specifies a fixed number of VM instances. This must be a positive integer.  **Returned:** success |
| **percent**  integer | Specifies a percentage of instances between 0 to 100%, inclusive.  For example, specify 80 for 80%.  **Returned:** success |
| **timeWindowSec**  integer | How long back autoscaling should look when computing recommendations to include directives regarding slower scale down, as described above.  **Returned:** success |
| **creationTimestamp**  string | Creation timestamp in RFC3339 text format.  **Returned:** success |
| **description**  string | An optional description of this resource.  **Returned:** success |
| **id**  integer | Unique identifier for the resource.  **Returned:** success |
| **name**  string | Name of the resource. The name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  **Returned:** success |
| **target**  dictionary | URL of the managed instance group that this autoscaler will scale.  **Returned:** success |
| **zone**  string | URL of the zone where the instance group resides.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
