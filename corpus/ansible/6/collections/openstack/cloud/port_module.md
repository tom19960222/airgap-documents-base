---
collection: ansible
version: "6"
title: "openstack.cloud.port module – Add/Update/Delete ports from an OpenStack cloud."
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/port_module.html
fetched_at: 2026-07-28T00:16:56+00:00
---
# openstack.cloud.port module – Add/Update/Delete ports from an OpenStack cloud.

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

- Add, Update or Remove ports from an OpenStack cloud. A *state* of ‘present’ will ensure the port is created or updated if required.

## [Requirements](port_module.md#id2)

The below requirements are needed on the host that executes this module.

- openstacksdk
- openstacksdk >= 0.36, < 0.99.0
- python >= 3.6

## [Parameters](port_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **admin_state_up**  boolean | Sets admin state.  Choices:   - `false` - `true` |
| **allowed_address_pairs**  list / elements=dictionary | Allowed address pairs list. Allowed address pairs are supported with dictionary structure. e.g. allowed_address_pairs: - ip_address: 10.1.0.12 mac_address: ab:cd:ef:12:34:56 - ip_address: … |
| **ip_address**  string | The IP address. |
| **mac_address**  string | The MAC address. |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **availability_zone**  string | Ignored. Present for backwards compatibility |
| **binding_profile**  dictionary | Binding profile dict that the port should be created with. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **device_id**  string | Device ID of device using this port. |
| **device_owner**  string | The ID of the entity that uses this port. |
| **dns_domain**  string | The dns domain of the port ( only with dns-integration enabled ) |
| **dns_name**  string | The dns name of the port ( only with dns-integration enabled ) |
| **extra_dhcp_opts**  list / elements=dictionary | Extra dhcp options to be assigned to this port. Extra options are supported with dictionary structure. Note that options cannot be removed only updated. e.g. extra_dhcp_opts: - opt_name: opt name1 opt_value: value1 ip_version: 4 - opt_name: … |
| **ip_version**  integer / required | The IP version this DHCP option is for. |
| **opt_name**  string / required | The name of the DHCP option to set. |
| **opt_value**  string / required | The value of the DHCP option to set. |
| **fixed_ips**  list / elements=dictionary | Desired IP and/or subnet for this port. Subnet is referenced by subnet_id and IP is referenced by ip_address. |
| **ip_address**  string / required | The fixed IP address to attempt to allocate. |
| **subnet_id**  string | The subnet to attach the IP address to. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  Choices:   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **mac_address**  string | MAC address of this port. |
| **name**  string | Name that has to be given to the port. |
| **network**  string | Network ID or name this port belongs to.  Required when creating a new port. |
| **no_security_groups**  boolean | Do not associate a security group with this port.  Choices:   - `false` ← (default) - `true` |
| **port_security_enabled**  boolean | Whether to enable or disable the port security on the network.  Choices:   - `false` - `true` |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  Choices:   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **security_groups**  list / elements=string | Security group(s) ID(s) or name(s) associated with the port (comma separated string or YAML list) |
| **state**  string | Should the resource be present or absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  Default: `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `yes`.  Choices:   - `false` - `true` |
| **vnic_type**  string | The type of the port that should be created  Choices:   - `"normal"` - `"direct"` - `"direct-physical"` - `"macvtap"` - `"baremetal"` - `"virtio-forwarder"` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  Choices:   - `false` - `true` ← (default) |

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
    vnic_type: direct

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
      "pci_slot": "0000:03:11.1"
      "physical_network": "provider"
```

## [Return Values](port_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **admin_state_up**  boolean | Admin state up flag for this port.  Returned: success |
| **allowed_address_pairs**  list / elements=string | Allowed address pairs with this port.  Returned: success |
| **binding:profile**  dictionary | Port binded profile  Returned: success |
| **fixed_ips**  list / elements=string | Fixed ip(s) associated with this port.  Returned: success |
| **id**  string | Unique UUID.  Returned: success |
| **name**  string | Name given to the port.  Returned: success |
| **network_id**  string | Network ID this port belongs in.  Returned: success |
| **port_security_enabled**  boolean | Port security state on the network.  Returned: success |
| **security_groups**  list / elements=string | Security group(s) associated with this port.  Returned: success |
| **status**  string | Port’s status.  Returned: success |
| **tenant_id**  string | Tenant id associated with this port.  Returned: success |
| **vnic_type**  string | Type of the created port  Returned: success |

### Authors

- OpenStack Ansible SIG

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
