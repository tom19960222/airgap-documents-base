---
collection: ansible
version: "6"
title: "community.network.avi_vsdatascriptset module – Module for setup of VSDataScriptSet Avi RESTful Object"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/avi_vsdatascriptset_module.html
fetched_at: 2026-07-27T17:17:08+00:00
---
# community.network.avi_vsdatascriptset module – Module for setup of VSDataScriptSet Avi RESTful Object

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
> see [Requirements](avi_vsdatascriptset_module.md#ansible-collections-community-network-avi-vsdatascriptset-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.avi_vsdatascriptset`.

- [Synopsis](avi_vsdatascriptset_module.md#synopsis)
- [Requirements](avi_vsdatascriptset_module.md#requirements)
- [Parameters](avi_vsdatascriptset_module.md#parameters)
- [Notes](avi_vsdatascriptset_module.md#notes)
- [Examples](avi_vsdatascriptset_module.md#examples)
- [Return Values](avi_vsdatascriptset_module.md#return-values)

## [Synopsis](avi_vsdatascriptset_module.md#id1)

- This module is used to configure VSDataScriptSet object
- more examples at <https://github.com/avinetworks/devops>

## [Requirements](avi_vsdatascriptset_module.md#id2)

The below requirements are needed on the host that executes this module.

- avisdk

## [Parameters](avi_vsdatascriptset_module.md#id3)

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
| **controller**  string | IP address or hostname of the controller. The default value is the environment variable `AVI_CONTROLLER`. |
| **created_by**  string | Creator name.  Field introduced in 17.1.11,17.2.4. |
| **datascript**  string | Datascripts to execute. |
| **description**  string | User defined description for the object. |
| **ipgroup_refs**  string | Uuid of ip groups that could be referred by vsdatascriptset objects.  It is a reference to an object of type ipaddrgroup. |
| **name**  string / required | Name for the virtual service datascript collection. |
| **password**  string | Password of Avi user in Avi controller. The default value is the environment variable `AVI_PASSWORD`. |
| **pool_group_refs**  string | Uuid of pool groups that could be referred by vsdatascriptset objects.  It is a reference to an object of type poolgroup. |
| **pool_refs**  string | Uuid of pools that could be referred by vsdatascriptset objects.  It is a reference to an object of type pool. |
| **protocol_parser_refs**  string | List of protocol parsers that could be referred by vsdatascriptset objects.  It is a reference to an object of type protocolparser.  Field introduced in 18.2.3. |
| **state**  string | The state that should be applied on the entity.  Choices:   - `"absent"` - `"present"` ← (default) |
| **string_group_refs**  string | Uuid of string groups that could be referred by vsdatascriptset objects.  It is a reference to an object of type stringgroup. |
| **tenant**  string | Name of tenant used for all Avi API calls and context of object.  Default: `"admin"` |
| **tenant_ref**  string | It is a reference to an object of type tenant. |
| **tenant_uuid**  string | UUID of tenant used for all Avi API calls and context of object.  Default: `""` |
| **url**  string | Avi controller URL of the object. |
| **username**  string | Username used for accessing Avi controller. The default value is the environment variable `AVI_USERNAME`. |
| **uuid**  string | Uuid of the virtual service datascript collection. |

## [Notes](avi_vsdatascriptset_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Avi Network devices see <https://www.ansible.com/ansible-avi-networks>.

## [Examples](avi_vsdatascriptset_module.md#id5)

```yaml+jinja
- name: Example to create VSDataScriptSet object
  community.network.avi_vsdatascriptset:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_vsdatascriptset
```

## [Return Values](avi_vsdatascriptset_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **obj**  dictionary | VSDataScriptSet (api/vsdatascriptset) object  Returned: success, changed |

### Authors

- Gaurav Rastogi (@grastogi23)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
