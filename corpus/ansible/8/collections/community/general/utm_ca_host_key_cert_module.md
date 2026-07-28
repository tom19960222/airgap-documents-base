---
collection: ansible
version: "8"
title: "community.general.utm_ca_host_key_cert module – Create, update or destroy ca host_key_cert entry in Sophos UTM"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/utm_ca_host_key_cert_module.html
fetched_at: 2026-07-28T01:51:07+00:00
---
# community.general.utm_ca_host_key_cert module – Create, update or destroy ca host_key_cert entry in Sophos UTM

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
> To use it in a playbook, specify: `community.general.utm_ca_host_key_cert`.

- [Synopsis](utm_ca_host_key_cert_module.md#synopsis)
- [Parameters](utm_ca_host_key_cert_module.md#parameters)
- [Attributes](utm_ca_host_key_cert_module.md#attributes)
- [Examples](utm_ca_host_key_cert_module.md#examples)
- [Return Values](utm_ca_host_key_cert_module.md#return-values)

## [Synopsis](utm_ca_host_key_cert_module.md#id1)

- Create, update or destroy a ca host_key_cert entry in SOPHOS UTM.
- This module needs to have the REST Ability of the UTM to be activated.

Aliases: web_infrastructure.sophos_utm.utm_ca_host_key_cert

## [Parameters](utm_ca_host_key_cert_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **ca**  string / required | A reference to an existing utm_ca_signing_ca or utm_ca_verification_ca object. |
| **certificate**  string / required | The certificate in PEM format. |
| **comment**  string | Optional comment string. |
| **encrypted**  boolean | Optionally enable encryption.  **Choices:**   - `false` ← (default) - `true` |
| **headers**  dictionary | A dictionary of additional headers to be sent to POST and PUT requests.  Is needed for some modules  **Default:** `{}` |
| **key**  string | Optional private key in PEM format. |
| **meta**  string / required | A reference to an existing utm_ca_meta_x509 object. |
| **name**  string / required | The name of the object. Will be used to identify the entry. |
| **state**  string | The desired state of the object.  `present` will create or update an object  `absent` will delete an object if it was present  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **utm_host**  string / required | The REST Endpoint of the Sophos UTM. |
| **utm_port**  integer | The port of the REST interface.  **Default:** `4444` |
| **utm_protocol**  string | The protocol of the REST Endpoint.  **Choices:**   - `"http"` - `"https"` ← (default) |
| **utm_token**  string / required | The token used to identify at the REST-API. See <https://www.sophos.com/en-us/medialibrary/PDFs/documentation/UTMonAWS/Sophos-UTM-RESTful-API.pdf?la=en>, Chapter 2.4.2. |
| **validate_certs**  boolean | Whether the REST interface’s ssl certificate should be verified or not.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](utm_ca_host_key_cert_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](utm_ca_host_key_cert_module.md#id4)

```yaml+jinja
- name: Create a ca_host_key_cert entry
  community.general.utm_ca_host_key_cert:
    utm_host: sophos.host.name
    utm_token: abcdefghijklmno1234
    name: TestHostKeyCertEntry
    ca: REF_ca/signing_ca_OBJECT_STRING
    meta: REF_ca/meta_x509_OBJECT_STRING
    certificate: |
      --- BEGIN CERTIFICATE ---
      . . .
       . . .
      . . .
      --- END CERTIFICATE ---
    state: present

- name: Remove a ca_host_key_cert entry
  community.general.utm_ca_host_key_cert:
    utm_host: sophos.host.name
    utm_token: abcdefghijklmno1234
    name: TestHostKeyCertEntry
    state: absent

- name: Read a ca_host_key_cert entry
  community.general.utm_ca_host_key_cert:
    utm_host: sophos.host.name
    utm_token: abcdefghijklmno1234
    name: TestHostKeyCertEntry
    state: info
```

## [Return Values](utm_ca_host_key_cert_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  complex | The utm object that was created  **Returned:** success |
| **_locked**  boolean | Whether or not the object is currently locked  **Returned:** success |
| **_ref**  string | The reference name of the object  **Returned:** success |
| **_type**  string | The type of the object  **Returned:** success |
| **ca**  string | A reference to an existing utm_ca_signing_ca or utm_ca_verification_ca object.  **Returned:** success |
| **certificate**  string | The certificate in PEM format  **Returned:** success |
| **comment**  string | Comment string (may be empty string)  **Returned:** success |
| **encrypted**  boolean | If encryption is enabled  **Returned:** success |
| **key**  string | Private key in PEM format (may be empty string)  **Returned:** success |
| **meta**  string | A reference to an existing utm_ca_meta_x509 object.  **Returned:** success |
| **name**  string | The name of the object  **Returned:** success |

### Authors

- Stephan Schwarz (@stearz)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
