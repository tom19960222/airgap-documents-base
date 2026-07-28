---
collection: ansible
version: "6"
title: "google.cloud.gcp_container_node_pool_info module – Gather info for GCP NodePool"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_container_node_pool_info_module.html
fetched_at: 2026-07-27T17:48:57+00:00
---
# google.cloud.gcp_container_node_pool_info module – Gather info for GCP NodePool

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
> see [Requirements](gcp_container_node_pool_info_module.md#ansible-collections-google-cloud-gcp-container-node-pool-info-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_container_node_pool_info`.

- [Synopsis](gcp_container_node_pool_info_module.md#synopsis)
- [Requirements](gcp_container_node_pool_info_module.md#requirements)
- [Parameters](gcp_container_node_pool_info_module.md#parameters)
- [Notes](gcp_container_node_pool_info_module.md#notes)
- [Examples](gcp_container_node_pool_info_module.md#examples)
- [Return Values](gcp_container_node_pool_info_module.md#return-values)

## [Synopsis](gcp_container_node_pool_info_module.md#id1)

- Gather info for GCP NodePool

## [Requirements](gcp_container_node_pool_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_container_node_pool_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **cluster**  dictionary / required | The cluster this node pool belongs to.  This field represents a link to a Cluster resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘name’ and value of your resource’s name Alternatively, you can add `register: name-of-resource` to a gcp_container_cluster task and then set this cluster field to “{{ name-of-resource }}” |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **location**  aliases: region, zone  string / required | The location where the node pool is deployed. |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |

## [Notes](gcp_container_node_pool_info_module.md#id4)

> **Note:**
>
> - for authentication, you can set service_account_file using the `gcp_service_account_file` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_container_node_pool_info_module.md#id5)

```yaml+jinja
- name: get info on a node pool
  gcp_container_node_pool_info:
    cluster: "{{ cluster }}"
    location: us-central1-a
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
```

## [Return Values](gcp_container_node_pool_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resources**  complex | List of resources  Returned: always |
| **autoscaling**  complex | Autoscaler configuration for this NodePool. Autoscaler is enabled only if a valid configuration is present.  Returned: success |
| **enabled**  boolean | Is autoscaling enabled for this node pool.  Returned: success |
| **maxNodeCount**  integer | Maximum number of nodes in the NodePool. Must be >= minNodeCount.  There has to enough quota to scale up the cluster.  Returned: success |
| **minNodeCount**  integer | Minimum number of nodes in the NodePool. Must be >= 1 and <= maxNodeCount.  Returned: success |
| **cluster**  dictionary | The cluster this node pool belongs to.  Returned: success |
| **conditions**  complex | Which conditions caused the current node pool state.  Returned: success |
| **code**  string | Machine-friendly representation of the condition.  Returned: success |
| **config**  complex | The node configuration of the pool.  Returned: success |
| **accelerators**  complex | A list of hardware accelerators to be attached to each node.  Returned: success |
| **acceleratorCount**  integer | The number of the accelerator cards exposed to an instance.  Returned: success |
| **acceleratorType**  string | The accelerator type resource name.  Returned: success |
| **diskSizeGb**  integer | Size of the disk attached to each node, specified in GB. The smallest allowed disk size is 10GB. If unspecified, the default disk size is 100GB.  Returned: success |
| **diskType**  string | Type of the disk attached to each node (e.g. ‘pd-standard’ or ‘pd-ssd’) If unspecified, the default disk type is ‘pd-standard’ .  Returned: success |
| **imageType**  string | The image type to use for this node. Note that for a given image type, the latest version of it will be used.  Returned: success |
| **labels**  dictionary | The map of Kubernetes labels (key/value pairs) to be applied to each node. These will added in addition to any default label(s) that Kubernetes may apply to the node. In case of conflict in label keys, the applied set may differ depending on the Kubernetes version – it’s best to assume the behavior is undefined and conflicts should be avoided. For more information, including usage and the valid values, see: <http://kubernetes.io/v1.1/docs/user-guide/labels.html> An object containing a list of “key”: value pairs.  Example: { “name”: “wrench”, “mass”: “1.3kg”, “count”: “3” }.  Returned: success |
| **localSsdCount**  integer | The number of local SSD disks to be attached to the node.  The limit for this value is dependant upon the maximum number of disks available on a machine per zone. See: <https://cloud.google.com/compute/docs/disks/local-ssd#local_ssd_limits> for more information.  Returned: success |
| **machineType**  string | The name of a Google Compute Engine machine type (e.g.  n1-standard-1). If unspecified, the default machine type is n1-standard-1.  Returned: success |
| **metadata**  dictionary | The metadata key/value pairs assigned to instances in the cluster.  Keys must conform to the regexp [a-zA-Z0-9-_]+ and be less than 128 bytes in length. These are reflected as part of a URL in the metadata server. Additionally, to avoid ambiguity, keys must not conflict with any other metadata keys for the project or be one of the four reserved keys: “instance-template”, “kube-env”, “startup-script”, and “user-data” Values are free-form strings, and only have meaning as interpreted by the image running in the instance. The only restriction placed on them is that each value’s size must be less than or equal to 32 KB.  The total size of all keys and values must be less than 512 KB.  An object containing a list of “key”: value pairs.  Example: { “name”: “wrench”, “mass”: “1.3kg”, “count”: “3” }.  Returned: success |
| **minCpuPlatform**  string | Minimum CPU platform to be used by this instance. The instance may be scheduled on the specified or newer CPU platform .  Returned: success |
| **oauthScopes**  list / elements=string | The set of Google API scopes to be made available on all of the node VMs under the “default” service account.  The following scopes are recommended, but not required, and by default are not included: <https://www.googleapis.com/auth/compute> is required for mounting persistent storage on your nodes.  <https://www.googleapis.com/auth/devstorage.read_only> is required for communicating with gcr.io (the Google Container Registry).  If unspecified, no scopes are added, unless Cloud Logging or Cloud Monitoring are enabled, in which case their required scopes will be added.  Returned: success |
| **preemptible**  boolean | Whether the nodes are created as preemptible VM instances. See: <https://cloud.google.com/compute/docs/instances/preemptible> for more information about preemptible VM instances.  Returned: success |
| **serviceAccount**  string | The Google Cloud Platform Service Account to be used by the node VMs. If no Service Account is specified, the “default” service account is used.  Returned: success |
| **shieldedInstanceConfig**  complex | Shielded Instance options.  Returned: success |
| **enableIntegrityMonitoring**  boolean | Defines whether the instance has integrity monitoring enabled.  Enables monitoring and attestation of the boot integrity of the instance.  The attestation is performed against the integrity policy baseline. This baseline is initially derived from the implicitly trusted boot image when the instance is created.  Returned: success |
| **enableSecureBoot**  boolean | Defines whether the instance has Secure Boot enabled.  Secure Boot helps ensure that the system only runs authentic software by verifying the digital signature of all boot components, and halting the boot process if signature verification fails.  Returned: success |
| **tags**  list / elements=string | The list of instance tags applied to all nodes. Tags are used to identify valid sources or targets for network firewalls and are specified by the client during cluster or node pool creation. Each tag within the list must comply with RFC1035.  Returned: success |
| **taints**  complex | List of kubernetes taints to be applied to each node.  Returned: success |
| **effect**  string | Effect for taint.  Returned: success |
| **key**  string | Key for taint.  Returned: success |
| **value**  string | Value for taint.  Returned: success |
| **workloadMetaConfig**  complex | WorkloadMetadataConfig defines the metadata configuration to expose to workloads on the node pool.  Returned: success |
| **mode**  string | Mode is the configuration for how to expose metadata to workloads running on the node pool.  Returned: success |
| **initialNodeCount**  integer | The initial node count for the pool. You must ensure that your Compute Engine resource quota is sufficient for this number of instances. You must also have available firewall and routes quota.  Returned: success |
| **location**  string | The location where the node pool is deployed.  Returned: success |
| **management**  complex | Management configuration for this NodePool.  Returned: success |
| **autoRepair**  boolean | A flag that specifies whether the node auto-repair is enabled for the node pool. If enabled, the nodes in this node pool will be monitored and, if they fail health checks too many times, an automatic repair action will be triggered.  Returned: success |
| **autoUpgrade**  boolean | A flag that specifies whether node auto-upgrade is enabled for the node pool. If enabled, node auto-upgrade helps keep the nodes in your node pool up to date with the latest release version of Kubernetes.  Returned: success |
| **upgradeOptions**  complex | Specifies the Auto Upgrade knobs for the node pool.  Returned: success |
| **autoUpgradeStartTime**  string | This field is set when upgrades are about to commence with the approximate start time for the upgrades, in RFC3339 text format.  Returned: success |
| **description**  string | This field is set when upgrades are about to commence with the description of the upgrade.  Returned: success |
| **maxPodsConstraint**  complex | The constraint on the maximum number of pods that can be run simultaneously on a node in the node pool.  Returned: success |
| **maxPodsPerNode**  integer | Constraint enforced on the max num of pods per node.  Returned: success |
| **name**  string | The name of the node pool.  Returned: success |
| **podIpv4CidrSize**  integer | The pod CIDR block size per node in this node pool.  Returned: success |
| **status**  string | Status of nodes in this pool instance.  Returned: success |
| **statusMessage**  string | Additional information about the current status of this node pool instance.  Returned: success |
| **version**  string | The version of the Kubernetes of this node.  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
