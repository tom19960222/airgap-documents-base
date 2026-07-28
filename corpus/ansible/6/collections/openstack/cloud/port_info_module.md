---
collection: ansible
version: "6"
title: "openstack.cloud.port_info module – Retrieve information about ports within OpenStack."
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/port_info_module.html
fetched_at: 2026-07-28T00:16:56+00:00
---
# openstack.cloud.port_info module – Retrieve information about ports within OpenStack.

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
> see [Requirements](port_info_module.md#ansible-collections-openstack-cloud-port-info-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.port_info`.

- [Synopsis](port_info_module.md#synopsis)
- [Requirements](port_info_module.md#requirements)
- [Parameters](port_info_module.md#parameters)
- [Notes](port_info_module.md#notes)
- [Examples](port_info_module.md#examples)
- [Return Values](port_info_module.md#return-values)

## [Synopsis](port_info_module.md#id1)

- Retrieve information about ports from OpenStack.
- This module was called `openstack.cloud.port_facts` before Ansible 2.9, returning `ansible_facts`. Note that the [openstack.cloud.port_info](port_info_module.md#ansible-collections-openstack-cloud-port-info-module) module no longer returns `ansible_facts`!

## [Requirements](port_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- openstacksdk
- openstacksdk >= 0.36, < 0.99.0
- python >= 3.6

## [Parameters](port_info_module.md#id3)

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
| **filters**  dictionary | A dictionary of meta data to use for further filtering. Elements of this dictionary will be matched against the returned port dictionaries. Matching is currently limited to strings within the port dictionary, or strings within nested dictionaries. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  Choices:   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **port**  string | Unique name or ID of a port. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  Choices:   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **timeout**  integer | How long should ansible wait for the requested resource.  Default: `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `yes`.  Choices:   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  Choices:   - `false` - `true` ← (default) |

## [Notes](port_info_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](port_info_module.md#id5)

```yaml+jinja
# Gather information about all ports
- openstack.cloud.port_info:
    cloud: mycloud
  register: result

- debug:
    msg: "{{ result.openstack_ports }}"

# Gather information about a single port
- openstack.cloud.port_info:
    cloud: mycloud
    port: 6140317d-e676-31e1-8a4a-b1913814a471

# Gather information about all ports that have device_id set to a specific value
# and with a status of ACTIVE.
- openstack.cloud.port_info:
    cloud: mycloud
    filters:
      device_id: 1038a010-3a37-4a9d-82ea-652f1da36597
      status: ACTIVE
```

## [Return Values](port_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **openstack_ports**  complex | List of port dictionaries. A subset of the dictionary keys listed below may be returned, depending on your cloud provider.  Returned: always, but can be null |
| **admin_state_up**  boolean | The administrative state of the router, which is up (true) or down (false).  Returned: success  Sample: `true` |
| **allowed_address_pairs**  list / elements=string | A set of zero or more allowed address pairs. An address pair consists of an IP address and MAC address.  Returned: success  Sample: `[]` |
| **binding:host_id**  string | The UUID of the host where the port is allocated.  Returned: success  Sample: `"b4bd682d-234a-4091-aa5b-4b025a6a7759"` |
| **binding:profile**  dictionary | A dictionary the enables the application running on the host to pass and receive VIF port-specific information to the plug-in.  Returned: success  Sample: `{}` |
| **binding:vif_details**  dictionary | A dictionary that enables the application to pass information about functions that the Networking API provides.  Returned: success  Sample: `{"port_filter": true}` |
| **binding:vif_type**  dictionary | The VIF type for the port.  Returned: success  Sample: `"ovs"` |
| **binding:vnic_type**  string | The virtual network interface card (vNIC) type that is bound to the neutron port.  Returned: success  Sample: `"normal"` |
| **device_id**  string | The UUID of the device that uses this port.  Returned: success  Sample: `"b4bd682d-234a-4091-aa5b-4b025a6a7759"` |
| **device_owner**  string | The UUID of the entity that uses this port.  Returned: success  Sample: `"network:router_interface"` |
| **dns_assignment**  list / elements=string | DNS assignment information.  Returned: success |
| **dns_name**  string | DNS name  Returned: success  Sample: `""` |
| **extra_dhcp_opts**  list / elements=string | A set of zero or more extra DHCP option pairs. An option pair consists of an option value and name.  Returned: success  Sample: `[]` |
| **fixed_ips**  list / elements=string | The IP addresses for the port. Includes the IP address and UUID of the subnet.  Returned: success |
| **id**  string | The UUID of the port.  Returned: success  Sample: `"3ec25c97-7052-4ab8-a8ba-92faf84148de"` |
| **ip_address**  string | The IP address.  Returned: success  Sample: `"127.0.0.1"` |
| **mac_address**  string | The MAC address.  Returned: success  Sample: `"00:00:5E:00:53:42"` |
| **name**  string | The port name.  Returned: success  Sample: `"port_name"` |
| **network_id**  string | The UUID of the attached network.  Returned: success  Sample: `"dd1ede4f-3952-4131-aab6-3b8902268c7d"` |
| **port_security_enabled**  boolean | The port security status. The status is enabled (true) or disabled (false).  Returned: success  Sample: `false` |
| **security_groups**  list / elements=string | The UUIDs of any attached security groups.  Returned: success |
| **status**  string | The port status.  Returned: success  Sample: `"ACTIVE"` |
| **tenant_id**  string | The UUID of the tenant who owns the network.  Returned: success  Sample: `"51fce036d7984ba6af4f6c849f65ef00"` |

### Authors

- OpenStack Ansible SIG

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
