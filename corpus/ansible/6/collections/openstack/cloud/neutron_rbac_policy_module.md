---
collection: ansible
version: "6"
title: "openstack.cloud.neutron_rbac_policy module – Create or delete a Neutron policy to apply a RBAC rule against an object."
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/neutron_rbac_policy_module.html
fetched_at: 2026-07-28T00:16:53+00:00
---
# openstack.cloud.neutron_rbac_policy module – Create or delete a Neutron policy to apply a RBAC rule against an object.

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
> see [Requirements](neutron_rbac_policy_module.md#ansible-collections-openstack-cloud-neutron-rbac-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.neutron_rbac_policy`.

- [Synopsis](neutron_rbac_policy_module.md#synopsis)
- [Requirements](neutron_rbac_policy_module.md#requirements)
- [Parameters](neutron_rbac_policy_module.md#parameters)
- [Notes](neutron_rbac_policy_module.md#notes)
- [Examples](neutron_rbac_policy_module.md#examples)
- [Return Values](neutron_rbac_policy_module.md#return-values)

## [Synopsis](neutron_rbac_policy_module.md#id1)

- Create a policy to apply a RBAC rule against a network, security group or a QoS Policy or update/delete an existing policy.
- If a `policy_id` was provided but not found, this module will attempt to create a new policy rather than error out when updating an existing rule.
- Accepts same arguments as OpenStackSDK network proxy `find_rbac_policy` and `rbac_policies` functions which are ultimately passed over to `RBACPolicy`

## [Requirements](neutron_rbac_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 0.36, < 0.99.0

## [Parameters](neutron_rbac_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **action**  string | Can be either of the following options `access_as_shared` | `access_as_external`  Cannot be changed when updating an existing policy  Required when creating a RBAC policy rule, ignored when deleting a policy  Choices:   - `"access_as_shared"` - `"access_as_external"` |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **availability_zone**  string | Ignored. Present for backwards compatibility |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  Choices:   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **object_id**  string | The object ID (the subject of the policy) to which the RBAC rule applies  Cannot be changed when updating an existing policy  Required when creating a RBAC policy rule, ignored when deleting a policy |
| **object_type**  string | Can be one of the following object types `network`, `security_group` or `qos_policy`  Cannot be changed when updating an existing policy  Required when creating a RBAC policy rule, ignored when deleting a policy  Choices:   - `"network"` - `"security_group"` - `"qos_policy"` |
| **policy_id**  string | The RBAC policy ID  Required when deleting or updating an existing RBAC policy rule, ignored otherwise |
| **project_id**  string | The project to which the object_id belongs  Cannot be changed when updating an existing policy  Required when creating a RBAC policy rule, ignored when deleting a policy |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  Choices:   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Whether the RBAC rule should be `present` or `absent`.  Choices:   - `"present"` ← (default) - `"absent"` |
| **target_project_id**  string | The project to which access to be allowed or revoked/disallowed  Can be specified/changed when updating an existing policy  Required when creating or updating a RBAC policy rule, ignored when deleting a policy |
| **timeout**  integer | How long should ansible wait for the requested resource.  Default: `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `yes`.  Choices:   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  Choices:   - `false` - `true` ← (default) |

## [Notes](neutron_rbac_policy_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](neutron_rbac_policy_module.md#id5)

```yaml+jinja
# Ensure network RBAC policy exists
- name: Create a new network RBAC policy
  neutron_rbac_policy:
    object_id: '7422172b-2961-475c-ac68-bd0f2a9960ad'
    object_type: 'network'
    target_project_id: 'a12f9ce1de0645e0a0b01c2e679f69ec'
    project_id: '84b8774d595b41e89f3dfaa1fd76932d'

# Update network RBAC policy
- name: Update an existing network RBAC policy
  neutron_rbac_policy:
    policy_id: 'f625242a-6a73-47ac-8d1f-91440b2c617f'
    target_project_id: '163c89e065a94e069064e551e15daf0e'

# Delete an existing RBAC policy
- name: Delete RBAC policy
  openstack.cloud.openstack.neutron_rbac_policy:
    policy_id: 'f625242a-6a73-47ac-8d1f-91440b2c617f'
    state: absent
```

## [Return Values](neutron_rbac_policy_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **policy**  complex | A hash representing the policy  Returned: always |
| **action**  string | The access model specified by the RBAC rules  Returned: success  Sample: `"access_as_shared"` |
| **id**  string | The ID of the RBAC rule/policy  Returned: success  Sample: `"4154ce0c-71a7-4d87-a905-09762098ddb9"` |
| **location**  dictionary | A dictionary of the project details to which access is granted  Returned: success  Sample: `{"cloud": "devstack", "project": {"domain_id": null, "domain_name": null, "id": "84b8774d595b41e89f3dfaa1fd76932c", "name": null}, "region_name": "", "zone": null}` |
| **name**  string | The name of the RBAC rule; usually null  Returned: success |
| **object_id**  string | The UUID of the object to which the RBAC rules apply  Returned: success  Sample: `"7422172b-2961-475c-ac68-bd0f2a9960ad"` |
| **object_type**  string | The object type to which the RBACs apply  Returned: success  Sample: `"network"` |
| **project_id**  string | The UUID of the project to which access is granted  Returned: success  Sample: `"84b8774d595b41e89f3dfaa1fd76932c"` |
| **target_project_id**  string | The UUID of the target project  Returned: success  Sample: `"c201a689c016435c8037977166f77368"` |

### Authors

- OpenStack Ansible SIG

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
