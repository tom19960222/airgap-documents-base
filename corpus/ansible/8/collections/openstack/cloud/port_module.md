---
collection: ansible
version: "8"
title: "openstack.cloud.port module – Add/Update/Delete ports from an OpenStack cloud."
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/port_module.html
fetched_at: 2026-07-28T02:48:26+00:00
---
# openstack.cloud.port module – Add/Update/Delete ports from an OpenStack cloud.

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
> see [Requirements](port_module.md#ansible-collections-openstack-cloud-port-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.port`.

- [Synopsis](port_module.md#synopsis)
- [Requirements](port_module.md#requirements)
- [Parameters](port_module.md#parameters)
- [Notes](port_module.md#notes)
- [Examples](port_module.md#examples)
- [Return Values](port_module.md#return-values)

## [Synopsis](port_module.md#id1)

- Add, Update or Remove ports from an OpenStack cloud.

## [Requirements](port_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](port_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allowed_address_pairs**  list / elements=dictionary | Allowed address pairs list. Allowed address pairs are supported with dictionary structure. e.g. allowed_address_pairs: - ip_address: 10.1.0.12 mac_address: ab:cd:ef:12:34:56 - ip_address: …  The port will change during update if not all suboptions are specified, e.g. when ip_address is given but mac_address is not. |
| **ip_address**  string | The IP address. |
| **mac_address**  string | The MAC address. |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **binding_profile**  dictionary | Binding profile dict that the port should be created with. |
| **binding_vnic_type**  aliases: vnic_type  string | The type of the port that should be created  **Choices:**   - `"normal"` - `"direct"` - `"direct-physical"` - `"macvtap"` - `"baremetal"` - `"virtio-forwarder"` |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **description**  string | Description of the port. |
| **device_id**  string | Device ID of device using this port. |
| **device_owner**  string | The ID of the entity that uses this port. |
| **dns_domain**  string | The dns domain of the port ( only with dns-integration enabled ) |
| **dns_name**  string | The dns name of the port ( only with dns-integration enabled ) |
| **extra_dhcp_opts**  list / elements=dictionary | Extra dhcp options to be assigned to this port. Extra options are supported with dictionary structure. Note that options cannot be removed only updated. e.g. extra_dhcp_opts: - ip_version: 4 opt_name: bootfile-name opt_value: pxelinux.0 - opt_name: …  The port will change during update if not all suboptions are specified, e.g. when opt_name is given but ip_version is not. |
| **ip_version**  integer / required | The IP version this DHCP option is for. |
| **opt_name**  string / required | The name of the DHCP option to set. |
| **opt_value**  string / required | The value of the DHCP option to set. |
| **fixed_ips**  list / elements=dictionary | Desired IP and/or subnet for this port. Subnet is referenced by subnet_id and IP is referenced by ip_address.  The port will change during update if not all suboptions are specified, e.g. when ip_address is given but subnet_id is not. |
| **ip_address**  string / required | The fixed IP address to attempt to allocate. |
| **subnet_id**  string | The subnet to attach the IP address to. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **is_admin_state_up**  aliases: admin_state_up  boolean | Sets admin state.  **Choices:**   - `false` - `true` |
| **is_port_security_enabled**  aliases: port_security_enabled  boolean | Whether to enable or disable the port security on the network.  **Choices:**   - `false` - `true` |
| **mac_address**  string | MAC address of this port. |
| **name**  string / required | Name that has to be given to the port.  This port attribute cannot be updated. |
| **network**  string | ID or name of the network this port belongs to.  Required when creating a new port.  Must be a name when creating a port.  This port attribute cannot be updated. |
| **no_security_groups**  boolean | Do not associate a security group with this port.  Deprecated. Use *security_groups*: `[]` instead of *no_security_groups*: `true`.  **Choices:**   - `false` ← (default) - `true` |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **security_groups**  list / elements=string | Security group(s) ID(s) or name(s) associated with the port. |
| **state**  string | Should the resource be present or absent.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](port_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](port_module.md#id5)

```yaml+jinja
# Create a port
- openstack.cloud.port:
    state: present
    auth:
      auth_url: https://identity.example.com
      username: admin
      password: admin
      project_name: admin
    name: port1
    network: foo

# Create a port with a static IP
- openstack.cloud.port:
    state: present
    auth:
      auth_url: https://identity.example.com
      username: admin
      password: admin
      project_name: admin
    name: port1
    network: foo
    fixed_ips:
      - ip_address: 10.1.0.21

# Create a port with No security groups
- openstack.cloud.port:
    state: present
    auth:
      auth_url: https://identity.example.com
      username: admin
      password: admin
      project_name: admin
    name: port1
    network: foo
    no_security_groups: True

# Update the existing 'port1' port with multiple security groups (version 1)
- openstack.cloud.port:
    state: present
    auth:
      auth_url: https://identity.example.com
      username: admin
      password: admin
      project_name: admin
    name: port1
    security_groups: 1496e8c7-4918-482a-9172-f4f00fc4a3a5,057d4bdf-6d4d-472...

# Update the existing 'port1' port with multiple security groups (version 2)
- openstack.cloud.port:
    state: present
    auth:
      auth_url: https://identity.example.com
      username: admin
      password: admin
      project_name: admin
    name: port1
    security_groups:
      - 1496e8c7-4918-482a-9172-f4f00fc4a3a5
      - 057d4bdf-6d4d-472...

# Create port of type 'direct'
- openstack.cloud.port:
    state: present
    auth:
      auth_url: https://identity.example.com
      username: admin
      password: admin
      project_name: admin
    name: port1
    network: foo
    binding_vnic_type: direct

# Create a port with binding profile
- openstack.cloud.port:
    state: present
    auth:
      auth_url: https://identity.example.com
      username: admin
      password: admin
      project_name: admin
    name: port1
    network: foo
    binding_profile:
      pci_slot: "0000:03:11.1"
      physical_network: "provider"
```

## [Return Values](port_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **port**  dictionary | Dictionary describing the port.  **Returned:** On success when *state* is `present`. |
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
