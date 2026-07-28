---
collection: ansible
version: "8"
title: "openstack.cloud.address_scope module – Create or delete address scopes from OpenStack"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/address_scope_module.html
fetched_at: 2026-07-28T02:47:20+00:00
---
# openstack.cloud.address_scope module – Create or delete address scopes from OpenStack

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
> see [Requirements](address_scope_module.md#ansible-collections-openstack-cloud-address-scope-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.address_scope`.

- [Synopsis](address_scope_module.md#synopsis)
- [Requirements](address_scope_module.md#requirements)
- [Parameters](address_scope_module.md#parameters)
- [Notes](address_scope_module.md#notes)
- [Examples](address_scope_module.md#examples)
- [Return Values](address_scope_module.md#return-values)

## [Synopsis](address_scope_module.md#id1)

- Create or Delete address scopes from OpenStack.

## [Requirements](address_scope_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](address_scope_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **extra_specs**  dictionary | Dictionary with extra key/value pairs passed to the API  **Default:** `{}` |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **ip_version**  string | The IP version of the subnet 4 or 6.  This option cannot be updated.  **Choices:**   - `"4"` ← (default) - `"6"` |
| **is_shared**  aliases: shared  boolean | Whether this address scope is shared or not.  **Choices:**   - `false` ← (default) - `true` |
| **name**  string / required | Name to be give to the address scope  This option cannot be updated. |
| **project**  string | Unique name or ID of the project.  This option cannot be updated. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Indicate desired state of the resource  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](address_scope_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](address_scope_module.md#id5)

```yaml+jinja
# Create an IPv4 address scope.
- openstack.cloud.address_scope:
    cloud: mycloud
    state: present
    name: my_adress_scope

# Create a shared IPv6 address scope for a given project.
- openstack.cloud.address_scope:
    cloud: mycloud
    state: present
    ip_version: 6
    name: ipv6_address_scope
    project: myproj

# Delete address scope.
- openstack.cloud.address_scope:
    cloud: mycloud
    state: absent
    name: my_adress_scope
```

## [Return Values](address_scope_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **address_scope**  dictionary | Dictionary describing the address scope.  **Returned:** On success when *state* is ‘present’ |
| **id**  string | Address Scope ID.  **Returned:** success  **Sample:** `"474acfe5-be34-494c-b339-50f06aa143e4"` |
| **ip_version**  string | The IP version of the subnet 4 or 6.  **Returned:** success  **Sample:** `"4"` |
| **is_shared**  boolean | Indicates whether this address scope is shared across all tenants.  **Returned:** success  **Sample:** `false` |
| **name**  string | Address Scope name.  **Returned:** success  **Sample:** `"my_address_scope"` |
| **project_id**  string | The project ID  **Returned:** success  **Sample:** `"474acfe5-be34-494c-b339-50f06aa143e4"` |
| **tenant_id**  string | The tenant ID.  **Returned:** success  **Sample:** `"861174b82b43463c9edc5202aadc60ef"` |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
