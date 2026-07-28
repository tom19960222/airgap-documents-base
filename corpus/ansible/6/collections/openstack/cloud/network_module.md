---
collection: ansible
version: "6"
title: "openstack.cloud.network module – Creates/removes networks from OpenStack"
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/network_module.html
fetched_at: 2026-07-28T00:16:51+00:00
---
# openstack.cloud.network module – Creates/removes networks from OpenStack

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
> see [Requirements](network_module.md#ansible-collections-openstack-cloud-network-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.network`.

- [Synopsis](network_module.md#synopsis)
- [Requirements](network_module.md#requirements)
- [Parameters](network_module.md#parameters)
- [Notes](network_module.md#notes)
- [Examples](network_module.md#examples)
- [Return Values](network_module.md#return-values)

## [Synopsis](network_module.md#id1)

- Add or remove network from OpenStack.

## [Requirements](network_module.md#id2)

The below requirements are needed on the host that executes this module.

- openstacksdk
- openstacksdk >= 0.36, < 0.99.0
- python >= 3.6

## [Parameters](network_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **admin_state_up**  boolean | Whether the state should be marked as up or down.  Choices:   - `false` - `true` ← (default) |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **availability_zone**  string | Ignored. Present for backwards compatibility |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **dns_domain**  string | The DNS domain value to set. Requires openstacksdk>=0.29. Network will use Openstack defaults if this option is not provided. |
| **external**  boolean | Whether this network is externally accessible.  Choices:   - `false` ← (default) - `true` |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  Choices:   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **mtu_size**  aliases: mtu  integer | The maximum transmission unit (MTU) value to address fragmentation. Network will use OpenStack defaults if this option is not provided. Requires openstacksdk>=0.18. |
| **name**  string / required | Name to be assigned to the network. |
| **port_security_enabled**  boolean | Whether port security is enabled on the network or not. Network will use OpenStack defaults if this option is not utilised. Requires openstacksdk>=0.18.  Choices:   - `false` - `true` |
| **project**  string | Project name or ID containing the network (name admin-only) |
| **provider_network_type**  string | The type of physical network that maps to this network resource. |
| **provider_physical_network**  string | The physical network where this network object is implemented. |
| **provider_segmentation_id**  integer | An isolated segment on the physical network. The *network_type* attribute defines the segmentation model. For example, if the *network_type* value is vlan, this ID is a vlan identifier. If the *network_type* value is gre, this ID is a gre key. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  Choices:   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **shared**  boolean | Whether this network is shared or not.  Choices:   - `false` ← (default) - `true` |
| **state**  string | Indicate desired state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  Default: `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `yes`.  Choices:   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  Choices:   - `false` - `true` ← (default) |

## [Notes](network_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](network_module.md#id5)

```yaml+jinja
# Create an externally accessible network named 'ext_network'.
- openstack.cloud.network:
    cloud: mycloud
    state: present
    name: ext_network
    external: true
```

## [Return Values](network_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **network**  complex | Dictionary describing the network.  Returned: On success when *state* is ‘present’. |
| **admin_state_up**  boolean | The administrative state of the network.  Returned: success  Sample: `true` |
| **dns_domain**  string | The DNS domain of a network resource.  Returned: success  Sample: `"sample.openstack.org."` |
| **id**  string | Network ID.  Returned: success  Sample: `"4bb4f9a5-3bd2-4562-bf6a-d17a6341bb56"` |
| **mtu**  integer | The MTU of a network resource.  Returned: success  Sample: `0` |
| **name**  string | Network name.  Returned: success  Sample: `"ext_network"` |
| **port_security_enabled**  boolean | The port security status  Returned: success  Sample: `true` |
| **provider:network_type**  string | The type of physical network that maps to this network resource.  Returned: success  Sample: `"vlan"` |
| **provider:physical_network**  string | The physical network where this network object is implemented.  Returned: success  Sample: `"my_vlan_net"` |
| **provider:segmentation_id**  string | An isolated segment on the physical network.  Returned: success  Sample: `"101"` |
| **router:external**  boolean | Indicates whether this network is externally accessible.  Returned: success  Sample: `true` |
| **shared**  boolean | Indicates whether this network is shared across all tenants.  Returned: success  Sample: `false` |
| **status**  string | Network status.  Returned: success  Sample: `"ACTIVE"` |
| **subnets**  list / elements=string | The associated subnets.  Returned: success  Sample: `[]` |
| **tenant_id**  string | The tenant ID.  Returned: success  Sample: `"06820f94b9f54b119636be2728d216fc"` |

### Authors

- OpenStack Ansible SIG

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
