---
collection: ansible
version: "6"
title: "openstack.cloud.baremetal_node module – Create/Delete Bare Metal Resources from OpenStack"
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/baremetal_node_module.html
fetched_at: 2026-07-28T00:16:20+00:00
---
# openstack.cloud.baremetal_node module – Create/Delete Bare Metal Resources from OpenStack

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
> see [Requirements](baremetal_node_module.md#ansible-collections-openstack-cloud-baremetal-node-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.baremetal_node`.

- [Synopsis](baremetal_node_module.md#synopsis)
- [Requirements](baremetal_node_module.md#requirements)
- [Parameters](baremetal_node_module.md#parameters)
- [Notes](baremetal_node_module.md#notes)
- [Examples](baremetal_node_module.md#examples)

## [Synopsis](baremetal_node_module.md#id1)

- Create or Remove Ironic nodes from OpenStack.

## [Requirements](baremetal_node_module.md#id2)

The below requirements are needed on the host that executes this module.

- jsonpatch
- openstacksdk
- openstacksdk >= 0.36, < 0.99.0
- python >= 3.6

## [Parameters](baremetal_node_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **availability_zone**  string | Ignored. Present for backwards compatibility |
| **bios_interface**  string | The bios interface for this node, e.g. “no-bios”. |
| **boot_interface**  string | The boot interface for this node, e.g. “pxe”. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **chassis_uuid**  string | Associate the node with a pre-defined chassis. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **console_interface**  string | The console interface for this node, e.g. “no-console”. |
| **deploy_interface**  string | The deploy interface for this node, e.g. “iscsi”. |
| **driver**  string | The name of the Ironic Driver to use with this node.  Required when *state=present* |
| **driver_info**  dictionary / required | Information for this server’s driver. Will vary based on which driver is in use. Any sub-field which is populated will be validated during creation. For compatibility reasons sub-fields `power`, `deploy`, `management` and `console` are flattened. |
| **inspect_interface**  string | The interface used for node inspection, e.g. “no-inspect”. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  Choices:   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **ironic_url**  string | If noauth mode is utilized, this is required to be set to the endpoint URL for the Ironic API. Use with “auth” and “auth_type” settings set to None. |
| **management_interface**  string | The interface for out-of-band management of this node, e.g. “ipmitool”. |
| **name**  string | unique name identifier to be given to the resource. |
| **network_interface**  string | The network interface provider to use when describing connections for this node. |
| **nics**  list / elements=dictionary / required | A list of network interface cards, eg, ” - mac: aa:bb:cc:aa:bb:cc” |
| **mac**  string / required | The MAC address of the network interface card. |
| **power_interface**  string | The interface used to manage power actions on this node, e.g. “ipmitool”. |
| **properties**  dictionary | Definition of the physical characteristics of this server, used for scheduling purposes |
| **capabilities**  string | special capabilities for the node, such as boot_option, node_role etc (see <https://docs.openstack.org/ironic/latest/install/advanced.html> for more information)  Default: `""` |
| **cpu_arch**  string | CPU architecture (x86_64, i686, …)  Default: `"x86_64"` |
| **cpus**  string | Number of CPU cores this machine has  Default: `1` |
| **disk_size**  string | size of first storage device in this machine (typically /dev/sda), in GB  Default: `1` |
| **ram**  string | amount of RAM this machine has, in MB  Default: `1` |
| **root_device**  string | Root disk device hints for deployment.  See <https://docs.openstack.org/ironic/latest/install/advanced.html#specifying-the-disk-for-deployment-root-device-hints> for allowed hints.  Default: `""` |
| **raid_interface**  string | Interface used for configuring raid on this node. |
| **region_name**  string | Name of the region. |
| **rescue_interface**  string | Interface used for node rescue, e.g. “no-rescue”. |
| **resource_class**  string | The specific resource type to which this node belongs. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  Choices:   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **skip_update_of_masked_password**  aliases: skip_update_of_driver_password  boolean | Allows the code that would assert changes to nodes to skip the update if the change is a single line consisting of the password field.  As of Kilo, by default, passwords are always masked to API requests, which means the logic as a result always attempts to re-assert the password field.  `skip_update_of_driver_password` is deprecated alias and will be removed in openstack.cloud 2.0.0.  Choices:   - `false` - `true` |
| **state**  string | Indicates desired state of the resource  Choices:   - `"present"` ← (default) - `"absent"` |
| **storage_interface**  string | Interface used for attaching and detaching volumes on this node, e.g. “cinder”. |
| **timeout**  integer | How long should ansible wait for the requested resource.  Default: `180` |
| **uuid**  string | globally unique identifier (UUID) to be given to the resource. Will be auto-generated if not specified, and name is specified.  Definition of a UUID will always take precedence to a name value. |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `yes`.  Choices:   - `false` - `true` |
| **vendor_interface**  string | Interface for all vendor-specific actions on this node, e.g. “no-vendor”. |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  Choices:   - `false` - `true` ← (default) |

## [Notes](baremetal_node_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](baremetal_node_module.md#id5)

```yaml+jinja
# Enroll a node with some basic properties and driver info
- openstack.cloud.baremetal_node:
    cloud: "devstack"
    driver: "pxe_ipmitool"
    uuid: "00000000-0000-0000-0000-000000000002"
    properties:
      cpus: 2
      cpu_arch: "x86_64"
      ram: 8192
      disk_size: 64
      capabilities: "boot_option:local"
      root_device:
        wwn: "0x4000cca77fc4dba1"
    nics:
      - mac: "aa:bb:cc:aa:bb:cc"
      - mac: "dd:ee:ff:dd:ee:ff"
    driver_info:
      ipmi_address: "1.2.3.4"
      ipmi_username: "admin"
      ipmi_password: "adminpass"
    chassis_uuid: "00000000-0000-0000-0000-000000000001"
```

### Authors

- OpenStack Ansible SIG

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
