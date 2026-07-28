---
collection: ansible
version: "8"
title: "openstack.cloud.coe_cluster module – Manage COE cluster in OpenStack Cloud"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/coe_cluster_module.html
fetched_at: 2026-07-28T02:47:32+00:00
---
# openstack.cloud.coe_cluster module – Manage COE cluster in OpenStack Cloud

> **Note:**
>
> This module is part of the [openstack.cloud collection](https://galaxy.ansible.com/ui/repo/published/openstack/cloud/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install openstack.cloud`.
> You need further requirements to be able to use this module,
> see [Requirements](coe_cluster_module.md#ansible-collections-openstack-cloud-coe-cluster-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.coe_cluster`.

- [Synopsis](coe_cluster_module.md#synopsis)
- [Requirements](coe_cluster_module.md#requirements)
- [Parameters](coe_cluster_module.md#parameters)
- [Notes](coe_cluster_module.md#notes)
- [Examples](coe_cluster_module.md#examples)
- [Return Values](coe_cluster_module.md#return-values)

## [Synopsis](coe_cluster_module.md#id1)

- Add or remove a COE (Container Orchestration Engine) cluster via OpenStack’s Magnum aka Container Infrastructure Management API.

## [Requirements](coe_cluster_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](coe_cluster_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **cluster_template_id**  string | The template ID of cluster template.  Required if *state* is `present`. |
| **discovery_url**  string | URL used for cluster node discovery. |
| **flavor_id**  string | The flavor of the minion node for this cluster template. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **is_floating_ip_enabled**  aliases: floating_ip_enabled  boolean | Indicates whether created cluster should have a floating ip.  Whether enable or not using the floating IP of cloud provider. Some cloud providers used floating IP, some used public IP, thus Magnum provide this option for specifying the choice of using floating IP.  If not set, the value of *is_floating_ip_enabled* of the cluster template specified with *cluster_template_id* will be used.  When *is_floating_ip_enabled* is set to `true`, then *external_network_id* in cluster template must be defined.  **Choices:**   - `false` - `true` |
| **keypair**  string | Name of the keypair to use. |
| **labels**  any | One or more key/value pairs. |
| **master_count**  integer | The number of master nodes for this cluster.  Magnum’s default value for *master_count* is 1. |
| **master_flavor_id**  string | The flavor of the master node for this cluster template. |
| **name**  string / required | Name that has to be given to the cluster template. |
| **node_count**  integer | The number of nodes for this cluster.  Magnum’s default value for *node_count* is 1. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Indicate desired state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](coe_cluster_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](coe_cluster_module.md#id5)

```yaml+jinja
- name: Create a new Kubernetes cluster
  openstack.cloud.coe_cluster:
    cloud: devstack
    cluster_template_id: k8s-ha
    keypair: mykey
    master_count: 3
    name: k8s
    node_count: 5
```

## [Return Values](coe_cluster_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cluster**  dictionary | Dictionary describing the cluster.  **Returned:** On success when *state* is `present`. |
| **api_address**  string | The endpoint URL of COE API exposed to end-users.  **Returned:** success  **Sample:** `"https://172.24.4.30:6443"` |
| **cluster_template_id**  string | The UUID of the cluster template.  **Returned:** success  **Sample:** `"7b1418c8-cea8-48fc-995d-52b66af9a9aa"` |
| **coe_version**  string | Version info of chosen COE in bay/cluster for helping client in picking the right version of client.  **Returned:** success  **Sample:** `"v1.11.1"` |
| **create_timeout**  integer | Timeout for creating the cluster in minutes. Default to 60 if not set.  **Returned:** success  **Sample:** `60` |
| **created_at**  string | The date and time in UTC at which the cluster is created.  **Returned:** success  **Sample:** `"2018-08-16T10:29:45+00:00"` |
| **discovery_url**  string | The custom discovery url for node discovery. This is used by the COE to discover the servers that have been created to host the containers. The actual discovery mechanism varies with the COE. In some cases, the service fills in the server info in the discovery service. In other cases, if the discovery_url is not specified, the service will use the public discovery service at <https://discovery.etcd.io>. In this case, the service will generate a unique url here for each bay and store the info for the servers.  **Returned:** success  **Sample:** `"https://discovery.etcd.io/a42ee38e7113f31f4d6324f24367aae5"` |
| **fixed_network**  string | The name or ID of the network to provide connectivity to the internal network for the bay/cluster.  **Returned:** success |
| **fixed_subnet**  string | The fixed subnet to use when allocating network addresses for nodes in bay/cluster.  **Returned:** success |
| **flavor_id**  string | The flavor name or ID to use when booting the node servers. Defaults to m1.small.  **Returned:** success |
| **id**  string | Unique UUID for this cluster.  **Returned:** success  **Sample:** `"86246a4d-a16c-4a58-9e96ad7719fe0f9d"` |
| **is_floating_ip_enabled**  boolean | Indicates whether created clusters should have a floating ip or not.  **Returned:** success  **Sample:** `true` |
| **is_master_lb_enabled**  boolean | Indicates whether created clusters should have a load balancer for master nodes or not.  **Returned:** success  **Sample:** `true` |
| **keypair**  string | Name of the keypair to use.  **Returned:** success  **Sample:** `"mykey"` |
| **labels**  dictionary | One or more key/value pairs.  **Returned:** success  **Sample:** `{"key1": "value1", "key2": "value2"}` |
| **master_addresses**  list / elements=string | A list of floating IPs of all master nodes.  **Returned:** success  **Sample:** `["172.24.4.5"]` |
| **master_count**  integer | The number of servers that will serve as master for the bay/cluster. Set to more than 1 master to enable High Availability. If the option master-lb-enabled is specified in the baymodel/cluster template, the master servers will be placed in a load balancer pool. Defaults to 1.  **Returned:** success  **Sample:** `1` |
| **master_flavor_id**  string | The flavor of the master node for this baymodel/cluster template.  **Returned:** success  **Sample:** `"c1.c1r1"` |
| **name**  string | Name that has to be given to the cluster.  **Returned:** success  **Sample:** `"k8scluster"` |
| **node_addresses**  list / elements=string | A list of floating IPs of all servers that serve as nodes.  **Returned:** success  **Sample:** `["172.24.4.8"]` |
| **node_count**  integer | The number of master nodes for this cluster.  **Returned:** success  **Sample:** `1` |
| **stack_id**  string | The reference UUID of orchestration stack from Heat orchestration service.  **Returned:** success  **Sample:** `"07767ec6-85f5-44cb-bd63-242a8e7f0d9d"` |
| **status**  string | Status of the cluster from the heat stack.  **Returned:** success  **Sample:** `"CREATE_COMLETE"` |
| **status_reason**  string | Status reason of the cluster from the heat stack  **Returned:** success  **Sample:** `"Stack CREATE completed successfully"` |
| **updated_at**  string | The date and time in UTC at which the cluster was updated.  **Returned:** success  **Sample:** `"2018-08-16T10:39:25+00:00"` |
| **uuid**  string | Unique UUID for this cluster.  **Returned:** success  **Sample:** `"86246a4d-a16c-4a58-9e96ad7719fe0f9d"` |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
