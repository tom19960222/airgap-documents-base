---
collection: ansible
version: "8"
title: "openstack.cloud.baremetal_port module – Create/Delete Bare Metal port Resources from OpenStack"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/baremetal_port_module.html
fetched_at: 2026-07-28T02:47:27+00:00
---
# openstack.cloud.baremetal_port module – Create/Delete Bare Metal port Resources from OpenStack

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
> see [Requirements](baremetal_port_module.md#ansible-collections-openstack-cloud-baremetal-port-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.baremetal_port`.

- [Synopsis](baremetal_port_module.md#synopsis)
- [Requirements](baremetal_port_module.md#requirements)
- [Parameters](baremetal_port_module.md#parameters)
- [Notes](baremetal_port_module.md#notes)
- [Examples](baremetal_port_module.md#examples)
- [Return Values](baremetal_port_module.md#return-values)

## [Synopsis](baremetal_port_module.md#id1)

- Create, Update and Remove ironic ports from OpenStack.

## [Requirements](baremetal_port_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](baremetal_port_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **address**  string | Physical hardware address of this network Port, typically the hardware MAC address. |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **extra**  dictionary | A set of one or more arbitrary metadata key and value pairs. |
| **id**  aliases: uuid  string | ID of the Port.  Will be auto-generated if not specified. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **is_pxe_enabled**  aliases: pxe_enabled  boolean | Whether PXE should be enabled or disabled on the Port.  **Choices:**   - `false` - `true` |
| **local_link_connection**  dictionary | The Port binding profile. |
| **port_id**  string | Identifier of the physical port on the switch to which node’s port is connected to. |
| **switch_id**  string | A MAC address or an OpenFlow based datapath_id of the switch. |
| **switch_info**  string | An optional string field to be used to store any vendor-specific information. |
| **node**  string | ID or Name of the Node this resource belongs to. |
| **physical_network**  string | The name of the physical network to which a port is connected. |
| **port_group**  aliases: portgroup  string | ID or Name of the portgroup this resource belongs to. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Indicates desired state of the resource  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](baremetal_port_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](baremetal_port_module.md#id5)

```yaml+jinja
- name: Create Bare Metal port
  openstack.cloud.baremetal_port:
    cloud: devstack
    state: present
    node: bm-0
    address: fa:16:3e:aa:aa:aa
    is_pxe_enabled: True
    local_link_connection:
      switch_id: 0a:1b:2c:3d:4e:5f
      port_id: Ethernet3/1
      switch_info: switch1
    extra:
      something: extra
    physical_network: datacenter
  register: result

- name: Delete Bare Metal port
  openstack.cloud.baremetal_port:
    cloud: devstack
    state: absent
    address: fa:16:3e:aa:aa:aa
  register: result

- name: Update Bare Metal port
  openstack.cloud.baremetal_port:
    cloud: devstack
    state: present
    id: 1a85ebca-22bf-42eb-ad9e-f640789b8098
    is_pxe_enabled: False
    local_link_connection:
      switch_id: a0:b1:c2:d3:e4:f5
      port_id: Ethernet4/12
      switch_info: switch2
```

## [Return Values](baremetal_port_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **port**  dictionary | A port dictionary, subset of the dictionary keys listed below may be returned, depending on your cloud provider.  **Returned:** success |
| **address**  string | Physical hardware address of this network Port, typically the hardware MAC address.  **Returned:** success |
| **created_at**  string | Bare Metal port created at timestamp.  **Returned:** success |
| **extra**  dictionary | A set of one or more arbitrary metadata key and value pairs.  **Returned:** success |
| **id**  string | The UUID for the Baremetal Port resource.  **Returned:** success |
| **internal_info**  dictionary | Internal metadata set and stored by the Port. This field is read-only.  **Returned:** success |
| **is_pxe_enabled**  boolean | Whether PXE is enabled or disabled on the Port.  **Returned:** success |
| **links**  list / elements=string | A list of relative links, including the self and bookmark links.  **Returned:** success |
| **local_link_connection**  dictionary | The Port binding profile. If specified, must contain switch_id (only a MAC address or an OpenFlow based datapath_id of the switch are accepted in this field and port_id (identifier of the physical port on the switch to which node’s port is connected to) fields. switch_info is an optional string field to be used to store any vendor-specific information.  **Returned:** success |
| **location**  dictionary | Cloud location of this resource (cloud, project, region, zone)  **Returned:** success |
| **name**  string | Bare Metal port name.  **Returned:** success |
| **node_id**  string | UUID of the Bare Metal Node this resource belongs to.  **Returned:** success |
| **physical_network**  string | The name of the physical network to which a port is connected.  **Returned:** success |
| **port_group_id**  string | UUID of the Portgroup this resource belongs to.  **Returned:** success |
| **updated_at**  string | Bare Metal port updated at timestamp.  **Returned:** success |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
