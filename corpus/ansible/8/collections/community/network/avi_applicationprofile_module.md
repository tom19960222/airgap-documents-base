---
collection: ansible
version: "8"
title: "community.network.avi_applicationprofile module – Module for setup of ApplicationProfile Avi RESTful Object"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/avi_applicationprofile_module.html
fetched_at: 2026-07-28T01:54:27+00:00
---
# community.network.avi_applicationprofile module – Module for setup of ApplicationProfile Avi RESTful Object

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
> see [Requirements](avi_applicationprofile_module.md#ansible-collections-community-network-avi-applicationprofile-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.avi_applicationprofile`.

- [Synopsis](avi_applicationprofile_module.md#synopsis)
- [Requirements](avi_applicationprofile_module.md#requirements)
- [Parameters](avi_applicationprofile_module.md#parameters)
- [Notes](avi_applicationprofile_module.md#notes)
- [Examples](avi_applicationprofile_module.md#examples)
- [Return Values](avi_applicationprofile_module.md#return-values)

## [Synopsis](avi_applicationprofile_module.md#id1)

- This module is used to configure ApplicationProfile object
- more examples at <https://github.com/avinetworks/devops>

Aliases: network.avi.avi_applicationprofile

## [Requirements](avi_applicationprofile_module.md#id2)

The below requirements are needed on the host that executes this module.

- avisdk

## [Parameters](avi_applicationprofile_module.md#id3)

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
| **cloud_config_cksum**  string | Checksum of application profiles.  Internally set by cloud connector.  Field introduced in 17.2.14, 18.1.5, 18.2.1. |
| **controller**  string | IP address or hostname of the controller. The default value is the environment variable `AVI_CONTROLLER`. |
| **created_by**  string | Name of the application profile creator.  Field introduced in 17.2.14, 18.1.5, 18.2.1. |
| **description**  string | User defined description for the object. |
| **dns_service_profile**  string | Specifies various dns service related controls for virtual service. |
| **dos_rl_profile**  string | Specifies various security related controls for virtual service. |
| **http_profile**  string | Specifies the http application proxy profile parameters. |
| **name**  string / required | The name of the application profile. |
| **password**  string | Password of Avi user in Avi controller. The default value is the environment variable `AVI_PASSWORD`. |
| **preserve_client_ip**  boolean | Specifies if client ip needs to be preserved for backend connection.  Not compatible with connection multiplexing.  Default value when not specified in API or module is interpreted by Avi Controller as False.  **Choices:**   - `false` - `true` |
| **preserve_client_port**  boolean | Specifies if we need to preserve client port while preserving client ip for backend connections.  Field introduced in 17.2.7.  Default value when not specified in API or module is interpreted by Avi Controller as False.  **Choices:**   - `false` - `true` |
| **sip_service_profile**  string | Specifies various sip service related controls for virtual service.  Field introduced in 17.2.8, 18.1.3, 18.2.1. |
| **state**  string | The state that should be applied on the entity.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **tcp_app_profile**  string | Specifies the tcp application proxy profile parameters. |
| **tenant**  string | Name of tenant used for all Avi API calls and context of object.  **Default:** `"admin"` |
| **tenant_ref**  string | It is a reference to an object of type tenant. |
| **tenant_uuid**  string | UUID of tenant used for all Avi API calls and context of object.  **Default:** `""` |
| **type**  string / required | Specifies which application layer proxy is enabled for the virtual service.  Enum options - APPLICATION_PROFILE_TYPE_L4, APPLICATION_PROFILE_TYPE_HTTP, APPLICATION_PROFILE_TYPE_SYSLOG, APPLICATION_PROFILE_TYPE_DNS,  APPLICATION_PROFILE_TYPE_SSL, APPLICATION_PROFILE_TYPE_SIP. |
| **url**  string | Avi controller URL of the object. |
| **username**  string | Username used for accessing Avi controller. The default value is the environment variable `AVI_USERNAME`. |
| **uuid**  string | Uuid of the application profile. |

## [Notes](avi_applicationprofile_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Avi Network devices see <https://www.ansible.com/ansible-avi-networks>.

## [Examples](avi_applicationprofile_module.md#id5)

```yaml+jinja
- name: Create an Application Profile for HTTP application enabled for SSL traffic
  community.network.avi_applicationprofile:
    controller: '{{ controller }}'
    username: '{{ username }}'
    password: '{{ password }}'
    http_profile:
      cache_config:
        age_header: true
        aggressive: false
        date_header: true
        default_expire: 600
        enabled: false
        heuristic_expire: false
        max_cache_size: 0
        max_object_size: 4194304
        mime_types_group_refs:
        - admin:System-Cacheable-Resource-Types
        min_object_size: 100
        query_cacheable: false
        xcache_header: true
      client_body_timeout: 0
      client_header_timeout: 10000
      client_max_body_size: 0
      client_max_header_size: 12
      client_max_request_size: 48
      compression_profile:
        compressible_content_ref: admin:System-Compressible-Content-Types
        compression: false
        remove_accept_encoding_header: true
        type: AUTO_COMPRESSION
      connection_multiplexing_enabled: true
      hsts_enabled: false
      hsts_max_age: 365
      http_to_https: false
      httponly_enabled: false
      keepalive_header: false
      keepalive_timeout: 30000
      max_bad_rps_cip: 0
      max_bad_rps_cip_uri: 0
      max_bad_rps_uri: 0
      max_rps_cip: 0
      max_rps_cip_uri: 0
      max_rps_unknown_cip: 0
      max_rps_unknown_uri: 0
      max_rps_uri: 0
      post_accept_timeout: 30000
      secure_cookie_enabled: false
      server_side_redirect_to_https: false
      spdy_enabled: false
      spdy_fwd_proxy_mode: false
      ssl_client_certificate_mode: SSL_CLIENT_CERTIFICATE_NONE
      ssl_everywhere_enabled: false
      websockets_enabled: true
      x_forwarded_proto_enabled: false
      xff_alternate_name: X-Forwarded-For
      xff_enabled: true
    name: System-HTTP
    tenant_ref: admin
    type: APPLICATION_PROFILE_TYPE_HTTP
```

## [Return Values](avi_applicationprofile_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **obj**  dictionary | ApplicationProfile (api/applicationprofile) object  **Returned:** success, changed |

### Authors

- Gaurav Rastogi (@grastogi23)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
