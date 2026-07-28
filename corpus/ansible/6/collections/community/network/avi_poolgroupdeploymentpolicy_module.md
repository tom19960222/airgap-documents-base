---
collection: ansible
version: "6"
title: "community.network.avi_poolgroupdeploymentpolicy module – Module for setup of PoolGroupDeploymentPolicy Avi RESTful Object"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/avi_poolgroupdeploymentpolicy_module.html
fetched_at: 2026-07-27T17:16:54+00:00
---
# community.network.avi_poolgroupdeploymentpolicy module – Module for setup of PoolGroupDeploymentPolicy Avi RESTful Object

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
> You need further requirements to be able to use this module,
> see [Requirements](avi_poolgroupdeploymentpolicy_module.md#ansible-collections-community-network-avi-poolgroupdeploymentpolicy-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.avi_poolgroupdeploymentpolicy`.

- [Synopsis](avi_poolgroupdeploymentpolicy_module.md#synopsis)
- [Requirements](avi_poolgroupdeploymentpolicy_module.md#requirements)
- [Parameters](avi_poolgroupdeploymentpolicy_module.md#parameters)
- [Notes](avi_poolgroupdeploymentpolicy_module.md#notes)
- [Examples](avi_poolgroupdeploymentpolicy_module.md#examples)
- [Return Values](avi_poolgroupdeploymentpolicy_module.md#return-values)

## [Synopsis](avi_poolgroupdeploymentpolicy_module.md#id1)

- This module is used to configure PoolGroupDeploymentPolicy object
- more examples at <https://github.com/avinetworks/devops>

## [Requirements](avi_poolgroupdeploymentpolicy_module.md#id2)

The below requirements are needed on the host that executes this module.

- avisdk

## [Parameters](avi_poolgroupdeploymentpolicy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_context**  dictionary | Avi API context that includes current session ID and CSRF Token.  This allows user to perform single login and re-use the session. |
| **api_version**  string | Avi API version of to use for Avi API and objects.  Default: `"16.4.4"` |
| **auto_disable_old_prod_pools**  boolean | It will automatically disable old production pools once there is a new production candidate.  Default value when not specified in API or module is interpreted by Avi Controller as True.  Choices:   - `false` - `true` |
| **avi_api_patch_op**  string | Patch operation to use when using avi_api_update_method as patch.  Choices:   - `"add"` - `"replace"` - `"delete"` |
| **avi_api_update_method**  string | Default method for object update is HTTP PUT.  Setting to patch will override that behavior to use HTTP PATCH.  Choices:   - `"put"` ← (default) - `"patch"` |
| **avi_credentials**  dictionary | Avi Credentials dictionary which can be used in lieu of enumerating Avi Controller login details. |
| **api_version**  string | Avi controller version  Default: `"16.4.4"` |
| **controller**  string | Avi controller IP or SQDN |
| **csrftoken**  string | Avi controller API csrftoken to reuse existing session with session id  Default: `""` |
| **password**  string | Avi controller password |
| **port**  string | Avi controller port |
| **session_id**  string | Avi controller API session id to reuse existing session with csrftoken  Default: `""` |
| **tenant**  string | Avi controller tenant  Default: `"admin"` |
| **tenant_uuid**  string | Avi controller tenant UUID  Default: `""` |
| **timeout**  string | Avi controller request timeout  Default: `300` |
| **token**  string | Avi controller API token  Default: `""` |
| **username**  string | Avi controller username |
| **avi_disable_session_cache_as_fact**  boolean | It disables avi session information to be cached as a fact.  Choices:   - `false` ← (default) - `true` |
| **controller**  string | IP address or hostname of the controller. The default value is the environment variable `AVI_CONTROLLER`. |
| **description**  string | User defined description for the object. |
| **evaluation_duration**  string | Duration of evaluation period for automatic deployment.  Allowed values are 60-86400.  Default value when not specified in API or module is interpreted by Avi Controller as 300. |
| **name**  string / required | The name of the pool group deployment policy. |
| **password**  string | Password of Avi user in Avi controller. The default value is the environment variable `AVI_PASSWORD`. |
| **rules**  string | List of pgdeploymentrule. |
| **scheme**  string | Deployment scheme.  Enum options - BLUE_GREEN, CANARY.  Default value when not specified in API or module is interpreted by Avi Controller as BLUE_GREEN. |
| **state**  string | The state that should be applied on the entity.  Choices:   - `"absent"` - `"present"` ← (default) |
| **target_test_traffic_ratio**  string | Target traffic ratio before pool is made production.  Allowed values are 1-100.  Default value when not specified in API or module is interpreted by Avi Controller as 100. |
| **tenant**  string | Name of tenant used for all Avi API calls and context of object.  Default: `"admin"` |
| **tenant_ref**  string | It is a reference to an object of type tenant. |
| **tenant_uuid**  string | UUID of tenant used for all Avi API calls and context of object.  Default: `""` |
| **test_traffic_ratio_rampup**  string | Ratio of the traffic that is sent to the pool under test.  Test ratio of 100 means blue green.  Allowed values are 1-100.  Default value when not specified in API or module is interpreted by Avi Controller as 100. |
| **url**  string | Avi controller URL of the object. |
| **username**  string | Username used for accessing Avi controller. The default value is the environment variable `AVI_USERNAME`. |
| **uuid**  string | Uuid of the pool group deployment policy. |
| **webhook_ref**  string | Webhook configured with url that avi controller will pass back information about pool group, old and new pool information and current deployment  rule results.  It is a reference to an object of type webhook.  Field introduced in 17.1.1. |

## [Notes](avi_poolgroupdeploymentpolicy_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Avi Network devices see <https://www.ansible.com/ansible-avi-networks>.

## [Examples](avi_poolgroupdeploymentpolicy_module.md#id5)

```yaml+jinja
- name: Example to create PoolGroupDeploymentPolicy object
  community.network.avi_poolgroupdeploymentpolicy:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_poolgroupdeploymentpolicy
```

## [Return Values](avi_poolgroupdeploymentpolicy_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **obj**  dictionary | PoolGroupDeploymentPolicy (api/poolgroupdeploymentpolicy) object  Returned: success, changed |

### Authors

- Gaurav Rastogi (@grastogi23)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
