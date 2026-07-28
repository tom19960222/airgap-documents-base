---
collection: ansible
version: "8"
title: "openstack.cloud.coe_cluster_template module – Manage COE cluster template in OpenStack Cloud"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/coe_cluster_template_module.html
fetched_at: 2026-07-28T02:47:32+00:00
---
# openstack.cloud.coe_cluster_template module – Manage COE cluster template in OpenStack Cloud

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

- Add or remove a COE (Container Orchestration Engine) cluster template via OpenStack’s Magnum aka Container Infrastructure Management API.

## [Requirements](coe_cluster_template_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](coe_cluster_template_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **coe**  string | The Container Orchestration Engine for this cluster template  Required if *state* is `present`.  **Choices:**   - `"kubernetes"` - `"swarm"` - `"mesos"` |
| **dns_nameserver**  string | The DNS nameserver address.  Magnum’s default value for *dns_nameserver* is `8.8.8.8`. |
| **docker_storage_driver**  string | Docker storage driver.  **Choices:**   - `"devicemapper"` - `"overlay"` - `"overlay2"` |
| **docker_volume_size**  integer | The size in GB of the docker volume. |
| **external_network_id**  string | The external network to attach to the cluster.  When *is_floating_ip_enabled* is set to `true`, then *external_network_id* must be defined. |
| **fixed_network**  string | The fixed network name or id to attach to the cluster. |
| **fixed_subnet**  string | The fixed subnet name or id to attach to the cluster. |
| **flavor_id**  string | The flavor of the minion node for this cluster template. |
| **http_proxy**  string | Address of a proxy that will receive all HTTP requests and relay them.  The format is a URL including a port number. |
| **https_proxy**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a URL including a port number. |
| **image_id**  string | Image id the cluster will be based on.  Required if *state* is `present`. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **is_floating_ip_enabled**  aliases: floating_ip_enabled  boolean | Indicates whether created clusters should have a floating ip or not.  When *is_floating_ip_enabled* is set to `true`, then *external_network_id* must be defined.  **Choices:**   - `false` - `true` ← (default) |
| **is_master_lb_enabled**  aliases: master_lb_enabled  boolean | Indicates whether created clusters should have a load balancer for master nodes or not.  Magnum’s default value for *is_master_lb_enabled* is `true`, ours is `false`.  **Choices:**   - `false` ← (default) - `true` |
| **is_public**  aliases: public  boolean | Indicates whether the cluster template is public or not.  Magnum’s default value for *is_public* is `false`.  **Choices:**   - `false` - `true` |
| **is_registry_enabled**  aliases: registry_enabled  boolean | Indicates whether the docker registry is enabled.  Magnum’s default value for *is_registry_enabled* is `false`.  **Choices:**   - `false` - `true` |
| **is_tls_disabled**  aliases: tls_disabled  boolean | Indicates whether the TLS should be disabled.  Magnum’s default value for *is_tls_disabled* is `false`.  **Choices:**   - `false` - `true` |
| **keypair_id**  string | Name or ID of the keypair to use. |
| **labels**  any | One or more key/value pairs. |
| **master_flavor_id**  string | The flavor of the master node for this cluster template. |
| **name**  string / required | Name that has to be given to the cluster template. |
| **network_driver**  string | The name of the driver used for instantiating container networks.  **Choices:**   - `"flannel"` - `"calico"` - `"docker"` |
| **no_proxy**  string | A comma separated list of IPs for which proxies should not be used in the cluster. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **server_type**  string | Server type for this cluster template.  Magnum’s default value for *server_type* is `vm`.  **Choices:**   - `"vm"` - `"bm"` |
| **state**  string | Indicate desired state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **volume_driver**  string | The name of the driver used for instantiating container volumes.  **Choices:**   - `"cinder"` - `"rexray"` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](coe_cluster_template_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](coe_cluster_template_module.md#id5)

```yaml+jinja
- name: Create a new Kubernetes cluster template
  openstack.cloud.coe_cluster_template:
    cloud: devstack
    coe: kubernetes
    image_id: 2a8c9888-9054-4b06-a1ca-2bb61f9adb72
    keypair_id: mykey
    name: k8s
    is_public: false
```

## [Return Values](coe_cluster_template_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cluster_template**  dictionary | Dictionary describing the template.  **Returned:** On success when *state* is `present`. |
| **apiserver_port**  integer | The exposed port of COE API server.  **Returned:** success |
| **cluster_distro**  string | Display the attribute os_distro defined as appropriate metadata in image for the bay/cluster driver.  **Returned:** success |
| **coe**  string | The Container Orchestration Engine for this cluster template. Supported COEs include kubernetes, swarm, mesos.  **Returned:** success  **Sample:** `"kubernetes"` |
| **created_at**  string | The date and time when the resource was created.  **Returned:** success |
| **dns_nameserver**  string | The DNS nameserver for the servers and containers in the bay/cluster to use.  **Returned:** success  **Sample:** `"8.8.8.8"` |
| **docker_storage_driver**  string | The name of a driver to manage the storage for the images and the container’s writable layer.  **Returned:** success |
| **docker_volume_size**  integer | The size in GB for the local storage on each server for the Docker daemon to cache the images and host the containers.  **Returned:** success  **Sample:** `5` |
| **external_network_id**  string | The name or network ID of a Neutron network to provide connectivity to the external internet for the bay/cluster.  **Returned:** success  **Sample:** `"public"` |
| **fixed_network**  string | The fixed network name to attach to the cluster.  **Returned:** success  **Sample:** `"07767ec6-85f5-44cb-bd63-242a8e7f0d9d"` |
| **fixed_subnet**  string | The fixed subnet name to attach to the cluster.  **Returned:** success  **Sample:** `"05567ec6-85f5-44cb-bd63-242a8e7f0d9d"` |
| **flavor_id**  string | The nova flavor ID or name for booting the node servers.  **Returned:** success  **Sample:** `"c1.c1r1"` |
| **http_proxy**  string | Address of a proxy that will receive all HTTP requests and relay them. The format is a URL including a port number.  **Returned:** success  **Sample:** `"http://10.0.0.11:9090"` |
| **https_proxy**  string | Address of a proxy that will receive all HTTPS requests and relay them. The format is a URL including a port number.  **Returned:** success  **Sample:** `"https://10.0.0.10:8443"` |
| **id**  string | The UUID of the cluster template.  **Returned:** success |
| **image_id**  string | The name or UUID of the base image in Glance to boot the servers for the bay/cluster.  **Returned:** success  **Sample:** `"05567ec6-85f5-44cb-bd63-242a8e7f0e9d"` |
| **insecure_registry**  string | The URL pointing to users’s own private insecure docker registry to deploy and run docker containers.  **Returned:** success |
| **is_floating_ip_enabled**  boolean | Indicates whether created clusters should have a floating ip or not.  **Returned:** success  **Sample:** `true` |
| **is_hidden**  boolean | Indicates whether the cluster template is hidden or not.  **Returned:** success  **Sample:** `false` |
| **is_master_lb_enabled**  boolean | Indicates whether created clusters should have a load balancer for master nodes or not.  **Returned:** success  **Sample:** `true` |
| **is_public**  boolean | Access to a baymodel/cluster template is normally limited to the admin, owner or users within the same tenant as the owners. Setting this flag makes the baymodel/cluster template public and accessible by other users. The default is not public.  **Returned:** success  **Sample:** `false` |
| **is_registry_enabled**  boolean | Docker images by default are pulled from the public Docker registry, but in some cases, users may want to use a private registry. This option provides an alternative registry based on the Registry V2: Magnum will create a local registry in the bay/cluster backed by swift to host the images. The default is to use the public registry.  **Returned:** success  **Sample:** `false` |
| **is_tls_disabled**  boolean | Transport Layer Security (TLS) is normally enabled to secure the bay/cluster. In some cases, users may want to disable TLS in the bay/cluster, for instance during development or to troubleshoot certain problems. Specifying this parameter will disable TLS so that users can access the COE endpoints without a certificate. The default is TLS enabled.  **Returned:** success  **Sample:** `false` |
| **keypair_id**  string | Name of the SSH keypair to configure in the bay/cluster servers for ssh access.  **Returned:** success  **Sample:** `"mykey"` |
| **labels**  dictionary | One or more key/value pairs.  **Returned:** success  **Sample:** `{"key1": "value1", "key2": "value2"}` |
| **master_flavor_id**  string | The flavor of the master node for this cluster template.  **Returned:** success  **Sample:** `"c1.c1r1"` |
| **name**  string | Name that has to be given to the cluster template.  **Returned:** success  **Sample:** `"k8scluster"` |
| **network_driver**  string | The name of a network driver for providing the networks for the containers  **Returned:** success  **Sample:** `"calico"` |
| **no_proxy**  string | A comma separated list of IPs for which proxies should not be used in the cluster.  **Returned:** success  **Sample:** `"10.0.0.4,10.0.0.5"` |
| **server_type**  string | The servers in the bay/cluster can be vm or baremetal.  **Returned:** success  **Sample:** `"vm"` |
| **updated_at**  string | The date and time when the resource was updated.  **Returned:** success |
| **uuid**  string | The UUID of the cluster template.  **Returned:** success |
| **volume_driver**  string | The name of a volume driver for managing the persistent storage for the containers.  **Returned:** success  **Sample:** `"cinder"` |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
