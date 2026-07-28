---
collection: ansible
version: "6"
title: "openstack.cloud.project module – Manage OpenStack Projects"
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/project_module.html
fetched_at: 2026-07-28T00:16:57+00:00
---
# openstack.cloud.project module – Manage OpenStack Projects

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
> see [Requirements](project_module.md#ansible-collections-openstack-cloud-project-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.project`.

- [Synopsis](project_module.md#synopsis)
- [Requirements](project_module.md#requirements)
- [Parameters](project_module.md#parameters)
- [Notes](project_module.md#notes)
- [Examples](project_module.md#examples)
- [Return Values](project_module.md#return-values)

## [Synopsis](project_module.md#id1)

- Manage OpenStack Projects. Projects can be created, updated or deleted using this module. A project will be updated if *name* matches an existing project and *state* is present. The value for *name* cannot be updated without deleting and re-creating the project.

## [Requirements](project_module.md#id2)

The below requirements are needed on the host that executes this module.

- openstacksdk
- openstacksdk >= 0.36, < 0.99.0
- python >= 3.6

## [Parameters](project_module.md#id3)

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
| **description**  string | Description for the project |
| **domain_id**  aliases: domain  string | Domain id to create the project in if the cloud supports domains. |
| **enabled**  boolean | Is the project enabled  Choices:   - `false` - `true` ← (default) |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  Choices:   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **name**  string / required | Name for the project |
| **properties**  dictionary | Additional properties to be associated with this project. Requires openstacksdk>0.45. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  Choices:   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Should the resource be present or absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  Default: `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `yes`.  Choices:   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  Choices:   - `false` - `true` ← (default) |

## [Notes](project_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](project_module.md#id5)

```yaml+jinja
# Create a project
- openstack.cloud.project:
    cloud: mycloud
    endpoint_type: admin
    state: present
    name: demoproject
    description: demodescription
    domain_id: demoid
    enabled: True
    properties:
      internal_alias: demo_project

# Delete a project
- openstack.cloud.project:
    cloud: mycloud
    endpoint_type: admin
    state: absent
    name: demoproject
```

## [Return Values](project_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **project**  complex | Dictionary describing the project.  Returned: On success when *state* is ‘present’ |
| **description**  string | Project description  Returned: success  Sample: `"demodescription"` |
| **enabled**  boolean | Boolean to indicate if project is enabled  Returned: success  Sample: `true` |
| **id**  string | Project ID  Returned: success  Sample: `"f59382db809c43139982ca4189404650"` |
| **name**  string | Project name  Returned: success  Sample: `"demoproject"` |

### Authors

- OpenStack Ansible SIG

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
