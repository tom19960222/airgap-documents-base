---
collection: ansible
version: "6"
title: "community.general.utm_proxy_frontend module – Create, update or destroy reverse_proxy frontend entry in Sophos UTM"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/utm_proxy_frontend_module.html
fetched_at: 2026-07-27T17:13:48+00:00
---
# community.general.utm_proxy_frontend module – Create, update or destroy reverse_proxy frontend entry in Sophos UTM

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
> To use it in a playbook, specify: `community.general.utm_proxy_frontend`.

- [Synopsis](utm_proxy_frontend_module.md#synopsis)
- [Parameters](utm_proxy_frontend_module.md#parameters)
- [Examples](utm_proxy_frontend_module.md#examples)
- [Return Values](utm_proxy_frontend_module.md#return-values)

## [Synopsis](utm_proxy_frontend_module.md#id2)

- Create, update or destroy a reverse_proxy frontend entry in Sophos UTM.
- This module needs to have the REST Ability of the UTM to be activated.

## [Parameters](utm_proxy_frontend_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **add_content_type_header**  boolean | Whether to add the content type header or not  Choices:   - `false` ← (default) - `true` |
| **address**  string | The reference name of the network/interface_address object.  Default: `"REF_DefaultInternalAddress"` |
| **allowed_networks**  list / elements=string | A list of reference names for the allowed networks.  Default: `["REF_NetworkAny"]` |
| **certificate**  string | The reference name of the ca/host_key_cert object.  Default: `""` |
| **comment**  string | An optional comment to add to the object  Default: `""` |
| **disable_compression**  boolean | Whether to enable the compression  Choices:   - `false` ← (default) - `true` |
| **domain**  list / elements=string | A list of domain names for the frontend object |
| **exceptions**  list / elements=string | A list of exception ref names (reverse_proxy/exception)  Default: `[]` |
| **headers**  dictionary | A dictionary of additional headers to be sent to POST and PUT requests.  Is needed for some modules  Default: `{}` |
| **htmlrewrite**  boolean | Whether to enable html rewrite or not  Choices:   - `false` ← (default) - `true` |
| **htmlrewrite_cookies**  boolean | Whether to enable html rewrite cookie or not  Choices:   - `false` ← (default) - `true` |
| **implicitredirect**  boolean | Whether to enable implicit redirection or not  Choices:   - `false` ← (default) - `true` |
| **lbmethod**  string | Which loadbalancer method should be used  Choices:   - `""` - `"bybusyness"` ← (default) - `"bytraffic"` - `"byrequests"` |
| **locations**  list / elements=string | A list of location ref names (reverse_proxy/location)  Default: `[]` |
| **name**  string / required | The name of the object. Will be used to identify the entry |
| **port**  integer | The frontend http port  Default: `80` |
| **preservehost**  boolean | Whether to preserve host header  Choices:   - `false` ← (default) - `true` |
| **profile**  string | The reference string of the reverse_proxy/profile  Default: `""` |
| **state**  string | The desired state of the object.  `present` will create or update an object  `absent` will delete an object if it was present  Choices:   - `"absent"` - `"present"` ← (default) |
| **status**  boolean | Whether to activate the frontend entry or not  Choices:   - `false` - `true` ← (default) |
| **type**  string | Which protocol should be used  Choices:   - `"http"` ← (default) - `"https"` |
| **utm_host**  string / required | The REST Endpoint of the Sophos UTM. |
| **utm_port**  integer | The port of the REST interface.  Default: `4444` |
| **utm_protocol**  string | The protocol of the REST Endpoint.  Choices:   - `"http"` - `"https"` ← (default) |
| **utm_token**  string / required | The token used to identify at the REST-API. See <https://www.sophos.com/en-us/medialibrary/PDFs/documentation/UTMonAWS/Sophos-UTM-RESTful-API.pdf?la%3Den>, Chapter 2.4.2. |
| **validate_certs**  boolean | Whether the REST interface’s ssl certificate should be verified or not.  Choices:   - `false` - `true` ← (default) |
| **xheaders**  boolean | Whether to pass the host header or not  Choices:   - `false` ← (default) - `true` |

## [Examples](utm_proxy_frontend_module.md#id4)

```yaml+jinja
- name: Create utm proxy_frontend
  community.general.utm_proxy_frontend:
    utm_host: sophos.host.name
    utm_token: abcdefghijklmno1234
    name: TestFrontendEntry
    host: REF_OBJECT_STRING
    state: present

- name: Remove utm proxy_frontend
  community.general.utm_proxy_frontend:
    utm_host: sophos.host.name
    utm_token: abcdefghijklmno1234
    name: TestFrontendEntry
    state: absent
```

## [Return Values](utm_proxy_frontend_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  complex | The utm object that was created  Returned: success |
| **_locked**  boolean | Whether or not the object is currently locked  Returned: success |
| **_ref**  string | The reference name of the object  Returned: success |
| **_type**  string | The type of the object  Returned: success |
| **add_content_type_header**  boolean | Whether to add the content type header  Returned: success |
| **address**  string | The reference name of the address  Returned: success |
| **allowed_networks**  list / elements=string | List of reference names of networks associated  Returned: success |
| **certificate**  string | Reference name of certificate (ca/host_key_cert)  Returned: success |
| **comment**  string | The comment string  Returned: success |
| **disable_compression**  boolean | State of compression support  Returned: success |
| **domain**  list / elements=string | List of hostnames  Returned: success |
| **exceptions**  list / elements=string | List of associated proxy exceptions  Returned: success |
| **htmlrewrite**  boolean | State of html rewrite  Returned: success |
| **htmlrewrite_cookies**  boolean | Whether the html rewrite cookie will be set  Returned: success |
| **implicitredirect**  boolean | Whether to use implicit redirection  Returned: success |
| **lbmethod**  string | The method of loadbalancer to use  Returned: success |
| **locations**  list / elements=string | The reference names of reverse_proxy/locations associated with the object  Returned: success |
| **name**  string | The name of the object  Returned: success |
| **port**  integer | The port of the frontend connection  Returned: success |
| **preservehost**  boolean | Preserve host header  Returned: success |
| **profile**  string | The associated reverse_proxy/profile  Returned: success |
| **status**  boolean | Whether the frontend object is active or not  Returned: success |
| **type**  string | The connection type  Returned: success |
| **xheaders**  boolean | The xheaders state  Returned: success |

### Authors

- Johannes Brunswicker (@MatrixCrawler)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
