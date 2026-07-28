---
collection: ansible
version: "8"
title: "community.general.utm_dns_host module – Create, update or destroy dns entry in Sophos UTM"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/utm_dns_host_module.html
fetched_at: 2026-07-28T01:51:09+00:00
---
# community.general.utm_dns_host module – Create, update or destroy dns entry in Sophos UTM

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
> To use it in a playbook, specify: `community.general.utm_dns_host`.

- [Synopsis](utm_dns_host_module.md#synopsis)
- [Parameters](utm_dns_host_module.md#parameters)
- [Attributes](utm_dns_host_module.md#attributes)
- [Examples](utm_dns_host_module.md#examples)
- [Return Values](utm_dns_host_module.md#return-values)

## [Synopsis](utm_dns_host_module.md#id1)

- Create, update or destroy a dns entry in SOPHOS UTM.
- This module needs to have the REST Ability of the UTM to be activated.

Aliases: web_infrastructure.sophos_utm.utm_dns_host

## [Parameters](utm_dns_host_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **address**  string | The IPV4 Address of the entry. Can be left empty for automatic resolving.  **Default:** `"0.0.0.0"` |
| **address6**  string | The IPV6 Address of the entry. Can be left empty for automatic resolving.  **Default:** `"::"` |
| **comment**  string | An optional comment to add to the dns host object  **Default:** `""` |
| **headers**  dictionary | A dictionary of additional headers to be sent to POST and PUT requests.  Is needed for some modules  **Default:** `{}` |
| **hostname**  string | The hostname for the dns host object |
| **interface**  string | The reference name of the interface to use. If not provided the default interface will be used  **Default:** `""` |
| **name**  string / required | The name of the object. Will be used to identify the entry |
| **resolved**  boolean | whether the hostname’s ipv4 address is already resolved or not  **Choices:**   - `false` ← (default) - `true` |
| **resolved6**  boolean | whether the hostname’s ipv6 address is already resolved or not  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | The desired state of the object.  `present` will create or update an object  `absent` will delete an object if it was present  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **timeout**  integer | the timeout for the utm to resolve the ip address for the hostname again  **Default:** `0` |
| **utm_host**  string / required | The REST Endpoint of the Sophos UTM. |
| **utm_port**  integer | The port of the REST interface.  **Default:** `4444` |
| **utm_protocol**  string | The protocol of the REST Endpoint.  **Choices:**   - `"http"` - `"https"` ← (default) |
| **utm_token**  string / required | The token used to identify at the REST-API. See <https://www.sophos.com/en-us/medialibrary/PDFs/documentation/UTMonAWS/Sophos-UTM-RESTful-API.pdf?la=en>, Chapter 2.4.2. |
| **validate_certs**  boolean | Whether the REST interface’s ssl certificate should be verified or not.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](utm_dns_host_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](utm_dns_host_module.md#id4)

```yaml+jinja
- name: Create UTM dns host entry
  community.general.utm_dns_host:
    utm_host: sophos.host.name
    utm_token: abcdefghijklmno1234
    name: TestDNSEntry
    hostname: testentry.some.tld
    state: present

- name: Remove UTM dns host entry
  community.general.utm_dns_host:
    utm_host: sophos.host.name
    utm_token: abcdefghijklmno1234
    name: TestDNSEntry
    state: absent
```

## [Return Values](utm_dns_host_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  complex | The utm object that was created  **Returned:** success |
| **_locked**  boolean | Whether or not the object is currently locked  **Returned:** success |
| **_ref**  string | The reference name of the object  **Returned:** success |
| **address**  string | The ipv4 address of the object  **Returned:** success |
| **address6**  string | The ipv6 address of the object  **Returned:** success |
| **comment**  string | The comment string  **Returned:** success |
| **hostname**  string | The hostname of the object  **Returned:** success |
| **interface**  string | The reference name of the interface the object is associated with  **Returned:** success |
| **name**  string | The name of the object  **Returned:** success |
| **resolved**  boolean | Whether the ipv4 address is resolved or not  **Returned:** success |
| **resolved6**  boolean | Whether the ipv6 address is resolved or not  **Returned:** success |
| **timeout**  integer | The timeout until a new resolving will be attempted  **Returned:** success |

### Authors

- Johannes Brunswicker (@MatrixCrawler)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
