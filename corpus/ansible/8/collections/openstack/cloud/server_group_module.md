---
collection: ansible
version: "8"
title: "openstack.cloud.server_group module – Manage OpenStack server groups"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/server_group_module.html
fetched_at: 2026-07-28T02:48:49+00:00
---
# openstack.cloud.server_group module – Manage OpenStack server groups

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
> see [Requirements](server_group_module.md#ansible-collections-openstack-cloud-server-group-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.server_group`.

- [Synopsis](server_group_module.md#synopsis)
- [Requirements](server_group_module.md#requirements)
- [Parameters](server_group_module.md#parameters)
- [Notes](server_group_module.md#notes)
- [Examples](server_group_module.md#examples)
- [Return Values](server_group_module.md#return-values)

## [Synopsis](server_group_module.md#id1)

- Add or remove server groups from OpenStack.

## [Requirements](server_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](server_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **name**  string / required | Server group name. |
| **policy**  string | Represents the current name of the policy.  **Choices:**   - `"anti-affinity"` - `"affinity"` - `"soft-anti-affinity"` - `"soft-affinity"` |
| **region_name**  string | Name of the region. |
| **rules**  dictionary | Rules to be applied to the policy. Currently, only the `max_server_per_host` rule is supported for the `anti-affinity` policy. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Indicate desired state of the resource. When *state* is `present`, then *policy* is required.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](server_group_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](server_group_module.md#id5)

```yaml+jinja
- name: Create a server group with 'affinity' policy.
  openstack.cloud.server_group:
    cloud: "{{ cloud }}"
    state: present
    name: my_server_group
    policy: affinity

- name: Delete 'my_server_group' server group.
  openstack.cloud.server_group:
    cloud: "{{ cloud }}"
    state: absent
    name: my_server_group
```

## [Return Values](server_group_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **server_group**  dictionary | Object representing the server group  **Returned:** On success when *state* is present |
| **id**  string | Unique UUID.  **Returned:** always |
| **member_ids**  list / elements=string | The list of members in the server group  **Returned:** always |
| **metadata**  dictionary | Metadata key and value pairs.  **Returned:** always |
| **name**  string | The name of the server group.  **Returned:** always |
| **policies**  list / elements=string | A list of exactly one policy name to associate with the group. Available until microversion 2.63  **Returned:** always |
| **policy**  string | Represents the name of the policy. Available from version 2.64 on.  **Returned:** always |
| **project_id**  string | The project ID who owns the server group.  **Returned:** always |
| **rules**  dictionary | The rules field, applied to the policy. Currently, only the `max_server_per_host` rule is supported for the `anti-affinity` policy.  **Returned:** always |
| **user_id**  string | The user ID who owns the server group.  **Returned:** always |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
