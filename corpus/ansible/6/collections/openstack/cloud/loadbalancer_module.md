---
collection: ansible
version: "6"
title: "openstack.cloud.loadbalancer module – Add/Delete load balancer from OpenStack Cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/loadbalancer_module.html
fetched_at: 2026-07-28T00:16:51+00:00
---
# openstack.cloud.loadbalancer module – Add/Delete load balancer from OpenStack Cloud

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

- Add or Remove load balancer from the OpenStack load-balancer service(Octavia). Load balancer update is not supported for now.

## [Requirements](loadbalancer_module.md#id2)

The below requirements are needed on the host that executes this module.

- openstacksdk
- openstacksdk >= 0.36, < 0.99.0
- python >= 3.6

## [Parameters](loadbalancer_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **auto_public_ip**  boolean | Allocate a public IP address and associate with the VIP automatically.  Choices:   - `false` ← (default) - `true` |
| **availability_zone**  string | Ignored. Present for backwards compatibility |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **delete_public_ip**  boolean | When `state=absent` and this option is true, any public IP address associated with the VIP will be deleted along with the load balancer.  Choices:   - `false` ← (default) - `true` |
| **flavor**  string | The flavor of the load balancer. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  Choices:   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **listeners**  list / elements=dictionary | A list of listeners that attached to the load balancer. |
| **allowed_cidrs**  string | A list of IPv4, IPv6 or mix of both CIDRs to be allowed access to the listener. The default is all allowed. When a list of CIDRs is provided, the default switches to deny all. Ignored on unsupported Octavia versions (less than 2.12)  Default: `[]` |
| **name**  string | The listener name or ID. |
| **pool**  string | The pool attached to the listener. |
| **lb_algorithm**  string | The load balancing algorithm for the pool.  Default: `"ROUND_ROBIN"` |
| **members**  string | A list of members that added to the pool. |
| **address**  string | The IP address of the member. |
| **name**  string | The member name or ID. |
| **protocol_port**  string | The protocol port number for the member.  Default: `80` |
| **subnet**  string | The name or ID of the subnet the member service is accessible from. |
| **name**  string | The pool name or ID. |
| **protocol**  string | The protocol for the pool.  Default: `"HTTP"` |
| **protocol**  string | The protocol for the listener.  Default: `"HTTP"` |
| **protocol_port**  string | The protocol port number for the listener.  Default: `80` |
| **name**  string / required | The name of the load balancer. |
| **public_ip_address**  string | Public IP address associated with the VIP. |
| **public_network**  string | The name or ID of a Neutron external network. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  Choices:   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Should the resource be present or absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | The amount of time the module should wait.  Default: `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `yes`.  Choices:   - `false` - `true` |
| **vip_address**  string | IP address of the load balancer virtual IP. |
| **vip_network**  string | The name or id of the network for the virtual IP of the load balancer. One of *vip_network*, *vip_subnet*, or *vip_port* must be specified for creation. |
| **vip_port**  string | The name or id of the load balancer virtual IP port. One of *vip_network*, *vip_subnet*, or *vip_port* must be specified for creation. |
| **vip_subnet**  string | The name or id of the subnet for the virtual IP of the load balancer. One of *vip_network*, *vip_subnet*, or *vip_port* must be specified for creation. |
| **wait**  boolean | If the module should wait for the load balancer to be created or deleted.  Choices:   - `false` - `true` ← (default) |

## [Notes](loadbalancer_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](loadbalancer_module.md#id5)

```yaml+jinja
# Create a load balancer by specifying the VIP subnet.
- openstack.cloud.loadbalancer:
    auth:
      auth_url: https://identity.example.com
      username: admin
      password: passme
      project_name: admin
    state: present
    name: my_lb
    vip_subnet: my_subnet
    timeout: 150

