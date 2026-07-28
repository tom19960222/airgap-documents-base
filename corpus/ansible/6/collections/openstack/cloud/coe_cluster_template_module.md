---
collection: ansible
version: "6"
title: "openstack.cloud.coe_cluster_template module – Add/Remove COE cluster template from OpenStack Cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/coe_cluster_template_module.html
fetched_at: 2026-07-28T00:16:27+00:00
---
# openstack.cloud.coe_cluster_template module – Add/Remove COE cluster template from OpenStack Cloud

> **Note:**
>
> This module is part of the [openstack.cloud collection](https://galaxy.ansible.com/openstack/cloud) (version 1.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install openstack.cloud`.
> You need further requirements to be able to use this module,
> see [Requirements](coe_cluster_template_module.md#ansible-collections-openstack-cloud-coe-cluster-template-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.coe_cluster_template`.

- [Synopsis](coe_cluster_template_module.md#synopsis)
- [Requirements](coe_cluster_template_module.md#requirements)
- [Parameters](coe_cluster_template_module.md#parameters)
- [Notes](coe_cluster_template_module.md#notes)
- [Examples](coe_cluster_template_module.md#examples)
- [Return Values](coe_cluster_template_module.md#return-values)

## [Synopsis](coe_cluster_template_module.md#id1)

- Add or Remove COE cluster template from the OpenStack Container Infra service.

## [Requirements](coe_cluster_template_module.md#id2)

The below requirements are needed on the host that executes this module.

- openstacksdk
- openstacksdk >= 0.36, < 0.99.0
- python >= 3.6

## [Parameters](coe_cluster_template_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **availability_zone**  string | Ignored. Present for backwards compatibility |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **coe**  string / required | The Container Orchestration Engine for this clustertemplate  Choices:   - `"kubernetes"` - `"swarm"` - `"mesos"` |
| **dns_nameserver**  string | The DNS nameserver address  Default: `"8.8.8.8"` |
| **docker_storage_driver**  string | Docker storage driver  Choices:   - `"devicemapper"` - `"overlay"` - `"overlay2"` |
| **docker_volume_size**  integer | The size in GB of the docker volume |
| **external_network_id**  string | The external network to attach to the Cluster |
| **fixed_network**  string | The fixed network name to attach to the Cluster |
| **fixed_subnet**  string | The fixed subnet name to attach to the Cluster |
| **flavor_id**  string | The flavor of the minion node for this ClusterTemplate |
| **floating_ip_enabled**  boolean | Indicates whether created clusters should have a floating ip or not  Choices:   - `false` - `true` ← (default) |
| **http_proxy**  string | Address of a proxy that will receive all HTTP requests and relay them The format is a URL including a port number |
| **https_proxy**  string | Address of a proxy that will receive all HTTPS requests and relay them. The format is a URL including a port number |
| **image_id**  string / required | Image id the cluster will be based on |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  Choices:   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **keypair_id**  string | Name or ID of the keypair to use. |
| **labels**  any | One or more key/value pairs |
| **master_flavor_id**  string | The flavor of the master node for this ClusterTemplate |
| **master_lb_enabled**  boolean | Indicates whether created clusters should have a load balancer for master nodes or not  Choices:   - `false` ← (default) - `true` |
| **name**  string / required | Name that has to be given to the cluster template |
| **network_driver**  string | The name of the driver used for instantiating container networks  Choices:   - `"flannel"` - `"calico"` - `"docker"` |
| **no_proxy**  string | A comma separated list of IPs for which proxies should not be used in the cluster |
| **public**  boolean | Indicates whether the ClusterTemplate is public or not  Choices:   - `false` ← (default) - `true` |
| **region_name**  string | Name of the region. |
| **registry_enabled**  boolean | Indicates whether the docker registry is enabled  Choices:   - `false` ← (default) - `true` |
| **sdk_log_level**  string | Log level of the OpenStackSDK  Choices:   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **server_type**  string | Server type for this ClusterTemplate  Choices:   - `"vm"` ← (default) - `"bm"` |
| **state**  string | Indicate desired state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  Default: `180` |
| **tls_disabled**  boolean | Indicates whether the TLS should be disabled  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `yes`.  Choices:   - `false` - `true` |
| **volume_driver**  string | The name of the driver used for instantiating container volumes  Choices:   - `"cinder"` - `"rexray"` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  Choices:   - `false` - `true` ← (default) |

## [Notes](coe_cluster_template_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](coe_cluster_template_module.md#id5)

```yaml+jinja
# Create a new Kubernetes cluster template
- openstack.cloud.coe_cluster_template:
    name: k8s
    coe: kubernetes
    keypair_id: mykey
    image_id: 2a8c9888-9054-4b06-a1ca-2bb61f9adb72
    public: no
```

## [Return Values](coe_cluster_template_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cluster_template**  complex | Dictionary describing the template.  Returned: On success when *state* is ‘present’ |
| **coe**  string | The Container Orchestration Engine for this clustertemplate  Returned: success  Sample: `"kubernetes"` |
| **dns_nameserver**  string | The DNS nameserver address  Returned: success  Sample: `"8.8.8.8"` |
| **docker_storage_driver**  string | Docker storage driver  Returned: success  Sample: `"devicemapper"` |
| **docker_volume_size**  integer | The size in GB of the docker volume  Returned: success  Sample: `5` |
| **external_network_id**  string | The external network to attach to the Cluster  Returned: success  Sample: `"public"` |
| **fixed_network**  string | The fixed network name to attach to the Cluster  Returned: success  Sample: `"07767ec6-85f5-44cb-bd63-242a8e7f0d9d"` |
| **fixed_subnet**  string | The fixed subnet name to attach to the Cluster  Returned: success  Sample: `"05567ec6-85f5-44cb-bd63-242a8e7f0d9d"` |
| **flavor_id**  string | The flavor of the minion node for this ClusterTemplate  Returned: success  Sample: `"c1.c1r1"` |
| **floating_ip_enabled**  boolean | Indicates whether created clusters should have a floating ip or not  Returned: success  Sample: `true` |
| **http_proxy**  string | Address of a proxy that will receive all HTTP requests and relay them The format is a URL including a port number  Returned: success  Sample: `"http://10.0.0.11:9090"` |
| **https_proxy**  string | Address of a proxy that will receive all HTTPS requests and relay them. The format is a URL including a port number  Returned: success  Sample: `"https://10.0.0.10:8443"` |
| **image_id**  string | Image id the cluster will be based on  Returned: success  Sample: `"05567ec6-85f5-44cb-bd63-242a8e7f0e9d"` |
| **keypair_id**  string | Name or ID of the keypair to use.  Returned: success  Sample: `"mykey"` |
| **labels**  dictionary | One or more key/value pairs  Returned: success  Sample: `{"key1": "value1", "key2": "value2"}` |
| **master_flavor_id**  string | The flavor of the master node for this ClusterTemplate  Returned: success  Sample: `"c1.c1r1"` |
| **master_lb_enabled**  boolean | Indicates whether created clusters should have a load balancer for master nodes or not  Returned: success  Sample: `true` |
| **name**  string | Name that has to be given to the cluster template  Returned: success  Sample: `"k8scluster"` |
| **network_driver**  string | The name of the driver used for instantiating container networks  Returned: success  Sample: `"calico"` |
| **no_proxy**  string | A comma separated list of IPs for which proxies should not be used in the cluster  Returned: success  Sample: `"10.0.0.4,10.0.0.5"` |
| **public**  boolean | Indicates whether the ClusterTemplate is public or not  Returned: success  Sample: `false` |
| **registry_enabled**  boolean | Indicates whether the docker registry is enabled  Returned: success  Sample: `false` |
| **server_type**  string | Server type for this ClusterTemplate  Returned: success  Sample: `"vm"` |
| **tls_disabled**  boolean | Indicates whether the TLS should be disabled  Returned: success  Sample: `false` |
| **volume_driver**  string | The name of the driver used for instantiating container volumes  Returned: success  Sample: `"cinder"` |
| **id**  string | The cluster UUID.  Returned: On success when *state* is ‘present’  Sample: `"39007a7e-ee4f-4d13-8283-b4da2e037c69"` |

### Authors

- OpenStack Ansible SIG

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
