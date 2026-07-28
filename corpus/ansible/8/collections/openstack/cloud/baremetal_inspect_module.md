---
collection: ansible
version: "8"
title: "openstack.cloud.baremetal_inspect module – Explicitly triggers baremetal node introspection in ironic."
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/baremetal_inspect_module.html
fetched_at: 2026-07-28T02:47:24+00:00
---
# openstack.cloud.baremetal_inspect module – Explicitly triggers baremetal node introspection in ironic.

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
> see [Requirements](baremetal_inspect_module.md#ansible-collections-openstack-cloud-baremetal-inspect-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.baremetal_inspect`.

- [Synopsis](baremetal_inspect_module.md#synopsis)
- [Requirements](baremetal_inspect_module.md#requirements)
- [Parameters](baremetal_inspect_module.md#parameters)
- [Notes](baremetal_inspect_module.md#notes)
- [Examples](baremetal_inspect_module.md#examples)
- [Return Values](baremetal_inspect_module.md#return-values)

## [Synopsis](baremetal_inspect_module.md#id1)

- Requests Ironic to set a node into inspect state in order to collect metadata regarding the node. This command may be out of band or in-band depending on the ironic driver configuration. This is only possible on nodes in ‘manageable’ and ‘available’ state.

## [Requirements](baremetal_inspect_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](baremetal_inspect_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **mac**  string | unique mac address that is used to attempt to identify the host. |
| **name**  aliases: id, uuid  string | Name or id of the node to inspect.  Mutually exclusive with *mac* |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](baremetal_inspect_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](baremetal_inspect_module.md#id5)

```yaml+jinja
# Invoke node inspection
- openstack.cloud.baremetal_inspect:
    name: "testnode1"
```

## [Return Values](baremetal_inspect_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **node**  dictionary | A dictionary describing the node after inspection  **Returned:** changed |
| **allocation_id**  string | The UUID of the allocation associated with the node.  **Returned:** success |
| **bios_interface**  string | The bios interface to be used for this node.  **Returned:** success |
| **boot_interface**  string | The boot interface for a Node, e.g. “pxe”.  **Returned:** success |
| **boot_mode**  string | The current boot mode state (uefi/bios).  **Returned:** success |
| **chassis_id**  string | UUID of the chassis associated with this Node.  **Returned:** success |
| **clean_step**  string | The current clean step. Introduced with the cleaning feature.  **Returned:** success |
| **conductor**  string | The conductor currently servicing a node.  **Returned:** success |
| **conductor_group**  string | The conductor group for a node.  **Returned:** success |
| **console_interface**  string | Console interface to use when working with serial console.  **Returned:** success  **Sample:** `"no-console"` |
| **created_at**  string | Timestamp at which the node was last updated.  **Returned:** success |
| **deploy_interface**  string | The deploy interface for a node  **Returned:** success  **Sample:** `"iscsi"` |
| **deploy_step**  string | The current deploy step.  **Returned:** success |
| **driver**  string | The name of the driver.  **Returned:** success |
| **driver_info**  dictionary | All the metadata required by the driver to manage this Node. List of fields varies between drivers.  **Returned:** success |
| **driver_internal_info**  dictionary | Internal metadata set and stored by the Node’s driver.  **Returned:** success |
| **extra**  dictionary | A set of one or more arbitrary metadata key and value pairs.  **Returned:** success |
| **fault**  string | The fault indicates the active fault detected by ironic, typically the Node is in “maintenance mode”. None means no fault has been detected by ironic. “power failure” indicates ironic failed to retrieve power state from this node. There are other possible types, e.g., “clean failure” and “rescue abort failure”.  **Returned:** success |
| **id**  string | The UUID for the resource.  **Returned:** success |
| **inspect_interface**  string | The interface used for node inspection.  **Returned:** success  **Sample:** `"no-inspect"` |
| **instance_id**  string | UUID of the Nova instance associated with this Node.  **Returned:** success |
| **instance_info**  dictionary | Information used to customize the deployed image. May include root partition size, a base 64 encoded config drive, and other metadata. Note that this field is erased automatically when the instance is deleted (this is done by requesting the Node provision state be changed to DELETED).  **Returned:** success |
| **is_automated_clean_enabled**  boolean | Override enabling of automated cleaning.  **Returned:** success |
| **is_console_enabled**  boolean | Indicates whether console access is enabled or disabled on this node.  **Returned:** success |
| **is_maintenance**  boolean | Whether or not this Node is currently in “maintenance mode”. Setting a Node into maintenance mode removes it from the available resource pool and halts some internal automation. This can happen manually (eg, via an API request) or automatically when Ironic detects a hardware fault that prevents communication with the machine.  **Returned:** success |
| **is_protected**  boolean | Whether the node is protected from undeploying, rebuilding and deletion.  **Returned:** success |
| **is_retired**  boolean | Whether the node is marked for retirement.  **Returned:** success |
| **is_secure_boot**  boolean | Whether the node is currently booted with secure boot turned on.  **Returned:** success |
| **last_error**  string | Any error from the most recent (last) transaction that started but failed to finish.  **Returned:** success |
| **links**  list / elements=string | A list of relative links. Includes the self and bookmark links.  **Returned:** success |
| **maintenance_reason**  string | User-settable description of the reason why this Node was placed into maintenance mode.  **Returned:** success |
| **management_interface**  string | Interface for out-of-band node management.  **Returned:** success  **Sample:** `"ipmitool"` |
| **name**  string | Human-readable identifier for the Node resource. Certain words are reserved.  **Returned:** success |
| **network_interface**  string | Which Network Interface provider to use when plumbing the network connections for this Node.  **Returned:** success |
| **owner**  string | A string or UUID of the tenant who owns the object.  **Returned:** success |
| **port_groups**  list / elements=string | Links to the collection of portgroups on this node.  **Returned:** success |
| **ports**  list / elements=string | Links to the collection of ports on this node  **Returned:** success |
| **power_interface**  string | Interface used for performing power actions on the node.  **Returned:** success  **Sample:** `"ipmitool"` |
| **power_state**  string | The current power state of this Node. Usually, “power on” or “power off”, but may be “None” if Ironic is unable to determine the power state (eg, due to hardware failure).  **Returned:** success |
| **properties**  dictionary | Properties of the node as found by inspection  **Returned:** success |
| **cpu_arch**  string | Detected CPU architecture type  **Returned:** success  **Sample:** `"x86_64"` |
| **cpus**  string | Count of cpu cores defined in the updated node properties.  **Returned:** success  **Sample:** `"1"` |
| **local_gb**  string | Total size of local disk storage as updated in node properties.  **Returned:** success  **Sample:** `"10"` |
| **memory_mb**  string | Amount of node memory as updated in the node properties  **Returned:** success  **Sample:** `"1024"` |
| **protected_reason**  string | The reason the node is marked as protected.  **Returned:** success |
| **provision_state**  string | The current provisioning state of this Node.  **Returned:** success |
| **raid_config**  dictionary | Represents the current RAID configuration of the node. Introduced with the cleaning feature.  **Returned:** success |
| **raid_interface**  string | Interface used for configuring RAID on this node.  **Returned:** success  **Sample:** `"no-raid"` |
| **rescue_interface**  string | The interface used for node rescue.  **Returned:** success  **Sample:** `"no-rescue"` |
| **reservation**  string | The name of an Ironic Conductor host which is holding a lock on this node, if a lock is held. Usually “null”, but this field can be useful for debugging.  **Returned:** success |
| **resource_class**  string | A string which can be used by external schedulers to identify this Node as a unit of a specific type of resource.  **Returned:** success |
| **retired_reason**  string | TODO  **Returned:** success |
| **states**  list / elements=string | Links to the collection of states. Note that this resource is also used to request state transitions.  **Returned:** success |
| **storage_interface**  string | Interface used for attaching and detaching volumes on this node, e.g. “cinder”.  **Returned:** success |
| **target_power_state**  string | If a power state transition has been requested, this field represents the requested (ie, “target”) state, either “power on” or “power off”.  **Returned:** success |
| **target_provision_state**  string | If a provisioning action has been requested, this field represents the requested (ie, “target”) state. Note that a Node may go through several states during its transition to this target state. For instance, when requesting an instance be deployed to an AVAILABLE Node, the Node may go through the following state change progression: AVAILABLE -> DEPLOYING -> DEPLOYWAIT -> DEPLOYING -> ACTIVE.  **Returned:** success |
| **target_raid_config**  dictionary | Represents the requested RAID configuration of the node, which will be applied when the Node next transitions through the CLEANING state. Introduced with the cleaning feature.  **Returned:** success |
| **traits**  list / elements=string | List of traits for this node.  **Returned:** success |
| **updated_at**  string | TODO  **Returned:** success |
| **vendor_interface**  string | Interface for vendor-specific functionality on this node, e.g. “no-vendor”.  **Returned:** success |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
