---
collection: ansible
version: "8"
title: "community.network.avi_applicationpersistenceprofile module – Module for setup of ApplicationPersistenceProfile Avi RESTful Object"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/avi_applicationpersistenceprofile_module.html
fetched_at: 2026-07-28T01:54:26+00:00
---
# community.network.avi_applicationpersistenceprofile module – Module for setup of ApplicationPersistenceProfile Avi RESTful Object

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
> see [Requirements](avi_applicationpersistenceprofile_module.md#ansible-collections-community-network-avi-applicationpersistenceprofile-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.avi_applicationpersistenceprofile`.

- [Synopsis](avi_applicationpersistenceprofile_module.md#synopsis)
- [Requirements](avi_applicationpersistenceprofile_module.md#requirements)
- [Parameters](avi_applicationpersistenceprofile_module.md#parameters)
- [Notes](avi_applicationpersistenceprofile_module.md#notes)
- [Examples](avi_applicationpersistenceprofile_module.md#examples)
- [Return Values](avi_applicationpersistenceprofile_module.md#return-values)

## [Synopsis](avi_applicationpersistenceprofile_module.md#id1)

- This module is used to configure ApplicationPersistenceProfile object
- more examples at <https://github.com/avinetworks/devops>

Aliases: network.avi.avi_applicationpersistenceprofile

## [Requirements](avi_applicationpersistenceprofile_module.md#id2)

The below requirements are needed on the host that executes this module.

- avisdk

## [Parameters](avi_applicationpersistenceprofile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_context**  dictionary | Avi API context that includes current session ID and CSRF Token.  This allows user to perform single login and re-use the session. |
| **api_version**  string | Avi API version of to use for Avi API and objects.  **Default:** `"16.4.4"` |
| **app_cookie_persistence_profile**  string | Specifies the application cookie persistence profile parameters. |
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
| **hdr_persistence_profile**  string | Specifies the custom http header persistence profile parameters. |
| **http_cookie_persistence_profile**  string | Specifies the http cookie persistence profile parameters. |
| **ip_persistence_profile**  string | Specifies the client ip persistence profile parameters. |
| **is_federated**  boolean | This field describes the object’s replication scope.  If the field is set to false, then the object is visible within the controller-cluster and its associated service-engines.  If the field is set to true, then the object is replicated across the federation.  Field introduced in 17.1.3.  Default value when not specified in API or module is interpreted by Avi Controller as False.  **Choices:**   - `false` - `true` |
| **name**  string / required | A user-friendly name for the persistence profile. |
| **password**  string | Password of Avi user in Avi controller. The default value is the environment variable `AVI_PASSWORD`. |
| **persistence_type**  string / required | Method used to persist clients to the same server for a duration of time or a session.  Enum options - PERSISTENCE_TYPE_CLIENT_IP_ADDRESS, PERSISTENCE_TYPE_HTTP_COOKIE, PERSISTENCE_TYPE_TLS, PERSISTENCE_TYPE_CLIENT_IPV6_ADDRESS,  PERSISTENCE_TYPE_CUSTOM_HTTP_HEADER, PERSISTENCE_TYPE_APP_COOKIE, PERSISTENCE_TYPE_GSLB_SITE.  Default value when not specified in API or module is interpreted by Avi Controller as PERSISTENCE_TYPE_CLIENT_IP_ADDRESS. |
| **server_hm_down_recovery**  string | Specifies behavior when a persistent server has been marked down by a health monitor.  Enum options - HM_DOWN_PICK_NEW_SERVER, HM_DOWN_ABORT_CONNECTION, HM_DOWN_CONTINUE_PERSISTENT_SERVER.  Default value when not specified in API or module is interpreted by Avi Controller as HM_DOWN_PICK_NEW_SERVER. |
| **state**  string | The state that should be applied on the entity.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **tenant**  string | Name of tenant used for all Avi API calls and context of object.  **Default:** `"admin"` |
| **tenant_ref**  string | It is a reference to an object of type tenant. |
| **tenant_uuid**  string | UUID of tenant used for all Avi API calls and context of object.  **Default:** `""` |
| **url**  string | Avi controller URL of the object. |
| **username**  string | Username used for accessing Avi controller. The default value is the environment variable `AVI_USERNAME`. |
| **uuid**  string | Uuid of the persistence profile. |

## [Notes](avi_applicationpersistenceprofile_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Avi Network devices see <https://www.ansible.com/ansible-avi-networks>.

## [Examples](avi_applicationpersistenceprofile_module.md#id5)

```yaml+jinja
- name: Create an Application Persistence setting using http cookie.
  community.network.avi_applicationpersistenceprofile:
    controller: '{{ controller }}'
    username: '{{ username }}'
    password: '{{ password }}'
    http_cookie_persistence_profile:
      always_send_cookie: false
      cookie_name: My-HTTP
      key:
      - aes_key: ShYGZdMks8j6Bpvm2sCvaXWzvXms2Z9ob+TTjRy46lQ=
        name: c1276819-550c-4adf-912d-59efa5fd7269
      - aes_key: OGsyVk84VCtyMENFOW0rMnRXVnNrb0RzdG5mT29oamJRb0dlbHZVSjR1az0=
        name: a080de57-77c3-4580-a3ea-e7a6493c14fd
      - aes_key: UVN0cU9HWmFUM2xOUzBVcmVXaHFXbnBLVUUxMU1VSktSVU5HWjJOWmVFMTBUMUV4UmxsNk4xQmFZejA9
        name: 60478846-33c6-484d-868d-bbc324fce4a5
      timeout: 15
    name: My-HTTP-Cookie
    persistence_type: PERSISTENCE_TYPE_HTTP_COOKIE
    server_hm_down_recovery: HM_DOWN_PICK_NEW_SERVER
    tenant_ref: Demo
```

## [Return Values](avi_applicationpersistenceprofile_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **obj**  dictionary | ApplicationPersistenceProfile (api/applicationpersistenceprofile) object  **Returned:** success, changed |

### Authors

- Gaurav Rastogi (@grastogi23)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
