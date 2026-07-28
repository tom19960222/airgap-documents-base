---
collection: ansible
version: "6"
title: "openstack.cloud.baremetal_node_info module – Retrieve information about Bare Metal nodes from OpenStack"
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/baremetal_node_info_module.html
fetched_at: 2026-07-28T00:16:22+00:00
---
# openstack.cloud.baremetal_node_info module – Retrieve information about Bare Metal nodes from OpenStack

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
> see [Requirements](baremetal_node_info_module.md#ansible-collections-openstack-cloud-baremetal-node-info-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.baremetal_node_info`.

- [Synopsis](baremetal_node_info_module.md#synopsis)
- [Requirements](baremetal_node_info_module.md#requirements)
- [Parameters](baremetal_node_info_module.md#parameters)
- [Notes](baremetal_node_info_module.md#notes)
- [Examples](baremetal_node_info_module.md#examples)
- [Return Values](baremetal_node_info_module.md#return-values)

## [Synopsis](baremetal_node_info_module.md#id1)

- Retrieve information about Bare Metal nodes from OpenStack.

## [Requirements](baremetal_node_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- openstacksdk
- openstacksdk >= 0.36, < 0.99.0
- python >= 3.6

## [Parameters](baremetal_node_info_module.md#id3)

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
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  Choices:   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **ironic_url**  string | If noauth mode is utilized, this is required to be set to the endpoint URL for the Ironic API. Use with “auth” and “auth_type” settings set to None. |
| **mac**  string | Unique mac address that is used to attempt to identify the host. |
| **node**  string | Name or globally unique identifier (UUID) to identify the host. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  Choices:   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **timeout**  integer | How long should ansible wait for the requested resource.  Default: `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `yes`.  Choices:   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  Choices:   - `false` - `true` ← (default) |

## [Notes](baremetal_node_info_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](baremetal_node_info_module.md#id5)

```yaml+jinja
# Gather information about all baremeal nodes
- openstack.cloud.baremetal_node_info:
    cloud: "devstack"
  register: result
- debug:
    msg: "{{ result.baremetal_nodes }}"
# Gather information about a baremeal node
- openstack.cloud.baremetal_node_info:
    cloud: "devstack"
    node: "00000000-0000-0000-0000-000000000002"
  register: result
- debug:
    msg: "{{ result.baremetal_nodes }}"
```

## [Return Values](baremetal_node_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **baremetal_nodes**  complex | Bare Metal node list. A subset of the dictionary keys listed below may be returned, depending on your cloud provider.  Returned: always, but can be null |
| **allocation_uuid**  string | The UUID of the allocation associated with the node. If not null, will be the same as instance_uuid (the opposite is not always true). Unlike instance_uuid, this field is read-only. Please use the Allocation API to remove allocations.  Returned: success |
| **automated_clean**  boolean | Indicates whether the node will perform automated clean or not.  Returned: success |
| **bios_interface**  string | The bios interface to be used for this node.  Returned: success |
| **boot_interface**  string | The boot interface for a Node, e.g. “pxe”.  Returned: success |
| **boot_mode**  string | The boot mode for a node, either “uefi” or “bios”  Returned: success |
| **chassis_uuid**  string | UUID of the chassis associated with this Node. May be empty or None.  Returned: success |
| **clean_step**  string | The current clean step.  Returned: success |
| **conductor**  string | The conductor currently servicing a node. This field is read-only.  Returned: success |
| **conductor_group**  string | The conductor group for a node. Case-insensitive string up to 255 characters, containing a-z, 0-9, _, -, and ..  Returned: success |
| **console_enabled**  boolean | Indicates whether console access is enabled or disabled on this node.  Returned: success |
| **console_interface**  string | The console interface for a node, e.g. “no-console”.  Returned: success |
| **created_at**  string | Bare Metal node created at timestamp.  Returned: success |
| **deploy_interface**  string | The deploy interface for a node, e.g. “direct”.  Returned: success |
| **deploy_step**  string | The current deploy step.  Returned: success |
| **driver**  string | The name of the driver.  Returned: success |
| **driver_info**  dictionary | All the metadata required by the driver to manage this Node. List of fields varies between drivers, and can be retrieved from the /v1/drivers/<DRIVER_NAME>/properties resource.  Returned: success |
| **driver_internal_info**  dictionary | Internal metadata set and stored by the Node’s driver.  Returned: success |
| **extra**  dictionary | A set of one or more arbitrary metadata key and value pairs.  Returned: success |
| **fault**  string | The fault indicates the active fault detected by ironic, typically the Node is in “maintenance mode”. None means no fault has been detected by ironic. “power failure” indicates ironic failed to retrieve power state from this node. There are other possible types, e.g., “clean failure” and “rescue abort failure”.  Returned: success |
| **id**  string | The UUID for the resource.  Returned: success |
| **inspect_interface**  string | The interface used for node inspection.  Returned: success |
| **instance_info**  dictionary | Information used to customize the deployed image. May include root partition size, a base 64 encoded config drive, and other metadata. Note that this field is erased automatically when the instance is deleted (this is done by requesting the Node provision state be changed to DELETED).  Returned: success |
| **instance_uuid**  string | UUID of the Nova instance associated with this Node.  Returned: success |
| **last_error**  string | Any error from the most recent (last) transaction that started but failed to finish.  Returned: success |
| **maintenance**  boolean | Whether or not this Node is currently in “maintenance mode”. Setting a Node into maintenance mode removes it from the available resource pool and halts some internal automation. This can happen manually (eg, via an API request) or automatically when Ironic detects a hardware fault that prevents communication with the machine.  Returned: success |
| **maintenance_reason**  string | User-settable description of the reason why this Node was placed into maintenance mode  Returned: success |
| **management_interface**  string | Interface for out-of-band node management.  Returned: success |
| **name**  string | Human-readable identifier for the Node resource. May be undefined. Certain words are reserved.  Returned: success |
| **network_interface**  string | Which Network Interface provider to use when plumbing the network connections for this Node.  Returned: success |
| **owner**  string | A string or UUID of the tenant who owns the object.  Returned: success |
| **portgroups**  list / elements=dictionary | List of ironic portgroups on this node.  Returned: success |
| **address**  string | Physical hardware address of this Portgroup, typically the hardware MAC address.  Returned: success |
| **created_at**  string | The UTC date and time when the resource was created, ISO 8601 format.  Returned: success |
| **extra**  dictionary | A set of one or more arbitrary metadata key and value pairs.  Returned: success |
| **id**  string | The UUID for the resource.  Returned: success |
| **internal_info**  dictionary | Internal metadata set and stored by the Portgroup. This field is read-only.  Returned: success |
| **is_standalone_ports_supported**  boolean | Indicates whether ports that are members of this portgroup can be used as stand-alone ports.  Returned: success |
| **mode**  string | Mode of the port group. For possible values, refer to <https://www.kernel.org/doc/Documentation/networking/bonding.txt>. If not specified in a request to create a port group, it will be set to the value of the [DEFAULT]default_portgroup_mode configuration option. When set, can not be removed from the port group.  Returned: success |
| **name**  string | Human-readable identifier for the Portgroup resource. May be undefined.  Returned: success |
| **node_id**  string | UUID of the Node this resource belongs to.  Returned: success |
| **ports**  list / elements=string | List of port UUID’s of ports belonging to this portgroup.  Returned: success |
| **properties**  dictionary | Key/value properties related to the port group’s configuration.  Returned: success |
| **updated_at**  string | The UTC date and time when the resource was updated, ISO 8601 format. May be “null”.  Returned: success |
| **ports**  list / elements=dictionary | List of ironic ports on this node.  Returned: success |
| **address**  string | Physical hardware address of this network Port, typically the hardware MAC address.  Returned: success |
| **created_at**  string | The UTC date and time when the resource was created, ISO 8601 format.  Returned: success |
| **extra**  dictionary | A set of one or more arbitrary metadata key and value pairs.  Returned: success |
| **id**  string | The UUID for the resource.  Returned: success |
| **internal_info**  dictionary | Internal metadata set and stored by the Port. This field is read-only.  Returned: success |
| **local_link_connection**  dictionary | The Port binding profile. If specified, must contain switch_id (only a MAC address or an OpenFlow based datapath_id of the switch are accepted in this field) and port_id (identifier of the physical port on the switch to which node’s port is connected to) fields. switch_info is an optional string field to be used to store any vendor-specific information.  Returned: success |
| **name**  string | The name of the resource.  Returned: success |
| **node_uuid**  string | UUID of the Node this resource belongs to.  Returned: success |
| **physical_network**  string | The name of the physical network to which a port is connected. May be empty.  Returned: success |
| **portgroup_uuid**  string | UUID of the Portgroup this resource belongs to.  Returned: success |
| **pxe_enabled**  string | Indicates whether PXE is enabled or disabled on the Port.  Returned: success |
| **updated_at**  string | The UTC date and time when the resource was updated, ISO 8601 format. May be “null”.  Returned: success |
| **uuid**  string | The UUID for the resource.  Returned: success |
| **power_interface**  string | Interface used for performing power actions on the node, e.g. “ipmitool”.  Returned: success |
| **power_state**  string | The current power state of this Node. Usually, “power on” or “power off”, but may be “None” if Ironic is unable to determine the power state (eg, due to hardware failure).  Returned: success |
| **properties**  dictionary | Physical characteristics of this Node. Populated by ironic-inspector during inspection. May be edited via the REST API at any time.  Returned: success |
| **protected**  boolean | Whether the node is protected from undeploying, rebuilding and deletion.  Returned: success |
| **protected_reason**  string | The reason the node is marked as protected.  Returned: success |
| **provision_state**  string | The current provisioning state of this Node.  Returned: success |
| **raid_config**  dictionary | Represents the current RAID configuration of the node. Introduced with the cleaning feature.  Returned: success |
| **raid_interface**  string | Interface used for configuring RAID on this node.  Returned: success |
| **rescue_interface**  string | The interface used for node rescue, e.g. “no-rescue”.  Returned: success |
| **reservation**  string | The name of an Ironic Conductor host which is holding a lock on this node, if a lock is held. Usually “null”, but this field can be useful for debugging.  Returned: success |
| **resource_class**  string | A string which can be used by external schedulers to identify this Node as a unit of a specific type of resource. For more details, see <https://docs.openstack.org/ironic/latest/install/configure-nova-flavors.html>  Returned: success |
| **retired**  boolean | Whether the node is retired and can hence no longer be provided, i.e. move from manageable to available, and will end up in manageable after cleaning (rather than available).  Returned: success |
| **retired_reason**  string | The reason the node is marked as retired.  Returned: success |
| **secure_boot**  boolean | Indicates whether node is currently booted with secure_boot turned on.  Returned: success |
| **storage_interface**  string | Interface used for attaching and detaching volumes on this node, e.g. “cinder”.  Returned: success |
| **target_power_state**  string | If a power state transition has been requested, this field represents the requested (ie, “target”) state, either “power on” or “power off”.  Returned: success |
| **target_provision_state**  string | If a provisioning action has been requested, this field represents the requested (ie, “target”) state. Note that a Node may go through several states during its transition to this target state. For instance, when requesting an instance be deployed to an AVAILABLE Node, the Node may go through the following state change progression, AVAILABLE -> DEPLOYING -> DEPLOYWAIT -> DEPLOYING -> ACTIVE  Returned: success |
| **target_raid_config**  dictionary | Represents the requested RAID configuration of the node, which will be applied when the Node next transitions through the CLEANING state. Introduced with the cleaning feature.  Returned: success |
| **traits**  list / elements=string | List of traits for this node.  Returned: success |
| **updated_at**  string | Bare Metal node updated at timestamp.  Returned: success |
| **uuid**  string | The UUID for the resource.  Returned: success |
| **vendor_interface**  string | Interface for vendor-specific functionality on this node, e.g. “no-vendor”.  Returned: success |

### Authors

- OpenStack Ansible SIG

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
