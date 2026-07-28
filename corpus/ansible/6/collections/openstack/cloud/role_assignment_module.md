---
collection: ansible
version: "6"
title: "openstack.cloud.role_assignment module – Associate OpenStack Identity users and roles"
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/role_assignment_module.html
fetched_at: 2026-07-28T00:17:01+00:00
---
# openstack.cloud.role_assignment module – Associate OpenStack Identity users and roles

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
> see [Requirements](role_assignment_module.md#ansible-collections-openstack-cloud-role-assignment-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.role_assignment`.

- [Synopsis](role_assignment_module.md#synopsis)
- [Requirements](role_assignment_module.md#requirements)
- [Parameters](role_assignment_module.md#parameters)
- [Notes](role_assignment_module.md#notes)
- [Examples](role_assignment_module.md#examples)

## [Synopsis](role_assignment_module.md#id1)

- Grant and revoke roles in either project or domain context for OpenStack Identity Users.

## [Requirements](role_assignment_module.md#id2)

The below requirements are needed on the host that executes this module.

- openstacksdk
- openstacksdk >= 0.36, < 0.99.0
- python >= 3.6

## [Parameters](role_assignment_module.md#id3)

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
| **domain**  string | Name or ID of the domain to scope the role association to. Valid only with keystone version 3, and required if *project* is not specified. |
| **group**  string | Name or ID for the group. Valid only with keystone version 3. If *group* is not specified, then *user* is required. Both may not be specified. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  Choices:   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **project**  string | Name or ID of the project to scope the role association to. If you are using keystone version 2, then this value is required. |
| **region_name**  string | Name of the region. |
| **role**  string / required | Name or ID for the role. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  Choices:   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Should the roles be present or absent on the user.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  Default: `180` |
| **user**  string | Name or ID for the user. If *user* is not specified, then *group* is required. Both may not be specified. |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `yes`.  Choices:   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  Choices:   - `false` - `true` ← (default) |

## [Notes](role_assignment_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](role_assignment_module.md#id5)

```yaml+jinja
# Grant an admin role on the user admin in the project project1
- openstack.cloud.role_assignment:
    cloud: mycloud
    user: admin
    role: admin
    project: project1

# Revoke the admin role from the user barney in the newyork domain
- openstack.cloud.role_assignment:
    cloud: mycloud
    state: absent
    user: barney
    role: admin
    domain: newyork
```

### Authors

- OpenStack Ansible SIG

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
