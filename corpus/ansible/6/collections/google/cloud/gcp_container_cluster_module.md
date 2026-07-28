---
collection: ansible
version: "6"
title: "google.cloud.gcp_container_cluster module – Creates a GCP Cluster"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_container_cluster_module.html
fetched_at: 2026-07-27T17:48:55+00:00
---
# google.cloud.gcp_container_cluster module – Creates a GCP Cluster

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
> see [Requirements](gcp_container_cluster_module.md#ansible-collections-google-cloud-gcp-container-cluster-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_container_cluster`.

- [Synopsis](gcp_container_cluster_module.md#synopsis)
- [Requirements](gcp_container_cluster_module.md#requirements)
- [Parameters](gcp_container_cluster_module.md#parameters)
- [Examples](gcp_container_cluster_module.md#examples)
- [Return Values](gcp_container_cluster_module.md#return-values)

## [Synopsis](gcp_container_cluster_module.md#id1)

- A Google Container Engine cluster.

## [Requirements](gcp_container_cluster_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_container_cluster_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **addons_config**  dictionary | Configurations for the various addons available to run in the cluster. |
| **horizontal_pod_autoscaling**  dictionary | Configuration for the horizontal pod autoscaling feature, which increases or decreases the number of replica pods a replication controller has based on the resource usage of the existing pods. |
| **disabled**  boolean | Whether the Horizontal Pod Autoscaling feature is enabled in the cluster. When enabled, it ensures that a Heapster pod is running in the cluster, which is also used by the Cloud Monitoring service.  Choices:   - `false` - `true` |
| **http_load_balancing**  dictionary | Configuration for the HTTP (L7) load balancing controller addon, which makes it easy to set up HTTP load balancers for services in a cluster. |
| **disabled**  boolean | Whether the HTTP Load Balancing controller is enabled in the cluster. When enabled, it runs a small pod in the cluster that manages the load balancers.  Choices:   - `false` - `true` |
| **network_policy_config**  dictionary | Configuration for NetworkPolicy. This only tracks whether the addon is enabled or not on the Master, it does not track whether network policy is enabled for the nodes. |
| **disabled**  boolean | Whether NetworkPolicy is enabled for this cluster.  Choices:   - `false` - `true` |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **binary_authorization**  dictionary | Configuration for the BinaryAuthorization feature. |
| **enabled**  boolean | If enabled, all container images will be validated by Binary Authorization.  Choices:   - `false` - `true` |
| **cluster_ipv4_cidr**  string | The IP address range of the container pods in this cluster, in CIDR notation (e.g. 10.96.0.0/14). Leave blank to have one automatically chosen or specify a /14 block in 10.0.0.0/8. |
| **database_encryption**  dictionary | Configuration of etcd encryption. |
| **key_name**  string | Name of CloudKMS key to use for the encryption of secrets in etcd. Ex.  `projects/my-project/locations/global/keyRings/my-ring/cryptoKeys/my-key` . |
| **state**  string | Denotes the state of etcd encryption.  Some valid choices include: “ENCRYPTED”, “DECRYPTED” |
| **default_max_pods_constraint**  dictionary | The default constraint on the maximum number of pods that can be run simultaneously on a node in the node pool of this cluster.  Only honored if cluster created with IP Alias support. |
| **max_pods_per_node**  string | Constraint enforced on the max num of pods per node. |
| **description**  string | An optional description of this cluster. |
| **enable_kubernetes_alpha**  boolean | Kubernetes alpha features are enabled on this cluster. This includes alpha API groups (e.g. v1alpha1) and features that may not be production ready in the kubernetes version of the master and nodes.  Choices:   - `false` - `true` |
| **enable_tpu**  boolean | (Optional) Whether to enable Cloud TPU resources in this cluster.  See the official documentation - <https://cloud.google.com/tpu/docs/kubernetes-engine-setup> .  Choices:   - `false` - `true` |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **initial_cluster_version**  string | The software version of the master endpoint and kubelets used in the cluster when it was first created. The version can be upgraded over time. |
| **initial_node_count**  integer | The number of nodes to create in this cluster. You must ensure that your Compute Engine resource quota is sufficient for this number of instances. You must also have available firewall and routes quota. For requests, this field should only be used in lieu of a “nodePool” object, since this configuration (along with the “nodeConfig”) will be used to create a “NodePool” object with an auto-generated name. Do not use this and a nodePool at the same time.  This field has been deprecated. Please use nodePool.initial_node_count instead. |
| **ip_allocation_policy**  dictionary | Configuration for controlling how IPs are allocated in the cluster. |
| **cluster_ipv4_cidr_block**  string | The IP address range for the cluster pod IPs. If this field is set, then cluster.cluster_ipv4_cidr must be left blank.  This field is only applicable when useIpAliases is true.  Set to blank to have a range chosen with the default size.  Set to /netmask (e.g. /14) to have a range chosen with a specific netmask. |
| **cluster_secondary_range_name**  string | The name of the secondary range to be used for the cluster CIDR block. The secondary range will be used for pod IP addresses.  This must be an existing secondary range associated with the cluster subnetwork . |
| **create_subnetwork**  boolean | Whether a new subnetwork will be created automatically for the cluster.  Choices:   - `false` - `true` |
| **node_ipv4_cidr_block**  string | The IP address range of the instance IPs in this cluster.  This is applicable only if createSubnetwork is true.  Set to blank to have a range chosen with the default size.  Set to /netmask (e.g. /14) to have a range chosen with a specific netmask. |
| **services_ipv4_cidr_block**  string | The IP address range of the services IPs in this cluster. If blank, a range will be automatically chosen with the default size.  This field is only applicable when useIpAliases is true.  Set to blank to have a range chosen with the default size.  Set to /netmask (e.g. /14) to have a range chosen with a specific netmask. |
| **services_secondary_range_name**  string | The name of the secondary range to be used as for the services CIDR block. The secondary range will be used for service ClusterIPs. This must be an existing secondary range associated with the cluster subnetwork. |
| **subnetwork_name**  string | A custom subnetwork name to be used if createSubnetwork is true.  If this field is empty, then an automatic name will be chosen for the new subnetwork. |
| **tpu_ipv4_cidr_block**  string | The IP address range of the Cloud TPUs in this cluster. If unspecified, a range will be automatically chosen with the default size.  This field is only applicable when useIpAliases is true.  If unspecified, the range will use the default size.  Set to /netmask (e.g. /14) to have a range chosen with a specific netmask. |
| **use_ip_aliases**  boolean | Whether alias IPs will be used for pod IPs in the cluster.  Choices:   - `false` - `true` |
| **kubectl_context**  string | The name of the context for the kubectl config file. Will default to the cluster name. |
| **kubectl_path**  string | The path that the kubectl config file will be written to.  The file will not be created if this path is unset.  Any existing file at this path will be completely overwritten.  This requires the PyYaml library. |
| **legacy_abac**  dictionary | Configuration for the legacy ABAC authorization mode. |
| **enabled**  boolean | Whether the ABAC authorizer is enabled for this cluster. When enabled, identities in the system, including service accounts, nodes, and controllers, will have statically granted permissions beyond those provided by the RBAC configuration or IAM.  Choices:   - `false` - `true` |
| **location**  aliases: zone  string / required | The location where the cluster is deployed. |
| **locations**  aliases: nodeLocations  list / elements=string | The list of Google Compute Engine zones in which the cluster’s nodes should be located. |
| **logging_service**  string | The logging service the cluster should use to write logs. Currently available options: logging.googleapis.com - the Google Cloud Logging service.  none - no logs will be exported from the cluster.  if left as an empty string,logging.googleapis.com will be used.  Some valid choices include: “logging.googleapis.com”, “none” |
| **master_auth**  dictionary | The authentication information for accessing the master endpoint. |
| **client_certificate_config**  dictionary | Configuration for client certificate authentication on the cluster. For clusters before v1.12, if no configuration is specified, a client certificate is issued. |
| **issue_client_certificate**  boolean | Issue a client certificate.  Choices:   - `false` - `true` |
| **password**  string | The password to use for HTTP basic authentication to the master endpoint. Because the master endpoint is open to the Internet, you should create a strong password with a minimum of 16 characters. |
| **username**  string | The username to use for HTTP basic authentication to the master endpoint. |
| **master_authorized_networks_config**  dictionary | Configuration for controlling how IPs are allocated in the cluster. |
| **cidr_blocks**  list / elements=dictionary | Define up to 50 external networks that could access Kubernetes master through HTTPS. |
| **cidr_block**  string | Block specified in CIDR notation. |
| **display_name**  string | Optional field used to identify cidr blocks. |
| **enabled**  boolean | Whether or not master authorized networks is enabled.  Choices:   - `false` - `true` |
| **monitoring_service**  string | The monitoring service the cluster should use to write metrics.  Currently available options: monitoring.googleapis.com - the Google Cloud Monitoring service.  none - no metrics will be exported from the cluster.  if left as an empty string, monitoring.googleapis.com will be used.  Some valid choices include: “monitoring.googleapis.com”, “none” |
| **name**  string | The name of this cluster. The name must be unique within this project and location, and can be up to 40 characters. Must be Lowercase letters, numbers, and hyphens only. Must start with a letter. Must end with a number or a letter. |
| **network**  string | The name of the Google Compute Engine network to which the cluster is connected. If left unspecified, the default network will be used. |
| **network_config**  dictionary | Network configurations . |
| **default_snat_status**  boolean | Whether the cluster disables default in-node sNAT rules. In-node sNAT rules will be disabled when defaultSnatStatus is disabled.  Choices:   - `false` - `true` |
| **enable_intra_node_visibility**  boolean | Whether Intra-node visibility is enabled for this cluster. This makes same node pod to pod traffic visible for VPC network.  Choices:   - `false` - `true` |
| **network_policy**  dictionary | Configuration options for the NetworkPolicy feature. |
| **enabled**  boolean | Whether network policy is enabled on the cluster.  Choices:   - `false` - `true` |
| **provider**  string | The selected network policy provider.  Some valid choices include: “PROVIDER_UNSPECIFIED”, “CALICO” |
| **node_config**  dictionary | Parameters used in creating the cluster’s nodes.  For requests, this field should only be used in lieu of a “nodePool” object, since this configuration (along with the “initialNodeCount”) will be used to create a “NodePool” object with an auto-generated name. Do not use this and a nodePool at the same time. For responses, this field will be populated with the node configuration of the first node pool. If unspecified, the defaults are used. |
| **accelerators**  list / elements=dictionary | A list of hardware accelerators to be attached to each node. See <https://cloud.google.com/compute/docs/gpus> for more information about support for GPUs. |
| **accelerator_count**  string | The number of accelerator cards exposed to an instance. |
| **accelerator_type**  string | The accelerator type resource name. |
| **disk_size_gb**  integer | Size of the disk attached to each node, specified in GB. The smallest allowed disk size is 10GB. If unspecified, the default disk size is 100GB. |
| **disk_type**  string | Type of the disk attached to each node (e.g. ‘pd-standard’ or ‘pd-ssd’) If unspecified, the default disk type is ‘pd-standard’ . |
| **image_type**  string | The image type to use for this node. Note that for a given image type, the latest version of it will be used. |
| **labels**  dictionary | The map of Kubernetes labels (key/value pairs) to be applied to each node. These will added in addition to any default label(s) that Kubernetes may apply to the node. In case of conflict in label keys, the applied set may differ depending on the Kubernetes version – it’s best to assume the behavior is undefined and conflicts should be avoided. For more information, including usage and the valid values, see: <http://kubernetes.io/v1.1/docs/user-guide/labels.html> An object containing a list of “key”: value pairs.  Example: { “name”: “wrench”, “mass”: “1.3kg”, “count”: “3” }. |
| **local_ssd_count**  integer | The number of local SSD disks to be attached to the node.  The limit for this value is dependant upon the maximum number of disks available on a machine per zone. See: <https://cloud.google.com/compute/docs/disks/local-ssd#local_ssd_limits> for more information. |
| **machine_type**  string | The name of a Google Compute Engine machine type (e.g.  n1-standard-1). If unspecified, the default machine type is n1-standard-1. |
| **metadata**  dictionary | The metadata key/value pairs assigned to instances in the cluster.  Keys must conform to the regexp [a-zA-Z0-9-_]+ and be less than 128 bytes in length. These are reflected as part of a URL in the metadata server. Additionally, to avoid ambiguity, keys must not conflict with any other metadata keys for the project or be one of the four reserved keys: “instance-template”, “kube-env”, “startup-script”, and “user-data” Values are free-form strings, and only have meaning as interpreted by the image running in the instance. The only restriction placed on them is that each value’s size must be less than or equal to 32 KB.  The total size of all keys and values must be less than 512 KB.  An object containing a list of “key”: value pairs.  Example: { “name”: “wrench”, “mass”: “1.3kg”, “count”: “3” }. |
| **min_cpu_platform**  string | Minimum CPU platform to be used by this instance. The instance may be scheduled on the specified or newer CPU platform. |
| **oauth_scopes**  list / elements=string | The set of Google API scopes to be made available on all of the node VMs under the “default” service account.  The following scopes are recommended, but not required, and by default are not included: <https://www.googleapis.com/auth/compute> is required for mounting persistent storage on your nodes.  <https://www.googleapis.com/auth/devstorage.read_only> is required for communicating with gcr.io (the Google Container Registry).  If unspecified, no scopes are added, unless Cloud Logging or Cloud Monitoring are enabled, in which case their required scopes will be added. |
| **preemptible**  boolean | Whether the nodes are created as preemptible VM instances. See: <https://cloud.google.com/compute/docs/instances/preemptible> for more information about preemptible VM instances.  Choices:   - `false` - `true` |
| **service_account**  string | The Google Cloud Platform Service Account to be used by the node VMs. If no Service Account is specified, the “default” service account is used. |
| **shielded_instance_config**  dictionary | Shielded Instance options. |
| **enable_integrity_monitoring**  boolean | Defines whether the instance has integrity monitoring enabled.  Enables monitoring and attestation of the boot integrity of the instance.  The attestation is performed against the integrity policy baseline. This baseline is initially derived from the implicitly trusted boot image when the instance is created.  Choices:   - `false` - `true` |
| **enable_secure_boot**  boolean | Defines whether the instance has Secure Boot enabled.  Secure Boot helps ensure that the system only runs authentic software by verifying the digital signature of all boot components, and halting the boot process if signature verification fails.  Choices:   - `false` - `true` |
| **tags**  list / elements=string | The list of instance tags applied to all nodes. Tags are used to identify valid sources or targets for network firewalls and are specified by the client during cluster or node pool creation. Each tag within the list must comply with RFC1035. |
| **taints**  list / elements=dictionary | List of kubernetes taints to be applied to each node.  For more information, including usage and the valid values, see: <https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/> . |
| **effect**  string | Effect for taint.  Some valid choices include: “EFFECT_UNSPECIFIED”, “NO_SCHEDULE”, “PREFER_NO_SCHEDULE”, “NO_EXECUTE” |
| **key**  string | Key for taint. |
| **value**  string | Value for taint. |
| **private_cluster_config**  dictionary | Configuration for a private cluster. |
| **enable_private_endpoint**  boolean | Whether the master’s internal IP address is used as the cluster endpoint.  Choices:   - `false` - `true` |
| **enable_private_nodes**  boolean | Whether nodes have internal IP addresses only. If enabled, all nodes are given only RFC 1918 private addresses and communicate with the master via private networking.  Choices:   - `false` - `true` |
| **master_ipv4_cidr_block**  string | The IP range in CIDR notation to use for the hosted master network. This range will be used for assigning internal IP addresses to the master or set of masters, as well as the ILB VIP. This range must not overlap with any other ranges in use within the cluster’s network. |
| **project**  string | The Google Cloud Platform project to use. |
| **release_channel**  dictionary | ReleaseChannel indicates which release channel a cluster is subscribed to.  Release channels are arranged in order of risk and frequency of updates. |
| **channel**  string | Which release channel the cluster is subscribed to.  Some valid choices include: “UNSPECIFIED”, “RAPID”, “REGULAR”, “STABLE” |
| **resource_labels**  dictionary | The resource labels for the cluster to use to annotate any related Google Compute Engine resources. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **shielded_nodes**  dictionary | Shielded Nodes configuration. |
| **enabled**  boolean | Whether Shielded Nodes features are enabled on all nodes in this cluster.  Choices:   - `false` - `true` |
| **state**  string | Whether the given object should exist in GCP  Choices:   - `"present"` ← (default) - `"absent"` |
| **subnetwork**  string | The name of the Google Compute Engine subnetwork to which the cluster is connected. |

## [Examples](gcp_container_cluster_module.md#id4)

```yaml+jinja
- name: create a cluster
  google.cloud.gcp_container_cluster:
    name: my-cluster
    initial_node_count: 2
    master_auth:
      username: cluster_admin
      password: my-secret-password
    node_config:
      machine_type: n1-standard-4
      disk_size_gb: 500
    location: us-central1-a
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_container_cluster_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **addonsConfig**  complex | Configurations for the various addons available to run in the cluster.  Returned: success |
| **horizontalPodAutoscaling**  complex | Configuration for the horizontal pod autoscaling feature, which increases or decreases the number of replica pods a replication controller has based on the resource usage of the existing pods.  Returned: success |
| **disabled**  boolean | Whether the Horizontal Pod Autoscaling feature is enabled in the cluster. When enabled, it ensures that a Heapster pod is running in the cluster, which is also used by the Cloud Monitoring service.  Returned: success |
| **httpLoadBalancing**  complex | Configuration for the HTTP (L7) load balancing controller addon, which makes it easy to set up HTTP load balancers for services in a cluster.  Returned: success |
| **disabled**  boolean | Whether the HTTP Load Balancing controller is enabled in the cluster. When enabled, it runs a small pod in the cluster that manages the load balancers.  Returned: success |
| **networkPolicyConfig**  complex | Configuration for NetworkPolicy. This only tracks whether the addon is enabled or not on the Master, it does not track whether network policy is enabled for the nodes.  Returned: success |
| **disabled**  boolean | Whether NetworkPolicy is enabled for this cluster.  Returned: success |
| **binaryAuthorization**  complex | Configuration for the BinaryAuthorization feature.  Returned: success |
| **enabled**  boolean | If enabled, all container images will be validated by Binary Authorization.  Returned: success |
| **clusterIpv4Cidr**  string | The IP address range of the container pods in this cluster, in CIDR notation (e.g. 10.96.0.0/14). Leave blank to have one automatically chosen or specify a /14 block in 10.0.0.0/8.  Returned: success |
| **conditions**  complex | Which conditions caused the current cluster state.  Returned: success |
| **code**  string | Machine-friendly representation of the condition.  Returned: success |
| **message**  string | Human-friendly representation of the condition.  Returned: success |
| **createTime**  string | The time the cluster was created, in RFC3339 text format.  Returned: success |
| **currentMasterVersion**  string | The current software version of the master endpoint.  Returned: success |
| **currentNodeCount**  integer | The number of nodes currently in the cluster.  Returned: success |
| **currentNodeVersion**  string | The current version of the node software components. If they are currently at multiple versions because they’re in the process of being upgraded, this reflects the minimum version of all nodes.  Returned: success |
| **databaseEncryption**  complex | Configuration of etcd encryption.  Returned: success |
| **keyName**  string | Name of CloudKMS key to use for the encryption of secrets in etcd. Ex.  `projects/my-project/locations/global/keyRings/my-ring/cryptoKeys/my-key` .  Returned: success |
| **state**  string | Denotes the state of etcd encryption.  Returned: success |
| **defaultMaxPodsConstraint**  complex | The default constraint on the maximum number of pods that can be run simultaneously on a node in the node pool of this cluster.  Only honored if cluster created with IP Alias support.  Returned: success |
| **maxPodsPerNode**  string | Constraint enforced on the max num of pods per node.  Returned: success |
| **description**  string | An optional description of this cluster.  Returned: success |
| **enableKubernetesAlpha**  boolean | Kubernetes alpha features are enabled on this cluster. This includes alpha API groups (e.g. v1alpha1) and features that may not be production ready in the kubernetes version of the master and nodes.  Returned: success |
| **enableTpu**  boolean | (Optional) Whether to enable Cloud TPU resources in this cluster.  See the official documentation - <https://cloud.google.com/tpu/docs/kubernetes-engine-setup> .  Returned: success |
| **endpoint**  string | The IP address of this cluster’s master endpoint.  The endpoint can be accessed from the internet at <https://username:password@endpoint/> See the masterAuth property of this resource for username and password information.  Returned: success |
| **expireTime**  string | The time the cluster will be automatically deleted in RFC3339 text format.  Returned: success |
| **initialClusterVersion**  string | The software version of the master endpoint and kubelets used in the cluster when it was first created. The version can be upgraded over time.  Returned: success |
| **initialNodeCount**  integer | The number of nodes to create in this cluster. You must ensure that your Compute Engine resource quota is sufficient for this number of instances. You must also have available firewall and routes quota. For requests, this field should only be used in lieu of a “nodePool” object, since this configuration (along with the “nodeConfig”) will be used to create a “NodePool” object with an auto-generated name. Do not use this and a nodePool at the same time.  This field has been deprecated. Please use nodePool.initial_node_count instead.  Returned: success |
| **ipAllocationPolicy**  complex | Configuration for controlling how IPs are allocated in the cluster.  Returned: success |
| **clusterIpv4CidrBlock**  string | The IP address range for the cluster pod IPs. If this field is set, then cluster.cluster_ipv4_cidr must be left blank.  This field is only applicable when useIpAliases is true.  Set to blank to have a range chosen with the default size.  Set to /netmask (e.g. /14) to have a range chosen with a specific netmask.  Returned: success |
| **clusterSecondaryRangeName**  string | The name of the secondary range to be used for the cluster CIDR block. The secondary range will be used for pod IP addresses.  This must be an existing secondary range associated with the cluster subnetwork .  Returned: success |
| **createSubnetwork**  boolean | Whether a new subnetwork will be created automatically for the cluster.  Returned: success |
| **nodeIpv4CidrBlock**  string | The IP address range of the instance IPs in this cluster.  This is applicable only if createSubnetwork is true.  Set to blank to have a range chosen with the default size.  Set to /netmask (e.g. /14) to have a range chosen with a specific netmask.  Returned: success |
| **servicesIpv4CidrBlock**  string | The IP address range of the services IPs in this cluster. If blank, a range will be automatically chosen with the default size.  This field is only applicable when useIpAliases is true.  Set to blank to have a range chosen with the default size.  Set to /netmask (e.g. /14) to have a range chosen with a specific netmask.  Returned: success |
| **servicesSecondaryRangeName**  string | The name of the secondary range to be used as for the services CIDR block. The secondary range will be used for service ClusterIPs. This must be an existing secondary range associated with the cluster subnetwork.  Returned: success |
| **subnetworkName**  string | A custom subnetwork name to be used if createSubnetwork is true.  If this field is empty, then an automatic name will be chosen for the new subnetwork.  Returned: success |
| **tpuIpv4CidrBlock**  string | The IP address range of the Cloud TPUs in this cluster. If unspecified, a range will be automatically chosen with the default size.  This field is only applicable when useIpAliases is true.  If unspecified, the range will use the default size.  Set to /netmask (e.g. /14) to have a range chosen with a specific netmask.  Returned: success |
| **useIpAliases**  boolean | Whether alias IPs will be used for pod IPs in the cluster.  Returned: success |
| **kubectlContext**  string | The name of the context for the kubectl config file. Will default to the cluster name.  Returned: success |
| **kubectlPath**  string | The path that the kubectl config file will be written to.  The file will not be created if this path is unset.  Any existing file at this path will be completely overwritten.  This requires the PyYaml library.  Returned: success |
| **labelFingerprint**  string | The fingerprint of the set of labels for this cluster.  Returned: success |
| **legacyAbac**  complex | Configuration for the legacy ABAC authorization mode.  Returned: success |
| **enabled**  boolean | Whether the ABAC authorizer is enabled for this cluster. When enabled, identities in the system, including service accounts, nodes, and controllers, will have statically granted permissions beyond those provided by the RBAC configuration or IAM.  Returned: success |
| **location**  string | The location where the cluster is deployed.  Returned: success |
| **locations**  list / elements=string | The list of Google Compute Engine zones in which the cluster’s nodes should be located.  Returned: success |
| **loggingService**  string | The logging service the cluster should use to write logs. Currently available options: logging.googleapis.com - the Google Cloud Logging service.  none - no logs will be exported from the cluster.  if left as an empty string,logging.googleapis.com will be used.  Returned: success |
| **masterAuth**  complex | The authentication information for accessing the master endpoint.  Returned: success |
| **clientCertificate**  string | Base64-encoded public certificate used by clients to authenticate to the cluster endpoint.  Returned: success |
| **clientCertificateConfig**  complex | Configuration for client certificate authentication on the cluster. For clusters before v1.12, if no configuration is specified, a client certificate is issued.  Returned: success |
| **issueClientCertificate**  boolean | Issue a client certificate.  Returned: success |
| **clientKey**  string | Base64-encoded private key used by clients to authenticate to the cluster endpoint.  Returned: success |
| **clusterCaCertificate**  string | Base64-encoded public certificate that is the root of trust for the cluster.  Returned: success |
| **password**  string | The password to use for HTTP basic authentication to the master endpoint. Because the master endpoint is open to the Internet, you should create a strong password with a minimum of 16 characters.  Returned: success |
| **username**  string | The username to use for HTTP basic authentication to the master endpoint.  Returned: success |
| **masterAuthorizedNetworksConfig**  complex | Configuration for controlling how IPs are allocated in the cluster.  Returned: success |
| **cidrBlocks**  complex | Define up to 50 external networks that could access Kubernetes master through HTTPS.  Returned: success |
| **cidrBlock**  string | Block specified in CIDR notation.  Returned: success |
| **displayName**  string | Optional field used to identify cidr blocks.  Returned: success |
| **enabled**  boolean | Whether or not master authorized networks is enabled.  Returned: success |
| **monitoringService**  string | The monitoring service the cluster should use to write metrics.  Currently available options: monitoring.googleapis.com - the Google Cloud Monitoring service.  none - no metrics will be exported from the cluster.  if left as an empty string, monitoring.googleapis.com will be used.  Returned: success |
| **name**  string | The name of this cluster. The name must be unique within this project and location, and can be up to 40 characters. Must be Lowercase letters, numbers, and hyphens only. Must start with a letter. Must end with a number or a letter.  Returned: success |
| **network**  string | The name of the Google Compute Engine network to which the cluster is connected. If left unspecified, the default network will be used.  Returned: success |
| **networkConfig**  complex | Network configurations .  Returned: success |
| **defaultSnatStatus**  boolean | Whether the cluster disables default in-node sNAT rules. In-node sNAT rules will be disabled when defaultSnatStatus is disabled.  Returned: success |
| **enableIntraNodeVisibility**  boolean | Whether Intra-node visibility is enabled for this cluster. This makes same node pod to pod traffic visible for VPC network.  Returned: success |
| **network**  string | The relative name of the Google Compute Engine network to which the cluster is connected.  Example: projects/my-project/global/networks/my-network .  Returned: success |
| **subnetwork**  string | The relative name of the Google Compute Engine subnetwork to which the cluster is connected.  Example: projects/my-project/regions/us-central1/subnetworks/my-subnet .  Returned: success |
| **networkPolicy**  complex | Configuration options for the NetworkPolicy feature.  Returned: success |
| **enabled**  boolean | Whether network policy is enabled on the cluster.  Returned: success |
| **provider**  string | The selected network policy provider.  Returned: success |
| **nodeConfig**  complex | Parameters used in creating the cluster’s nodes.  For requests, this field should only be used in lieu of a “nodePool” object, since this configuration (along with the “initialNodeCount”) will be used to create a “NodePool” object with an auto-generated name. Do not use this and a nodePool at the same time. For responses, this field will be populated with the node configuration of the first node pool. If unspecified, the defaults are used.  Returned: success |
| **accelerators**  complex | A list of hardware accelerators to be attached to each node. See <https://cloud.google.com/compute/docs/gpus> for more information about support for GPUs.  Returned: success |
| **acceleratorCount**  string | The number of accelerator cards exposed to an instance.  Returned: success |
| **acceleratorType**  string | The accelerator type resource name.  Returned: success |
| **diskSizeGb**  integer | Size of the disk attached to each node, specified in GB. The smallest allowed disk size is 10GB. If unspecified, the default disk size is 100GB.  Returned: success |
| **diskType**  string | Type of the disk attached to each node (e.g. ‘pd-standard’ or ‘pd-ssd’) If unspecified, the default disk type is ‘pd-standard’ .  Returned: success |
| **imageType**  string | The image type to use for this node. Note that for a given image type, the latest version of it will be used.  Returned: success |
| **labels**  dictionary | The map of Kubernetes labels (key/value pairs) to be applied to each node. These will added in addition to any default label(s) that Kubernetes may apply to the node. In case of conflict in label keys, the applied set may differ depending on the Kubernetes version – it’s best to assume the behavior is undefined and conflicts should be avoided. For more information, including usage and the valid values, see: <http://kubernetes.io/v1.1/docs/user-guide/labels.html> An object containing a list of “key”: value pairs.  Example: { “name”: “wrench”, “mass”: “1.3kg”, “count”: “3” }.  Returned: success |
| **localSsdCount**  integer | The number of local SSD disks to be attached to the node.  The limit for this value is dependant upon the maximum number of disks available on a machine per zone. See: <https://cloud.google.com/compute/docs/disks/local-ssd#local_ssd_limits> for more information.  Returned: success |
| **machineType**  string | The name of a Google Compute Engine machine type (e.g.  n1-standard-1). If unspecified, the default machine type is n1-standard-1.  Returned: success |
| **metadata**  dictionary | The metadata key/value pairs assigned to instances in the cluster.  Keys must conform to the regexp [a-zA-Z0-9-_]+ and be less than 128 bytes in length. These are reflected as part of a URL in the metadata server. Additionally, to avoid ambiguity, keys must not conflict with any other metadata keys for the project or be one of the four reserved keys: “instance-template”, “kube-env”, “startup-script”, and “user-data” Values are free-form strings, and only have meaning as interpreted by the image running in the instance. The only restriction placed on them is that each value’s size must be less than or equal to 32 KB.  The total size of all keys and values must be less than 512 KB.  An object containing a list of “key”: value pairs.  Example: { “name”: “wrench”, “mass”: “1.3kg”, “count”: “3” }.  Returned: success |
| **minCpuPlatform**  string | Minimum CPU platform to be used by this instance. The instance may be scheduled on the specified or newer CPU platform.  Returned: success |
| **oauthScopes**  list / elements=string | The set of Google API scopes to be made available on all of the node VMs under the “default” service account.  The following scopes are recommended, but not required, and by default are not included: <https://www.googleapis.com/auth/compute> is required for mounting persistent storage on your nodes.  <https://www.googleapis.com/auth/devstorage.read_only> is required for communicating with gcr.io (the Google Container Registry).  If unspecified, no scopes are added, unless Cloud Logging or Cloud Monitoring are enabled, in which case their required scopes will be added.  Returned: success |
| **preemptible**  boolean | Whether the nodes are created as preemptible VM instances. See: <https://cloud.google.com/compute/docs/instances/preemptible> for more information about preemptible VM instances.  Returned: success |
| **serviceAccount**  string | The Google Cloud Platform Service Account to be used by the node VMs. If no Service Account is specified, the “default” service account is used.  Returned: success |
| **shieldedInstanceConfig**  complex | Shielded Instance options.  Returned: success |
| **enableIntegrityMonitoring**  boolean | Defines whether the instance has integrity monitoring enabled.  Enables monitoring and attestation of the boot integrity of the instance.  The attestation is performed against the integrity policy baseline. This baseline is initially derived from the implicitly trusted boot image when the instance is created.  Returned: success |
| **enableSecureBoot**  boolean | Defines whether the instance has Secure Boot enabled.  Secure Boot helps ensure that the system only runs authentic software by verifying the digital signature of all boot components, and halting the boot process if signature verification fails.  Returned: success |
| **tags**  list / elements=string | The list of instance tags applied to all nodes. Tags are used to identify valid sources or targets for network firewalls and are specified by the client during cluster or node pool creation. Each tag within the list must comply with RFC1035.  Returned: success |
| **taints**  complex | List of kubernetes taints to be applied to each node.  For more information, including usage and the valid values, see: <https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/> .  Returned: success |
| **effect**  string | Effect for taint.  Returned: success |
| **key**  string | Key for taint.  Returned: success |
| **value**  string | Value for taint.  Returned: success |
| **nodeIpv4CidrSize**  integer | The size of the address space on each node for hosting containers.  This is provisioned from within the container_ipv4_cidr range.  Returned: success |
| **nodePools**  complex | Node pools belonging to this cluster.  Returned: success |
| **name**  string | Name of the node pool.  Returned: success |
| **privateClusterConfig**  complex | Configuration for a private cluster.  Returned: success |
| **enablePrivateEndpoint**  boolean | Whether the master’s internal IP address is used as the cluster endpoint.  Returned: success |
| **enablePrivateNodes**  boolean | Whether nodes have internal IP addresses only. If enabled, all nodes are given only RFC 1918 private addresses and communicate with the master via private networking.  Returned: success |
| **masterIpv4CidrBlock**  string | The IP range in CIDR notation to use for the hosted master network. This range will be used for assigning internal IP addresses to the master or set of masters, as well as the ILB VIP. This range must not overlap with any other ranges in use within the cluster’s network.  Returned: success |
| **privateEndpoint**  string | The internal IP address of this cluster’s master endpoint.  Returned: success |
| **publicEndpoint**  string | The external IP address of this cluster’s master endpoint.  Returned: success |
| **releaseChannel**  complex | ReleaseChannel indicates which release channel a cluster is subscribed to.  Release channels are arranged in order of risk and frequency of updates.  Returned: success |
| **channel**  string | Which release channel the cluster is subscribed to.  Returned: success |
| **resourceLabels**  dictionary | The resource labels for the cluster to use to annotate any related Google Compute Engine resources.  Returned: success |
| **servicesIpv4Cidr**  string | The IP address range of the Kubernetes services in this cluster, in CIDR notation (e.g. 1.2.3.4/29). Service addresses are typically put in the last /16 from the container CIDR.  Returned: success |
| **shieldedNodes**  complex | Shielded Nodes configuration.  Returned: success |
| **enabled**  boolean | Whether Shielded Nodes features are enabled on all nodes in this cluster.  Returned: success |
| **status**  string | The current status of this cluster.  Returned: success |
| **statusMessage**  string | Additional information about the current status of this cluster, if available.  Returned: success |
| **subnetwork**  string | The name of the Google Compute Engine subnetwork to which the cluster is connected.  Returned: success |
| **tpuIpv4CidrBlock**  string | The IP address range of the Cloud TPUs in this cluster, in [CIDR](<http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>) notation (e.g. `1.2.3.4/29`).  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
