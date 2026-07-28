---
collection: ansible
version: "8"
title: "openstack.cloud.baremetal_node module – Create/Delete Bare Metal Resources from OpenStack"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/baremetal_node_module.html
fetched_at: 2026-07-28T02:47:25+00:00
---
# openstack.cloud.baremetal_node module – Create/Delete Bare Metal Resources from OpenStack

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
> see [Requirements](baremetal_node_module.md#ansible-collections-openstack-cloud-baremetal-node-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.baremetal_node`.

- [Synopsis](baremetal_node_module.md#synopsis)
- [Requirements](baremetal_node_module.md#requirements)
- [Parameters](baremetal_node_module.md#parameters)
- [Notes](baremetal_node_module.md#notes)
- [Examples](baremetal_node_module.md#examples)
- [Return Values](baremetal_node_module.md#return-values)

## [Synopsis](baremetal_node_module.md#id1)

- Create or Remove Ironic nodes from OpenStack.

## [Requirements](baremetal_node_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](baremetal_node_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **bios_interface**  string | The bios interface for this node, e.g. `no-bios`. |
| **boot_interface**  string | The boot interface for this node, e.g. `pxe`. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **chassis_id**  aliases: chassis_uuid  string | Associate the node with a pre-defined chassis. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **console_interface**  string | The console interface for this node, e.g. `no-console`. |
| **deploy_interface**  string | The deploy interface for this node, e.g. `iscsi`. |
| **driver**  string | The name of the Ironic Driver to use with this node.  Required when *state* is `present` |
| **driver_info**  dictionary / required | Information for this node’s driver. Will vary based on which driver is in use. Any sub-field which is populated will be validated during creation. For compatibility reasons sub-fields `power`, `deploy`, `management` and `console` are flattened. |
| **id**  aliases: uuid  string | ID to be given to the baremetal node. Will be auto-generated on creation if not specified, and *name* is specified.  Definition of *id* will always take precedence over *name*. |
| **inspect_interface**  string | The interface used for node inspection, e.g. `no-inspect`. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **management_interface**  string | The interface for out-of-band management of this node, e.g. “ipmitool”. |
| **name**  string | unique name identifier to be given to the resource. |
| **network_interface**  string | The network interface provider to use when describing connections for this node. |
| **nics**  list / elements=dictionary / required | A list of network interface cards, eg,  `- mac: aa:bb:cc:aa:bb:cc`  This node attribute cannot be updated. |
| **mac**  string / required | The MAC address of the network interface card. |
| **power_interface**  string | The interface used to manage power actions on this node, e.g. `ipmitool`. |
| **properties**  dictionary | Definition of the physical characteristics of this node  Used for scheduling purposes |
| **capabilities**  string | Special capabilities for this node such as boot_option etc.  For more information refer to <https://docs.openstack.org/ironic/latest/install/advanced.html>. |
| **cpu_arch**  string | CPU architecture (x86_64, i686, …) |
| **cpus**  string | Number of CPU cores this machine has |
| **local_gb**  aliases: disk_size  string | Size in GB of first storage device in this machine (typically /dev/sda) |
| **memory_mb**  aliases: ram  string | Amount of RAM in MB this machine has |
| **root_device**  dictionary | Root disk device hints for deployment.  For allowed hints refer to <https://docs.openstack.org/ironic/latest/install/advanced.html>. |
| **raid_interface**  string | Interface used for configuring raid on this node. |
| **region_name**  string | Name of the region. |
| **rescue_interface**  string | Interface used for node rescue, e.g. `no-rescue`. |
| **resource_class**  string | The specific resource type to which this node belongs. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **skip_update_of_masked_password**  boolean | Deprecated, no longer used.  Updating or specifing a password has not been supported for a while.  **Choices:**   - `false` - `true` |
| **state**  string | Indicates desired state of the resource  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **storage_interface**  string | Interface used for attaching and detaching volumes on this node, e.g. `cinder`. |
| **timeout**  integer | Number of seconds to wait for the newly created node to reach the available state.  **Default:** `1800` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **vendor_interface**  string | Interface for all vendor-specific actions on this node, e.g. `no-vendor`. |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](baremetal_node_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](baremetal_node_module.md#id5)

```yaml+jinja
- name: Enroll a node with some basic properties and driver info
  openstack.cloud.baremetal_node:
    chassis_id: "00000000-0000-0000-0000-000000000001"
    cloud: "devstack"
    driver: "pxe_ipmitool"
    driver_info:
      ipmi_address: "1.2.3.4"
      ipmi_username: "admin"
      ipmi_password: "adminpass"
    id: "00000000-0000-0000-0000-000000000002"
    nics:
      - mac: "aa:bb:cc:aa:bb:cc"
      - mac: "dd:ee:ff:dd:ee:ff"
    properties:
      capabilities: "boot_option:local"
      cpu_arch: "x86_64"
      cpus: 2
      local_gb: 64
      memory_mb: 8192
      root_device:
        wwn: "0x4000cca77fc4dba1"
```

## [Return Values](baremetal_node_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **node**  dictionary | Dictionary describing the Bare Metal node.  **Returned:** On success when *state* is ‘present’. |
| **allocation_id**  string | The UUID of the allocation associated with the node. If not null, will be the same as instance_id (the opposite is not always true). Unlike instance_id, this field is read-only. Please use the Allocation API to remove allocations.  **Returned:** success |
| **bios_interface**  string | The bios interface to be used for this node.  **Returned:** success |
| **boot_interface**  string | The boot interface for a node, e.g. “pxe”.  **Returned:** success |
| **boot_mode**  string | The boot mode for a node, either “uefi” or “bios”  **Returned:** success |
| **chassis_id**  string | UUID of the chassis associated with this node. May be empty or None.  **Returned:** success |
| **clean_step**  string | The current clean step.  **Returned:** success |
| **conductor**  string | The conductor currently servicing a node.  **Returned:** success |
| **conductor_group**  string | The conductor group for a node.  **Returned:** success |
| **console_interface**  string | The console interface for a node, e.g. “no-console”.  **Returned:** success |
| **created_at**  string | Bare Metal node created at timestamp.  **Returned:** success |
| **deploy_interface**  string | The deploy interface for a node, e.g. “direct”.  **Returned:** success |
| **deploy_step**  string | The current deploy step.  **Returned:** success |
| **driver**  string | The name of the driver.  **Returned:** success |
| **driver_info**  dictionary | All the metadata required by the driver to manage this node. List of fields varies between drivers, and can be retrieved from the /v1/drivers/<DRIVER_NAME>/properties resource.  **Returned:** success |
| **driver_internal_info**  dictionary | Internal metadata set and stored by the node’s driver.  **Returned:** success |
| **extra**  dictionary | A set of one or more arbitrary metadata key and value pairs.  **Returned:** success |
| **fault**  string | The fault indicates the active fault detected by ironic, typically the node is in “maintenance mode”. None means no fault has been detected by ironic. “power failure” indicates ironic failed to retrieve power state from this node. There are other possible types, e.g., “clean failure” and “rescue abort failure”.  **Returned:** success |
| **id**  string | The UUID for the resource.  **Returned:** success |
| **inspect_interface**  string | The interface used for node inspection.  **Returned:** success |
| **instance_id**  string | UUID of the Nova instance associated with this node.  **Returned:** success |
| **instance_info**  dictionary | Information used to customize the deployed image. May include root partition size, a base 64 encoded config drive, and other metadata. Note that this field is erased automatically when the instance is deleted (this is done by requesting the node provision state be changed to DELETED).  **Returned:** success |
| **is_automated_clean_enabled**  boolean | Indicates whether the node will perform automated clean or not.  **Returned:** success |
| **is_console_enabled**  boolean | Indicates whether console access is enabled or disabled on this node.  **Returned:** success |
| **is_maintenance**  boolean | Whether or not this node is currently in “maintenance mode”. Setting a node into maintenance mode removes it from the available resource pool and halts some internal automation. This can happen manually (eg, via an API request) or automatically when Ironic detects a hardware fault that prevents communication with the machine.  **Returned:** success |
| **is_protected**  boolean | Whether the node is protected from undeploying, rebuilding and deletion.  **Returned:** success |
| **is_retired**  boolean | Whether the node is retired and can hence no longer be provided, i.e. move from manageable to available, and will end up in manageable after cleaning (rather than available).  **Returned:** success |
| **is_secure_boot**  boolean | Indicates whether node is currently booted with secure_boot turned on.  **Returned:** success |
| **last_error**  string | Any error from the most recent (last) transaction that started but failed to finish.  **Returned:** success |
| **links**  list / elements=string | A list of relative links, including self and bookmark links.  **Returned:** success |
| **maintenance_reason**  string | User-settable description of the reason why this node was placed into maintenance mode  **Returned:** success |
| **management_interface**  string | Interface for out-of-band node management.  **Returned:** success |
| **name**  string | Human-readable identifier for the node resource. May be undefined. Certain words are reserved.  **Returned:** success |
| **network_interface**  string | Which Network Interface provider to use when plumbing the network connections for this node.  **Returned:** success |
| **owner**  string | A string or UUID of the tenant who owns the object.  **Returned:** success |
| **port_groups**  list / elements=string | List of ironic port groups on this node.  **Returned:** success |
| **ports**  list / elements=string | List of ironic ports on this node.  **Returned:** success |
| **power_interface**  string | Interface used for performing power actions on the node, e.g. “ipmitool”.  **Returned:** success |
| **power_state**  string | The current power state of this node. Usually, “power on” or “power off”, but may be “None” if Ironic is unable to determine the power state (eg, due to hardware failure).  **Returned:** success |
| **properties**  dictionary | Physical characteristics of this node. Populated by ironic-inspector during inspection. May be edited via the REST API at any time.  **Returned:** success |
| **protected_reason**  string | The reason the node is marked as protected.  **Returned:** success |
| **provision_state**  string | The current provisioning state of this node.  **Returned:** success |
| **raid_config**  dictionary | Represents the current RAID configuration of the node. Introduced with the cleaning feature.  **Returned:** success |
| **raid_interface**  string | Interface used for configuring RAID on this node.  **Returned:** success |
| **rescue_interface**  string | The interface used for node rescue, e.g. “no-rescue”.  **Returned:** success |
| **reservation**  string | The name of an Ironic Conductor host which is holding a lock on this node, if a lock is held. Usually “null”, but this field can be useful for debugging.  **Returned:** success |
| **resource_class**  string | A string which can be used by external schedulers to identify this node as a unit of a specific type of resource. For more details, see <https://docs.openstack.org/ironic/latest/install/configure-nova-flavors.html>  **Returned:** success |
| **retired_reason**  string | The reason the node is marked as retired.  **Returned:** success |
| **states**  list / elements=string | Links to the collection of states.  **Returned:** success |
| **storage_interface**  string | Interface used for attaching and detaching volumes on this node, e.g. “cinder”.  **Returned:** success |
| **target_power_state**  string | If a power state transition has been requested, this field represents the requested (ie, “target”) state, either “power on” or “power off”.  **Returned:** success |
| **target_provision_state**  string | If a provisioning action has been requested, this field represents the requested (ie, “target”) state. Note that a node may go through several states during its transition to this target state. For instance, when requesting an instance be deployed to an AVAILABLE node, the node may go through the following state change progression, AVAILABLE -> DEPLOYING -> DEPLOYWAIT -> DEPLOYING -> ACTIVE  **Returned:** success |
| **target_raid_config**  dictionary | Represents the requested RAID configuration of the node, which will be applied when the node next transitions through the CLEANING state. Introduced with the cleaning feature.  **Returned:** success |
| **traits**  list / elements=string | List of traits for this node.  **Returned:** success |
| **updated_at**  string | Bare Metal node updated at timestamp.  **Returned:** success |
| **vendor_interface**  string | Interface for vendor-specific functionality on this node, e.g. “no-vendor”.  **Returned:** success |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
