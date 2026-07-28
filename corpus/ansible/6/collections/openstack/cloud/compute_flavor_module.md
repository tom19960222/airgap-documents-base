---
collection: ansible
version: "6"
title: "openstack.cloud.compute_flavor module – Manage OpenStack compute flavors"
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/compute_flavor_module.html
fetched_at: 2026-07-28T00:16:27+00:00
---
# openstack.cloud.compute_flavor module – Manage OpenStack compute flavors

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
> see [Requirements](compute_flavor_module.md#ansible-collections-openstack-cloud-compute-flavor-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.compute_flavor`.

- [Synopsis](compute_flavor_module.md#synopsis)
- [Requirements](compute_flavor_module.md#requirements)
- [Parameters](compute_flavor_module.md#parameters)
- [Notes](compute_flavor_module.md#notes)
- [Examples](compute_flavor_module.md#examples)
- [Return Values](compute_flavor_module.md#return-values)

## [Synopsis](compute_flavor_module.md#id1)

- Add or remove flavors from OpenStack.

## [Requirements](compute_flavor_module.md#id2)

The below requirements are needed on the host that executes this module.

- openstacksdk
- openstacksdk >= 0.36, < 0.99.0
- python >= 3.6

## [Parameters](compute_flavor_module.md#id3)

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
| **disk**  integer | Size of local disk, in GB.  Default: `0` |
| **ephemeral**  integer | Ephemeral space size, in GB.  Default: `0` |
| **extra_specs**  dictionary | Metadata dictionary |
| **flavorid**  string | ID for the flavor. This is optional as a unique UUID will be assigned if a value is not specified.  Default: `"auto"` |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  Choices:   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **is_public**  boolean | Make flavor accessible to the public.  Choices:   - `false` - `true` ← (default) |
| **name**  string / required | Flavor name. |
| **ram**  integer | Amount of memory, in MB. |
| **region_name**  string | Name of the region. |
| **rxtx_factor**  float | RX/TX factor.  Default: `1.0` |
| **sdk_log_level**  string | Log level of the OpenStackSDK  Choices:   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Indicate desired state of the resource. When *state* is ‘present’, then *ram*, *vcpus*, and *disk* are all required. There are no default values for those parameters.  Choices:   - `"present"` ← (default) - `"absent"` |
| **swap**  integer | Swap space size, in MB.  Default: `0` |
| **timeout**  integer | How long should ansible wait for the requested resource.  Default: `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `yes`.  Choices:   - `false` - `true` |
| **vcpus**  integer | Number of virtual CPUs. |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  Choices:   - `false` - `true` ← (default) |

## [Notes](compute_flavor_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](compute_flavor_module.md#id5)

```yaml+jinja
- name: "Create 'tiny' flavor with 1024MB of RAM, 1 virtual CPU, and 10GB of local disk, and 10GB of ephemeral."
  openstack.cloud.compute_flavor:
    cloud: mycloud
    state: present
    name: tiny
    ram: 1024
    vcpus: 1
    disk: 10
    ephemeral: 10

- name: "Delete 'tiny' flavor"
  openstack.cloud.compute_flavor:
    cloud: mycloud
    state: absent
    name: tiny

- name: Create flavor with metadata
  openstack.cloud.compute_flavor:
    cloud: mycloud
    state: present
    name: tiny
    ram: 1024
    vcpus: 1
    disk: 10
    extra_specs:
      "quota:disk_read_iops_sec": 5000
      "aggregate_instance_extra_specs:pinned": false
```

## [Return Values](compute_flavor_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **flavor**  complex | Dictionary describing the flavor.  Returned: On success when *state* is ‘present’ |
| **disk**  integer | Size of local disk, in GB.  Returned: success  Sample: `10` |
| **ephemeral**  integer | Ephemeral space size, in GB.  Returned: success  Sample: `10` |
| **extra_specs**  dictionary | Flavor metadata  Returned: success  Sample: `{"aggregate_instance_extra_specs:pinned": false, "quota:disk_read_iops_sec": 5000}` |
| **id**  string | Flavor ID.  Returned: success  Sample: `"515256b8-7027-4d73-aa54-4e30a4a4a339"` |
| **is_public**  boolean | Make flavor accessible to the public.  Returned: success  Sample: `true` |
| **name**  string | Flavor name.  Returned: success  Sample: `"tiny"` |
| **ram**  integer | Amount of memory, in MB.  Returned: success  Sample: `1024` |
| **swap**  integer | Swap space size, in MB.  Returned: success  Sample: `100` |
| **vcpus**  integer | Number of virtual CPUs.  Returned: success  Sample: `2` |

### Authors

- OpenStack Ansible SIG

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
