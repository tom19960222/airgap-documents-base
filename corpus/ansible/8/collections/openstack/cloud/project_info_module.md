---
collection: ansible
version: "8"
title: "openstack.cloud.project_info module – Retrieve information about one or more OpenStack projects"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/project_info_module.html
fetched_at: 2026-07-28T02:48:31+00:00
---
# openstack.cloud.project_info module – Retrieve information about one or more OpenStack projects

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
> see [Requirements](project_info_module.md#ansible-collections-openstack-cloud-project-info-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.project_info`.

- [Synopsis](project_info_module.md#synopsis)
- [Requirements](project_info_module.md#requirements)
- [Parameters](project_info_module.md#parameters)
- [Notes](project_info_module.md#notes)
- [Examples](project_info_module.md#examples)
- [Return Values](project_info_module.md#return-values)

## [Synopsis](project_info_module.md#id1)

- Retrieve information about a one or more OpenStack projects

## [Requirements](project_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](project_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **domain**  string | Name or ID of the domain containing the project. |
| **filters**  dictionary | A dictionary of meta data to use for filtering projects.  Elements of *filters* are passed as query parameters to OpenStack Identity API. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **name**  string | Name or ID of the project. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](project_info_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](project_info_module.md#id5)

```yaml+jinja
- name: Fetch all Identity (Keystone) projects
  openstack.cloud.project_info:
    cloud: awesomecloud

- name: Fetch all projects with a name
  openstack.cloud.project_info:
    cloud: awesomecloud
    name: demoproject

- name: Fetch all projects with a name in a domain
  openstack.cloud.project_info:
    cloud: awesomecloud
    name: demoproject
    domain: admindomain

- name: Fetch all disabled projects
  openstack.cloud.project_info:
    cloud: awesomecloud
    filters:
      is_enabled: false
```

## [Return Values](project_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **projects**  list / elements=dictionary | List of dictionaries describing Identity (Keystone) projects.  **Returned:** always, but can be empty |
| **description**  string | Project description  **Returned:** success  **Sample:** `"demodescription"` |
| **domain_id**  string | Domain ID to which the project belongs  **Returned:** success  **Sample:** `"default"` |
| **id**  string | Project ID  **Returned:** success  **Sample:** `"f59382db809c43139982ca4189404650"` |
| **is_domain**  boolean | Indicates whether the project also acts as a domain.  **Returned:** success |
| **is_enabled**  boolean | Indicates whether the project is enabled  **Returned:** success |
| **name**  string | Project name  **Returned:** success  **Sample:** `"demoproject"` |
| **options**  dictionary | The resource options for the project  **Returned:** success |
| **parent_id**  string | The ID of the parent of the project  **Returned:** success |
| **tags**  list / elements=string | A list of associated tags  **Returned:** success |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
