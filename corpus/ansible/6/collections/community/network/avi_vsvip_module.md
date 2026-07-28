---
collection: ansible
version: "6"
title: "community.network.avi_vsvip module – Module for setup of VsVip Avi RESTful Object"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/avi_vsvip_module.html
fetched_at: 2026-07-27T17:17:08+00:00
---
# community.network.avi_vsvip module – Module for setup of VsVip Avi RESTful Object

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
> see [Requirements](avi_vsvip_module.md#ansible-collections-community-network-avi-vsvip-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.avi_vsvip`.

- [Synopsis](avi_vsvip_module.md#synopsis)
- [Requirements](avi_vsvip_module.md#requirements)
- [Parameters](avi_vsvip_module.md#parameters)
- [Notes](avi_vsvip_module.md#notes)
- [Examples](avi_vsvip_module.md#examples)
- [Return Values](avi_vsvip_module.md#return-values)

## [Synopsis](avi_vsvip_module.md#id1)

- This module is used to configure VsVip object
- more examples at <https://github.com/avinetworks/devops>

## [Requirements](avi_vsvip_module.md#id2)

The below requirements are needed on the host that executes this module.

- avisdk

## [Parameters](avi_vsvip_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_context**  dictionary | Avi API context that includes current session ID and CSRF Token.  This allows user to perform single login and re-use the session. |
| **api_version**  string | Avi API version of to use for Avi API and objects.  Default: `"16.4.4"` |
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
| **cloud_ref**  string | It is a reference to an object of type cloud.  Field introduced in 17.1.1. |
| **controller**  string | IP address or hostname of the controller. The default value is the environment variable `AVI_CONTROLLER`. |
| **dns_info**  string | Service discovery specific data including fully qualified domain name, type and time-to-live of the dns record.  Field introduced in 17.1.1. |
| **east_west_placement**  boolean | Force placement on all service engines in the service engine group (container clouds only).  Field introduced in 17.1.1.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **name**  string / required | Name for the vsvip object.  Field introduced in 17.1.1. |
| **password**  string | Password of Avi user in Avi controller. The default value is the environment variable `AVI_PASSWORD`. |
| **state**  string | The state that should be applied on the entity.  Choices:   - `"absent"` - `"present"` ← (default) |
| **tenant**  string | Name of tenant used for all Avi API calls and context of object.  Default: `"admin"` |
| **tenant_ref**  string | It is a reference to an object of type tenant.  Field introduced in 17.1.1. |
| **tenant_uuid**  string | UUID of tenant used for all Avi API calls and context of object.  Default: `""` |
| **url**  string | Avi controller URL of the object. |
| **use_standard_alb**  boolean | This overrides the cloud level default and needs to match the se group value in which it will be used if the se group use_standard_alb value is  set.  This is only used when fip is used for vs on azure cloud.  Field introduced in 18.2.3.  Choices:   - `false` - `true` |
| **username**  string | Username used for accessing Avi controller. The default value is the environment variable `AVI_USERNAME`. |
| **uuid**  string | Uuid of the vsvip object.  Field introduced in 17.1.1. |
| **vip**  string | List of virtual service ips and other shareable entities.  Field introduced in 17.1.1. |
| **vrf_context_ref**  string | Virtual routing context that the virtual service is bound to.  This is used to provide the isolation of the set of networks the application is attached to.  It is a reference to an object of type vrfcontext.  Field introduced in 17.1.1. |
| **vsvip_cloud_config_cksum**  string | Checksum of cloud configuration for vsvip.  Internally set by cloud connector.  Field introduced in 17.2.9, 18.1.2. |

## [Notes](avi_vsvip_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Avi Network devices see <https://www.ansible.com/ansible-avi-networks>.

## [Examples](avi_vsvip_module.md#id5)

```yaml+jinja
- name: Example to create VsVip object
  community.network.avi_vsvip:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_vsvip
```

## [Return Values](avi_vsvip_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **obj**  dictionary | VsVip (api/vsvip) object  Returned: success, changed |

### Authors

- Gaurav Rastogi (@grastogi23)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
