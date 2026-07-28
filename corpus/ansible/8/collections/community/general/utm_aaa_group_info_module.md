---
collection: ansible
version: "8"
title: "community.general.utm_aaa_group_info module – Get info for reverse_proxy frontend entry in Sophos UTM"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/utm_aaa_group_info_module.html
fetched_at: 2026-07-28T01:51:07+00:00
---
# community.general.utm_aaa_group_info module – Get info for reverse_proxy frontend entry in Sophos UTM

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
> To use it in a playbook, specify: `community.general.utm_aaa_group_info`.

- [Synopsis](utm_aaa_group_info_module.md#synopsis)
- [Parameters](utm_aaa_group_info_module.md#parameters)
- [Attributes](utm_aaa_group_info_module.md#attributes)
- [Examples](utm_aaa_group_info_module.md#examples)
- [Return Values](utm_aaa_group_info_module.md#return-values)

## [Synopsis](utm_aaa_group_info_module.md#id1)

- get info for a reverse_proxy frontend entry in SOPHOS UTM.

Aliases: web_infrastructure.sophos_utm.utm_aaa_group_info

## [Parameters](utm_aaa_group_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **headers**  dictionary | A dictionary of additional headers to be sent to POST and PUT requests.  Is needed for some modules  **Default:** `{}` |
| **name**  string / required | The name of the object. Will be used to identify the entry |
| **state**  string | The desired state of the object.  `present` will create or update an object  `absent` will delete an object if it was present  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **utm_host**  string / required | The REST Endpoint of the Sophos UTM. |
| **utm_port**  integer | The port of the REST interface.  **Default:** `4444` |
| **utm_protocol**  string | The protocol of the REST Endpoint.  **Choices:**   - `"http"` - `"https"` ← (default) |
| **utm_token**  string / required | The token used to identify at the REST-API. See <https://www.sophos.com/en-us/medialibrary/PDFs/documentation/UTMonAWS/Sophos-UTM-RESTful-API.pdf?la=en>, Chapter 2.4.2. |
| **validate_certs**  boolean | Whether the REST interface’s ssl certificate should be verified or not.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](utm_aaa_group_info_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  *added in community.general 3.3.0*  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](utm_aaa_group_info_module.md#id4)

```yaml+jinja
- name: Remove UTM aaa_group
  community.general.utm_aaa_group_info:
    utm_host: sophos.host.name
    utm_token: abcdefghijklmno1234
    name: TestAAAGroupEntry
```

## [Return Values](utm_aaa_group_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  complex | The utm object that was created  **Returned:** success |
| **_locked**  boolean | Whether or not the object is currently locked  **Returned:** success |
| **_ref**  string | The reference name of the object  **Returned:** success |
| **_type**  string | The type of the object  **Returned:** success |
| **adirectory_groups**  string | List of Active Directory Groups  **Returned:** success |
| **adirectory_groups_sids**  list / elements=string | List of Active Directory Groups SIDS  **Returned:** success |
| **backend_match**  string | The backend to use  **Returned:** success |
| **comment**  string | The comment string  **Returned:** success |
| **dynamic**  string | Whether the group match is ipsec_dn or directory_group  **Returned:** success |
| **edirectory_groups**  string | List of eDirectory Groups  **Returned:** success |
| **ipsec_dn**  string | ipsec_dn identifier to match  **Returned:** success |
| **ldap_attribute**  string | The LDAP Attribute to match against  **Returned:** success |
| **ldap_attribute_value**  string | The LDAP Attribute Value to match against  **Returned:** success |
| **members**  list / elements=string | List of member identifiers of the group  **Returned:** success |
| **name**  string | The name of the object  **Returned:** success |
| **network**  string | The identifier of the network (network/aaa)  **Returned:** success |
| **radius_group**  string | The radius group identifier  **Returned:** success |
| **tacacs_group**  string | The tacacs group identifier  **Returned:** success |

### Authors

- Johannes Brunswicker (@MatrixCrawler)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
