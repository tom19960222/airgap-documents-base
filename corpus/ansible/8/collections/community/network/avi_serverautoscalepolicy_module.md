---
collection: ansible
version: "8"
title: "community.network.avi_serverautoscalepolicy module – Module for setup of ServerAutoScalePolicy Avi RESTful Object"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/avi_serverautoscalepolicy_module.html
fetched_at: 2026-07-28T01:54:55+00:00
---
# community.network.avi_serverautoscalepolicy module – Module for setup of ServerAutoScalePolicy Avi RESTful Object

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
> You need further requirements to be able to use this module,
> see [Requirements](avi_serverautoscalepolicy_module.md#ansible-collections-community-network-avi-serverautoscalepolicy-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.avi_serverautoscalepolicy`.

- [Synopsis](avi_serverautoscalepolicy_module.md#synopsis)
- [Requirements](avi_serverautoscalepolicy_module.md#requirements)
- [Parameters](avi_serverautoscalepolicy_module.md#parameters)
- [Notes](avi_serverautoscalepolicy_module.md#notes)
- [Examples](avi_serverautoscalepolicy_module.md#examples)
- [Return Values](avi_serverautoscalepolicy_module.md#return-values)

## [Synopsis](avi_serverautoscalepolicy_module.md#id1)

- This module is used to configure ServerAutoScalePolicy object
- more examples at <https://github.com/avinetworks/devops>

Aliases: network.avi.avi_serverautoscalepolicy

## [Requirements](avi_serverautoscalepolicy_module.md#id2)

The below requirements are needed on the host that executes this module.

- avisdk

## [Parameters](avi_serverautoscalepolicy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_context**  dictionary | Avi API context that includes current session ID and CSRF Token.  This allows user to perform single login and re-use the session. |
| **api_version**  string | Avi API version of to use for Avi API and objects.  **Default:** `"16.4.4"` |
| **avi_api_patch_op**  string | Patch operation to use when using avi_api_update_method as patch.  **Choices:**   - `"add"` - `"replace"` - `"delete"` |
| **avi_api_update_method**  string | Default method for object update is HTTP PUT.  Setting to patch will override that behavior to use HTTP PATCH.  **Choices:**   - `"put"` ← (default) - `"patch"` |
| **avi_credentials**  dictionary | Avi Credentials dictionary which can be used in lieu of enumerating Avi Controller login details. |
| **api_version**  string | Avi controller version  **Default:** `"16.4.4"` |
| **controller**  string | Avi controller IP or SQDN |
| **csrftoken**  string | Avi controller API csrftoken to reuse existing session with session id  **Default:** `""` |
| **password**  string | Avi controller password |
| **port**  string | Avi controller port |
| **session_id**  string | Avi controller API session id to reuse existing session with csrftoken  **Default:** `""` |
| **tenant**  string | Avi controller tenant  **Default:** `"admin"` |
| **tenant_uuid**  string | Avi controller tenant UUID  **Default:** `""` |
| **timeout**  string | Avi controller request timeout  **Default:** `300` |
| **token**  string | Avi controller API token  **Default:** `""` |
| **username**  string | Avi controller username |
| **avi_disable_session_cache_as_fact**  boolean | It disables avi session information to be cached as a fact.  **Choices:**   - `false` ← (default) - `true` |
| **controller**  string | IP address or hostname of the controller. The default value is the environment variable `AVI_CONTROLLER`. |
| **description**  string | User defined description for the object. |
| **intelligent_autoscale**  boolean | Use avi intelligent autoscale algorithm where autoscale is performed by comparing load on the pool against estimated capacity of all the servers.  Default value when not specified in API or module is interpreted by Avi Controller as False.  **Choices:**   - `false` - `true` |
| **intelligent_scalein_margin**  string | Maximum extra capacity as percentage of load used by the intelligent scheme.  Scalein is triggered when available capacity is more than this margin.  Allowed values are 1-99.  Default value when not specified in API or module is interpreted by Avi Controller as 40. |
| **intelligent_scaleout_margin**  string | Minimum extra capacity as percentage of load used by the intelligent scheme.  Scaleout is triggered when available capacity is less than this margin.  Allowed values are 1-99.  Default value when not specified in API or module is interpreted by Avi Controller as 20. |
| **max_scalein_adjustment_step**  string | Maximum number of servers to scalein simultaneously.  The actual number of servers to scalein is chosen such that target number of servers is always more than or equal to the min_size.  Default value when not specified in API or module is interpreted by Avi Controller as 1. |
| **max_scaleout_adjustment_step**  string | Maximum number of servers to scaleout simultaneously.  The actual number of servers to scaleout is chosen such that target number of servers is always less than or equal to the max_size.  Default value when not specified in API or module is interpreted by Avi Controller as 1. |
| **max_size**  string | Maximum number of servers after scaleout.  Allowed values are 0-400. |
| **min_size**  string | No scale-in happens once number of operationally up servers reach min_servers.  Allowed values are 0-400. |
| **name**  string / required | Name of the object. |
| **password**  string | Password of Avi user in Avi controller. The default value is the environment variable `AVI_PASSWORD`. |
| **scalein_alertconfig_refs**  string | Trigger scalein when alerts due to any of these alert configurations are raised.  It is a reference to an object of type alertconfig. |
| **scalein_cooldown**  string | Cooldown period during which no new scalein is triggered to allow previous scalein to successfully complete.  Default value when not specified in API or module is interpreted by Avi Controller as 300. |
| **scaleout_alertconfig_refs**  string | Trigger scaleout when alerts due to any of these alert configurations are raised.  It is a reference to an object of type alertconfig. |
| **scaleout_cooldown**  string | Cooldown period during which no new scaleout is triggered to allow previous scaleout to successfully complete.  Default value when not specified in API or module is interpreted by Avi Controller as 300. |
| **state**  string | The state that should be applied on the entity.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **tenant**  string | Name of tenant used for all Avi API calls and context of object.  **Default:** `"admin"` |
| **tenant_ref**  string | It is a reference to an object of type tenant. |
| **tenant_uuid**  string | UUID of tenant used for all Avi API calls and context of object.  **Default:** `""` |
| **url**  string | Avi controller URL of the object. |
| **use_predicted_load**  boolean | Use predicted load rather than current load.  Default value when not specified in API or module is interpreted by Avi Controller as False.  **Choices:**   - `false` - `true` |
| **username**  string | Username used for accessing Avi controller. The default value is the environment variable `AVI_USERNAME`. |
| **uuid**  string | Unique object identifier of the object. |

## [Notes](avi_serverautoscalepolicy_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Avi Network devices see <https://www.ansible.com/ansible-avi-networks>.

## [Examples](avi_serverautoscalepolicy_module.md#id5)

```yaml+jinja
- name: Example to create ServerAutoScalePolicy object
  community.network.avi_serverautoscalepolicy:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_serverautoscalepolicy
```

## [Return Values](avi_serverautoscalepolicy_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **obj**  dictionary | ServerAutoScalePolicy (api/serverautoscalepolicy) object  **Returned:** success, changed |

### Authors

- Gaurav Rastogi (@grastogi23)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
