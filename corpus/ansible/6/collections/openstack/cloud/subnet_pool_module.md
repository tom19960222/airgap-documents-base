---
collection: ansible
version: "6"
title: "openstack.cloud.subnet_pool module – Create or delete subnet pools from OpenStack"
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/subnet_pool_module.html
fetched_at: 2026-07-28T00:17:12+00:00
---
# openstack.cloud.subnet_pool module – Create or delete subnet pools from OpenStack

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
> see [Requirements](subnet_pool_module.md#ansible-collections-openstack-cloud-subnet-pool-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.subnet_pool`.

- [Synopsis](subnet_pool_module.md#synopsis)
- [Requirements](subnet_pool_module.md#requirements)
- [Parameters](subnet_pool_module.md#parameters)
- [Notes](subnet_pool_module.md#notes)
- [Examples](subnet_pool_module.md#examples)
- [Return Values](subnet_pool_module.md#return-values)

## [Synopsis](subnet_pool_module.md#id1)

- Create or Delete subnet pools from OpenStack.

## [Requirements](subnet_pool_module.md#id2)

The below requirements are needed on the host that executes this module.

- openstacksdk
- openstacksdk >= 0.36, < 0.99.0
- python >= 3.6

## [Parameters](subnet_pool_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **address_scope**  string | Set address scope (ID or name) associated with the subnet pool |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **availability_zone**  string | Ignored. Present for backwards compatibility |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **default_prefix_length**  integer | The length of the prefix to allocate when the cidr or prefixlen attributes are omitted when creating a subnet |
| **default_quota**  integer | A per-project quota on the prefix space that can be allocated from the subnet pool for project subnets |
| **description**  string | The subnet pool description |
| **extra_specs**  dictionary | Dictionary with extra key/value pairs passed to the API  Default: `{}` |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  Choices:   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **is_default**  boolean | Whether this subnet pool is by default  Choices:   - `false` ← (default) - `true` |
| **maximum_prefix_length**  integer | The maximum prefix length that can be allocated from the subnet pool. |
| **minimum_prefix_length**  integer | The minimum prefix length that can be allocated from the subnet pool. |
| **name**  string / required | Name to be give to the subnet pool |
| **prefixes**  list / elements=string | Set subnet pool prefixes (in CIDR notation) |
| **project**  string | Unique name or ID of the project. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  Choices:   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **shared**  boolean | Whether this subnet pool is shared or not.  Choices:   - `false` ← (default) - `true` |
| **state**  string | Indicate desired state of the resource  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  Default: `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `yes`.  Choices:   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  Choices:   - `false` - `true` ← (default) |

## [Notes](subnet_pool_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](subnet_pool_module.md#id5)

```yaml+jinja
# Create an subnet pool.
- openstack.cloud.subnet_pool:
    cloud: mycloud
    state: present
    name: my_subnet_pool
    prefixes:
        - 10.10.10.0/24

# Create a subnet pool for a given project.
- openstack.cloud.subnet_pool:
    cloud: mycloud
    state: present
    name: my_subnet_pool
    project: myproj
    prefixes:
        - 10.10.10.0/24

# Create a shared and default subnet pool in existing address scope
- openstack.cloud.subnet_pool:
    cloud: mycloud
    state: present
    name: my_subnet_pool
    address_scope: my_adress_scope
    is_default: True
    default_quota: 10
    maximum_prefix_length: 32
    minimum_prefix_length: 8
    default_prefix_length: 24
    shared: True
    prefixes:
        - 10.10.10.0/8

# Delete subnet poool.
- openstack.cloud.subnet_pool:
    cloud: mycloud
    state: absent
    name: my_subnet_pool
```

## [Return Values](subnet_pool_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **subnet_pool**  complex | Dictionary describing the subnet pool.  Returned: On success when *state* is ‘present’ |
| **address_scope_id**  string | The address scope ID.  Returned: success  Sample: `"861174b82b43463c9edc5202aadc60ef"` |
| **created_at**  string | Timestamp when the subnet pool was created.  Returned: success  Sample: `""` |
| **default_prefix_length**  integer | The length of the prefix to allocate when the cidr or prefixlen attributes are omitted when creating a subnet  Returned: success  Sample: `32` |
| **default_quota**  integer | The per-project quota on the prefix space that can be allocated from the subnet pool for project subnets.  Returned: success  Sample: `22` |
| **description**  string | The subnet pool description.  Returned: success  Sample: `"My test subnet pool."` |
| **id**  string | Subnet Pool ID.  Returned: success  Sample: `"474acfe5-be34-494c-b339-50f06aa143e4"` |
| **ip_version**  integer | The IP version of the subnet pool 4 or 6.  Returned: success  Sample: `4` |
| **is_default**  boolean | Indicates whether this is the default subnet pool.  Returned: success  Sample: `false` |
| **is_shared**  boolean | Indicates whether this subnet pool is shared across all projects.  Returned: success  Sample: `false` |
| **maximum_prefix_length**  integer | The maximum prefix length that can be allocated from the subnet pool.  Returned: success  Sample: `22` |
| **minimum_prefix_length**  integer | The minimum prefix length that can be allocated from the subnet pool.  Returned: success  Sample: `8` |
| **name**  string | Subnet Pool name.  Returned: success  Sample: `"my_subnet_pool"` |
| **prefixes**  list / elements=string | A list of subnet prefixes that are assigned to the subnet pool.  Returned: success  Sample: `["10.10.20.0/24", "10.20.10.0/24"]` |
| **project_id**  string | The ID of the project.  Returned: success  Sample: `"861174b82b43463c9edc5202aadc60ef"` |
| **revision_number**  integer | Revision number of the subnet pool.  Returned: success  Sample: `5` |
| **updated_at**  string | Timestamp when the subnet pool was last updated.  Returned: success |

### Authors

- OpenStack Ansible SIG

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
