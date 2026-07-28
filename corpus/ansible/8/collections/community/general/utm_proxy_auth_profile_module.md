---
collection: ansible
version: "8"
title: "community.general.utm_proxy_auth_profile module – Create, update or destroy reverse_proxy auth_profile entry in Sophos UTM"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/utm_proxy_auth_profile_module.html
fetched_at: 2026-07-28T01:51:11+00:00
---
# community.general.utm_proxy_auth_profile module – Create, update or destroy reverse_proxy auth_profile entry in Sophos UTM

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.utm_proxy_auth_profile`.

- [Synopsis](utm_proxy_auth_profile_module.md#synopsis)
- [Parameters](utm_proxy_auth_profile_module.md#parameters)
- [Attributes](utm_proxy_auth_profile_module.md#attributes)
- [Examples](utm_proxy_auth_profile_module.md#examples)
- [Return Values](utm_proxy_auth_profile_module.md#return-values)

## [Synopsis](utm_proxy_auth_profile_module.md#id1)

- Create, update or destroy a reverse_proxy auth_profile entry in SOPHOS UTM.
- This module needs to have the REST Ability of the UTM to be activated.

Aliases: web_infrastructure.sophos_utm.utm_proxy_auth_profile

## [Parameters](utm_proxy_auth_profile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aaa**  list / elements=string / required | List of references to utm_aaa objects (allowed users or groups) |
| **backend_mode**  string | Specifies if the backend server needs authentication ([Basic|None])  **Choices:**   - `"Basic"` - `"None"` ← (default) |
| **backend_strip_basic_auth**  boolean | Should the login data be stripped when proxying the request to the backend host  **Choices:**   - `false` - `true` ← (default) |
| **backend_user_prefix**  string | Prefix string to prepend to the username for backend authentication  **Default:** `""` |
| **backend_user_suffix**  string | Suffix string to append to the username for backend authentication  **Default:** `""` |
| **basic_prompt**  string / required | The message in the basic authentication prompt |
| **comment**  string | Optional comment string  **Default:** `""` |
| **frontend_cookie**  string | Frontend cookie name |
| **frontend_cookie_secret**  string | Frontend cookie secret |
| **frontend_form**  string | Frontend authentication form name |
| **frontend_form_template**  string | Frontend authentication form template  **Default:** `""` |
| **frontend_login**  string | Frontend login name |
| **frontend_logout**  string | Frontend logout name |
| **frontend_mode**  string | Frontend authentication mode (Form|Basic)  **Choices:**   - `"Basic"` ← (default) - `"Form"` |
| **frontend_realm**  string | Frontend authentication realm |
| **frontend_session_allow_persistency**  boolean | Allow session persistency  **Choices:**   - `false` ← (default) - `true` |
| **frontend_session_lifetime**  integer / required | session lifetime |
| **frontend_session_lifetime_limited**  boolean | Specifies if limitation of session lifetime is active  **Choices:**   - `false` - `true` ← (default) |
| **frontend_session_lifetime_scope**  string | scope for frontend_session_lifetime (days|hours|minutes)  **Choices:**   - `"days"` - `"hours"` ← (default) - `"minutes"` |
| **frontend_session_timeout**  integer / required | session timeout |
| **frontend_session_timeout_enabled**  boolean | Specifies if session timeout is active  **Choices:**   - `false` - `true` ← (default) |
| **frontend_session_timeout_scope**  string | scope for frontend_session_timeout (days|hours|minutes)  **Choices:**   - `"days"` - `"hours"` - `"minutes"` ← (default) |
| **headers**  dictionary | A dictionary of additional headers to be sent to POST and PUT requests.  Is needed for some modules  **Default:** `{}` |
| **logout_delegation_urls**  list / elements=string | List of logout URLs that logouts are delegated to  **Default:** `[]` |
| **logout_mode**  string | Mode of logout (None|Delegation)  **Choices:**   - `"None"` ← (default) - `"Delegation"` |
| **name**  string / required | The name of the object. Will be used to identify the entry |
| **redirect_to_requested_url**  boolean | Should a redirect to the requested URL be made  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | The desired state of the object.  `present` will create or update an object  `absent` will delete an object if it was present  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **utm_host**  string / required | The REST Endpoint of the Sophos UTM. |
| **utm_port**  integer | The port of the REST interface.  **Default:** `4444` |
| **utm_protocol**  string | The protocol of the REST Endpoint.  **Choices:**   - `"http"` - `"https"` ← (default) |
| **utm_token**  string / required | The token used to identify at the REST-API. See <https://www.sophos.com/en-us/medialibrary/PDFs/documentation/UTMonAWS/Sophos-UTM-RESTful-API.pdf?la=en>, Chapter 2.4.2. |
| **validate_certs**  boolean | Whether the REST interface’s ssl certificate should be verified or not.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](utm_proxy_auth_profile_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](utm_proxy_auth_profile_module.md#id4)

```yaml+jinja
- name: Create UTM proxy_auth_profile
  community.general.utm_proxy_auth_profile:
    utm_host: sophos.host.name
    utm_token: abcdefghijklmno1234
    name: TestAuthProfileEntry
    aaa: [REF_OBJECT_STRING,REF_ANOTHEROBJECT_STRING]
    basic_prompt: "Authentication required: Please login"
    frontend_session_lifetime: 1
    frontend_session_timeout: 1
    state: present

