---
collection: ansible
version: "8"
title: "openstack.cloud.subnet module – Add/Remove subnet to an OpenStack network"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/subnet_module.html
fetched_at: 2026-07-28T02:48:58+00:00
---
# openstack.cloud.subnet module – Add/Remove subnet to an OpenStack network

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
> see [Requirements](subnet_module.md#ansible-collections-openstack-cloud-subnet-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.subnet`.

- [Synopsis](subnet_module.md#synopsis)
- [Requirements](subnet_module.md#requirements)
- [Parameters](subnet_module.md#parameters)
- [Notes](subnet_module.md#notes)
- [Examples](subnet_module.md#examples)
- [Return Values](subnet_module.md#return-values)

## [Synopsis](subnet_module.md#id1)

- Add or Remove a subnet to an OpenStack network

## [Requirements](subnet_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](subnet_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allocation_pool_end**  string | From the subnet pool the last IP that should be assigned to the virtual machines. |
| **allocation_pool_start**  string | From the subnet pool the starting address from which the IP should be allocated. |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **cidr**  string | The CIDR representation of the subnet that should be assigned to the subnet. Required when *state* is ‘present’ and a subnetpool is not specified. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **description**  string | Description of the subnet |
| **disable_gateway_ip**  aliases: no_gateway_ip  boolean | The gateway IP would not be assigned for this subnet  **Choices:**   - `false` ← (default) - `true` |
| **dns_nameservers**  list / elements=string | List of DNS nameservers for this subnet. |
| **extra_attrs**  aliases: extra_specs  dictionary | Dictionary with extra key/value pairs passed to the API  **Default:** `{}` |
| **gateway_ip**  string | The ip that would be assigned to the gateway for this subnet |
| **host_routes**  list / elements=dictionary | A list of host route dictionaries for the subnet. |
| **destination**  string / required | The destination network (CIDR). |
| **nexthop**  string / required | The next hop (aka gateway) for the *destination*. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **ip_version**  integer | The IP version of the subnet 4 or 6  **Choices:**   - `4` ← (default) - `6` |
| **ipv6_address_mode**  string | IPv6 address mode  **Choices:**   - `"dhcpv6-stateful"` - `"dhcpv6-stateless"` - `"slaac"` |
| **ipv6_ra_mode**  string | IPv6 router advertisement mode  **Choices:**   - `"dhcpv6-stateful"` - `"dhcpv6-stateless"` - `"slaac"` |
| **is_dhcp_enabled**  aliases: enable_dhcp  boolean | Whether DHCP should be enabled for this subnet.  **Choices:**   - `false` - `true` ← (default) |
| **name**  string / required | The name of the subnet that should be created. Although Neutron allows for non-unique subnet names, this module enforces subnet name uniqueness. |
| **network**  aliases: network_name  string | Name or id of the network to which the subnet should be attached  Required when *state* is ‘present’ |
| **prefix_length**  string | The prefix length to use for subnet allocation from a subnet pool |
| **project**  string | Project name or ID containing the subnet (name admin-only) |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Indicate desired state of the resource  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **subnet_pool**  string | The subnet pool name or ID from which to obtain a CIDR |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **use_default_subnet_pool**  aliases: use_default_subnetpool  boolean | Use the default subnetpool for *ip_version* to obtain a CIDR.  **Choices:**   - `false` - `true` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](subnet_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](subnet_module.md#id5)

```yaml+jinja
# Create a new (or update an existing) subnet on the specified network
- openstack.cloud.subnet:
    state: present
    network_name: network1
    name: net1subnet
    cidr: 192.168.0.0/24
    dns_nameservers:
       - 8.8.8.7
       - 8.8.8.8
    host_routes:
       - destination: 0.0.0.0/0
         nexthop: 12.34.56.78
       - destination: 192.168.0.0/24
         nexthop: 192.168.0.1

# Delete a subnet
- openstack.cloud.subnet:
    state: absent
    name: net1subnet

# Create an ipv6 stateless subnet
- openstack.cloud.subnet:
    state: present
    name: intv6
    network_name: internal
    ip_version: 6
    cidr: 2db8:1::/64
    dns_nameservers:
        - 2001:4860:4860::8888
        - 2001:4860:4860::8844
    ipv6_ra_mode: dhcpv6-stateless
    ipv6_address_mode: dhcpv6-stateless
```

## [Return Values](subnet_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | Id of subnet  **Returned:** On success when subnet exists. |
| **subnet**  dictionary | Dictionary describing the subnet.  **Returned:** On success when subnet exists. |
| **allocation_pools**  list / elements=dictionary | Allocation pools associated with this subnet.  **Returned:** success |
| **cidr**  string | Subnet’s CIDR.  **Returned:** success |
| **created_at**  string | Created at timestamp  **Returned:** success |
| **description**  string | Description  **Returned:** success |
| **dns_nameservers**  list / elements=string | DNS name servers for this subnet.  **Returned:** success |
| **dns_publish_fixed_ip**  boolean | Whether to publish DNS records for fixed IPs.  **Returned:** success |
| **gateway_ip**  string | Subnet’s gateway ip.  **Returned:** success |
| **host_routes**  string | A list of host routes.  **Returned:** success |
| **id**  string | Unique UUID.  **Returned:** success |
| **ip_version**  integer | IP version for this subnet.  **Returned:** success |
| **ipv6_address_mode**  string | The IPv6 address modes which are ‘dhcpv6-stateful’, ‘dhcpv6-stateless’ or ‘slaac’.  **Returned:** success |
| **ipv6_ra_mode**  string | The IPv6 router advertisements modes which can be ‘slaac’, ‘dhcpv6-stateful’, ‘dhcpv6-stateless’.  **Returned:** success |
| **is_dhcp_enabled**  boolean | DHCP enable flag for this subnet.  **Returned:** success |
| **name**  string | Name given to the subnet.  **Returned:** success |
| **network_id**  string | Network ID this subnet belongs in.  **Returned:** success |
| **prefix_length**  string | The prefix length to use for subnet allocation from a subnet pool.  **Returned:** success |
| **project_id**  string | Project id associated with this subnet.  **Returned:** success |
| **revision_number**  integer | Revision number of the resource  **Returned:** success |
| **segment_id**  string | The ID of the segment this subnet is associated with.  **Returned:** success |
| **service_types**  list / elements=string | Service types for this subnet  **Returned:** success |
| **subnet_pool_id**  string | The subnet pool ID from which to obtain a CIDR.  **Returned:** success |
| **tags**  string | Tags  **Returned:** success |
| **updated_at**  string | Timestamp when the subnet was last updated.  **Returned:** success |
| **use_default_subnet_pool**  boolean | Whether to use the default subnet pool to obtain a CIDR.  **Returned:** success |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
