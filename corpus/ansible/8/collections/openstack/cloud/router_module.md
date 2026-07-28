---
collection: ansible
version: "8"
title: "openstack.cloud.router module – Create or delete routers from OpenStack"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/router_module.html
fetched_at: 2026-07-28T02:48:37+00:00
---
# openstack.cloud.router module – Create or delete routers from OpenStack

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
> see [Requirements](router_module.md#ansible-collections-openstack-cloud-router-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.router`.

- [Synopsis](router_module.md#synopsis)
- [Requirements](router_module.md#requirements)
- [Parameters](router_module.md#parameters)
- [Notes](router_module.md#notes)
- [Examples](router_module.md#examples)
- [Return Values](router_module.md#return-values)

## [Synopsis](router_module.md#id1)

- Create or Delete routers from OpenStack. Although Neutron allows routers to share the same name, this module enforces name uniqueness to be more user friendly.

## [Requirements](router_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](router_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **enable_snat**  boolean | Enable Source NAT (SNAT) attribute.  **Choices:**   - `false` - `true` |
| **external_fixed_ips**  list / elements=dictionary | The IP address parameters for the external gateway network. Each is a dictionary with the subnet name or ID (subnet) and the IP address to assign on the subnet (ip_address). If no IP is specified, one is automatically assigned from that subnet. |
| **ip_address**  aliases: ip  string | The fixed IP address to attempt to allocate. |
| **subnet_id**  aliases: subnet  string / required | The subnet to attach the IP address to. |
| **external_gateway_info**  dictionary | Information about the router’s external gateway |
| **enable_snat**  boolean | Unique name or ID of the external gateway network.  required *interfaces* or *enable_snat* are provided.  **Choices:**   - `false` - `true` |
| **external_fixed_ips**  list / elements=dictionary | The IP address parameters for the external gateway network. Each is a dictionary with the subnet name or ID (subnet) and the IP address to assign on the subnet (ip_address). If no IP is specified, one is automatically assigned from that subnet. |
| **ip_address**  aliases: ip  string | The fixed IP address to attempt to allocate. |
| **subnet_id**  aliases: subnet  string / required | The subnet to attach the IP address to. |
| **network**  string | Unique name or ID of the external gateway network.  required *interfaces* or *enable_snat* are provided. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **interfaces**  list / elements=any | List of subnets to attach to the router internal interface. Default gateway associated with the subnet will be automatically attached with the router’s internal interface. In order to provide an ip address different from the default gateway,parameters are passed as dictionary with keys as network name or ID (*net*), subnet name or ID (*subnet*) and the IP of port (*portip*) from the network. User defined portip is often required when a multiple router need to be connected to a single subnet for which the default gateway has been already used. |
| **is_admin_state_up**  aliases: admin_state_up  boolean | Desired admin state of the created or existing router.  **Choices:**   - `false` - `true` ← (default) |
| **name**  string / required | Name to be give to the router.  This router attribute cannot be updated. |
| **network**  string | Unique name or ID of the external gateway network.  Required if *external_fixed_ips* or *enable_snat* are provided.  This router attribute cannot be updated. |
| **project**  string | Unique name or ID of the project.  This router attribute cannot be updated. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Indicate desired state of the resource  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](router_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](router_module.md#id5)

```yaml+jinja
# Create a simple router, not attached to a gateway or subnets.
- openstack.cloud.router:
    cloud: mycloud
    state: present
    name: simple_router

# Create a router, not attached to a gateway or subnets for a given project.
- openstack.cloud.router:
    cloud: mycloud
    state: present
    name: simple_router
    project: myproj

# Creates a router attached to ext_network1 on an IPv4 subnet and with one
# internal subnet interface.
- openstack.cloud.router:
    cloud: mycloud
    state: present
    name: router1
    network: ext_network1
    external_fixed_ips:
      - subnet: public-subnet
        ip_address: 172.24.4.2
    interfaces:
      - private-subnet

# Create a router with two internal subnet interfaces and a user defined port
# ip and another with default gateway.
- openstack.cloud.router:
    cloud: mycloud
    state: present
    name: router2
    network: ext_network1
    interfaces:
      - net: private-net
        subnet: private-subnet
        portip: 10.1.1.10
      - project-subnet

# Create a router with two internal subnet interface. One with user defined
# port ip and and another with default gateway.
- openstack.cloud.router:
    cloud: mycloud
    state: present
    name: router2
    network: ext_network1
    interfaces:
      - net: private-net
        subnet: private-subnet
        portip: 10.1.1.10
      - project-subnet

# Create a router with two internal subnet interface. One with user defined
# port ip and and another  with default gateway.
- openstack.cloud.router:
    cloud: mycloud
    state: present
    name: router2
    network: ext_network1
    interfaces:
      - net: private-net
        subnet: private-subnet
        portip: 10.1.1.10
      - project-subnet

# Update existing router1 external gateway to include the IPv6 subnet.
# Note that since 'interfaces' is not provided, any existing internal
# interfaces on an existing router will be left intact.
- openstack.cloud.router:
    cloud: mycloud
    state: present
    name: router1
    network: ext_network1
    external_fixed_ips:
      - subnet: public-subnet
        ip_address: 172.24.4.2
      - subnet: ipv6-public-subnet
        ip_address: 2001:db8::3

# Delete router1
- openstack.cloud.router:
    cloud: mycloud
    state: absent
    name: router1
```

## [Return Values](router_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **router**  dictionary | Dictionary describing the router.  **Returned:** On success when *state* is ‘present’ |
| **availability_zone_hints**  list / elements=string | Availability zone hints  **Returned:** success |
| **availability_zones**  list / elements=string | Availability zones  **Returned:** success |
| **created_at**  string | Date and time when the router was created  **Returned:** success |
| **description**  string | Description notes of the router  **Returned:** success |
| **external_gateway_info**  dictionary | The external gateway information of the router.  **Returned:** success  **Sample:** `{"enable_snat": true, "external_fixed_ips": [{"ip_address": "10.6.6.99", "subnet_id": "4272cb52-a456-4c20-8f3c-c26024ecfa81"}]}` |
| **flavor_id**  string | ID of the flavor of the router  **Returned:** success |
| **id**  string | Unique UUID.  **Returned:** success  **Sample:** `"474acfe5-be34-494c-b339-50f06aa143e4"` |
| **is_admin_state_up**  boolean | Network administrative state  **Returned:** success |
| **is_distributed**  boolean | Indicates a distributed router.  **Returned:** success |
| **is_ha**  boolean | Indicates a highly-available router.  **Returned:** success |
| **name**  string | Name given to the router.  **Returned:** success  **Sample:** `"router1"` |
| **project_id**  string | Project id associated with this router.  **Returned:** success |
| **revision_number**  integer | Revision number  **Returned:** success |
| **routes**  list / elements=string | The extra routes configuration for L3 router.  **Returned:** success |
| **status**  string | Router status.  **Returned:** success  **Sample:** `"ACTIVE"` |
| **tags**  list / elements=string | List of tags  **Returned:** success |
| **tenant_id**  string | Owner tenant ID  **Returned:** success |
| **updated_at**  string | Date of last update on the router  **Returned:** success |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