- name: Remove UTM proxy_auth_profile
  community.general.utm_proxy_auth_profile:
    utm_host: sophos.host.name
    utm_token: abcdefghijklmno1234
    name: TestAuthProfileEntry
    state: absent

- name: Read UTM proxy_auth_profile
  community.general.utm_proxy_auth_profile:
    utm_host: sophos.host.name
    utm_token: abcdefghijklmno1234
    name: TestAuthProfileEntry
    state: info
```

## [Return Values](utm_proxy_auth_profile_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  complex | The utm object that was created  **Returned:** success |
| **_locked**  boolean | Whether or not the object is currently locked  **Returned:** success |
| **_ref**  string | The reference name of the object  **Returned:** success |
| **_type**  string | The type of the object  **Returned:** success |
| **aaa**  list / elements=string | List of references to utm_aaa objects (allowed users or groups)  **Returned:** success |
| **backend_mode**  string | Specifies if the backend server needs authentication ([Basic|None])  **Returned:** success |
| **backend_strip_basic_auth**  boolean | Should the login data be stripped when proxying the request to the backend host  **Returned:** success |
| **backend_user_prefix**  string | Prefix string to prepend to the username for backend authentication  **Returned:** success |
| **backend_user_suffix**  string | Suffix string to append to the username for backend authentication  **Returned:** success |
| **basic_prompt**  string | The message in the basic authentication prompt  **Returned:** success |
| **comment**  string | Optional comment string  **Returned:** success |
| **frontend_cookie**  string | Frontend cookie name  **Returned:** success |
| **frontend_form**  string | Frontend authentication form name  **Returned:** success |
| **frontend_form_template**  string | Frontend authentication form template  **Returned:** success |
| **frontend_login**  string | Frontend login name  **Returned:** success |
| **frontend_logout**  string | Frontend logout name  **Returned:** success |
| **frontend_mode**  string | Frontend authentication mode (Form|Basic)  **Returned:** success |
| **frontend_realm**  string | Frontend authentication realm  **Returned:** success |
| **frontend_session_allow_persistency**  boolean | Allow session persistency  **Returned:** success |
| **frontend_session_lifetime**  integer | session lifetime  **Returned:** success |
| **frontend_session_lifetime_limited**  boolean | Specifies if limitation of session lifetime is active  **Returned:** success |
| **frontend_session_lifetime_scope**  string | scope for frontend_session_lifetime (days|hours|minutes)  **Returned:** success |
| **frontend_session_timeout**  integer | session timeout  **Returned:** success |
| **frontend_session_timeout_enabled**  boolean | Specifies if session timeout is active  **Returned:** success |
| **frontend_session_timeout_scope**  string | scope for frontend_session_timeout (days|hours|minutes)  **Returned:** success |
| **logout_delegation_urls**  list / elements=string | List of logout URLs that logouts are delegated to  **Returned:** success |
| **logout_mode**  string | Mode of logout (None|Delegation)  **Returned:** success |
| **name**  string | The name of the object  **Returned:** success |
| **redirect_to_requested_url**  boolean | Should a redirect to the requested URL be made  **Returned:** success |

### Authors

- Stephan Schwarz (@stearz)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
