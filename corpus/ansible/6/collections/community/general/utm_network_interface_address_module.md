---
collection: ansible
version: "6"
title: "community.general.utm_network_interface_address module – Create, update or destroy network/interface_address object"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/utm_network_interface_address_module.html
fetched_at: 2026-07-27T17:13:46+00:00
---
# community.general.utm_network_interface_address module – Create, update or destroy network/interface_address object

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.utm_network_interface_address`.

- [Synopsis](utm_network_interface_address_module.md#synopsis)
- [Parameters](utm_network_interface_address_module.md#parameters)
- [Examples](utm_network_interface_address_module.md#examples)
- [Return Values](utm_network_interface_address_module.md#return-values)

## [Synopsis](utm_network_interface_address_module.md#id1)

- Create, update or destroy a network/interface_address object in SOPHOS UTM.
- This module needs to have the REST Ability of the UTM to be activated.

## [Parameters](utm_network_interface_address_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **address**  string / required | The ip4 address of the network/interface_address object. |
| **address6**  string | The ip6 address of the network/interface_address object. |
| **comment**  string | An optional comment to add to the object  Default: `""` |
| **headers**  dictionary | A dictionary of additional headers to be sent to POST and PUT requests.  Is needed for some modules  Default: `{}` |
| **name**  string / required | The name of the object. Will be used to identify the entry |
| **resolved**  boolean | Whether or not the object is resolved  Choices:   - `false` - `true` |
| **resolved6**  boolean | Whether or not the object is resolved  Choices:   - `false` - `true` |
| **state**  string | The desired state of the object.  `present` will create or update an object  `absent` will delete an object if it was present  Choices:   - `"absent"` - `"present"` ← (default) |
| **utm_host**  string / required | The REST Endpoint of the Sophos UTM. |
| **utm_port**  integer | The port of the REST interface.  Default: `4444` |
| **utm_protocol**  string | The protocol of the REST Endpoint.  Choices:   - `"http"` - `"https"` ← (default) |
| **utm_token**  string / required | The token used to identify at the REST-API. See <https://www.sophos.com/en-us/medialibrary/PDFs/documentation/UTMonAWS/Sophos-UTM-RESTful-API.pdf?la%3Den>, Chapter 2.4.2. |
| **validate_certs**  boolean | Whether the REST interface’s ssl certificate should be verified or not.  Choices:   - `false` - `true` ← (default) |

## [Examples](utm_network_interface_address_module.md#id3)

```yaml+jinja
- name: Create a network interface address
  utm_proxy_backend:
    utm_host: sophos.host.name
    utm_token: abcdefghijklmno1234
    name: TestNetworkInterfaceAddress
    address: 0.0.0.0
    state: present

- name: Remove a network interface address
  network_interface_address:
    utm_host: sophos.host.name
    utm_token: abcdefghijklmno1234
    name: TestNetworkInterfaceAddress
    address: 0.0.0.0
    state: absent
```

## [Return Values](utm_network_interface_address_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  complex | The utm object that was created  Returned: success |
| **_locked**  boolean | Whether or not the object is currently locked  Returned: success |
| **_ref**  string | The reference name of the object  Returned: success |
| **_type**  string | The type of the object  Returned: success |
| **address**  string | The ip4 address of the network/interface_address object  Returned: success |
| **address6**  string | The ip6 address of the network/interface_address object  Returned: success |
| **comment**  string | The comment string  Returned: success |
| **name**  string | The name of the object  Returned: success |
| **resolved**  boolean | Whether or not the object is resolved  Returned: success |
| **resolved6**  boolean | Whether or not the object is resolved  Returned: success |

### Authors

- Juergen Wiebe (@steamx)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
