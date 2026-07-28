---
collection: ansible
version: "8"
title: "openstack.cloud.port_info module – Retrieve information about ports within OpenStack."
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/port_info_module.html
fetched_at: 2026-07-28T02:48:29+00:00
---
# openstack.cloud.port_info module – Retrieve information about ports within OpenStack.

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

## [Requirements](port_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](port_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **filters**  dictionary | A dictionary of meta data to use for further filtering. Elements of this dictionary will be matched passed to the API as query parameter filters. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **name**  aliases: port  string | Unique name or ID of a port. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

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
    msg: "{{ result.ports}}"

# Gather information about a single port
- openstack.cloud.port_info:
    cloud: mycloud
    name: 6140317d-e676-31e1-8a4a-b1913814a471

# Gather information about all ports that have device_id set to a specific
# value and with a status of ACTIVE.
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
| **ports**  list / elements=dictionary | List of port dictionaries. A subset of the dictionary keys listed below may be returned, depending on your cloud provider.  **Returned:** always |
| **allowed_address_pairs**  list / elements=string | Allowed address pairs.  **Returned:** success  **Sample:** `[]` |
| **binding_host_id**  string | The ID of the host where the port is allocated. In some cases, different implementations can run on different hosts.  **Returned:** success  **Sample:** `"b4bd682d-234a-4091-aa5b-4b025a6a7759"` |
| **binding_profile**  dictionary | A dictionary the enables the application running on the specified host to pass and receive vif port-specific information to the plug-in.  **Returned:** success  **Sample:** `{}` |
| **binding_vif_details**  dictionary | A dictionary that enables the application to pass information about functions that the Networking API provides.  **Returned:** success |
| **binding_vif_type**  dictionary | The VIF type for the port.  **Returned:** success |
| **binding_vnic_type**  string | The virtual network interface card (vNIC) type that is bound to the neutron port.  **Returned:** success  **Sample:** `"normal"` |
| **created_at**  string | Timestamp when the port was created.  **Returned:** success  **Sample:** `"2022-02-03T13:28:25Z"` |
| **data_plane_status**  string | Status of the underlying data plane of a port.  **Returned:** success |
| **description**  string | The port description.  **Returned:** success |
| **device_id**  string | Device ID of this port.  **Returned:** success  **Sample:** `"b4bd682d-234a-4091-aa5b-4b025a6a7759"` |
| **device_owner**  string | Device owner of this port, e.g. `network:dhcp`.  **Returned:** success  **Sample:** `"network:router_interface"` |
| **device_profile**  string | Device profile of this port, refers to Cyborg device-profiles: <https://docs.openstack.org/api-ref/accelerator/v2/index>.html# device-profiles.  **Returned:** success |
| **dns_assignment**  list / elements=string | DNS assignment for the port.  **Returned:** success |
| **dns_domain**  string | DNS domain assigned to the port.  **Returned:** success |
| **dns_name**  string | DNS name for the port.  **Returned:** success |
| **extra_dhcp_opts**  list / elements=string | A set of zero or more extra DHCP option pairs. An option pair consists of an option value and name.  **Returned:** success  **Sample:** `[]` |
| **fixed_ips**  list / elements=string | IP addresses for the port. Includes the IP address and subnet ID.  **Returned:** success |
| **id**  string | The port ID.  **Returned:** success  **Sample:** `"3ec25c97-7052-4ab8-a8ba-92faf84148de"` |
| **ip_allocation**  string | The ip_allocation indicates when ports use deferred, immediate or no IP allocation.  **Returned:** success |
| **is_admin_state_up**  boolean | The administrative state of the port, which is up `True` or down `False`.  **Returned:** success  **Sample:** `true` |
| **is_port_security_enabled**  boolean | The port security status, which is enabled `True` or disabled `False`.  **Returned:** success  **Sample:** `false` |
| **mac_address**  string | The MAC address of an allowed address pair.  **Returned:** success  **Sample:** `"00:00:5E:00:53:42"` |
| **name**  string | The port name.  **Returned:** success  **Sample:** `"port_name"` |
| **network_id**  string | The ID of the attached network.  **Returned:** success  **Sample:** `"dd1ede4f-3952-4131-aab6-3b8902268c7d"` |
| **numa_affinity_policy**  string | The NUMA affinity policy defined for this port.  **Returned:** success  **Sample:** `"required"` |
| **project_id**  string | The ID of the project who owns the network.  **Returned:** success  **Sample:** `"aa1ede4f-3952-4131-aab6-3b8902268c7d"` |
| **propagate_uplink_status**  boolean | Whether to propagate uplink status of the port.  **Returned:** success  **Sample:** `false` |
| **qos_network_policy_id**  string | The ID of the QoS policy attached to the network where the port is bound.  **Returned:** success  **Sample:** `"1e4f3958-c0c9-4dec-82fa-ed2dc1c5cb34"` |
| **qos_policy_id**  string | The ID of the QoS policy attached to the port.  **Returned:** success  **Sample:** `"b20bb47f-5d6d-45a6-8fe7-2c1b44f0db73"` |
| **resource_request**  string | The port-resource-request exposes Placement resources (i.e.: minimum-bandwidth) and traits (i.e.: vnic-type, physnet) requested by a port to Nova and Placement.  **Returned:** success |
| **revision_number**  integer | The revision number of the resource.  **Returned:** success  **Sample:** `0` |
| **security_group_ids**  list / elements=string | The IDs of any attached security groups.  **Returned:** success |
| **status**  string | The port status. Value is `ACTIVE` or `DOWN`.  **Returned:** success  **Sample:** `"ACTIVE"` |
| **tags**  list / elements=string | The list of tags on the resource.  **Returned:** success  **Sample:** `[]` |
| **tenant_id**  string | Same as *project_id*. Deprecated.  **Returned:** success  **Sample:** `"51fce036d7984ba6af4f6c849f65ef00"` |
| **trunk_details**  dictionary | The trunk referring to this parent port and its subports. Present for trunk parent ports if `trunk-details` extension is loaded.  **Returned:** success |
| **updated_at**  string | Timestamp when the port was last updated.  **Returned:** success  **Sample:** `"2022-02-03T13:28:25Z"` |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
