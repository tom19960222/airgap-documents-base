---
collection: ansible
version: "6"
title: "community.general.utm_proxy_exception module – Create, update or destroy reverse_proxy exception entry in Sophos UTM"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/utm_proxy_exception_module.html
fetched_at: 2026-07-27T17:13:48+00:00
---
# community.general.utm_proxy_exception module – Create, update or destroy reverse_proxy exception entry in Sophos UTM

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
> To use it in a playbook, specify: `community.general.utm_proxy_exception`.

- [Synopsis](utm_proxy_exception_module.md#synopsis)
- [Parameters](utm_proxy_exception_module.md#parameters)
- [Examples](utm_proxy_exception_module.md#examples)
- [Return Values](utm_proxy_exception_module.md#return-values)

## [Synopsis](utm_proxy_exception_module.md#id1)

- Create, update or destroy a reverse_proxy exception entry in SOPHOS UTM.
- This module needs to have the REST Ability of the UTM to be activated.

## [Parameters](utm_proxy_exception_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **headers**  dictionary | A dictionary of additional headers to be sent to POST and PUT requests.  Is needed for some modules  Default: `{}` |
| **name**  string / required | The name of the object. Will be used to identify the entry |
| **op**  string | The operand to be used with the entries of the path parameter  Choices:   - `"AND"` ← (default) - `"OR"` |
| **path**  list / elements=string | The paths the exception in the reverse proxy is defined for  Default: `[]` |
| **skip_custom_threats_filters**  list / elements=string | A list of threats to be skipped  Default: `[]` |
| **skip_threats_filter_categories**  list / elements=string | Define which categories of threats are skipped  Default: `[]` |
| **skipav**  boolean | Skip the Antivirus Scanning  Choices:   - `false` ← (default) - `true` |
| **skipbadclients**  boolean | Block clients with bad reputation  Choices:   - `false` ← (default) - `true` |
| **skipcookie**  boolean | Skip the Cookie Signing check  Choices:   - `false` ← (default) - `true` |
| **skipform**  boolean | Enable form hardening  Choices:   - `false` ← (default) - `true` |
| **skipform_missingtoken**  boolean | Enable form hardening with missing tokens  Choices:   - `false` ← (default) - `true` |
| **skiphtmlrewrite**  boolean | Protection against SQL  Choices:   - `false` ← (default) - `true` |
| **skiptft**  boolean | Enable true file type control  Choices:   - `false` ← (default) - `true` |
| **skipurl**  boolean | Enable static URL hardening  Choices:   - `false` ← (default) - `true` |
| **source**  list / elements=string | Define which categories of threats are skipped  Default: `[]` |
| **state**  string | The desired state of the object.  `present` will create or update an object  `absent` will delete an object if it was present  Choices:   - `"absent"` - `"present"` ← (default) |
| **status**  boolean | Status of the exception rule set  Choices:   - `false` - `true` ← (default) |
| **utm_host**  string / required | The REST Endpoint of the Sophos UTM. |
| **utm_port**  integer | The port of the REST interface.  Default: `4444` |
| **utm_protocol**  string | The protocol of the REST Endpoint.  Choices:   - `"http"` - `"https"` ← (default) |
| **utm_token**  string / required | The token used to identify at the REST-API. See <https://www.sophos.com/en-us/medialibrary/PDFs/documentation/UTMonAWS/Sophos-UTM-RESTful-API.pdf?la%3Den>, Chapter 2.4.2. |
| **validate_certs**  boolean | Whether the REST interface’s ssl certificate should be verified or not.  Choices:   - `false` - `true` ← (default) |

## [Examples](utm_proxy_exception_module.md#id3)

```yaml+jinja
- name: Create UTM proxy_exception
  community.general.utm_proxy_exception:
    utm_host: sophos.host.name
    utm_token: abcdefghijklmno1234
    name: TestExceptionEntry
    backend: REF_OBJECT_STRING
    state: present

- name: Remove UTM proxy_exception
  community.general.utm_proxy_exception:
    utm_host: sophos.host.name
    utm_token: abcdefghijklmno1234
    name: TestExceptionEntry
    state: absent
```

## [Return Values](utm_proxy_exception_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  complex | The utm object that was created  Returned: success |
| **_locked**  boolean | Whether or not the object is currently locked  Returned: success |
| **_ref**  string | The reference name of the object  Returned: success |
| **_type**  string | The type of the object  Returned: success |
| **comment**  string | The optional comment string  Returned: success |
| **name**  string | The name of the object  Returned: success |
| **op**  string | The operand to be used with the entries of the path parameter  Returned: success |
| **path**  list / elements=string | The paths the exception in the reverse proxy is defined for  Returned: success |
| **skip_custom_threats_filters**  list / elements=string | A list of threats to be skipped  Returned: success |
| **skip_threats_filter_categories**  list / elements=string | Define which categories of threats are skipped  Returned: success |
| **skipav**  boolean | Skip the Antivirus Scanning  Returned: success |
| **skipbadclients**  boolean | Block clients with bad reputation  Returned: success |
| **skipcookie**  boolean | Skip the Cookie Signing check  Returned: success |
| **skipform**  boolean | Enable form hardening  Returned: success |
| **skipform_missingtoken**  boolean | Enable form hardening with missing tokens  Returned: success |
| **skiphtmlrewrite**  boolean | Protection against SQL  Returned: success |
| **skiptft**  boolean | Enable true file type control  Returned: success |
| **skipurl**  boolean | Enable static URL hardening  Returned: success |
| **source**  list / elements=string | Define which categories of threats are skipped  Returned: success |

### Authors

- Sebastian Schenzel (@RickS-C137)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
