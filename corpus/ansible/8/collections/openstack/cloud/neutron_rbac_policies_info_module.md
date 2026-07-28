---
collection: ansible
version: "8"
title: "openstack.cloud.neutron_rbac_policies_info module – Fetch Neutron RBAC policies."
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/neutron_rbac_policies_info_module.html
fetched_at: 2026-07-28T02:48:18+00:00
---
# openstack.cloud.neutron_rbac_policies_info module – Fetch Neutron RBAC policies.

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
> see [Requirements](neutron_rbac_policies_info_module.md#ansible-collections-openstack-cloud-neutron-rbac-policies-info-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.neutron_rbac_policies_info`.

- [Synopsis](neutron_rbac_policies_info_module.md#synopsis)
- [Requirements](neutron_rbac_policies_info_module.md#requirements)
- [Parameters](neutron_rbac_policies_info_module.md#parameters)
- [Notes](neutron_rbac_policies_info_module.md#notes)
- [Examples](neutron_rbac_policies_info_module.md#examples)
- [Return Values](neutron_rbac_policies_info_module.md#return-values)

## [Synopsis](neutron_rbac_policies_info_module.md#id1)

- Fetch RBAC policies against a network, security group or a QoS Policy for one or more projects.

## [Requirements](neutron_rbac_policies_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](neutron_rbac_policies_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **action**  string | Action for the RBAC policy.  Can be either of the following options `access_as_shared` or `access_as_external`.  Logically AND’ed with other filters.  **Choices:**   - `"access_as_shared"` - `"access_as_external"` |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **object_id**  string | The object ID (the subject of the policy) to which the RBAC rules applies.  This is an ID of a network, security group or a qos policy.  Mutually exclusive with the `object_type`. |
| **object_type**  string | Type of the object that this RBAC policy affects.  Can be one of the following object types `network`, `security_group` or `qos_policy`.  Mutually exclusive with the `object_id`.  **Choices:**   - `"network"` - `"security_group"` - `"qos_policy"` |
| **policy_id**  string | The RBAC policy ID.  If `policy_id` is not provided, all available policies will be fetched.  If `policy_id` provided, all other filters are ignored. |
| **project**  aliases: project_id  string | ID or name of the project to which `object_id` belongs to.  Filters the RBAC rules based on the project name.  Logically AND’ed with other filters. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **target_project_id**  string | The ID of the project this RBAC will be enforced.  Filters the RBAC rules based on the target project id.  Logically AND’ed with other filters. |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](neutron_rbac_policies_info_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](neutron_rbac_policies_info_module.md#id5)

```yaml+jinja
- name: Get all rbac policies for a project
  openstack.cloud.neutron_rbac_policies_info:
    project: one_project
```

## [Return Values](neutron_rbac_policies_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **policies**  list / elements=dictionary | Same as `rbac_policies`, kept for backward compatibility.  **Returned:** always |
| **rbac_policies**  list / elements=dictionary | List of Neutron RBAC policies.  **Returned:** always |
| **action**  string | The access model specified by the RBAC rules  **Returned:** success  **Sample:** `"access_as_shared"` |
| **id**  string | The ID of the RBAC rule/policy  **Returned:** success  **Sample:** `"4154ce0c-71a7-4d87-a905-09762098ddb9"` |
| **name**  string | The name of the RBAC rule; usually null  **Returned:** success |
| **object_id**  string | The UUID of the object to which the RBAC rules apply  **Returned:** success  **Sample:** `"7422172b-2961-475c-ac68-bd0f2a9960ad"` |
| **object_type**  string | The object type to which the RBACs apply  **Returned:** success  **Sample:** `"network"` |
| **project_id**  string | The UUID of the project to which access is granted  **Returned:** success  **Sample:** `"84b8774d595b41e89f3dfaa1fd76932c"` |
| **target_project_id**  string | The UUID of the target project  **Returned:** success  **Sample:** `"c201a689c016435c8037977166f77368"` |
| **tenant_id**  string | The UUID of the project to which access is granted. Deprecated.  **Returned:** success  **Sample:** `"84b8774d595b41e89f3dfaa1fd76932c"` |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
