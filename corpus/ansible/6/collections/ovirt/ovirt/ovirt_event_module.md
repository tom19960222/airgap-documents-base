---
collection: ansible
version: "6"
title: "ovirt.ovirt.ovirt_event module – Create or delete an event in oVirt/RHV"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ovirt/ovirt/ovirt_event_module.html
fetched_at: 2026-07-28T00:17:28+00:00
---
# ovirt.ovirt.ovirt_event module – Create or delete an event in oVirt/RHV

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
> see [Requirements](ovirt_event_module.md#ansible-collections-ovirt-ovirt-ovirt-event-module-requirements) for details.
>
> To use it in a playbook, specify: `ovirt.ovirt.ovirt_event`.

New in ovirt.ovirt 1.0.0

- [Synopsis](ovirt_event_module.md#synopsis)
- [Requirements](ovirt_event_module.md#requirements)
- [Parameters](ovirt_event_module.md#parameters)
- [Notes](ovirt_event_module.md#notes)
- [Examples](ovirt_event_module.md#examples)
- [Return Values](ovirt_event_module.md#return-values)

## [Synopsis](ovirt_event_module.md#id1)

- This module can be used to create or delete an event in oVirt/RHV.

## [Requirements](ovirt_event_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- ovirt-engine-sdk-python >= 4.4.0

## [Parameters](ovirt_event_module.md#id3)

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
| **cluster**  string | The id of the cluster associated with this event. |
| **correlation_id**  string | The event correlation identifier. If not specified, the ‘correlation-id’ in the connection header will be used. If neither are available, it is not set. |
| **custom_id**  integer | Custom ID for the event. This ID must be unique for each event.  Required when state is present. |
| **data_center**  string | The id of the data center associated with this event. |
| **description**  string | Message for the event.  Required when state is present. |
| **fetch_nested**  boolean | If *True* the module will fetch additional data from the API.  It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying `nested_attributes`.  Choices:   - `false` ← (default) - `true` |
| **host**  string | The id of the host associated with this event. |
| **id**  string | The event ID in the oVirt/RHV audit_log table. This ID is not the same as custom_id and is only used when state is absent.  Required when state is absent. |
| **nested_attributes**  list / elements=string | Specifies list of the attributes which should be fetched from the API.  This parameter apply only when `fetch_nested` is *true*. |
| **origin**  string | Originator of the event.  Required when state is present. |
| **poll_interval**  integer | Number of the seconds the module waits until another poll request on entity status is sent.  Default: `3` |
| **severity**  string | Severity of the event.  Required when state is present.  Choices:   - `"error"` - `"normal"` ← (default) - `"warning"` |
| **state**  string | Should the event be present/absent.  The `wait` option must be set to false when state is absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **storage_domain**  string | The id of the storage domain associated with this event. |
| **template**  string | The id of the template associated with this event. |
| **timeout**  integer | The amount of time in seconds the module should wait for the instance to get into desired state.  Default: `180` |
| **user**  string | The id of the user associated with this event. |
| **vm**  string | The id of the VM associated with this event. |
| **wait**  boolean | `yes` if the module should wait for the entity to get into desired state.  Choices:   - `false` - `true` ← (default) |

## [Notes](ovirt_event_module.md#id4)

> **Note:**
>
> - In order to use this module you have to install oVirt Python SDK. To ensure it’s installed with correct version you can create the following task: *pip: name=ovirt-engine-sdk-python version=4.4.0*

## [Examples](ovirt_event_module.md#id5)

```yaml+jinja
# Examples don't contain the auth parameter for simplicity,
# look at the ovirt_auth module to see how to reuse authentication.

- name: Create an event
  ovirt.ovirt.ovirt_event:
    state: present
    description: "The file system /home on host xyz is almost full!"
    origin: "mymonitor"
    custom_id: 123456789
    severity: warning

- name: Create an event and link it to a specific object
  ovirt.ovirt.ovirt_event:
    state: present
    description: "The file system /home is almost full!"
    origin: "mymonitor"
    custom_id: 123456789
    severity: warning
    vm: "c79db183-46ef-44d1-95f9-1a368c516c19"

- name: Remove an event
  ovirt.ovirt.ovirt_event:
    state: absent
    id: 123456789
    wait: false
```

## [Return Values](ovirt_event_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **event**  dictionary | Dictionary of all the Event attributes. All event attributes can be found at the following url: <http://ovirt.github.io/ovirt-engine-api-model/master/#types/event>  Returned: On success. |
| **id**  string | ID of the event that was created.  Returned: On success. |

### Authors

- Chris Keller (@nasx)

### Collection links

[Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
[Homepage](https://www.ovirt.org/)
[Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
