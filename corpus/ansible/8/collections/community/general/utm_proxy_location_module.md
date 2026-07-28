---
collection: ansible
version: "8"
title: "community.general.utm_proxy_location module – Create, update or destroy reverse_proxy location entry in Sophos UTM"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/utm_proxy_location_module.html
fetched_at: 2026-07-28T01:51:14+00:00
---
# community.general.utm_proxy_location module – Create, update or destroy reverse_proxy location entry in Sophos UTM

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
> To use it in a playbook, specify: `community.general.utm_proxy_location`.

- [Synopsis](utm_proxy_location_module.md#synopsis)
- [Parameters](utm_proxy_location_module.md#parameters)
- [Attributes](utm_proxy_location_module.md#attributes)
- [Examples](utm_proxy_location_module.md#examples)
- [Return Values](utm_proxy_location_module.md#return-values)

## [Synopsis](utm_proxy_location_module.md#id1)

- Create, update or destroy a reverse_proxy location entry in SOPHOS UTM.
- This module needs to have the REST Ability of the UTM to be activated.

Aliases: web_infrastructure.sophos_utm.utm_proxy_location

## [Parameters](utm_proxy_location_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_control**  string | whether to activate the access control for the location  **Choices:**   - `"0"` ← (default) - `"1"` |
| **allowed_networks**  list / elements=string | A list of allowed networks  **Default:** `["REF_NetworkAny"]` |
| **auth_profile**  string | The reference name of the auth profile  **Default:** `""` |
| **backend**  list / elements=string | A list of backends that are connected with this location declaration  **Default:** `[]` |
| **be_path**  string | The path of the backend  **Default:** `""` |
| **comment**  string | The optional comment string  **Default:** `""` |
| **denied_networks**  list / elements=string | A list of denied network references  **Default:** `[]` |
| **headers**  dictionary | A dictionary of additional headers to be sent to POST and PUT requests.  Is needed for some modules  **Default:** `{}` |
| **hot_standby**  boolean | Activate hot standby mode  **Choices:**   - `false` ← (default) - `true` |
| **name**  string / required | The name of the object. Will be used to identify the entry |
| **path**  string | The path of the location  **Default:** `"/"` |
| **state**  string | The desired state of the object.  `present` will create or update an object  `absent` will delete an object if it was present  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **status**  boolean | Whether the location is active or not  **Choices:**   - `false` - `true` ← (default) |
| **stickysession_id**  string | The stickysession id  **Default:** `"ROUTEID"` |
| **stickysession_status**  boolean | Enable the stickysession  **Choices:**   - `false` ← (default) - `true` |
| **utm_host**  string / required | The REST Endpoint of the Sophos UTM. |
| **utm_port**  integer | The port of the REST interface.  **Default:** `4444` |
| **utm_protocol**  string | The protocol of the REST Endpoint.  **Choices:**   - `"http"` - `"https"` ← (default) |
| **utm_token**  string / required | The token used to identify at the REST-API. See <https://www.sophos.com/en-us/medialibrary/PDFs/documentation/UTMonAWS/Sophos-UTM-RESTful-API.pdf?la=en>, Chapter 2.4.2. |
| **validate_certs**  boolean | Whether the REST interface’s ssl certificate should be verified or not.  **Choices:**   - `false` - `true` ← (default) |
| **websocket_passthrough**  boolean | Enable the websocket passthrough  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](utm_proxy_location_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](utm_proxy_location_module.md#id4)

```yaml+jinja
- name: Create UTM proxy_location
  utm_proxy_backend:
    utm_host: sophos.host.name
    utm_token: abcdefghijklmno1234
    name: TestLocationEntry
    backend: REF_OBJECT_STRING
    state: present

- name: Remove UTM proxy_location
  utm_proxy_backend:
    utm_host: sophos.host.name
    utm_token: abcdefghijklmno1234
    name: TestLocationEntry
    state: absent
```

## [Return Values](utm_proxy_location_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  complex | The utm object that was created  **Returned:** success |
| **_locked**  boolean | Whether or not the object is currently locked  **Returned:** success |
| **_ref**  string | The reference name of the object  **Returned:** success |
| **_type**  string | The type of the object  **Returned:** success |
| **access_control**  string | Whether to use access control state  **Returned:** success |
| **allowed_networks**  list / elements=string | List of allowed network reference names  **Returned:** success |
| **auth_profile**  string | The auth profile reference name  **Returned:** success |
| **backend**  string | The backend reference name  **Returned:** success |
| **be_path**  string | The backend path  **Returned:** success |
| **comment**  string | The comment string  **Returned:** success |
| **denied_networks**  list / elements=string | The list of the denied network names  **Returned:** success |
| **hot_standby**  boolean | Use hot standby  **Returned:** success |
| **name**  string | The name of the object  **Returned:** success |
| **path**  string | Path name  **Returned:** success |
| **status**  boolean | Whether the object is active or not  **Returned:** success |
| **stickysession_id**  string | The identifier of the stickysession  **Returned:** success |
| **stickysession_status**  boolean | Whether to use stickysession or not  **Returned:** success |
| **websocket_passthrough**  boolean | Whether websocket passthrough will be used or not  **Returned:** success |

### Authors

- Johannes Brunswicker (@MatrixCrawler)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
