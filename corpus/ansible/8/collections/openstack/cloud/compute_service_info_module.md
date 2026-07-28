---
collection: ansible
version: "8"
title: "openstack.cloud.compute_service_info module – Fetch OpenStack Compute (Nova) services"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/compute_service_info_module.html
fetched_at: 2026-07-28T02:47:36+00:00
---
# openstack.cloud.compute_service_info module – Fetch OpenStack Compute (Nova) services

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
> see [Requirements](compute_service_info_module.md#ansible-collections-openstack-cloud-compute-service-info-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.compute_service_info`.

- [Synopsis](compute_service_info_module.md#synopsis)
- [Requirements](compute_service_info_module.md#requirements)
- [Parameters](compute_service_info_module.md#parameters)
- [Notes](compute_service_info_module.md#notes)
- [Examples](compute_service_info_module.md#examples)
- [Return Values](compute_service_info_module.md#return-values)

## [Synopsis](compute_service_info_module.md#id1)

- Fetch OpenStack Compute (Nova) services.

## [Requirements](compute_service_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](compute_service_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **binary**  string | Filter the service list result by binary name of the service. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **host**  string | Filter the service list result by the host name. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](compute_service_info_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](compute_service_info_module.md#id5)

```yaml+jinja
- name: Fetch all OpenStack Compute (Nova) services
  openstack.cloud.compute_service_info:
    cloud: awesomecloud

- name: Fetch a subset of OpenStack Compute (Nova) services
  openstack.cloud.compute_service_info:
    cloud: awesomecloud
    binary: "nova-compute"
    host: "localhost"
```

## [Return Values](compute_service_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **compute_services**  list / elements=dictionary | List of dictionaries describing Compute (Nova) services.  **Returned:** always |
| **availability_zone**  string | The availability zone name.  **Returned:** success |
| **binary**  string | The binary name of the service.  **Returned:** success |
| **disabled_reason**  string | The reason why the service is disabled  **Returned:** success |
| **host**  string | The name of the host.  **Returned:** success |
| **id**  string | Unique UUID.  **Returned:** success |
| **is_forced_down**  boolean | If the service has been forced down or nova-compute  **Returned:** success |
| **name**  string | Service name  **Returned:** success |
| **state**  string | The state of the service. One of up or down.  **Returned:** success |
| **status**  string | The status of the service. One of enabled or disabled.  **Returned:** success |
| **update_at**  string | The date and time when the resource was updated  **Returned:** success |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
