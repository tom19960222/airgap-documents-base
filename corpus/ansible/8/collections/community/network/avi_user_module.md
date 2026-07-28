---
collection: ansible
version: "8"
title: "community.network.avi_user module – Avi User Module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/avi_user_module.html
fetched_at: 2026-07-28T01:55:02+00:00
---
# community.network.avi_user module – Avi User Module

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
> see [Requirements](avi_user_module.md#ansible-collections-community-network-avi-user-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.avi_user`.

- [Synopsis](avi_user_module.md#synopsis)
- [Requirements](avi_user_module.md#requirements)
- [Parameters](avi_user_module.md#parameters)
- [Notes](avi_user_module.md#notes)
- [Examples](avi_user_module.md#examples)
- [Return Values](avi_user_module.md#return-values)

## [Synopsis](avi_user_module.md#id1)

- This module can be used for creation, updation and deletion of a user.

Aliases: network.avi.avi_user

## [Requirements](avi_user_module.md#id2)

The below requirements are needed on the host that executes this module.

- avisdk

## [Parameters](avi_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access**  list / elements=string | Access settings (write, read, or no access) for each type of resource within Vantage. |
| **api_context**  dictionary | Avi API context that includes current session ID and CSRF Token.  This allows user to perform single login and re-use the session. |
| **api_version**  string | Avi API version of to use for Avi API and objects.  **Default:** `"16.4.4"` |
| **avi_api_patch_op**  string | Patch operation to use when using avi_api_update_method as patch.  **Choices:**   - `"add"` - `"replace"` - `"delete"` |
| **avi_api_update_method**  string | Default method for object update is HTTP PUT.  Setting to patch will override that behavior to use HTTP PATCH.  **Choices:**   - `"post"` - `"put"` ← (default) - `"patch"` |
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
| **default_tenant_ref**  string | Default tenant reference.  This can also be full URI same as it comes in response payload  **Default:** `"/api/tenant?name=admin"` |
| **email**  string | Email address of the user. This field is used when a user loses their password and requests to have it reset. See Password Recovery. |
| **is_active**  boolean | Activates the current user account.  **Choices:**   - `false` - `true` |
| **is_superuser**  boolean | If the user will need to have the same privileges as the admin account, set it to true.  **Choices:**   - `false` - `true` |
| **name**  string / required | Full name of the user. |
| **obj_password**  string / required | You may either enter a case-sensitive password in this field for the new or existing user. |
| **obj_username**  string / required | Name that the user will supply when signing into Avi Vantage, such as jdoe or [jdoe@avinetworks.com](mailto:jdoe%40avinetworks.com). |
| **password**  string | Password of Avi user in Avi controller. The default value is the environment variable `AVI_PASSWORD`. |
| **state**  string | The state that should be applied on the entity.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **tenant**  string | Name of tenant used for all Avi API calls and context of object.  **Default:** `"admin"` |
| **tenant_uuid**  string | UUID of tenant used for all Avi API calls and context of object.  **Default:** `""` |
| **user_profile_ref**  string | Refer user profile.  This can also be full URI same as it comes in response payload |
| **username**  string | Username used for accessing Avi controller. The default value is the environment variable `AVI_USERNAME`. |

## [Notes](avi_user_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Avi Network devices see <https://www.ansible.com/ansible-avi-networks>.

## [Examples](avi_user_module.md#id5)

```yaml+jinja
- name: User creation
  community.network.avi_user:
    controller: ""
    username: ""
    password: ""
    api_version: ""
    name: "testuser"
    obj_username: "testuser"
    obj_password: "test123"
    email: "test@abc.test"
    access:
      - role_ref: "/api/role?name=Tenant-Admin"
        tenant_ref: "/api/tenant/admin#admin"
    user_profile_ref: "/api/useraccountprofile?name=Default-User-Account-Profile"
    is_active: true
    is_superuser: true
    default_tenant_ref: "/api/tenant?name=admin"

- name: User creation
  community.network.avi_user:
    controller: ""
    username: ""
    password: ""
    api_version: ""
    name: "testuser"
    obj_username: "testuser2"
    obj_password: "password"
    email: "testuser2@abc.test"
    access:
      - role_ref: "https://192.0.2.10/api/role?name=Tenant-Admin"
        tenant_ref: "https://192.0.2.10/api/tenant/admin#admin"
    user_profile_ref: "https://192.0.2.10/api/useraccountprofile?name=Default-User-Account-Profile"
    is_active: true
    is_superuser: true
    default_tenant_ref: "https://192.0.2.10/api/tenant?name=admin"
```

## [Return Values](avi_user_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **obj**  dictionary | Avi REST resource  **Returned:** success, changed |

### Authors

- Shrikant Chaudhari (@gitshrikant)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
