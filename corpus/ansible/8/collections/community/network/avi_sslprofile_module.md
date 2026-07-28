---
collection: ansible
version: "8"
title: "community.network.avi_sslprofile module – Module for setup of SSLProfile Avi RESTful Object"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/avi_sslprofile_module.html
fetched_at: 2026-07-28T01:54:58+00:00
---
# community.network.avi_sslprofile module – Module for setup of SSLProfile Avi RESTful Object

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
> see [Requirements](avi_sslprofile_module.md#ansible-collections-community-network-avi-sslprofile-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.avi_sslprofile`.

- [Synopsis](avi_sslprofile_module.md#synopsis)
- [Requirements](avi_sslprofile_module.md#requirements)
- [Parameters](avi_sslprofile_module.md#parameters)
- [Notes](avi_sslprofile_module.md#notes)
- [Examples](avi_sslprofile_module.md#examples)
- [Return Values](avi_sslprofile_module.md#return-values)

## [Synopsis](avi_sslprofile_module.md#id1)

- This module is used to configure SSLProfile object
- more examples at <https://github.com/avinetworks/devops>

Aliases: network.avi.avi_sslprofile

## [Requirements](avi_sslprofile_module.md#id2)

The below requirements are needed on the host that executes this module.

- avisdk

## [Parameters](avi_sslprofile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **accepted_ciphers**  string | Ciphers suites represented as defined by <http://www.openssl.org/docs/apps/ciphers.html>.  Default value when not specified in API or module is interpreted by Avi Controller as AES:3DES:RC4. |
| **accepted_versions**  string | Set of versions accepted by the server. |
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
| **cipher_enums**  string | Enum options - tls_ecdhe_ecdsa_with_aes_128_gcm_sha256, tls_ecdhe_ecdsa_with_aes_256_gcm_sha384, tls_ecdhe_rsa_with_aes_128_gcm_sha256,  tls_ecdhe_rsa_with_aes_256_gcm_sha384, tls_ecdhe_ecdsa_with_aes_128_cbc_sha256, tls_ecdhe_ecdsa_with_aes_256_cbc_sha384,  tls_ecdhe_rsa_with_aes_128_cbc_sha256, tls_ecdhe_rsa_with_aes_256_cbc_sha384, tls_rsa_with_aes_128_gcm_sha256, tls_rsa_with_aes_256_gcm_sha384,  tls_rsa_with_aes_128_cbc_sha256, tls_rsa_with_aes_256_cbc_sha256, tls_ecdhe_ecdsa_with_aes_128_cbc_sha, tls_ecdhe_ecdsa_with_aes_256_cbc_sha,  tls_ecdhe_rsa_with_aes_128_cbc_sha, tls_ecdhe_rsa_with_aes_256_cbc_sha, tls_rsa_with_aes_128_cbc_sha, tls_rsa_with_aes_256_cbc_sha,  tls_rsa_with_3des_ede_cbc_sha, tls_rsa_with_rc4_128_sha. |
| **controller**  string | IP address or hostname of the controller. The default value is the environment variable `AVI_CONTROLLER`. |
| **description**  string | User defined description for the object. |
| **dhparam**  string | Dh parameters used in ssl.  At this time, it is not configurable and is set to 2048 bits. |
| **enable_ssl_session_reuse**  boolean | Enable ssl session re-use.  Default value when not specified in API or module is interpreted by Avi Controller as True.  **Choices:**   - `false` - `true` |
| **name**  string / required | Name of the object. |
| **password**  string | Password of Avi user in Avi controller. The default value is the environment variable `AVI_PASSWORD`. |
| **prefer_client_cipher_ordering**  boolean | Prefer the ssl cipher ordering presented by the client during the ssl handshake over the one specified in the ssl profile.  Default value when not specified in API or module is interpreted by Avi Controller as False.  **Choices:**   - `false` - `true` |
| **send_close_notify**  boolean | Send ‘close notify’ alert message for a clean shutdown of the ssl connection.  Default value when not specified in API or module is interpreted by Avi Controller as True.  **Choices:**   - `false` - `true` |
| **ssl_rating**  string | Sslrating settings for sslprofile. |
| **ssl_session_timeout**  string | The amount of time in seconds before an ssl session expires.  Default value when not specified in API or module is interpreted by Avi Controller as 86400. |
| **state**  string | The state that should be applied on the entity.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **tags**  string | List of tag. |
| **tenant**  string | Name of tenant used for all Avi API calls and context of object.  **Default:** `"admin"` |
| **tenant_ref**  string | It is a reference to an object of type tenant. |
| **tenant_uuid**  string | UUID of tenant used for all Avi API calls and context of object.  **Default:** `""` |
| **type**  string | Ssl profile type.  Enum options - SSL_PROFILE_TYPE_APPLICATION, SSL_PROFILE_TYPE_SYSTEM.  Field introduced in 17.2.8.  Default value when not specified in API or module is interpreted by Avi Controller as SSL_PROFILE_TYPE_APPLICATION. |
| **url**  string | Avi controller URL of the object. |
| **username**  string | Username used for accessing Avi controller. The default value is the environment variable `AVI_USERNAME`. |
| **uuid**  string | Unique object identifier of the object. |

## [Notes](avi_sslprofile_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Avi Network devices see <https://www.ansible.com/ansible-avi-networks>.

## [Examples](avi_sslprofile_module.md#id5)

```yaml+jinja
- name: Create SSL profile with list of allowed ciphers
  community.network.avi_sslprofile:
    controller: '{{ controller }}'
    username: '{{ username }}'
    password: '{{ password }}'
    accepted_ciphers: >
      ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA:ECDHE-ECDSA-AES256-SHA:
      ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA384:
      AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:
      AES256-SHA:DES-CBC3-SHA:ECDHE-RSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:
      ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA
    accepted_versions:
    - type: SSL_VERSION_TLS1
    - type: SSL_VERSION_TLS1_1
    - type: SSL_VERSION_TLS1_2
    cipher_enums:
    - TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
    - TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA
    - TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA
    - TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
    - TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256
    - TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384
    - TLS_RSA_WITH_AES_128_GCM_SHA256
    - TLS_RSA_WITH_AES_256_GCM_SHA384
    - TLS_RSA_WITH_AES_128_CBC_SHA256
    - TLS_RSA_WITH_AES_256_CBC_SHA256
    - TLS_RSA_WITH_AES_128_CBC_SHA
    - TLS_RSA_WITH_AES_256_CBC_SHA
    - TLS_RSA_WITH_3DES_EDE_CBC_SHA
    - TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA
    - TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384
    - TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
    - TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
    - TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
    - TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA
    name: PFS-BOTH-RSA-EC
    send_close_notify: true
    ssl_rating:
      compatibility_rating: SSL_SCORE_EXCELLENT
      performance_rating: SSL_SCORE_EXCELLENT
      security_score: '100.0'
    tenant_ref: Demo
```

## [Return Values](avi_sslprofile_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **obj**  dictionary | SSLProfile (api/sslprofile) object  **Returned:** success, changed |

### Authors

- Gaurav Rastogi (@grastogi23)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
