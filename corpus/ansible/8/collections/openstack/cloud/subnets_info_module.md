---
collection: ansible
version: "8"
title: "openstack.cloud.subnets_info module – Retrieve information about one or more OpenStack subnets."
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/subnets_info_module.html
fetched_at: 2026-07-28T02:49:00+00:00
---
# openstack.cloud.subnets_info module – Retrieve information about one or more OpenStack subnets.

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
> see [Requirements](subnets_info_module.md#ansible-collections-openstack-cloud-subnets-info-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.subnets_info`.

- [Synopsis](subnets_info_module.md#synopsis)
- [Requirements](subnets_info_module.md#requirements)
- [Parameters](subnets_info_module.md#parameters)
- [Notes](subnets_info_module.md#notes)
- [Examples](subnets_info_module.md#examples)
- [Return Values](subnets_info_module.md#return-values)

## [Synopsis](subnets_info_module.md#id1)

- Retrieve information about one or more subnets from OpenStack.

## [Requirements](subnets_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](subnets_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **filters**  dictionary | A dictionary of meta data to use for further filtering. Elements of this dictionary may be additional dictionaries. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **name**  aliases: subnet  string | Name or ID of the subnet.  Alias ‘subnet’ added in version 2.8. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](subnets_info_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](subnets_info_module.md#id5)

```yaml+jinja
- name: Gather information about previously created subnets
  openstack.cloud.subnets_info:
    auth:
      auth_url: https://identity.example.com
      username: user
      password: password
      project_name: someproject
  register: result

- name: Show openstack subnets
  debug:
    msg: "{{ result.subnets }}"

- name: Gather information about a previously created subnet by name
  openstack.cloud.subnets_info:
    auth:
      auth_url: https://identity.example.com
      username: user
      password: password
      project_name: someproject
    name: subnet1
  register: result

- name: Show openstack subnets
  debug:
    msg: "{{ result.subnets }}"

- name: Gather information about a previously created subnet with filter
  # Note: name and filters parameters are not mutually exclusive
  openstack.cloud.subnets_info:
    auth:
      auth_url: https://identity.example.com
      username: user
      password: password
      project_name: someproject
    filters:
      project_id: 55e2ce24b2a245b09f181bf025724cbe
  register: result

- name: Show openstack subnets
  debug:
    msg: "{{ result.subnets }}"
```

## [Return Values](subnets_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **subnets**  list / elements=dictionary | has all the openstack information about the subnets  **Returned:** always, but can be empty list |
| **allocation_pools**  list / elements=dictionary | Allocation pools associated with this subnet.  **Returned:** success |
| **cidr**  string | Subnet’s CIDR.  **Returned:** success |
| **created_at**  string | Date and time when the resource was created.  **Returned:** success |
| **description**  string | Description of the subnet.  **Returned:** success |
| **dns_nameservers**  list / elements=string | DNS name servers for this subnet.  **Returned:** success |
| **dns_publish_fixed_ip**  string | Whether to publish DNS records for IPs from this subnet.  **Returned:** success |
| **gateway_ip**  string | Subnet’s gateway ip.  **Returned:** success |
| **host_routes**  list / elements=dictionary | Additional routes for the subnet.  **Returned:** success |
| **id**  string | The ID of the subnet.  **Returned:** success |
| **ip_version**  integer | IP version for this subnet.  **Returned:** success |
| **ipv6_address_mode**  string | The IPv6 address modes specifies mechanisms for assigning IP addresses.  **Returned:** success |
| **ipv6_ra_mode**  string | The IPv6 router advertisement specifies whether the networking service should transmit ICMPv6 packets, for a subnet.  **Returned:** success |
| **is_dhcp_enabled**  boolean | Is DHCP enabled.  **Returned:** success |
| **name**  string | Name given to the subnet.  **Returned:** success |
| **network_id**  string | Network ID this subnet belongs in.  **Returned:** success |
| **prefix_length**  string | The prefix length to use for subnet allocation from a subnet pool.  **Returned:** success |
| **project_id**  string | The ID of the project.  **Returned:** success |
| **revision_number**  string | The revision number of the resource.  **Returned:** success |
| **segment_id**  string | The ID of a network segment the subnet is associated with.  **Returned:** success |
| **service_types**  list / elements=string | The service types associated with the subnet.  **Returned:** success |
| **subnet_pool_id**  string | The ID of the subnet pool associated with the subnet.  **Returned:** success |
| **tags**  list / elements=string | The list of tags on the resource.  **Returned:** success |
| **updated_at**  string | Date and time when the resource was updated.  **Returned:** success |
| **use_default_subnet_pool**  boolean | Whether to use the default subnet pool to obtain a CIDR.  **Returned:** success |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
