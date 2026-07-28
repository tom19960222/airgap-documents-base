---
collection: ansible
version: "6"
title: "openstack.cloud.server_action module – Perform actions on Compute Instances from OpenStack"
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/server_action_module.html
fetched_at: 2026-07-28T00:17:06+00:00
---
# openstack.cloud.server_action module – Perform actions on Compute Instances from OpenStack

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
> see [Requirements](server_action_module.md#ansible-collections-openstack-cloud-server-action-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.server_action`.

- [Synopsis](server_action_module.md#synopsis)
- [Requirements](server_action_module.md#requirements)
- [Parameters](server_action_module.md#parameters)
- [Notes](server_action_module.md#notes)
- [Examples](server_action_module.md#examples)

## [Synopsis](server_action_module.md#id1)

- Perform server actions on an existing compute instance from OpenStack. This module does not return any data other than changed true/false. When *action* is ‘rebuild’, then *image* parameter is required.

## [Requirements](server_action_module.md#id2)

The below requirements are needed on the host that executes this module.

- openstacksdk
- openstacksdk >= 0.36, < 0.99.0
- python >= 3.6

## [Parameters](server_action_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **action**  string / required | Perform the given action. The lock and unlock actions always return changed as the servers API does not provide lock status.  Choices:   - `"stop"` - `"start"` - `"pause"` - `"unpause"` - `"lock"` - `"unlock"` - `"suspend"` - `"resume"` - `"rebuild"` - `"shelve"` - `"shelve_offload"` - `"unshelve"` |
| **admin_password**  string | Admin password for server to rebuild |
| **all_projects**  boolean | Whether to search for server in all projects or just the current auth scoped project.  Choices:   - `false` ← (default) - `true` |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **availability_zone**  string | Ignored. Present for backwards compatibility |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **image**  string | Image the server should be rebuilt with |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  Choices:   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  Choices:   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **server**  string / required | Name or ID of the instance |
| **timeout**  integer | The amount of time the module should wait for the instance to perform the requested action.  Default: `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `yes`.  Choices:   - `false` - `true` |
| **wait**  boolean | If the module should wait for the instance action to be performed.  Choices:   - `false` - `true` ← (default) |

## [Notes](server_action_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](server_action_module.md#id5)

```yaml+jinja
# Pauses a compute instance
- openstack.cloud.server_action:
      action: pause
      auth:
        auth_url: https://identity.example.com
        username: admin
        password: admin
        project_name: admin
      server: vm1
      timeout: 200
```

### Authors

- OpenStack Ansible SIG

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