# Create a load balancer by specifying the VIP network and the IP address.
- openstack.cloud.loadbalancer:
    auth:
      auth_url: https://identity.example.com
      username: admin
      password: passme
      project_name: admin
    state: present
    name: my_lb
    vip_network: my_network
    vip_address: 192.168.0.11

# Create a load balancer together with its sub-resources in the 'all in one'
# way. A public IP address is also allocated to the load balancer VIP.
- openstack.cloud.loadbalancer:
    auth:
      auth_url: https://identity.example.com
      username: admin
      password: passme
      project_name: admin
    name: lingxian_test
    state: present
    vip_subnet: kong_subnet
    auto_public_ip: yes
    public_network: public
    listeners:
      - name: lingxian_80
        protocol: TCP
        protocol_port: 80
        pool:
          name: lingxian_80_pool
          protocol: TCP
          members:
            - name: mywebserver1
              address: 192.168.2.81
              protocol_port: 80
              subnet: webserver_subnet
      - name: lingxian_8080
        protocol: TCP
        protocol_port: 8080
        pool:
          name: lingxian_8080-pool
          protocol: TCP
          members:
            - name: mywebserver2
              address: 192.168.2.82
              protocol_port: 8080
    wait: yes
    timeout: 600

# Delete a load balancer(and all its related resources)
- openstack.cloud.loadbalancer:
    auth:
      auth_url: https://identity.example.com
      username: admin
      password: passme
      project_name: admin
    state: absent
    name: my_lb

# Delete a load balancer(and all its related resources) together with the
# public IP address(if any) attached to it.
- openstack.cloud.loadbalancer:
    auth:
      auth_url: https://identity.example.com
      username: admin
      password: passme
      project_name: admin
    state: absent
    name: my_lb
    delete_public_ip: yes
```

## [Return Values](loadbalancer_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | The load balancer UUID.  Returned: On success when `state=present`  Sample: `"39007a7e-ee4f-4d13-8283-b4da2e037c69"` |
| **loadbalancer**  complex | Dictionary describing the load balancer.  Returned: On success when `state=present` |
| **id**  string | Unique UUID.  Returned: success  Sample: `"39007a7e-ee4f-4d13-8283-b4da2e037c69"` |
| **is_admin_state_up**  boolean | The administrative state of the load balancer.  Returned: success  Sample: `true` |
| **listeners**  list / elements=string | The associated listener IDs, if any.  Returned: success  Sample: `[{"id": "7aa1b380-beec-459c-a8a7-3a4fb6d30645"}, {"id": "692d06b8-c4f8-4bdb-b2a3-5a263cc23ba6"}]` |
| **name**  string | Name given to the load balancer.  Returned: success  Sample: `"lingxian_test"` |
| **operating_status**  string | The operating status of the load balancer.  Returned: success  Sample: `"ONLINE"` |
| **pools**  list / elements=string | The associated pool IDs, if any.  Returned: success  Sample: `[{"id": "27b78d92-cee1-4646-b831-e3b90a7fa714"}, {"id": "befc1fb5-1992-4697-bdb9-eee330989344"}]` |
| **provisioning_status**  string | The provisioning status of the load balancer.  Returned: success  Sample: `"ACTIVE"` |
| **public_vip_address**  string | The load balancer public VIP address.  Returned: success  Sample: `"10.17.8.254"` |
| **vip_address**  string | The load balancer virtual IP address.  Returned: success  Sample: `"192.168.2.88"` |
| **vip_network_id**  string | Network ID the load balancer virtual IP port belongs in.  Returned: success  Sample: `"f171db43-56fd-41cf-82d7-4e91d741762e"` |
| **vip_port_id**  string | The load balancer virtual IP port ID.  Returned: success  Sample: `"2061395c-1c01-47ab-b925-c91b93df9c1d"` |
| **vip_subnet_id**  string | Subnet ID the load balancer virtual IP port belongs in.  Returned: success  Sample: `"c53e3c70-9d62-409a-9f71-db148e7aa853"` |

### Authors

- OpenStack Ansible SIG

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
