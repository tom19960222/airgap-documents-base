---
collection: ansible
version: "8"
title: "community.general.utm_aaa_group module – Create, update or destroy an aaa group object in Sophos UTM"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/utm_aaa_group_module.html
fetched_at: 2026-07-28T01:51:06+00:00
---
# community.general.utm_aaa_group module – Create, update or destroy an aaa group object in Sophos UTM

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
> To use it in a playbook, specify: `community.general.utm_aaa_group`.

- [Synopsis](utm_aaa_group_module.md#synopsis)
- [Parameters](utm_aaa_group_module.md#parameters)
- [Attributes](utm_aaa_group_module.md#attributes)
- [Examples](utm_aaa_group_module.md#examples)
- [Return Values](utm_aaa_group_module.md#return-values)

## [Synopsis](utm_aaa_group_module.md#id1)

- Create, update or destroy an aaa group object in Sophos UTM.
- This module needs to have the REST Ability of the UTM to be activated.

Aliases: web_infrastructure.sophos_utm.utm_aaa_group

## [Parameters](utm_aaa_group_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adirectory_groups**  list / elements=string | List of adirectory group strings.  **Default:** `[]` |
| **adirectory_groups_sids**  dictionary | Dictionary of group sids.  **Default:** `{}` |
| **backend_match**  string | The backend for the group.  **Choices:**   - `"none"` ← (default) - `"adirectory"` - `"edirectory"` - `"radius"` - `"tacacs"` - `"ldap"` |
| **comment**  string | Comment that describes the AAA group.  **Default:** `""` |
| **dynamic**  string | Group type. Is static if none is selected.  **Choices:**   - `"none"` ← (default) - `"ipsec_dn"` - `"directory_groups"` |
| **edirectory_groups**  list / elements=string | List of edirectory group strings.  **Default:** `[]` |
| **headers**  dictionary | A dictionary of additional headers to be sent to POST and PUT requests.  Is needed for some modules  **Default:** `{}` |
| **ipsec_dn**  string | The ipsec dn string.  **Default:** `""` |
| **ldap_attribute**  string | The ldap attribute to check against.  **Default:** `""` |
| **ldap_attribute_value**  string | The ldap attribute value to check against.  **Default:** `""` |
| **members**  list / elements=string | A list of user ref names (aaa/user).  **Default:** `[]` |
| **name**  string / required | The name of the object. Will be used to identify the entry. |
| **network**  string | The network reference name. The objects contains the known ip addresses for the authentication object (network/aaa).  **Default:** `""` |
| **radius_groups**  list / elements=string | A list of radius group strings.  **Default:** `[]` |
| **state**  string | The desired state of the object.  `present` will create or update an object  `absent` will delete an object if it was present  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **tacacs_groups**  list / elements=string | A list of tacacs group strings.  **Default:** `[]` |
| **utm_host**  string / required | The REST Endpoint of the Sophos UTM. |
| **utm_port**  integer | The port of the REST interface.  **Default:** `4444` |
| **utm_protocol**  string | The protocol of the REST Endpoint.  **Choices:**   - `"http"` - `"https"` ← (default) |
| **utm_token**  string / required | The token used to identify at the REST-API. See <https://www.sophos.com/en-us/medialibrary/PDFs/documentation/UTMonAWS/Sophos-UTM-RESTful-API.pdf?la=en>, Chapter 2.4.2. |
| **validate_certs**  boolean | Whether the REST interface’s ssl certificate should be verified or not.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](utm_aaa_group_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](utm_aaa_group_module.md#id4)

```yaml+jinja
- name: Create UTM aaa_group
  community.general.utm_aaa_group:
    utm_host: sophos.host.name
    utm_token: abcdefghijklmno1234
    name: TestAAAGroupEntry
    backend_match: ldap
    dynamic: directory_groups
    ldap_attributes: memberof
    ldap_attributes_value: "cn=groupname,ou=Groups,dc=mydomain,dc=com"
    network: REF_OBJECT_STRING
    state: present

- name: Remove UTM aaa_group
  community.general.utm_aaa_group:
    utm_host: sophos.host.name
    utm_token: abcdefghijklmno1234
    name: TestAAAGroupEntry
    state: absent
```

## [Return Values](utm_aaa_group_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  complex | The utm object that was created.  **Returned:** success |
| **_locked**  boolean | Whether or not the object is currently locked.  **Returned:** success |
| **_ref**  string | The reference name of the object.  **Returned:** success |
| **_type**  string | The type of the object.  **Returned:** success |
| **adirectory_groups**  string | List of Active Directory Groups.  **Returned:** success |
| **adirectory_groups_sids**  list / elements=string | List of Active Directory Groups SIDS.  **Returned:** success |
| **backend_match**  string | The backend to use.  **Returned:** success |
| **comment**  string | The comment string.  **Returned:** success |
| **dynamic**  string | Whether the group match is ipsec_dn or directory_group.  **Returned:** success |
| **edirectory_groups**  string | List of eDirectory Groups.  **Returned:** success |
| **ipsec_dn**  string | ipsec_dn identifier to match.  **Returned:** success |
| **ldap_attribute**  string | The LDAP Attribute to match against.  **Returned:** success |
| **ldap_attribute_value**  string | The LDAP Attribute Value to match against.  **Returned:** success |
| **members**  list / elements=string | List of member identifiers of the group.  **Returned:** success |
| **name**  string | The name of the object.  **Returned:** success |
| **network**  string | The identifier of the network (network/aaa).  **Returned:** success |
| **radius_group**  string | The radius group identifier.  **Returned:** success |
| **tacacs_group**  string | The tacacs group identifier.  **Returned:** success |

### Authors

- Johannes Brunswicker (@MatrixCrawler)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
