---
collection: ansible
version: "6"
title: "openstack.cloud.security_group_info module – Lists security groups"
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/security_group_info_module.html
fetched_at: 2026-07-28T00:17:03+00:00
---
# openstack.cloud.security_group_info module – Lists security groups

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
> see [Requirements](security_group_info_module.md#ansible-collections-openstack-cloud-security-group-info-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.security_group_info`.

- [Synopsis](security_group_info_module.md#synopsis)
- [Requirements](security_group_info_module.md#requirements)
- [Parameters](security_group_info_module.md#parameters)
- [Notes](security_group_info_module.md#notes)
- [Examples](security_group_info_module.md#examples)
- [Return Values](security_group_info_module.md#return-values)

## [Synopsis](security_group_info_module.md#id1)

- List security groups

## [Requirements](security_group_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- openstacksdk
- openstacksdk >= 0.36, < 0.99.0
- python >= 3.6

## [Parameters](security_group_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **any_tags**  list / elements=string | A list of tags to filter the list result by.  Resources that match any tag in this list will be returned. |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **availability_zone**  string | Ignored. Present for backwards compatibility |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **description**  string | Description of the security group |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  Choices:   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **name**  string | Name or id of the security group. |
| **not_any_tags**  list / elements=string | A list of tags to filter the list result by.  Resources that match any tag in this list will be excluded. |
| **not_tags**  list / elements=string | A list of tags to filter the list result by.  Resources that match all tags in this list will be excluded. |
| **project_id**  string | Specifies the project id as filter criteria |
| **region_name**  string | Name of the region. |
| **revision_number**  integer | Filter the list result by the revision number of the  resource. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  Choices:   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **tags**  list / elements=string | A list of tags to filter the list result by.  Resources that match all tags in this list will be returned. |
| **timeout**  integer | How long should ansible wait for the requested resource.  Default: `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `yes`.  Choices:   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  Choices:   - `false` - `true` ← (default) |

## [Notes](security_group_info_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](security_group_info_module.md#id5)

```yaml+jinja
# Get specific security group
- openstack.cloud.security_group_info:
    cloud: "{{ cloud }}"
    name: "{{ my_sg }}"
  register: sg
# Get all security groups
- openstack.cloud.security_group_info:
    cloud: "{{ cloud }}"
  register: sg
```

## [Return Values](security_group_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **security_groups**  complex | List of dictionaries describing security groups.  Returned: On Success. |
| **created_at**  string | Creation time of the security group  Returned: success  Sample: `"yyyy-mm-dd hh:mm:ss"` |
| **description**  string | Description of the security group  Returned: success  Sample: `"My security group"` |
| **id**  string | ID of the security group  Returned: success  Sample: `"d90e55ba-23bd-4d97-b722-8cb6fb485d69"` |
| **name**  string | Name of the security group.  Returned: success  Sample: `"my-sg"` |
| **project_id**  string | Project ID where the security group is located in.  Returned: success  Sample: `"25d24fc8-d019-4a34-9fff-0a09fde6a567"` |
| **security_group_rules**  list / elements=string | Specifies the security group rule list  Returned: success  Sample: `[{"description": null, "direction": "ingress", "ethertype": "IPv4", "id": "d90e55ba-23bd-4d97-b722-8cb6fb485d69", "port_range_max": null, "port_range_min": null, "protocol": null, "remote_group_id": "0431c9c5-1660-42e0-8a00-134bec7f03e2", "remote_ip_prefix": null, "security_group_id": "0431c9c5-1660-42e0-8a00-134bec7f03e2", "tenant_id": "bbfe8c41dd034a07bebd592bf03b4b0c"}, {"description": null, "direction": "egress", "ethertype": "IPv4", "id": "aecff4d4-9ce9-489c-86a3-803aedec65f7", "port_range_max": null, "port_range_min": null, "protocol": null, "remote_group_id": null, "remote_ip_prefix": null, "security_group_id": "0431c9c5-1660-42e0-8a00-134bec7f03e2", "tenant_id": "bbfe8c41dd034a07bebd592bf03b4b0c"}]` |
| **updated_at**  string | Update time of the security group  Returned: success  Sample: `"yyyy-mm-dd hh:mm:ss"` |

### Authors

- OpenStack Ansible SIG

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
