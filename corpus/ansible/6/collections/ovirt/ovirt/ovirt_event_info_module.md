---
collection: ansible
version: "6"
title: "ovirt.ovirt.ovirt_event_info module – This module can be used to retrieve information about one or more oVirt/RHV events"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ovirt/ovirt/ovirt_event_info_module.html
fetched_at: 2026-07-28T00:17:29+00:00
---
# ovirt.ovirt.ovirt_event_info module – This module can be used to retrieve information about one or more oVirt/RHV events

> **Note:**
>
> This module is part of the [ovirt.ovirt collection](https://galaxy.ansible.com/ovirt/ovirt) (version 2.4.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ovirt.ovirt`.
> You need further requirements to be able to use this module,
> see [Requirements](ovirt_event_info_module.md#ansible-collections-ovirt-ovirt-ovirt-event-info-module-requirements) for details.
>
> To use it in a playbook, specify: `ovirt.ovirt.ovirt_event_info`.

New in ovirt.ovirt 1.0.0

- [Synopsis](ovirt_event_info_module.md#synopsis)
- [Requirements](ovirt_event_info_module.md#requirements)
- [Parameters](ovirt_event_info_module.md#parameters)
- [Notes](ovirt_event_info_module.md#notes)
- [Examples](ovirt_event_info_module.md#examples)
- [Return Values](ovirt_event_info_module.md#return-values)

## [Synopsis](ovirt_event_info_module.md#id1)

- Retrieve information about one or more oVirt/RHV events.
- This module was called `ovirt_event_facts` before Ansible 2.9, returning `ansible_facts`. Note that the [ovirt.ovirt.ovirt_event_info](ovirt_event_info_module.md#ansible-collections-ovirt-ovirt-ovirt-event-info-module) module no longer returns `ansible_facts`!

## [Requirements](ovirt_event_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- ovirt-engine-sdk-python >= 4.4.0

## [Parameters](ovirt_event_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth**  dictionary / required | Dictionary with values needed to create HTTP/HTTPS connection to oVirt: |
| **ca_file**  string | A PEM file containing the trusted CA certificates.  The certificate presented by the server will be verified using these CA certificates.  If `ca_file` parameter is not set, system wide CA certificate store is used.  Default value is set by `OVIRT_CAFILE` environment variable. |
| **compress**  boolean | Flag indicating if compression is used for connection.  Choices:   - `false` - `true` ← (default) |
| **headers**  dictionary | Dictionary of HTTP headers to be added to each API call. |
| **hostname**  string | A string containing the hostname of the server, usually something like `*server.example.com*`.  Default value is set by `OVIRT_HOSTNAME` environment variable.  Either `url` or `hostname` is required. |
| **insecure**  boolean | A boolean flag that indicates if the server TLS certificate and host name should be checked.  Choices:   - `false` ← (default) - `true` |
| **kerberos**  boolean | A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.  Choices:   - `false` - `true` |
| **password**  string | The password of the user.  Default value is set by `OVIRT_PASSWORD` environment variable. |
| **timeout**  integer | Number of seconds to wait for response. |
| **token**  string | Token to be used instead of login with username/password.  Default value is set by `OVIRT_TOKEN` environment variable. |
| **url**  string | A string containing the API URL of the server, usually something like `*https://server.example.com/ovirt-engine/api*`.  Default value is set by `OVIRT_URL` environment variable.  Either `url` or `hostname` is required. |
| **username**  string | The name of the user, something like *admin@internal*.  Default value is set by `OVIRT_USERNAME` environment variable. |
| **case_sensitive**  boolean | Indicates if the search performed using the search parameter should be performed taking case into account. The default value is true, which means that case is taken into account. If you want to search ignoring case set it to false.  Choices:   - `false` - `true` ← (default) |
| **fetch_nested**  boolean | If *yes* the module will fetch additional data from the API.  It will fetch only IDs of nested entity. It doesn’t fetch multiple levels of nested attributes. Only the attributes of the current entity. User can configure to fetch other attributes of the nested entities by specifying `nested_attributes`.  This parameter is deprecated and replaced by `follow`.  Choices:   - `false` ← (default) - `true` |
| **follow**  aliases: follows  list / elements=string  added in ovirt.ovirt 1.5.0 | List of linked entities, which should be fetched along with the main entity.  This parameter replaces usage of `fetch_nested` and `nested_attributes`.  All follow parameters can be found at following url: <https://ovirt.github.io/ovirt-engine-api-model/master/#types/event/links_summary> |
| **from_**  integer | Indicates the event index after which events should be returned. The indexes of events are strictly increasing, so when this parameter is used only the events with greater indexes will be returned. |
| **headers**  string | Additional HTTP headers. |
| **max**  integer | Sets the maximum number of events to return. If not specified all the events are returned. |
| **nested_attributes**  list / elements=string | Specifies list of the attributes which should be fetched from the API.  This parameter apply only when `fetch_nested` is *true*.  This parameter is deprecated and replaced by `follow`. |
| **query**  string | Additional URL query parameters. |
| **search**  string | Search term which is accepted by the oVirt/RHV API.  For example to search for events of severity alert use the following pattern: severity=alert |
| **wait**  boolean | If True wait for the response.  Choices:   - `false` - `true` ← (default) |

## [Notes](ovirt_event_info_module.md#id4)

> **Note:**
>
> - In order to use this module you have to install oVirt Python SDK. To ensure it’s installed with correct version you can create the following task: pip: name=ovirt-engine-sdk-python version=4.4.0

## [Examples](ovirt_event_info_module.md#id5)

```yaml+jinja
# Examples don't contain the auth parameter for simplicity,
# look at the ovirt_auth module to see how to reuse authentication.

- name: Return all events
  ovirt.ovirt.ovirt_event_info:
  register: result

- name: Return the last 10 events
  ovirt.ovirt.ovirt_event_info:
    max: 10
  register: result

- name: Return all events of type alert
  ovirt.ovirt.ovirt_event_info:
    search: "severity=alert"
  register: result
- ansible.builtin.debug:
    msg: "{{ result.ovirt_events }}"
```

## [Return Values](ovirt_event_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ovirt_events**  list / elements=string | List of dictionaries describing the events. Event attributes are mapped to dictionary keys. All event attributes can be found at the following url: <http://ovirt.github.io/ovirt-engine-api-model/master/#types/event>  Returned: On success.” |

### Authors

- Chris Keller (@nasx)

### Collection links

[Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
[Homepage](https://www.ovirt.org/)
[Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
