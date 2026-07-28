---
collection: ansible
version: "8"
title: "openstack.cloud.loadbalancer module – Manage Octavia load-balancer in an OpenStack cloud"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/loadbalancer_module.html
fetched_at: 2026-07-28T02:48:15+00:00
---
# openstack.cloud.loadbalancer module – Manage Octavia load-balancer in an OpenStack cloud

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
> see [Requirements](loadbalancer_module.md#ansible-collections-openstack-cloud-loadbalancer-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.loadbalancer`.

- [Synopsis](loadbalancer_module.md#synopsis)
- [Requirements](loadbalancer_module.md#requirements)
- [Parameters](loadbalancer_module.md#parameters)
- [Notes](loadbalancer_module.md#notes)
- [Examples](loadbalancer_module.md#examples)
- [Return Values](loadbalancer_module.md#return-values)

## [Synopsis](loadbalancer_module.md#id1)

- Add, update or remove Octavia load-balancer from OpenStack cloud.

## [Requirements](loadbalancer_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](loadbalancer_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **assign_floating_ip**  aliases: auto_public_ip  boolean | Allocate floating ip address and associate with the VIP automatically.  Deprecated, use [openstack.cloud.floating_ip](floating_ip_module.md#ansible-collections-openstack-cloud-floating-ip-module) instead.  **Choices:**   - `false` ← (default) - `true` |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **delete_floating_ip**  aliases: delete_public_ip  boolean | When *state* is `present` and *delete_floating_ip* is `true`, then any floating ip address associated with the VIP will be deleted.  When *state* is `absent` and *delete_floating_ip* is `true`, then any floating ip address associated with the VIP will be deleted along with the load balancer.  Deprecated, use [openstack.cloud.floating_ip](floating_ip_module.md#ansible-collections-openstack-cloud-floating-ip-module) instead.  **Choices:**   - `false` ← (default) - `true` |
| **description**  string | A human-readable description for the load-balancer. |
| **flavor**  string | The flavor of the load balancer.  This attribute cannot be updated. |
| **floating_ip_address**  aliases: public_ip_address  string | Floating ip address aka public ip address associated with the VIP.  Deprecated, use [openstack.cloud.floating_ip](floating_ip_module.md#ansible-collections-openstack-cloud-floating-ip-module) instead. |
| **floating_ip_network**  aliases: public_network  string | Name or ID of a Neutron external network where floating ip address will be created on.  Deprecated, use [openstack.cloud.floating_ip](floating_ip_module.md#ansible-collections-openstack-cloud-floating-ip-module) instead. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **name**  string / required | The name of the load balancer.  This attribute cannot be updated. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Should the resource be present or absent.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **vip_address**  string | IP address of the load balancer virtual IP.  This attribute cannot be updated. |
| **vip_network**  string | The name or id of the network for the virtual IP of the load balancer.  One of *vip_network*, *vip_subnet*, or *vip_port* must be specified for creation.  This attribute cannot be updated. |
| **vip_port**  string | The name or id of the load balancer virtual IP port. One of  One of *vip_network*, *vip_subnet*, or *vip_port* must be specified for creation.  This attribute cannot be updated. |
| **vip_subnet**  string | The name or id of the subnet for the virtual IP of the load balancer.  One of *vip_network*, *vip_subnet*, or *vip_port* must be specified for creation.  This attribute cannot be updated. |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](loadbalancer_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](loadbalancer_module.md#id5)

```yaml+jinja
- name: Create a load balancer
  openstack.cloud.loadbalancer:
    cloud: devstack
    name: my_lb
    state: present
    vip_subnet: my_subnet

- name: Create another load balancer
  openstack.cloud.loadbalancer:
    cloud: devstack
    name: my_lb
    state: present
    vip_address: 192.168.0.11
    vip_network: my_network

- name: Delete a load balancer and all its related resources
  openstack.cloud.loadbalancer:
    cloud: devstack
    name: my_lb
    state: absent

- name: Delete a load balancer, its related resources and its floating ip
  openstack.cloud.loadbalancer:
    cloud: devstack
    delete_floating_ip: true
    name: my_lb
    state: absent
```

## [Return Values](loadbalancer_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **floating_ip**  dictionary | Dictionary describing the floating ip address attached to the load-balancer.  **Returned:** On success when *state* is `present` and *assign_floating_ip* is `true`. |
| **created_at**  string | Timestamp at which the floating IP was assigned.  **Returned:** success |
| **description**  string | The description of a floating IP.  **Returned:** success |
| **dns_domain**  string | The DNS domain.  **Returned:** success |
| **dns_name**  string | The DNS name.  **Returned:** success |
| **fixed_ip_address**  string | The fixed IP address associated with a floating IP address.  **Returned:** success |
| **floating_ip_address**  string | The IP address of a floating IP.  **Returned:** success |
| **floating_network_id**  string | The id of the network associated with a floating IP.  **Returned:** success |
| **id**  string | Id of the floating ip.  **Returned:** success |
| **name**  string | Name of the floating ip.  **Returned:** success |
| **port_details**  dictionary | The details of the port that this floating IP associates with. Present if `fip-port-details` extension is loaded.  **Returned:** success |
| **port_id**  string | The port ID floating ip associated with.  **Returned:** success |
| **project_id**  string | The ID of the project this floating IP is associated with.  **Returned:** success |
| **qos_policy_id**  string | The ID of the QoS policy attached to the floating IP.  **Returned:** success |
| **revision_number**  string | Revision number.  **Returned:** success |
| **router_id**  string | The id of the router floating ip associated with.  **Returned:** success |
| **status**  string | The status of a floating IP, which can be ‘ACTIVE’ or ‘DOWN’.  **Returned:** success |
| **subnet_id**  string | The id of the subnet the floating ip associated with.  **Returned:** success |
| **tags**  list / elements=string | List of tags.  **Returned:** success |
| **updated_at**  string | Timestamp at which the floating IP was last updated.  **Returned:** success |
| **load_balancer**  dictionary | Dictionary describing the load-balancer.  **Returned:** On success when *state* is `present`. |
| **additional_vips**  string | Additional VIPs.  **Returned:** success |
| **availability_zone**  string | Name of the target Octavia availability zone.  **Returned:** success |
| **created_at**  string | Timestamp when the load balancer was created.  **Returned:** success |
| **description**  string | The load balancer description.  **Returned:** success |
| **flavor_id**  string | The load balancer flavor ID.  **Returned:** success |
| **id**  string | Unique UUID.  **Returned:** success |
| **is_admin_state_up**  boolean | The administrative state of the load balancer.  **Returned:** success |
| **listeners**  list / elements=string | The associated listener IDs, if any.  **Returned:** success |
| **name**  string | Name given to the load balancer.  **Returned:** success |
| **operating_status**  string | The operating status of the load balancer.  **Returned:** success |
| **pools**  list / elements=string | The associated pool IDs, if any.  **Returned:** success |
| **project_id**  string | The ID of the project this load balancer is associated with.  **Returned:** success |
| **provider**  string | Provider name for the load balancer.  **Returned:** success |
| **provisioning_status**  string | The provisioning status of the load balancer.  **Returned:** success |
| **tags**  string | A list of associated tags.  **Returned:** success |
| **updated_at**  string | Timestamp when the load balancer was last updated.  **Returned:** success |
| **vip_address**  string | The load balancer virtual IP address.  **Returned:** success |
| **vip_network_id**  string | Network ID the load balancer virtual IP port belongs in.  **Returned:** success |
| **vip_port_id**  string | The load balancer virtual IP port ID.  **Returned:** success |
| **vip_qos_policy_id**  string | VIP qos policy id.  **Returned:** success |
| **vip_subnet_id**  string | Subnet ID the load balancer virtual IP port belongs in.  **Returned:** success |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
