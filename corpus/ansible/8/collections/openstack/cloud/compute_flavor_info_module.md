---
collection: ansible
version: "8"
title: "openstack.cloud.compute_flavor_info module – Fetch compute flavors from OpenStack cloud"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/compute_flavor_info_module.html
fetched_at: 2026-07-28T02:47:35+00:00
---
# openstack.cloud.compute_flavor_info module – Fetch compute flavors from OpenStack cloud

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

- Fetch OpenStack compute flavors.

## [Requirements](compute_flavor_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](compute_flavor_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **ephemeral**  string | Filter flavors based on the amount of ephemeral storage.  *ephemeral* supports same format as *ram* option. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **limit**  integer | Limits number of flavors to *limit* results.  By default all matching flavors are returned. |
| **name**  string | Flavor name. |
| **ram**  string | A string used for filtering flavors based on the amount of RAM (in MB) desired. This string accepts the following special values: ‘MIN’ (return flavors with the minimum amount of RAM), and ‘MAX’ (return flavors with the maximum amount of RAM).  A specific amount of RAM may also be specified. Any flavors with this exact amount of RAM will be returned.  A range of acceptable RAM may be given using a special syntax. Simply prefix the amount of RAM with one of these acceptable range values: ‘<’, ‘>’, ‘<=’, ‘>=’. These values represent less than, greater than, less than or equal to, and greater than or equal to, respectively. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **vcpus**  string | Filter flavors based on the number of virtual CPUs.  *vcpus* supports same format as *ram* option. |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](compute_flavor_info_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](compute_flavor_info_module.md#id5)

```yaml+jinja
- name: Gather information about all available flavors
  openstack.cloud.compute_flavor_info:
    cloud: mycloud

- name: Gather information for the flavor named "xlarge-flavor"
  openstack.cloud.compute_flavor_info:
    cloud: mycloud
    name: "xlarge-flavor"

- name: Get all flavors with 512 MB of RAM
  openstack.cloud.compute_flavor_info:
    cloud: mycloud
    ram: "512"

- name: Get all flavors with >= 1024 MB RAM
  openstack.cloud.compute_flavor_info:
    cloud: mycloud
    ram: ">=1024"

- name: Get a single flavor with minimum amount of RAM
  openstack.cloud.compute_flavor_info:
    cloud: mycloud
    ram: "MIN"
    limit: 1

- name: Get all flavors with >=1024 MB RAM and 2 vCPUs
  openstack.cloud.compute_flavor_info:
    cloud: mycloud
    ram: ">=1024"
    vcpus: "2"

- name: Get flavors with >= 1024 MB RAM 2 vCPUs and < 30gb ephemeral storage
  openstack.cloud.compute_flavor_info:
    cloud: mycloud
    ram: ">=1024"
    vcpus: "2"
    ephemeral: "<30"
```

## [Return Values](compute_flavor_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **flavors**  list / elements=dictionary | List of dictionaries describing the compute flavors.  **Returned:** always |
| **description**  string | Description of the flavor  **Returned:** success  **Sample:** `"Small flavor"` |
| **disk**  integer | Size of local disk, in GB.  **Returned:** success  **Sample:** `10` |
| **ephemeral**  integer | Ephemeral space size, in GB.  **Returned:** success  **Sample:** `10` |
| **extra_specs**  dictionary | Optional parameters to configure different flavors options.  **Returned:** success  **Sample:** `{"hw_rng:allowed": true}` |
| **id**  string | Flavor ID.  **Returned:** success  **Sample:** `"515256b8-7027-4d73-aa54-4e30a4a4a339"` |
| **is_disabled**  boolean | Wether the flavor is enabled or not  **Returned:** success  **Sample:** `false` |
| **is_public**  boolean | Make flavor accessible to the public.  **Returned:** success  **Sample:** `true` |
| **name**  string | Flavor name.  **Returned:** success  **Sample:** `"tiny"` |
| **original_name**  string | Original flavor name  **Returned:** success  **Sample:** `"tiny"` |
| **ram**  integer | Amount of memory, in MB.  **Returned:** success  **Sample:** `1024` |
| **rxtx_factor**  float | Factor to be multiplied by the rxtx_base property of the network it is attached to in order to have a different bandwidth cap.  **Returned:** success  **Sample:** `1.0` |
| **swap**  integer | Swap space size, in MB.  **Returned:** success  **Sample:** `100` |
| **vcpus**  integer | Number of virtual CPUs.  **Returned:** success  **Sample:** `2` |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
