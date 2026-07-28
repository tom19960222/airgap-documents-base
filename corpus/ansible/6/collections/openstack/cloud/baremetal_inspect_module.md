---
collection: ansible
version: "6"
title: "openstack.cloud.baremetal_inspect module – Explicitly triggers baremetal node introspection in ironic."
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/baremetal_inspect_module.html
fetched_at: 2026-07-28T00:16:19+00:00
---
# openstack.cloud.baremetal_inspect module – Explicitly triggers baremetal node introspection in ironic.

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
> see [Requirements](baremetal_inspect_module.md#ansible-collections-openstack-cloud-baremetal-inspect-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.baremetal_inspect`.

- [Synopsis](baremetal_inspect_module.md#synopsis)
- [Requirements](baremetal_inspect_module.md#requirements)
- [Parameters](baremetal_inspect_module.md#parameters)
- [Notes](baremetal_inspect_module.md#notes)
- [Examples](baremetal_inspect_module.md#examples)
- [Returned Facts](baremetal_inspect_module.md#returned-facts)

## [Synopsis](baremetal_inspect_module.md#id1)

- Requests Ironic to set a node into inspect state in order to collect metadata regarding the node. This command may be out of band or in-band depending on the ironic driver configuration. This is only possible on nodes in ‘manageable’ and ‘available’ state.

## [Requirements](baremetal_inspect_module.md#id2)

The below requirements are needed on the host that executes this module.

- openstacksdk
- openstacksdk >= 0.36, < 0.99.0
- python >= 3.6

## [Parameters](baremetal_inspect_module.md#id3)

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
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  Choices:   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **ironic_url**  string | If noauth mode is utilized, this is required to be set to the endpoint URL for the Ironic API. Use with “auth” and “auth_type” settings set to None. |
| **mac**  string | unique mac address that is used to attempt to identify the host. |
| **name**  string | unique name identifier to identify the host in Ironic. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  Choices:   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **timeout**  integer | A timeout in seconds to tell the role to wait for the node to complete introspection if wait is set to True.  Default: `1200` |
| **uuid**  string | globally unique identifier (UUID) to identify the host. |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `yes`.  Choices:   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  Choices:   - `false` - `true` ← (default) |

## [Notes](baremetal_inspect_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](baremetal_inspect_module.md#id5)

```yaml+jinja
# Invoke node inspection
- openstack.cloud.baremetal_inspect:
    name: "testnode1"
```

## [Returned Facts](baremetal_inspect_module.md#id6)

Facts returned by this module are added/updated in the `hostvars` host facts and can be referenced by name just like any other host fact. They do not need to be registered in order to use them.

| Key | Description |
| --- | --- |
| **cpu_arch**  string | Detected CPU architecture type  Returned: success  Sample: `"x86_64"` |
| **cpus**  string | Count of cpu cores defined in the updated node properties.  Returned: success  Sample: `"1"` |
| **local_gb**  string | Total size of local disk storage as updated in node properties.  Returned: success  Sample: `"10"` |
| **memory_mb**  string | Amount of node memory as updated in the node properties  Returned: success  Sample: `"1024"` |

### Authors

- OpenStack Ansible SIG

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
