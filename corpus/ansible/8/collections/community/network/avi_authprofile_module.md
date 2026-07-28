---
collection: ansible
version: "8"
title: "community.network.avi_authprofile module – Module for setup of AuthProfile Avi RESTful Object"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/avi_authprofile_module.html
fetched_at: 2026-07-28T01:54:28+00:00
---
# community.network.avi_authprofile module – Module for setup of AuthProfile Avi RESTful Object

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
> see [Requirements](avi_authprofile_module.md#ansible-collections-community-network-avi-authprofile-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.avi_authprofile`.

- [Synopsis](avi_authprofile_module.md#synopsis)
- [Requirements](avi_authprofile_module.md#requirements)
- [Parameters](avi_authprofile_module.md#parameters)
- [Notes](avi_authprofile_module.md#notes)
- [Examples](avi_authprofile_module.md#examples)
- [Return Values](avi_authprofile_module.md#return-values)

## [Synopsis](avi_authprofile_module.md#id1)

- This module is used to configure AuthProfile object
- more examples at <https://github.com/avinetworks/devops>

Aliases: network.avi.avi_authprofile

## [Requirements](avi_authprofile_module.md#id2)

The below requirements are needed on the host that executes this module.

- avisdk

## [Parameters](avi_authprofile_module.md#id3)

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
| **http**  string | Http user authentication params. |
| **ldap**  string | Ldap server and directory settings. |
| **name**  string / required | Name of the auth profile. |
| **pa_agent_ref**  string | Pingaccessagent uuid.  It is a reference to an object of type pingaccessagent.  Field introduced in 18.2.3. |
| **password**  string | Password of Avi user in Avi controller. The default value is the environment variable `AVI_PASSWORD`. |
| **saml**  string | Saml settings.  Field introduced in 17.2.3. |
| **state**  string | The state that should be applied on the entity.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **tacacs_plus**  string | Tacacs+ settings. |
| **tenant**  string | Name of tenant used for all Avi API calls and context of object.  **Default:** `"admin"` |
| **tenant_ref**  string | It is a reference to an object of type tenant. |
| **tenant_uuid**  string | UUID of tenant used for all Avi API calls and context of object.  **Default:** `""` |
| **type**  string / required | Type of the auth profile.  Enum options - AUTH_PROFILE_LDAP, AUTH_PROFILE_TACACS_PLUS, AUTH_PROFILE_SAML, AUTH_PROFILE_PINGACCESS. |
| **url**  string | Avi controller URL of the object. |
| **username**  string | Username used for accessing Avi controller. The default value is the environment variable `AVI_USERNAME`. |
| **uuid**  string | Uuid of the auth profile. |

## [Notes](avi_authprofile_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Avi Network devices see <https://www.ansible.com/ansible-avi-networks>.

## [Examples](avi_authprofile_module.md#id5)

```yaml+jinja
- name: Create user authorization profile based on the LDAP
  community.network.avi_authprofile:
    controller: '{{ controller }}'
    password: '{{ password }}'
    username: '{{ username }}'
    http:
      cache_expiration_time: 5
      group_member_is_full_dn: false
    ldap:
      base_dn: dc=avi,dc=local
      bind_as_administrator: true
      port: 389
      security_mode: AUTH_LDAP_SECURE_NONE
      server:
      - 10.10.0.100
      settings:
        admin_bind_dn: user@avi.local
        group_filter: (objectClass=*)
        group_member_attribute: member
        group_member_is_full_dn: true
        group_search_dn: dc=avi,dc=local
        group_search_scope: AUTH_LDAP_SCOPE_SUBTREE
        ignore_referrals: true
        password: password
        user_id_attribute: samAccountname
        user_search_dn: dc=avi,dc=local
        user_search_scope: AUTH_LDAP_SCOPE_ONE
    name: ProdAuth
    tenant_ref: admin
    type: AUTH_PROFILE_LDAP
```

## [Return Values](avi_authprofile_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **obj**  dictionary | AuthProfile (api/authprofile) object  **Returned:** success, changed |

### Authors

- Gaurav Rastogi (@grastogi23)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
