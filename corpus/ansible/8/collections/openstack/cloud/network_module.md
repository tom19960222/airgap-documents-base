---
collection: ansible
version: "8"
title: "openstack.cloud.network module – Creates/removes networks from OpenStack"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/network_module.html
fetched_at: 2026-07-28T02:48:16+00:00
---
# openstack.cloud.network module – Creates/removes networks from OpenStack

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

- Add, update or remove network from OpenStack.

## [Requirements](network_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](network_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **admin_state_up**  boolean | Whether the state should be marked as up or down.  **Choices:**   - `false` - `true` |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **dns_domain**  string | The DNS domain value to set. Network will use Openstack defaults if this option is not provided. |
| **external**  boolean | Whether this network is externally accessible.  **Choices:**   - `false` - `true` |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **mtu**  aliases: mtu_size  integer | The maximum transmission unit (MTU) value to address fragmentation. Network will use OpenStack defaults if this option is not provided. |
| **name**  string / required | Name to be assigned to the network. |
| **port_security_enabled**  boolean | Whether port security is enabled on the network or not. Network will use OpenStack defaults if this option is not utilised.  **Choices:**   - `false` - `true` |
| **project**  string | Project name or ID containing the network (name admin-only) |
| **provider_network_type**  string | The type of physical network that maps to this network resource. |
| **provider_physical_network**  string | The physical network where this network object is implemented. |
| **provider_segmentation_id**  integer | An isolated segment on the physical network. The *network_type* attribute defines the segmentation model. For example, if the *network_type* value is vlan, this ID is a vlan identifier. If the *network_type* value is gre, this ID is a gre key. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **shared**  boolean | Whether this network is shared or not.  **Choices:**   - `false` - `true` |
| **state**  string | Indicate desired state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

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
| **id**  string | Id of network  **Returned:** On success when network exists. |
| **network**  dictionary | Dictionary describing the network.  **Returned:** On success when network exists. |
| **availability_zone_hints**  string | Availability zone hints  **Returned:** success |
| **availability_zones**  string | Availability zones  **Returned:** success |
| **created_at**  string | Created at timestamp  **Returned:** success |
| **description**  string | Description  **Returned:** success |
| **dns_domain**  string | Dns domain  **Returned:** success |
| **id**  string | Id  **Returned:** success |
| **ipv4_address_scope_id**  string | Ipv4 address scope id  **Returned:** success |
| **ipv6_address_scope_id**  string | Ipv6 address scope id  **Returned:** success |
| **is_admin_state_up**  string | Is admin state up  **Returned:** success |
| **is_default**  string | Is default  **Returned:** success |
| **is_port_security_enabled**  string | Is port security enabled  **Returned:** success |
| **is_router_external**  string | Is router external  **Returned:** success |
| **is_shared**  string | Is shared  **Returned:** success |
| **is_vlan_transparent**  string | Is vlan transparent  **Returned:** success |
| **mtu**  string | Mtu  **Returned:** success |
| **name**  string | Name  **Returned:** success |
| **project_id**  string | Project id  **Returned:** success |
| **provider_network_type**  string | Provider network type  **Returned:** success |
| **provider_physical_network**  string | Provider physical network  **Returned:** success |
| **provider_segmentation_id**  string | Provider segmentation id  **Returned:** success |
| **qos_policy_id**  string | Qos policy id  **Returned:** success |
| **revision_number**  string | Revision number  **Returned:** success |
| **segments**  string | Segments  **Returned:** success |
| **status**  string | Status  **Returned:** success |
| **subnet_ids**  string | Subnet ids  **Returned:** success |
| **tags**  string | Tags  **Returned:** success |
| **updated_at**  string | Updated at timestamp  **Returned:** success |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
