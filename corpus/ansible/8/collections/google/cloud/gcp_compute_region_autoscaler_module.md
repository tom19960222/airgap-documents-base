---
collection: ansible
version: "8"
title: "google.cloud.gcp_compute_region_autoscaler module – Creates a GCP RegionAutoscaler"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_compute_region_autoscaler_module.html
fetched_at: 2026-07-28T02:32:25+00:00
---
# google.cloud.gcp_compute_region_autoscaler module – Creates a GCP RegionAutoscaler

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
> see [Requirements](gcp_compute_region_autoscaler_module.md#ansible-collections-google-cloud-gcp-compute-region-autoscaler-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_region_autoscaler`.

- [Synopsis](gcp_compute_region_autoscaler_module.md#synopsis)
- [Requirements](gcp_compute_region_autoscaler_module.md#requirements)
- [Parameters](gcp_compute_region_autoscaler_module.md#parameters)
- [Notes](gcp_compute_region_autoscaler_module.md#notes)
- [Examples](gcp_compute_region_autoscaler_module.md#examples)
- [Return Values](gcp_compute_region_autoscaler_module.md#return-values)

## [Synopsis](gcp_compute_region_autoscaler_module.md#id1)

- Represents an Autoscaler resource.
- Autoscalers allow you to automatically scale virtual machine instances in managed instance groups according to an autoscaling policy that you define.

## [Requirements](gcp_compute_region_autoscaler_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_region_autoscaler_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **autoscaling_policy**  dictionary / required | The configuration parameters for the autoscaling algorithm. You can define one or more of the policies for an autoscaler: cpuUtilization, customMetricUtilizations, and loadBalancingUtilization.  If none of these are specified, the default will be to autoscale based on cpuUtilization to 0.6 or 60%. |
| **cool_down_period_sec**  integer | The number of seconds that the autoscaler should wait before it starts collecting information from a new instance. This prevents the autoscaler from collecting information when the instance is initializing, during which the collected usage would not be reliable. The default time autoscaler waits is 60 seconds.  Virtual machine initialization times might vary because of numerous factors. We recommend that you test how long an instance may take to initialize. To do this, create an instance and time the startup process.  **Default:** `60` |
| **cpu_utilization**  dictionary | Defines the CPU utilization policy that allows the autoscaler to scale based on the average CPU utilization of a managed instance group. |
| **predictive_method**  string | Indicates whether predictive autoscaling based on CPU metric is enabled. Valid values are: - NONE (default). No predictive method is used. The autoscaler scales the group to meet current demand based on real-time metrics.   - OPTIMIZE_AVAILABILITY. Predictive autoscaling improves availability by monitoring daily and weekly load patterns and scaling out ahead of anticipated demand.   **Default:** `"NONE"` |
| **utilization_target**  string | The target CPU utilization that the autoscaler should maintain.  Must be a float value in the range (0, 1]. If not specified, the default is 0.6.  If the CPU level is below the target utilization, the autoscaler scales down the number of instances until it reaches the minimum number of instances you specified or until the average CPU of your instances reaches the target utilization.  If the average CPU is above the target utilization, the autoscaler scales up until it reaches the maximum number of instances you specified or until the average utilization reaches the target utilization. |
| **custom_metric_utilizations**  list / elements=dictionary | Configuration parameters of autoscaling based on a custom metric. |
| **metric**  string / required | The identifier (type) of the Stackdriver Monitoring metric.  The metric cannot have negative values.  The metric must have a value type of INT64 or DOUBLE. |
| **utilization_target**  string | The target value of the metric that autoscaler should maintain. This must be a positive value. A utilization metric scales number of virtual machines handling requests to increase or decrease proportionally to the metric.  For example, a good metric to use as a utilizationTarget is www.googleapis.com/compute/instance/network/received_bytes_count.  The autoscaler will work to keep this value constant for each of the instances. |
| **utilization_target_type**  string | Defines how target utilization value is expressed for a Stackdriver Monitoring metric.  Some valid choices include: “GAUGE”, “DELTA_PER_SECOND”, “DELTA_PER_MINUTE” |
| **load_balancing_utilization**  dictionary | Configuration parameters of autoscaling based on a load balancer. |
| **utilization_target**  string | Fraction of backend capacity utilization (set in HTTP(s) load balancing configuration) that autoscaler should maintain. Must be a positive float value. If not defined, the default is 0.8. |
| **max_num_replicas**  integer / required | The maximum number of instances that the autoscaler can scale up to. This is required when creating or updating an autoscaler. The maximum number of replicas should not be lower than minimal number of replicas. |
| **min_num_replicas**  integer | The minimum number of replicas that the autoscaler can scale down to. This cannot be less than 0. If not provided, autoscaler will choose a default value depending on maximum number of instances allowed. |
| **mode**  string | Defines operating mode for this policy.  Some valid choices include: “OFF”, “ONLY_UP”, “ON”  **Default:** `"ON"` |
| **scale_in_control**  dictionary | Defines scale in controls to reduce the risk of response latency and outages due to abrupt scale-in events . |
| **max_scaled_in_replicas**  dictionary | A nested object resource. |
| **fixed**  integer | Specifies a fixed number of VM instances. This must be a positive integer. |
| **percent**  integer | Specifies a percentage of instances between 0 to 100%, inclusive.  For example, specify 80 for 80%. |
| **time_window_sec**  integer | How long back autoscaling should look when computing recommendations to include directives regarding slower scale down, as described above. |
| **description**  string | An optional description of this resource. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **name**  string / required | Name of the resource. The name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| **project**  string | The Google Cloud Platform project to use. |
| **region**  string / required | URL of the region where the instance group resides. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **target**  string / required | URL of the managed instance group that this autoscaler will scale. |

## [Notes](gcp_compute_region_autoscaler_module.md#id4)

> **Note:**
>
> - API Reference: <https://cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers>
> - Autoscaling Groups of Instances: <https://cloud.google.com/compute/docs/autoscaler/>
> - for authentication, you can set service_account_file using the `GCP_SERVICE_ACCOUNT_FILE` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set access_token using the `GCP_ACCESS_TOKEN` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_compute_region_autoscaler_module.md#id5)

```yaml+jinja
- name: create a network
  google.cloud.gcp_compute_network:
    name: network-instancetemplate
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: network

- name: create a address
  google.cloud.gcp_compute_address:
    name: address-instancetemplate
    region: us-central1
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: address

- name: create a instance template
  google.cloud.gcp_compute_instance_template:
    name: "{{ resource_name }}"
    properties:
      disks:
      - auto_delete: 'true'
        boot: 'true'
        initialize_params:
          source_image: projects/ubuntu-os-cloud/global/images/family/ubuntu-1604-lts
      machine_type: n1-standard-1
      network_interfaces:
      - network: "{{ network }}"
        access_configs:
        - name: test-config
          type: ONE_TO_ONE_NAT
          nat_ip: "{{ address }}"
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: instancetemplate

- name: create a region instance group manager
  google.cloud.gcp_compute_region_instance_group_manager:
    name: "{{ resource_name }}"
    base_instance_name: test1-child
    region: us-central1
    instance_template: "{{ instancetemplate }}"
    target_size: 3
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: igrm

- name: create a region autoscaler
  google.cloud.gcp_compute_region_autoscaler:
    name: my-region-autoscaler
    region: us-central1
    autoscaling_policy:
      min_num_replicas: 1
      max_num_replicas: 5
      cool_down_period_sec: 60
      cpu_utilization:
        utilization_target: 0.5
    target: "{{igrm.selfLink}}"
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_compute_region_autoscaler_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
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
| **region**  string | URL of the region where the instance group resides.  **Returned:** success |
| **target**  string | URL of the managed instance group that this autoscaler will scale.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
