---
collection: ansible
version: "6"
title: "openstack.cloud.compute_flavor_info module – Retrieve information about one or more flavors"
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/compute_flavor_info_module.html
fetched_at: 2026-07-28T00:16:28+00:00
---
# openstack.cloud.compute_flavor_info module – Retrieve information about one or more flavors

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
> see [Requirements](compute_flavor_info_module.md#ansible-collections-openstack-cloud-compute-flavor-info-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.compute_flavor_info`.

- [Synopsis](compute_flavor_info_module.md#synopsis)
- [Requirements](compute_flavor_info_module.md#requirements)
- [Parameters](compute_flavor_info_module.md#parameters)
- [Notes](compute_flavor_info_module.md#notes)
- [Examples](compute_flavor_info_module.md#examples)
- [Return Values](compute_flavor_info_module.md#return-values)

## [Synopsis](compute_flavor_info_module.md#id1)

- Retrieve information about available OpenStack instance flavors. By default, information about ALL flavors are retrieved. Filters can be applied to get information for only matching flavors. For example, you can filter on the amount of RAM available to the flavor, or the number of virtual CPUs available to the flavor, or both. When specifying multiple filters, \*ALL\* filters must match on a flavor before that flavor is returned as a fact.
- This module was called `openstack.cloud.compute_flavor_facts` before Ansible 2.9, returning `ansible_facts`. Note that the [openstack.cloud.compute_flavor_info](compute_flavor_info_module.md#ansible-collections-openstack-cloud-compute-flavor-info-module) module no longer returns `ansible_facts`!

## [Requirements](compute_flavor_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- openstacksdk
- openstacksdk >= 0.36, < 0.99.0
- python >= 3.6

## [Parameters](compute_flavor_info_module.md#id3)

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
| **ephemeral**  string | A string used for filtering flavors based on the amount of ephemeral storage. Format is the same as the *ram* parameter |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  Choices:   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **limit**  integer | Limits the number of flavors returned. All matching flavors are returned by default. |
| **name**  string | A flavor name. Cannot be used with *ram* or *vcpus* or *ephemeral*. |
| **ram**  string | A string used for filtering flavors based on the amount of RAM (in MB) desired. This string accepts the following special values: ‘MIN’ (return flavors with the minimum amount of RAM), and ‘MAX’ (return flavors with the maximum amount of RAM).  A specific amount of RAM may also be specified. Any flavors with this exact amount of RAM will be returned.  A range of acceptable RAM may be given using a special syntax. Simply prefix the amount of RAM with one of these acceptable range values: ‘<’, ‘>’, ‘<=’, ‘>=’. These values represent less than, greater than, less than or equal to, and greater than or equal to, respectively. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  Choices:   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **timeout**  integer | How long should ansible wait for the requested resource.  Default: `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `yes`.  Choices:   - `false` - `true` |
| **vcpus**  string | A string used for filtering flavors based on the number of virtual CPUs desired. Format is the same as the *ram* parameter. |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  Choices:   - `false` - `true` ← (default) |

## [Notes](compute_flavor_info_module.md#id4)

> **Note:**
>
> - The result contains a list of unsorted flavors.
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](compute_flavor_info_module.md#id5)

```yaml+jinja
# Gather information about all available flavors
- openstack.cloud.compute_flavor_info:
    cloud: mycloud
  register: result

- debug:
    msg: "{{ result.openstack_flavors }}"

# Gather information for the flavor named "xlarge-flavor"
- openstack.cloud.compute_flavor_info:
    cloud: mycloud
    name: "xlarge-flavor"

# Get all flavors that have exactly 512 MB of RAM.
- openstack.cloud.compute_flavor_info:
    cloud: mycloud
    ram: "512"

# Get all flavors that have 1024 MB or more of RAM.
- openstack.cloud.compute_flavor_info:
    cloud: mycloud
    ram: ">=1024"

# Get a single flavor that has the minimum amount of RAM. Using the 'limit'
# option will guarantee only a single flavor is returned.
- openstack.cloud.compute_flavor_info:
    cloud: mycloud
    ram: "MIN"
    limit: 1

# Get all flavors with 1024 MB of RAM or more, AND exactly 2 virtual CPUs.
- openstack.cloud.compute_flavor_info:
    cloud: mycloud
    ram: ">=1024"
    vcpus: "2"

# Get all flavors with 1024 MB of RAM or more, exactly 2 virtual CPUs, and
# less than 30gb of ephemeral storage.
- openstack.cloud.compute_flavor_info:
    cloud: mycloud
    ram: ">=1024"
    vcpus: "2"
    ephemeral: "<30"
```

## [Return Values](compute_flavor_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **openstack_flavors**  complex | Dictionary describing the flavors.  Returned: On success. |
| **description**  string | Description of the flavor  Returned: success  Sample: `"Small flavor"` |
| **disk**  integer | Size of local disk, in GB.  Returned: success  Sample: `10` |
| **ephemeral**  integer | Ephemeral space size, in GB.  Returned: success  Sample: `10` |
| **extra_specs**  dictionary | Optional parameters to configure different flavors options.  Returned: success  Sample: `{"hw_rng:allowed": true}` |
| **id**  string | Flavor ID.  Returned: success  Sample: `"515256b8-7027-4d73-aa54-4e30a4a4a339"` |
| **is_disabled**  boolean | Wether the flavor is enabled or not  Returned: success  Sample: `false` |
| **is_public**  boolean | Make flavor accessible to the public.  Returned: success  Sample: `true` |
| **name**  string | Flavor name.  Returned: success  Sample: `"tiny"` |
| **ram**  integer | Amount of memory, in MB.  Returned: success  Sample: `1024` |
| **rxtx_factor**  float | Factor to be multiplied by the rxtx_base property of the network it is attached to in order to have a different bandwidth cap.  Returned: success  Sample: `1.0` |
| **swap**  integer | Swap space size, in MB.  Returned: success  Sample: `100` |
| **vcpus**  integer | Number of virtual CPUs.  Returned: success  Sample: `2` |

### Authors

- OpenStack Ansible SIG

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
